# Repository Information
Name: mikrotik_dan_laravel

# Directory Structure
Directory structure:
└── github_repos/mikrotik_dan_laravel/
    ├── .editorconfig
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
    │   │       ├── pack-6ab5680b5909eef7f0369a4ffa5ba1c0c7d0161f.idx
    │   │       └── pack-6ab5680b5909eef7f0369a4ffa5ba1c0c7d0161f.pack
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
    │   │   └── Kernel.php
    │   ├── Exceptions/
    │   │   └── Handler.php
    │   ├── Http/
    │   │   ├── Controllers/
    │   │   │   ├── Auth/
    │   │   │   │   ├── ForgotPasswordController.php
    │   │   │   │   ├── LoginController.php
    │   │   │   │   ├── RegisterController.php
    │   │   │   │   ├── ResetPasswordController.php
    │   │   │   │   └── VerificationController.php
    │   │   │   ├── BelajarController.php
    │   │   │   ├── Controller.php
    │   │   │   └── RouterController.php
    │   │   ├── Kernel.php
    │   │   └── Middleware/
    │   │       ├── Authenticate.php
    │   │       ├── CheckForMaintenanceMode.php
    │   │       ├── EncryptCookies.php
    │   │       ├── RedirectIfAuthenticated.php
    │   │       ├── TrimStrings.php
    │   │       ├── TrustProxies.php
    │   │       └── VerifyCsrfToken.php
    │   ├── Providers/
    │   │   ├── AppServiceProvider.php
    │   │   ├── AuthServiceProvider.php
    │   │   ├── BroadcastServiceProvider.php
    │   │   ├── EventServiceProvider.php
    │   │   └── RouteServiceProvider.php
    │   └── User.php
    ├── artisan
    ├── bootstrap/
    │   ├── app.php
    │   └── cache/
    │       └── .gitignore
    ├── composer.json
    ├── composer.lock
    ├── config/
    │   ├── app.php
    │   ├── auth.php
    │   ├── broadcasting.php
    │   ├── cache.php
    │   ├── database.php
    │   ├── filesystems.php
    │   ├── hashing.php
    │   ├── logging.php
    │   ├── mail.php
    │   ├── queue.php
    │   ├── services.php
    │   ├── session.php
    │   └── view.php
    ├── database/
    │   ├── .gitignore
    │   ├── factories/
    │   │   └── UserFactory.php
    │   ├── migrations/
    │   │   ├── 2014_10_12_000000_create_users_table.php
    │   │   └── 2014_10_12_100000_create_password_resets_table.php
    │   └── seeds/
    │       └── DatabaseSeeder.php
    ├── package.json
    ├── phpunit.xml
    ├── public/
    │   ├── .htaccess
    │   ├── css/
    │   │   └── app.css
    │   ├── index.php
    │   ├── js/
    │   │   └── app.js
    │   ├── robots.txt
    │   ├── svg/
    │   └── web.config
    ├── readme.md
    ├── resources/
    │   ├── js/
    │   │   ├── app.js
    │   │   ├── bootstrap.js
    │   │   └── components/
    │   │       └── ExampleComponent.vue
    │   ├── lang/
    │   │   └── en/
    │   │       ├── auth.php
    │   │       ├── pagination.php
    │   │       ├── passwords.php
    │   │       └── validation.php
    │   ├── sass/
    │   │   ├── app.scss
    │   │   └── _variables.scss
    │   └── views/
    │       └── welcome.blade.php
    ├── routes/
    │   ├── api.php
    │   ├── channels.php
    │   ├── console.php
    │   └── web.php
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
    │   │   ├── testing/
    │   │   │   └── .gitignore
    │   │   └── views/
    │   │       └── .gitignore
    │   └── logs/
    │       └── .gitignore
    ├── tests/
    │   ├── CreatesApplication.php
    │   ├── Feature/
    │   │   └── ExampleTest.php
    │   ├── TestCase.php
    │   └── Unit/
    │       └── ExampleTest.php
    └── webpack.mix.js


# Content
File: /.editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[*.yml]
indent_size = 2


File: /.env.example
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=secret

BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_DRIVER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/sikuning/mikrotik_dan_laravel.git
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
0000000000000000000000000000000000000000 4eb409d2c95be2b877d40ab7ff0326c176096634 vivek-dodia <vivek.dodia@icloud.com> 1738606442 -0500	clone: from https://github.com/sikuning/mikrotik_dan_laravel.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 4eb409d2c95be2b877d40ab7ff0326c176096634 vivek-dodia <vivek.dodia@icloud.com> 1738606442 -0500	clone: from https://github.com/sikuning/mikrotik_dan_laravel.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 4eb409d2c95be2b877d40ab7ff0326c176096634 vivek-dodia <vivek.dodia@icloud.com> 1738606442 -0500	clone: from https://github.com/sikuning/mikrotik_dan_laravel.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4eb409d2c95be2b877d40ab7ff0326c176096634 refs/remotes/origin/master


File: /.git\refs\heads\master
4eb409d2c95be2b877d40ab7ff0326c176096634


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
* text=auto
*.css linguist-vendored
*.scss linguist-vendored
*.js linguist-vendored
CHANGELOG.md export-ignore


File: /.gitignore
/node_modules
/public/hot
/public/storage
/storage/*.key
/vendor
/.idea
/.vscode
/.vagrant
Homestead.json
Homestead.yaml
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
        //
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

    /**
     * Register the commands for the application.
     *
     * @return void
     */
    protected function commands()
    {
        $this->load(__DIR__.'/Commands');

        require base_path('routes/console.php');
    }
}


File: /app\Exceptions\Handler.php
<?php

namespace App\Exceptions;

use Exception;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;

class Handler extends ExceptionHandler
{
    /**
     * A list of the exception types that are not reported.
     *
     * @var array
     */
    protected $dontReport = [
        //
    ];

    /**
     * A list of the inputs that are never flashed for validation exceptions.
     *
     * @var array
     */
    protected $dontFlash = [
        'password',
        'password_confirmation',
    ];

    /**
     * Report or log an exception.
     *
     * @param  \Exception  $exception
     * @return void
     */
    public function report(Exception $exception)
    {
        parent::report($exception);
    }

    /**
     * Render an exception into an HTTP response.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Exception  $exception
     * @return \Illuminate\Http\Response
     */
    public function render($request, Exception $exception)
    {
        return parent::render($request, $exception);
    }
}


File: /app\Http\Controllers\Auth\ForgotPasswordController.php
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\SendsPasswordResetEmails;

class ForgotPasswordController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Password Reset Controller
    |--------------------------------------------------------------------------
    |
    | This controller is responsible for handling password reset emails and
    | includes a trait which assists in sending these notifications from
    | your application to your users. Feel free to explore this trait.
    |
    */

    use SendsPasswordResetEmails;

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest');
    }
}


File: /app\Http\Controllers\Auth\LoginController.php
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\AuthenticatesUsers;

class LoginController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles authenticating users for the application and
    | redirecting them to your home screen. The controller uses a trait
    | to conveniently provide its functionality to your applications.
    |
    */

    use AuthenticatesUsers;

    /**
     * Where to redirect users after login.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest')->except('logout');
    }
}


File: /app\Http\Controllers\Auth\RegisterController.php
<?php

namespace App\Http\Controllers\Auth;

use App\User;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use Illuminate\Foundation\Auth\RegistersUsers;

class RegisterController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Register Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles the registration of new users as well as their
    | validation and creation. By default this controller uses a trait to
    | provide this functionality without requiring any additional code.
    |
    */

    use RegistersUsers;

    /**
     * Where to redirect users after registration.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest');
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
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:6|confirmed',
        ]);
    }

    /**
     * Create a new user instance after a valid registration.
     *
     * @param  array  $data
     * @return \App\User
     */
    protected function create(array $data)
    {
        return User::create([
            'name' => $data['name'],
            'email' => $data['email'],
            'password' => Hash::make($data['password']),
        ]);
    }
}


File: /app\Http\Controllers\Auth\ResetPasswordController.php
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\ResetsPasswords;

class ResetPasswordController extends Controller
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
     * Where to redirect users after resetting their password.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest');
    }
}


File: /app\Http\Controllers\Auth\VerificationController.php
<?php

namespace App\Http\Controllers\Auth;

use Illuminate\Http\Request;
use Illuminate\Routing\Controller;
use Illuminate\Foundation\Auth\VerifiesEmails;

class VerificationController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Email Verification Controller
    |--------------------------------------------------------------------------
    |
    | This controller is responsible for handling email verification for any
    | user that recently registered with the application. Emails may also
    | be resent if the user did not receive the original email message.
    |
    */

    use VerifiesEmails;

    /**
     * Where to redirect users after verification.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
        $this->middleware('signed')->only('verify');
        $this->middleware('throttle:6,1')->only('verify', 'resend');
    }
}


File: /app\Http\Controllers\BelajarController.php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Mikrokit;
use PEAR2\Net\RouterOS;
use Response;

class BelajarController extends Controller
{
    private $client;
    public function __construct()
    {
        $this->client = new RouterOS\Client('<host>', '<user>', '<password>');
    }
    public function tes_koneksi()
    {
       // $conn = Mikrokit::connect(['192.168.88.1', 'admin', 'pingwatchsdog']);
       
    //dd($client);
    $responses =$this->client->sendSync(new RouterOS\Request('/ip/arp/print'));
  echo "<a href='/ping'> Klik Untuk Ping 192.168.1.1</a>";
    echo 'Ip Address setiap Interface :<br>';
foreach ($responses as $response) {
  echo'IP'.$response->getProperty('address');
 echo 'MAC: ', $response->getProperty('mac-address').'<br>';

    }
   echo 'Data Logs : <br>';
    $util = new RouterOS\Util($this->client);
    foreach ($util->setMenu('/log')->getAll() as $entry) {

        echo $entry('time') . ' ' . $entry('topics') . ' ' . $entry('message') . "<br>";
    }
}
public function ping()
{
    $pingRequest = new RouterOS\Request('/ping count=3');
    $results = $this->client->sendSync($pingRequest->setArgument('address','192.168.1.1'));
  
    foreach ($results as $result) {
        //Add whatever you want displayed in this section.
        echo '<li>Host'.$result('host').' Size'.$result('size').'</li>';
    } 
}
}


File: /app\Http\Controllers\Controller.php
<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
}


File: /app\Http\Controllers\RouterController.php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RouterController extends Controller
{
    public function __construct()
    {
       
    }
    public function tes_koneksi(Type $var = null)
    {
        $conn = Mikrokit::connect(['192.168.88.1', 'admin', 'pingwatchsdog']);
        if($conn->isConnected()) {
        dd('terkoneksi ');
        }

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
        \App\Http\Middleware\CheckForMaintenanceMode::class,
        \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
        \App\Http\Middleware\TrimStrings::class,
        \Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull::class,
        \App\Http\Middleware\TrustProxies::class,
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
            // \Illuminate\Session\Middleware\AuthenticateSession::class,
            \Illuminate\View\Middleware\ShareErrorsFromSession::class,
            \App\Http\Middleware\VerifyCsrfToken::class,
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
        ],

        'api' => [
            'throttle:60,1',
            'bindings',
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
        'bindings' => \Illuminate\Routing\Middleware\SubstituteBindings::class,
        'cache.headers' => \Illuminate\Http\Middleware\SetCacheHeaders::class,
        'can' => \Illuminate\Auth\Middleware\Authorize::class,
        'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
        'signed' => \Illuminate\Routing\Middleware\ValidateSignature::class,
        'throttle' => \Illuminate\Routing\Middleware\ThrottleRequests::class,
        'verified' => \Illuminate\Auth\Middleware\EnsureEmailIsVerified::class,
    ];
}


File: /app\Http\Middleware\Authenticate.php
<?php

namespace App\Http\Middleware;

use Illuminate\Auth\Middleware\Authenticate as Middleware;

class Authenticate extends Middleware
{
    /**
     * Get the path the user should be redirected to when they are not authenticated.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return string
     */
    protected function redirectTo($request)
    {
        return route('login');
    }
}


File: /app\Http\Middleware\CheckForMaintenanceMode.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode as Middleware;

class CheckForMaintenanceMode extends Middleware
{
    /**
     * The URIs that should be reachable while maintenance mode is enabled.
     *
     * @var array
     */
    protected $except = [
        //
    ];
}


File: /app\Http\Middleware\EncryptCookies.php
<?php

namespace App\Http\Middleware;

use Illuminate\Cookie\Middleware\EncryptCookies as Middleware;

class EncryptCookies extends Middleware
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
            return redirect('/home');
        }

        return $next($request);
    }
}


File: /app\Http\Middleware\TrimStrings.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\TrimStrings as Middleware;

class TrimStrings extends Middleware
{
    /**
     * The names of the attributes that should not be trimmed.
     *
     * @var array
     */
    protected $except = [
        'password',
        'password_confirmation',
    ];
}


File: /app\Http\Middleware\TrustProxies.php
<?php

namespace App\Http\Middleware;

use Illuminate\Http\Request;
use Fideloper\Proxy\TrustProxies as Middleware;

class TrustProxies extends Middleware
{
    /**
     * The trusted proxies for this application.
     *
     * @var array
     */
    protected $proxies;

    /**
     * The headers that should be used to detect proxies.
     *
     * @var int
     */
    protected $headers = Request::HEADER_X_FORWARDED_ALL;
}


File: /app\Http\Middleware\VerifyCsrfToken.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
{
    /**
     * Indicates whether the XSRF-TOKEN cookie should be set on the response.
     *
     * @var bool
     */
    protected $addHttpCookie = true;

    /**
     * The URIs that should be excluded from CSRF verification.
     *
     * @var array
     */
    protected $except = [
        //
    ];
}


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

use Illuminate\Support\Facades\Gate;
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
     * Register any authentication / authorization services.
     *
     * @return void
     */
    public function boot()
    {
        $this->registerPolicies();

        //
    }
}


File: /app\Providers\BroadcastServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Broadcast;

class BroadcastServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        Broadcast::routes();

        require base_path('routes/channels.php');
    }
}


File: /app\Providers\EventServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\Facades\Event;
use Illuminate\Auth\Events\Registered;
use Illuminate\Auth\Listeners\SendEmailVerificationNotification;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;

class EventServiceProvider extends ServiceProvider
{
    /**
     * The event listener mappings for the application.
     *
     * @var array
     */
    protected $listen = [
        Registered::class => [
            SendEmailVerificationNotification::class,
        ],
    ];

    /**
     * Register any events for your application.
     *
     * @return void
     */
    public function boot()
    {
        parent::boot();

        //
    }
}


File: /app\Providers\RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\Facades\Route;
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
     * @return void
     */
    public function boot()
    {
        //

        parent::boot();
    }

    /**
     * Define the routes for the application.
     *
     * @return void
     */
    public function map()
    {
        $this->mapApiRoutes();

        $this->mapWebRoutes();

        //
    }

    /**
     * Define the "web" routes for the application.
     *
     * These routes all receive session state, CSRF protection, etc.
     *
     * @return void
     */
    protected function mapWebRoutes()
    {
        Route::middleware('web')
             ->namespace($this->namespace)
             ->group(base_path('routes/web.php'));
    }

    /**
     * Define the "api" routes for the application.
     *
     * These routes are typically stateless.
     *
     * @return void
     */
    protected function mapApiRoutes()
    {
        Route::prefix('api')
             ->middleware('api')
             ->namespace($this->namespace)
             ->group(base_path('routes/api.php'));
    }
}


File: /app\User.php
<?php

namespace App;

use Illuminate\Notifications\Notifiable;
use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable
{
    use Notifiable;

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

define('LARAVEL_START', microtime(true));

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

require __DIR__.'/vendor/autoload.php';

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
| Once Artisan has finished running, we will fire off the shutdown events
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
        "php": "^7.1.3",
        "fideloper/proxy": "^4.0",
        "jjsquady/mikrotikapi": "^0.3.6",
        "laravel/framework": "5.7.*",
        "laravel/tinker": "^1.0",
        "pear2/cache_shm": "*@alpha",
        "pear2/net_routeros": "*@beta"
    },
    "require-dev": {
        "beyondcode/laravel-dump-server": "^1.0",
        "filp/whoops": "^2.0",
        "fzaninotto/faker": "^1.4",
        "mockery/mockery": "^1.0",
        "nunomaduro/collision": "^2.0",
        "phpunit/phpunit": "^7.0"
    },
    "autoload": {
        "classmap": [
            "database/seeds",
            "database/factories"
        ],
        "psr-4": {
            "App\\": "app/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "extra": {
        "laravel": {
            "dont-discover": [
            ]
        }
    },
    "scripts": {
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate"
        ],
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover"
        ]
    },
    "config": {
        "preferred-install": "dist",
        "sort-packages": true,
        "optimize-autoloader": true
    },
    "minimum-stability": "dev",
    "prefer-stable": true
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "b0840fe60185f60faa95b3fd1e4ad141",
    "packages": [
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
            "time": "2014-10-24T07:27:01+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "v1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "5527a48b7313d15261292c149e55e26eae771b0a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/5527a48b7313d15261292c149e55e26eae771b0a",
                "reference": "5527a48b7313d15261292c149e55e26eae771b0a",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Inflector\\": "lib/Doctrine/Common/Inflector"
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
            "time": "2018-01-09T20:05:19+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "v1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "83893c552fd2045dd78aef794c31e694c37c0b8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/83893c552fd2045dd78aef794c31e694c37c0b8c",
                "reference": "83893c552fd2045dd78aef794c31e694c37c0b8c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Lexer\\": "lib/"
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
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Base library for a lexer that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "lexer",
                "parser"
            ],
            "time": "2014-09-09T13:34:57+00:00"
        },
        {
            "name": "dragonmantank/cron-expression",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/dragonmantank/cron-expression.git",
                "reference": "92a2c3768d50e21a1f26a53cb795ce72806266c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dragonmantank/cron-expression/zipball/92a2c3768d50e21a1f26a53cb795ce72806266c5",
                "reference": "92a2c3768d50e21a1f26a53cb795ce72806266c5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~6.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Cron\\": "src/Cron/"
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
                },
                {
                    "name": "Chris Tankersley",
                    "email": "chris@ctankersley.com",
                    "homepage": "https://github.com/dragonmantank"
                }
            ],
            "description": "CRON for PHP: Calculate the next or previous run date and determine if a CRON expression is due",
            "keywords": [
                "cron",
                "schedule"
            ],
            "time": "2018-06-06T03:12:17+00:00"
        },
        {
            "name": "egulias/email-validator",
            "version": "2.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/egulias/EmailValidator.git",
                "reference": "54859fabea8b3beecbb1a282888d5c990036b9e3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/egulias/EmailValidator/zipball/54859fabea8b3beecbb1a282888d5c990036b9e3",
                "reference": "54859fabea8b3beecbb1a282888d5c990036b9e3",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "^1.0.1",
                "php": ">= 5.5"
            },
            "require-dev": {
                "dominicsayers/isemail": "dev-master",
                "phpunit/phpunit": "^4.8.35||^5.7||^6.0",
                "satooshi/php-coveralls": "^1.0.1"
            },
            "suggest": {
                "ext-intl": "PHP Internationalization Libraries are required to use the SpoofChecking validation"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Egulias\\EmailValidator\\": "EmailValidator"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Eduardo Gulias Davis"
                }
            ],
            "description": "A library for validating emails against several RFCs",
            "homepage": "https://github.com/egulias/EmailValidator",
            "keywords": [
                "email",
                "emailvalidation",
                "emailvalidator",
                "validation",
                "validator"
            ],
            "time": "2018-08-16T20:49:45+00:00"
        },
        {
            "name": "erusev/parsedown",
            "version": "1.7.1",
            "source": {
                "type": "git",
                "url": "https://github.com/erusev/parsedown.git",
                "reference": "92e9c27ba0e74b8b028b111d1b6f956a15c01fc1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/erusev/parsedown/zipball/92e9c27ba0e74b8b028b111d1b6f956a15c01fc1",
                "reference": "92e9c27ba0e74b8b028b111d1b6f956a15c01fc1",
                "shasum": ""
            },
            "require": {
                "ext-mbstring": "*",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "Parsedown": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Emanuil Rusev",
                    "email": "hello@erusev.com",
                    "homepage": "http://erusev.com"
                }
            ],
            "description": "Parser for Markdown.",
            "homepage": "http://parsedown.org",
            "keywords": [
                "markdown",
                "parser"
            ],
            "time": "2018-03-08T01:11:30+00:00"
        },
        {
            "name": "fideloper/proxy",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/fideloper/TrustedProxy.git",
                "reference": "cf8a0ca4b85659b9557e206c90110a6a4dba980a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fideloper/TrustedProxy/zipball/cf8a0ca4b85659b9557e206c90110a6a4dba980a",
                "reference": "cf8a0ca4b85659b9557e206c90110a6a4dba980a",
                "shasum": ""
            },
            "require": {
                "illuminate/contracts": "~5.0",
                "php": ">=5.4.0"
            },
            "require-dev": {
                "illuminate/http": "~5.6",
                "mockery/mockery": "~1.0",
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "Fideloper\\Proxy\\TrustedProxyServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Fideloper\\Proxy\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Chris Fidao",
                    "email": "fideloper@gmail.com"
                }
            ],
            "description": "Set trusted proxies for Laravel",
            "keywords": [
                "load balancing",
                "proxy",
                "trusted proxy"
            ],
            "time": "2018-02-07T20:20:57+00:00"
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
            "time": "2014-04-08T15:00:19+00:00"
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
            "time": "2015-04-20T18:58:01+00:00"
        },
        {
            "name": "jjsquady/mikrotikapi",
            "version": "0.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/jjsquady/mikrotikapi.git",
                "reference": "c4a4f768a73a2828eeb7fc2512157c4089d2dcf8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/jjsquady/mikrotikapi/zipball/c4a4f768a73a2828eeb7fc2512157c4089d2dcf8",
                "reference": "c4a4f768a73a2828eeb7fc2512157c4089d2dcf8",
                "shasum": ""
            },
            "require": {
                "pear2/net_routeros": "1.0.0b5",
                "pear2/net_transmitter": "1.0.0a5"
            },
            "require-dev": {
                "laravel/framework": "5.4.*",
                "orchestra/testbench": "~3.0",
                "phpunit/phpunit": "~5.7"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "jjsquady\\MikrotikApi\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jorge 'jjsquady' Junior",
                    "email": "jjsquady@gmail.com"
                }
            ],
            "description": "An Mikrotik Api Wrapper",
            "time": "2017-04-20T22:43:03+00:00"
        },
        {
            "name": "laravel/framework",
            "version": "v5.7.3",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/framework.git",
                "reference": "536a024e3ef6b93f55f4039a7f4568efa7e60aea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/framework/zipball/536a024e3ef6b93f55f4039a7f4568efa7e60aea",
                "reference": "536a024e3ef6b93f55f4039a7f4568efa7e60aea",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.1",
                "dragonmantank/cron-expression": "^2.0",
                "erusev/parsedown": "^1.7",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "league/flysystem": "^1.0.8",
                "monolog/monolog": "^1.12",
                "nesbot/carbon": "^1.26.3",
                "php": "^7.1.3",
                "psr/container": "^1.0",
                "psr/simple-cache": "^1.0",
                "ramsey/uuid": "^3.7",
                "swiftmailer/swiftmailer": "^6.0",
                "symfony/console": "^4.1",
                "symfony/debug": "^4.1",
                "symfony/finder": "^4.1",
                "symfony/http-foundation": "^4.1",
                "symfony/http-kernel": "^4.1",
                "symfony/process": "^4.1",
                "symfony/routing": "^4.1",
                "symfony/var-dumper": "^4.1",
                "tijsverkoyen/css-to-inline-styles": "^2.2.1",
                "vlucas/phpdotenv": "^2.2"
            },
            "conflict": {
                "tightenco/collect": "<5.5.33"
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
                "illuminate/filesystem": "self.version",
                "illuminate/hashing": "self.version",
                "illuminate/http": "self.version",
                "illuminate/log": "self.version",
                "illuminate/mail": "self.version",
                "illuminate/notifications": "self.version",
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
                "aws/aws-sdk-php": "^3.0",
                "doctrine/dbal": "^2.6",
                "filp/whoops": "^2.1.4",
                "league/flysystem-cached-adapter": "^1.0",
                "mockery/mockery": "^1.0",
                "moontoast/math": "^1.1",
                "orchestra/testbench-core": "3.7.*",
                "pda/pheanstalk": "^3.0",
                "phpunit/phpunit": "^7.0",
                "predis/predis": "^1.1.1",
                "symfony/css-selector": "^4.1",
                "symfony/dom-crawler": "^4.1",
                "true/punycode": "^2.1"
            },
            "suggest": {
                "aws/aws-sdk-php": "Required to use the SQS queue driver and SES mail driver (^3.0).",
                "doctrine/dbal": "Required to rename columns and drop SQLite columns (^2.6).",
                "ext-pcntl": "Required to use all features of the queue worker.",
                "ext-posix": "Required to use all features of the queue worker.",
                "fzaninotto/faker": "Required to use the eloquent factory builder (^1.4).",
                "guzzlehttp/guzzle": "Required to use the Mailgun and Mandrill mail drivers and the ping methods on schedules (^6.0).",
                "laravel/tinker": "Required to use the tinker console command (^1.0).",
                "league/flysystem-aws-s3-v3": "Required to use the Flysystem S3 driver (^1.0).",
                "league/flysystem-cached-adapter": "Required to use the Flysystem cache (^1.0).",
                "league/flysystem-rackspace": "Required to use the Flysystem Rackspace driver (^1.0).",
                "league/flysystem-sftp": "Required to use the Flysystem SFTP driver (^1.0).",
                "moontoast/math": "Required to use ordered UUIDs (^1.1).",
                "nexmo/client": "Required to use the Nexmo transport (^1.0).",
                "pda/pheanstalk": "Required to use the beanstalk queue driver (^3.0).",
                "predis/predis": "Required to use the redis cache and queue drivers (^1.0).",
                "pusher/pusher-php-server": "Required to use the Pusher broadcast driver (^3.0).",
                "symfony/css-selector": "Required to use some of the crawler integration testing tools (^4.1).",
                "symfony/dom-crawler": "Required to use most of the crawler integration testing tools (^4.1).",
                "symfony/psr-http-message-bridge": "Required to psr7 bridging features (^1.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.7-dev"
                }
            },
            "autoload": {
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
                    "email": "taylor@laravel.com"
                }
            ],
            "description": "The Laravel Framework.",
            "homepage": "https://laravel.com",
            "keywords": [
                "framework",
                "laravel"
            ],
            "time": "2018-09-11T13:42:55+00:00"
        },
        {
            "name": "laravel/tinker",
            "version": "v1.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/tinker.git",
                "reference": "e3086ee8cb1f54a39ae8dcb72d1c37d10128997d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/tinker/zipball/e3086ee8cb1f54a39ae8dcb72d1c37d10128997d",
                "reference": "e3086ee8cb1f54a39ae8dcb72d1c37d10128997d",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "~5.1",
                "illuminate/contracts": "~5.1",
                "illuminate/support": "~5.1",
                "php": ">=5.5.9",
                "psy/psysh": "0.7.*|0.8.*|0.9.*",
                "symfony/var-dumper": "~3.0|~4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0|~5.0"
            },
            "suggest": {
                "illuminate/database": "The Illuminate Database package (~5.1)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                },
                "laravel": {
                    "providers": [
                        "Laravel\\Tinker\\TinkerServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Laravel\\Tinker\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Taylor Otwell",
                    "email": "taylor@laravel.com"
                }
            ],
            "description": "Powerful REPL for the Laravel framework.",
            "keywords": [
                "REPL",
                "Tinker",
                "laravel",
                "psysh"
            ],
            "time": "2018-05-17T13:42:07+00:00"
        },
        {
            "name": "league/flysystem",
            "version": "1.0.47",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/flysystem.git",
                "reference": "a11e4a75f256bdacf99d20780ce42d3b8272975c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/flysystem/zipball/a11e4a75f256bdacf99d20780ce42d3b8272975c",
                "reference": "a11e4a75f256bdacf99d20780ce42d3b8272975c",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "php": ">=5.5.9"
            },
            "conflict": {
                "league/flysystem-sftp": "<1.0.6"
            },
            "require-dev": {
                "phpspec/phpspec": "^3.4",
                "phpunit/phpunit": "^5.7.10"
            },
            "suggest": {
                "ext-fileinfo": "Required for MimeType",
                "ext-ftp": "Allows you to use FTP server storage",
                "ext-openssl": "Allows you to use FTPS server storage",
                "league/flysystem-aws-s3-v2": "Allows you to use S3 storage with AWS SDK v2",
                "league/flysystem-aws-s3-v3": "Allows you to use S3 storage with AWS SDK v3",
                "league/flysystem-azure": "Allows you to use Windows Azure Blob storage",
                "league/flysystem-cached-adapter": "Flysystem adapter decorator for metadata caching",
                "league/flysystem-eventable-filesystem": "Allows you to use EventableFilesystem",
                "league/flysystem-rackspace": "Allows you to use Rackspace Cloud Files",
                "league/flysystem-sftp": "Allows you to use SFTP server storage via phpseclib",
                "league/flysystem-webdav": "Allows you to use WebDAV storage",
                "league/flysystem-ziparchive": "Allows you to use ZipArchive adapter",
                "spatie/flysystem-dropbox": "Allows you to use Dropbox storage",
                "srmklive/flysystem-dropbox-v2": "Allows you to use Dropbox storage for PHP 5 applications"
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
            "time": "2018-09-14T15:30:29+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "fd8c787753b3a2ad11bc60c063cff1358a32a3b4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/fd8c787753b3a2ad11bc60c063cff1358a32a3b4",
                "reference": "fd8c787753b3a2ad11bc60c063cff1358a32a3b4",
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
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "graylog2/gelf-php": "~1.0",
                "jakub-onderka/php-parallel-lint": "0.9",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpunit/phpunit": "~4.5",
                "phpunit/phpunit-mock-objects": "2.3.0",
                "ruflin/elastica": ">=0.90 <3.0",
                "sentry/sentry": "^0.13",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
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
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server",
                "sentry/sentry": "Allow sending log messages to a Sentry server"
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
            "time": "2017-06-19T01:22:40+00:00"
        },
        {
            "name": "nesbot/carbon",
            "version": "1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/briannesbitt/Carbon.git",
                "reference": "55667c1007a99e82030874b1bb14d24d07108413"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/briannesbitt/Carbon/zipball/55667c1007a99e82030874b1bb14d24d07108413",
                "reference": "55667c1007a99e82030874b1bb14d24d07108413",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9",
                "symfony/translation": "~2.6 || ~3.0 || ~4.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "~2",
                "phpunit/phpunit": "^4.8.35 || ^5.7"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "Carbon\\Laravel\\ServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "": "src/"
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
            "time": "2018-08-07T08:39:47+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "bd088dc940a418f09cda079a9b5c7c478890fb8d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/bd088dc940a418f09cda079a9b5c7c478890fb8d",
                "reference": "bd088dc940a418f09cda079a9b5c7c478890fb8d",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.5 || ^7.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
            "time": "2018-07-15T17:25:16+00:00"
        },
        {
            "name": "paragonie/random_compat",
            "version": "v9.99.99",
            "source": {
                "type": "git",
                "url": "https://github.com/paragonie/random_compat.git",
                "reference": "84b4dfb120c6f9b4ff7b3685f9b8f1aa365a0c95"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/paragonie/random_compat/zipball/84b4dfb120c6f9b4ff7b3685f9b8f1aa365a0c95",
                "reference": "84b4dfb120c6f9b4ff7b3685f9b8f1aa365a0c95",
                "shasum": ""
            },
            "require": {
                "php": "^7"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*|5.*",
                "vimeo/psalm": "^1"
            },
            "suggest": {
                "ext-libsodium": "Provides a modern crypto API that can be used to generate random bytes."
            },
            "type": "library",
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
                "polyfill",
                "pseudorandom",
                "random"
            ],
            "time": "2018-07-02T15:55:56+00:00"
        },
        {
            "name": "pear2/cache_shm",
            "version": "0.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Cache_SHM.git",
                "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Cache_SHM/zipball/1de608d1b59df5ba55172ba727b1da581e1497eb",
                "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9"
            },
            "suggest": {
                "ext-apc": ">=5.0.0",
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
            "time": "2016-11-07T02:09:36+00:00"
        },
        {
            "name": "pear2/net_routeros",
            "version": "1.0.0b5",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_RouterOS.git",
                "reference": "db24b8c4cd63d593dc8387987a954926d96cafb8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_RouterOS/zipball/db24b8c4cd63d593dc8387987a954926d96cafb8",
                "reference": "db24b8c4cd63d593dc8387987a954926d96cafb8",
                "shasum": ""
            },
            "require": {
                "pear2/net_transmitter": ">=1.0.0a5",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "pear2/cache_shm": "dev-develop",
                "pear2/console_color": "dev-develop",
                "pear2/console_commandline": "dev-master",
                "phpunit/phpunit": "@stable",
                "squizlabs/php_codesniffer": "@stable"
            },
            "suggest": {
                "ext-apc": "This or Wincache is required for persistent connections.",
                "ext-openssl": "Enables encrypted connections.",
                "ext-wincache": "This or APC is required for persistent connections. Reccomended instead of APC on Windows.",
                "pear2/cache_shm": "Enables persistent connections.",
                "pear2/console_color": "Enables colors in the console",
                "pear2/console_commandline": "Enables the console"
            },
            "bin": [
                "scripts/roscon.php"
            ],
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Net\\RouterOS\\": "src/",
                    "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
                    "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
                    "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
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
            "time": "2014-11-04T12:52:46+00:00"
        },
        {
            "name": "pear2/net_transmitter",
            "version": "1.0.0a5",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_Transmitter.git",
                "reference": "ac4d5fe6b7fd1a25f9a45c4454a8e85462837370"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_Transmitter/zipball/ac4d5fe6b7fd1a25f9a45c4454a8e85462837370",
                "reference": "ac4d5fe6b7fd1a25f9a45c4454a8e85462837370",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "pear2/cache_shm": "dev-develop",
                "phpunit/phpunit": "@stable"
            },
            "suggest": {
                "ext-apc": ">=3.0.13",
                "ext-openssl": "*",
                "ext-wincache": ">=1.1.0",
                "pear2/cache_shm": ">=0.1.3"
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
                    "role": "lead"
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
            "time": "2014-11-02T05:04:39+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
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
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "time": "2017-02-14T16:28:37+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "4ebe3a8bf773a19edfe0a84b6585ba3d401b724d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/4ebe3a8bf773a19edfe0a84b6585ba3d401b724d",
                "reference": "4ebe3a8bf773a19edfe0a84b6585ba3d401b724d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "Psr/Log/"
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
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "time": "2016-10-10T12:19:37+00:00"
        },
        {
            "name": "psr/simple-cache",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/simple-cache.git",
                "reference": "408d5eafb83c57f6365a3ca330ff23aa4a5fa39b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/simple-cache/zipball/408d5eafb83c57f6365a3ca330ff23aa4a5fa39b",
                "reference": "408d5eafb83c57f6365a3ca330ff23aa4a5fa39b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\SimpleCache\\": "src/"
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
            "description": "Common interfaces for simple caching",
            "keywords": [
                "cache",
                "caching",
                "psr",
                "psr-16",
                "simple-cache"
            ],
            "time": "2017-10-23T01:57:42+00:00"
        },
        {
            "name": "psy/psysh",
            "version": "v0.9.8",
            "source": {
                "type": "git",
                "url": "https://github.com/bobthecow/psysh.git",
                "reference": "ed3c32c4304e1a678a6e0f9dc11dd2d927d89555"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/bobthecow/psysh/zipball/ed3c32c4304e1a678a6e0f9dc11dd2d927d89555",
                "reference": "ed3c32c4304e1a678a6e0f9dc11dd2d927d89555",
                "shasum": ""
            },
            "require": {
                "dnoegel/php-xdg-base-dir": "0.1",
                "ext-json": "*",
                "ext-tokenizer": "*",
                "jakub-onderka/php-console-highlighter": "0.3.*",
                "nikic/php-parser": "~1.3|~2.0|~3.0|~4.0",
                "php": ">=5.4.0",
                "symfony/console": "~2.3.10|^2.4.2|~3.0|~4.0",
                "symfony/var-dumper": "~2.7|~3.0|~4.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.2",
                "hoa/console": "~2.15|~3.16",
                "phpunit/phpunit": "~4.8.35|~5.0|~6.0|~7.0"
            },
            "suggest": {
                "ext-pcntl": "Enabling the PCNTL extension makes PsySH a lot happier :)",
                "ext-pdo-sqlite": "The doc command requires SQLite to work.",
                "ext-posix": "If you have PCNTL, you'll want the POSIX extension as well.",
                "ext-readline": "Enables support for arrow-key history navigation, and showing and manipulating command history.",
                "hoa/console": "A pure PHP readline implementation. You'll want this if your PHP install doesn't already support readline or libedit."
            },
            "bin": [
                "bin/psysh"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-develop": "0.9.x-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/functions.php"
                ],
                "psr-4": {
                    "Psy\\": "src/"
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
            "time": "2018-09-05T11:40:09+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "3.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "d09ea80159c1929d75b3f9c60504d613aeb4a1e3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/d09ea80159c1929d75b3f9c60504d613aeb4a1e3",
                "reference": "d09ea80159c1929d75b3f9c60504d613aeb4a1e3",
                "shasum": ""
            },
            "require": {
                "paragonie/random_compat": "^1.0|^2.0|9.99.99",
                "php": "^5.4 || ^7.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "codeception/aspect-mock": "^1.0 | ~2.0.0",
                "doctrine/annotations": "~1.2.0",
                "goaop/framework": "1.0.0-alpha.2 | ^1.0 | ~2.1.0",
                "ircmaxell/random-lib": "^1.1",
                "jakub-onderka/php-parallel-lint": "^0.9.0",
                "mockery/mockery": "^0.9.9",
                "moontoast/math": "^1.1",
                "php-mock/php-mock-phpunit": "^0.3|^1.1",
                "phpunit/phpunit": "^4.7|^5.0|^6.5",
                "squizlabs/php_codesniffer": "^2.3"
            },
            "suggest": {
                "ext-ctype": "Provides support for PHP Ctype functions",
                "ext-libsodium": "Provides the PECL libsodium extension for use with the SodiumRandomGenerator",
                "ext-uuid": "Provides the PECL UUID extension for use with the PeclUuidTimeGenerator and PeclUuidRandomGenerator",
                "ircmaxell/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "moontoast/math": "Provides support for converting UUID to 128-bit integer (in string form).",
                "ramsey/uuid-console": "A console application for generating UUIDs with ramsey/uuid",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marijn Huizendveld",
                    "email": "marijn.huizendveld@gmail.com"
                },
                {
                    "name": "Thibaud Fabre",
                    "email": "thibaud@aztech.io"
                },
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "Formerly rhumsaa/uuid. A PHP 5.4+ library for generating RFC 4122 version 1, 3, 4, and 5 universally unique identifiers (UUID).",
            "homepage": "https://github.com/ramsey/uuid",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "time": "2018-07-19T23:38:55+00:00"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "v6.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "8ddcb66ac10c392d3beb54829eef8ac1438595f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/8ddcb66ac10c392d3beb54829eef8ac1438595f4",
                "reference": "8ddcb66ac10c392d3beb54829eef8ac1438595f4",
                "shasum": ""
            },
            "require": {
                "egulias/email-validator": "~2.0",
                "php": ">=7.0.0"
            },
            "require-dev": {
                "mockery/mockery": "~0.9.1",
                "symfony/phpunit-bridge": "~3.3@dev"
            },
            "suggest": {
                "ext-intl": "Needed to support internationalized email addresses",
                "true/punycode": "Needed to support internationalized email addresses, if ext-intl is not installed"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.1-dev"
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
            "homepage": "https://swiftmailer.symfony.com",
            "keywords": [
                "email",
                "mail",
                "mailer"
            ],
            "time": "2018-09-11T07:12:52+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "ca80b8ced97cf07390078b29773dc384c39eee1f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/ca80b8ced97cf07390078b29773dc384c39eee1f",
                "reference": "ca80b8ced97cf07390078b29773dc384c39eee1f",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/dependency-injection": "<3.4",
                "symfony/process": "<3.3"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "~3.4|~4.0",
                "symfony/dependency-injection": "~3.4|~4.0",
                "symfony/event-dispatcher": "~3.4|~4.0",
                "symfony/lock": "~3.4|~4.0",
                "symfony/process": "~3.4|~4.0"
            },
            "suggest": {
                "psr/log-implementation": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-07-26T11:24:31+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "2a4df7618f869b456f9096781e78c57b509d76c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/2a4df7618f869b456f9096781e78c57b509d76c7",
                "reference": "2a4df7618f869b456f9096781e78c57b509d76c7",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-07-26T09:10:45+00:00"
        },
        {
            "name": "symfony/debug",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/debug.git",
                "reference": "47ead688f1f2877f3f14219670f52e4722ee7052"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/debug/zipball/47ead688f1f2877f3f14219670f52e4722ee7052",
                "reference": "47ead688f1f2877f3f14219670f52e4722ee7052",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "psr/log": "~1.0"
            },
            "conflict": {
                "symfony/http-kernel": "<3.4"
            },
            "require-dev": {
                "symfony/http-kernel": "~3.4|~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-03T11:13:38+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "bfb30c2ad377615a463ebbc875eba64a99f6aa3e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/bfb30c2ad377615a463ebbc875eba64a99f6aa3e",
                "reference": "bfb30c2ad377615a463ebbc875eba64a99f6aa3e",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "conflict": {
                "symfony/dependency-injection": "<3.4"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "~3.4|~4.0",
                "symfony/dependency-injection": "~3.4|~4.0",
                "symfony/expression-language": "~3.4|~4.0",
                "symfony/stopwatch": "~3.4|~4.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-07-26T09:10:45+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "e162f1df3102d0b7472805a5a9d5db9fcf0a8068"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/e162f1df3102d0b7472805a5a9d5db9fcf0a8068",
                "reference": "e162f1df3102d0b7472805a5a9d5db9fcf0a8068",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-07-26T11:24:31+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "3a5c91e133b220bb882b3cd773ba91bf39989345"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/3a5c91e133b220bb882b3cd773ba91bf39989345",
                "reference": "3a5c91e133b220bb882b3cd773ba91bf39989345",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.1"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/expression-language": "~3.4|~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-27T17:47:02+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "33de0a1ff2e1720096189e3ced682d7a4e8f5e35"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/33de0a1ff2e1720096189e3ced682d7a4e8f5e35",
                "reference": "33de0a1ff2e1720096189e3ced682d7a4e8f5e35",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "psr/log": "~1.0",
                "symfony/debug": "~3.4|~4.0",
                "symfony/event-dispatcher": "~4.1",
                "symfony/http-foundation": "^4.1.1",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/config": "<3.4",
                "symfony/dependency-injection": "<4.1",
                "symfony/var-dumper": "<4.1.1",
                "twig/twig": "<1.34|<2.4,>=2"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/cache": "~1.0",
                "symfony/browser-kit": "~3.4|~4.0",
                "symfony/config": "~3.4|~4.0",
                "symfony/console": "~3.4|~4.0",
                "symfony/css-selector": "~3.4|~4.0",
                "symfony/dependency-injection": "^4.1",
                "symfony/dom-crawler": "~3.4|~4.0",
                "symfony/expression-language": "~3.4|~4.0",
                "symfony/finder": "~3.4|~4.0",
                "symfony/process": "~3.4|~4.0",
                "symfony/routing": "~3.4|~4.0",
                "symfony/stopwatch": "~3.4|~4.0",
                "symfony/templating": "~3.4|~4.0",
                "symfony/translation": "~3.4|~4.0",
                "symfony/var-dumper": "^4.1.1"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": "",
                "symfony/var-dumper": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-28T06:17:42+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "e3d826245268269cd66f8326bd8bc066687b4a19"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/e3d826245268269cd66f8326bd8bc066687b4a19",
                "reference": "e3d826245268269cd66f8326bd8bc066687b4a19",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Ctype\\": ""
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
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                },
                {
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                }
            ],
            "description": "Symfony polyfill for ctype functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "ctype",
                "polyfill",
                "portable"
            ],
            "time": "2018-08-06T14:22:27+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "d0cd638f4634c16d8df4508e847f14e9e43168b8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/d0cd638f4634c16d8df4508e847f14e9e43168b8",
                "reference": "d0cd638f4634c16d8df4508e847f14e9e43168b8",
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
                    "dev-master": "1.9-dev"
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
            "time": "2018-08-06T14:22:27+00:00"
        },
        {
            "name": "symfony/polyfill-php72",
            "version": "v1.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php72.git",
                "reference": "95c50420b0baed23852452a7f0c7b527303ed5ae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php72/zipball/95c50420b0baed23852452a7f0c7b527303ed5ae",
                "reference": "95c50420b0baed23852452a7f0c7b527303ed5ae",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php72\\": ""
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
            "description": "Symfony polyfill backporting some PHP 7.2+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2018-08-06T14:22:27+00:00"
        },
        {
            "name": "symfony/process",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/process.git",
                "reference": "86cdb930a6a855b0ab35fb60c1504cb36184f843"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/process/zipball/86cdb930a6a855b0ab35fb60c1504cb36184f843",
                "reference": "86cdb930a6a855b0ab35fb60c1504cb36184f843",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-03T11:13:38+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "a5784c2ec4168018c87b38f0e4f39d2278499f51"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/a5784c2ec4168018c87b38f0e4f39d2278499f51",
                "reference": "a5784c2ec4168018c87b38f0e4f39d2278499f51",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "conflict": {
                "symfony/config": "<3.4",
                "symfony/dependency-injection": "<3.4",
                "symfony/yaml": "<3.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.0",
                "psr/log": "~1.0",
                "symfony/config": "~3.4|~4.0",
                "symfony/dependency-injection": "~3.4|~4.0",
                "symfony/expression-language": "~3.4|~4.0",
                "symfony/http-foundation": "~3.4|~4.0",
                "symfony/yaml": "~3.4|~4.0"
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
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-03T07:58:40+00:00"
        },
        {
            "name": "symfony/translation",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "fa2182669f7983b7aa5f1a770d053f79f0ef144f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/fa2182669f7983b7aa5f1a770d053f79f0ef144f",
                "reference": "fa2182669f7983b7aa5f1a770d053f79f0ef144f",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/config": "<3.4",
                "symfony/dependency-injection": "<3.4",
                "symfony/yaml": "<3.4"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "~3.4|~4.0",
                "symfony/console": "~3.4|~4.0",
                "symfony/dependency-injection": "~3.4|~4.0",
                "symfony/finder": "~2.8|~3.0|~4.0",
                "symfony/intl": "~3.4|~4.0",
                "symfony/yaml": "~3.4|~4.0"
            },
            "suggest": {
                "psr/log-implementation": "To use logging capability in translator",
                "symfony/config": "",
                "symfony/yaml": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-07T12:45:11+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v4.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "a05426e27294bba7b0226ffc17dd01a3c6ef9777"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/a05426e27294bba7b0226ffc17dd01a3c6ef9777",
                "reference": "a05426e27294bba7b0226ffc17dd01a3c6ef9777",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php72": "~1.5"
            },
            "conflict": {
                "phpunit/phpunit": "<4.8.35|<5.4.3,>=5.0",
                "symfony/console": "<3.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/process": "~3.4|~4.0",
                "twig/twig": "~1.34|~2.4"
            },
            "suggest": {
                "ext-iconv": "To convert non-UTF-8 strings to UTF-8 (or symfony/polyfill-iconv in case ext-iconv cannot be used).",
                "ext-intl": "To show region name in time zone dump",
                "symfony/console": "To use the ServerDumpCommand and/or the bin/var-dump-server script"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.1-dev"
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
            "time": "2018-08-02T09:24:26+00:00"
        },
        {
            "name": "tijsverkoyen/css-to-inline-styles",
            "version": "2.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/tijsverkoyen/CssToInlineStyles.git",
                "reference": "0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/tijsverkoyen/CssToInlineStyles/zipball/0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757",
                "reference": "0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757",
                "shasum": ""
            },
            "require": {
                "php": "^5.5 || ^7.0",
                "symfony/css-selector": "^2.7 || ^3.0 || ^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "TijsVerkoyen\\CssToInlineStyles\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Tijs Verkoyen",
                    "email": "css_to_inline_styles@verkoyen.eu",
                    "role": "Developer"
                }
            ],
            "description": "CssToInlineStyles is a class that enables you to convert HTML-pages/files into HTML-pages/files with inline styles. This is very useful when you're sending emails.",
            "homepage": "https://github.com/tijsverkoyen/CssToInlineStyles",
            "time": "2017-11-27T11:13:29+00:00"
        },
        {
            "name": "vlucas/phpdotenv",
            "version": "v2.5.1",
            "source": {
                "type": "git",
                "url": "https://github.com/vlucas/phpdotenv.git",
                "reference": "8abb4f9aa89ddea9d52112c65bbe8d0125e2fa8e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vlucas/phpdotenv/zipball/8abb4f9aa89ddea9d52112c65bbe8d0125e2fa8e",
                "reference": "8abb4f9aa89ddea9d52112c65bbe8d0125e2fa8e",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.5-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Dotenv\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Vance Lucas",
                    "email": "vance@vancelucas.com",
                    "homepage": "http://www.vancelucas.com"
                }
            ],
            "description": "Loads environment variables from `.env` to `getenv()`, `$_ENV` and `$_SERVER` automagically.",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "time": "2018-07-29T20:33:41+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "beyondcode/laravel-dump-server",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/beyondcode/laravel-dump-server.git",
                "reference": "d24b641e9c8db7c33ad6e4db7042bbd352b92ad1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/beyondcode/laravel-dump-server/zipball/d24b641e9c8db7c33ad6e4db7042bbd352b92ad1",
                "reference": "d24b641e9c8db7c33ad6e4db7042bbd352b92ad1",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "5.6.*|5.7.*",
                "illuminate/http": "5.6.*|5.7.*",
                "illuminate/support": "5.6.*|5.7.*",
                "php": "^7.1",
                "symfony/var-dumper": "^4.1.1"
            },
            "require-dev": {
                "larapack/dd": "^1.0",
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "BeyondCode\\DumpServer\\DumpServerServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "BeyondCode\\DumpServer\\": "src"
                },
                "files": [
                    "helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marcel Pociot",
                    "email": "marcel@beyondco.de",
                    "homepage": "https://beyondcode.de",
                    "role": "Developer"
                }
            ],
            "description": "Symfony Var-Dump Server for Laravel",
            "homepage": "https://github.com/beyondcode/laravel-dump-server",
            "keywords": [
                "beyondcode",
                "laravel-dump-server"
            ],
            "time": "2018-08-05T19:09:56+00:00"
        },
        {
            "name": "doctrine/instantiator",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "185b8868aa9bf7159f5f953ed5afb2d7fcdc3bda"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/185b8868aa9bf7159f5f953ed5afb2d7fcdc3bda",
                "reference": "185b8868aa9bf7159f5f953ed5afb2d7fcdc3bda",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "athletic/athletic": "~0.1.8",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpunit/phpunit": "^6.2.3",
                "squizlabs/php_codesniffer": "^3.0.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
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
            "time": "2017-07-22T11:58:36+00:00"
        },
        {
            "name": "filp/whoops",
            "version": "2.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/filp/whoops.git",
                "reference": "e79cd403fb77fc8963a99ecc30e80ddd885b3311"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/filp/whoops/zipball/e79cd403fb77fc8963a99ecc30e80ddd885b3311",
                "reference": "e79cd403fb77fc8963a99ecc30e80ddd885b3311",
                "shasum": ""
            },
            "require": {
                "php": "^5.5.9 || ^7.0",
                "psr/log": "^1.0.1"
            },
            "require-dev": {
                "mockery/mockery": "^0.9 || ^1.0",
                "phpunit/phpunit": "^4.8.35 || ^5.7",
                "symfony/var-dumper": "^2.6 || ^3.0 || ^4.0"
            },
            "suggest": {
                "symfony/var-dumper": "Pretty print complex values better with var-dumper available",
                "whoops/soap": "Formats errors as SOAP responses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Whoops\\": "src/Whoops/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Filipe Dobreira",
                    "homepage": "https://github.com/filp",
                    "role": "Developer"
                }
            ],
            "description": "php error handling for cool kids",
            "homepage": "https://filp.github.io/whoops/",
            "keywords": [
                "error",
                "exception",
                "handling",
                "library",
                "throwable",
                "whoops"
            ],
            "time": "2018-06-30T13:14:06+00:00"
        },
        {
            "name": "fzaninotto/faker",
            "version": "v1.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/fzaninotto/Faker.git",
                "reference": "f72816b43e74063c8b10357394b6bba8cb1c10de"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fzaninotto/Faker/zipball/f72816b43e74063c8b10357394b6bba8cb1c10de",
                "reference": "f72816b43e74063c8b10357394b6bba8cb1c10de",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "ext-intl": "*",
                "phpunit/phpunit": "^4.8.35 || ^5.7",
                "squizlabs/php_codesniffer": "^1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.8-dev"
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
            "time": "2018-07-12T10:23:15+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "776503d3a8e85d4f9a1148614f95b7a608b046ad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/776503d3a8e85d4f9a1148614f95b7a608b046ad",
                "reference": "776503d3a8e85d4f9a1148614f95b7a608b046ad",
                "shasum": ""
            },
            "require": {
                "php": "^5.3|^7.0"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "1.3.3",
                "phpunit/phpunit": "~4.0",
                "satooshi/php-coveralls": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "hamcrest"
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
            "time": "2016-01-20T08:20:44+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "99e29d3596b16dabe4982548527d5ddf90232e99"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/99e29d3596b16dabe4982548527d5ddf90232e99",
                "reference": "99e29d3596b16dabe4982548527d5ddf90232e99",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "~2.0",
                "lib-pcre": ">=7.0",
                "php": ">=5.6.0"
            },
            "require-dev": {
                "phpdocumentor/phpdocumentor": "^2.9",
                "phpunit/phpunit": "~5.7.10|~6.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
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
            "description": "Mockery is a simple yet flexible PHP mock object framework",
            "homepage": "https://github.com/mockery/mockery",
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
            "time": "2018-05-08T08:54:48+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.8.1",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "3e01bdad3e18354c3dce54466b7fbe33a9f9f7f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/3e01bdad3e18354c3dce54466b7fbe33a9f9f7f8",
                "reference": "3e01bdad3e18354c3dce54466b7fbe33a9f9f7f8",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "replace": {
                "myclabs/deep-copy": "self.version"
            },
            "require-dev": {
                "doctrine/collections": "^1.0",
                "doctrine/common": "^2.6",
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DeepCopy\\": "src/DeepCopy/"
                },
                "files": [
                    "src/DeepCopy/deep_copy.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Create deep copies (clones) of your objects",
            "keywords": [
                "clone",
                "copy",
                "duplicate",
                "object",
                "object graph"
            ],
            "time": "2018-06-11T23:09:50+00:00"
        },
        {
            "name": "nunomaduro/collision",
            "version": "v2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/nunomaduro/collision.git",
                "reference": "b1f606399ae77e9479b5597cd1aa3d8ea0078176"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nunomaduro/collision/zipball/b1f606399ae77e9479b5597cd1aa3d8ea0078176",
                "reference": "b1f606399ae77e9479b5597cd1aa3d8ea0078176",
                "shasum": ""
            },
            "require": {
                "filp/whoops": "^2.1.4",
                "jakub-onderka/php-console-highlighter": "0.3.*",
                "php": "^7.1",
                "symfony/console": "~2.8|~3.3|~4.0"
            },
            "require-dev": {
                "laravel/framework": "5.6.*",
                "phpstan/phpstan": "^0.9.2",
                "phpunit/phpunit": "~7.2"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "NunoMaduro\\Collision\\Adapters\\Laravel\\CollisionServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "NunoMaduro\\Collision\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nuno Maduro",
                    "email": "enunomaduro@gmail.com"
                }
            ],
            "description": "Cli error handling for console/command-line PHP applications.",
            "keywords": [
                "artisan",
                "cli",
                "command-line",
                "console",
                "error",
                "handling",
                "laravel",
                "laravel-zero",
                "php",
                "symfony"
            ],
            "time": "2018-06-16T22:05:52+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "phar-io/version": "^2.0",
                "php": "^5.6 || ^7.0"
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
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Component for reading phar.io manifest information from a PHP Archive (PHAR)",
            "time": "2018-07-08T19:23:20+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
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
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Library for handling version information and constraints",
            "time": "2018-07-08T19:19:57+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6",
                "reference": "21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jaap van Otterdijk",
                    "email": "opensource@ijaap.nl"
                }
            ],
            "description": "Common reflection classes used by phpdocumentor to reflect the code structure",
            "homepage": "http://www.phpdoc.org",
            "keywords": [
                "FQSEN",
                "phpDocumentor",
                "phpdoc",
                "reflection",
                "static analysis"
            ],
            "time": "2017-09-11T18:02:19+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "4.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "94fd0001232e47129dd3504189fa1c7225010d08"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/94fd0001232e47129dd3504189fa1c7225010d08",
                "reference": "94fd0001232e47129dd3504189fa1c7225010d08",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "phpdocumentor/reflection-common": "^1.0.0",
                "phpdocumentor/type-resolver": "^0.4.0",
                "webmozart/assert": "^1.0"
            },
            "require-dev": {
                "doctrine/instantiator": "~1.0.5",
                "mockery/mockery": "^1.0",
                "phpunit/phpunit": "^6.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
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
                    "email": "me@mikevanriel.com"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "time": "2017-11-30T07:14:17+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "0.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/9c977708995954784726e25d0cd1dddf4e65b0f7",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7",
                "shasum": ""
            },
            "require": {
                "php": "^5.5 || ^7.0",
                "phpdocumentor/reflection-common": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^0.9.4",
                "phpunit/phpunit": "^5.2||^4.8.24"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
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
                    "email": "me@mikevanriel.com"
                }
            ],
            "time": "2017-07-14T14:27:02+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "1.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "4ba436b55987b4bf311cb7c6ba82aa528aac0a06"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/4ba436b55987b4bf311cb7c6ba82aa528aac0a06",
                "reference": "4ba436b55987b4bf311cb7c6ba82aa528aac0a06",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^5.3|^7.0",
                "phpdocumentor/reflection-docblock": "^2.0|^3.0.2|^4.0",
                "sebastian/comparator": "^1.1|^2.0|^3.0",
                "sebastian/recursion-context": "^1.0|^2.0|^3.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^2.5|^3.2",
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.5 || ^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.8.x-dev"
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
            "time": "2018-08-05T17:53:17+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "6.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "865662550c384bc1db7e51d29aeda1c2c161d69a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/865662550c384bc1db7e51d29aeda1c2c161d69a",
                "reference": "865662550c384bc1db7e51d29aeda1c2c161d69a",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-xmlwriter": "*",
                "php": "^7.1",
                "phpunit/php-file-iterator": "^2.0",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-token-stream": "^3.0",
                "sebastian/code-unit-reverse-lookup": "^1.0.1",
                "sebastian/environment": "^3.1",
                "sebastian/version": "^2.0.1",
                "theseer/tokenizer": "^1.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "suggest": {
                "ext-xdebug": "^2.6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.0-dev"
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
            "description": "Library that provides collection, processing, and rendering functionality for PHP code coverage information.",
            "homepage": "https://github.com/sebastianbergmann/php-code-coverage",
            "keywords": [
                "coverage",
                "testing",
                "xunit"
            ],
            "time": "2018-06-01T07:51:50+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "050bedf145a257b1ff02746c31894800e5122946"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/050bedf145a257b1ff02746c31894800e5122946",
                "reference": "050bedf145a257b1ff02746c31894800e5122946",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
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
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "time": "2018-09-13T20:33:42+00:00"
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
            "time": "2015-06-21T13:50:34+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "8b8454ea6958c3dee38453d3bd571e023108c91f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/8b8454ea6958c3dee38453d3bd571e023108c91f",
                "reference": "8b8454ea6958c3dee38453d3bd571e023108c91f",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
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
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "time": "2018-02-01T13:07:23+00:00"
        },
        {
            "name": "phpunit/php-token-stream",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "21ad88bbba7c3d93530d93994e0a33cd45f02ace"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/21ad88bbba7c3d93530d93994e0a33cd45f02ace",
                "reference": "21ad88bbba7c3d93530d93994e0a33cd45f02ace",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
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
            "time": "2018-02-01T13:16:43+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "7.3.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "7b331efabbb628c518c408fdfcaf571156775de2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/7b331efabbb628c518c408fdfcaf571156775de2",
                "reference": "7b331efabbb628c518c408fdfcaf571156775de2",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.1",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "myclabs/deep-copy": "^1.7",
                "phar-io/manifest": "^1.0.2",
                "phar-io/version": "^2.0",
                "php": "^7.1",
                "phpspec/prophecy": "^1.7",
                "phpunit/php-code-coverage": "^6.0.7",
                "phpunit/php-file-iterator": "^2.0.1",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-timer": "^2.0",
                "sebastian/comparator": "^3.0",
                "sebastian/diff": "^3.0",
                "sebastian/environment": "^3.1",
                "sebastian/exporter": "^3.1",
                "sebastian/global-state": "^2.0",
                "sebastian/object-enumerator": "^3.0.3",
                "sebastian/resource-operations": "^1.0",
                "sebastian/version": "^2.0.1"
            },
            "conflict": {
                "phpunit/phpunit-mock-objects": "*"
            },
            "require-dev": {
                "ext-pdo": "*"
            },
            "suggest": {
                "ext-soap": "*",
                "ext-xdebug": "*",
                "phpunit/php-invoker": "^2.0"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "7.3-dev"
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
            "time": "2018-09-08T15:14:29+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "4419fcdb5eabb9caa61a27c7a1db532a6b55dd18"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/4419fcdb5eabb9caa61a27c7a1db532a6b55dd18",
                "reference": "4419fcdb5eabb9caa61a27c7a1db532a6b55dd18",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.7 || ^6.0"
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
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "time": "2017-03-04T06:30:41+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "5de4fc177adf9bce8df98d8d141a7559d7ccf6da"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/5de4fc177adf9bce8df98d8d141a7559d7ccf6da",
                "reference": "5de4fc177adf9bce8df98d8d141a7559d7ccf6da",
                "shasum": ""
            },
            "require": {
                "php": "^7.1",
                "sebastian/diff": "^3.0",
                "sebastian/exporter": "^3.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
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
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "time": "2018-07-12T15:12:46+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "3.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "366541b989927187c4ca70490a35615d3fef2dce"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/366541b989927187c4ca70490a35615d3fef2dce",
                "reference": "366541b989927187c4ca70490a35615d3fef2dce",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0",
                "symfony/process": "^2 || ^3.3 || ^4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
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
                "diff",
                "udiff",
                "unidiff",
                "unified diff"
            ],
            "time": "2018-06-10T07:54:39+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "cd0871b3975fb7fc44d11314fd1ee20925fce4f5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/cd0871b3975fb7fc44d11314fd1ee20925fce4f5",
                "reference": "cd0871b3975fb7fc44d11314fd1ee20925fce4f5",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
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
            "time": "2017-07-01T08:51:00+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "234199f4528de6d12aaa58b612e98f7d36adb937"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/234199f4528de6d12aaa58b612e98f7d36adb937",
                "reference": "234199f4528de6d12aaa58b612e98f7d36adb937",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
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
            "time": "2017-04-03T13:19:02+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
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
            "time": "2017-04-27T15:39:26+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "7cfd9e65d11ffb5af41198476395774d4c8a84c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/7cfd9e65d11ffb5af41198476395774d4c8a84c5",
                "reference": "7cfd9e65d11ffb5af41198476395774d4c8a84c5",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/object-reflector": "^1.1.1",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
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
            "description": "Traverses array structures and object graphs to enumerate all referenced objects",
            "homepage": "https://github.com/sebastianbergmann/object-enumerator/",
            "time": "2017-08-03T12:35:26+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "773f97c67f28de00d397be301821b06708fca0be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/773f97c67f28de00d397be301821b06708fca0be",
                "reference": "773f97c67f28de00d397be301821b06708fca0be",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
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
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "time": "2017-03-29T09:07:27+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8",
                "reference": "5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
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
            "time": "2017-03-03T06:23:57+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "ce990bb21759f94aeafd30209e8cfcdfa8bc3f52"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/ce990bb21759f94aeafd30209e8cfcdfa8bc3f52",
                "reference": "ce990bb21759f94aeafd30209e8cfcdfa8bc3f52",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6.0"
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
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "time": "2015-07-28T20:34:47+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/99732be0ddb3361e16ad77b68ba41efc8e979019",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
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
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "time": "2016-10-03T07:35:21+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "cb2f008f3f05af2893a87208fe6a6c4985483f8b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/cb2f008f3f05af2893a87208fe6a6c4985483f8b",
                "reference": "cb2f008f3f05af2893a87208fe6a6c4985483f8b",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.0"
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
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                }
            ],
            "description": "A small library for converting tokenized PHP source code into XML and potentially other formats",
            "time": "2017-04-07T12:08:54+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozart/assert.git",
                "reference": "0df1908962e7a3071564e857d86874dad1ef204a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozart/assert/zipball/0df1908962e7a3071564e857d86874dad1ef204a",
                "reference": "0df1908962e7a3071564e857d86874dad1ef204a",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6",
                "sebastian/version": "^1.0.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Webmozart\\Assert\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Assertions to validate method input/output with nice error messages.",
            "keywords": [
                "assert",
                "check",
                "validate"
            ],
            "time": "2018-01-29T19:49:41+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "dev",
    "stability-flags": {
        "pear2/cache_shm": 15,
        "pear2/net_routeros": 10
    },
    "prefer-stable": true,
    "prefer-lowest": false,
    "platform": {
        "php": "^7.1.3"
    },
    "platform-dev": []
}


File: /config\app.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Application Name
    |--------------------------------------------------------------------------
    |
    | This value is the name of your application. This value is used when the
    | framework needs to place the application's name in a notification or
    | any other location as required by the application or its packages.
    |
    */

    'name' => env('APP_NAME', 'Laravel'),

    /*
    |--------------------------------------------------------------------------
    | Application Environment
    |--------------------------------------------------------------------------
    |
    | This value determines the "environment" your application is currently
    | running in. This may determine how you prefer to configure various
    | services the application utilizes. Set this in your ".env" file.
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
        Illuminate\Notifications\NotificationServiceProvider::class,
        Illuminate\Pagination\PaginationServiceProvider::class,
        Illuminate\Pipeline\PipelineServiceProvider::class,
        Illuminate\Queue\QueueServiceProvider::class,
        Illuminate\Redis\RedisServiceProvider::class,
        Illuminate\Auth\Passwords\PasswordResetServiceProvider::class,
        Illuminate\Session\SessionServiceProvider::class,
        Illuminate\Translation\TranslationServiceProvider::class,
        Illuminate\Validation\ValidationServiceProvider::class,
        Illuminate\View\ViewServiceProvider::class,
        jjsquady\MikrotikApi\MikrotikServiceProvider::class,

        /*
         * Package Service Providers...
         */

        /*
         * Application Service Providers...
         */
        App\Providers\AppServiceProvider::class,
        App\Providers\AuthServiceProvider::class,
        // App\Providers\BroadcastServiceProvider::class,
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
        'Broadcast' => Illuminate\Support\Facades\Broadcast::class,
        'Bus' => Illuminate\Support\Facades\Bus::class,
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
        'Notification' => Illuminate\Support\Facades\Notification::class,
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
        'Mikrokit' => jjsquady\MikrotikApi\Facades\MikrotikFacade::class

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
    | Supported: "pusher", "redis", "log", "null"
    |
    */

    'default' => env('BROADCAST_DRIVER', 'null'),

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
            'key' => env('PUSHER_APP_KEY'),
            'secret' => env('PUSHER_APP_SECRET'),
            'app_id' => env('PUSHER_APP_ID'),
            'options' => [
                'cluster' => env('PUSHER_APP_CLUSTER'),
                'encrypted' => true,
            ],
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
        ],

        'log' => [
            'driver' => 'log',
        ],

        'null' => [
            'driver' => 'null',
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
    | Supported: "apc", "array", "database", "file", "memcached", "redis"
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
            'path' => storage_path('framework/cache/data'),
        ],

        'memcached' => [
            'driver' => 'memcached',
            'persistent_id' => env('MEMCACHED_PERSISTENT_ID'),
            'sasl' => [
                env('MEMCACHED_USERNAME'),
                env('MEMCACHED_PASSWORD'),
            ],
            'options' => [
                // Memcached::OPT_CONNECT_TIMEOUT  => 2000,
            ],
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
            'connection' => 'cache',
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

    'prefix' => env(
        'CACHE_PREFIX',
        str_slug(env('APP_NAME', 'laravel'), '_').'_cache'
    ),

];


File: /config\database.php
<?php

return [

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
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'strict' => true,
            'engine' => null,
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'schema' => 'public',
            'sslmode' => 'prefer',
        ],

        'sqlsrv' => [
            'driver' => 'sqlsrv',
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '1433'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
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

        'client' => 'predis',

        'default' => [
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', 6379),
            'database' => env('REDIS_DB', 0),
        ],

        'cache' => [
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', 6379),
            'database' => env('REDIS_CACHE_DB', 1),
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
    | by the framework. The "local" disk, as well as a variety of cloud
    | based disks are available to your application. Just store away!
    |
    */

    'default' => env('FILESYSTEM_DRIVER', 'local'),

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

    'cloud' => env('FILESYSTEM_CLOUD', 's3'),

    /*
    |--------------------------------------------------------------------------
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Here you may configure as many filesystem "disks" as you wish, and you
    | may even configure multiple disks of the same driver. Defaults have
    | been setup for each driver as an example of the required options.
    |
    | Supported Drivers: "local", "ftp", "sftp", "s3", "rackspace"
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
            'url' => env('APP_URL').'/storage',
            'visibility' => 'public',
        ],

        's3' => [
            'driver' => 's3',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION'),
            'bucket' => env('AWS_BUCKET'),
            'url' => env('AWS_URL'),
        ],

    ],

];


File: /config\hashing.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Hash Driver
    |--------------------------------------------------------------------------
    |
    | This option controls the default hash driver that will be used to hash
    | passwords for your application. By default, the bcrypt algorithm is
    | used; however, you remain free to modify this option if you wish.
    |
    | Supported: "bcrypt", "argon", "argon2id"
    |
    */

    'driver' => 'bcrypt',

    /*
    |--------------------------------------------------------------------------
    | Bcrypt Options
    |--------------------------------------------------------------------------
    |
    | Here you may specify the configuration options that should be used when
    | passwords are hashed using the Bcrypt algorithm. This will allow you
    | to control the amount of time it takes to hash the given password.
    |
    */

    'bcrypt' => [
        'rounds' => env('BCRYPT_ROUNDS', 10),
    ],

    /*
    |--------------------------------------------------------------------------
    | Argon Options
    |--------------------------------------------------------------------------
    |
    | Here you may specify the configuration options that should be used when
    | passwords are hashed using the Argon algorithm. These will allow you
    | to control the amount of time it takes to hash the given password.
    |
    */

    'argon' => [
        'memory' => 1024,
        'threads' => 2,
        'time' => 2,
    ],

];


File: /config\logging.php
<?php

use Monolog\Handler\StreamHandler;

return [

    /*
    |--------------------------------------------------------------------------
    | Default Log Channel
    |--------------------------------------------------------------------------
    |
    | This option defines the default log channel that gets used when writing
    | messages to the logs. The name specified in this option should match
    | one of the channels defined in the "channels" configuration array.
    |
    */

    'default' => env('LOG_CHANNEL', 'stack'),

    /*
    |--------------------------------------------------------------------------
    | Log Channels
    |--------------------------------------------------------------------------
    |
    | Here you may configure the log channels for your application. Out of
    | the box, Laravel uses the Monolog PHP logging library. This gives
    | you a variety of powerful log handlers / formatters to utilize.
    |
    | Available Drivers: "single", "daily", "slack", "syslog",
    |                    "errorlog", "monolog",
    |                    "custom", "stack"
    |
    */

    'channels' => [
        'stack' => [
            'driver' => 'stack',
            'channels' => ['single'],
        ],

        'single' => [
            'driver' => 'single',
            'path' => storage_path('logs/laravel.log'),
            'level' => 'debug',
        ],

        'daily' => [
            'driver' => 'daily',
            'path' => storage_path('logs/laravel.log'),
            'level' => 'debug',
            'days' => 7,
        ],

        'slack' => [
            'driver' => 'slack',
            'url' => env('LOG_SLACK_WEBHOOK_URL'),
            'username' => 'Laravel Log',
            'emoji' => ':boom:',
            'level' => 'critical',
        ],

        'stderr' => [
            'driver' => 'monolog',
            'handler' => StreamHandler::class,
            'with' => [
                'stream' => 'php://stderr',
            ],
        ],

        'syslog' => [
            'driver' => 'syslog',
            'level' => 'debug',
        ],

        'errorlog' => [
            'driver' => 'errorlog',
            'level' => 'debug',
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
    | Supported: "smtp", "sendmail", "mailgun", "mandrill", "ses",
    |            "sparkpost", "log", "array"
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

    'from' => [
        'address' => env('MAIL_FROM_ADDRESS', 'hello@example.com'),
        'name' => env('MAIL_FROM_NAME', 'Example'),
    ],

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

    /*
    |--------------------------------------------------------------------------
    | Markdown Mail Settings
    |--------------------------------------------------------------------------
    |
    | If you are using Markdown based email rendering, you may configure your
    | theme and component paths here, allowing you to customize the design
    | of the emails. Or, you may simply stick with the Laravel defaults!
    |
    */

    'markdown' => [
        'theme' => 'default',

        'paths' => [
            resource_path('views/vendor/mail'),
        ],
    ],

];


File: /config\queue.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Queue Connection Name
    |--------------------------------------------------------------------------
    |
    | Laravel's queue API supports an assortment of back-ends via a single
    | API, giving you convenient access to each back-end using the same
    | syntax for every one. Here you may define a default connection.
    |
    */

    'default' => env('QUEUE_CONNECTION', 'sync'),

    /*
    |--------------------------------------------------------------------------
    | Queue Connections
    |--------------------------------------------------------------------------
    |
    | Here you may configure the connection information for each server that
    | is used by your application. A default configuration has been added
    | for each back-end shipped with Laravel. You are free to add more.
    |
    | Drivers: "sync", "database", "beanstalkd", "sqs", "redis", "null"
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
            'retry_after' => 90,
        ],

        'beanstalkd' => [
            'driver' => 'beanstalkd',
            'host' => 'localhost',
            'queue' => 'default',
            'retry_after' => 90,
        ],

        'sqs' => [
            'driver' => 'sqs',
            'key' => env('SQS_KEY', 'your-public-key'),
            'secret' => env('SQS_SECRET', 'your-secret-key'),
            'prefix' => env('SQS_PREFIX', 'https://sqs.us-east-1.amazonaws.com/your-account-id'),
            'queue' => env('SQS_QUEUE', 'your-queue-name'),
            'region' => env('SQS_REGION', 'us-east-1'),
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => 'default',
            'retry_after' => 90,
            'block_for' => null,
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
    | as Stripe, Mailgun, SparkPost and others. This file provides a sane
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
        'region' => env('SES_REGION', 'us-east-1'),
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

    'lifetime' => env('SESSION_LIFETIME', 120),

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

    'connection' => env('SESSION_CONNECTION', null),

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
    | Session Cache Store
    |--------------------------------------------------------------------------
    |
    | When using the "apc" or "memcached" session drivers, you may specify a
    | cache store that should be used for these sessions. This value must
    | correspond with one of the application's configured cache stores.
    |
    */

    'store' => env('SESSION_STORE', null),

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

    'cookie' => env(
        'SESSION_COOKIE',
        str_slug(env('APP_NAME', 'laravel'), '_').'_session'
    ),

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

    'domain' => env('SESSION_DOMAIN', null),

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

    'secure' => env('SESSION_SECURE_COOKIE', false),

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

    /*
    |--------------------------------------------------------------------------
    | Same-Site Cookies
    |--------------------------------------------------------------------------
    |
    | This option determines how your cookies behave when cross-site requests
    | take place, and can be used to mitigate CSRF attacks. By default, we
    | do not enable this as other CSRF protection services are in place.
    |
    | Supported: "lax", "strict"
    |
    */

    'same_site' => null,

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
        resource_path('views'),
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


File: /database\factories\UserFactory.php
<?php

use Faker\Generator as Faker;

/*
|--------------------------------------------------------------------------
| Model Factories
|--------------------------------------------------------------------------
|
| This directory should contain each of the model factory definitions for
| your application. Factories provide a convenient way to generate new
| model instances for testing / seeding your application's database.
|
*/

$factory->define(App\User::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => '$2y$10$TKh8H1.PfQx37YgCzwiKb.KjNyWgaHb9cbcoQgdIVFlYg7B77UdFm', // secret
        'remember_token' => str_random(10),
    ];
});


File: /database\migrations\2014_10_12_000000_create_users_table.php
<?php

use Illuminate\Support\Facades\Schema;
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
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}


File: /database\migrations\2014_10_12_100000_create_password_resets_table.php
<?php

use Illuminate\Support\Facades\Schema;
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
            $table->string('token');
            $table->timestamp('created_at')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('password_resets');
    }
}


File: /database\seeds\DatabaseSeeder.php
<?php

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // $this->call(UsersTableSeeder::class);
    }
}


File: /package.json
{
    "private": true,
    "scripts": {
        "dev": "npm run development",
File: /phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit backupGlobals="false"
         backupStaticAttributes="false"
         bootstrap="vendor/autoload.php"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false">
    <testsuites>
        <testsuite name="Unit">
            <directory suffix="Test.php">./tests/Unit</directory>
        </testsuite>

        <testsuite name="Feature">
            <directory suffix="Test.php">./tests/Feature</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory suffix=".php">./app</directory>
        </whitelist>
    </filter>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="BCRYPT_ROUNDS" value="4"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="QUEUE_DRIVER" value="sync"/>
        <env name="MAIL_DRIVER" value="array"/>
    </php>
</phpunit>


File: /public\.htaccess
<IfModule mod_rewrite.c>
    <IfModule mod_negotiation.c>
        Options -MultiViews -Indexes
    </IfModule>

    RewriteEngine On

    # Handle Authorization Header
    RewriteCond %{HTTP:Authorization} .
    RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

    # Redirect Trailing Slashes If Not A Folder...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_URI} (.+)/$
    RewriteRule ^ %1 [L,R=301]

    # Handle Front Controller...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [L]
</IfModule>


File: /public\css\app.css
@import url(https://fonts.googleapis.com/css?family=Nunito);/*!
 * Bootstrap v4.1.2 (https://getbootstrap.com/)
 * Copyright 2011-2018 The Bootstrap Authors
 * Copyright 2011-2018 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */:root{--blue:#3490dc;--indigo:#6574cd;--purple:#9561e2;--pink:#f66d9b;--red:#e3342f;--orange:#f6993f;--yellow:#ffed4a;--green:#38c172;--teal:#4dc0b5;--cyan:#6cb2eb;--white:#fff;--gray:#6c757d;--gray-dark:#343a40;--primary:#3490dc;--secondary:#6c757d;--success:#38c172;--info:#6cb2eb;--warning:#ffed4a;--danger:#e3342f;--light:#f8f9fa;--dark:#343a40;--breakpoint-xs:0;--breakpoint-sm:576px;--breakpoint-md:768px;--breakpoint-lg:992px;--breakpoint-xl:1200px;--font-family-sans-serif:"Nunito",sans-serif;--font-family-monospace:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace}*,:after,:before{-webkit-box-sizing:border-box;box-sizing:border-box}html{font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;-ms-overflow-style:scrollbar;-webkit-tap-highlight-color:rgba(0,0,0,0)}@-ms-viewport{width:device-width}article,aside,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}body{margin:0;font-family:Nunito,sans-serif;font-size:.9rem;font-weight:400;line-height:1.6;color:#212529;text-align:left;background-color:#f8fafc}[tabindex="-1"]:focus{outline:0!important}hr{-webkit-box-sizing:content-box;box-sizing:content-box;height:0;overflow:visible}h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:.5rem}p{margin-top:0;margin-bottom:1rem}abbr[data-original-title],abbr[title]{text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted;cursor:help;border-bottom:0}address{font-style:normal;line-height:inherit}address,dl,ol,ul{margin-bottom:1rem}dl,ol,ul{margin-top:0}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}dt{font-weight:700}dd{margin-bottom:.5rem;margin-left:0}blockquote{margin:0 0 1rem}dfn{font-style:italic}b,strong{font-weight:bolder}small{font-size:80%}sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}a{color:#3490dc;text-decoration:none;background-color:transparent;-webkit-text-decoration-skip:objects}a:hover{color:#1d68a7;text-decoration:underline}a:not([href]):not([tabindex]),a:not([href]):not([tabindex]):focus,a:not([href]):not([tabindex]):hover{color:inherit;text-decoration:none}a:not([href]):not([tabindex]):focus{outline:0}code,kbd,pre,samp{font-family:SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:1em}pre{margin-top:0;margin-bottom:1rem;overflow:auto;-ms-overflow-style:scrollbar}figure{margin:0 0 1rem}img{border-style:none}img,svg:not(:root){vertical-align:middle}svg:not(:root){overflow:hidden}table{border-collapse:collapse}caption{padding-top:.75rem;padding-bottom:.75rem;color:#6c757d;text-align:left;caption-side:bottom}th{text-align:inherit}label{display:inline-block;margin-bottom:.5rem}button{border-radius:0}button:focus{outline:1px dotted;outline:5px auto -webkit-focus-ring-color}button,input,optgroup,select,textarea{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{padding:0;border-style:none}input[type=checkbox],input[type=radio]{-webkit-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=date],input[type=datetime-local],input[type=month],input[type=time]{-webkit-appearance:listbox}textarea{overflow:auto;resize:vertical}fieldset{min-width:0;padding:0;margin:0;border:0}legend{display:block;width:100%;max-width:100%;padding:0;margin-bottom:.5rem;font-size:1.5rem;line-height:inherit;color:inherit;white-space:normal}progress{vertical-align:baseline}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{outline-offset:-2px;-webkit-appearance:none}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}output{display:inline-block}summary{display:list-item;cursor:pointer}template{display:none}[hidden]{display:none!important}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{margin-bottom:.5rem;font-family:inherit;font-weight:500;line-height:1.2;color:inherit}.h1,h1{font-size:2.25rem}.h2,h2{font-size:1.8rem}.h3,h3{font-size:1.575rem}.h4,h4{font-size:1.35rem}.h5,h5{font-size:1.125rem}.h6,h6{font-size:.9rem}.lead{font-size:1.125rem;font-weight:300}.display-1{font-size:6rem}.display-1,.display-2{font-weight:300;line-height:1.2}.display-2{font-size:5.5rem}.display-3{font-size:4.5rem}.display-3,.display-4{font-weight:300;line-height:1.2}.display-4{font-size:3.5rem}hr{margin-top:1rem;margin-bottom:1rem;border:0;border-top:1px solid rgba(0,0,0,.1)}.small,small{font-size:80%;font-weight:400}.mark,mark{padding:.2em;background-color:#fcf8e3}.list-inline,.list-unstyled{padding-left:0;list-style:none}.list-inline-item{display:inline-block}.list-inline-item:not(:last-child){margin-right:.5rem}.initialism{font-size:90%;text-transform:uppercase}.blockquote{margin-bottom:1rem;font-size:1.125rem}.blockquote-footer{display:block;font-size:80%;color:#6c757d}.blockquote-footer:before{content:"\2014   \A0"}.img-fluid,.img-thumbnail{max-width:100%;height:auto}.img-thumbnail{padding:.25rem;background-color:#f8fafc;border:1px solid #dee2e6;border-radius:.25rem}.figure{display:inline-block}.figure-img{margin-bottom:.5rem;line-height:1}.figure-caption{font-size:90%;color:#6c757d}code{font-size:87.5%;color:#f66d9b;word-break:break-word}a>code{color:inherit}kbd{padding:.2rem .4rem;font-size:87.5%;color:#fff;background-color:#212529;border-radius:.2rem}kbd kbd{padding:0;font-size:100%;font-weight:700}pre{display:block;font-size:87.5%;color:#212529}pre code{font-size:inherit;color:inherit;word-break:normal}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:576px){.container{max-width:540px}}@media (min-width:768px){.container{max-width:720px}}@media (min-width:992px){.container{max-width:960px}}@media (min-width:1200px){.container{max-width:1140px}}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.row{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.no-gutters{margin-right:0;margin-left:0}.no-gutters>.col,.no-gutters>[class*=col-]{padding-right:0;padding-left:0}.col,.col-1,.col-2,.col-3,.col-4,.col-5,.col-6,.col-7,.col-8,.col-9,.col-10,.col-11,.col-12,.col-auto,.col-lg,.col-lg-1,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-auto,.col-md,.col-md-1,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-md-10,.col-md-11,.col-md-12,.col-md-auto,.col-sm,.col-sm-1,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-auto,.col-xl,.col-xl-1,.col-xl-2,.col-xl-3,.col-xl-4,.col-xl-5,.col-xl-6,.col-xl-7,.col-xl-8,.col-xl-9,.col-xl-10,.col-xl-11,.col-xl-12,.col-xl-auto{position:relative;width:100%;min-height:1px;padding-right:15px;padding-left:15px}.col{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-auto{-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-1,.col-auto{-webkit-box-flex:0}.col-1{-ms-flex:0 0 8.33333333%;flex:0 0 8.33333333%;max-width:8.33333333%}.col-2{-ms-flex:0 0 16.66666667%;flex:0 0 16.66666667%;max-width:16.66666667%}.col-2,.col-3{-webkit-box-flex:0}.col-3{-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-4{-ms-flex:0 0 33.33333333%;flex:0 0 33.33333333%;max-width:33.33333333%}.col-4,.col-5{-webkit-box-flex:0}.col-5{-ms-flex:0 0 41.66666667%;flex:0 0 41.66666667%;max-width:41.66666667%}.col-6{-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-6,.col-7{-webkit-box-flex:0}.col-7{-ms-flex:0 0 58.33333333%;flex:0 0 58.33333333%;max-width:58.33333333%}.col-8{-ms-flex:0 0 66.66666667%;flex:0 0 66.66666667%;max-width:66.66666667%}.col-8,.col-9{-webkit-box-flex:0}.col-9{-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-10{-ms-flex:0 0 83.33333333%;flex:0 0 83.33333333%;max-width:83.33333333%}.col-10,.col-11{-webkit-box-flex:0}.col-11{-ms-flex:0 0 91.66666667%;flex:0 0 91.66666667%;max-width:91.66666667%}.col-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-1{margin-left:8.33333333%}.offset-2{margin-left:16.66666667%}.offset-3{margin-left:25%}.offset-4{margin-left:33.33333333%}.offset-5{margin-left:41.66666667%}.offset-6{margin-left:50%}.offset-7{margin-left:58.33333333%}.offset-8{margin-left:66.66666667%}.offset-9{margin-left:75%}.offset-10{margin-left:83.33333333%}.offset-11{margin-left:91.66666667%}@media (min-width:576px){.col-sm{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-sm-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-sm-1{-webkit-box-flex:0;-ms-flex:0 0 8.33333333%;flex:0 0 8.33333333%;max-width:8.33333333%}.col-sm-2{-webkit-box-flex:0;-ms-flex:0 0 16.66666667%;flex:0 0 16.66666667%;max-width:16.66666667%}.col-sm-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-sm-4{-webkit-box-flex:0;-ms-flex:0 0 33.33333333%;flex:0 0 33.33333333%;max-width:33.33333333%}.col-sm-5{-webkit-box-flex:0;-ms-flex:0 0 41.66666667%;flex:0 0 41.66666667%;max-width:41.66666667%}.col-sm-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-sm-7{-webkit-box-flex:0;-ms-flex:0 0 58.33333333%;flex:0 0 58.33333333%;max-width:58.33333333%}.col-sm-8{-webkit-box-flex:0;-ms-flex:0 0 66.66666667%;flex:0 0 66.66666667%;max-width:66.66666667%}.col-sm-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-sm-10{-webkit-box-flex:0;-ms-flex:0 0 83.33333333%;flex:0 0 83.33333333%;max-width:83.33333333%}.col-sm-11{-webkit-box-flex:0;-ms-flex:0 0 91.66666667%;flex:0 0 91.66666667%;max-width:91.66666667%}.col-sm-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-sm-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-sm-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-sm-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-sm-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-sm-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-sm-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-sm-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-sm-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-sm-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-sm-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-sm-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-sm-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-sm-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-sm-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-sm-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-sm-0{margin-left:0}.offset-sm-1{margin-left:8.33333333%}.offset-sm-2{margin-left:16.66666667%}.offset-sm-3{margin-left:25%}.offset-sm-4{margin-left:33.33333333%}.offset-sm-5{margin-left:41.66666667%}.offset-sm-6{margin-left:50%}.offset-sm-7{margin-left:58.33333333%}.offset-sm-8{margin-left:66.66666667%}.offset-sm-9{margin-left:75%}.offset-sm-10{margin-left:83.33333333%}.offset-sm-11{margin-left:91.66666667%}}@media (min-width:768px){.col-md{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-md-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-md-1{-webkit-box-flex:0;-ms-flex:0 0 8.33333333%;flex:0 0 8.33333333%;max-width:8.33333333%}.col-md-2{-webkit-box-flex:0;-ms-flex:0 0 16.66666667%;flex:0 0 16.66666667%;max-width:16.66666667%}.col-md-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-md-4{-webkit-box-flex:0;-ms-flex:0 0 33.33333333%;flex:0 0 33.33333333%;max-width:33.33333333%}.col-md-5{-webkit-box-flex:0;-ms-flex:0 0 41.66666667%;flex:0 0 41.66666667%;max-width:41.66666667%}.col-md-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-md-7{-webkit-box-flex:0;-ms-flex:0 0 58.33333333%;flex:0 0 58.33333333%;max-width:58.33333333%}.col-md-8{-webkit-box-flex:0;-ms-flex:0 0 66.66666667%;flex:0 0 66.66666667%;max-width:66.66666667%}.col-md-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-md-10{-webkit-box-flex:0;-ms-flex:0 0 83.33333333%;flex:0 0 83.33333333%;max-width:83.33333333%}.col-md-11{-webkit-box-flex:0;-ms-flex:0 0 91.66666667%;flex:0 0 91.66666667%;max-width:91.66666667%}.col-md-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-md-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-md-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-md-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-md-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-md-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-md-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-md-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-md-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-md-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-md-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-md-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-md-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-md-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-md-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-md-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-md-0{margin-left:0}.offset-md-1{margin-left:8.33333333%}.offset-md-2{margin-left:16.66666667%}.offset-md-3{margin-left:25%}.offset-md-4{margin-left:33.33333333%}.offset-md-5{margin-left:41.66666667%}.offset-md-6{margin-left:50%}.offset-md-7{margin-left:58.33333333%}.offset-md-8{margin-left:66.66666667%}.offset-md-9{margin-left:75%}.offset-md-10{margin-left:83.33333333%}.offset-md-11{margin-left:91.66666667%}}@media (min-width:992px){.col-lg{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-lg-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-lg-1{-webkit-box-flex:0;-ms-flex:0 0 8.33333333%;flex:0 0 8.33333333%;max-width:8.33333333%}.col-lg-2{-webkit-box-flex:0;-ms-flex:0 0 16.66666667%;flex:0 0 16.66666667%;max-width:16.66666667%}.col-lg-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-lg-4{-webkit-box-flex:0;-ms-flex:0 0 33.33333333%;flex:0 0 33.33333333%;max-width:33.33333333%}.col-lg-5{-webkit-box-flex:0;-ms-flex:0 0 41.66666667%;flex:0 0 41.66666667%;max-width:41.66666667%}.col-lg-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-lg-7{-webkit-box-flex:0;-ms-flex:0 0 58.33333333%;flex:0 0 58.33333333%;max-width:58.33333333%}.col-lg-8{-webkit-box-flex:0;-ms-flex:0 0 66.66666667%;flex:0 0 66.66666667%;max-width:66.66666667%}.col-lg-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-lg-10{-webkit-box-flex:0;-ms-flex:0 0 83.33333333%;flex:0 0 83.33333333%;max-width:83.33333333%}.col-lg-11{-webkit-box-flex:0;-ms-flex:0 0 91.66666667%;flex:0 0 91.66666667%;max-width:91.66666667%}.col-lg-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-lg-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-lg-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-lg-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-lg-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-lg-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-lg-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-lg-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-lg-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-lg-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-lg-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-lg-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-lg-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-lg-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-lg-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-lg-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-lg-0{margin-left:0}.offset-lg-1{margin-left:8.33333333%}.offset-lg-2{margin-left:16.66666667%}.offset-lg-3{margin-left:25%}.offset-lg-4{margin-left:33.33333333%}.offset-lg-5{margin-left:41.66666667%}.offset-lg-6{margin-left:50%}.offset-lg-7{margin-left:58.33333333%}.offset-lg-8{margin-left:66.66666667%}.offset-lg-9{margin-left:75%}.offset-lg-10{margin-left:83.33333333%}.offset-lg-11{margin-left:91.66666667%}}@media (min-width:1200px){.col-xl{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}.col-xl-auto{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;width:auto;max-width:none}.col-xl-1{-webkit-box-flex:0;-ms-flex:0 0 8.33333333%;flex:0 0 8.33333333%;max-width:8.33333333%}.col-xl-2{-webkit-box-flex:0;-ms-flex:0 0 16.66666667%;flex:0 0 16.66666667%;max-width:16.66666667%}.col-xl-3{-webkit-box-flex:0;-ms-flex:0 0 25%;flex:0 0 25%;max-width:25%}.col-xl-4{-webkit-box-flex:0;-ms-flex:0 0 33.33333333%;flex:0 0 33.33333333%;max-width:33.33333333%}.col-xl-5{-webkit-box-flex:0;-ms-flex:0 0 41.66666667%;flex:0 0 41.66666667%;max-width:41.66666667%}.col-xl-6{-webkit-box-flex:0;-ms-flex:0 0 50%;flex:0 0 50%;max-width:50%}.col-xl-7{-webkit-box-flex:0;-ms-flex:0 0 58.33333333%;flex:0 0 58.33333333%;max-width:58.33333333%}.col-xl-8{-webkit-box-flex:0;-ms-flex:0 0 66.66666667%;flex:0 0 66.66666667%;max-width:66.66666667%}.col-xl-9{-webkit-box-flex:0;-ms-flex:0 0 75%;flex:0 0 75%;max-width:75%}.col-xl-10{-webkit-box-flex:0;-ms-flex:0 0 83.33333333%;flex:0 0 83.33333333%;max-width:83.33333333%}.col-xl-11{-webkit-box-flex:0;-ms-flex:0 0 91.66666667%;flex:0 0 91.66666667%;max-width:91.66666667%}.col-xl-12{-webkit-box-flex:0;-ms-flex:0 0 100%;flex:0 0 100%;max-width:100%}.order-xl-first{-webkit-box-ordinal-group:0;-ms-flex-order:-1;order:-1}.order-xl-last{-webkit-box-ordinal-group:14;-ms-flex-order:13;order:13}.order-xl-0{-webkit-box-ordinal-group:1;-ms-flex-order:0;order:0}.order-xl-1{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}.order-xl-2{-webkit-box-ordinal-group:3;-ms-flex-order:2;order:2}.order-xl-3{-webkit-box-ordinal-group:4;-ms-flex-order:3;order:3}.order-xl-4{-webkit-box-ordinal-group:5;-ms-flex-order:4;order:4}.order-xl-5{-webkit-box-ordinal-group:6;-ms-flex-order:5;order:5}.order-xl-6{-webkit-box-ordinal-group:7;-ms-flex-order:6;order:6}.order-xl-7{-webkit-box-ordinal-group:8;-ms-flex-order:7;order:7}.order-xl-8{-webkit-box-ordinal-group:9;-ms-flex-order:8;order:8}.order-xl-9{-webkit-box-ordinal-group:10;-ms-flex-order:9;order:9}.order-xl-10{-webkit-box-ordinal-group:11;-ms-flex-order:10;order:10}.order-xl-11{-webkit-box-ordinal-group:12;-ms-flex-order:11;order:11}.order-xl-12{-webkit-box-ordinal-group:13;-ms-flex-order:12;order:12}.offset-xl-0{margin-left:0}.offset-xl-1{margin-left:8.33333333%}.offset-xl-2{margin-left:16.66666667%}.offset-xl-3{margin-left:25%}.offset-xl-4{margin-left:33.33333333%}.offset-xl-5{margin-left:41.66666667%}.offset-xl-6{margin-left:50%}.offset-xl-7{margin-left:58.33333333%}.offset-xl-8{margin-left:66.66666667%}.offset-xl-9{margin-left:75%}.offset-xl-10{margin-left:83.33333333%}.offset-xl-11{margin-left:91.66666667%}}.table{width:100%;max-width:100%;margin-bottom:1rem;background-color:transparent}.table td,.table th{padding:.75rem;vertical-align:top;border-top:1px solid #dee2e6}.table thead th{vertical-align:bottom;border-bottom:2px solid #dee2e6}.table tbody+tbody{border-top:2px solid #dee2e6}.table .table{background-color:#f8fafc}.table-sm td,.table-sm th{padding:.3rem}.table-bordered,.table-bordered td,.table-bordered th{border:1px solid #dee2e6}.table-bordered thead td,.table-bordered thead th{border-bottom-width:2px}.table-borderless tbody+tbody,.table-borderless td,.table-borderless th,.table-borderless thead th{border:0}.table-striped tbody tr:nth-of-type(odd){background-color:rgba(0,0,0,.05)}.table-hover tbody tr:hover{background-color:rgba(0,0,0,.075)}.table-primary,.table-primary>td,.table-primary>th{background-color:#c6e0f5}.table-hover .table-primary:hover,.table-hover .table-primary:hover>td,.table-hover .table-primary:hover>th{background-color:#b0d4f1}.table-secondary,.table-secondary>td,.table-secondary>th{background-color:#d6d8db}.table-hover .table-secondary:hover,.table-hover .table-secondary:hover>td,.table-hover .table-secondary:hover>th{background-color:#c8cbcf}.table-success,.table-success>td,.table-success>th{background-color:#c7eed8}.table-hover .table-success:hover,.table-hover .table-success:hover>td,.table-hover .table-success:hover>th{background-color:#b3e8ca}.table-info,.table-info>td,.table-info>th{background-color:#d6e9f9}.table-hover .table-info:hover,.table-hover .table-info:hover>td,.table-hover .table-info:hover>th{background-color:#c0ddf6}.table-warning,.table-warning>td,.table-warning>th{background-color:#fffacc}.table-hover .table-warning:hover,.table-hover .table-warning:hover>td,.table-hover .table-warning:hover>th{background-color:#fff8b3}.table-danger,.table-danger>td,.table-danger>th{background-color:#f7c6c5}.table-hover .table-danger:hover,.table-hover .table-danger:hover>td,.table-hover .table-danger:hover>th{background-color:#f4b0af}.table-light,.table-light>td,.table-light>th{background-color:#fdfdfe}.table-hover .table-light:hover,.table-hover .table-light:hover>td,.table-hover .table-light:hover>th{background-color:#ececf6}.table-dark,.table-dark>td,.table-dark>th{background-color:#c6c8ca}.table-hover .table-dark:hover,.table-hover .table-dark:hover>td,.table-hover .table-dark:hover>th{background-color:#b9bbbe}.table-active,.table-active>td,.table-active>th,.table-hover .table-active:hover,.table-hover .table-active:hover>td,.table-hover .table-active:hover>th{background-color:rgba(0,0,0,.075)}.table .thead-dark th{color:#f8fafc;background-color:#212529;border-color:#32383e}.table .thead-light th{color:#495057;background-color:#e9ecef;border-color:#dee2e6}.table-dark{color:#f8fafc;background-color:#212529}.table-dark td,.table-dark th,.table-dark thead th{border-color:#32383e}.table-dark.table-bordered{border:0}.table-dark.table-striped tbody tr:nth-of-type(odd){background-color:hsla(0,0%,100%,.05)}.table-dark.table-hover tbody tr:hover{background-color:hsla(0,0%,100%,.075)}@media (max-width:575.98px){.table-responsive-sm{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-sm>.table-bordered{border:0}}@media (max-width:767.98px){.table-responsive-md{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-md>.table-bordered{border:0}}@media (max-width:991.98px){.table-responsive-lg{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-lg>.table-bordered{border:0}}@media (max-width:1199.98px){.table-responsive-xl{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-xl>.table-bordered{border:0}}.table-responsive{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive>.table-bordered{border:0}.form-control{display:block;width:100%;padding:.375rem .75rem;font-size:.9rem;line-height:1.6;color:#495057;background-color:#fff;background-clip:padding-box;border:1px solid #ced4da;border-radius:.25rem;-webkit-transition:border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out}@media screen and (prefers-reduced-motion:reduce){.form-control{-webkit-transition:none;transition:none}}.form-control::-ms-expand{background-color:transparent;border:0}.form-control:focus{color:#495057;background-color:#fff;border-color:#a1cbef;outline:0;-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 .2rem rgba(52,144,220,.25)}.form-control::-webkit-input-placeholder{color:#6c757d;opacity:1}.form-control:-ms-input-placeholder,.form-control::-ms-input-placeholder{color:#6c757d;opacity:1}.form-control::placeholder{color:#6c757d;opacity:1}.form-control:disabled,.form-control[readonly]{background-color:#e9ecef;opacity:1}select.form-control:not([size]):not([multiple]){height:calc(2.19rem + 2px)}select.form-control:focus::-ms-value{color:#495057;background-color:#fff}.form-control-file,.form-control-range{display:block;width:100%}.col-form-label{padding-top:calc(.375rem + 1px);padding-bottom:calc(.375rem + 1px);margin-bottom:0;font-size:inherit;line-height:1.6}.col-form-label-lg{padding-top:calc(.5rem + 1px);padding-bottom:calc(.5rem + 1px);font-size:1.125rem;line-height:1.5}.col-form-label-sm{padding-top:calc(.25rem + 1px);padding-bottom:calc(.25rem + 1px);font-size:.7875rem;line-height:1.5}.form-control-plaintext{display:block;width:100%;padding-top:.375rem;padding-bottom:.375rem;margin-bottom:0;line-height:1.6;color:#212529;background-color:transparent;border:solid transparent;border-width:1px 0}.form-control-plaintext.form-control-lg,.form-control-plaintext.form-control-sm,.input-group-lg>.form-control-plaintext.form-control,.input-group-lg>.input-group-append>.form-control-plaintext.btn,.input-group-lg>.input-group-append>.form-control-plaintext.input-group-text,.input-group-lg>.input-group-prepend>.form-control-plaintext.btn,.input-group-lg>.input-group-prepend>.form-control-plaintext.input-group-text,.input-group-sm>.form-control-plaintext.form-control,.input-group-sm>.input-group-append>.form-control-plaintext.btn,.input-group-sm>.input-group-append>.form-control-plaintext.input-group-text,.input-group-sm>.input-group-prepend>.form-control-plaintext.btn,.input-group-sm>.input-group-prepend>.form-control-plaintext.input-group-text{padding-right:0;padding-left:0}.form-control-sm,.input-group-sm>.form-control,.input-group-sm>.input-group-append>.btn,.input-group-sm>.input-group-append>.input-group-text,.input-group-sm>.input-group-prepend>.btn,.input-group-sm>.input-group-prepend>.input-group-text{padding:.25rem .5rem;font-size:.7875rem;line-height:1.5;border-radius:.2rem}.input-group-sm>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-sm>select.form-control:not([size]):not([multiple]),select.form-control-sm:not([size]):not([multiple]){height:calc(1.68125rem + 2px)}.form-control-lg,.input-group-lg>.form-control,.input-group-lg>.input-group-append>.btn,.input-group-lg>.input-group-append>.input-group-text,.input-group-lg>.input-group-prepend>.btn,.input-group-lg>.input-group-prepend>.input-group-text{padding:.5rem 1rem;font-size:1.125rem;line-height:1.5;border-radius:.3rem}.input-group-lg>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-lg>select.form-control:not([size]):not([multiple]),select.form-control-lg:not([size]):not([multiple]){height:calc(2.6875rem + 2px)}.form-group{margin-bottom:1rem}.form-text{display:block;margin-top:.25rem}.form-row{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-5px;margin-left:-5px}.form-row>.col,.form-row>[class*=col-]{padding-right:5px;padding-left:5px}.form-check{position:relative;display:block;padding-left:1.25rem}.form-check-input{position:absolute;margin-top:.3rem;margin-left:-1.25rem}.form-check-input:disabled~.form-check-label{color:#6c757d}.form-check-label{margin-bottom:0}.form-check-inline{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-left:0;margin-right:.75rem}.form-check-inline .form-check-input{position:static;margin-top:0;margin-right:.3125rem;margin-left:0}.valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#38c172}.valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(56,193,114,.8);border-radius:.2rem}.custom-select.is-valid,.form-control.is-valid,.was-validated .custom-select:valid,.was-validated .form-control:valid{border-color:#38c172}.custom-select.is-valid:focus,.form-control.is-valid:focus,.was-validated .custom-select:valid:focus,.was-validated .form-control:valid:focus{border-color:#38c172;-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.25);box-shadow:0 0 0 .2rem rgba(56,193,114,.25)}.custom-select.is-valid~.valid-feedback,.custom-select.is-valid~.valid-tooltip,.form-control-file.is-valid~.valid-feedback,.form-control-file.is-valid~.valid-tooltip,.form-control.is-valid~.valid-feedback,.form-control.is-valid~.valid-tooltip,.was-validated .custom-select:valid~.valid-feedback,.was-validated .custom-select:valid~.valid-tooltip,.was-validated .form-control-file:valid~.valid-feedback,.was-validated .form-control-file:valid~.valid-tooltip,.was-validated .form-control:valid~.valid-feedback,.was-validated .form-control:valid~.valid-tooltip{display:block}.form-check-input.is-valid~.form-check-label,.was-validated .form-check-input:valid~.form-check-label{color:#38c172}.form-check-input.is-valid~.valid-feedback,.form-check-input.is-valid~.valid-tooltip,.was-validated .form-check-input:valid~.valid-feedback,.was-validated .form-check-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid~.custom-control-label,.was-validated .custom-control-input:valid~.custom-control-label{color:#38c172}.custom-control-input.is-valid~.custom-control-label:before,.was-validated .custom-control-input:valid~.custom-control-label:before{background-color:#98e1b7}.custom-control-input.is-valid~.valid-feedback,.custom-control-input.is-valid~.valid-tooltip,.was-validated .custom-control-input:valid~.valid-feedback,.was-validated .custom-control-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .custom-control-input:valid:checked~.custom-control-label:before{background-color:#5cd08d}.custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .custom-control-input:valid:focus~.custom-control-label:before{-webkit-box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(56,193,114,.25);box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(56,193,114,.25)}.custom-file-input.is-valid~.custom-file-label,.was-validated .custom-file-input:valid~.custom-file-label{border-color:#38c172}.custom-file-input.is-valid~.custom-file-label:before,.was-validated .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.custom-file-input.is-valid~.valid-feedback,.custom-file-input.is-valid~.valid-tooltip,.was-validated .custom-file-input:valid~.valid-feedback,.was-validated .custom-file-input:valid~.valid-tooltip{display:block}.custom-file-input.is-valid:focus~.custom-file-label,.was-validated .custom-file-input:valid:focus~.custom-file-label{-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.25);box-shadow:0 0 0 .2rem rgba(56,193,114,.25)}.invalid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#e3342f}.invalid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(227,52,47,.8);border-radius:.2rem}.custom-select.is-invalid,.form-control.is-invalid,.was-validated .custom-select:invalid,.was-validated .form-control:invalid{border-color:#e3342f}.custom-select.is-invalid:focus,.form-control.is-invalid:focus,.was-validated .custom-select:invalid:focus,.was-validated .form-control:invalid:focus{border-color:#e3342f;-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.25);box-shadow:0 0 0 .2rem rgba(227,52,47,.25)}.custom-select.is-invalid~.invalid-feedback,.custom-select.is-invalid~.invalid-tooltip,.form-control-file.is-invalid~.invalid-feedback,.form-control-file.is-invalid~.invalid-tooltip,.form-control.is-invalid~.invalid-feedback,.form-control.is-invalid~.invalid-tooltip,.was-validated .custom-select:invalid~.invalid-feedback,.was-validated .custom-select:invalid~.invalid-tooltip,.was-validated .form-control-file:invalid~.invalid-feedback,.was-validated .form-control-file:invalid~.invalid-tooltip,.was-validated .form-control:invalid~.invalid-feedback,.was-validated .form-control:invalid~.invalid-tooltip{display:block}.form-check-input.is-invalid~.form-check-label,.was-validated .form-check-input:invalid~.form-check-label{color:#e3342f}.form-check-input.is-invalid~.invalid-feedback,.form-check-input.is-invalid~.invalid-tooltip,.was-validated .form-check-input:invalid~.invalid-feedback,.was-validated .form-check-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid~.custom-control-label,.was-validated .custom-control-input:invalid~.custom-control-label{color:#e3342f}.custom-control-input.is-invalid~.custom-control-label:before,.was-validated .custom-control-input:invalid~.custom-control-label:before{background-color:#f2a29f}.custom-control-input.is-invalid~.invalid-feedback,.custom-control-input.is-invalid~.invalid-tooltip,.was-validated .custom-control-input:invalid~.invalid-feedback,.was-validated .custom-control-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid:checked~.custom-control-label:before,.was-validated .custom-control-input:invalid:checked~.custom-control-label:before{background-color:#e9605c}.custom-control-input.is-invalid:focus~.custom-control-label:before,.was-validated .custom-control-input:invalid:focus~.custom-control-label:before{-webkit-box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(227,52,47,.25);box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(227,52,47,.25)}.custom-file-input.is-invalid~.custom-file-label,.was-validated .custom-file-input:invalid~.custom-file-label{border-color:#e3342f}.custom-file-input.is-invalid~.custom-file-label:before,.was-validated .custom-file-input:invalid~.custom-file-label:before{border-color:inherit}.custom-file-input.is-invalid~.invalid-feedback,.custom-file-input.is-invalid~.invalid-tooltip,.was-validated .custom-file-input:invalid~.invalid-feedback,.was-validated .custom-file-input:invalid~.invalid-tooltip{display:block}.custom-file-input.is-invalid:focus~.custom-file-label,.was-validated .custom-file-input:invalid:focus~.custom-file-label{-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.25);box-shadow:0 0 0 .2rem rgba(227,52,47,.25)}.form-inline{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.form-inline .form-check{width:100%}@media (min-width:576px){.form-inline label{-ms-flex-align:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.form-inline .form-group,.form-inline label{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;align-items:center;margin-bottom:0}.form-inline .form-group{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap;-ms-flex-align:center}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-plaintext{display:inline-block}.form-inline .custom-select,.form-inline .input-group{width:auto}.form-inline .form-check{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:auto;padding-left:0}.form-inline .form-check-input{position:relative;margin-top:0;margin-right:.25rem;margin-left:0}.form-inline .custom-control{-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.form-inline .custom-control-label{margin-bottom:0}}.btn{display:inline-block;font-weight:400;text-align:center;white-space:nowrap;vertical-align:middle;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;border:1px solid transparent;padding:.375rem .75rem;font-size:.9rem;line-height:1.6;border-radius:.25rem;-webkit-transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out}@media screen and (prefers-reduced-motion:reduce){.btn{-webkit-transition:none;transition:none}}.btn:focus,.btn:hover{text-decoration:none}.btn.focus,.btn:focus{outline:0;-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 .2rem rgba(52,144,220,.25)}.btn.disabled,.btn:disabled{opacity:.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.btn:not(:disabled):not(.disabled).active,.btn:not(:disabled):not(.disabled):active{background-image:none}a.btn.disabled,fieldset:disabled a.btn{pointer-events:none}.btn-primary{color:#fff;background-color:#3490dc;border-color:#3490dc}.btn-primary:hover{color:#fff;background-color:#227dc7;border-color:#2176bd}.btn-primary.focus,.btn-primary:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.5);box-shadow:0 0 0 .2rem rgba(52,144,220,.5)}.btn-primary.disabled,.btn-primary:disabled{color:#fff;background-color:#3490dc;border-color:#3490dc}.btn-primary:not(:disabled):not(.disabled).active,.btn-primary:not(:disabled):not(.disabled):active,.show>.btn-primary.dropdown-toggle{color:#fff;background-color:#2176bd;border-color:#1f6fb2}.btn-primary:not(:disabled):not(.disabled).active:focus,.btn-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-primary.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.5);box-shadow:0 0 0 .2rem rgba(52,144,220,.5)}.btn-secondary{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-secondary:hover{color:#fff;background-color:#5a6268;border-color:#545b62}.btn-secondary.focus,.btn-secondary:focus{-webkit-box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5);box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-secondary.disabled,.btn-secondary:disabled{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-secondary:not(:disabled):not(.disabled).active,.btn-secondary:not(:disabled):not(.disabled):active,.show>.btn-secondary.dropdown-toggle{color:#fff;background-color:#545b62;border-color:#4e555b}.btn-secondary:not(:disabled):not(.disabled).active:focus,.btn-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-secondary.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5);box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-success{color:#fff;background-color:#38c172;border-color:#38c172}.btn-success:hover{color:#fff;background-color:#2fa360;border-color:#2d995b}.btn-success.focus,.btn-success:focus{-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.5);box-shadow:0 0 0 .2rem rgba(56,193,114,.5)}.btn-success.disabled,.btn-success:disabled{color:#fff;background-color:#38c172;border-color:#38c172}.btn-success:not(:disabled):not(.disabled).active,.btn-success:not(:disabled):not(.disabled):active,.show>.btn-success.dropdown-toggle{color:#fff;background-color:#2d995b;border-color:#2a9055}.btn-success:not(:disabled):not(.disabled).active:focus,.btn-success:not(:disabled):not(.disabled):active:focus,.show>.btn-success.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.5);box-shadow:0 0 0 .2rem rgba(56,193,114,.5)}.btn-info{color:#212529;background-color:#6cb2eb;border-color:#6cb2eb}.btn-info:hover{color:#fff;background-color:#4aa0e6;border-color:#3f9ae5}.btn-info.focus,.btn-info:focus{-webkit-box-shadow:0 0 0 .2rem rgba(108,178,235,.5);box-shadow:0 0 0 .2rem rgba(108,178,235,.5)}.btn-info.disabled,.btn-info:disabled{color:#212529;background-color:#6cb2eb;border-color:#6cb2eb}.btn-info:not(:disabled):not(.disabled).active,.btn-info:not(:disabled):not(.disabled):active,.show>.btn-info.dropdown-toggle{color:#fff;background-color:#3f9ae5;border-color:#3495e3}.btn-info:not(:disabled):not(.disabled).active:focus,.btn-info:not(:disabled):not(.disabled):active:focus,.show>.btn-info.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(108,178,235,.5);box-shadow:0 0 0 .2rem rgba(108,178,235,.5)}.btn-warning{color:#212529;background-color:#ffed4a;border-color:#ffed4a}.btn-warning:hover{color:#212529;background-color:#ffe924;border-color:#ffe817}.btn-warning.focus,.btn-warning:focus{-webkit-box-shadow:0 0 0 .2rem rgba(255,237,74,.5);box-shadow:0 0 0 .2rem rgba(255,237,74,.5)}.btn-warning.disabled,.btn-warning:disabled{color:#212529;background-color:#ffed4a;border-color:#ffed4a}.btn-warning:not(:disabled):not(.disabled).active,.btn-warning:not(:disabled):not(.disabled):active,.show>.btn-warning.dropdown-toggle{color:#212529;background-color:#ffe817;border-color:#ffe70a}.btn-warning:not(:disabled):not(.disabled).active:focus,.btn-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-warning.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(255,237,74,.5);box-shadow:0 0 0 .2rem rgba(255,237,74,.5)}.btn-danger{color:#fff;background-color:#e3342f;border-color:#e3342f}.btn-danger:hover{color:#fff;background-color:#d0211c;border-color:#c51f1a}.btn-danger.focus,.btn-danger:focus{-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.5);box-shadow:0 0 0 .2rem rgba(227,52,47,.5)}.btn-danger.disabled,.btn-danger:disabled{color:#fff;background-color:#e3342f;border-color:#e3342f}.btn-danger:not(:disabled):not(.disabled).active,.btn-danger:not(:disabled):not(.disabled):active,.show>.btn-danger.dropdown-toggle{color:#fff;background-color:#c51f1a;border-color:#b91d19}.btn-danger:not(:disabled):not(.disabled).active:focus,.btn-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-danger.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.5);box-shadow:0 0 0 .2rem rgba(227,52,47,.5)}.btn-light{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:hover{color:#212529;background-color:#e2e6ea;border-color:#dae0e5}.btn-light.focus,.btn-light:focus{-webkit-box-shadow:0 0 0 .2rem rgba(248,249,250,.5);box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-light.disabled,.btn-light:disabled{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:not(:disabled):not(.disabled).active,.btn-light:not(:disabled):not(.disabled):active,.show>.btn-light.dropdown-toggle{color:#212529;background-color:#dae0e5;border-color:#d3d9df}.btn-light:not(:disabled):not(.disabled).active:focus,.btn-light:not(:disabled):not(.disabled):active:focus,.show>.btn-light.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(248,249,250,.5);box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-dark{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:hover{color:#fff;background-color:#23272b;border-color:#1d2124}.btn-dark.focus,.btn-dark:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,58,64,.5);box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-dark.disabled,.btn-dark:disabled{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:not(:disabled):not(.disabled).active,.btn-dark:not(:disabled):not(.disabled):active,.show>.btn-dark.dropdown-toggle{color:#fff;background-color:#1d2124;border-color:#171a1d}.btn-dark:not(:disabled):not(.disabled).active:focus,.btn-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-dark.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,58,64,.5);box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-primary{color:#3490dc;background-color:transparent;background-image:none;border-color:#3490dc}.btn-outline-primary:hover{color:#fff;background-color:#3490dc;border-color:#3490dc}.btn-outline-primary.focus,.btn-outline-primary:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.5);box-shadow:0 0 0 .2rem rgba(52,144,220,.5)}.btn-outline-primary.disabled,.btn-outline-primary:disabled{color:#3490dc;background-color:transparent}.btn-outline-primary:not(:disabled):not(.disabled).active,.btn-outline-primary:not(:disabled):not(.disabled):active,.show>.btn-outline-primary.dropdown-toggle{color:#fff;background-color:#3490dc;border-color:#3490dc}.btn-outline-primary:not(:disabled):not(.disabled).active:focus,.btn-outline-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-primary.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.5);box-shadow:0 0 0 .2rem rgba(52,144,220,.5)}.btn-outline-secondary{color:#6c757d;background-color:transparent;background-image:none;border-color:#6c757d}.btn-outline-secondary:hover{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary.focus,.btn-outline-secondary:focus{-webkit-box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5);box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-outline-secondary.disabled,.btn-outline-secondary:disabled{color:#6c757d;background-color:transparent}.btn-outline-secondary:not(:disabled):not(.disabled).active,.btn-outline-secondary:not(:disabled):not(.disabled):active,.show>.btn-outline-secondary.dropdown-toggle{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary:not(:disabled):not(.disabled).active:focus,.btn-outline-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-secondary.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5);box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-outline-success{color:#38c172;background-color:transparent;background-image:none;border-color:#38c172}.btn-outline-success:hover{color:#fff;background-color:#38c172;border-color:#38c172}.btn-outline-success.focus,.btn-outline-success:focus{-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.5);box-shadow:0 0 0 .2rem rgba(56,193,114,.5)}.btn-outline-success.disabled,.btn-outline-success:disabled{color:#38c172;background-color:transparent}.btn-outline-success:not(:disabled):not(.disabled).active,.btn-outline-success:not(:disabled):not(.disabled):active,.show>.btn-outline-success.dropdown-toggle{color:#fff;background-color:#38c172;border-color:#38c172}.btn-outline-success:not(:disabled):not(.disabled).active:focus,.btn-outline-success:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-success.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(56,193,114,.5);box-shadow:0 0 0 .2rem rgba(56,193,114,.5)}.btn-outline-info{color:#6cb2eb;background-color:transparent;background-image:none;border-color:#6cb2eb}.btn-outline-info:hover{color:#212529;background-color:#6cb2eb;border-color:#6cb2eb}.btn-outline-info.focus,.btn-outline-info:focus{-webkit-box-shadow:0 0 0 .2rem rgba(108,178,235,.5);box-shadow:0 0 0 .2rem rgba(108,178,235,.5)}.btn-outline-info.disabled,.btn-outline-info:disabled{color:#6cb2eb;background-color:transparent}.btn-outline-info:not(:disabled):not(.disabled).active,.btn-outline-info:not(:disabled):not(.disabled):active,.show>.btn-outline-info.dropdown-toggle{color:#212529;background-color:#6cb2eb;border-color:#6cb2eb}.btn-outline-info:not(:disabled):not(.disabled).active:focus,.btn-outline-info:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-info.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(108,178,235,.5);box-shadow:0 0 0 .2rem rgba(108,178,235,.5)}.btn-outline-warning{color:#ffed4a;background-color:transparent;background-image:none;border-color:#ffed4a}.btn-outline-warning:hover{color:#212529;background-color:#ffed4a;border-color:#ffed4a}.btn-outline-warning.focus,.btn-outline-warning:focus{-webkit-box-shadow:0 0 0 .2rem rgba(255,237,74,.5);box-shadow:0 0 0 .2rem rgba(255,237,74,.5)}.btn-outline-warning.disabled,.btn-outline-warning:disabled{color:#ffed4a;background-color:transparent}.btn-outline-warning:not(:disabled):not(.disabled).active,.btn-outline-warning:not(:disabled):not(.disabled):active,.show>.btn-outline-warning.dropdown-toggle{color:#212529;background-color:#ffed4a;border-color:#ffed4a}.btn-outline-warning:not(:disabled):not(.disabled).active:focus,.btn-outline-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-warning.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(255,237,74,.5);box-shadow:0 0 0 .2rem rgba(255,237,74,.5)}.btn-outline-danger{color:#e3342f;background-color:transparent;background-image:none;border-color:#e3342f}.btn-outline-danger:hover{color:#fff;background-color:#e3342f;border-color:#e3342f}.btn-outline-danger.focus,.btn-outline-danger:focus{-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.5);box-shadow:0 0 0 .2rem rgba(227,52,47,.5)}.btn-outline-danger.disabled,.btn-outline-danger:disabled{color:#e3342f;background-color:transparent}.btn-outline-danger:not(:disabled):not(.disabled).active,.btn-outline-danger:not(:disabled):not(.disabled):active,.show>.btn-outline-danger.dropdown-toggle{color:#fff;background-color:#e3342f;border-color:#e3342f}.btn-outline-danger:not(:disabled):not(.disabled).active:focus,.btn-outline-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-danger.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(227,52,47,.5);box-shadow:0 0 0 .2rem rgba(227,52,47,.5)}.btn-outline-light{color:#f8f9fa;background-color:transparent;background-image:none;border-color:#f8f9fa}.btn-outline-light:hover{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light.focus,.btn-outline-light:focus{-webkit-box-shadow:0 0 0 .2rem rgba(248,249,250,.5);box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-light.disabled,.btn-outline-light:disabled{color:#f8f9fa;background-color:transparent}.btn-outline-light:not(:disabled):not(.disabled).active,.btn-outline-light:not(:disabled):not(.disabled):active,.show>.btn-outline-light.dropdown-toggle{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light:not(:disabled):not(.disabled).active:focus,.btn-outline-light:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-light.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(248,249,250,.5);box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-dark{color:#343a40;background-color:transparent;background-image:none;border-color:#343a40}.btn-outline-dark:hover{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark.focus,.btn-outline-dark:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,58,64,.5);box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-dark.disabled,.btn-outline-dark:disabled{color:#343a40;background-color:transparent}.btn-outline-dark:not(:disabled):not(.disabled).active,.btn-outline-dark:not(:disabled):not(.disabled):active,.show>.btn-outline-dark.dropdown-toggle{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark:not(:disabled):not(.disabled).active:focus,.btn-outline-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-dark.dropdown-toggle:focus{-webkit-box-shadow:0 0 0 .2rem rgba(52,58,64,.5);box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-link{font-weight:400;color:#3490dc;background-color:transparent}.btn-link:hover{color:#1d68a7;background-color:transparent}.btn-link.focus,.btn-link:focus,.btn-link:hover{text-decoration:underline;border-color:transparent}.btn-link.focus,.btn-link:focus{-webkit-box-shadow:none;box-shadow:none}.btn-link.disabled,.btn-link:disabled{color:#6c757d;pointer-events:none}.btn-group-lg>.btn,.btn-lg{padding:.5rem 1rem;font-size:1.125rem;line-height:1.5;border-radius:.3rem}.btn-group-sm>.btn,.btn-sm{padding:.25rem .5rem;font-size:.7875rem;line-height:1.5;border-radius:.2rem}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:.5rem}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}.fade{-webkit-transition:opacity .15s linear;transition:opacity .15s linear}@media screen and (prefers-reduced-motion:reduce){.fade{-webkit-transition:none;transition:none}}.fade:not(.show){opacity:0}.collapse:not(.show){display:none}.collapsing{position:relative;height:0;overflow:hidden;-webkit-transition:height .35s ease;transition:height .35s ease}@media screen and (prefers-reduced-motion:reduce){.collapsing{-webkit-transition:none;transition:none}}.dropdown,.dropleft,.dropright,.dropup{position:relative}.dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid;border-right:.3em solid transparent;border-bottom:0;border-left:.3em solid transparent}.dropdown-toggle:empty:after{margin-left:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:.5rem 0;margin:.125rem 0 0;font-size:.9rem;color:#212529;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.15);border-radius:.25rem}.dropdown-menu-right{right:0;left:auto}.dropup .dropdown-menu{top:auto;bottom:100%;margin-top:0;margin-bottom:.125rem}.dropup .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:0;border-right:.3em solid transparent;border-bottom:.3em solid;border-left:.3em solid transparent}.dropup .dropdown-toggle:empty:after{margin-left:0}.dropright .dropdown-menu{top:0;right:auto;left:100%;margin-top:0;margin-left:.125rem}.dropright .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:0;border-bottom:.3em solid transparent;border-left:.3em solid}.dropright .dropdown-toggle:empty:after{margin-left:0}.dropright .dropdown-toggle:after{vertical-align:0}.dropleft .dropdown-menu{top:0;right:100%;left:auto;margin-top:0;margin-right:.125rem}.dropleft .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";display:none}.dropleft .dropdown-toggle:before{display:inline-block;width:0;height:0;margin-right:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:.3em solid;border-bottom:.3em solid transparent}.dropleft .dropdown-toggle:empty:after{margin-left:0}.dropleft .dropdown-toggle:before{vertical-align:0}.dropdown-menu[x-placement^=bottom],.dropdown-menu[x-placement^=left],.dropdown-menu[x-placement^=right],.dropdown-menu[x-placement^=top]{right:auto;bottom:auto}.dropdown-divider{height:0;margin:.5rem 0;overflow:hidden;border-top:1px solid #e9ecef}.dropdown-item{display:block;width:100%;padding:.25rem 1.5rem;clear:both;font-weight:400;color:#212529;text-align:inherit;white-space:nowrap;background-color:transparent;border:0}.dropdown-item:focus,.dropdown-item:hover{color:#16181b;text-decoration:none;background-color:#f8f9fa}.dropdown-item.active,.dropdown-item:active{color:#fff;text-decoration:none;background-color:#3490dc}.dropdown-item.disabled,.dropdown-item:disabled{color:#6c757d;background-color:transparent}.dropdown-menu.show{display:block}.dropdown-header{display:block;padding:.5rem 1.5rem;margin-bottom:0;font-size:.7875rem;color:#6c757d;white-space:nowrap}.dropdown-item-text{display:block;padding:.25rem 1.5rem;color:#212529}.btn-group,.btn-group-vertical{position:relative;display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto}.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group-vertical>.btn:hover,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus,.btn-group>.btn:hover{z-index:1}.btn-group-vertical .btn+.btn,.btn-group-vertical .btn+.btn-group,.btn-group-vertical .btn-group+.btn,.btn-group-vertical .btn-group+.btn-group,.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.btn-toolbar .input-group{width:auto}.btn-group>.btn:first-child{margin-left:0}.btn-group>.btn-group:not(:last-child)>.btn,.btn-group>.btn:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn-group:not(:first-child)>.btn,.btn-group>.btn:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.dropdown-toggle-split{padding-right:.5625rem;padding-left:.5625rem}.dropdown-toggle-split:after,.dropright .dropdown-toggle-split:after,.dropup .dropdown-toggle-split:after{margin-left:0}.dropleft .dropdown-toggle-split:before{margin-right:0}.btn-group-sm>.btn+.dropdown-toggle-split,.btn-sm+.dropdown-toggle-split{padding-right:.375rem;padding-left:.375rem}.btn-group-lg>.btn+.dropdown-toggle-split,.btn-lg+.dropdown-toggle-split{padding-right:.75rem;padding-left:.75rem}.btn-group-vertical{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.btn-group-vertical .btn,.btn-group-vertical .btn-group{width:100%}.btn-group-vertical>.btn+.btn,.btn-group-vertical>.btn+.btn-group,.btn-group-vertical>.btn-group+.btn,.btn-group-vertical>.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical>.btn-group:not(:last-child)>.btn,.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:not(:first-child)>.btn,.btn-group-vertical>.btn:not(:first-child){border-top-left-radius:0;border-top-right-radius:0}.btn-group-toggle>.btn,.btn-group-toggle>.btn-group>.btn{margin-bottom:0}.btn-group-toggle>.btn-group>.btn input[type=checkbox],.btn-group-toggle>.btn-group>.btn input[type=radio],.btn-group-toggle>.btn input[type=checkbox],.btn-group-toggle>.btn input[type=radio]{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.input-group{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;width:100%}.input-group>.custom-file,.input-group>.custom-select,.input-group>.form-control{position:relative;-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;width:1%;margin-bottom:0}.input-group>.custom-file+.custom-file,.input-group>.custom-file+.custom-select,.input-group>.custom-file+.form-control,.input-group>.custom-select+.custom-file,.input-group>.custom-select+.custom-select,.input-group>.custom-select+.form-control,.input-group>.form-control+.custom-file,.input-group>.form-control+.custom-select,.input-group>.form-control+.form-control{margin-left:-1px}.input-group>.custom-file .custom-file-input:focus~.custom-file-label,.input-group>.custom-select:focus,.input-group>.form-control:focus{z-index:3}.input-group>.custom-select:not(:last-child),.input-group>.form-control:not(:last-child){border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-select:not(:first-child),.input-group>.form-control:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.input-group>.custom-file{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.input-group>.custom-file:not(:last-child) .custom-file-label,.input-group>.custom-file:not(:last-child) .custom-file-label:after{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-file:not(:first-child) .custom-file-label{border-top-left-radius:0;border-bottom-left-radius:0}.input-group-append,.input-group-prepend{display:-webkit-box;display:-ms-flexbox;display:flex}.input-group-append .btn,.input-group-prepend .btn{position:relative;z-index:2}.input-group-append .btn+.btn,.input-group-append .btn+.input-group-text,.input-group-append .input-group-text+.btn,.input-group-append .input-group-text+.input-group-text,.input-group-prepend .btn+.btn,.input-group-prepend .btn+.input-group-text,.input-group-prepend .input-group-text+.btn,.input-group-prepend .input-group-text+.input-group-text{margin-left:-1px}.input-group-prepend{margin-right:-1px}.input-group-append{margin-left:-1px}.input-group-text{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:.375rem .75rem;margin-bottom:0;font-size:.9rem;font-weight:400;line-height:1.6;color:#495057;text-align:center;white-space:nowrap;background-color:#e9ecef;border:1px solid #ced4da;border-radius:.25rem}.input-group-text input[type=checkbox],.input-group-text input[type=radio]{margin-top:0}.input-group>.input-group-append:last-child>.btn:not(:last-child):not(.dropdown-toggle),.input-group>.input-group-append:last-child>.input-group-text:not(:last-child),.input-group>.input-group-append:not(:last-child)>.btn,.input-group>.input-group-append:not(:last-child)>.input-group-text,.input-group>.input-group-prepend>.btn,.input-group>.input-group-prepend>.input-group-text{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.input-group-append>.btn,.input-group>.input-group-append>.input-group-text,.input-group>.input-group-prepend:first-child>.btn:not(:first-child),.input-group>.input-group-prepend:first-child>.input-group-text:not(:first-child),.input-group>.input-group-prepend:not(:first-child)>.btn,.input-group>.input-group-prepend:not(:first-child)>.input-group-text{border-top-left-radius:0;border-bottom-left-radius:0}.custom-control{position:relative;display:block;min-height:1.6rem;padding-left:1.5rem}.custom-control-inline{display:-webkit-inline-box;display:-ms-inline-flexbox;display:inline-flex;margin-right:1rem}.custom-control-input{position:absolute;z-index:-1;opacity:0}.custom-control-input:checked~.custom-control-label:before{color:#fff;background-color:#3490dc}.custom-control-input:focus~.custom-control-label:before{-webkit-box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25)}.custom-control-input:active~.custom-control-label:before{color:#fff;background-color:#cce3f6}.custom-control-input:disabled~.custom-control-label{color:#6c757d}.custom-control-input:disabled~.custom-control-label:before{background-color:#e9ecef}.custom-control-label{position:relative;margin-bottom:0}.custom-control-label:before{pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:#dee2e6}.custom-control-label:after,.custom-control-label:before{position:absolute;top:.3rem;left:-1.5rem;display:block;width:1rem;height:1rem;content:""}.custom-control-label:after{background-repeat:no-repeat;background-position:50%;background-size:50% 50%}.custom-checkbox .custom-control-label:before{border-radius:.25rem}.custom-checkbox .custom-control-input:checked~.custom-control-label:before{background-color:#3490dc}.custom-checkbox .custom-control-input:checked~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E%3Cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label:before{background-color:#3490dc}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3E%3Cpath stroke='%23fff' d='M0 2h4'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:disabled:checked~.custom-control-label:before{background-color:rgba(52,144,220,.5)}.custom-checkbox .custom-control-input:disabled:indeterminate~.custom-control-label:before{background-color:rgba(52,144,220,.5)}.custom-radio .custom-control-label:before{border-radius:50%}.custom-radio .custom-control-input:checked~.custom-control-label:before{background-color:#3490dc}.custom-radio .custom-control-input:checked~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3E%3Ccircle r='3' fill='%23fff'/%3E%3C/svg%3E")}.custom-radio .custom-control-input:disabled:checked~.custom-control-label:before{background-color:rgba(52,144,220,.5)}.custom-select{display:inline-block;width:100%;height:calc(2.19rem + 2px);padding:.375rem 1.75rem .375rem .75rem;line-height:1.6;color:#495057;vertical-align:middle;background:#fff url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") no-repeat right .75rem center;background-size:8px 10px;border:1px solid #ced4da;border-radius:.25rem;-webkit-appearance:none;-moz-appearance:none;appearance:none}.custom-select:focus{border-color:#a1cbef;outline:0;-webkit-box-shadow:0 0 0 .2rem rgba(161,203,239,.5);box-shadow:0 0 0 .2rem rgba(161,203,239,.5)}.custom-select:focus::-ms-value{color:#495057;background-color:#fff}.custom-select[multiple],.custom-select[size]:not([size="1"]){height:auto;padding-right:.75rem;background-image:none}.custom-select:disabled{color:#6c757d;background-color:#e9ecef}.custom-select::-ms-expand{opacity:0}.custom-select-sm{height:calc(1.68125rem + 2px);font-size:75%}.custom-select-lg,.custom-select-sm{padding-top:.375rem;padding-bottom:.375rem}.custom-select-lg{height:calc(2.6875rem + 2px);font-size:125%}.custom-file{display:inline-block;margin-bottom:0}.custom-file,.custom-file-input{position:relative;width:100%;height:calc(2.19rem + 2px)}.custom-file-input{z-index:2;margin:0;opacity:0}.custom-file-input:focus~.custom-file-label{border-color:#a1cbef;-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 .2rem rgba(52,144,220,.25)}.custom-file-input:focus~.custom-file-label:after{border-color:#a1cbef}.custom-file-input:disabled~.custom-file-label{background-color:#e9ecef}.custom-file-input:lang(en)~.custom-file-label:after{content:"Browse"}.custom-file-label{left:0;z-index:1;height:calc(2.19rem + 2px);background-color:#fff;border:1px solid #ced4da;border-radius:.25rem}.custom-file-label,.custom-file-label:after{position:absolute;top:0;right:0;padding:.375rem .75rem;line-height:1.6;color:#495057}.custom-file-label:after{bottom:0;z-index:3;display:block;height:2.19rem;content:"Browse";background-color:#e9ecef;border-left:1px solid #ced4da;border-radius:0 .25rem .25rem 0}.custom-range{width:100%;padding-left:0;background-color:transparent;-webkit-appearance:none;-moz-appearance:none;appearance:none}.custom-range:focus{outline:none}.custom-range::-moz-focus-outer{border:0}.custom-range::-webkit-slider-thumb{width:1rem;height:1rem;margin-top:-.25rem;background-color:#3490dc;border:0;border-radius:1rem;-webkit-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;-webkit-appearance:none;appearance:none}@media screen and (prefers-reduced-motion:reduce){.custom-range::-webkit-slider-thumb{-webkit-transition:none;transition:none}}.custom-range::-webkit-slider-thumb:focus{outline:none;-webkit-box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25)}.custom-range::-webkit-slider-thumb:active{background-color:#cce3f6}.custom-range::-webkit-slider-runnable-track{width:100%;height:.5rem;color:transparent;cursor:pointer;background-color:#dee2e6;border-color:transparent;border-radius:1rem}.custom-range::-moz-range-thumb{width:1rem;height:1rem;background-color:#3490dc;border:0;border-radius:1rem;-webkit-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;-moz-appearance:none;appearance:none}@media screen and (prefers-reduced-motion:reduce){.custom-range::-moz-range-thumb{-webkit-transition:none;transition:none}}.custom-range::-moz-range-thumb:focus{outline:none;box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25)}.custom-range::-moz-range-thumb:active{background-color:#cce3f6}.custom-range::-moz-range-track{width:100%;height:.5rem;color:transparent;cursor:pointer;background-color:#dee2e6;border-color:transparent;border-radius:1rem}.custom-range::-ms-thumb{width:1rem;height:1rem;background-color:#3490dc;border:0;border-radius:1rem;-webkit-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;appearance:none}@media screen and (prefers-reduced-motion:reduce){.custom-range::-ms-thumb{-webkit-transition:none;transition:none}}.custom-range::-ms-thumb:focus{outline:none;box-shadow:0 0 0 1px #f8fafc,0 0 0 .2rem rgba(52,144,220,.25)}.custom-range::-ms-thumb:active{background-color:#cce3f6}.custom-range::-ms-track{width:100%;height:.5rem;color:transparent;cursor:pointer;background-color:transparent;border-color:transparent;border-width:.5rem}.custom-range::-ms-fill-lower,.custom-range::-ms-fill-upper{background-color:#dee2e6;border-radius:1rem}.custom-range::-ms-fill-upper{margin-right:15px}.custom-control-label:before,.custom-file-label,.custom-select{-webkit-transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,-webkit-box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;transition:background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out,-webkit-box-shadow .15s ease-in-out}@media screen and (prefers-reduced-motion:reduce){.custom-control-label:before,.custom-file-label,.custom-select{-webkit-transition:none;transition:none}}.nav{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.nav-link{display:block;padding:.5rem 1rem}.nav-link:focus,.nav-link:hover{text-decoration:none}.nav-link.disabled{color:#6c757d}.nav-tabs{border-bottom:1px solid #dee2e6}.nav-tabs .nav-item{margin-bottom:-1px}.nav-tabs .nav-link{border:1px solid transparent;border-top-left-radius:.25rem;border-top-right-radius:.25rem}.nav-tabs .nav-link:focus,.nav-tabs .nav-link:hover{border-color:#e9ecef #e9ecef #dee2e6}.nav-tabs .nav-link.disabled{color:#6c757d;background-color:transparent;border-color:transparent}.nav-tabs .nav-item.show .nav-link,.nav-tabs .nav-link.active{color:#495057;background-color:#f8fafc;border-color:#dee2e6 #dee2e6 #f8fafc}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-left-radius:0;border-top-right-radius:0}.nav-pills .nav-link{border-radius:.25rem}.nav-pills .nav-link.active,.nav-pills .show>.nav-link{color:#fff;background-color:#3490dc}.nav-fill .nav-item{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;text-align:center}.nav-justified .nav-item{-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;text-align:center}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.navbar{position:relative;padding:.5rem 1rem}.navbar,.navbar>.container,.navbar>.container-fluid{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.navbar-brand{display:inline-block;padding-top:.32rem;padding-bottom:.32rem;margin-right:1rem;font-size:1.125rem;line-height:inherit;white-space:nowrap}.navbar-brand:focus,.navbar-brand:hover{text-decoration:none}.navbar-nav{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .nav-link{padding-right:0;padding-left:0}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-text{display:inline-block;padding-top:.5rem;padding-bottom:.5rem}.navbar-collapse{-ms-flex-preferred-size:100%;flex-basis:100%;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.navbar-toggler{padding:.25rem .75rem;font-size:1.125rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:.25rem}.navbar-toggler:focus,.navbar-toggler:hover{text-decoration:none}.navbar-toggler:not(:disabled):not(.disabled){cursor:pointer}.navbar-toggler-icon{display:inline-block;width:1.5em;height:1.5em;vertical-align:middle;content:"";background:no-repeat 50%;background-size:100% 100%}@media (max-width:575.98px){.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:576px){.navbar-expand-sm{-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.navbar-expand-sm,.navbar-expand-sm .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal}.navbar-expand-sm .navbar-nav{-ms-flex-direction:row;flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}@media (max-width:767.98px){.navbar-expand-md>.container,.navbar-expand-md>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:768px){.navbar-expand-md{-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.navbar-expand-md,.navbar-expand-md .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal}.navbar-expand-md .navbar-nav{-ms-flex-direction:row;flex-direction:row}.navbar-expand-md .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-md .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-md>.container,.navbar-expand-md>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.navbar-expand-md .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}.navbar-expand-md .navbar-toggler{display:none}}@media (max-width:991.98px){.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:992px){.navbar-expand-lg{-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.navbar-expand-lg,.navbar-expand-lg .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal}.navbar-expand-lg .navbar-nav{-ms-flex-direction:row;flex-direction:row}.navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-lg .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.navbar-expand-lg .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}.navbar-expand-lg .navbar-toggler{display:none}}@media (max-width:1199.98px){.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:1200px){.navbar-expand-xl{-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.navbar-expand-xl,.navbar-expand-xl .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal}.navbar-expand-xl .navbar-nav{-ms-flex-direction:row;flex-direction:row}.navbar-expand-xl .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-xl .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.navbar-expand-xl .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}.navbar-expand-xl .navbar-toggler{display:none}}.navbar-expand{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.navbar-expand>.container,.navbar-expand>.container-fluid{padding-right:0;padding-left:0}.navbar-expand .navbar-nav{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-direction:row;flex-direction:row}.navbar-expand .navbar-nav .dropdown-menu{position:absolute}.navbar-expand .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand>.container,.navbar-expand>.container-fluid{-ms-flex-wrap:nowrap;flex-wrap:nowrap}.navbar-expand .navbar-collapse{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important;-ms-flex-preferred-size:auto;flex-basis:auto}.navbar-expand .navbar-toggler{display:none}.navbar-light .navbar-brand,.navbar-light .navbar-brand:focus,.navbar-light .navbar-brand:hover{color:rgba(0,0,0,.9)}.navbar-light .navbar-nav .nav-link{color:rgba(0,0,0,.5)}.navbar-light .navbar-nav .nav-link:focus,.navbar-light .navbar-nav .nav-link:hover{color:rgba(0,0,0,.7)}.navbar-light .navbar-nav .nav-link.disabled{color:rgba(0,0,0,.3)}.navbar-light .navbar-nav .active>.nav-link,.navbar-light .navbar-nav .nav-link.active,.navbar-light .navbar-nav .nav-link.show,.navbar-light .navbar-nav .show>.nav-link{color:rgba(0,0,0,.9)}.navbar-light .navbar-toggler{color:rgba(0,0,0,.5);border-color:rgba(0,0,0,.1)}.navbar-light .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}.navbar-light .navbar-text{color:rgba(0,0,0,.5)}.navbar-light .navbar-text a,.navbar-light .navbar-text a:focus,.navbar-light .navbar-text a:hover{color:rgba(0,0,0,.9)}.navbar-dark .navbar-brand,.navbar-dark .navbar-brand:focus,.navbar-dark .navbar-brand:hover{color:#fff}.navbar-dark .navbar-nav .nav-link{color:hsla(0,0%,100%,.5)}.navbar-dark .navbar-nav .nav-link:focus,.navbar-dark .navbar-nav .nav-link:hover{color:hsla(0,0%,100%,.75)}.navbar-dark .navbar-nav .nav-link.disabled{color:hsla(0,0%,100%,.25)}.navbar-dark .navbar-nav .active>.nav-link,.navbar-dark .navbar-nav .nav-link.active,.navbar-dark .navbar-nav .nav-link.show,.navbar-dark .navbar-nav .show>.nav-link{color:#fff}.navbar-dark .navbar-toggler{color:hsla(0,0%,100%,.5);border-color:hsla(0,0%,100%,.1)}.navbar-dark .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}.navbar-dark .navbar-text{color:hsla(0,0%,100%,.5)}.navbar-dark .navbar-text a,.navbar-dark .navbar-text a:focus,.navbar-dark .navbar-text a:hover{color:#fff}.card{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;min-width:0;word-wrap:break-word;background-color:#fff;background-clip:border-box;border:1px solid rgba(0,0,0,.125);border-radius:.25rem}.card>hr{margin-right:0;margin-left:0}.card>.list-group:first-child .list-group-item:first-child{border-top-left-radius:.25rem;border-top-right-radius:.25rem}.card>.list-group:last-child .list-group-item:last-child{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}.card-body{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;padding:1.25rem}.card-title{margin-bottom:.75rem}.card-subtitle{margin-top:-.375rem}.card-subtitle,.card-text:last-child{margin-bottom:0}.card-link:hover{text-decoration:none}.card-link+.card-link{margin-left:1.25rem}.card-header{padding:.75rem 1.25rem;margin-bottom:0;background-color:rgba(0,0,0,.03);border-bottom:1px solid rgba(0,0,0,.125)}.card-header:first-child{border-radius:calc(.25rem - 1px) calc(.25rem - 1px) 0 0}.card-header+.list-group .list-group-item:first-child{border-top:0}.card-footer{padding:.75rem 1.25rem;background-color:rgba(0,0,0,.03);border-top:1px solid rgba(0,0,0,.125)}.card-footer:last-child{border-radius:0 0 calc(.25rem - 1px) calc(.25rem - 1px)}.card-header-tabs{margin-bottom:-.75rem;border-bottom:0}.card-header-pills,.card-header-tabs{margin-right:-.625rem;margin-left:-.625rem}.card-img-overlay{position:absolute;top:0;right:0;bottom:0;left:0;padding:1.25rem}.card-img{width:100%;border-radius:calc(.25rem - 1px)}.card-img-top{width:100%;border-top-left-radius:calc(.25rem - 1px);border-top-right-radius:calc(.25rem - 1px)}.card-img-bottom{width:100%;border-bottom-right-radius:calc(.25rem - 1px);border-bottom-left-radius:calc(.25rem - 1px)}.card-deck{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.card-deck .card{margin-bottom:15px}@media (min-width:576px){.card-deck{-webkit-box-orient:horizontal;-ms-flex-flow:row wrap;flex-flow:row wrap;margin-right:-15px;margin-left:-15px}.card-deck,.card-deck .card{-webkit-box-direction:normal}.card-deck .card{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-flex:1;-ms-flex:1 0 0%;flex:1 0 0%;-webkit-box-orient:vertical;-ms-flex-direction:column;flex-direction:column;margin-right:15px;margin-bottom:0;margin-left:15px}}.card-group{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.card-group>.card{margin-bottom:15px}@media (min-width:576px){.card-group{-webkit-box-orient:horizontal;-webkit-box-direction:normal;-ms-flex-flow:row wrap;flex-flow:row wrap}.card-group>.card{-webkit-box-flex:1;-ms-flex:1 0 0%;flex:1 0 0%;margin-bottom:0}.card-group>.card+.card{margin-left:0;border-left:0}.card-group>.card:first-child{border-top-right-radius:0;border-bottom-right-radius:0}.card-group>.card:first-child .card-header,.card-group>.card:first-child .card-img-top{border-top-right-radius:0}.card-group>.card:first-child .card-footer,.card-group>.card:first-child .card-img-bottom{border-bottom-right-radius:0}.card-group>.card:last-child{border-top-left-radius:0;border-bottom-left-radius:0}.card-group>.card:last-child .card-header,.card-group>.card:last-child .card-img-top{border-top-left-radius:0}.card-group>.card:last-child .card-footer,.card-group>.card:last-child .card-img-bottom{border-bottom-left-radius:0}.card-group>.card:only-child{border-radius:.25rem}.card-group>.card:only-child .card-header,.card-group>.card:only-child .card-img-top{border-top-left-radius:.25rem;border-top-right-radius:.25rem}.card-group>.card:only-child .card-footer,.card-group>.card:only-child .card-img-bottom{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}.card-group>.card:not(:first-child):not(:last-child):not(:only-child),.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-footer,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-header,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-top{border-radius:0}}.card-columns .card{margin-bottom:.75rem}@media (min-width:576px){.card-columns{-webkit-column-count:3;column-count:3;-webkit-column-gap:1.25rem;column-gap:1.25rem;orphans:1;widows:1}.card-columns .card{display:inline-block;width:100%}}.accordion .card:not(:first-of-type):not(:last-of-type){border-bottom:0;border-radius:0}.accordion .card:not(:first-of-type) .card-header:first-child{border-radius:0}.accordion .card:first-of-type{border-bottom:0;border-bottom-right-radius:0;border-bottom-left-radius:0}.accordion .card:last-of-type{border-top-left-radius:0;border-top-right-radius:0}.breadcrumb{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;padding:.75rem 1rem;margin-bottom:1rem;list-style:none;background-color:#e9ecef;border-radius:.25rem}.breadcrumb-item+.breadcrumb-item{padding-left:.5rem}.breadcrumb-item+.breadcrumb-item:before{display:inline-block;padding-right:.5rem;color:#6c757d;content:"/"}.breadcrumb-item+.breadcrumb-item:hover:before{text-decoration:underline;text-decoration:none}.breadcrumb-item.active{color:#6c757d}.pagination{display:-webkit-box;display:-ms-flexbox;display:flex;padding-left:0;list-style:none;border-radius:.25rem}.page-link{position:relative;display:block;padding:.5rem .75rem;margin-left:-1px;line-height:1.25;color:#3490dc;background-color:#fff;border:1px solid #dee2e6}.page-link:hover{z-index:2;color:#1d68a7;text-decoration:none;background-color:#e9ecef;border-color:#dee2e6}.page-link:focus{z-index:2;outline:0;-webkit-box-shadow:0 0 0 .2rem rgba(52,144,220,.25);box-shadow:0 0 0 .2rem rgba(52,144,220,.25)}.page-link:not(:disabled):not(.disabled){cursor:pointer}.page-item:first-child .page-link{margin-left:0;border-top-left-radius:.25rem;border-bottom-left-radius:.25rem}.page-item:last-child .page-link{border-top-right-radius:.25rem;border-bottom-right-radius:.25rem}.page-item.active .page-link{z-index:1;color:#fff;background-color:#3490dc;border-color:#3490dc}.page-item.disabled .page-link{color:#6c757d;pointer-events:none;cursor:auto;background-color:#fff;border-color:#dee2e6}.pagination-lg .page-link{padding:.75rem 1.5rem;font-size:1.125rem;line-height:1.5}.pagination-lg .page-item:first-child .page-link{border-top-left-radius:.3rem;border-bottom-left-radius:.3rem}.pagination-lg .page-item:last-child .page-link{border-top-right-radius:.3rem;border-bottom-right-radius:.3rem}.pagination-sm .page-link{padding:.25rem .5rem;font-size:.7875rem;line-height:1.5}.pagination-sm .page-item:first-child .page-link{border-top-left-radius:.2rem;border-bottom-left-radius:.2rem}.pagination-sm .page-item:last-child .page-link{border-top-right-radius:.2rem;border-bottom-right-radius:.2rem}.badge{display:inline-block;padding:.25em .4em;font-size:75%;font-weight:700;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:.6em;padding-left:.6em;border-radius:10rem}.badge-primary{color:#fff;background-color:#3490dc}.badge-primary[href]:focus,.badge-primary[href]:hover{color:#fff;text-decoration:none;background-color:#2176bd}.badge-secondary{color:#fff;background-color:#6c757d}.badge-secondary[href]:focus,.badge-secondary[href]:hover{color:#fff;text-decoration:none;background-color:#545b62}.badge-success{color:#fff;background-color:#38c172}.badge-success[href]:focus,.badge-success[href]:hover{color:#fff;text-decoration:none;background-color:#2d995b}.badge-info{color:#212529;background-color:#6cb2eb}.badge-info[href]:focus,.badge-info[href]:hover{color:#212529;text-decoration:none;background-color:#3f9ae5}.badge-warning{color:#212529;background-color:#ffed4a}.badge-warning[href]:focus,.badge-warning[href]:hover{color:#212529;text-decoration:none;background-color:#ffe817}.badge-danger{color:#fff;background-color:#e3342f}.badge-danger[href]:focus,.badge-danger[href]:hover{color:#fff;text-decoration:none;background-color:#c51f1a}.badge-light{color:#212529;background-color:#f8f9fa}.badge-light[href]:focus,.badge-light[href]:hover{color:#212529;text-decoration:none;background-color:#dae0e5}.badge-dark{color:#fff;background-color:#343a40}.badge-dark[href]:focus,.badge-dark[href]:hover{color:#fff;text-decoration:none;background-color:#1d2124}.jumbotron{padding:2rem 1rem;margin-bottom:2rem;background-color:#e9ecef;border-radius:.3rem}@media (min-width:576px){.jumbotron{padding:4rem 2rem}}.jumbotron-fluid{padding-right:0;padding-left:0;border-radius:0}.alert{position:relative;padding:.75rem 1.25rem;margin-bottom:1rem;border:1px solid transparent;border-radius:.25rem}.alert-heading{color:inherit}.alert-link{font-weight:700}.alert-dismissible{padding-right:3.85rem}.alert-dismissible .close{position:absolute;top:0;right:0;padding:.75rem 1.25rem;color:inherit}.alert-primary{color:#1b4b72;background-color:#d6e9f8;border-color:#c6e0f5}.alert-primary hr{border-top-color:#b0d4f1}.alert-primary .alert-link{color:#113049}.alert-secondary{color:#383d41;background-color:#e2e3e5;border-color:#d6d8db}.alert-secondary hr{border-top-color:#c8cbcf}.alert-secondary .alert-link{color:#202326}.alert-success{color:#1d643b;background-color:#d7f3e3;border-color:#c7eed8}.alert-success hr{border-top-color:#b3e8ca}.alert-success .alert-link{color:#123c24}.alert-info{color:#385d7a;background-color:#e2f0fb;border-color:#d6e9f9}.alert-info hr{border-top-color:#c0ddf6}.alert-info .alert-link{color:#284257}.alert-warning{color:#857b26;background-color:#fffbdb;border-color:#fffacc}.alert-warning hr{border-top-color:#fff8b3}.alert-warning .alert-link{color:#5d561b}.alert-danger{color:#761b18;background-color:#f9d6d5;border-color:#f7c6c5}.alert-danger hr{border-top-color:#f4b0af}.alert-danger .alert-link{color:#4c110f}.alert-light{color:#818182;background-color:#fefefe;border-color:#fdfdfe}.alert-light hr{border-top-color:#ececf6}.alert-light .alert-link{color:#686868}.alert-dark{color:#1b1e21;background-color:#d6d8d9;border-color:#c6c8ca}.alert-dark hr{border-top-color:#b9bbbe}.alert-dark .alert-link{color:#040505}@-webkit-keyframes progress-bar-stripes{0%{background-position:1rem 0}to{background-position:0 0}}@keyframes progress-bar-stripes{0%{background-position:1rem 0}to{background-position:0 0}}.progress{height:1rem;overflow:hidden;font-size:.675rem;background-color:#e9ecef;border-radius:.25rem}.progress,.progress-bar{display:-webkit-box;display:-ms-flexbox;display:flex}.progress-bar{-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;color:#fff;text-align:center;white-space:nowrap;background-color:#3490dc;-webkit-transition:width .6s ease;transition:width .6s ease}@media screen and (prefers-reduced-motion:reduce){.progress-bar{-webkit-transition:none;transition:none}}.progress-bar-striped{background-image:linear-gradient(45deg,hsla(0,0%,100%,.15) 25%,transparent 0,transparent 50%,hsla(0,0%,100%,.15) 0,hsla(0,0%,100%,.15) 75%,transparent 0,transparent);background-size:1rem 1rem}.progress-bar-animated{-webkit-animation:progress-bar-stripes 1s linear infinite;animation:progress-bar-stripes 1s linear infinite}.media{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start}.media-body{-webkit-box-flex:1;-ms-flex:1;flex:1}.list-group{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;padding-left:0;margin-bottom:0}.list-group-item-action{width:100%;color:#495057;text-align:inherit}.list-group-item-action:focus,.list-group-item-action:hover{color:#495057;text-decoration:none;background-color:#f8f9fa}.list-group-item-action:active{color:#212529;background-color:#e9ecef}.list-group-item{position:relative;display:block;padding:.75rem 1.25rem;margin-bottom:-1px;background-color:#fff;border:1px solid rgba(0,0,0,.125)}.list-group-item:first-child{border-top-left-radius:.25rem;border-top-right-radius:.25rem}.list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}.list-group-item:focus,.list-group-item:hover{z-index:1;text-decoration:none}.list-group-item.disabled,.list-group-item:disabled{color:#6c757d;background-color:#fff}.list-group-item.active{z-index:2;color:#fff;background-color:#3490dc;border-color:#3490dc}.list-group-flush .list-group-item{border-right:0;border-left:0;border-radius:0}.list-group-flush:first-child .list-group-item:first-child{border-top:0}.list-group-flush:last-child .list-group-item:last-child{border-bottom:0}.list-group-item-primary{color:#1b4b72;background-color:#c6e0f5}.list-group-item-primary.list-group-item-action:focus,.list-group-item-primary.list-group-item-action:hover{color:#1b4b72;background-color:#b0d4f1}.list-group-item-primary.list-group-item-action.active{color:#fff;background-color:#1b4b72;border-color:#1b4b72}.list-group-item-secondary{color:#383d41;background-color:#d6d8db}.list-group-item-secondary.list-group-item-action:focus,.list-group-item-secondary.list-group-item-action:hover{color:#383d41;background-color:#c8cbcf}.list-group-item-secondary.list-group-item-action.active{color:#fff;background-color:#383d41;border-color:#383d41}.list-group-item-success{color:#1d643b;background-color:#c7eed8}.list-group-item-success.list-group-item-action:focus,.list-group-item-success.list-group-item-action:hover{color:#1d643b;background-color:#b3e8ca}.list-group-item-success.list-group-item-action.active{color:#fff;background-color:#1d643b;border-color:#1d643b}.list-group-item-info{color:#385d7a;background-color:#d6e9f9}.list-group-item-info.list-group-item-action:focus,.list-group-item-info.list-group-item-action:hover{color:#385d7a;background-color:#c0ddf6}.list-group-item-info.list-group-item-action.active{color:#fff;background-color:#385d7a;border-color:#385d7a}.list-group-item-warning{color:#857b26;background-color:#fffacc}.list-group-item-warning.list-group-item-action:focus,.list-group-item-warning.list-group-item-action:hover{color:#857b26;background-color:#fff8b3}.list-group-item-warning.list-group-item-action.active{color:#fff;background-color:#857b26;border-color:#857b26}.list-group-item-danger{color:#761b18;background-color:#f7c6c5}.list-group-item-danger.list-group-item-action:focus,.list-group-item-danger.list-group-item-action:hover{color:#761b18;background-color:#f4b0af}.list-group-item-danger.list-group-item-action.active{color:#fff;background-color:#761b18;border-color:#761b18}.list-group-item-light{color:#818182;background-color:#fdfdfe}.list-group-item-light.list-group-item-action:focus,.list-group-item-light.list-group-item-action:hover{color:#818182;background-color:#ececf6}.list-group-item-light.list-group-item-action.active{color:#fff;background-color:#818182;border-color:#818182}.list-group-item-dark{color:#1b1e21;background-color:#c6c8ca}.list-group-item-dark.list-group-item-action:focus,.list-group-item-dark.list-group-item-action:hover{color:#1b1e21;background-color:#b9bbbe}.list-group-item-dark.list-group-item-action.active{color:#fff;background-color:#1b1e21;border-color:#1b1e21}.close{float:right;font-size:1.35rem;font-weight:700;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.5}.close:not(:disabled):not(.disabled){cursor:pointer}.close:not(:disabled):not(.disabled):focus,.close:not(:disabled):not(.disabled):hover{color:#000;text-decoration:none;opacity:.75}button.close{padding:0;background-color:transparent;border:0;-webkit-appearance:none}.modal,.modal-open{overflow:hidden}.modal{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;display:none;outline:0}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal-dialog{position:relative;width:auto;margin:.5rem;pointer-events:none}.modal.fade .modal-dialog{-webkit-transition:-webkit-transform .3s ease-out;transition:-webkit-transform .3s ease-out;transition:transform .3s ease-out;transition:transform .3s ease-out,-webkit-transform .3s ease-out;-webkit-transform:translateY(-25%);transform:translateY(-25%)}@media screen and (prefers-reduced-motion:reduce){.modal.fade .modal-dialog{-webkit-transition:none;transition:none}}.modal.show .modal-dialog{-webkit-transform:translate(0);transform:translate(0)}.modal-dialog-centered{-webkit-box-align:center;-ms-flex-align:center;align-items:center;min-height:calc(100% - 1rem)}.modal-content,.modal-dialog-centered{display:-webkit-box;display:-ms-flexbox;display:flex}.modal-content{position:relative;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;width:100%;pointer-events:auto;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem;outline:0}.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0}.modal-backdrop.show{opacity:.5}.modal-header{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;padding:1rem;border-bottom:1px solid #e9ecef;border-top-left-radius:.3rem;border-top-right-radius:.3rem}.modal-header .close{padding:1rem;margin:-1rem -1rem -1rem auto}.modal-title{margin-bottom:0;line-height:1.6}.modal-body{position:relative;-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;padding:1rem}.modal-footer{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end;padding:1rem;border-top:1px solid #e9ecef}.modal-footer>:not(:first-child){margin-left:.25rem}.modal-footer>:not(:last-child){margin-right:.25rem}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:576px){.modal-dialog{max-width:500px;margin:1.75rem auto}.modal-dialog-centered{min-height:calc(100% - 3.5rem)}.modal-sm{max-width:300px}}@media (min-width:992px){.modal-lg{max-width:800px}}.tooltip{position:absolute;z-index:1070;display:block;margin:0;font-family:Nunito,sans-serif;font-style:normal;font-weight:400;line-height:1.6;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;font-size:.7875rem;word-wrap:break-word;opacity:0}.tooltip.show{opacity:.9}.tooltip .arrow{position:absolute;display:block;width:.8rem;height:.4rem}.tooltip .arrow:before{position:absolute;content:"";border-color:transparent;border-style:solid}.bs-tooltip-auto[x-placement^=top],.bs-tooltip-top{padding:.4rem 0}.bs-tooltip-auto[x-placement^=top] .arrow,.bs-tooltip-top .arrow{bottom:0}.bs-tooltip-auto[x-placement^=top] .arrow:before,.bs-tooltip-top .arrow:before{top:0;border-width:.4rem .4rem 0;border-top-color:#000}.bs-tooltip-auto[x-placement^=right],.bs-tooltip-right{padding:0 .4rem}.bs-tooltip-auto[x-placement^=right] .arrow,.bs-tooltip-right .arrow{left:0;width:.4rem;height:.8rem}.bs-tooltip-auto[x-placement^=right] .arrow:before,.bs-tooltip-right .arrow:before{right:0;border-width:.4rem .4rem .4rem 0;border-right-color:#000}.bs-tooltip-auto[x-placement^=bottom],.bs-tooltip-bottom{padding:.4rem 0}.bs-tooltip-auto[x-placement^=bottom] .arrow,.bs-tooltip-bottom .arrow{top:0}.bs-tooltip-auto[x-placement^=bottom] .arrow:before,.bs-tooltip-bottom .arrow:before{bottom:0;border-width:0 .4rem .4rem;border-bottom-color:#000}.bs-tooltip-auto[x-placement^=left],.bs-tooltip-left{padding:0 .4rem}.bs-tooltip-auto[x-placement^=left] .arrow,.bs-tooltip-left .arrow{right:0;width:.4rem;height:.8rem}.bs-tooltip-auto[x-placement^=left] .arrow:before,.bs-tooltip-left .arrow:before{left:0;border-width:.4rem 0 .4rem .4rem;border-left-color:#000}.tooltip-inner{max-width:200px;padding:.25rem .5rem;color:#fff;text-align:center;background-color:#000;border-radius:.25rem}.popover{top:0;left:0;z-index:1060;max-width:276px;font-family:Nunito,sans-serif;font-style:normal;font-weight:400;line-height:1.6;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;font-size:.7875rem;word-wrap:break-word;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem}.popover,.popover .arrow{position:absolute;display:block}.popover .arrow{width:1rem;height:.5rem;margin:0 .3rem}.popover .arrow:after,.popover .arrow:before{position:absolute;display:block;content:"";border-color:transparent;border-style:solid}.bs-popover-auto[x-placement^=top],.bs-popover-top{margin-bottom:.5rem}.bs-popover-auto[x-placement^=top] .arrow,.bs-popover-top .arrow{bottom:calc((.5rem + 1px) * -1)}.bs-popover-auto[x-placement^=top] .arrow:after,.bs-popover-auto[x-placement^=top] .arrow:before,.bs-popover-top .arrow:after,.bs-popover-top .arrow:before{border-width:.5rem .5rem 0}.bs-popover-auto[x-placement^=top] .arrow:before,.bs-popover-top .arrow:before{bottom:0;border-top-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=top] .arrow:after,.bs-popover-top .arrow:after{bottom:1px;border-top-color:#fff}.bs-popover-auto[x-placement^=right],.bs-popover-right{margin-left:.5rem}.bs-popover-auto[x-placement^=right] .arrow,.bs-popover-right .arrow{left:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}.bs-popover-auto[x-placement^=right] .arrow:after,.bs-popover-auto[x-placement^=right] .arrow:before,.bs-popover-right .arrow:after,.bs-popover-right .arrow:before{border-width:.5rem .5rem .5rem 0}.bs-popover-auto[x-placement^=right] .arrow:before,.bs-popover-right .arrow:before{left:0;border-right-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=right] .arrow:after,.bs-popover-right .arrow:after{left:1px;border-right-color:#fff}.bs-popover-auto[x-placement^=bottom],.bs-popover-bottom{margin-top:.5rem}.bs-popover-auto[x-placement^=bottom] .arrow,.bs-popover-bottom .arrow{top:calc((.5rem + 1px) * -1)}.bs-popover-auto[x-placement^=bottom] .arrow:after,.bs-popover-auto[x-placement^=bottom] .arrow:before,.bs-popover-bottom .arrow:after,.bs-popover-bottom .arrow:before{border-width:0 .5rem .5rem}.bs-popover-auto[x-placement^=bottom] .arrow:before,.bs-popover-bottom .arrow:before{top:0;border-bottom-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=bottom] .arrow:after,.bs-popover-bottom .arrow:after{top:1px;border-bottom-color:#fff}.bs-popover-auto[x-placement^=bottom] .popover-header:before,.bs-popover-bottom .popover-header:before{position:absolute;top:0;left:50%;display:block;width:1rem;margin-left:-.5rem;content:"";border-bottom:1px solid #f7f7f7}.bs-popover-auto[x-placement^=left],.bs-popover-left{margin-right:.5rem}.bs-popover-auto[x-placement^=left] .arrow,.bs-popover-left .arrow{right:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}.bs-popover-auto[x-placement^=left] .arrow:after,.bs-popover-auto[x-placement^=left] .arrow:before,.bs-popover-left .arrow:after,.bs-popover-left .arrow:before{border-width:.5rem 0 .5rem .5rem}.bs-popover-auto[x-placement^=left] .arrow:before,.bs-popover-left .arrow:before{right:0;border-left-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=left] .arrow:after,.bs-popover-left .arrow:after{right:1px;border-left-color:#fff}.popover-header{padding:.5rem .75rem;margin-bottom:0;font-size:.9rem;color:inherit;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-top-left-radius:calc(.3rem - 1px);border-top-right-radius:calc(.3rem - 1px)}.popover-header:empty{display:none}.popover-body{padding:.5rem .75rem;color:#212529}.carousel{position:relative}.carousel-inner{position:relative;width:100%;overflow:hidden}.carousel-item{position:relative;display:none;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:100%;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-perspective:1000px;perspective:1000px}.carousel-item-next,.carousel-item-prev,.carousel-item.active{display:block;-webkit-transition:-webkit-transform .6s ease;transition:-webkit-transform .6s ease;transition:transform .6s ease;transition:transform .6s ease,-webkit-transform .6s ease}@media screen and (prefers-reduced-motion:reduce){.carousel-item-next,.carousel-item-prev,.carousel-item.active{-webkit-transition:none;transition:none}}.carousel-item-next,.carousel-item-prev{position:absolute;top:0}.carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{-webkit-transform:translateX(0);transform:translateX(0)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{-webkit-transform:translateZ(0);transform:translateZ(0)}}.active.carousel-item-right,.carousel-item-next{-webkit-transform:translateX(100%);transform:translateX(100%)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.active.carousel-item-right,.carousel-item-next{-webkit-transform:translate3d(100%,0,0);transform:translate3d(100%,0,0)}}.active.carousel-item-left,.carousel-item-prev{-webkit-transform:translateX(-100%);transform:translateX(-100%)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.active.carousel-item-left,.carousel-item-prev{-webkit-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0)}}.carousel-fade .carousel-item{opacity:0;-webkit-transition-duration:.6s;transition-duration:.6s;-webkit-transition-property:opacity;transition-property:opacity}.carousel-fade .carousel-item-next.carousel-item-left,.carousel-fade .carousel-item-prev.carousel-item-right,.carousel-fade .carousel-item.active{opacity:1}.carousel-fade .active.carousel-item-left,.carousel-fade .active.carousel-item-right{opacity:0}.carousel-fade .active.carousel-item-left,.carousel-fade .active.carousel-item-prev,.carousel-fade .carousel-item-next,.carousel-fade .carousel-item-prev,.carousel-fade .carousel-item.active{-webkit-transform:translateX(0);transform:translateX(0)}@supports ((-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d)){.carousel-fade .active.carousel-item-left,.carousel-fade .active.carousel-item-prev,.carousel-fade .carousel-item-next,.carousel-fade .carousel-item-prev,.carousel-fade .carousel-item.active{-webkit-transform:translateZ(0);transform:translateZ(0)}}.carousel-control-next,.carousel-control-prev{position:absolute;top:0;bottom:0;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;width:15%;color:#fff;text-align:center;opacity:.5}.carousel-control-next:focus,.carousel-control-next:hover,.carousel-control-prev:focus,.carousel-control-prev:hover{color:#fff;text-decoration:none;outline:0;opacity:.9}.carousel-control-prev{left:0}.carousel-control-next{right:0}.carousel-control-next-icon,.carousel-control-prev-icon{display:inline-block;width:20px;height:20px;background:transparent no-repeat 50%;background-size:100% 100%}.carousel-control-prev-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E")}.carousel-control-next-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E")}.carousel-indicators{position:absolute;right:0;bottom:10px;left:0;z-index:15;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;padding-left:0;margin-right:15%;margin-left:15%;list-style:none}.carousel-indicators li{position:relative;-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto;width:30px;height:3px;margin-right:3px;margin-left:3px;text-indent:-999px;cursor:pointer;background-color:hsla(0,0%,100%,.5)}.carousel-indicators li:before{top:-10px}.carousel-indicators li:after,.carousel-indicators li:before{position:absolute;left:0;display:inline-block;width:100%;height:10px;content:""}.carousel-indicators li:after{bottom:-10px}.carousel-indicators .active{background-color:#fff}.carousel-caption{position:absolute;right:15%;bottom:20px;left:15%;z-index:10;padding-top:20px;padding-bottom:20px;color:#fff;text-align:center}.align-baseline{vertical-align:baseline!important}.align-top{vertical-align:top!important}.align-middle{vertical-align:middle!important}.align-bottom{vertical-align:bottom!important}.align-text-bottom{vertical-align:text-bottom!important}.align-text-top{vertical-align:text-top!important}.bg-primary{background-color:#3490dc!important}a.bg-primary:focus,a.bg-primary:hover,button.bg-primary:focus,button.bg-primary:hover{background-color:#2176bd!important}.bg-secondary{background-color:#6c757d!important}a.bg-secondary:focus,a.bg-secondary:hover,button.bg-secondary:focus,button.bg-secondary:hover{background-color:#545b62!important}.bg-success{background-color:#38c172!important}a.bg-success:focus,a.bg-success:hover,button.bg-success:focus,button.bg-success:hover{background-color:#2d995b!important}.bg-info{background-color:#6cb2eb!important}a.bg-info:focus,a.bg-info:hover,button.bg-info:focus,button.bg-info:hover{background-color:#3f9ae5!important}.bg-warning{background-color:#ffed4a!important}a.bg-warning:focus,a.bg-warning:hover,button.bg-warning:focus,button.bg-warning:hover{background-color:#ffe817!important}.bg-danger{background-color:#e3342f!important}a.bg-danger:focus,a.bg-danger:hover,button.bg-danger:focus,button.bg-danger:hover{background-color:#c51f1a!important}.bg-light{background-color:#f8f9fa!important}a.bg-light:focus,a.bg-light:hover,button.bg-light:focus,button.bg-light:hover{background-color:#dae0e5!important}.bg-dark{background-color:#343a40!important}a.bg-dark:focus,a.bg-dark:hover,button.bg-dark:focus,button.bg-dark:hover{background-color:#1d2124!important}.bg-white{background-color:#fff!important}.bg-transparent{background-color:transparent!important}.border{border:1px solid #dee2e6!important}.border-top{border-top:1px solid #dee2e6!important}.border-right{border-right:1px solid #dee2e6!important}.border-bottom{border-bottom:1px solid #dee2e6!important}.border-left{border-left:1px solid #dee2e6!important}.border-0{border:0!important}.border-top-0{border-top:0!important}.border-right-0{border-right:0!important}.border-bottom-0{border-bottom:0!important}.border-left-0{border-left:0!important}.border-primary{border-color:#3490dc!important}.border-secondary{border-color:#6c757d!important}.border-success{border-color:#38c172!important}.border-info{border-color:#6cb2eb!important}.border-warning{border-color:#ffed4a!important}.border-danger{border-color:#e3342f!important}.border-light{border-color:#f8f9fa!important}.border-dark{border-color:#343a40!important}.border-white{border-color:#fff!important}.rounded{border-radius:.25rem!important}.rounded-top{border-top-left-radius:.25rem!important}.rounded-right,.rounded-top{border-top-right-radius:.25rem!important}.rounded-bottom,.rounded-right{border-bottom-right-radius:.25rem!important}.rounded-bottom,.rounded-left{border-bottom-left-radius:.25rem!important}.rounded-left{border-top-left-radius:.25rem!important}.rounded-circle{border-radius:50%!important}.rounded-0{border-radius:0!important}.clearfix:after{display:block;clear:both;content:""}.d-none{display:none!important}.d-inline{display:inline!important}.d-inline-block{display:inline-block!important}.d-block{display:block!important}.d-table{display:table!important}.d-table-row{display:table-row!important}.d-table-cell{display:table-cell!important}.d-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}@media (min-width:576px){.d-sm-none{display:none!important}.d-sm-inline{display:inline!important}.d-sm-inline-block{display:inline-block!important}.d-sm-block{display:block!important}.d-sm-table{display:table!important}.d-sm-table-row{display:table-row!important}.d-sm-table-cell{display:table-cell!important}.d-sm-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-sm-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:768px){.d-md-none{display:none!important}.d-md-inline{display:inline!important}.d-md-inline-block{display:inline-block!important}.d-md-block{display:block!important}.d-md-table{display:table!important}.d-md-table-row{display:table-row!important}.d-md-table-cell{display:table-cell!important}.d-md-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-md-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:992px){.d-lg-none{display:none!important}.d-lg-inline{display:inline!important}.d-lg-inline-block{display:inline-block!important}.d-lg-block{display:block!important}.d-lg-table{display:table!important}.d-lg-table-row{display:table-row!important}.d-lg-table-cell{display:table-cell!important}.d-lg-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-lg-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media (min-width:1200px){.d-xl-none{display:none!important}.d-xl-inline{display:inline!important}.d-xl-inline-block{display:inline-block!important}.d-xl-block{display:block!important}.d-xl-table{display:table!important}.d-xl-table-row{display:table-row!important}.d-xl-table-cell{display:table-cell!important}.d-xl-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-xl-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}@media print{.d-print-none{display:none!important}.d-print-inline{display:inline!important}.d-print-inline-block{display:inline-block!important}.d-print-block{display:block!important}.d-print-table{display:table!important}.d-print-table-row{display:table-row!important}.d-print-table-cell{display:table-cell!important}.d-print-flex{display:-webkit-box!important;display:-ms-flexbox!important;display:flex!important}.d-print-inline-flex{display:-webkit-inline-box!important;display:-ms-inline-flexbox!important;display:inline-flex!important}}.embed-responsive{position:relative;display:block;width:100%;padding:0;overflow:hidden}.embed-responsive:before{display:block;content:""}.embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;bottom:0;left:0;width:100%;height:100%;border:0}.embed-responsive-21by9:before{padding-top:42.85714286%}.embed-responsive-16by9:before{padding-top:56.25%}.embed-responsive-4by3:before{padding-top:75%}.embed-responsive-1by1:before{padding-top:100%}.flex-row{-webkit-box-orient:horizontal!important;-ms-flex-direction:row!important;flex-direction:row!important}.flex-column,.flex-row{-webkit-box-direction:normal!important}.flex-column{-webkit-box-orient:vertical!important;-ms-flex-direction:column!important;flex-direction:column!important}.flex-row-reverse{-webkit-box-orient:horizontal!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}.flex-column-reverse,.flex-row-reverse{-webkit-box-direction:reverse!important}.flex-column-reverse{-webkit-box-orient:vertical!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}.flex-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}.flex-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}.flex-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}.flex-fill{-webkit-box-flex:1!important;-ms-flex:1 1 auto!important;flex:1 1 auto!important}.flex-grow-0{-webkit-box-flex:0!important;-ms-flex-positive:0!important;flex-grow:0!important}.flex-grow-1{-webkit-box-flex:1!important;-ms-flex-positive:1!important;flex-grow:1!important}.flex-shrink-0{-ms-flex-negative:0!important;flex-shrink:0!important}.flex-shrink-1{-ms-flex-negative:1!important;flex-shrink:1!important}.justify-content-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}.justify-content-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}.justify-content-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}.justify-content-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}.justify-content-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}.align-items-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}.align-items-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}.align-items-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.align-items-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}.align-items-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}.align-content-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}.align-content-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}.align-content-center{-ms-flex-line-pack:center!important;align-content:center!important}.align-content-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}.align-content-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}.align-content-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}.align-self-auto{-ms-flex-item-align:auto!important;align-self:auto!important}.align-self-start{-ms-flex-item-align:start!important;align-self:flex-start!important}.align-self-end{-ms-flex-item-align:end!important;align-self:flex-end!important}.align-self-center{-ms-flex-item-align:center!important;align-self:center!important}.align-self-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}.align-self-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}@media (min-width:576px){.flex-sm-row{-webkit-box-orient:horizontal!important;-ms-flex-direction:row!important;flex-direction:row!important}.flex-sm-column,.flex-sm-row{-webkit-box-direction:normal!important}.flex-sm-column{-webkit-box-orient:vertical!important;-ms-flex-direction:column!important;flex-direction:column!important}.flex-sm-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}.flex-sm-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}.flex-sm-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}.flex-sm-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}.flex-sm-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}.flex-sm-fill{-webkit-box-flex:1!important;-ms-flex:1 1 auto!important;flex:1 1 auto!important}.flex-sm-grow-0{-webkit-box-flex:0!important;-ms-flex-positive:0!important;flex-grow:0!important}.flex-sm-grow-1{-webkit-box-flex:1!important;-ms-flex-positive:1!important;flex-grow:1!important}.flex-sm-shrink-0{-ms-flex-negative:0!important;flex-shrink:0!important}.flex-sm-shrink-1{-ms-flex-negative:1!important;flex-shrink:1!important}.justify-content-sm-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}.justify-content-sm-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}.justify-content-sm-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}.justify-content-sm-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}.justify-content-sm-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}.align-items-sm-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}.align-items-sm-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}.align-items-sm-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.align-items-sm-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}.align-items-sm-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}.align-content-sm-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}.align-content-sm-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}.align-content-sm-center{-ms-flex-line-pack:center!important;align-content:center!important}.align-content-sm-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}.align-content-sm-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}.align-content-sm-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}.align-self-sm-auto{-ms-flex-item-align:auto!important;align-self:auto!important}.align-self-sm-start{-ms-flex-item-align:start!important;align-self:flex-start!important}.align-self-sm-end{-ms-flex-item-align:end!important;align-self:flex-end!important}.align-self-sm-center{-ms-flex-item-align:center!important;align-self:center!important}.align-self-sm-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}.align-self-sm-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:768px){.flex-md-row{-webkit-box-orient:horizontal!important;-ms-flex-direction:row!important;flex-direction:row!important}.flex-md-column,.flex-md-row{-webkit-box-direction:normal!important}.flex-md-column{-webkit-box-orient:vertical!important;-ms-flex-direction:column!important;flex-direction:column!important}.flex-md-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}.flex-md-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}.flex-md-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}.flex-md-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}.flex-md-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}.flex-md-fill{-webkit-box-flex:1!important;-ms-flex:1 1 auto!important;flex:1 1 auto!important}.flex-md-grow-0{-webkit-box-flex:0!important;-ms-flex-positive:0!important;flex-grow:0!important}.flex-md-grow-1{-webkit-box-flex:1!important;-ms-flex-positive:1!important;flex-grow:1!important}.flex-md-shrink-0{-ms-flex-negative:0!important;flex-shrink:0!important}.flex-md-shrink-1{-ms-flex-negative:1!important;flex-shrink:1!important}.justify-content-md-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}.justify-content-md-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}.justify-content-md-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}.justify-content-md-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}.justify-content-md-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}.align-items-md-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}.align-items-md-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}.align-items-md-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.align-items-md-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}.align-items-md-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}.align-content-md-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}.align-content-md-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}.align-content-md-center{-ms-flex-line-pack:center!important;align-content:center!important}.align-content-md-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}.align-content-md-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}.align-content-md-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}.align-self-md-auto{-ms-flex-item-align:auto!important;align-self:auto!important}.align-self-md-start{-ms-flex-item-align:start!important;align-self:flex-start!important}.align-self-md-end{-ms-flex-item-align:end!important;align-self:flex-end!important}.align-self-md-center{-ms-flex-item-align:center!important;align-self:center!important}.align-self-md-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}.align-self-md-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:992px){.flex-lg-row{-webkit-box-orient:horizontal!important;-ms-flex-direction:row!important;flex-direction:row!important}.flex-lg-column,.flex-lg-row{-webkit-box-direction:normal!important}.flex-lg-column{-webkit-box-orient:vertical!important;-ms-flex-direction:column!important;flex-direction:column!important}.flex-lg-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}.flex-lg-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}.flex-lg-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}.flex-lg-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}.flex-lg-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}.flex-lg-fill{-webkit-box-flex:1!important;-ms-flex:1 1 auto!important;flex:1 1 auto!important}.flex-lg-grow-0{-webkit-box-flex:0!important;-ms-flex-positive:0!important;flex-grow:0!important}.flex-lg-grow-1{-webkit-box-flex:1!important;-ms-flex-positive:1!important;flex-grow:1!important}.flex-lg-shrink-0{-ms-flex-negative:0!important;flex-shrink:0!important}.flex-lg-shrink-1{-ms-flex-negative:1!important;flex-shrink:1!important}.justify-content-lg-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}.justify-content-lg-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}.justify-content-lg-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}.justify-content-lg-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}.justify-content-lg-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}.align-items-lg-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}.align-items-lg-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}.align-items-lg-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.align-items-lg-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}.align-items-lg-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}.align-content-lg-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}.align-content-lg-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}.align-content-lg-center{-ms-flex-line-pack:center!important;align-content:center!important}.align-content-lg-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}.align-content-lg-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}.align-content-lg-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}.align-self-lg-auto{-ms-flex-item-align:auto!important;align-self:auto!important}.align-self-lg-start{-ms-flex-item-align:start!important;align-self:flex-start!important}.align-self-lg-end{-ms-flex-item-align:end!important;align-self:flex-end!important}.align-self-lg-center{-ms-flex-item-align:center!important;align-self:center!important}.align-self-lg-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}.align-self-lg-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}@media (min-width:1200px){.flex-xl-row{-webkit-box-orient:horizontal!important;-ms-flex-direction:row!important;flex-direction:row!important}.flex-xl-column,.flex-xl-row{-webkit-box-direction:normal!important}.flex-xl-column{-webkit-box-orient:vertical!important;-ms-flex-direction:column!important;flex-direction:column!important}.flex-xl-row-reverse{-webkit-box-orient:horizontal!important;-webkit-box-direction:reverse!important;-ms-flex-direction:row-reverse!important;flex-direction:row-reverse!important}.flex-xl-column-reverse{-webkit-box-orient:vertical!important;-webkit-box-direction:reverse!important;-ms-flex-direction:column-reverse!important;flex-direction:column-reverse!important}.flex-xl-wrap{-ms-flex-wrap:wrap!important;flex-wrap:wrap!important}.flex-xl-nowrap{-ms-flex-wrap:nowrap!important;flex-wrap:nowrap!important}.flex-xl-wrap-reverse{-ms-flex-wrap:wrap-reverse!important;flex-wrap:wrap-reverse!important}.flex-xl-fill{-webkit-box-flex:1!important;-ms-flex:1 1 auto!important;flex:1 1 auto!important}.flex-xl-grow-0{-webkit-box-flex:0!important;-ms-flex-positive:0!important;flex-grow:0!important}.flex-xl-grow-1{-webkit-box-flex:1!important;-ms-flex-positive:1!important;flex-grow:1!important}.flex-xl-shrink-0{-ms-flex-negative:0!important;flex-shrink:0!important}.flex-xl-shrink-1{-ms-flex-negative:1!important;flex-shrink:1!important}.justify-content-xl-start{-webkit-box-pack:start!important;-ms-flex-pack:start!important;justify-content:flex-start!important}.justify-content-xl-end{-webkit-box-pack:end!important;-ms-flex-pack:end!important;justify-content:flex-end!important}.justify-content-xl-center{-webkit-box-pack:center!important;-ms-flex-pack:center!important;justify-content:center!important}.justify-content-xl-between{-webkit-box-pack:justify!important;-ms-flex-pack:justify!important;justify-content:space-between!important}.justify-content-xl-around{-ms-flex-pack:distribute!important;justify-content:space-around!important}.align-items-xl-start{-webkit-box-align:start!important;-ms-flex-align:start!important;align-items:flex-start!important}.align-items-xl-end{-webkit-box-align:end!important;-ms-flex-align:end!important;align-items:flex-end!important}.align-items-xl-center{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.align-items-xl-baseline{-webkit-box-align:baseline!important;-ms-flex-align:baseline!important;align-items:baseline!important}.align-items-xl-stretch{-webkit-box-align:stretch!important;-ms-flex-align:stretch!important;align-items:stretch!important}.align-content-xl-start{-ms-flex-line-pack:start!important;align-content:flex-start!important}.align-content-xl-end{-ms-flex-line-pack:end!important;align-content:flex-end!important}.align-content-xl-center{-ms-flex-line-pack:center!important;align-content:center!important}.align-content-xl-between{-ms-flex-line-pack:justify!important;align-content:space-between!important}.align-content-xl-around{-ms-flex-line-pack:distribute!important;align-content:space-around!important}.align-content-xl-stretch{-ms-flex-line-pack:stretch!important;align-content:stretch!important}.align-self-xl-auto{-ms-flex-item-align:auto!important;align-self:auto!important}.align-self-xl-start{-ms-flex-item-align:start!important;align-self:flex-start!important}.align-self-xl-end{-ms-flex-item-align:end!important;align-self:flex-end!important}.align-self-xl-center{-ms-flex-item-align:center!important;align-self:center!important}.align-self-xl-baseline{-ms-flex-item-align:baseline!important;align-self:baseline!important}.align-self-xl-stretch{-ms-flex-item-align:stretch!important;align-self:stretch!important}}.float-left{float:left!important}.float-right{float:right!important}.float-none{float:none!important}@media (min-width:576px){.float-sm-left{float:left!important}.float-sm-right{float:right!important}.float-sm-none{float:none!important}}@media (min-width:768px){.float-md-left{float:left!important}.float-md-right{float:right!important}.float-md-none{float:none!important}}@media (min-width:992px){.float-lg-left{float:left!important}.float-lg-right{float:right!important}.float-lg-none{float:none!important}}@media (min-width:1200px){.float-xl-left{float:left!important}.float-xl-right{float:right!important}.float-xl-none{float:none!important}}.position-static{position:static!important}.position-relative{position:relative!important}.position-absolute{position:absolute!important}.position-fixed{position:fixed!important}.position-sticky{position:-webkit-sticky!important;position:sticky!important}.fixed-top{top:0}.fixed-bottom,.fixed-top{position:fixed;right:0;left:0;z-index:1030}.fixed-bottom{bottom:0}@supports ((position:-webkit-sticky) or (position:sticky)){.sticky-top{position:-webkit-sticky;position:sticky;top:0;z-index:1020}}.sr-only{position:absolute;width:1px;height:1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;overflow:visible;clip:auto;white-space:normal}.shadow-sm{-webkit-box-shadow:0 .125rem .25rem rgba(0,0,0,.075)!important;box-shadow:0 .125rem .25rem rgba(0,0,0,.075)!important}.shadow{-webkit-box-shadow:0 .5rem 1rem rgba(0,0,0,.15)!important;box-shadow:0 .5rem 1rem rgba(0,0,0,.15)!important}.shadow-lg{-webkit-box-shadow:0 1rem 3rem rgba(0,0,0,.175)!important;box-shadow:0 1rem 3rem rgba(0,0,0,.175)!important}.shadow-none{-webkit-box-shadow:none!important;box-shadow:none!important}.w-25{width:25%!important}.w-50{width:50%!important}.w-75{width:75%!important}.w-100{width:100%!important}.w-auto{width:auto!important}.h-25{height:25%!important}.h-50{height:50%!important}.h-75{height:75%!important}.h-100{height:100%!important}.h-auto{height:auto!important}.mw-100{max-width:100%!important}.mh-100{max-height:100%!important}.m-0{margin:0!important}.mt-0,.my-0{margin-top:0!important}.mr-0,.mx-0{margin-right:0!important}.mb-0,.my-0{margin-bottom:0!important}.ml-0,.mx-0{margin-left:0!important}.m-1{margin:.25rem!important}.mt-1,.my-1{margin-top:.25rem!important}.mr-1,.mx-1{margin-right:.25rem!important}.mb-1,.my-1{margin-bottom:.25rem!important}.ml-1,.mx-1{margin-left:.25rem!important}.m-2{margin:.5rem!important}.mt-2,.my-2{margin-top:.5rem!important}.mr-2,.mx-2{margin-right:.5rem!important}.mb-2,.my-2{margin-bottom:.5rem!important}.ml-2,.mx-2{margin-left:.5rem!important}.m-3{margin:1rem!important}.mt-3,.my-3{margin-top:1rem!important}.mr-3,.mx-3{margin-right:1rem!important}.mb-3,.my-3{margin-bottom:1rem!important}.ml-3,.mx-3{margin-left:1rem!important}.m-4{margin:1.5rem!important}.mt-4,.my-4{margin-top:1.5rem!important}.mr-4,.mx-4{margin-right:1.5rem!important}.mb-4,.my-4{margin-bottom:1.5rem!important}.ml-4,.mx-4{margin-left:1.5rem!important}.m-5{margin:3rem!important}.mt-5,.my-5{margin-top:3rem!important}.mr-5,.mx-5{margin-right:3rem!important}.mb-5,.my-5{margin-bottom:3rem!important}.ml-5,.mx-5{margin-left:3rem!important}.p-0{padding:0!important}.pt-0,.py-0{padding-top:0!important}.pr-0,.px-0{padding-right:0!important}.pb-0,.py-0{padding-bottom:0!important}.pl-0,.px-0{padding-left:0!important}.p-1{padding:.25rem!important}.pt-1,.py-1{padding-top:.25rem!important}.pr-1,.px-1{padding-right:.25rem!important}.pb-1,.py-1{padding-bottom:.25rem!important}.pl-1,.px-1{padding-left:.25rem!important}.p-2{padding:.5rem!important}.pt-2,.py-2{padding-top:.5rem!important}.pr-2,.px-2{padding-right:.5rem!important}.pb-2,.py-2{padding-bottom:.5rem!important}.pl-2,.px-2{padding-left:.5rem!important}.p-3{padding:1rem!important}.pt-3,.py-3{padding-top:1rem!important}.pr-3,.px-3{padding-right:1rem!important}.pb-3,.py-3{padding-bottom:1rem!important}.pl-3,.px-3{padding-left:1rem!important}.p-4{padding:1.5rem!important}.pt-4,.py-4{padding-top:1.5rem!important}.pr-4,.px-4{padding-right:1.5rem!important}.pb-4,.py-4{padding-bottom:1.5rem!important}.pl-4,.px-4{padding-left:1.5rem!important}.p-5{padding:3rem!important}.pt-5,.py-5{padding-top:3rem!important}.pr-5,.px-5{padding-right:3rem!important}.pb-5,.py-5{padding-bottom:3rem!important}.pl-5,.px-5{padding-left:3rem!important}.m-auto{margin:auto!important}.mt-auto,.my-auto{margin-top:auto!important}.mr-auto,.mx-auto{margin-right:auto!important}.mb-auto,.my-auto{margin-bottom:auto!important}.ml-auto,.mx-auto{margin-left:auto!important}@media (min-width:576px){.m-sm-0{margin:0!important}.mt-sm-0,.my-sm-0{margin-top:0!important}.mr-sm-0,.mx-sm-0{margin-right:0!important}.mb-sm-0,.my-sm-0{margin-bottom:0!important}.ml-sm-0,.mx-sm-0{margin-left:0!important}.m-sm-1{margin:.25rem!important}.mt-sm-1,.my-sm-1{margin-top:.25rem!important}.mr-sm-1,.mx-sm-1{margin-right:.25rem!important}.mb-sm-1,.my-sm-1{margin-bottom:.25rem!important}.ml-sm-1,.mx-sm-1{margin-left:.25rem!important}.m-sm-2{margin:.5rem!important}.mt-sm-2,.my-sm-2{margin-top:.5rem!important}.mr-sm-2,.mx-sm-2{margin-right:.5rem!important}.mb-sm-2,.my-sm-2{margin-bottom:.5rem!important}.ml-sm-2,.mx-sm-2{margin-left:.5rem!important}.m-sm-3{margin:1rem!important}.mt-sm-3,.my-sm-3{margin-top:1rem!important}.mr-sm-3,.mx-sm-3{margin-right:1rem!important}.mb-sm-3,.my-sm-3{margin-bottom:1rem!important}.ml-sm-3,.mx-sm-3{margin-left:1rem!important}.m-sm-4{margin:1.5rem!important}.mt-sm-4,.my-sm-4{margin-top:1.5rem!important}.mr-sm-4,.mx-sm-4{margin-right:1.5rem!important}.mb-sm-4,.my-sm-4{margin-bottom:1.5rem!important}.ml-sm-4,.mx-sm-4{margin-left:1.5rem!important}.m-sm-5{margin:3rem!important}.mt-sm-5,.my-sm-5{margin-top:3rem!important}.mr-sm-5,.mx-sm-5{margin-right:3rem!important}.mb-sm-5,.my-sm-5{margin-bottom:3rem!important}.ml-sm-5,.mx-sm-5{margin-left:3rem!important}.p-sm-0{padding:0!important}.pt-sm-0,.py-sm-0{padding-top:0!important}.pr-sm-0,.px-sm-0{padding-right:0!important}.pb-sm-0,.py-sm-0{padding-bottom:0!important}.pl-sm-0,.px-sm-0{padding-left:0!important}.p-sm-1{padding:.25rem!important}.pt-sm-1,.py-sm-1{padding-top:.25rem!important}.pr-sm-1,.px-sm-1{padding-right:.25rem!important}.pb-sm-1,.py-sm-1{padding-bottom:.25rem!important}.pl-sm-1,.px-sm-1{padding-left:.25rem!important}.p-sm-2{padding:.5rem!important}.pt-sm-2,.py-sm-2{padding-top:.5rem!important}.pr-sm-2,.px-sm-2{padding-right:.5rem!important}.pb-sm-2,.py-sm-2{padding-bottom:.5rem!important}.pl-sm-2,.px-sm-2{padding-left:.5rem!important}.p-sm-3{padding:1rem!important}.pt-sm-3,.py-sm-3{padding-top:1rem!important}.pr-sm-3,.px-sm-3{padding-right:1rem!important}.pb-sm-3,.py-sm-3{padding-bottom:1rem!important}.pl-sm-3,.px-sm-3{padding-left:1rem!important}.p-sm-4{padding:1.5rem!important}.pt-sm-4,.py-sm-4{padding-top:1.5rem!important}.pr-sm-4,.px-sm-4{padding-right:1.5rem!important}.pb-sm-4,.py-sm-4{padding-bottom:1.5rem!important}.pl-sm-4,.px-sm-4{padding-left:1.5rem!important}.p-sm-5{padding:3rem!important}.pt-sm-5,.py-sm-5{padding-top:3rem!important}.pr-sm-5,.px-sm-5{padding-right:3rem!important}.pb-sm-5,.py-sm-5{padding-bottom:3rem!important}.pl-sm-5,.px-sm-5{padding-left:3rem!important}.m-sm-auto{margin:auto!important}.mt-sm-auto,.my-sm-auto{margin-top:auto!important}.mr-sm-auto,.mx-sm-auto{margin-right:auto!important}.mb-sm-auto,.my-sm-auto{margin-bottom:auto!important}.ml-sm-auto,.mx-sm-auto{margin-left:auto!important}}@media (min-width:768px){.m-md-0{margin:0!important}.mt-md-0,.my-md-0{margin-top:0!important}.mr-md-0,.mx-md-0{margin-right:0!important}.mb-md-0,.my-md-0{margin-bottom:0!important}.ml-md-0,.mx-md-0{margin-left:0!important}.m-md-1{margin:.25rem!important}.mt-md-1,.my-md-1{margin-top:.25rem!important}.mr-md-1,.mx-md-1{margin-right:.25rem!important}.mb-md-1,.my-md-1{margin-bottom:.25rem!important}.ml-md-1,.mx-md-1{margin-left:.25rem!important}.m-md-2{margin:.5rem!important}.mt-md-2,.my-md-2{margin-top:.5rem!important}.mr-md-2,.mx-md-2{margin-right:.5rem!important}.mb-md-2,.my-md-2{margin-bottom:.5rem!important}.ml-md-2,.mx-md-2{margin-left:.5rem!important}.m-md-3{margin:1rem!important}.mt-md-3,.my-md-3{margin-top:1rem!important}.mr-md-3,.mx-md-3{margin-right:1rem!important}.mb-md-3,.my-md-3{margin-bottom:1rem!important}.ml-md-3,.mx-md-3{margin-left:1rem!important}.m-md-4{margin:1.5rem!important}.mt-md-4,.my-md-4{margin-top:1.5rem!important}.mr-md-4,.mx-md-4{margin-right:1.5rem!important}.mb-md-4,.my-md-4{margin-bottom:1.5rem!important}.ml-md-4,.mx-md-4{margin-left:1.5rem!important}.m-md-5{margin:3rem!important}.mt-md-5,.my-md-5{margin-top:3rem!important}.mr-md-5,.mx-md-5{margin-right:3rem!important}.mb-md-5,.my-md-5{margin-bottom:3rem!important}.ml-md-5,.mx-md-5{margin-left:3rem!important}.p-md-0{padding:0!important}.pt-md-0,.py-md-0{padding-top:0!important}.pr-md-0,.px-md-0{padding-right:0!important}.pb-md-0,.py-md-0{padding-bottom:0!important}.pl-md-0,.px-md-0{padding-left:0!important}.p-md-1{padding:.25rem!important}.pt-md-1,.py-md-1{padding-top:.25rem!important}.pr-md-1,.px-md-1{padding-right:.25rem!important}.pb-md-1,.py-md-1{padding-bottom:.25rem!important}.pl-md-1,.px-md-1{padding-left:.25rem!important}.p-md-2{padding:.5rem!important}.pt-md-2,.py-md-2{padding-top:.5rem!important}.pr-md-2,.px-md-2{padding-right:.5rem!important}.pb-md-2,.py-md-2{padding-bottom:.5rem!important}.pl-md-2,.px-md-2{padding-left:.5rem!important}.p-md-3{padding:1rem!important}.pt-md-3,.py-md-3{padding-top:1rem!important}.pr-md-3,.px-md-3{padding-right:1rem!important}.pb-md-3,.py-md-3{padding-bottom:1rem!important}.pl-md-3,.px-md-3{padding-left:1rem!important}.p-md-4{padding:1.5rem!important}.pt-md-4,.py-md-4{padding-top:1.5rem!important}.pr-md-4,.px-md-4{padding-right:1.5rem!important}.pb-md-4,.py-md-4{padding-bottom:1.5rem!important}.pl-md-4,.px-md-4{padding-left:1.5rem!important}.p-md-5{padding:3rem!important}.pt-md-5,.py-md-5{padding-top:3rem!important}.pr-md-5,.px-md-5{padding-right:3rem!important}.pb-md-5,.py-md-5{padding-bottom:3rem!important}.pl-md-5,.px-md-5{padding-left:3rem!important}.m-md-auto{margin:auto!important}.mt-md-auto,.my-md-auto{margin-top:auto!important}.mr-md-auto,.mx-md-auto{margin-right:auto!important}.mb-md-auto,.my-md-auto{margin-bottom:auto!important}.ml-md-auto,.mx-md-auto{margin-left:auto!important}}@media (min-width:992px){.m-lg-0{margin:0!important}.mt-lg-0,.my-lg-0{margin-top:0!important}.mr-lg-0,.mx-lg-0{margin-right:0!important}.mb-lg-0,.my-lg-0{margin-bottom:0!important}.ml-lg-0,.mx-lg-0{margin-left:0!important}.m-lg-1{margin:.25rem!important}.mt-lg-1,.my-lg-1{margin-top:.25rem!important}.mr-lg-1,.mx-lg-1{margin-right:.25rem!important}.mb-lg-1,.my-lg-1{margin-bottom:.25rem!important}.ml-lg-1,.mx-lg-1{margin-left:.25rem!important}.m-lg-2{margin:.5rem!important}.mt-lg-2,.my-lg-2{margin-top:.5rem!important}.mr-lg-2,.mx-lg-2{margin-right:.5rem!important}.mb-lg-2,.my-lg-2{margin-bottom:.5rem!important}.ml-lg-2,.mx-lg-2{margin-left:.5rem!important}.m-lg-3{margin:1rem!important}.mt-lg-3,.my-lg-3{margin-top:1rem!important}.mr-lg-3,.mx-lg-3{margin-right:1rem!important}.mb-lg-3,.my-lg-3{margin-bottom:1rem!important}.ml-lg-3,.mx-lg-3{margin-left:1rem!important}.m-lg-4{margin:1.5rem!important}.mt-lg-4,.my-lg-4{margin-top:1.5rem!important}.mr-lg-4,.mx-lg-4{margin-right:1.5rem!important}.mb-lg-4,.my-lg-4{margin-bottom:1.5rem!important}.ml-lg-4,.mx-lg-4{margin-left:1.5rem!important}.m-lg-5{margin:3rem!important}.mt-lg-5,.my-lg-5{margin-top:3rem!important}.mr-lg-5,.mx-lg-5{margin-right:3rem!important}.mb-lg-5,.my-lg-5{margin-bottom:3rem!important}.ml-lg-5,.mx-lg-5{margin-left:3rem!important}.p-lg-0{padding:0!important}.pt-lg-0,.py-lg-0{padding-top:0!important}.pr-lg-0,.px-lg-0{padding-right:0!important}.pb-lg-0,.py-lg-0{padding-bottom:0!important}.pl-lg-0,.px-lg-0{padding-left:0!important}.p-lg-1{padding:.25rem!important}.pt-lg-1,.py-lg-1{padding-top:.25rem!important}.pr-lg-1,.px-lg-1{padding-right:.25rem!important}.pb-lg-1,.py-lg-1{padding-bottom:.25rem!important}.pl-lg-1,.px-lg-1{padding-left:.25rem!important}.p-lg-2{padding:.5rem!important}.pt-lg-2,.py-lg-2{padding-top:.5rem!important}.pr-lg-2,.px-lg-2{padding-right:.5rem!important}.pb-lg-2,.py-lg-2{padding-bottom:.5rem!important}.pl-lg-2,.px-lg-2{padding-left:.5rem!important}.p-lg-3{padding:1rem!important}.pt-lg-3,.py-lg-3{padding-top:1rem!important}.pr-lg-3,.px-lg-3{padding-right:1rem!important}.pb-lg-3,.py-lg-3{padding-bottom:1rem!important}.pl-lg-3,.px-lg-3{padding-left:1rem!important}.p-lg-4{padding:1.5rem!important}.pt-lg-4,.py-lg-4{padding-top:1.5rem!important}.pr-lg-4,.px-lg-4{padding-right:1.5rem!important}.pb-lg-4,.py-lg-4{padding-bottom:1.5rem!important}.pl-lg-4,.px-lg-4{padding-left:1.5rem!important}.p-lg-5{padding:3rem!important}.pt-lg-5,.py-lg-5{padding-top:3rem!important}.pr-lg-5,.px-lg-5{padding-right:3rem!important}.pb-lg-5,.py-lg-5{padding-bottom:3rem!important}.pl-lg-5,.px-lg-5{padding-left:3rem!important}.m-lg-auto{margin:auto!important}.mt-lg-auto,.my-lg-auto{margin-top:auto!important}.mr-lg-auto,.mx-lg-auto{margin-right:auto!important}.mb-lg-auto,.my-lg-auto{margin-bottom:auto!important}.ml-lg-auto,.mx-lg-auto{margin-left:auto!important}}@media (min-width:1200px){.m-xl-0{margin:0!important}.mt-xl-0,.my-xl-0{margin-top:0!important}.mr-xl-0,.mx-xl-0{margin-right:0!important}.mb-xl-0,.my-xl-0{margin-bottom:0!important}.ml-xl-0,.mx-xl-0{margin-left:0!important}.m-xl-1{margin:.25rem!important}.mt-xl-1,.my-xl-1{margin-top:.25rem!important}.mr-xl-1,.mx-xl-1{margin-right:.25rem!important}.mb-xl-1,.my-xl-1{margin-bottom:.25rem!important}.ml-xl-1,.mx-xl-1{margin-left:.25rem!important}.m-xl-2{margin:.5rem!important}.mt-xl-2,.my-xl-2{margin-top:.5rem!important}.mr-xl-2,.mx-xl-2{margin-right:.5rem!important}.mb-xl-2,.my-xl-2{margin-bottom:.5rem!important}.ml-xl-2,.mx-xl-2{margin-left:.5rem!important}.m-xl-3{margin:1rem!important}.mt-xl-3,.my-xl-3{margin-top:1rem!important}.mr-xl-3,.mx-xl-3{margin-right:1rem!important}.mb-xl-3,.my-xl-3{margin-bottom:1rem!important}.ml-xl-3,.mx-xl-3{margin-left:1rem!important}.m-xl-4{margin:1.5rem!important}.mt-xl-4,.my-xl-4{margin-top:1.5rem!important}.mr-xl-4,.mx-xl-4{margin-right:1.5rem!important}.mb-xl-4,.my-xl-4{margin-bottom:1.5rem!important}.ml-xl-4,.mx-xl-4{margin-left:1.5rem!important}.m-xl-5{margin:3rem!important}.mt-xl-5,.my-xl-5{margin-top:3rem!important}.mr-xl-5,.mx-xl-5{margin-right:3rem!important}.mb-xl-5,.my-xl-5{margin-bottom:3rem!important}.ml-xl-5,.mx-xl-5{margin-left:3rem!important}.p-xl-0{padding:0!important}.pt-xl-0,.py-xl-0{padding-top:0!important}.pr-xl-0,.px-xl-0{padding-right:0!important}.pb-xl-0,.py-xl-0{padding-bottom:0!important}.pl-xl-0,.px-xl-0{padding-left:0!important}.p-xl-1{padding:.25rem!important}.pt-xl-1,.py-xl-1{padding-top:.25rem!important}.pr-xl-1,.px-xl-1{padding-right:.25rem!important}.pb-xl-1,.py-xl-1{padding-bottom:.25rem!important}.pl-xl-1,.px-xl-1{padding-left:.25rem!important}.p-xl-2{padding:.5rem!important}.pt-xl-2,.py-xl-2{padding-top:.5rem!important}.pr-xl-2,.px-xl-2{padding-right:.5rem!important}.pb-xl-2,.py-xl-2{padding-bottom:.5rem!important}.pl-xl-2,.px-xl-2{padding-left:.5rem!important}.p-xl-3{padding:1rem!important}.pt-xl-3,.py-xl-3{padding-top:1rem!important}.pr-xl-3,.px-xl-3{padding-right:1rem!important}.pb-xl-3,.py-xl-3{padding-bottom:1rem!important}.pl-xl-3,.px-xl-3{padding-left:1rem!important}.p-xl-4{padding:1.5rem!important}.pt-xl-4,.py-xl-4{padding-top:1.5rem!important}.pr-xl-4,.px-xl-4{padding-right:1.5rem!important}.pb-xl-4,.py-xl-4{padding-bottom:1.5rem!important}.pl-xl-4,.px-xl-4{padding-left:1.5rem!important}.p-xl-5{padding:3rem!important}.pt-xl-5,.py-xl-5{padding-top:3rem!important}.pr-xl-5,.px-xl-5{padding-right:3rem!important}.pb-xl-5,.py-xl-5{padding-bottom:3rem!important}.pl-xl-5,.px-xl-5{padding-left:3rem!important}.m-xl-auto{margin:auto!important}.mt-xl-auto,.my-xl-auto{margin-top:auto!important}.mr-xl-auto,.mx-xl-auto{margin-right:auto!important}.mb-xl-auto,.my-xl-auto{margin-bottom:auto!important}.ml-xl-auto,.mx-xl-auto{margin-left:auto!important}}.text-monospace{font-family:SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.text-justify{text-align:justify!important}.text-nowrap{white-space:nowrap!important}.text-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.text-left{text-align:left!important}.text-right{text-align:right!important}.text-center{text-align:center!important}@media (min-width:576px){.text-sm-left{text-align:left!important}.text-sm-right{text-align:right!important}.text-sm-center{text-align:center!important}}@media (min-width:768px){.text-md-left{text-align:left!important}.text-md-right{text-align:right!important}.text-md-center{text-align:center!important}}@media (min-width:992px){.text-lg-left{text-align:left!important}.text-lg-right{text-align:right!important}.text-lg-center{text-align:center!important}}@media (min-width:1200px){.text-xl-left{text-align:left!important}.text-xl-right{text-align:right!important}.text-xl-center{text-align:center!important}}.text-lowercase{text-transform:lowercase!important}.text-uppercase{text-transform:uppercase!important}.text-capitalize{text-transform:capitalize!important}.font-weight-light{font-weight:300!important}.font-weight-normal{font-weight:400!important}.font-weight-bold{font-weight:700!important}.font-italic{font-style:italic!important}.text-white{color:#fff!important}.text-primary{color:#3490dc!important}a.text-primary:focus,a.text-primary:hover{color:#2176bd!important}.text-secondary{color:#6c757d!important}a.text-secondary:focus,a.text-secondary:hover{color:#545b62!important}.text-success{color:#38c172!important}a.text-success:focus,a.text-success:hover{color:#2d995b!important}.text-info{color:#6cb2eb!important}a.text-info:focus,a.text-info:hover{color:#3f9ae5!important}.text-warning{color:#ffed4a!important}a.text-warning:focus,a.text-warning:hover{color:#ffe817!important}.text-danger{color:#e3342f!important}a.text-danger:focus,a.text-danger:hover{color:#c51f1a!important}.text-light{color:#f8f9fa!important}a.text-light:focus,a.text-light:hover{color:#dae0e5!important}.text-dark{color:#343a40!important}a.text-dark:focus,a.text-dark:hover{color:#1d2124!important}.text-body{color:#212529!important}.text-muted{color:#6c757d!important}.text-black-50{color:rgba(0,0,0,.5)!important}.text-white-50{color:hsla(0,0%,100%,.5)!important}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.visible{visibility:visible!important}.invisible{visibility:hidden!important}@media print{*,:after,:before{text-shadow:none!important;-webkit-box-shadow:none!important;box-shadow:none!important}a:not(.btn){text-decoration:underline}abbr[title]:after{content:" (" attr(title) ")"}pre{white-space:pre-wrap!important}blockquote,pre{border:1px solid #adb5bd;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}@page{size:a3}.container,body{min-width:992px!important}.navbar{display:none}.badge{border:1px solid #000}.table{border-collapse:collapse!important}.table td,.table th{background-color:#fff!important}.table-bordered td,.table-bordered th{border:1px solid #dee2e6!important}.table-dark{color:inherit}.table-dark tbody+tbody,.table-dark td,.table-dark th,.table-dark thead th{border-color:#dee2e6}.table .thead-dark th{color:inherit;border-color:#dee2e6}}.navbar-laravel{background-color:#fff;-webkit-box-shadow:0 2px 4px rgba(0,0,0,.04);box-shadow:0 2px 4px rgba(0,0,0,.04)}

File: /public\index.php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylor@laravel.com>
 */

define('LARAVEL_START', microtime(true));

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader for
| our application. We just need to utilize it! We'll simply require it
| into the script here so that we don't have to worry about manual
| loading any of our classes later on. It feels great to relax.
|
*/

require __DIR__.'/../vendor/autoload.php';

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


File: /public\js\app.js
!function(e){var t={};function n(r){if(t[r])return t[r].exports;var i=t[r]={i:r,l:!1,exports:{}};return e[r].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{configurable:!1,enumerable:!0,get:r})},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/",n(n.s=11)}([function(e,t,n){"use strict";var r=n(5),i=n(19),o=Object.prototype.toString;function a(e){return"[object Array]"===o.call(e)}function s(e){return null!==e&&"object"==typeof e}function u(e){return"[object Function]"===o.call(e)}function c(e,t){if(null!=e)if("object"!=typeof e&&(e=[e]),a(e))for(var n=0,r=e.length;n<r;n++)t.call(null,e[n],n,e);else for(var i in e)Object.prototype.hasOwnProperty.call(e,i)&&t.call(null,e[i],i,e)}e.exports={isArray:a,isArrayBuffer:function(e){return"[object ArrayBuffer]"===o.call(e)},isBuffer:i,isFormData:function(e){return"undefined"!=typeof FormData&&e instanceof FormData},isArrayBufferView:function(e){return"undefined"!=typeof ArrayBuffer&&ArrayBuffer.isView?ArrayBuffer.isView(e):e&&e.buffer&&e.buffer instanceof ArrayBuffer},isString:function(e){return"string"==typeof e},isNumber:function(e){return"number"==typeof e},isObject:s,isUndefined:function(e){return void 0===e},isDate:function(e){return"[object Date]"===o.call(e)},isFile:function(e){return"[object File]"===o.call(e)},isBlob:function(e){return"[object Blob]"===o.call(e)},isFunction:u,isStream:function(e){return s(e)&&u(e.pipe)},isURLSearchParams:function(e){return"undefined"!=typeof URLSearchParams&&e instanceof URLSearchParams},isStandardBrowserEnv:function(){return("undefined"==typeof navigator||"ReactNative"!==navigator.product)&&"undefined"!=typeof window&&"undefined"!=typeof document},forEach:c,merge:function e(){var t={};function n(n,r){"object"==typeof t[r]&&"object"==typeof n?t[r]=e(t[r],n):t[r]=n}for(var r=0,i=arguments.length;r<i;r++)c(arguments[r],n);return t},extend:function(e,t,n){return c(t,function(t,i){e[i]=n&&"function"==typeof t?r(t,n):t}),e},trim:function(e){return e.replace(/^\s*/,"").replace(/\s*$/,"")}}},function(e,t){var n;n=function(){return this}();try{n=n||Function("return this")()||(0,eval)("this")}catch(e){"object"==typeof window&&(n=window)}e.exports=n},function(e,t,n){"use strict";(function(t){var r=n(0),i=n(21),o={"Content-Type":"application/x-www-form-urlencoded"};function a(e,t){!r.isUndefined(e)&&r.isUndefined(e["Content-Type"])&&(e["Content-Type"]=t)}var s,u={adapter:("undefined"!=typeof XMLHttpRequest?s=n(7):void 0!==t&&(s=n(7)),s),transformRequest:[function(e,t){return i(t,"Content-Type"),r.isFormData(e)||r.isArrayBuffer(e)||r.isBuffer(e)||r.isStream(e)||r.isFile(e)||r.isBlob(e)?e:r.isArrayBufferView(e)?e.buffer:r.isURLSearchParams(e)?(a(t,"application/x-www-form-urlencoded;charset=utf-8"),e.toString()):r.isObject(e)?(a(t,"application/json;charset=utf-8"),JSON.stringify(e)):e}],transformResponse:[function(e){if("string"==typeof e)try{e=JSON.parse(e)}catch(e){}return e}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,validateStatus:function(e){return e>=200&&e<300}};u.headers={common:{Accept:"application/json, text/plain, */*"}},r.forEach(["delete","get","head"],function(e){u.headers[e]={}}),r.forEach(["post","put","patch"],function(e){u.headers[e]=r.merge(o)}),e.exports=u}).call(t,n(6))},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e){for(var n="undefined"!=typeof window&&"undefined"!=typeof document,r=["Edge","Trident","Firefox"],i=0,o=0;o<r.length;o+=1)if(n&&navigator.userAgent.indexOf(r[o])>=0){i=1;break}var a=n&&window.Promise?function(e){var t=!1;return function(){t||(t=!0,window.Promise.resolve().then(function(){t=!1,e()}))}}:function(e){var t=!1;return function(){t||(t=!0,setTimeout(function(){t=!1,e()},i))}};function s(e){return e&&"[object Function]"==={}.toString.call(e)}function u(e,t){if(1!==e.nodeType)return[];var n=getComputedStyle(e,null);return t?n[t]:n}function c(e){return"HTML"===e.nodeName?e:e.parentNode||e.host}function l(e){if(!e)return document.body;switch(e.nodeName){case"HTML":case"BODY":return e.ownerDocument.body;case"#document":return e.body}var t=u(e),n=t.overflow,r=t.overflowX,i=t.overflowY;return/(auto|scroll|overlay)/.test(n+i+r)?e:l(c(e))}var f=n&&!(!window.MSInputMethodContext||!document.documentMode),p=n&&/MSIE 10/.test(navigator.userAgent);function d(e){return 11===e?f:10===e?p:f||p}function h(e){if(!e)return document.documentElement;for(var t=d(10)?document.body:null,n=e.offsetParent;n===t&&e.nextElementSibling;)n=(e=e.nextElementSibling).offsetParent;var r=n&&n.nodeName;return r&&"BODY"!==r&&"HTML"!==r?-1!==["TD","TABLE"].indexOf(n.nodeName)&&"static"===u(n,"position")?h(n):n:e?e.ownerDocument.documentElement:document.documentElement}function v(e){return null!==e.parentNode?v(e.parentNode):e}function g(e,t){if(!(e&&e.nodeType&&t&&t.nodeType))return document.documentElement;var n=e.compareDocumentPosition(t)&Node.DOCUMENT_POSITION_FOLLOWING,r=n?e:t,i=n?t:e,o=document.createRange();o.setStart(r,0),o.setEnd(i,0);var a,s,u=o.commonAncestorContainer;if(e!==u&&t!==u||r.contains(i))return"BODY"===(s=(a=u).nodeName)||"HTML"!==s&&h(a.firstElementChild)!==a?h(u):u;var c=v(e);return c.host?g(c.host,t):g(e,v(t).host)}function m(e){var t="top"===(arguments.length>1&&void 0!==arguments[1]?arguments[1]:"top")?"scrollTop":"scrollLeft",n=e.nodeName;if("BODY"===n||"HTML"===n){var r=e.ownerDocument.documentElement;return(e.ownerDocument.scrollingElement||r)[t]}return e[t]}function y(e,t){var n="x"===t?"Left":"Top",r="Left"===n?"Right":"Bottom";return parseFloat(e["border"+n+"Width"],10)+parseFloat(e["border"+r+"Width"],10)}function _(e,t,n,r){return Math.max(t["offset"+e],t["scroll"+e],n["client"+e],n["offset"+e],n["scroll"+e],d(10)?n["offset"+e]+r["margin"+("Height"===e?"Top":"Left")]+r["margin"+("Height"===e?"Bottom":"Right")]:0)}function b(){var e=document.body,t=document.documentElement,n=d(10)&&getComputedStyle(t);return{height:_("Height",e,t,n),width:_("Width",e,t,n)}}var w=function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")},x=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),C=function(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e},E=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e};function T(e){return E({},e,{right:e.left+e.width,bottom:e.top+e.height})}function A(e){var t={};try{if(d(10)){t=e.getBoundingClientRect();var n=m(e,"top"),r=m(e,"left");t.top+=n,t.left+=r,t.bottom+=n,t.right+=r}else t=e.getBoundingClientRect()}catch(e){}var i={left:t.left,top:t.top,width:t.right-t.left,height:t.bottom-t.top},o="HTML"===e.nodeName?b():{},a=o.width||e.clientWidth||i.right-i.left,s=o.height||e.clientHeight||i.bottom-i.top,c=e.offsetWidth-a,l=e.offsetHeight-s;if(c||l){var f=u(e);c-=y(f,"x"),l-=y(f,"y"),i.width-=c,i.height-=l}return T(i)}function S(e,t){var n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=d(10),i="HTML"===t.nodeName,o=A(e),a=A(t),s=l(e),c=u(t),f=parseFloat(c.borderTopWidth,10),p=parseFloat(c.borderLeftWidth,10);n&&"HTML"===t.nodeName&&(a.top=Math.max(a.top,0),a.left=Math.max(a.left,0));var h=T({top:o.top-a.top-f,left:o.left-a.left-p,width:o.width,height:o.height});if(h.marginTop=0,h.marginLeft=0,!r&&i){var v=parseFloat(c.marginTop,10),g=parseFloat(c.marginLeft,10);h.top-=f-v,h.bottom-=f-v,h.left-=p-g,h.right-=p-g,h.marginTop=v,h.marginLeft=g}return(r&&!n?t.contains(s):t===s&&"BODY"!==s.nodeName)&&(h=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],r=m(t,"top"),i=m(t,"left"),o=n?-1:1;return e.top+=r*o,e.bottom+=r*o,e.left+=i*o,e.right+=i*o,e}(h,t)),h}function k(e){if(!e||!e.parentElement||d())return document.documentElement;for(var t=e.parentElement;t&&"none"===u(t,"transform");)t=t.parentElement;return t||document.documentElement}function O(e,t,n,r){var i=arguments.length>4&&void 0!==arguments[4]&&arguments[4],o={top:0,left:0},a=i?k(e):g(e,t);if("viewport"===r)o=function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=e.ownerDocument.documentElement,r=S(e,n),i=Math.max(n.clientWidth,window.innerWidth||0),o=Math.max(n.clientHeight,window.innerHeight||0),a=t?0:m(n),s=t?0:m(n,"left");return T({top:a-r.top+r.marginTop,left:s-r.left+r.marginLeft,width:i,height:o})}(a,i);else{var s=void 0;"scrollParent"===r?"BODY"===(s=l(c(t))).nodeName&&(s=e.ownerDocument.documentElement):s="window"===r?e.ownerDocument.documentElement:r;var f=S(s,a,i);if("HTML"!==s.nodeName||function e(t){var n=t.nodeName;return"BODY"!==n&&"HTML"!==n&&("fixed"===u(t,"position")||e(c(t)))}(a))o=f;else{var p=b(),d=p.height,h=p.width;o.top+=f.top-f.marginTop,o.bottom=d+f.top,o.left+=f.left-f.marginLeft,o.right=h+f.left}}return o.left+=n,o.top+=n,o.right-=n,o.bottom-=n,o}function D(e,t,n,r,i){var o=arguments.length>5&&void 0!==arguments[5]?arguments[5]:0;if(-1===e.indexOf("auto"))return e;var a=O(n,r,o,i),s={top:{width:a.width,height:t.top-a.top},right:{width:a.right-t.right,height:a.height},bottom:{width:a.width,height:a.bottom-t.bottom},left:{width:t.left-a.left,height:a.height}},u=Object.keys(s).map(function(e){return E({key:e},s[e],{area:(t=s[e],t.width*t.height)});var t}).sort(function(e,t){return t.area-e.area}),c=u.filter(function(e){var t=e.width,r=e.height;return t>=n.clientWidth&&r>=n.clientHeight}),l=c.length>0?c[0].key:u[0].key,f=e.split("-")[1];return l+(f?"-"+f:"")}function I(e,t,n){var r=arguments.length>3&&void 0!==arguments[3]?arguments[3]:null;return S(n,r?k(t):g(t,n),r)}function N(e){var t=getComputedStyle(e),n=parseFloat(t.marginTop)+parseFloat(t.marginBottom),r=parseFloat(t.marginLeft)+parseFloat(t.marginRight);return{width:e.offsetWidth+r,height:e.offsetHeight+n}}function j(e){var t={left:"right",right:"left",bottom:"top",top:"bottom"};return e.replace(/left|right|bottom|top/g,function(e){return t[e]})}function L(e,t,n){n=n.split("-")[0];var r=N(e),i={width:r.width,height:r.height},o=-1!==["right","left"].indexOf(n),a=o?"top":"left",s=o?"left":"top",u=o?"height":"width",c=o?"width":"height";return i[a]=t[a]+t[u]/2-r[u]/2,i[s]=n===s?t[s]-r[c]:t[j(s)],i}function $(e,t){return Array.prototype.find?e.find(t):e.filter(t)[0]}function P(e,t,n){return(void 0===n?e:e.slice(0,function(e,t,n){if(Array.prototype.findIndex)return e.findIndex(function(e){return e[t]===n});var r=$(e,function(e){return e[t]===n});return e.indexOf(r)}(e,"name",n))).forEach(function(e){e.function&&console.warn("`modifier.function` is deprecated, use `modifier.fn`!");var n=e.function||e.fn;e.enabled&&s(n)&&(t.offsets.popper=T(t.offsets.popper),t.offsets.reference=T(t.offsets.reference),t=n(t,e))}),t}function R(e,t){return e.some(function(e){var n=e.name;return e.enabled&&n===t})}function M(e){for(var t=[!1,"ms","Webkit","Moz","O"],n=e.charAt(0).toUpperCase()+e.slice(1),r=0;r<t.length;r++){var i=t[r],o=i?""+i+n:e;if(void 0!==document.body.style[o])return o}return null}function H(e){var t=e.ownerDocument;return t?t.defaultView:window}function F(e,t,n,r){n.updateBound=r,H(e).addEventListener("resize",n.updateBound,{passive:!0});var i=l(e);return function e(t,n,r,i){var o="BODY"===t.nodeName,a=o?t.ownerDocument.defaultView:t;a.addEventListener(n,r,{passive:!0}),o||e(l(a.parentNode),n,r,i),i.push(a)}(i,"scroll",n.updateBound,n.scrollParents),n.scrollElement=i,n.eventsEnabled=!0,n}function q(){var e,t;this.state.eventsEnabled&&(cancelAnimationFrame(this.scheduleUpdate),this.state=(e=this.reference,t=this.state,H(e).removeEventListener("resize",t.updateBound),t.scrollParents.forEach(function(e){e.removeEventListener("scroll",t.updateBound)}),t.updateBound=null,t.scrollParents=[],t.scrollElement=null,t.eventsEnabled=!1,t))}function B(e){return""!==e&&!isNaN(parseFloat(e))&&isFinite(e)}function W(e,t){Object.keys(t).forEach(function(n){var r="";-1!==["width","height","top","right","bottom","left"].indexOf(n)&&B(t[n])&&(r="px"),e.style[n]=t[n]+r})}function U(e,t,n){var r=$(e,function(e){return e.name===t}),i=!!r&&e.some(function(e){return e.name===n&&e.enabled&&e.order<r.order});if(!i){var o="`"+t+"`",a="`"+n+"`";console.warn(a+" modifier is required by "+o+" modifier in order to work, be sure to include it before "+o+"!")}return i}var z=["auto-start","auto","auto-end","top-start","top","top-end","right-start","right","right-end","bottom-end","bottom","bottom-start","left-end","left","left-start"],V=z.slice(3);function K(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=V.indexOf(e),r=V.slice(n+1).concat(V.slice(0,n));return t?r.reverse():r}var Q={FLIP:"flip",CLOCKWISE:"clockwise",COUNTERCLOCKWISE:"counterclockwise"};function Y(e,t,n,r){var i=[0,0],o=-1!==["right","left"].indexOf(r),a=e.split(/(\+|\-)/).map(function(e){return e.trim()}),s=a.indexOf($(a,function(e){return-1!==e.search(/,|\s/)}));a[s]&&-1===a[s].indexOf(",")&&console.warn("Offsets separated by white space(s) are deprecated, use a comma (,) instead.");var u=/\s*,\s*|\s+/,c=-1!==s?[a.slice(0,s).concat([a[s].split(u)[0]]),[a[s].split(u)[1]].concat(a.slice(s+1))]:[a];return(c=c.map(function(e,r){var i=(1===r?!o:o)?"height":"width",a=!1;return e.reduce(function(e,t){return""===e[e.length-1]&&-1!==["+","-"].indexOf(t)?(e[e.length-1]=t,a=!0,e):a?(e[e.length-1]+=t,a=!1,e):e.concat(t)},[]).map(function(e){return function(e,t,n,r){var i=e.match(/((?:\-|\+)?\d*\.?\d*)(.*)/),o=+i[1],a=i[2];if(!o)return e;if(0===a.indexOf("%")){var s=void 0;switch(a){case"%p":s=n;break;case"%":case"%r":default:s=r}return T(s)[t]/100*o}if("vh"===a||"vw"===a)return("vh"===a?Math.max(document.documentElement.clientHeight,window.innerHeight||0):Math.max(document.documentElement.clientWidth,window.innerWidth||0))/100*o;return o}(e,i,t,n)})})).forEach(function(e,t){e.forEach(function(n,r){B(n)&&(i[t]+=n*("-"===e[r-1]?-1:1))})}),i}var X={placement:"bottom",positionFixed:!1,eventsEnabled:!0,removeOnDestroy:!1,onCreate:function(){},onUpdate:function(){},modifiers:{shift:{order:100,enabled:!0,fn:function(e){var t=e.placement,n=t.split("-")[0],r=t.split("-")[1];if(r){var i=e.offsets,o=i.reference,a=i.popper,s=-1!==["bottom","top"].indexOf(n),u=s?"left":"top",c=s?"width":"height",l={start:C({},u,o[u]),end:C({},u,o[u]+o[c]-a[c])};e.offsets.popper=E({},a,l[r])}return e}},offset:{order:200,enabled:!0,fn:function(e,t){var n=t.offset,r=e.placement,i=e.offsets,o=i.popper,a=i.reference,s=r.split("-")[0],u=void 0;return u=B(+n)?[+n,0]:Y(n,o,a,s),"left"===s?(o.top+=u[0],o.left-=u[1]):"right"===s?(o.top+=u[0],o.left+=u[1]):"top"===s?(o.left+=u[0],o.top-=u[1]):"bottom"===s&&(o.left+=u[0],o.top+=u[1]),e.popper=o,e},offset:0},preventOverflow:{order:300,enabled:!0,fn:function(e,t){var n=t.boundariesElement||h(e.instance.popper);e.instance.reference===n&&(n=h(n));var r=M("transform"),i=e.instance.popper.style,o=i.top,a=i.left,s=i[r];i.top="",i.left="",i[r]="";var u=O(e.instance.popper,e.instance.reference,t.padding,n,e.positionFixed);i.top=o,i.left=a,i[r]=s,t.boundaries=u;var c=t.priority,l=e.offsets.popper,f={primary:function(e){var n=l[e];return l[e]<u[e]&&!t.escapeWithReference&&(n=Math.max(l[e],u[e])),C({},e,n)},secondary:function(e){var n="right"===e?"left":"top",r=l[n];return l[e]>u[e]&&!t.escapeWithReference&&(r=Math.min(l[n],u[e]-("right"===e?l.width:l.height))),C({},n,r)}};return c.forEach(function(e){var t=-1!==["left","top"].indexOf(e)?"primary":"secondary";l=E({},l,f[t](e))}),e.offsets.popper=l,e},priority:["left","right","top","bottom"],padding:5,boundariesElement:"scrollParent"},keepTogether:{order:400,enabled:!0,fn:function(e){var t=e.offsets,n=t.popper,r=t.reference,i=e.placement.split("-")[0],o=Math.floor,a=-1!==["top","bottom"].indexOf(i),s=a?"right":"bottom",u=a?"left":"top",c=a?"width":"height";return n[s]<o(r[u])&&(e.offsets.popper[u]=o(r[u])-n[c]),n[u]>o(r[s])&&(e.offsets.popper[u]=o(r[s])),e}},arrow:{order:500,enabled:!0,fn:function(e,t){var n;if(!U(e.instance.modifiers,"arrow","keepTogether"))return e;var r=t.element;if("string"==typeof r){if(!(r=e.instance.popper.querySelector(r)))return e}else if(!e.instance.popper.contains(r))return console.warn("WARNING: `arrow.element` must be child of its popper element!"),e;var i=e.placement.split("-")[0],o=e.offsets,a=o.popper,s=o.reference,c=-1!==["left","right"].indexOf(i),l=c?"height":"width",f=c?"Top":"Left",p=f.toLowerCase(),d=c?"left":"top",h=c?"bottom":"right",v=N(r)[l];s[h]-v<a[p]&&(e.offsets.popper[p]-=a[p]-(s[h]-v)),s[p]+v>a[h]&&(e.offsets.popper[p]+=s[p]+v-a[h]),e.offsets.popper=T(e.offsets.popper);var g=s[p]+s[l]/2-v/2,m=u(e.instance.popper),y=parseFloat(m["margin"+f],10),_=parseFloat(m["border"+f+"Width"],10),b=g-e.offsets.popper[p]-y-_;return b=Math.max(Math.min(a[l]-v,b),0),e.arrowElement=r,e.offsets.arrow=(C(n={},p,Math.round(b)),C(n,d,""),n),e},element:"[x-arrow]"},flip:{order:600,enabled:!0,fn:function(e,t){if(R(e.instance.modifiers,"inner"))return e;if(e.flipped&&e.placement===e.originalPlacement)return e;var n=O(e.instance.popper,e.instance.reference,t.padding,t.boundariesElement,e.positionFixed),r=e.placement.split("-")[0],i=j(r),o=e.placement.split("-")[1]||"",a=[];switch(t.behavior){case Q.FLIP:a=[r,i];break;case Q.CLOCKWISE:a=K(r);break;case Q.COUNTERCLOCKWISE:a=K(r,!0);break;default:a=t.behavior}return a.forEach(function(s,u){if(r!==s||a.length===u+1)return e;r=e.placement.split("-")[0],i=j(r);var c=e.offsets.popper,l=e.offsets.reference,f=Math.floor,p="left"===r&&f(c.right)>f(l.left)||"right"===r&&f(c.left)<f(l.right)||"top"===r&&f(c.bottom)>f(l.top)||"bottom"===r&&f(c.top)<f(l.bottom),d=f(c.left)<f(n.left),h=f(c.right)>f(n.right),v=f(c.top)<f(n.top),g=f(c.bottom)>f(n.bottom),m="left"===r&&d||"right"===r&&h||"top"===r&&v||"bottom"===r&&g,y=-1!==["top","bottom"].indexOf(r),_=!!t.flipVariations&&(y&&"start"===o&&d||y&&"end"===o&&h||!y&&"start"===o&&v||!y&&"end"===o&&g);(p||m||_)&&(e.flipped=!0,(p||m)&&(r=a[u+1]),_&&(o=function(e){return"end"===e?"start":"start"===e?"end":e}(o)),e.placement=r+(o?"-"+o:""),e.offsets.popper=E({},e.offsets.popper,L(e.instance.popper,e.offsets.reference,e.placement)),e=P(e.instance.modifiers,e,"flip"))}),e},behavior:"flip",padding:5,boundariesElement:"viewport"},inner:{order:700,enabled:!1,fn:function(e){var t=e.placement,n=t.split("-")[0],r=e.offsets,i=r.popper,o=r.reference,a=-1!==["left","right"].indexOf(n),s=-1===["top","left"].indexOf(n);return i[a?"left":"top"]=o[n]-(s?i[a?"width":"height"]:0),e.placement=j(t),e.offsets.popper=T(i),e}},hide:{order:800,enabled:!0,fn:function(e){if(!U(e.instance.modifiers,"hide","preventOverflow"))return e;var t=e.offsets.reference,n=$(e.instance.modifiers,function(e){return"preventOverflow"===e.name}).boundaries;if(t.bottom<n.top||t.left>n.right||t.top>n.bottom||t.right<n.left){if(!0===e.hide)return e;e.hide=!0,e.attributes["x-out-of-boundaries"]=""}else{if(!1===e.hide)return e;e.hide=!1,e.attributes["x-out-of-boundaries"]=!1}return e}},computeStyle:{order:850,enabled:!0,fn:function(e,t){var n=t.x,r=t.y,i=e.offsets.popper,o=$(e.instance.modifiers,function(e){return"applyStyle"===e.name}).gpuAcceleration;void 0!==o&&console.warn("WARNING: `gpuAcceleration` option moved to `computeStyle` modifier and will not be supported in future versions of Popper.js!");var a=void 0!==o?o:t.gpuAcceleration,s=A(h(e.instance.popper)),u={position:i.position},c={left:Math.floor(i.left),top:Math.round(i.top),bottom:Math.round(i.bottom),right:Math.floor(i.right)},l="bottom"===n?"top":"bottom",f="right"===r?"left":"right",p=M("transform"),d=void 0,v=void 0;if(v="bottom"===l?-s.height+c.bottom:c.top,d="right"===f?-s.width+c.right:c.left,a&&p)u[p]="translate3d("+d+"px, "+v+"px, 0)",u[l]=0,u[f]=0,u.willChange="transform";else{var g="bottom"===l?-1:1,m="right"===f?-1:1;u[l]=v*g,u[f]=d*m,u.willChange=l+", "+f}var y={"x-placement":e.placement};return e.attributes=E({},y,e.attributes),e.styles=E({},u,e.styles),e.arrowStyles=E({},e.offsets.arrow,e.arrowStyles),e},gpuAcceleration:!0,x:"bottom",y:"right"},applyStyle:{order:900,enabled:!0,fn:function(e){var t,n;return W(e.instance.popper,e.styles),t=e.instance.popper,n=e.attributes,Object.keys(n).forEach(function(e){!1!==n[e]?t.setAttribute(e,n[e]):t.removeAttribute(e)}),e.arrowElement&&Object.keys(e.arrowStyles).length&&W(e.arrowElement,e.arrowStyles),e},onLoad:function(e,t,n,r,i){var o=I(i,t,e,n.positionFixed),a=D(n.placement,o,t,e,n.modifiers.flip.boundariesElement,n.modifiers.flip.padding);return t.setAttribute("x-placement",a),W(t,{position:n.positionFixed?"fixed":"absolute"}),n},gpuAcceleration:void 0}}},G=function(){function e(t,n){var r=this,i=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};w(this,e),this.scheduleUpdate=function(){return requestAnimationFrame(r.update)},this.update=a(this.update.bind(this)),this.options=E({},e.Defaults,i),this.state={isDestroyed:!1,isCreated:!1,scrollParents:[]},this.reference=t&&t.jquery?t[0]:t,this.popper=n&&n.jquery?n[0]:n,this.options.modifiers={},Object.keys(E({},e.Defaults.modifiers,i.modifiers)).forEach(function(t){r.options.modifiers[t]=E({},e.Defaults.modifiers[t]||{},i.modifiers?i.modifiers[t]:{})}),this.modifiers=Object.keys(this.options.modifiers).map(function(e){return E({name:e},r.options.modifiers[e])}).sort(function(e,t){return e.order-t.order}),this.modifiers.forEach(function(e){e.enabled&&s(e.onLoad)&&e.onLoad(r.reference,r.popper,r.options,e,r.state)}),this.update();var o=this.options.eventsEnabled;o&&this.enableEventListeners(),this.state.eventsEnabled=o}return x(e,[{key:"update",value:function(){return function(){if(!this.state.isDestroyed){var e={instance:this,styles:{},arrowStyles:{},attributes:{},flipped:!1,offsets:{}};e.offsets.reference=I(this.state,this.popper,this.reference,this.options.positionFixed),e.placement=D(this.options.placement,e.offsets.reference,this.popper,this.reference,this.options.modifiers.flip.boundariesElement,this.options.modifiers.flip.padding),e.originalPlacement=e.placement,e.positionFixed=this.options.positionFixed,e.offsets.popper=L(this.popper,e.offsets.reference,e.placement),e.offsets.popper.position=this.options.positionFixed?"fixed":"absolute",e=P(this.modifiers,e),this.state.isCreated?this.options.onUpdate(e):(this.state.isCreated=!0,this.options.onCreate(e))}}.call(this)}},{key:"destroy",value:function(){return function(){return this.state.isDestroyed=!0,R(this.modifiers,"applyStyle")&&(this.popper.removeAttribute("x-placement"),this.popper.style.position="",this.popper.style.top="",this.popper.style.left="",this.popper.style.right="",this.popper.style.bottom="",this.popper.style.willChange="",this.popper.style[M("transform")]=""),this.disableEventListeners(),this.options.removeOnDestroy&&this.popper.parentNode.removeChild(this.popper),this}.call(this)}},{key:"enableEventListeners",value:function(){return function(){this.state.eventsEnabled||(this.state=F(this.reference,this.options,this.state,this.scheduleUpdate))}.call(this)}},{key:"disableEventListeners",value:function(){return q.call(this)}}]),e}();G.Utils=("undefined"!=typeof window?window:e).PopperUtils,G.placements=z,G.Defaults=X,t.default=G}.call(t,n(1))},function(e,t,n){var r;!function(t,n){"use strict";"object"==typeof e&&"object"==typeof e.exports?e.exports=t.document?n(t,!0):function(e){if(!e.document)throw new Error("jQuery requires a window with a document");return n(e)}:n(t)}("undefined"!=typeof window?window:this,function(n,i){"use strict";var o=[],a=n.document,s=Object.getPrototypeOf,u=o.slice,c=o.concat,l=o.push,f=o.indexOf,p={},d=p.toString,h=p.hasOwnProperty,v=h.toString,g=v.call(Object),m={},y=function(e){return"function"==typeof e&&"number"!=typeof e.nodeType},_=function(e){return null!=e&&e===e.window},b={type:!0,src:!0,noModule:!0};function w(e,t,n){var r,i=(t=t||a).createElement("script");if(i.text=e,n)for(r in b)n[r]&&(i[r]=n[r]);t.head.appendChild(i).parentNode.removeChild(i)}function x(e){return null==e?e+"":"object"==typeof e||"function"==typeof e?p[d.call(e)]||"object":typeof e}var C=function(e,t){return new C.fn.init(e,t)},E=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;function T(e){var t=!!e&&"length"in e&&e.length,n=x(e);return!y(e)&&!_(e)&&("array"===n||0===t||"number"==typeof t&&t>0&&t-1 in e)}C.fn=C.prototype={jquery:"3.3.1",constructor:C,length:0,toArray:function(){return u.call(this)},get:function(e){return null==e?u.call(this):e<0?this[e+this.length]:this[e]},pushStack:function(e){var t=C.merge(this.constructor(),e);return t.prevObject=this,t},each:function(e){return C.each(this,e)},map:function(e){return this.pushStack(C.map(this,function(t,n){return e.call(t,n,t)}))},slice:function(){return this.pushStack(u.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(e){var t=this.length,n=+e+(e<0?t:0);return this.pushStack(n>=0&&n<t?[this[n]]:[])},end:function(){return this.prevObject||this.constructor()},push:l,sort:o.sort,splice:o.splice},C.extend=C.fn.extend=function(){var e,t,n,r,i,o,a=arguments[0]||{},s=1,u=arguments.length,c=!1;for("boolean"==typeof a&&(c=a,a=arguments[s]||{},s++),"object"==typeof a||y(a)||(a={}),s===u&&(a=this,s--);s<u;s++)if(null!=(e=arguments[s]))for(t in e)n=a[t],a!==(r=e[t])&&(c&&r&&(C.isPlainObject(r)||(i=Array.isArray(r)))?(i?(i=!1,o=n&&Array.isArray(n)?n:[]):o=n&&C.isPlainObject(n)?n:{},a[t]=C.extend(c,o,r)):void 0!==r&&(a[t]=r));return a},C.extend({expando:"jQuery"+("3.3.1"+Math.random()).replace(/\D/g,""),isReady:!0,error:function(e){throw new Error(e)},noop:function(){},isPlainObject:function(e){var t,n;return!(!e||"[object Object]"!==d.call(e))&&(!(t=s(e))||"function"==typeof(n=h.call(t,"constructor")&&t.constructor)&&v.call(n)===g)},isEmptyObject:function(e){var t;for(t in e)return!1;return!0},globalEval:function(e){w(e)},each:function(e,t){var n,r=0;if(T(e))for(n=e.length;r<n&&!1!==t.call(e[r],r,e[r]);r++);else for(r in e)if(!1===t.call(e[r],r,e[r]))break;return e},trim:function(e){return null==e?"":(e+"").replace(E,"")},makeArray:function(e,t){var n=t||[];return null!=e&&(T(Object(e))?C.merge(n,"string"==typeof e?[e]:e):l.call(n,e)),n},inArray:function(e,t,n){return null==t?-1:f.call(t,e,n)},merge:function(e,t){for(var n=+t.length,r=0,i=e.length;r<n;r++)e[i++]=t[r];return e.length=i,e},grep:function(e,t,n){for(var r=[],i=0,o=e.length,a=!n;i<o;i++)!t(e[i],i)!==a&&r.push(e[i]);return r},map:function(e,t,n){var r,i,o=0,a=[];if(T(e))for(r=e.length;o<r;o++)null!=(i=t(e[o],o,n))&&a.push(i);else for(o in e)null!=(i=t(e[o],o,n))&&a.push(i);return c.apply([],a)},guid:1,support:m}),"function"==typeof Symbol&&(C.fn[Symbol.iterator]=o[Symbol.iterator]),C.each("Boolean Number String Function Array Date RegExp Object Error Symbol".split(" "),function(e,t){p["[object "+t+"]"]=t.toLowerCase()});var A=function(e){var t,n,r,i,o,a,s,u,c,l,f,p,d,h,v,g,m,y,_,b="sizzle"+1*new Date,w=e.document,x=0,C=0,E=ae(),T=ae(),A=ae(),S=function(e,t){return e===t&&(f=!0),0},k={}.hasOwnProperty,O=[],D=O.pop,I=O.push,N=O.push,j=O.slice,L=function(e,t){for(var n=0,r=e.length;n<r;n++)if(e[n]===t)return n;return-1},$="checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",P="[\\x20\\t\\r\\n\\f]",R="(?:\\\\.|[\\w-]|[^\0-\\xa0])+",M="\\["+P+"*("+R+")(?:"+P+"*([*^$|!~]?=)"+P+"*(?:'((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\"|("+R+"))|)"+P+"*\\]",H=":("+R+")(?:\\((('((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\")|((?:\\\\.|[^\\\\()[\\]]|"+M+")*)|.*)\\)|)",F=new RegExp(P+"+","g"),q=new RegExp("^"+P+"+|((?:^|[^\\\\])(?:\\\\.)*)"+P+"+$","g"),B=new RegExp("^"+P+"*,"+P+"*"),W=new RegExp("^"+P+"*([>+~]|"+P+")"+P+"*"),U=new RegExp("="+P+"*([^\\]'\"]*?)"+P+"*\\]","g"),z=new RegExp(H),V=new RegExp("^"+R+"$"),K={ID:new RegExp("^#("+R+")"),CLASS:new RegExp("^\\.("+R+")"),TAG:new RegExp("^("+R+"|[*])"),ATTR:new RegExp("^"+M),PSEUDO:new RegExp("^"+H),CHILD:new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\("+P+"*(even|odd|(([+-]|)(\\d*)n|)"+P+"*(?:([+-]|)"+P+"*(\\d+)|))"+P+"*\\)|)","i"),bool:new RegExp("^(?:"+$+")$","i"),needsContext:new RegExp("^"+P+"*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\("+P+"*((?:-\\d)?\\d*)"+P+"*\\)|)(?=[^-]|$)","i")},Q=/^(?:input|select|textarea|button)$/i,Y=/^h\d$/i,X=/^[^{]+\{\s*\[native \w/,G=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,J=/[+~]/,Z=new RegExp("\\\\([\\da-f]{1,6}"+P+"?|("+P+")|.)","ig"),ee=function(e,t,n){var r="0x"+t-65536;return r!=r||n?t:r<0?String.fromCharCode(r+65536):String.fromCharCode(r>>10|55296,1023&r|56320)},te=/([\0-\x1f\x7f]|^-?\d)|^-$|[^\0-\x1f\x7f-\uFFFF\w-]/g,ne=function(e,t){return t?"\0"===e?"�":e.slice(0,-1)+"\\"+e.charCodeAt(e.length-1).toString(16)+" ":"\\"+e},re=function(){p()},ie=ye(function(e){return!0===e.disabled&&("form"in e||"label"in e)},{dir:"parentNode",next:"legend"});try{N.apply(O=j.call(w.childNodes),w.childNodes),O[w.childNodes.length].nodeType}catch(e){N={apply:O.length?function(e,t){I.apply(e,j.call(t))}:function(e,t){for(var n=e.length,r=0;e[n++]=t[r++];);e.length=n-1}}}function oe(e,t,r,i){var o,s,c,l,f,h,m,y=t&&t.ownerDocument,x=t?t.nodeType:9;if(r=r||[],"string"!=typeof e||!e||1!==x&&9!==x&&11!==x)return r;if(!i&&((t?t.ownerDocument||t:w)!==d&&p(t),t=t||d,v)){if(11!==x&&(f=G.exec(e)))if(o=f[1]){if(9===x){if(!(c=t.getElementById(o)))return r;if(c.id===o)return r.push(c),r}else if(y&&(c=y.getElementById(o))&&_(t,c)&&c.id===o)return r.push(c),r}else{if(f[2])return N.apply(r,t.getElementsByTagName(e)),r;if((o=f[3])&&n.getElementsByClassName&&t.getElementsByClassName)return N.apply(r,t.getElementsByClassName(o)),r}if(n.qsa&&!A[e+" "]&&(!g||!g.test(e))){if(1!==x)y=t,m=e;else if("object"!==t.nodeName.toLowerCase()){for((l=t.getAttribute("id"))?l=l.replace(te,ne):t.setAttribute("id",l=b),s=(h=a(e)).length;s--;)h[s]="#"+l+" "+me(h[s]);m=h.join(","),y=J.test(e)&&ve(t.parentNode)||t}if(m)try{return N.apply(r,y.querySelectorAll(m)),r}catch(e){}finally{l===b&&t.removeAttribute("id")}}}return u(e.replace(q,"$1"),t,r,i)}function ae(){var e=[];return function t(n,i){return e.push(n+" ")>r.cacheLength&&delete t[e.shift()],t[n+" "]=i}}function se(e){return e[b]=!0,e}function ue(e){var t=d.createElement("fieldset");try{return!!e(t)}catch(e){return!1}finally{t.parentNode&&t.parentNode.removeChild(t),t=null}}function ce(e,t){for(var n=e.split("|"),i=n.length;i--;)r.attrHandle[n[i]]=t}function le(e,t){var n=t&&e,r=n&&1===e.nodeType&&1===t.nodeType&&e.sourceIndex-t.sourceIndex;if(r)return r;if(n)for(;n=n.nextSibling;)if(n===t)return-1;return e?1:-1}function fe(e){return function(t){return"input"===t.nodeName.toLowerCase()&&t.type===e}}function pe(e){return function(t){var n=t.nodeName.toLowerCase();return("input"===n||"button"===n)&&t.type===e}}function de(e){return function(t){return"form"in t?t.parentNode&&!1===t.disabled?"label"in t?"label"in t.parentNode?t.parentNode.disabled===e:t.disabled===e:t.isDisabled===e||t.isDisabled!==!e&&ie(t)===e:t.disabled===e:"label"in t&&t.disabled===e}}function he(e){return se(function(t){return t=+t,se(function(n,r){for(var i,o=e([],n.length,t),a=o.length;a--;)n[i=o[a]]&&(n[i]=!(r[i]=n[i]))})})}function ve(e){return e&&void 0!==e.getElementsByTagName&&e}for(t in n=oe.support={},o=oe.isXML=function(e){var t=e&&(e.ownerDocument||e).documentElement;return!!t&&"HTML"!==t.nodeName},p=oe.setDocument=function(e){var t,i,a=e?e.ownerDocument||e:w;return a!==d&&9===a.nodeType&&a.documentElement?(h=(d=a).documentElement,v=!o(d),w!==d&&(i=d.defaultView)&&i.top!==i&&(i.addEventListener?i.addEventListener("unload",re,!1):i.attachEvent&&i.attachEvent("onunload",re)),n.attributes=ue(function(e){return e.className="i",!e.getAttribute("className")}),n.getElementsByTagName=ue(function(e){return e.appendChild(d.createComment("")),!e.getElementsByTagName("*").length}),n.getElementsByClassName=X.test(d.getElementsByClassName),n.getById=ue(function(e){return h.appendChild(e).id=b,!d.getElementsByName||!d.getElementsByName(b).length}),n.getById?(r.filter.ID=function(e){var t=e.replace(Z,ee);return function(e){return e.getAttribute("id")===t}},r.find.ID=function(e,t){if(void 0!==t.getElementById&&v){var n=t.getElementById(e);return n?[n]:[]}}):(r.filter.ID=function(e){var t=e.replace(Z,ee);return function(e){var n=void 0!==e.getAttributeNode&&e.getAttributeNode("id");return n&&n.value===t}},r.find.ID=function(e,t){if(void 0!==t.getElementById&&v){var n,r,i,o=t.getElementById(e);if(o){if((n=o.getAttributeNode("id"))&&n.value===e)return[o];for(i=t.getElementsByName(e),r=0;o=i[r++];)if((n=o.getAttributeNode("id"))&&n.value===e)return[o]}return[]}}),r.find.TAG=n.getElementsByTagName?function(e,t){return void 0!==t.getElementsByTagName?t.getElementsByTagName(e):n.qsa?t.querySelectorAll(e):void 0}:function(e,t){var n,r=[],i=0,o=t.getElementsByTagName(e);if("*"===e){for(;n=o[i++];)1===n.nodeType&&r.push(n);return r}return o},r.find.CLASS=n.getElementsByClassName&&function(e,t){if(void 0!==t.getElementsByClassName&&v)return t.getElementsByClassName(e)},m=[],g=[],(n.qsa=X.test(d.querySelectorAll))&&(ue(function(e){h.appendChild(e).innerHTML="<a id='"+b+"'></a><select id='"+b+"-\r\\' msallowcapture=''><option selected=''></option></select>",e.querySelectorAll("[msallowcapture^='']").length&&g.push("[*^$]="+P+"*(?:''|\"\")"),e.querySelectorAll("[selected]").length||g.push("\\["+P+"*(?:value|"+$+")"),e.querySelectorAll("[id~="+b+"-]").length||g.push("~="),e.querySelectorAll(":checked").length||g.push(":checked"),e.querySelectorAll("a#"+b+"+*").length||g.push(".#.+[+~]")}),ue(function(e){e.innerHTML="<a href='' disabled='disabled'></a><select disabled='disabled'><option/></select>";var t=d.createElement("input");t.setAttribute("type","hidden"),e.appendChild(t).setAttribute("name","D"),e.querySelectorAll("[name=d]").length&&g.push("name"+P+"*[*^$|!~]?="),2!==e.querySelectorAll(":enabled").length&&g.push(":enabled",":disabled"),h.appendChild(e).disabled=!0,2!==e.querySelectorAll(":disabled").length&&g.push(":enabled",":disabled"),e.querySelectorAll("*,:x"),g.push(",.*:")})),(n.matchesSelector=X.test(y=h.matches||h.webkitMatchesSelector||h.mozMatchesSelector||h.oMatchesSelector||h.msMatchesSelector))&&ue(function(e){n.disconnectedMatch=y.call(e,"*"),y.call(e,"[s!='']:x"),m.push("!=",H)}),g=g.length&&new RegExp(g.join("|")),m=m.length&&new RegExp(m.join("|")),t=X.test(h.compareDocumentPosition),_=t||X.test(h.contains)?function(e,t){var n=9===e.nodeType?e.documentElement:e,r=t&&t.parentNode;return e===r||!(!r||1!==r.nodeType||!(n.contains?n.contains(r):e.compareDocumentPosition&&16&e.compareDocumentPosition(r)))}:function(e,t){if(t)for(;t=t.parentNode;)if(t===e)return!0;return!1},S=t?function(e,t){if(e===t)return f=!0,0;var r=!e.compareDocumentPosition-!t.compareDocumentPosition;return r||(1&(r=(e.ownerDocument||e)===(t.ownerDocument||t)?e.compareDocumentPosition(t):1)||!n.sortDetached&&t.compareDocumentPosition(e)===r?e===d||e.ownerDocument===w&&_(w,e)?-1:t===d||t.ownerDocument===w&&_(w,t)?1:l?L(l,e)-L(l,t):0:4&r?-1:1)}:function(e,t){if(e===t)return f=!0,0;var n,r=0,i=e.parentNode,o=t.parentNode,a=[e],s=[t];if(!i||!o)return e===d?-1:t===d?1:i?-1:o?1:l?L(l,e)-L(l,t):0;if(i===o)return le(e,t);for(n=e;n=n.parentNode;)a.unshift(n);for(n=t;n=n.parentNode;)s.unshift(n);for(;a[r]===s[r];)r++;return r?le(a[r],s[r]):a[r]===w?-1:s[r]===w?1:0},d):d},oe.matches=function(e,t){return oe(e,null,null,t)},oe.matchesSelector=function(e,t){if((e.ownerDocument||e)!==d&&p(e),t=t.replace(U,"='$1']"),n.matchesSelector&&v&&!A[t+" "]&&(!m||!m.test(t))&&(!g||!g.test(t)))try{var r=y.call(e,t);if(r||n.disconnectedMatch||e.document&&11!==e.document.nodeType)return r}catch(e){}return oe(t,d,null,[e]).length>0},oe.contains=function(e,t){return(e.ownerDocument||e)!==d&&p(e),_(e,t)},oe.attr=function(e,t){(e.ownerDocument||e)!==d&&p(e);var i=r.attrHandle[t.toLowerCase()],o=i&&k.call(r.attrHandle,t.toLowerCase())?i(e,t,!v):void 0;return void 0!==o?o:n.attributes||!v?e.getAttribute(t):(o=e.getAttributeNode(t))&&o.specified?o.value:null},oe.escape=function(e){return(e+"").replace(te,ne)},oe.error=function(e){throw new Error("Syntax error, unrecognized expression: "+e)},oe.uniqueSort=function(e){var t,r=[],i=0,o=0;if(f=!n.detectDuplicates,l=!n.sortStable&&e.slice(0),e.sort(S),f){for(;t=e[o++];)t===e[o]&&(i=r.push(o));for(;i--;)e.splice(r[i],1)}return l=null,e},i=oe.getText=function(e){var t,n="",r=0,o=e.nodeType;if(o){if(1===o||9===o||11===o){if("string"==typeof e.textContent)return e.textContent;for(e=e.firstChild;e;e=e.nextSibling)n+=i(e)}else if(3===o||4===o)return e.nodeValue}else for(;t=e[r++];)n+=i(t);return n},(r=oe.selectors={cacheLength:50,createPseudo:se,match:K,attrHandle:{},find:{},relative:{">":{dir:"parentNode",first:!0}," ":{dir:"parentNode"},"+":{dir:"previousSibling",first:!0},"~":{dir:"previousSibling"}},preFilter:{ATTR:function(e){return e[1]=e[1].replace(Z,ee),e[3]=(e[3]||e[4]||e[5]||"").replace(Z,ee),"~="===e[2]&&(e[3]=" "+e[3]+" "),e.slice(0,4)},CHILD:function(e){return e[1]=e[1].toLowerCase(),"nth"===e[1].slice(0,3)?(e[3]||oe.error(e[0]),e[4]=+(e[4]?e[5]+(e[6]||1):2*("even"===e[3]||"odd"===e[3])),e[5]=+(e[7]+e[8]||"odd"===e[3])):e[3]&&oe.error(e[0]),e},PSEUDO:function(e){var t,n=!e[6]&&e[2];return K.CHILD.test(e[0])?null:(e[3]?e[2]=e[4]||e[5]||"":n&&z.test(n)&&(t=a(n,!0))&&(t=n.indexOf(")",n.length-t)-n.length)&&(e[0]=e[0].slice(0,t),e[2]=n.slice(0,t)),e.slice(0,3))}},filter:{TAG:function(e){var t=e.replace(Z,ee).toLowerCase();return"*"===e?function(){return!0}:function(e){return e.nodeName&&e.nodeName.toLowerCase()===t}},CLASS:function(e){var t=E[e+" "];return t||(t=new RegExp("(^|"+P+")"+e+"("+P+"|$)"))&&E(e,function(e){return t.test("string"==typeof e.className&&e.className||void 0!==e.getAttribute&&e.getAttribute("class")||"")})},ATTR:function(e,t,n){return function(r){var i=oe.attr(r,e);return null==i?"!="===t:!t||(i+="","="===t?i===n:"!="===t?i!==n:"^="===t?n&&0===i.indexOf(n):"*="===t?n&&i.indexOf(n)>-1:"$="===t?n&&i.slice(-n.length)===n:"~="===t?(" "+i.replace(F," ")+" ").indexOf(n)>-1:"|="===t&&(i===n||i.slice(0,n.length+1)===n+"-"))}},CHILD:function(e,t,n,r,i){var o="nth"!==e.slice(0,3),a="last"!==e.slice(-4),s="of-type"===t;return 1===r&&0===i?function(e){return!!e.parentNode}:function(t,n,u){var c,l,f,p,d,h,v=o!==a?"nextSibling":"previousSibling",g=t.parentNode,m=s&&t.nodeName.toLowerCase(),y=!u&&!s,_=!1;if(g){if(o){for(;v;){for(p=t;p=p[v];)if(s?p.nodeName.toLowerCase()===m:1===p.nodeType)return!1;h=v="only"===e&&!h&&"nextSibling"}return!0}if(h=[a?g.firstChild:g.lastChild],a&&y){for(_=(d=(c=(l=(f=(p=g)[b]||(p[b]={}))[p.uniqueID]||(f[p.uniqueID]={}))[e]||[])[0]===x&&c[1])&&c[2],p=d&&g.childNodes[d];p=++d&&p&&p[v]||(_=d=0)||h.pop();)if(1===p.nodeType&&++_&&p===t){l[e]=[x,d,_];break}}else if(y&&(_=d=(c=(l=(f=(p=t)[b]||(p[b]={}))[p.uniqueID]||(f[p.uniqueID]={}))[e]||[])[0]===x&&c[1]),!1===_)for(;(p=++d&&p&&p[v]||(_=d=0)||h.pop())&&((s?p.nodeName.toLowerCase()!==m:1!==p.nodeType)||!++_||(y&&((l=(f=p[b]||(p[b]={}))[p.uniqueID]||(f[p.uniqueID]={}))[e]=[x,_]),p!==t)););return(_-=i)===r||_%r==0&&_/r>=0}}},PSEUDO:function(e,t){var n,i=r.pseudos[e]||r.setFilters[e.toLowerCase()]||oe.error("unsupported pseudo: "+e);return i[b]?i(t):i.length>1?(n=[e,e,"",t],r.setFilters.hasOwnProperty(e.toLowerCase())?se(function(e,n){for(var r,o=i(e,t),a=o.length;a--;)e[r=L(e,o[a])]=!(n[r]=o[a])}):function(e){return i(e,0,n)}):i}},pseudos:{not:se(function(e){var t=[],n=[],r=s(e.replace(q,"$1"));return r[b]?se(function(e,t,n,i){for(var o,a=r(e,null,i,[]),s=e.length;s--;)(o=a[s])&&(e[s]=!(t[s]=o))}):function(e,i,o){return t[0]=e,r(t,null,o,n),t[0]=null,!n.pop()}}),has:se(function(e){return function(t){return oe(e,t).length>0}}),contains:se(function(e){return e=e.replace(Z,ee),function(t){return(t.textContent||t.innerText||i(t)).indexOf(e)>-1}}),lang:se(function(e){return V.test(e||"")||oe.error("unsupported lang: "+e),e=e.replace(Z,ee).toLowerCase(),function(t){var n;do{if(n=v?t.lang:t.getAttribute("xml:lang")||t.getAttribute("lang"))return(n=n.toLowerCase())===e||0===n.indexOf(e+"-")}while((t=t.parentNode)&&1===t.nodeType);return!1}}),target:function(t){var n=e.location&&e.location.hash;return n&&n.slice(1)===t.id},root:function(e){return e===h},focus:function(e){return e===d.activeElement&&(!d.hasFocus||d.hasFocus())&&!!(e.type||e.href||~e.tabIndex)},enabled:de(!1),disabled:de(!0),checked:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&!!e.checked||"option"===t&&!!e.selected},selected:function(e){return e.parentNode&&e.parentNode.selectedIndex,!0===e.selected},empty:function(e){for(e=e.firstChild;e;e=e.nextSibling)if(e.nodeType<6)return!1;return!0},parent:function(e){return!r.pseudos.empty(e)},header:function(e){return Y.test(e.nodeName)},input:function(e){return Q.test(e.nodeName)},button:function(e){var t=e.nodeName.toLowerCase();return"input"===t&&"button"===e.type||"button"===t},text:function(e){var t;return"input"===e.nodeName.toLowerCase()&&"text"===e.type&&(null==(t=e.getAttribute("type"))||"text"===t.toLowerCase())},first:he(function(){return[0]}),last:he(function(e,t){return[t-1]}),eq:he(function(e,t,n){return[n<0?n+t:n]}),even:he(function(e,t){for(var n=0;n<t;n+=2)e.push(n);return e}),odd:he(function(e,t){for(var n=1;n<t;n+=2)e.push(n);return e}),lt:he(function(e,t,n){for(var r=n<0?n+t:n;--r>=0;)e.push(r);return e}),gt:he(function(e,t,n){for(var r=n<0?n+t:n;++r<t;)e.push(r);return e})}}).pseudos.nth=r.pseudos.eq,{radio:!0,checkbox:!0,file:!0,password:!0,image:!0})r.pseudos[t]=fe(t);for(t in{submit:!0,reset:!0})r.pseudos[t]=pe(t);function ge(){}function me(e){for(var t=0,n=e.length,r="";t<n;t++)r+=e[t].value;return r}function ye(e,t,n){var r=t.dir,i=t.next,o=i||r,a=n&&"parentNode"===o,s=C++;return t.first?function(t,n,i){for(;t=t[r];)if(1===t.nodeType||a)return e(t,n,i);return!1}:function(t,n,u){var c,l,f,p=[x,s];if(u){for(;t=t[r];)if((1===t.nodeType||a)&&e(t,n,u))return!0}else for(;t=t[r];)if(1===t.nodeType||a)if(l=(f=t[b]||(t[b]={}))[t.uniqueID]||(f[t.uniqueID]={}),i&&i===t.nodeName.toLowerCase())t=t[r]||t;else{if((c=l[o])&&c[0]===x&&c[1]===s)return p[2]=c[2];if(l[o]=p,p[2]=e(t,n,u))return!0}return!1}}function _e(e){return e.length>1?function(t,n,r){for(var i=e.length;i--;)if(!e[i](t,n,r))return!1;return!0}:e[0]}function be(e,t,n,r,i){for(var o,a=[],s=0,u=e.length,c=null!=t;s<u;s++)(o=e[s])&&(n&&!n(o,r,i)||(a.push(o),c&&t.push(s)));return a}function we(e,t,n,r,i,o){return r&&!r[b]&&(r=we(r)),i&&!i[b]&&(i=we(i,o)),se(function(o,a,s,u){var c,l,f,p=[],d=[],h=a.length,v=o||function(e,t,n){for(var r=0,i=t.length;r<i;r++)oe(e,t[r],n);return n}(t||"*",s.nodeType?[s]:s,[]),g=!e||!o&&t?v:be(v,p,e,s,u),m=n?i||(o?e:h||r)?[]:a:g;if(n&&n(g,m,s,u),r)for(c=be(m,d),r(c,[],s,u),l=c.length;l--;)(f=c[l])&&(m[d[l]]=!(g[d[l]]=f));if(o){if(i||e){if(i){for(c=[],l=m.length;l--;)(f=m[l])&&c.push(g[l]=f);i(null,m=[],c,u)}for(l=m.length;l--;)(f=m[l])&&(c=i?L(o,f):p[l])>-1&&(o[c]=!(a[c]=f))}}else m=be(m===a?m.splice(h,m.length):m),i?i(null,a,m,u):N.apply(a,m)})}function xe(e){for(var t,n,i,o=e.length,a=r.relative[e[0].type],s=a||r.relative[" "],u=a?1:0,l=ye(function(e){return e===t},s,!0),f=ye(function(e){return L(t,e)>-1},s,!0),p=[function(e,n,r){var i=!a&&(r||n!==c)||((t=n).nodeType?l(e,n,r):f(e,n,r));return t=null,i}];u<o;u++)if(n=r.relative[e[u].type])p=[ye(_e(p),n)];else{if((n=r.filter[e[u].type].apply(null,e[u].matches))[b]){for(i=++u;i<o&&!r.relative[e[i].type];i++);return we(u>1&&_e(p),u>1&&me(e.slice(0,u-1).concat({value:" "===e[u-2].type?"*":""})).replace(q,"$1"),n,u<i&&xe(e.slice(u,i)),i<o&&xe(e=e.slice(i)),i<o&&me(e))}p.push(n)}return _e(p)}return ge.prototype=r.filters=r.pseudos,r.setFilters=new ge,a=oe.tokenize=function(e,t){var n,i,o,a,s,u,c,l=T[e+" "];if(l)return t?0:l.slice(0);for(s=e,u=[],c=r.preFilter;s;){for(a in n&&!(i=B.exec(s))||(i&&(s=s.slice(i[0].length)||s),u.push(o=[])),n=!1,(i=W.exec(s))&&(n=i.shift(),o.push({value:n,type:i[0].replace(q," ")}),s=s.slice(n.length)),r.filter)!(i=K[a].exec(s))||c[a]&&!(i=c[a](i))||(n=i.shift(),o.push({value:n,type:a,matches:i}),s=s.slice(n.length));if(!n)break}return t?s.length:s?oe.error(e):T(e,u).slice(0)},s=oe.compile=function(e,t){var n,i=[],o=[],s=A[e+" "];if(!s){for(t||(t=a(e)),n=t.length;n--;)(s=xe(t[n]))[b]?i.push(s):o.push(s);(s=A(e,function(e,t){var n=t.length>0,i=e.length>0,o=function(o,a,s,u,l){var f,h,g,m=0,y="0",_=o&&[],b=[],w=c,C=o||i&&r.find.TAG("*",l),E=x+=null==w?1:Math.random()||.1,T=C.length;for(l&&(c=a===d||a||l);y!==T&&null!=(f=C[y]);y++){if(i&&f){for(h=0,a||f.ownerDocument===d||(p(f),s=!v);g=e[h++];)if(g(f,a||d,s)){u.push(f);break}l&&(x=E)}n&&((f=!g&&f)&&m--,o&&_.push(f))}if(m+=y,n&&y!==m){for(h=0;g=t[h++];)g(_,b,a,s);if(o){if(m>0)for(;y--;)_[y]||b[y]||(b[y]=D.call(u));b=be(b)}N.apply(u,b),l&&!o&&b.length>0&&m+t.length>1&&oe.uniqueSort(u)}return l&&(x=E,c=w),_};return n?se(o):o}(o,i))).selector=e}return s},u=oe.select=function(e,t,n,i){var o,u,c,l,f,p="function"==typeof e&&e,d=!i&&a(e=p.selector||e);if(n=n||[],1===d.length){if((u=d[0]=d[0].slice(0)).length>2&&"ID"===(c=u[0]).type&&9===t.nodeType&&v&&r.relative[u[1].type]){if(!(t=(r.find.ID(c.matches[0].replace(Z,ee),t)||[])[0]))return n;p&&(t=t.parentNode),e=e.slice(u.shift().value.length)}for(o=K.needsContext.test(e)?0:u.length;o--&&(c=u[o],!r.relative[l=c.type]);)if((f=r.find[l])&&(i=f(c.matches[0].replace(Z,ee),J.test(u[0].type)&&ve(t.parentNode)||t))){if(u.splice(o,1),!(e=i.length&&me(u)))return N.apply(n,i),n;break}}return(p||s(e,d))(i,t,!v,n,!t||J.test(e)&&ve(t.parentNode)||t),n},n.sortStable=b.split("").sort(S).join("")===b,n.detectDuplicates=!!f,p(),n.sortDetached=ue(function(e){return 1&e.compareDocumentPosition(d.createElement("fieldset"))}),ue(function(e){return e.innerHTML="<a href='#'></a>","#"===e.firstChild.getAttribute("href")})||ce("type|href|height|width",function(e,t,n){if(!n)return e.getAttribute(t,"type"===t.toLowerCase()?1:2)}),n.attributes&&ue(function(e){return e.innerHTML="<input/>",e.firstChild.setAttribute("value",""),""===e.firstChild.getAttribute("value")})||ce("value",function(e,t,n){if(!n&&"input"===e.nodeName.toLowerCase())return e.defaultValue}),ue(function(e){return null==e.getAttribute("disabled")})||ce($,function(e,t,n){var r;if(!n)return!0===e[t]?t.toLowerCase():(r=e.getAttributeNode(t))&&r.specified?r.value:null}),oe}(n);C.find=A,C.expr=A.selectors,C.expr[":"]=C.expr.pseudos,C.uniqueSort=C.unique=A.uniqueSort,C.text=A.getText,C.isXMLDoc=A.isXML,C.contains=A.contains,C.escapeSelector=A.escape;var S=function(e,t,n){for(var r=[],i=void 0!==n;(e=e[t])&&9!==e.nodeType;)if(1===e.nodeType){if(i&&C(e).is(n))break;r.push(e)}return r},k=function(e,t){for(var n=[];e;e=e.nextSibling)1===e.nodeType&&e!==t&&n.push(e);return n},O=C.expr.match.needsContext;function D(e,t){return e.nodeName&&e.nodeName.toLowerCase()===t.toLowerCase()}var I=/^<([a-z][^\/\0>:\x20\t\r\n\f]*)[\x20\t\r\n\f]*\/?>(?:<\/\1>|)$/i;function N(e,t,n){return y(t)?C.grep(e,function(e,r){return!!t.call(e,r,e)!==n}):t.nodeType?C.grep(e,function(e){return e===t!==n}):"string"!=typeof t?C.grep(e,function(e){return f.call(t,e)>-1!==n}):C.filter(t,e,n)}C.filter=function(e,t,n){var r=t[0];return n&&(e=":not("+e+")"),1===t.length&&1===r.nodeType?C.find.matchesSelector(r,e)?[r]:[]:C.find.matches(e,C.grep(t,function(e){return 1===e.nodeType}))},C.fn.extend({find:function(e){var t,n,r=this.length,i=this;if("string"!=typeof e)return this.pushStack(C(e).filter(function(){for(t=0;t<r;t++)if(C.contains(i[t],this))return!0}));for(n=this.pushStack([]),t=0;t<r;t++)C.find(e,i[t],n);return r>1?C.uniqueSort(n):n},filter:function(e){return this.pushStack(N(this,e||[],!1))},not:function(e){return this.pushStack(N(this,e||[],!0))},is:function(e){return!!N(this,"string"==typeof e&&O.test(e)?C(e):e||[],!1).length}});var j,L=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]+))$/;(C.fn.init=function(e,t,n){var r,i;if(!e)return this;if(n=n||j,"string"==typeof e){if(!(r="<"===e[0]&&">"===e[e.length-1]&&e.length>=3?[null,e,null]:L.exec(e))||!r[1]&&t)return!t||t.jquery?(t||n).find(e):this.constructor(t).find(e);if(r[1]){if(t=t instanceof C?t[0]:t,C.merge(this,C.parseHTML(r[1],t&&t.nodeType?t.ownerDocument||t:a,!0)),I.test(r[1])&&C.isPlainObject(t))for(r in t)y(this[r])?this[r](t[r]):this.attr(r,t[r]);return this}return(i=a.getElementById(r[2]))&&(this[0]=i,this.length=1),this}return e.nodeType?(this[0]=e,this.length=1,this):y(e)?void 0!==n.ready?n.ready(e):e(C):C.makeArray(e,this)}).prototype=C.fn,j=C(a);var $=/^(?:parents|prev(?:Until|All))/,P={children:!0,contents:!0,next:!0,prev:!0};function R(e,t){for(;(e=e[t])&&1!==e.nodeType;);return e}C.fn.extend({has:function(e){var t=C(e,this),n=t.length;return this.filter(function(){for(var e=0;e<n;e++)if(C.contains(this,t[e]))return!0})},closest:function(e,t){var n,r=0,i=this.length,o=[],a="string"!=typeof e&&C(e);if(!O.test(e))for(;r<i;r++)for(n=this[r];n&&n!==t;n=n.parentNode)if(n.nodeType<11&&(a?a.index(n)>-1:1===n.nodeType&&C.find.matchesSelector(n,e))){o.push(n);break}return this.pushStack(o.length>1?C.uniqueSort(o):o)},index:function(e){return e?"string"==typeof e?f.call(C(e),this[0]):f.call(this,e.jquery?e[0]:e):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(e,t){return this.pushStack(C.uniqueSort(C.merge(this.get(),C(e,t))))},addBack:function(e){return this.add(null==e?this.prevObject:this.prevObject.filter(e))}}),C.each({parent:function(e){var t=e.parentNode;return t&&11!==t.nodeType?t:null},parents:function(e){return S(e,"parentNode")},parentsUntil:function(e,t,n){return S(e,"parentNode",n)},next:function(e){return R(e,"nextSibling")},prev:function(e){return R(e,"previousSibling")},nextAll:function(e){return S(e,"nextSibling")},prevAll:function(e){return S(e,"previousSibling")},nextUntil:function(e,t,n){return S(e,"nextSibling",n)},prevUntil:function(e,t,n){return S(e,"previousSibling",n)},siblings:function(e){return k((e.parentNode||{}).firstChild,e)},children:function(e){return k(e.firstChild)},contents:function(e){return D(e,"iframe")?e.contentDocument:(D(e,"template")&&(e=e.content||e),C.merge([],e.childNodes))}},function(e,t){C.fn[e]=function(n,r){var i=C.map(this,t,n);return"Until"!==e.slice(-5)&&(r=n),r&&"string"==typeof r&&(i=C.filter(r,i)),this.length>1&&(P[e]||C.uniqueSort(i),$.test(e)&&i.reverse()),this.pushStack(i)}});var M=/[^\x20\t\r\n\f]+/g;function H(e){return e}function F(e){throw e}function q(e,t,n,r){var i;try{e&&y(i=e.promise)?i.call(e).done(t).fail(n):e&&y(i=e.then)?i.call(e,t,n):t.apply(void 0,[e].slice(r))}catch(e){n.apply(void 0,[e])}}C.Callbacks=function(e){e="string"==typeof e?function(e){var t={};return C.each(e.match(M)||[],function(e,n){t[n]=!0}),t}(e):C.extend({},e);var t,n,r,i,o=[],a=[],s=-1,u=function(){for(i=i||e.once,r=t=!0;a.length;s=-1)for(n=a.shift();++s<o.length;)!1===o[s].apply(n[0],n[1])&&e.stopOnFalse&&(s=o.length,n=!1);e.memory||(n=!1),t=!1,i&&(o=n?[]:"")},c={add:function(){return o&&(n&&!t&&(s=o.length-1,a.push(n)),function t(n){C.each(n,function(n,r){y(r)?e.unique&&c.has(r)||o.push(r):r&&r.length&&"string"!==x(r)&&t(r)})}(arguments),n&&!t&&u()),this},remove:function(){return C.each(arguments,function(e,t){for(var n;(n=C.inArray(t,o,n))>-1;)o.splice(n,1),n<=s&&s--}),this},has:function(e){return e?C.inArray(e,o)>-1:o.length>0},empty:function(){return o&&(o=[]),this},disable:function(){return i=a=[],o=n="",this},disabled:function(){return!o},lock:function(){return i=a=[],n||t||(o=n=""),this},locked:function(){return!!i},fireWith:function(e,n){return i||(n=[e,(n=n||[]).slice?n.slice():n],a.push(n),t||u()),this},fire:function(){return c.fireWith(this,arguments),this},fired:function(){return!!r}};return c},C.extend({Deferred:function(e){var t=[["notify","progress",C.Callbacks("memory"),C.Callbacks("memory"),2],["resolve","done",C.Callbacks("once memory"),C.Callbacks("once memory"),0,"resolved"],["reject","fail",C.Callbacks("once memory"),C.Callbacks("once memory"),1,"rejected"]],r="pending",i={state:function(){return r},always:function(){return o.done(arguments).fail(arguments),this},catch:function(e){return i.then(null,e)},pipe:function(){var e=arguments;return C.Deferred(function(n){C.each(t,function(t,r){var i=y(e[r[4]])&&e[r[4]];o[r[1]](function(){var e=i&&i.apply(this,arguments);e&&y(e.promise)?e.promise().progress(n.notify).done(n.resolve).fail(n.reject):n[r[0]+"With"](this,i?[e]:arguments)})}),e=null}).promise()},then:function(e,r,i){var o=0;function a(e,t,r,i){return function(){var s=this,u=arguments,c=function(){var n,c;if(!(e<o)){if((n=r.apply(s,u))===t.promise())throw new TypeError("Thenable self-resolution");c=n&&("object"==typeof n||"function"==typeof n)&&n.then,y(c)?i?c.call(n,a(o,t,H,i),a(o,t,F,i)):(o++,c.call(n,a(o,t,H,i),a(o,t,F,i),a(o,t,H,t.notifyWith))):(r!==H&&(s=void 0,u=[n]),(i||t.resolveWith)(s,u))}},l=i?c:function(){try{c()}catch(n){C.Deferred.exceptionHook&&C.Deferred.exceptionHook(n,l.stackTrace),e+1>=o&&(r!==F&&(s=void 0,u=[n]),t.rejectWith(s,u))}};e?l():(C.Deferred.getStackHook&&(l.stackTrace=C.Deferred.getStackHook()),n.setTimeout(l))}}return C.Deferred(function(n){t[0][3].add(a(0,n,y(i)?i:H,n.notifyWith)),t[1][3].add(a(0,n,y(e)?e:H)),t[2][3].add(a(0,n,y(r)?r:F))}).promise()},promise:function(e){return null!=e?C.extend(e,i):i}},o={};return C.each(t,function(e,n){var a=n[2],s=n[5];i[n[1]]=a.add,s&&a.add(function(){r=s},t[3-e][2].disable,t[3-e][3].disable,t[0][2].lock,t[0][3].lock),a.add(n[3].fire),o[n[0]]=function(){return o[n[0]+"With"](this===o?void 0:this,arguments),this},o[n[0]+"With"]=a.fireWith}),i.promise(o),e&&e.call(o,o),o},when:function(e){var t=arguments.length,n=t,r=Array(n),i=u.call(arguments),o=C.Deferred(),a=function(e){return function(n){r[e]=this,i[e]=arguments.length>1?u.call(arguments):n,--t||o.resolveWith(r,i)}};if(t<=1&&(q(e,o.done(a(n)).resolve,o.reject,!t),"pending"===o.state()||y(i[n]&&i[n].then)))return o.then();for(;n--;)q(i[n],a(n),o.reject);return o.promise()}});var B=/^(Eval|Internal|Range|Reference|Syntax|Type|URI)Error$/;C.Deferred.exceptionHook=function(e,t){n.console&&n.console.warn&&e&&B.test(e.name)&&n.console.warn("jQuery.Deferred exception: "+e.message,e.stack,t)},C.readyException=function(e){n.setTimeout(function(){throw e})};var W=C.Deferred();function U(){a.removeEventListener("DOMContentLoaded",U),n.removeEventListener("load",U),C.ready()}C.fn.ready=function(e){return W.then(e).catch(function(e){C.readyException(e)}),this},C.extend({isReady:!1,readyWait:1,ready:function(e){(!0===e?--C.readyWait:C.isReady)||(C.isReady=!0,!0!==e&&--C.readyWait>0||W.resolveWith(a,[C]))}}),C.ready.then=W.then,"complete"===a.readyState||"loading"!==a.readyState&&!a.documentElement.doScroll?n.setTimeout(C.ready):(a.addEventListener("DOMContentLoaded",U),n.addEventListener("load",U));var z=function(e,t,n,r,i,o,a){var s=0,u=e.length,c=null==n;if("object"===x(n))for(s in i=!0,n)z(e,t,s,n[s],!0,o,a);else if(void 0!==r&&(i=!0,y(r)||(a=!0),c&&(a?(t.call(e,r),t=null):(c=t,t=function(e,t,n){return c.call(C(e),n)})),t))for(;s<u;s++)t(e[s],n,a?r:r.call(e[s],s,t(e[s],n)));return i?e:c?t.call(e):u?t(e[0],n):o},V=/^-ms-/,K=/-([a-z])/g;function Q(e,t){return t.toUpperCase()}function Y(e){return e.replace(V,"ms-").replace(K,Q)}var X=function(e){return 1===e.nodeType||9===e.nodeType||!+e.nodeType};function G(){this.expando=C.expando+G.uid++}G.uid=1,G.prototype={cache:function(e){var t=e[this.expando];return t||(t={},X(e)&&(e.nodeType?e[this.expando]=t:Object.defineProperty(e,this.expando,{value:t,configurable:!0}))),t},set:function(e,t,n){var r,i=this.cache(e);if("string"==typeof t)i[Y(t)]=n;else for(r in t)i[Y(r)]=t[r];return i},get:function(e,t){return void 0===t?this.cache(e):e[this.expando]&&e[this.expando][Y(t)]},access:function(e,t,n){return void 0===t||t&&"string"==typeof t&&void 0===n?this.get(e,t):(this.set(e,t,n),void 0!==n?n:t)},remove:function(e,t){var n,r=e[this.expando];if(void 0!==r){if(void 0!==t){n=(t=Array.isArray(t)?t.map(Y):(t=Y(t))in r?[t]:t.match(M)||[]).length;for(;n--;)delete r[t[n]]}(void 0===t||C.isEmptyObject(r))&&(e.nodeType?e[this.expando]=void 0:delete e[this.expando])}},hasData:function(e){var t=e[this.expando];return void 0!==t&&!C.isEmptyObject(t)}};var J=new G,Z=new G,ee=/^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,te=/[A-Z]/g;function ne(e,t,n){var r;if(void 0===n&&1===e.nodeType)if(r="data-"+t.replace(te,"-$&").toLowerCase(),"string"==typeof(n=e.getAttribute(r))){try{n=function(e){return"true"===e||"false"!==e&&("null"===e?null:e===+e+""?+e:ee.test(e)?JSON.parse(e):e)}(n)}catch(e){}Z.set(e,t,n)}else n=void 0;return n}C.extend({hasData:function(e){return Z.hasData(e)||J.hasData(e)},data:function(e,t,n){return Z.access(e,t,n)},removeData:function(e,t){Z.remove(e,t)},_data:function(e,t,n){return J.access(e,t,n)},_removeData:function(e,t){J.remove(e,t)}}),C.fn.extend({data:function(e,t){var n,r,i,o=this[0],a=o&&o.attributes;if(void 0===e){if(this.length&&(i=Z.get(o),1===o.nodeType&&!J.get(o,"hasDataAttrs"))){for(n=a.length;n--;)a[n]&&0===(r=a[n].name).indexOf("data-")&&(r=Y(r.slice(5)),ne(o,r,i[r]));J.set(o,"hasDataAttrs",!0)}return i}return"object"==typeof e?this.each(function(){Z.set(this,e)}):z(this,function(t){var n;if(o&&void 0===t)return void 0!==(n=Z.get(o,e))?n:void 0!==(n=ne(o,e))?n:void 0;this.each(function(){Z.set(this,e,t)})},null,t,arguments.length>1,null,!0)},removeData:function(e){return this.each(function(){Z.remove(this,e)})}}),C.extend({queue:function(e,t,n){var r;if(e)return t=(t||"fx")+"queue",r=J.get(e,t),n&&(!r||Array.isArray(n)?r=J.access(e,t,C.makeArray(n)):r.push(n)),r||[]},dequeue:function(e,t){t=t||"fx";var n=C.queue(e,t),r=n.length,i=n.shift(),o=C._queueHooks(e,t);"inprogress"===i&&(i=n.shift(),r--),i&&("fx"===t&&n.unshift("inprogress"),delete o.stop,i.call(e,function(){C.dequeue(e,t)},o)),!r&&o&&o.empty.fire()},_queueHooks:function(e,t){var n=t+"queueHooks";return J.get(e,n)||J.access(e,n,{empty:C.Callbacks("once memory").add(function(){J.remove(e,[t+"queue",n])})})}}),C.fn.extend({queue:function(e,t){var n=2;return"string"!=typeof e&&(t=e,e="fx",n--),arguments.length<n?C.queue(this[0],e):void 0===t?this:this.each(function(){var n=C.queue(this,e,t);C._queueHooks(this,e),"fx"===e&&"inprogress"!==n[0]&&C.dequeue(this,e)})},dequeue:function(e){return this.each(function(){C.dequeue(this,e)})},clearQueue:function(e){return this.queue(e||"fx",[])},promise:function(e,t){var n,r=1,i=C.Deferred(),o=this,a=this.length,s=function(){--r||i.resolveWith(o,[o])};for("string"!=typeof e&&(t=e,e=void 0),e=e||"fx";a--;)(n=J.get(o[a],e+"queueHooks"))&&n.empty&&(r++,n.empty.add(s));return s(),i.promise(t)}});var re=/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,ie=new RegExp("^(?:([+-])=|)("+re+")([a-z%]*)$","i"),oe=["Top","Right","Bottom","Left"],ae=function(e,t){return"none"===(e=t||e).style.display||""===e.style.display&&C.contains(e.ownerDocument,e)&&"none"===C.css(e,"display")},se=function(e,t,n,r){var i,o,a={};for(o in t)a[o]=e.style[o],e.style[o]=t[o];for(o in i=n.apply(e,r||[]),t)e.style[o]=a[o];return i};function ue(e,t,n,r){var i,o,a=20,s=r?function(){return r.cur()}:function(){return C.css(e,t,"")},u=s(),c=n&&n[3]||(C.cssNumber[t]?"":"px"),l=(C.cssNumber[t]||"px"!==c&&+u)&&ie.exec(C.css(e,t));if(l&&l[3]!==c){for(u/=2,c=c||l[3],l=+u||1;a--;)C.style(e,t,l+c),(1-o)*(1-(o=s()/u||.5))<=0&&(a=0),l/=o;l*=2,C.style(e,t,l+c),n=n||[]}return n&&(l=+l||+u||0,i=n[1]?l+(n[1]+1)*n[2]:+n[2],r&&(r.unit=c,r.start=l,r.end=i)),i}var ce={};function le(e){var t,n=e.ownerDocument,r=e.nodeName,i=ce[r];return i||(t=n.body.appendChild(n.createElement(r)),i=C.css(t,"display"),t.parentNode.removeChild(t),"none"===i&&(i="block"),ce[r]=i,i)}function fe(e,t){for(var n,r,i=[],o=0,a=e.length;o<a;o++)(r=e[o]).style&&(n=r.style.display,t?("none"===n&&(i[o]=J.get(r,"display")||null,i[o]||(r.style.display="")),""===r.style.display&&ae(r)&&(i[o]=le(r))):"none"!==n&&(i[o]="none",J.set(r,"display",n)));for(o=0;o<a;o++)null!=i[o]&&(e[o].style.display=i[o]);return e}C.fn.extend({show:function(){return fe(this,!0)},hide:function(){return fe(this)},toggle:function(e){return"boolean"==typeof e?e?this.show():this.hide():this.each(function(){ae(this)?C(this).show():C(this).hide()})}});var pe=/^(?:checkbox|radio)$/i,de=/<([a-z][^\/\0>\x20\t\r\n\f]+)/i,he=/^$|^module$|\/(?:java|ecma)script/i,ve={option:[1,"<select multiple='multiple'>","</select>"],thead:[1,"<table>","</table>"],col:[2,"<table><colgroup>","</colgroup></table>"],tr:[2,"<table><tbody>","</tbody></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:[0,"",""]};function ge(e,t){var n;return n=void 0!==e.getElementsByTagName?e.getElementsByTagName(t||"*"):void 0!==e.querySelectorAll?e.querySelectorAll(t||"*"):[],void 0===t||t&&D(e,t)?C.merge([e],n):n}function me(e,t){for(var n=0,r=e.length;n<r;n++)J.set(e[n],"globalEval",!t||J.get(t[n],"globalEval"))}ve.optgroup=ve.option,ve.tbody=ve.tfoot=ve.colgroup=ve.caption=ve.thead,ve.th=ve.td;var ye,_e,be=/<|&#?\w+;/;function we(e,t,n,r,i){for(var o,a,s,u,c,l,f=t.createDocumentFragment(),p=[],d=0,h=e.length;d<h;d++)if((o=e[d])||0===o)if("object"===x(o))C.merge(p,o.nodeType?[o]:o);else if(be.test(o)){for(a=a||f.appendChild(t.createElement("div")),s=(de.exec(o)||["",""])[1].toLowerCase(),u=ve[s]||ve._default,a.innerHTML=u[1]+C.htmlPrefilter(o)+u[2],l=u[0];l--;)a=a.lastChild;C.merge(p,a.childNodes),(a=f.firstChild).textContent=""}else p.push(t.createTextNode(o));for(f.textContent="",d=0;o=p[d++];)if(r&&C.inArray(o,r)>-1)i&&i.push(o);else if(c=C.contains(o.ownerDocument,o),a=ge(f.appendChild(o),"script"),c&&me(a),n)for(l=0;o=a[l++];)he.test(o.type||"")&&n.push(o);return f}ye=a.createDocumentFragment().appendChild(a.createElement("div")),(_e=a.createElement("input")).setAttribute("type","radio"),_e.setAttribute("checked","checked"),_e.setAttribute("name","t"),ye.appendChild(_e),m.checkClone=ye.cloneNode(!0).cloneNode(!0).lastChild.checked,ye.innerHTML="<textarea>x</textarea>",m.noCloneChecked=!!ye.cloneNode(!0).lastChild.defaultValue;var xe=a.documentElement,Ce=/^key/,Ee=/^(?:mouse|pointer|contextmenu|drag|drop)|click/,Te=/^([^.]*)(?:\.(.+)|)/;function Ae(){return!0}function Se(){return!1}function ke(){try{return a.activeElement}catch(e){}}function Oe(e,t,n,r,i,o){var a,s;if("object"==typeof t){for(s in"string"!=typeof n&&(r=r||n,n=void 0),t)Oe(e,s,n,r,t[s],o);return e}if(null==r&&null==i?(i=n,r=n=void 0):null==i&&("string"==typeof n?(i=r,r=void 0):(i=r,r=n,n=void 0)),!1===i)i=Se;else if(!i)return e;return 1===o&&(a=i,(i=function(e){return C().off(e),a.apply(this,arguments)}).guid=a.guid||(a.guid=C.guid++)),e.each(function(){C.event.add(this,t,i,r,n)})}C.event={global:{},add:function(e,t,n,r,i){var o,a,s,u,c,l,f,p,d,h,v,g=J.get(e);if(g)for(n.handler&&(n=(o=n).handler,i=o.selector),i&&C.find.matchesSelector(xe,i),n.guid||(n.guid=C.guid++),(u=g.events)||(u=g.events={}),(a=g.handle)||(a=g.handle=function(t){return void 0!==C&&C.event.triggered!==t.type?C.event.dispatch.apply(e,arguments):void 0}),c=(t=(t||"").match(M)||[""]).length;c--;)d=v=(s=Te.exec(t[c])||[])[1],h=(s[2]||"").split(".").sort(),d&&(f=C.event.special[d]||{},d=(i?f.delegateType:f.bindType)||d,f=C.event.special[d]||{},l=C.extend({type:d,origType:v,data:r,handler:n,guid:n.guid,selector:i,needsContext:i&&C.expr.match.needsContext.test(i),namespace:h.join(".")},o),(p=u[d])||((p=u[d]=[]).delegateCount=0,f.setup&&!1!==f.setup.call(e,r,h,a)||e.addEventListener&&e.addEventListener(d,a)),f.add&&(f.add.call(e,l),l.handler.guid||(l.handler.guid=n.guid)),i?p.splice(p.delegateCount++,0,l):p.push(l),C.event.global[d]=!0)},remove:function(e,t,n,r,i){var o,a,s,u,c,l,f,p,d,h,v,g=J.hasData(e)&&J.get(e);if(g&&(u=g.events)){for(c=(t=(t||"").match(M)||[""]).length;c--;)if(d=v=(s=Te.exec(t[c])||[])[1],h=(s[2]||"").split(".").sort(),d){for(f=C.event.special[d]||{},p=u[d=(r?f.delegateType:f.bindType)||d]||[],s=s[2]&&new RegExp("(^|\\.)"+h.join("\\.(?:.*\\.|)")+"(\\.|$)"),a=o=p.length;o--;)l=p[o],!i&&v!==l.origType||n&&n.guid!==l.guid||s&&!s.test(l.namespace)||r&&r!==l.selector&&("**"!==r||!l.selector)||(p.splice(o,1),l.selector&&p.delegateCount--,f.remove&&f.remove.call(e,l));a&&!p.length&&(f.teardown&&!1!==f.teardown.call(e,h,g.handle)||C.removeEvent(e,d,g.handle),delete u[d])}else for(d in u)C.event.remove(e,d+t[c],n,r,!0);C.isEmptyObject(u)&&J.remove(e,"handle events")}},dispatch:function(e){var t,n,r,i,o,a,s=C.event.fix(e),u=new Array(arguments.length),c=(J.get(this,"events")||{})[s.type]||[],l=C.event.special[s.type]||{};for(u[0]=s,t=1;t<arguments.length;t++)u[t]=arguments[t];if(s.delegateTarget=this,!l.preDispatch||!1!==l.preDispatch.call(this,s)){for(a=C.event.handlers.call(this,s,c),t=0;(i=a[t++])&&!s.isPropagationStopped();)for(s.currentTarget=i.elem,n=0;(o=i.handlers[n++])&&!s.isImmediatePropagationStopped();)s.rnamespace&&!s.rnamespace.test(o.namespace)||(s.handleObj=o,s.data=o.data,void 0!==(r=((C.event.special[o.origType]||{}).handle||o.handler).apply(i.elem,u))&&!1===(s.result=r)&&(s.preventDefault(),s.stopPropagation()));return l.postDispatch&&l.postDispatch.call(this,s),s.result}},handlers:function(e,t){var n,r,i,o,a,s=[],u=t.delegateCount,c=e.target;if(u&&c.nodeType&&!("click"===e.type&&e.button>=1))for(;c!==this;c=c.parentNode||this)if(1===c.nodeType&&("click"!==e.type||!0!==c.disabled)){for(o=[],a={},n=0;n<u;n++)void 0===a[i=(r=t[n]).selector+" "]&&(a[i]=r.needsContext?C(i,this).index(c)>-1:C.find(i,this,null,[c]).length),a[i]&&o.push(r);o.length&&s.push({elem:c,handlers:o})}return c=this,u<t.length&&s.push({elem:c,handlers:t.slice(u)}),s},addProp:function(e,t){Object.defineProperty(C.Event.prototype,e,{enumerable:!0,configurable:!0,get:y(t)?function(){if(this.originalEvent)return t(this.originalEvent)}:function(){if(this.originalEvent)return this.originalEvent[e]},set:function(t){Object.defineProperty(this,e,{enumerable:!0,configurable:!0,writable:!0,value:t})}})},fix:function(e){return e[C.expando]?e:new C.Event(e)},special:{load:{noBubble:!0},focus:{trigger:function(){if(this!==ke()&&this.focus)return this.focus(),!1},delegateType:"focusin"},blur:{trigger:function(){if(this===ke()&&this.blur)return this.blur(),!1},delegateType:"focusout"},click:{trigger:function(){if("checkbox"===this.type&&this.click&&D(this,"input"))return this.click(),!1},_default:function(e){return D(e.target,"a")}},beforeunload:{postDispatch:function(e){void 0!==e.result&&e.originalEvent&&(e.originalEvent.returnValue=e.result)}}}},C.removeEvent=function(e,t,n){e.removeEventListener&&e.removeEventListener(t,n)},C.Event=function(e,t){if(!(this instanceof C.Event))return new C.Event(e,t);e&&e.type?(this.originalEvent=e,this.type=e.type,this.isDefaultPrevented=e.defaultPrevented||void 0===e.defaultPrevented&&!1===e.returnValue?Ae:Se,this.target=e.target&&3===e.target.nodeType?e.target.parentNode:e.target,this.currentTarget=e.currentTarget,this.relatedTarget=e.relatedTarget):this.type=e,t&&C.extend(this,t),this.timeStamp=e&&e.timeStamp||Date.now(),this[C.expando]=!0},C.Event.prototype={constructor:C.Event,isDefaultPrevented:Se,isPropagationStopped:Se,isImmediatePropagationStopped:Se,isSimulated:!1,preventDefault:function(){var e=this.originalEvent;this.isDefaultPrevented=Ae,e&&!this.isSimulated&&e.preventDefault()},stopPropagation:function(){var e=this.originalEvent;this.isPropagationStopped=Ae,e&&!this.isSimulated&&e.stopPropagation()},stopImmediatePropagation:function(){var e=this.originalEvent;this.isImmediatePropagationStopped=Ae,e&&!this.isSimulated&&e.stopImmediatePropagation(),this.stopPropagation()}},C.each({altKey:!0,bubbles:!0,cancelable:!0,changedTouches:!0,ctrlKey:!0,detail:!0,eventPhase:!0,metaKey:!0,pageX:!0,pageY:!0,shiftKey:!0,view:!0,char:!0,charCode:!0,key:!0,keyCode:!0,button:!0,buttons:!0,clientX:!0,clientY:!0,offsetX:!0,offsetY:!0,pointerId:!0,pointerType:!0,screenX:!0,screenY:!0,targetTouches:!0,toElement:!0,touches:!0,which:function(e){var t=e.button;return null==e.which&&Ce.test(e.type)?null!=e.charCode?e.charCode:e.keyCode:!e.which&&void 0!==t&&Ee.test(e.type)?1&t?1:2&t?3:4&t?2:0:e.which}},C.event.addProp),C.each({mouseenter:"mouseover",mouseleave:"mouseout",pointerenter:"pointerover",pointerleave:"pointerout"},function(e,t){C.event.special[e]={delegateType:t,bindType:t,handle:function(e){var n,r=e.relatedTarget,i=e.handleObj;return r&&(r===this||C.contains(this,r))||(e.type=i.origType,n=i.handler.apply(this,arguments),e.type=t),n}}}),C.fn.extend({on:function(e,t,n,r){return Oe(this,e,t,n,r)},one:function(e,t,n,r){return Oe(this,e,t,n,r,1)},off:function(e,t,n){var r,i;if(e&&e.preventDefault&&e.handleObj)return r=e.handleObj,C(e.delegateTarget).off(r.namespace?r.origType+"."+r.namespace:r.origType,r.selector,r.handler),this;if("object"==typeof e){for(i in e)this.off(i,t,e[i]);return this}return!1!==t&&"function"!=typeof t||(n=t,t=void 0),!1===n&&(n=Se),this.each(function(){C.event.remove(this,e,n,t)})}});var De=/<(?!area|br|col|embed|hr|img|input|link|meta|param)(([a-z][^\/\0>\x20\t\r\n\f]*)[^>]*)\/>/gi,Ie=/<script|<style|<link/i,Ne=/checked\s*(?:[^=]|=\s*.checked.)/i,je=/^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g;function Le(e,t){return D(e,"table")&&D(11!==t.nodeType?t:t.firstChild,"tr")&&C(e).children("tbody")[0]||e}function $e(e){return e.type=(null!==e.getAttribute("type"))+"/"+e.type,e}function Pe(e){return"true/"===(e.type||"").slice(0,5)?e.type=e.type.slice(5):e.removeAttribute("type"),e}function Re(e,t){var n,r,i,o,a,s,u,c;if(1===t.nodeType){if(J.hasData(e)&&(o=J.access(e),a=J.set(t,o),c=o.events))for(i in delete a.handle,a.events={},c)for(n=0,r=c[i].length;n<r;n++)C.event.add(t,i,c[i][n]);Z.hasData(e)&&(s=Z.access(e),u=C.extend({},s),Z.set(t,u))}}function Me(e,t,n,r){t=c.apply([],t);var i,o,a,s,u,l,f=0,p=e.length,d=p-1,h=t[0],v=y(h);if(v||p>1&&"string"==typeof h&&!m.checkClone&&Ne.test(h))return e.each(function(i){var o=e.eq(i);v&&(t[0]=h.call(this,i,o.html())),Me(o,t,n,r)});if(p&&(o=(i=we(t,e[0].ownerDocument,!1,e,r)).firstChild,1===i.childNodes.length&&(i=o),o||r)){for(s=(a=C.map(ge(i,"script"),$e)).length;f<p;f++)u=i,f!==d&&(u=C.clone(u,!0,!0),s&&C.merge(a,ge(u,"script"))),n.call(e[f],u,f);if(s)for(l=a[a.length-1].ownerDocument,C.map(a,Pe),f=0;f<s;f++)u=a[f],he.test(u.type||"")&&!J.access(u,"globalEval")&&C.contains(l,u)&&(u.src&&"module"!==(u.type||"").toLowerCase()?C._evalUrl&&C._evalUrl(u.src):w(u.textContent.replace(je,""),l,u))}return e}function He(e,t,n){for(var r,i=t?C.filter(t,e):e,o=0;null!=(r=i[o]);o++)n||1!==r.nodeType||C.cleanData(ge(r)),r.parentNode&&(n&&C.contains(r.ownerDocument,r)&&me(ge(r,"script")),r.parentNode.removeChild(r));return e}C.extend({htmlPrefilter:function(e){return e.replace(De,"<$1></$2>")},clone:function(e,t,n){var r,i,o,a,s,u,c,l=e.cloneNode(!0),f=C.contains(e.ownerDocument,e);if(!(m.noCloneChecked||1!==e.nodeType&&11!==e.nodeType||C.isXMLDoc(e)))for(a=ge(l),r=0,i=(o=ge(e)).length;r<i;r++)s=o[r],u=a[r],void 0,"input"===(c=u.nodeName.toLowerCase())&&pe.test(s.type)?u.checked=s.checked:"input"!==c&&"textarea"!==c||(u.defaultValue=s.defaultValue);if(t)if(n)for(o=o||ge(e),a=a||ge(l),r=0,i=o.length;r<i;r++)Re(o[r],a[r]);else Re(e,l);return(a=ge(l,"script")).length>0&&me(a,!f&&ge(e,"script")),l},cleanData:function(e){for(var t,n,r,i=C.event.special,o=0;void 0!==(n=e[o]);o++)if(X(n)){if(t=n[J.expando]){if(t.events)for(r in t.events)i[r]?C.event.remove(n,r):C.removeEvent(n,r,t.handle);n[J.expando]=void 0}n[Z.expando]&&(n[Z.expando]=void 0)}}}),C.fn.extend({detach:function(e){return He(this,e,!0)},remove:function(e){return He(this,e)},text:function(e){return z(this,function(e){return void 0===e?C.text(this):this.empty().each(function(){1!==this.nodeType&&11!==this.nodeType&&9!==this.nodeType||(this.textContent=e)})},null,e,arguments.length)},append:function(){return Me(this,arguments,function(e){1!==this.nodeType&&11!==this.nodeType&&9!==this.nodeType||Le(this,e).appendChild(e)})},prepend:function(){return Me(this,arguments,function(e){if(1===this.nodeType||11===this.nodeType||9===this.nodeType){var t=Le(this,e);t.insertBefore(e,t.firstChild)}})},before:function(){return Me(this,arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this)})},after:function(){return Me(this,arguments,function(e){this.parentNode&&this.parentNode.insertBefore(e,this.nextSibling)})},empty:function(){for(var e,t=0;null!=(e=this[t]);t++)1===e.nodeType&&(C.cleanData(ge(e,!1)),e.textContent="");return this},clone:function(e,t){return e=null!=e&&e,t=null==t?e:t,this.map(function(){return C.clone(this,e,t)})},html:function(e){return z(this,function(e){var t=this[0]||{},n=0,r=this.length;if(void 0===e&&1===t.nodeType)return t.innerHTML;if("string"==typeof e&&!Ie.test(e)&&!ve[(de.exec(e)||["",""])[1].toLowerCase()]){e=C.htmlPrefilter(e);try{for(;n<r;n++)1===(t=this[n]||{}).nodeType&&(C.cleanData(ge(t,!1)),t.innerHTML=e);t=0}catch(e){}}t&&this.empty().append(e)},null,e,arguments.length)},replaceWith:function(){var e=[];return Me(this,arguments,function(t){var n=this.parentNode;C.inArray(this,e)<0&&(C.cleanData(ge(this)),n&&n.replaceChild(t,this))},e)}}),C.each({appendTo:"append",prependTo:"prepend",insertBefore:"before",insertAfter:"after",replaceAll:"replaceWith"},function(e,t){C.fn[e]=function(e){for(var n,r=[],i=C(e),o=i.length-1,a=0;a<=o;a++)n=a===o?this:this.clone(!0),C(i[a])[t](n),l.apply(r,n.get());return this.pushStack(r)}});var Fe=new RegExp("^("+re+")(?!px)[a-z%]+$","i"),qe=function(e){var t=e.ownerDocument.defaultView;return t&&t.opener||(t=n),t.getComputedStyle(e)},Be=new RegExp(oe.join("|"),"i");function We(e,t,n){var r,i,o,a,s=e.style;return(n=n||qe(e))&&(""!==(a=n.getPropertyValue(t)||n[t])||C.contains(e.ownerDocument,e)||(a=C.style(e,t)),!m.pixelBoxStyles()&&Fe.test(a)&&Be.test(t)&&(r=s.width,i=s.minWidth,o=s.maxWidth,s.minWidth=s.maxWidth=s.width=a,a=n.width,s.width=r,s.minWidth=i,s.maxWidth=o)),void 0!==a?a+"":a}function Ue(e,t){return{get:function(){if(!e())return(this.get=t).apply(this,arguments);delete this.get}}}!function(){function e(){if(l){c.style.cssText="position:absolute;left:-11111px;width:60px;margin-top:1px;padding:0;border:0",l.style.cssText="position:relative;display:block;box-sizing:border-box;overflow:scroll;margin:auto;border:1px;padding:1px;width:60%;top:1%",xe.appendChild(c).appendChild(l);var e=n.getComputedStyle(l);r="1%"!==e.top,u=12===t(e.marginLeft),l.style.right="60%",s=36===t(e.right),i=36===t(e.width),l.style.position="absolute",o=36===l.offsetWidth||"absolute",xe.removeChild(c),l=null}}function t(e){return Math.round(parseFloat(e))}var r,i,o,s,u,c=a.createElement("div"),l=a.createElement("div");l.style&&(l.style.backgroundClip="content-box",l.cloneNode(!0).style.backgroundClip="",m.clearCloneStyle="content-box"===l.style.backgroundClip,C.extend(m,{boxSizingReliable:function(){return e(),i},pixelBoxStyles:function(){return e(),s},pixelPosition:function(){return e(),r},reliableMarginLeft:function(){return e(),u},scrollboxSize:function(){return e(),o}}))}();var ze=/^(none|table(?!-c[ea]).+)/,Ve=/^--/,Ke={position:"absolute",visibility:"hidden",display:"block"},Qe={letterSpacing:"0",fontWeight:"400"},Ye=["Webkit","Moz","ms"],Xe=a.createElement("div").style;function Ge(e){var t=C.cssProps[e];return t||(t=C.cssProps[e]=function(e){if(e in Xe)return e;for(var t=e[0].toUpperCase()+e.slice(1),n=Ye.length;n--;)if((e=Ye[n]+t)in Xe)return e}(e)||e),t}function Je(e,t,n){var r=ie.exec(t);return r?Math.max(0,r[2]-(n||0))+(r[3]||"px"):t}function Ze(e,t,n,r,i,o){var a="width"===t?1:0,s=0,u=0;if(n===(r?"border":"content"))return 0;for(;a<4;a+=2)"margin"===n&&(u+=C.css(e,n+oe[a],!0,i)),r?("content"===n&&(u-=C.css(e,"padding"+oe[a],!0,i)),"margin"!==n&&(u-=C.css(e,"border"+oe[a]+"Width",!0,i))):(u+=C.css(e,"padding"+oe[a],!0,i),"padding"!==n?u+=C.css(e,"border"+oe[a]+"Width",!0,i):s+=C.css(e,"border"+oe[a]+"Width",!0,i));return!r&&o>=0&&(u+=Math.max(0,Math.ceil(e["offset"+t[0].toUpperCase()+t.slice(1)]-o-u-s-.5))),u}function et(e,t,n){var r=qe(e),i=We(e,t,r),o="border-box"===C.css(e,"boxSizing",!1,r),a=o;if(Fe.test(i)){if(!n)return i;i="auto"}return a=a&&(m.boxSizingReliable()||i===e.style[t]),("auto"===i||!parseFloat(i)&&"inline"===C.css(e,"display",!1,r))&&(i=e["offset"+t[0].toUpperCase()+t.slice(1)],a=!0),(i=parseFloat(i)||0)+Ze(e,t,n||(o?"border":"content"),a,r,i)+"px"}function tt(e,t,n,r,i){return new tt.prototype.init(e,t,n,r,i)}C.extend({cssHooks:{opacity:{get:function(e,t){if(t){var n=We(e,"opacity");return""===n?"1":n}}}},cssNumber:{animationIterationCount:!0,columnCount:!0,fillOpacity:!0,flexGrow:!0,flexShrink:!0,fontWeight:!0,lineHeight:!0,opacity:!0,order:!0,orphans:!0,widows:!0,zIndex:!0,zoom:!0},cssProps:{},style:function(e,t,n,r){if(e&&3!==e.nodeType&&8!==e.nodeType&&e.style){var i,o,a,s=Y(t),u=Ve.test(t),c=e.style;if(u||(t=Ge(s)),a=C.cssHooks[t]||C.cssHooks[s],void 0===n)return a&&"get"in a&&void 0!==(i=a.get(e,!1,r))?i:c[t];"string"===(o=typeof n)&&(i=ie.exec(n))&&i[1]&&(n=ue(e,t,i),o="number"),null!=n&&n==n&&("number"===o&&(n+=i&&i[3]||(C.cssNumber[s]?"":"px")),m.clearCloneStyle||""!==n||0!==t.indexOf("background")||(c[t]="inherit"),a&&"set"in a&&void 0===(n=a.set(e,n,r))||(u?c.setProperty(t,n):c[t]=n))}},css:function(e,t,n,r){var i,o,a,s=Y(t);return Ve.test(t)||(t=Ge(s)),(a=C.cssHooks[t]||C.cssHooks[s])&&"get"in a&&(i=a.get(e,!0,n)),void 0===i&&(i=We(e,t,r)),"normal"===i&&t in Qe&&(i=Qe[t]),""===n||n?(o=parseFloat(i),!0===n||isFinite(o)?o||0:i):i}}),C.each(["height","width"],function(e,t){C.cssHooks[t]={get:function(e,n,r){if(n)return!ze.test(C.css(e,"display"))||e.getClientRects().length&&e.getBoundingClientRect().width?et(e,t,r):se(e,Ke,function(){return et(e,t,r)})},set:function(e,n,r){var i,o=qe(e),a="border-box"===C.css(e,"boxSizing",!1,o),s=r&&Ze(e,t,r,a,o);return a&&m.scrollboxSize()===o.position&&(s-=Math.ceil(e["offset"+t[0].toUpperCase()+t.slice(1)]-parseFloat(o[t])-Ze(e,t,"border",!1,o)-.5)),s&&(i=ie.exec(n))&&"px"!==(i[3]||"px")&&(e.style[t]=n,n=C.css(e,t)),Je(0,n,s)}}}),C.cssHooks.marginLeft=Ue(m.reliableMarginLeft,function(e,t){if(t)return(parseFloat(We(e,"marginLeft"))||e.getBoundingClientRect().left-se(e,{marginLeft:0},function(){return e.getBoundingClientRect().left}))+"px"}),C.each({margin:"",padding:"",border:"Width"},function(e,t){C.cssHooks[e+t]={expand:function(n){for(var r=0,i={},o="string"==typeof n?n.split(" "):[n];r<4;r++)i[e+oe[r]+t]=o[r]||o[r-2]||o[0];return i}},"margin"!==e&&(C.cssHooks[e+t].set=Je)}),C.fn.extend({css:function(e,t){return z(this,function(e,t,n){var r,i,o={},a=0;if(Array.isArray(t)){for(r=qe(e),i=t.length;a<i;a++)o[t[a]]=C.css(e,t[a],!1,r);return o}return void 0!==n?C.style(e,t,n):C.css(e,t)},e,t,arguments.length>1)}}),C.Tween=tt,tt.prototype={constructor:tt,init:function(e,t,n,r,i,o){this.elem=e,this.prop=n,this.easing=i||C.easing._default,this.options=t,this.start=this.now=this.cur(),this.end=r,this.unit=o||(C.cssNumber[n]?"":"px")},cur:function(){var e=tt.propHooks[this.prop];return e&&e.get?e.get(this):tt.propHooks._default.get(this)},run:function(e){var t,n=tt.propHooks[this.prop];return this.options.duration?this.pos=t=C.easing[this.easing](e,this.options.duration*e,0,1,this.options.duration):this.pos=t=e,this.now=(this.end-this.start)*t+this.start,this.options.step&&this.options.step.call(this.elem,this.now,this),n&&n.set?n.set(this):tt.propHooks._default.set(this),this}},tt.prototype.init.prototype=tt.prototype,tt.propHooks={_default:{get:function(e){var t;return 1!==e.elem.nodeType||null!=e.elem[e.prop]&&null==e.elem.style[e.prop]?e.elem[e.prop]:(t=C.css(e.elem,e.prop,""))&&"auto"!==t?t:0},set:function(e){C.fx.step[e.prop]?C.fx.step[e.prop](e):1!==e.elem.nodeType||null==e.elem.style[C.cssProps[e.prop]]&&!C.cssHooks[e.prop]?e.elem[e.prop]=e.now:C.style(e.elem,e.prop,e.now+e.unit)}}},tt.propHooks.scrollTop=tt.propHooks.scrollLeft={set:function(e){e.elem.nodeType&&e.elem.parentNode&&(e.elem[e.prop]=e.now)}},C.easing={linear:function(e){return e},swing:function(e){return.5-Math.cos(e*Math.PI)/2},_default:"swing"},C.fx=tt.prototype.init,C.fx.step={};var nt,rt,it=/^(?:toggle|show|hide)$/,ot=/queueHooks$/;function at(){rt&&(!1===a.hidden&&n.requestAnimationFrame?n.requestAnimationFrame(at):n.setTimeout(at,C.fx.interval),C.fx.tick())}function st(){return n.setTimeout(function(){nt=void 0}),nt=Date.now()}function ut(e,t){var n,r=0,i={height:e};for(t=t?1:0;r<4;r+=2-t)i["margin"+(n=oe[r])]=i["padding"+n]=e;return t&&(i.opacity=i.width=e),i}function ct(e,t,n){for(var r,i=(lt.tweeners[t]||[]).concat(lt.tweeners["*"]),o=0,a=i.length;o<a;o++)if(r=i[o].call(n,t,e))return r}function lt(e,t,n){var r,i,o=0,a=lt.prefilters.length,s=C.Deferred().always(function(){delete u.elem}),u=function(){if(i)return!1;for(var t=nt||st(),n=Math.max(0,c.startTime+c.duration-t),r=1-(n/c.duration||0),o=0,a=c.tweens.length;o<a;o++)c.tweens[o].run(r);return s.notifyWith(e,[c,r,n]),r<1&&a?n:(a||s.notifyWith(e,[c,1,0]),s.resolveWith(e,[c]),!1)},c=s.promise({elem:e,props:C.extend({},t),opts:C.extend(!0,{specialEasing:{},easing:C.easing._default},n),originalProperties:t,originalOptions:n,startTime:nt||st(),duration:n.duration,tweens:[],createTween:function(t,n){var r=C.Tween(e,c.opts,t,n,c.opts.specialEasing[t]||c.opts.easing);return c.tweens.push(r),r},stop:function(t){var n=0,r=t?c.tweens.length:0;if(i)return this;for(i=!0;n<r;n++)c.tweens[n].run(1);return t?(s.notifyWith(e,[c,1,0]),s.resolveWith(e,[c,t])):s.rejectWith(e,[c,t]),this}}),l=c.props;for(!function(e,t){var n,r,i,o,a;for(n in e)if(i=t[r=Y(n)],o=e[n],Array.isArray(o)&&(i=o[1],o=e[n]=o[0]),n!==r&&(e[r]=o,delete e[n]),(a=C.cssHooks[r])&&"expand"in a)for(n in o=a.expand(o),delete e[r],o)n in e||(e[n]=o[n],t[n]=i);else t[r]=i}(l,c.opts.specialEasing);o<a;o++)if(r=lt.prefilters[o].call(c,e,l,c.opts))return y(r.stop)&&(C._queueHooks(c.elem,c.opts.queue).stop=r.stop.bind(r)),r;return C.map(l,ct,c),y(c.opts.start)&&c.opts.start.call(e,c),c.progress(c.opts.progress).done(c.opts.done,c.opts.complete).fail(c.opts.fail).always(c.opts.always),C.fx.timer(C.extend(u,{elem:e,anim:c,queue:c.opts.queue})),c}C.Animation=C.extend(lt,{tweeners:{"*":[function(e,t){var n=this.createTween(e,t);return ue(n.elem,e,ie.exec(t),n),n}]},tweener:function(e,t){y(e)?(t=e,e=["*"]):e=e.match(M);for(var n,r=0,i=e.length;r<i;r++)n=e[r],lt.tweeners[n]=lt.tweeners[n]||[],lt.tweeners[n].unshift(t)},prefilters:[function(e,t,n){var r,i,o,a,s,u,c,l,f="width"in t||"height"in t,p=this,d={},h=e.style,v=e.nodeType&&ae(e),g=J.get(e,"fxshow");for(r in n.queue||(null==(a=C._queueHooks(e,"fx")).unqueued&&(a.unqueued=0,s=a.empty.fire,a.empty.fire=function(){a.unqueued||s()}),a.unqueued++,p.always(function(){p.always(function(){a.unqueued--,C.queue(e,"fx").length||a.empty.fire()})})),t)if(i=t[r],it.test(i)){if(delete t[r],o=o||"toggle"===i,i===(v?"hide":"show")){if("show"!==i||!g||void 0===g[r])continue;v=!0}d[r]=g&&g[r]||C.style(e,r)}if((u=!C.isEmptyObject(t))||!C.isEmptyObject(d))for(r in f&&1===e.nodeType&&(n.overflow=[h.overflow,h.overflowX,h.overflowY],null==(c=g&&g.display)&&(c=J.get(e,"display")),"none"===(l=C.css(e,"display"))&&(c?l=c:(fe([e],!0),c=e.style.display||c,l=C.css(e,"display"),fe([e]))),("inline"===l||"inline-block"===l&&null!=c)&&"none"===C.css(e,"float")&&(u||(p.done(function(){h.display=c}),null==c&&(l=h.display,c="none"===l?"":l)),h.display="inline-block")),n.overflow&&(h.overflow="hidden",p.always(function(){h.overflow=n.overflow[0],h.overflowX=n.overflow[1],h.overflowY=n.overflow[2]})),u=!1,d)u||(g?"hidden"in g&&(v=g.hidden):g=J.access(e,"fxshow",{display:c}),o&&(g.hidden=!v),v&&fe([e],!0),p.done(function(){for(r in v||fe([e]),J.remove(e,"fxshow"),d)C.style(e,r,d[r])})),u=ct(v?g[r]:0,r,p),r in g||(g[r]=u.start,v&&(u.end=u.start,u.start=0))}],prefilter:function(e,t){t?lt.prefilters.unshift(e):lt.prefilters.push(e)}}),C.speed=function(e,t,n){var r=e&&"object"==typeof e?C.extend({},e):{complete:n||!n&&t||y(e)&&e,duration:e,easing:n&&t||t&&!y(t)&&t};return C.fx.off?r.duration=0:"number"!=typeof r.duration&&(r.duration in C.fx.speeds?r.duration=C.fx.speeds[r.duration]:r.duration=C.fx.speeds._default),null!=r.queue&&!0!==r.queue||(r.queue="fx"),r.old=r.complete,r.complete=function(){y(r.old)&&r.old.call(this),r.queue&&C.dequeue(this,r.queue)},r},C.fn.extend({fadeTo:function(e,t,n,r){return this.filter(ae).css("opacity",0).show().end().animate({opacity:t},e,n,r)},animate:function(e,t,n,r){var i=C.isEmptyObject(e),o=C.speed(t,n,r),a=function(){var t=lt(this,C.extend({},e),o);(i||J.get(this,"finish"))&&t.stop(!0)};return a.finish=a,i||!1===o.queue?this.each(a):this.queue(o.queue,a)},stop:function(e,t,n){var r=function(e){var t=e.stop;delete e.stop,t(n)};return"string"!=typeof e&&(n=t,t=e,e=void 0),t&&!1!==e&&this.queue(e||"fx",[]),this.each(function(){var t=!0,i=null!=e&&e+"queueHooks",o=C.timers,a=J.get(this);if(i)a[i]&&a[i].stop&&r(a[i]);else for(i in a)a[i]&&a[i].stop&&ot.test(i)&&r(a[i]);for(i=o.length;i--;)o[i].elem!==this||null!=e&&o[i].queue!==e||(o[i].anim.stop(n),t=!1,o.splice(i,1));!t&&n||C.dequeue(this,e)})},finish:function(e){return!1!==e&&(e=e||"fx"),this.each(function(){var t,n=J.get(this),r=n[e+"queue"],i=n[e+"queueHooks"],o=C.timers,a=r?r.length:0;for(n.finish=!0,C.queue(this,e,[]),i&&i.stop&&i.stop.call(this,!0),t=o.length;t--;)o[t].elem===this&&o[t].queue===e&&(o[t].anim.stop(!0),o.splice(t,1));for(t=0;t<a;t++)r[t]&&r[t].finish&&r[t].finish.call(this);delete n.finish})}}),C.each(["toggle","show","hide"],function(e,t){var n=C.fn[t];C.fn[t]=function(e,r,i){return null==e||"boolean"==typeof e?n.apply(this,arguments):this.animate(ut(t,!0),e,r,i)}}),C.each({slideDown:ut("show"),slideUp:ut("hide"),slideToggle:ut("toggle"),fadeIn:{opacity:"show"},fadeOut:{opacity:"hide"},fadeToggle:{opacity:"toggle"}},function(e,t){C.fn[e]=function(e,n,r){return this.animate(t,e,n,r)}}),C.timers=[],C.fx.tick=function(){var e,t=0,n=C.timers;for(nt=Date.now();t<n.length;t++)(e=n[t])()||n[t]!==e||n.splice(t--,1);n.length||C.fx.stop(),nt=void 0},C.fx.timer=function(e){C.timers.push(e),C.fx.start()},C.fx.interval=13,C.fx.start=function(){rt||(rt=!0,at())},C.fx.stop=function(){rt=null},C.fx.speeds={slow:600,fast:200,_default:400},C.fn.delay=function(e,t){return e=C.fx&&C.fx.speeds[e]||e,t=t||"fx",this.queue(t,function(t,r){var i=n.setTimeout(t,e);r.stop=function(){n.clearTimeout(i)}})},function(){var e=a.createElement("input"),t=a.createElement("select").appendChild(a.createElement("option"));e.type="checkbox",m.checkOn=""!==e.value,m.optSelected=t.selected,(e=a.createElement("input")).value="t",e.type="radio",m.radioValue="t"===e.value}();var ft,pt=C.expr.attrHandle;C.fn.extend({attr:function(e,t){return z(this,C.attr,e,t,arguments.length>1)},removeAttr:function(e){return this.each(function(){C.removeAttr(this,e)})}}),C.extend({attr:function(e,t,n){var r,i,o=e.nodeType;if(3!==o&&8!==o&&2!==o)return void 0===e.getAttribute?C.prop(e,t,n):(1===o&&C.isXMLDoc(e)||(i=C.attrHooks[t.toLowerCase()]||(C.expr.match.bool.test(t)?ft:void 0)),void 0!==n?null===n?void C.removeAttr(e,t):i&&"set"in i&&void 0!==(r=i.set(e,n,t))?r:(e.setAttribute(t,n+""),n):i&&"get"in i&&null!==(r=i.get(e,t))?r:null==(r=C.find.attr(e,t))?void 0:r)},attrHooks:{type:{set:function(e,t){if(!m.radioValue&&"radio"===t&&D(e,"input")){var n=e.value;return e.setAttribute("type",t),n&&(e.value=n),t}}}},removeAttr:function(e,t){var n,r=0,i=t&&t.match(M);if(i&&1===e.nodeType)for(;n=i[r++];)e.removeAttribute(n)}}),ft={set:function(e,t,n){return!1===t?C.removeAttr(e,n):e.setAttribute(n,n),n}},C.each(C.expr.match.bool.source.match(/\w+/g),function(e,t){var n=pt[t]||C.find.attr;pt[t]=function(e,t,r){var i,o,a=t.toLowerCase();return r||(o=pt[a],pt[a]=i,i=null!=n(e,t,r)?a:null,pt[a]=o),i}});var dt=/^(?:input|select|textarea|button)$/i,ht=/^(?:a|area)$/i;function vt(e){return(e.match(M)||[]).join(" ")}function gt(e){return e.getAttribute&&e.getAttribute("class")||""}function mt(e){return Array.isArray(e)?e:"string"==typeof e&&e.match(M)||[]}C.fn.extend({prop:function(e,t){return z(this,C.prop,e,t,arguments.length>1)},removeProp:function(e){return this.each(function(){delete this[C.propFix[e]||e]})}}),C.extend({prop:function(e,t,n){var r,i,o=e.nodeType;if(3!==o&&8!==o&&2!==o)return 1===o&&C.isXMLDoc(e)||(t=C.propFix[t]||t,i=C.propHooks[t]),void 0!==n?i&&"set"in i&&void 0!==(r=i.set(e,n,t))?r:e[t]=n:i&&"get"in i&&null!==(r=i.get(e,t))?r:e[t]},propHooks:{tabIndex:{get:function(e){var t=C.find.attr(e,"tabindex");return t?parseInt(t,10):dt.test(e.nodeName)||ht.test(e.nodeName)&&e.href?0:-1}}},propFix:{for:"htmlFor",class:"className"}}),m.optSelected||(C.propHooks.selected={get:function(e){var t=e.parentNode;return t&&t.parentNode&&t.parentNode.selectedIndex,null},set:function(e){var t=e.parentNode;t&&(t.selectedIndex,t.parentNode&&t.parentNode.selectedIndex)}}),C.each(["tabIndex","readOnly","maxLength","cellSpacing","cellPadding","rowSpan","colSpan","useMap","frameBorder","contentEditable"],function(){C.propFix[this.toLowerCase()]=this}),C.fn.extend({addClass:function(e){var t,n,r,i,o,a,s,u=0;if(y(e))return this.each(function(t){C(this).addClass(e.call(this,t,gt(this)))});if((t=mt(e)).length)for(;n=this[u++];)if(i=gt(n),r=1===n.nodeType&&" "+vt(i)+" "){for(a=0;o=t[a++];)r.indexOf(" "+o+" ")<0&&(r+=o+" ");i!==(s=vt(r))&&n.setAttribute("class",s)}return this},removeClass:function(e){var t,n,r,i,o,a,s,u=0;if(y(e))return this.each(function(t){C(this).removeClass(e.call(this,t,gt(this)))});if(!arguments.length)return this.attr("class","");if((t=mt(e)).length)for(;n=this[u++];)if(i=gt(n),r=1===n.nodeType&&" "+vt(i)+" "){for(a=0;o=t[a++];)for(;r.indexOf(" "+o+" ")>-1;)r=r.replace(" "+o+" "," ");i!==(s=vt(r))&&n.setAttribute("class",s)}return this},toggleClass:function(e,t){var n=typeof e,r="string"===n||Array.isArray(e);return"boolean"==typeof t&&r?t?this.addClass(e):this.removeClass(e):y(e)?this.each(function(n){C(this).toggleClass(e.call(this,n,gt(this),t),t)}):this.each(function(){var t,i,o,a;if(r)for(i=0,o=C(this),a=mt(e);t=a[i++];)o.hasClass(t)?o.removeClass(t):o.addClass(t);else void 0!==e&&"boolean"!==n||((t=gt(this))&&J.set(this,"__className__",t),this.setAttribute&&this.setAttribute("class",t||!1===e?"":J.get(this,"__className__")||""))})},hasClass:function(e){var t,n,r=0;for(t=" "+e+" ";n=this[r++];)if(1===n.nodeType&&(" "+vt(gt(n))+" ").indexOf(t)>-1)return!0;return!1}});var yt=/\r/g;C.fn.extend({val:function(e){var t,n,r,i=this[0];return arguments.length?(r=y(e),this.each(function(n){var i;1===this.nodeType&&(null==(i=r?e.call(this,n,C(this).val()):e)?i="":"number"==typeof i?i+="":Array.isArray(i)&&(i=C.map(i,function(e){return null==e?"":e+""})),(t=C.valHooks[this.type]||C.valHooks[this.nodeName.toLowerCase()])&&"set"in t&&void 0!==t.set(this,i,"value")||(this.value=i))})):i?(t=C.valHooks[i.type]||C.valHooks[i.nodeName.toLowerCase()])&&"get"in t&&void 0!==(n=t.get(i,"value"))?n:"string"==typeof(n=i.value)?n.replace(yt,""):null==n?"":n:void 0}}),C.extend({valHooks:{option:{get:function(e){var t=C.find.attr(e,"value");return null!=t?t:vt(C.text(e))}},select:{get:function(e){var t,n,r,i=e.options,o=e.selectedIndex,a="select-one"===e.type,s=a?null:[],u=a?o+1:i.length;for(r=o<0?u:a?o:0;r<u;r++)if(((n=i[r]).selected||r===o)&&!n.disabled&&(!n.parentNode.disabled||!D(n.parentNode,"optgroup"))){if(t=C(n).val(),a)return t;s.push(t)}return s},set:function(e,t){for(var n,r,i=e.options,o=C.makeArray(t),a=i.length;a--;)((r=i[a]).selected=C.inArray(C.valHooks.option.get(r),o)>-1)&&(n=!0);return n||(e.selectedIndex=-1),o}}}}),C.each(["radio","checkbox"],function(){C.valHooks[this]={set:function(e,t){if(Array.isArray(t))return e.checked=C.inArray(C(e).val(),t)>-1}},m.checkOn||(C.valHooks[this].get=function(e){return null===e.getAttribute("value")?"on":e.value})}),m.focusin="onfocusin"in n;var _t=/^(?:focusinfocus|focusoutblur)$/,bt=function(e){e.stopPropagation()};C.extend(C.event,{trigger:function(e,t,r,i){var o,s,u,c,l,f,p,d,v=[r||a],g=h.call(e,"type")?e.type:e,m=h.call(e,"namespace")?e.namespace.split("."):[];if(s=d=u=r=r||a,3!==r.nodeType&&8!==r.nodeType&&!_t.test(g+C.event.triggered)&&(g.indexOf(".")>-1&&(g=(m=g.split(".")).shift(),m.sort()),l=g.indexOf(":")<0&&"on"+g,(e=e[C.expando]?e:new C.Event(g,"object"==typeof e&&e)).isTrigger=i?2:3,e.namespace=m.join("."),e.rnamespace=e.namespace?new RegExp("(^|\\.)"+m.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,e.result=void 0,e.target||(e.target=r),t=null==t?[e]:C.makeArray(t,[e]),p=C.event.special[g]||{},i||!p.trigger||!1!==p.trigger.apply(r,t))){if(!i&&!p.noBubble&&!_(r)){for(c=p.delegateType||g,_t.test(c+g)||(s=s.parentNode);s;s=s.parentNode)v.push(s),u=s;u===(r.ownerDocument||a)&&v.push(u.defaultView||u.parentWindow||n)}for(o=0;(s=v[o++])&&!e.isPropagationStopped();)d=s,e.type=o>1?c:p.bindType||g,(f=(J.get(s,"events")||{})[e.type]&&J.get(s,"handle"))&&f.apply(s,t),(f=l&&s[l])&&f.apply&&X(s)&&(e.result=f.apply(s,t),!1===e.result&&e.preventDefault());return e.type=g,i||e.isDefaultPrevented()||p._default&&!1!==p._default.apply(v.pop(),t)||!X(r)||l&&y(r[g])&&!_(r)&&((u=r[l])&&(r[l]=null),C.event.triggered=g,e.isPropagationStopped()&&d.addEventListener(g,bt),r[g](),e.isPropagationStopped()&&d.removeEventListener(g,bt),C.event.triggered=void 0,u&&(r[l]=u)),e.result}},simulate:function(e,t,n){var r=C.extend(new C.Event,n,{type:e,isSimulated:!0});C.event.trigger(r,null,t)}}),C.fn.extend({trigger:function(e,t){return this.each(function(){C.event.trigger(e,t,this)})},triggerHandler:function(e,t){var n=this[0];if(n)return C.event.trigger(e,t,n,!0)}}),m.focusin||C.each({focus:"focusin",blur:"focusout"},function(e,t){var n=function(e){C.event.simulate(t,e.target,C.event.fix(e))};C.event.special[t]={setup:function(){var r=this.ownerDocument||this,i=J.access(r,t);i||r.addEventListener(e,n,!0),J.access(r,t,(i||0)+1)},teardown:function(){var r=this.ownerDocument||this,i=J.access(r,t)-1;i?J.access(r,t,i):(r.removeEventListener(e,n,!0),J.remove(r,t))}}});var wt=n.location,xt=Date.now(),Ct=/\?/;C.parseXML=function(e){var t;if(!e||"string"!=typeof e)return null;try{t=(new n.DOMParser).parseFromString(e,"text/xml")}catch(e){t=void 0}return t&&!t.getElementsByTagName("parsererror").length||C.error("Invalid XML: "+e),t};var Et=/\[\]$/,Tt=/\r?\n/g,At=/^(?:submit|button|image|reset|file)$/i,St=/^(?:input|select|textarea|keygen)/i;function kt(e,t,n,r){var i;if(Array.isArray(t))C.each(t,function(t,i){n||Et.test(e)?r(e,i):kt(e+"["+("object"==typeof i&&null!=i?t:"")+"]",i,n,r)});else if(n||"object"!==x(t))r(e,t);else for(i in t)kt(e+"["+i+"]",t[i],n,r)}C.param=function(e,t){var n,r=[],i=function(e,t){var n=y(t)?t():t;r[r.length]=encodeURIComponent(e)+"="+encodeURIComponent(null==n?"":n)};if(Array.isArray(e)||e.jquery&&!C.isPlainObject(e))C.each(e,function(){i(this.name,this.value)});else for(n in e)kt(n,e[n],t,i);return r.join("&")},C.fn.extend({serialize:function(){return C.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var e=C.prop(this,"elements");return e?C.makeArray(e):this}).filter(function(){var e=this.type;return this.name&&!C(this).is(":disabled")&&St.test(this.nodeName)&&!At.test(e)&&(this.checked||!pe.test(e))}).map(function(e,t){var n=C(this).val();return null==n?null:Array.isArray(n)?C.map(n,function(e){return{name:t.name,value:e.replace(Tt,"\r\n")}}):{name:t.name,value:n.replace(Tt,"\r\n")}}).get()}});var Ot=/%20/g,Dt=/#.*$/,It=/([?&])_=[^&]*/,Nt=/^(.*?):[ \t]*([^\r\n]*)$/gm,jt=/^(?:GET|HEAD)$/,Lt=/^\/\//,$t={},Pt={},Rt="*/".concat("*"),Mt=a.createElement("a");function Ht(e){return function(t,n){"string"!=typeof t&&(n=t,t="*");var r,i=0,o=t.toLowerCase().match(M)||[];if(y(n))for(;r=o[i++];)"+"===r[0]?(r=r.slice(1)||"*",(e[r]=e[r]||[]).unshift(n)):(e[r]=e[r]||[]).push(n)}}function Ft(e,t,n,r){var i={},o=e===Pt;function a(s){var u;return i[s]=!0,C.each(e[s]||[],function(e,s){var c=s(t,n,r);return"string"!=typeof c||o||i[c]?o?!(u=c):void 0:(t.dataTypes.unshift(c),a(c),!1)}),u}return a(t.dataTypes[0])||!i["*"]&&a("*")}function qt(e,t){var n,r,i=C.ajaxSettings.flatOptions||{};for(n in t)void 0!==t[n]&&((i[n]?e:r||(r={}))[n]=t[n]);return r&&C.extend(!0,e,r),e}Mt.href=wt.href,C.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:wt.href,type:"GET",isLocal:/^(?:about|app|app-storage|.+-extension|file|res|widget):$/.test(wt.protocol),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":Rt,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/\bxml\b/,html:/\bhtml/,json:/\bjson\b/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":JSON.parse,"text xml":C.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(e,t){return t?qt(qt(e,C.ajaxSettings),t):qt(C.ajaxSettings,e)},ajaxPrefilter:Ht($t),ajaxTransport:Ht(Pt),ajax:function(e,t){"object"==typeof e&&(t=e,e=void 0),t=t||{};var r,i,o,s,u,c,l,f,p,d,h=C.ajaxSetup({},t),v=h.context||h,g=h.context&&(v.nodeType||v.jquery)?C(v):C.event,m=C.Deferred(),y=C.Callbacks("once memory"),_=h.statusCode||{},b={},w={},x="canceled",E={readyState:0,getResponseHeader:function(e){var t;if(l){if(!s)for(s={};t=Nt.exec(o);)s[t[1].toLowerCase()]=t[2];t=s[e.toLowerCase()]}return null==t?null:t},getAllResponseHeaders:function(){return l?o:null},setRequestHeader:function(e,t){return null==l&&(e=w[e.toLowerCase()]=w[e.toLowerCase()]||e,b[e]=t),this},overrideMimeType:function(e){return null==l&&(h.mimeType=e),this},statusCode:function(e){var t;if(e)if(l)E.always(e[E.status]);else for(t in e)_[t]=[_[t],e[t]];return this},abort:function(e){var t=e||x;return r&&r.abort(t),T(0,t),this}};if(m.promise(E),h.url=((e||h.url||wt.href)+"").replace(Lt,wt.protocol+"//"),h.type=t.method||t.type||h.method||h.type,h.dataTypes=(h.dataType||"*").toLowerCase().match(M)||[""],null==h.crossDomain){c=a.createElement("a");try{c.href=h.url,c.href=c.href,h.crossDomain=Mt.protocol+"//"+Mt.host!=c.protocol+"//"+c.host}catch(e){h.crossDomain=!0}}if(h.data&&h.processData&&"string"!=typeof h.data&&(h.data=C.param(h.data,h.traditional)),Ft($t,h,t,E),l)return E;for(p in(f=C.event&&h.global)&&0==C.active++&&C.event.trigger("ajaxStart"),h.type=h.type.toUpperCase(),h.hasContent=!jt.test(h.type),i=h.url.replace(Dt,""),h.hasContent?h.data&&h.processData&&0===(h.contentType||"").indexOf("application/x-www-form-urlencoded")&&(h.data=h.data.replace(Ot,"+")):(d=h.url.slice(i.length),h.data&&(h.processData||"string"==typeof h.data)&&(i+=(Ct.test(i)?"&":"?")+h.data,delete h.data),!1===h.cache&&(i=i.replace(It,"$1"),d=(Ct.test(i)?"&":"?")+"_="+xt+++d),h.url=i+d),h.ifModified&&(C.lastModified[i]&&E.setRequestHeader("If-Modified-Since",C.lastModified[i]),C.etag[i]&&E.setRequestHeader("If-None-Match",C.etag[i])),(h.data&&h.hasContent&&!1!==h.contentType||t.contentType)&&E.setRequestHeader("Content-Type",h.contentType),E.setRequestHeader("Accept",h.dataTypes[0]&&h.accepts[h.dataTypes[0]]?h.accepts[h.dataTypes[0]]+("*"!==h.dataTypes[0]?", "+Rt+"; q=0.01":""):h.accepts["*"]),h.headers)E.setRequestHeader(p,h.headers[p]);if(h.beforeSend&&(!1===h.beforeSend.call(v,E,h)||l))return E.abort();if(x="abort",y.add(h.complete),E.done(h.success),E.fail(h.error),r=Ft(Pt,h,t,E)){if(E.readyState=1,f&&g.trigger("ajaxSend",[E,h]),l)return E;h.async&&h.timeout>0&&(u=n.setTimeout(function(){E.abort("timeout")},h.timeout));try{l=!1,r.send(b,T)}catch(e){if(l)throw e;T(-1,e)}}else T(-1,"No Transport");function T(e,t,a,s){var c,p,d,b,w,x=t;l||(l=!0,u&&n.clearTimeout(u),r=void 0,o=s||"",E.readyState=e>0?4:0,c=e>=200&&e<300||304===e,a&&(b=function(e,t,n){for(var r,i,o,a,s=e.contents,u=e.dataTypes;"*"===u[0];)u.shift(),void 0===r&&(r=e.mimeType||t.getResponseHeader("Content-Type"));if(r)for(i in s)if(s[i]&&s[i].test(r)){u.unshift(i);break}if(u[0]in n)o=u[0];else{for(i in n){if(!u[0]||e.converters[i+" "+u[0]]){o=i;break}a||(a=i)}o=o||a}if(o)return o!==u[0]&&u.unshift(o),n[o]}(h,E,a)),b=function(e,t,n,r){var i,o,a,s,u,c={},l=e.dataTypes.slice();if(l[1])for(a in e.converters)c[a.toLowerCase()]=e.converters[a];for(o=l.shift();o;)if(e.responseFields[o]&&(n[e.responseFields[o]]=t),!u&&r&&e.dataFilter&&(t=e.dataFilter(t,e.dataType)),u=o,o=l.shift())if("*"===o)o=u;else if("*"!==u&&u!==o){if(!(a=c[u+" "+o]||c["* "+o]))for(i in c)if((s=i.split(" "))[1]===o&&(a=c[u+" "+s[0]]||c["* "+s[0]])){!0===a?a=c[i]:!0!==c[i]&&(o=s[0],l.unshift(s[1]));break}if(!0!==a)if(a&&e.throws)t=a(t);else try{t=a(t)}catch(e){return{state:"parsererror",error:a?e:"No conversion from "+u+" to "+o}}}return{state:"success",data:t}}(h,b,E,c),c?(h.ifModified&&((w=E.getResponseHeader("Last-Modified"))&&(C.lastModified[i]=w),(w=E.getResponseHeader("etag"))&&(C.etag[i]=w)),204===e||"HEAD"===h.type?x="nocontent":304===e?x="notmodified":(x=b.state,p=b.data,c=!(d=b.error))):(d=x,!e&&x||(x="error",e<0&&(e=0))),E.status=e,E.statusText=(t||x)+"",c?m.resolveWith(v,[p,x,E]):m.rejectWith(v,[E,x,d]),E.statusCode(_),_=void 0,f&&g.trigger(c?"ajaxSuccess":"ajaxError",[E,h,c?p:d]),y.fireWith(v,[E,x]),f&&(g.trigger("ajaxComplete",[E,h]),--C.active||C.event.trigger("ajaxStop")))}return E},getJSON:function(e,t,n){return C.get(e,t,n,"json")},getScript:function(e,t){return C.get(e,void 0,t,"script")}}),C.each(["get","post"],function(e,t){C[t]=function(e,n,r,i){return y(n)&&(i=i||r,r=n,n=void 0),C.ajax(C.extend({url:e,type:t,dataType:i,data:n,success:r},C.isPlainObject(e)&&e))}}),C._evalUrl=function(e){return C.ajax({url:e,type:"GET",dataType:"script",cache:!0,async:!1,global:!1,throws:!0})},C.fn.extend({wrapAll:function(e){var t;return this[0]&&(y(e)&&(e=e.call(this[0])),t=C(e,this[0].ownerDocument).eq(0).clone(!0),this[0].parentNode&&t.insertBefore(this[0]),t.map(function(){for(var e=this;e.firstElementChild;)e=e.firstElementChild;return e}).append(this)),this},wrapInner:function(e){return y(e)?this.each(function(t){C(this).wrapInner(e.call(this,t))}):this.each(function(){var t=C(this),n=t.contents();n.length?n.wrapAll(e):t.append(e)})},wrap:function(e){var t=y(e);return this.each(function(n){C(this).wrapAll(t?e.call(this,n):e)})},unwrap:function(e){return this.parent(e).not("body").each(function(){C(this).replaceWith(this.childNodes)}),this}}),C.expr.pseudos.hidden=function(e){return!C.expr.pseudos.visible(e)},C.expr.pseudos.visible=function(e){return!!(e.offsetWidth||e.offsetHeight||e.getClientRects().length)},C.ajaxSettings.xhr=function(){try{return new n.XMLHttpRequest}catch(e){}};var Bt={0:200,1223:204},Wt=C.ajaxSettings.xhr();m.cors=!!Wt&&"withCredentials"in Wt,m.ajax=Wt=!!Wt,C.ajaxTransport(function(e){var t,r;if(m.cors||Wt&&!e.crossDomain)return{send:function(i,o){var a,s=e.xhr();if(s.open(e.type,e.url,e.async,e.username,e.password),e.xhrFields)for(a in e.xhrFields)s[a]=e.xhrFields[a];for(a in e.mimeType&&s.overrideMimeType&&s.overrideMimeType(e.mimeType),e.crossDomain||i["X-Requested-With"]||(i["X-Requested-With"]="XMLHttpRequest"),i)s.setRequestHeader(a,i[a]);t=function(e){return function(){t&&(t=r=s.onload=s.onerror=s.onabort=s.ontimeout=s.onreadystatechange=null,"abort"===e?s.abort():"error"===e?"number"!=typeof s.status?o(0,"error"):o(s.status,s.statusText):o(Bt[s.status]||s.status,s.statusText,"text"!==(s.responseType||"text")||"string"!=typeof s.responseText?{binary:s.response}:{text:s.responseText},s.getAllResponseHeaders()))}},s.onload=t(),r=s.onerror=s.ontimeout=t("error"),void 0!==s.onabort?s.onabort=r:s.onreadystatechange=function(){4===s.readyState&&n.setTimeout(function(){t&&r()})},t=t("abort");try{s.send(e.hasContent&&e.data||null)}catch(e){if(t)throw e}},abort:function(){t&&t()}}}),C.ajaxPrefilter(function(e){e.crossDomain&&(e.contents.script=!1)}),C.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/\b(?:java|ecma)script\b/},converters:{"text script":function(e){return C.globalEval(e),e}}}),C.ajaxPrefilter("script",function(e){void 0===e.cache&&(e.cache=!1),e.crossDomain&&(e.type="GET")}),C.ajaxTransport("script",function(e){var t,n;if(e.crossDomain)return{send:function(r,i){t=C("<script>").prop({charset:e.scriptCharset,src:e.url}).on("load error",n=function(e){t.remove(),n=null,e&&i("error"===e.type?404:200,e.type)}),a.head.appendChild(t[0])},abort:function(){n&&n()}}});var Ut,zt=[],Vt=/(=)\?(?=&|$)|\?\?/;C.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var e=zt.pop()||C.expando+"_"+xt++;return this[e]=!0,e}}),C.ajaxPrefilter("json jsonp",function(e,t,r){var i,o,a,s=!1!==e.jsonp&&(Vt.test(e.url)?"url":"string"==typeof e.data&&0===(e.contentType||"").indexOf("application/x-www-form-urlencoded")&&Vt.test(e.data)&&"data");if(s||"jsonp"===e.dataTypes[0])return i=e.jsonpCallback=y(e.jsonpCallback)?e.jsonpCallback():e.jsonpCallback,s?e[s]=e[s].replace(Vt,"$1"+i):!1!==e.jsonp&&(e.url+=(Ct.test(e.url)?"&":"?")+e.jsonp+"="+i),e.converters["script json"]=function(){return a||C.error(i+" was not called"),a[0]},e.dataTypes[0]="json",o=n[i],n[i]=function(){a=arguments},r.always(function(){void 0===o?C(n).removeProp(i):n[i]=o,e[i]&&(e.jsonpCallback=t.jsonpCallback,zt.push(i)),a&&y(o)&&o(a[0]),a=o=void 0}),"script"}),m.createHTMLDocument=((Ut=a.implementation.createHTMLDocument("").body).innerHTML="<form></form><form></form>",2===Ut.childNodes.length),C.parseHTML=function(e,t,n){return"string"!=typeof e?[]:("boolean"==typeof t&&(n=t,t=!1),t||(m.createHTMLDocument?((r=(t=a.implementation.createHTMLDocument("")).createElement("base")).href=a.location.href,t.head.appendChild(r)):t=a),o=!n&&[],(i=I.exec(e))?[t.createElement(i[1])]:(i=we([e],t,o),o&&o.length&&C(o).remove(),C.merge([],i.childNodes)));var r,i,o},C.fn.load=function(e,t,n){var r,i,o,a=this,s=e.indexOf(" ");return s>-1&&(r=vt(e.slice(s)),e=e.slice(0,s)),y(t)?(n=t,t=void 0):t&&"object"==typeof t&&(i="POST"),a.length>0&&C.ajax({url:e,type:i||"GET",dataType:"html",data:t}).done(function(e){o=arguments,a.html(r?C("<div>").append(C.parseHTML(e)).find(r):e)}).always(n&&function(e,t){a.each(function(){n.apply(this,o||[e.responseText,t,e])})}),this},C.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(e,t){C.fn[t]=function(e){return this.on(t,e)}}),C.expr.pseudos.animated=function(e){return C.grep(C.timers,function(t){return e===t.elem}).length},C.offset={setOffset:function(e,t,n){var r,i,o,a,s,u,c=C.css(e,"position"),l=C(e),f={};"static"===c&&(e.style.position="relative"),s=l.offset(),o=C.css(e,"top"),u=C.css(e,"left"),("absolute"===c||"fixed"===c)&&(o+u).indexOf("auto")>-1?(a=(r=l.position()).top,i=r.left):(a=parseFloat(o)||0,i=parseFloat(u)||0),y(t)&&(t=t.call(e,n,C.extend({},s))),null!=t.top&&(f.top=t.top-s.top+a),null!=t.left&&(f.left=t.left-s.left+i),"using"in t?t.using.call(e,f):l.css(f)}},C.fn.extend({offset:function(e){if(arguments.length)return void 0===e?this:this.each(function(t){C.offset.setOffset(this,e,t)});var t,n,r=this[0];return r?r.getClientRects().length?(t=r.getBoundingClientRect(),n=r.ownerDocument.defaultView,{top:t.top+n.pageYOffset,left:t.left+n.pageXOffset}):{top:0,left:0}:void 0},position:function(){if(this[0]){var e,t,n,r=this[0],i={top:0,left:0};if("fixed"===C.css(r,"position"))t=r.getBoundingClientRect();else{for(t=this.offset(),n=r.ownerDocument,e=r.offsetParent||n.documentElement;e&&(e===n.body||e===n.documentElement)&&"static"===C.css(e,"position");)e=e.parentNode;e&&e!==r&&1===e.nodeType&&((i=C(e).offset()).top+=C.css(e,"borderTopWidth",!0),i.left+=C.css(e,"borderLeftWidth",!0))}return{top:t.top-i.top-C.css(r,"marginTop",!0),left:t.left-i.left-C.css(r,"marginLeft",!0)}}},offsetParent:function(){return this.map(function(){for(var e=this.offsetParent;e&&"static"===C.css(e,"position");)e=e.offsetParent;return e||xe})}}),C.each({scrollLeft:"pageXOffset",scrollTop:"pageYOffset"},function(e,t){var n="pageYOffset"===t;C.fn[e]=function(r){return z(this,function(e,r,i){var o;if(_(e)?o=e:9===e.nodeType&&(o=e.defaultView),void 0===i)return o?o[t]:e[r];o?o.scrollTo(n?o.pageXOffset:i,n?i:o.pageYOffset):e[r]=i},e,r,arguments.length)}}),C.each(["top","left"],function(e,t){C.cssHooks[t]=Ue(m.pixelPosition,function(e,n){if(n)return n=We(e,t),Fe.test(n)?C(e).position()[t]+"px":n})}),C.each({Height:"height",Width:"width"},function(e,t){C.each({padding:"inner"+e,content:t,"":"outer"+e},function(n,r){C.fn[r]=function(i,o){var a=arguments.length&&(n||"boolean"!=typeof i),s=n||(!0===i||!0===o?"margin":"border");return z(this,function(t,n,i){var o;return _(t)?0===r.indexOf("outer")?t["inner"+e]:t.document.documentElement["client"+e]:9===t.nodeType?(o=t.documentElement,Math.max(t.body["scroll"+e],o["scroll"+e],t.body["offset"+e],o["offset"+e],o["client"+e])):void 0===i?C.css(t,n,s):C.style(t,n,i,s)},t,a?i:void 0,a)}})}),C.each("blur focus focusin focusout resize scroll click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup contextmenu".split(" "),function(e,t){C.fn[t]=function(e,n){return arguments.length>0?this.on(t,null,e,n):this.trigger(t)}}),C.fn.extend({hover:function(e,t){return this.mouseenter(e).mouseleave(t||e)}}),C.fn.extend({bind:function(e,t,n){return this.on(e,null,t,n)},unbind:function(e,t){return this.off(e,null,t)},delegate:function(e,t,n,r){return this.on(t,e,n,r)},undelegate:function(e,t,n){return 1===arguments.length?this.off(e,"**"):this.off(t,e||"**",n)}}),C.proxy=function(e,t){var n,r,i;if("string"==typeof t&&(n=e[t],t=e,e=n),y(e))return r=u.call(arguments,2),(i=function(){return e.apply(t||this,r.concat(u.call(arguments)))}).guid=e.guid=e.guid||C.guid++,i},C.holdReady=function(e){e?C.readyWait++:C.ready(!0)},C.isArray=Array.isArray,C.parseJSON=JSON.parse,C.nodeName=D,C.isFunction=y,C.isWindow=_,C.camelCase=Y,C.type=x,C.now=Date.now,C.isNumeric=function(e){var t=C.type(e);return("number"===t||"string"===t)&&!isNaN(e-parseFloat(e))},void 0===(r=function(){return C}.apply(t,[]))||(e.exports=r);var Kt=n.jQuery,Qt=n.$;return C.noConflict=function(e){return n.$===C&&(n.$=Qt),e&&n.jQuery===C&&(n.jQuery=Kt),C},i||(n.jQuery=n.$=C),C})},function(e,t,n){"use strict";e.exports=function(e,t){return function(){for(var n=new Array(arguments.length),r=0;r<n.length;r++)n[r]=arguments[r];return e.apply(t,n)}}},function(e,t){var n,r,i=e.exports={};function o(){throw new Error("setTimeout has not been defined")}function a(){throw new Error("clearTimeout has not been defined")}function s(e){if(n===setTimeout)return setTimeout(e,0);if((n===o||!n)&&setTimeout)return n=setTimeout,setTimeout(e,0);try{return n(e,0)}catch(t){try{return n.call(null,e,0)}catch(t){return n.call(this,e,0)}}}!function(){try{n="function"==typeof setTimeout?setTimeout:o}catch(e){n=o}try{r="function"==typeof clearTimeout?clearTimeout:a}catch(e){r=a}}();var u,c=[],l=!1,f=-1;function p(){l&&u&&(l=!1,u.length?c=u.concat(c):f=-1,c.length&&d())}function d(){if(!l){var e=s(p);l=!0;for(var t=c.length;t;){for(u=c,c=[];++f<t;)u&&u[f].run();f=-1,t=c.length}u=null,l=!1,function(e){if(r===clearTimeout)return clearTimeout(e);if((r===a||!r)&&clearTimeout)return r=clearTimeout,clearTimeout(e);try{r(e)}catch(t){try{return r.call(null,e)}catch(t){return r.call(this,e)}}}(e)}}function h(e,t){this.fun=e,this.array=t}function v(){}i.nextTick=function(e){var t=new Array(arguments.length-1);if(arguments.length>1)for(var n=1;n<arguments.length;n++)t[n-1]=arguments[n];c.push(new h(e,t)),1!==c.length||l||s(d)},h.prototype.run=function(){this.fun.apply(null,this.array)},i.title="browser",i.browser=!0,i.env={},i.argv=[],i.version="",i.versions={},i.on=v,i.addListener=v,i.once=v,i.off=v,i.removeListener=v,i.removeAllListeners=v,i.emit=v,i.prependListener=v,i.prependOnceListener=v,i.listeners=function(e){return[]},i.binding=function(e){throw new Error("process.binding is not supported")},i.cwd=function(){return"/"},i.chdir=function(e){throw new Error("process.chdir is not supported")},i.umask=function(){return 0}},function(e,t,n){"use strict";var r=n(0),i=n(22),o=n(24),a=n(25),s=n(26),u=n(8),c="undefined"!=typeof window&&window.btoa&&window.btoa.bind(window)||n(27);e.exports=function(e){return new Promise(function(t,l){var f=e.data,p=e.headers;r.isFormData(f)&&delete p["Content-Type"];var d=new XMLHttpRequest,h="onreadystatechange",v=!1;if("undefined"==typeof window||!window.XDomainRequest||"withCredentials"in d||s(e.url)||(d=new window.XDomainRequest,h="onload",v=!0,d.onprogress=function(){},d.ontimeout=function(){}),e.auth){var g=e.auth.username||"",m=e.auth.password||"";p.Authorization="Basic "+c(g+":"+m)}if(d.open(e.method.toUpperCase(),o(e.url,e.params,e.paramsSerializer),!0),d.timeout=e.timeout,d[h]=function(){if(d&&(4===d.readyState||v)&&(0!==d.status||d.responseURL&&0===d.responseURL.indexOf("file:"))){var n="getAllResponseHeaders"in d?a(d.getAllResponseHeaders()):null,r={data:e.responseType&&"text"!==e.responseType?d.response:d.responseText,status:1223===d.status?204:d.status,statusText:1223===d.status?"No Content":d.statusText,headers:n,config:e,request:d};i(t,l,r),d=null}},d.onerror=function(){l(u("Network Error",e,null,d)),d=null},d.ontimeout=function(){l(u("timeout of "+e.timeout+"ms exceeded",e,"ECONNABORTED",d)),d=null},r.isStandardBrowserEnv()){var y=n(28),_=(e.withCredentials||s(e.url))&&e.xsrfCookieName?y.read(e.xsrfCookieName):void 0;_&&(p[e.xsrfHeaderName]=_)}if("setRequestHeader"in d&&r.forEach(p,function(e,t){void 0===f&&"content-type"===t.toLowerCase()?delete p[t]:d.setRequestHeader(t,e)}),e.withCredentials&&(d.withCredentials=!0),e.responseType)try{d.responseType=e.responseType}catch(t){if("json"!==e.responseType)throw t}"function"==typeof e.onDownloadProgress&&d.addEventListener("progress",e.onDownloadProgress),"function"==typeof e.onUploadProgress&&d.upload&&d.upload.addEventListener("progress",e.onUploadProgress),e.cancelToken&&e.cancelToken.promise.then(function(e){d&&(d.abort(),l(e),d=null)}),void 0===f&&(f=null),d.send(f)})}},function(e,t,n){"use strict";var r=n(23);e.exports=function(e,t,n,i,o){var a=new Error(e);return r(a,t,n,i,o)}},function(e,t,n){"use strict";e.exports=function(e){return!(!e||!e.__CANCEL__)}},function(e,t,n){"use strict";function r(e){this.message=e}r.prototype.toString=function(){return"Cancel"+(this.message?": "+this.message:"")},r.prototype.__CANCEL__=!0,e.exports=r},function(e,t,n){n(12),e.exports=n(43)},function(e,t,n){n(13),window.Vue=n(36),Vue.component("example-component",n(39));new Vue({el:"#app"})},function(e,t,n){window._=n(14),window.Popper=n(3).default;try{window.$=window.jQuery=n(4),n(16)}catch(e){}window.axios=n(17),window.axios.defaults.headers.common["X-Requested-With"]="XMLHttpRequest";var r=document.head.querySelector('meta[name="csrf-token"]');r?window.axios.defaults.headers.common["X-CSRF-TOKEN"]=r.content:console.error("CSRF token not found: https://laravel.com/docs/csrf#csrf-x-csrf-token")},function(e,t,n){(function(e,r){var i;(function(){var o,a=200,s="Unsupported core-js use. Try https://npms.io/search?q=ponyfill.",u="Expected a function",c="__lodash_hash_undefined__",l=500,f="__lodash_placeholder__",p=1,d=2,h=4,v=1,g=2,m=1,y=2,_=4,b=8,w=16,x=32,C=64,E=128,T=256,A=512,S=30,k="...",O=800,D=16,I=1,N=2,j=1/0,L=9007199254740991,$=1.7976931348623157e308,P=NaN,R=4294967295,M=R-1,H=R>>>1,F=[["ary",E],["bind",m],["bindKey",y],["curry",b],["curryRight",w],["flip",A],["partial",x],["partialRight",C],["rearg",T]],q="[object Arguments]",B="[object Array]",W="[object AsyncFunction]",U="[object Boolean]",z="[object Date]",V="[object DOMException]",K="[object Error]",Q="[object Function]",Y="[object GeneratorFunction]",X="[object Map]",G="[object Number]",J="[object Null]",Z="[object Object]",ee="[object Proxy]",te="[object RegExp]",ne="[object Set]",re="[object String]",ie="[object Symbol]",oe="[object Undefined]",ae="[object WeakMap]",se="[object WeakSet]",ue="[object ArrayBuffer]",ce="[object DataView]",le="[object Float32Array]",fe="[object Float64Array]",pe="[object Int8Array]",de="[object Int16Array]",he="[object Int32Array]",ve="[object Uint8Array]",ge="[object Uint8ClampedArray]",me="[object Uint16Array]",ye="[object Uint32Array]",_e=/\b__p \+= '';/g,be=/\b(__p \+=) '' \+/g,we=/(__e\(.*?\)|\b__t\)) \+\n'';/g,xe=/&(?:amp|lt|gt|quot|#39);/g,Ce=/[&<>"']/g,Ee=RegExp(xe.source),Te=RegExp(Ce.source),Ae=/<%-([\s\S]+?)%>/g,Se=/<%([\s\S]+?)%>/g,ke=/<%=([\s\S]+?)%>/g,Oe=/\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,De=/^\w*$/,Ie=/[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g,Ne=/[\\^$.*+?()[\]{}|]/g,je=RegExp(Ne.source),Le=/^\s+|\s+$/g,$e=/^\s+/,Pe=/\s+$/,Re=/\{(?:\n\/\* \[wrapped with .+\] \*\/)?\n?/,Me=/\{\n\/\* \[wrapped with (.+)\] \*/,He=/,? & /,Fe=/[^\x00-\x2f\x3a-\x40\x5b-\x60\x7b-\x7f]+/g,qe=/\\(\\)?/g,Be=/\$\{([^\\}]*(?:\\.[^\\}]*)*)\}/g,We=/\w*$/,Ue=/^[-+]0x[0-9a-f]+$/i,ze=/^0b[01]+$/i,Ve=/^\[object .+?Constructor\]$/,Ke=/^0o[0-7]+$/i,Qe=/^(?:0|[1-9]\d*)$/,Ye=/[\xc0-\xd6\xd8-\xf6\xf8-\xff\u0100-\u017f]/g,Xe=/($^)/,Ge=/['\n\r\u2028\u2029\\]/g,Je="\\u0300-\\u036f\\ufe20-\\ufe2f\\u20d0-\\u20ff",Ze="\\xac\\xb1\\xd7\\xf7\\x00-\\x2f\\x3a-\\x40\\x5b-\\x60\\x7b-\\xbf\\u2000-\\u206f \\t\\x0b\\f\\xa0\\ufeff\\n\\r\\u2028\\u2029\\u1680\\u180e\\u2000\\u2001\\u2002\\u2003\\u2004\\u2005\\u2006\\u2007\\u2008\\u2009\\u200a\\u202f\\u205f\\u3000",et="[\\ud800-\\udfff]",tt="["+Ze+"]",nt="["+Je+"]",rt="\\d+",it="[\\u2700-\\u27bf]",ot="[a-z\\xdf-\\xf6\\xf8-\\xff]",at="[^\\ud800-\\udfff"+Ze+rt+"\\u2700-\\u27bfa-z\\xdf-\\xf6\\xf8-\\xffA-Z\\xc0-\\xd6\\xd8-\\xde]",st="\\ud83c[\\udffb-\\udfff]",ut="[^\\ud800-\\udfff]",ct="(?:\\ud83c[\\udde6-\\uddff]){2}",lt="[\\ud800-\\udbff][\\udc00-\\udfff]",ft="[A-Z\\xc0-\\xd6\\xd8-\\xde]",pt="(?:"+ot+"|"+at+")",dt="(?:"+ft+"|"+at+")",ht="(?:"+nt+"|"+st+")"+"?",vt="[\\ufe0e\\ufe0f]?"+ht+("(?:\\u200d(?:"+[ut,ct,lt].join("|")+")[\\ufe0e\\ufe0f]?"+ht+")*"),gt="(?:"+[it,ct,lt].join("|")+")"+vt,mt="(?:"+[ut+nt+"?",nt,ct,lt,et].join("|")+")",yt=RegExp("['’]","g"),_t=RegExp(nt,"g"),bt=RegExp(st+"(?="+st+")|"+mt+vt,"g"),wt=RegExp([ft+"?"+ot+"+(?:['’](?:d|ll|m|re|s|t|ve))?(?="+[tt,ft,"$"].join("|")+")",dt+"+(?:['’](?:D|LL|M|RE|S|T|VE))?(?="+[tt,ft+pt,"$"].join("|")+")",ft+"?"+pt+"+(?:['’](?:d|ll|m|re|s|t|ve))?",ft+"+(?:['’](?:D|LL|M|RE|S|T|VE))?","\\d*(?:1ST|2ND|3RD|(?![123])\\dTH)(?=\\b|[a-z_])","\\d*(?:1st|2nd|3rd|(?![123])\\dth)(?=\\b|[A-Z_])",rt,gt].join("|"),"g"),xt=RegExp("[\\u200d\\ud800-\\udfff"+Je+"\\ufe0e\\ufe0f]"),Ct=/[a-z][A-Z]|[A-Z]{2,}[a-z]|[0-9][a-zA-Z]|[a-zA-Z][0-9]|[^a-zA-Z0-9 ]/,Et=["Array","Buffer","DataView","Date","Error","Float32Array","Float64Array","Function","Int8Array","Int16Array","Int32Array","Map","Math","Object","Promise","RegExp","Set","String","Symbol","TypeError","Uint8Array","Uint8ClampedArray","Uint16Array","Uint32Array","WeakMap","_","clearTimeout","isFinite","parseInt","setTimeout"],Tt=-1,At={};At[le]=At[fe]=At[pe]=At[de]=At[he]=At[ve]=At[ge]=At[me]=At[ye]=!0,At[q]=At[B]=At[ue]=At[U]=At[ce]=At[z]=At[K]=At[Q]=At[X]=At[G]=At[Z]=At[te]=At[ne]=At[re]=At[ae]=!1;var St={};St[q]=St[B]=St[ue]=St[ce]=St[U]=St[z]=St[le]=St[fe]=St[pe]=St[de]=St[he]=St[X]=St[G]=St[Z]=St[te]=St[ne]=St[re]=St[ie]=St[ve]=St[ge]=St[me]=St[ye]=!0,St[K]=St[Q]=St[ae]=!1;var kt={"\\":"\\","'":"'","\n":"n","\r":"r","\u2028":"u2028","\u2029":"u2029"},Ot=parseFloat,Dt=parseInt,It="object"==typeof e&&e&&e.Object===Object&&e,Nt="object"==typeof self&&self&&self.Object===Object&&self,jt=It||Nt||Function("return this")(),Lt="object"==typeof t&&t&&!t.nodeType&&t,$t=Lt&&"object"==typeof r&&r&&!r.nodeType&&r,Pt=$t&&$t.exports===Lt,Rt=Pt&&It.process,Mt=function(){try{var e=$t&&$t.require&&$t.require("util").types;return e||Rt&&Rt.binding&&Rt.binding("util")}catch(e){}}(),Ht=Mt&&Mt.isArrayBuffer,Ft=Mt&&Mt.isDate,qt=Mt&&Mt.isMap,Bt=Mt&&Mt.isRegExp,Wt=Mt&&Mt.isSet,Ut=Mt&&Mt.isTypedArray;function zt(e,t,n){switch(n.length){case 0:return e.call(t);case 1:return e.call(t,n[0]);case 2:return e.call(t,n[0],n[1]);case 3:return e.call(t,n[0],n[1],n[2])}return e.apply(t,n)}function Vt(e,t,n,r){for(var i=-1,o=null==e?0:e.length;++i<o;){var a=e[i];t(r,a,n(a),e)}return r}function Kt(e,t){for(var n=-1,r=null==e?0:e.length;++n<r&&!1!==t(e[n],n,e););return e}function Qt(e,t){for(var n=null==e?0:e.length;n--&&!1!==t(e[n],n,e););return e}function Yt(e,t){for(var n=-1,r=null==e?0:e.length;++n<r;)if(!t(e[n],n,e))return!1;return!0}function Xt(e,t){for(var n=-1,r=null==e?0:e.length,i=0,o=[];++n<r;){var a=e[n];t(a,n,e)&&(o[i++]=a)}return o}function Gt(e,t){return!!(null==e?0:e.length)&&un(e,t,0)>-1}function Jt(e,t,n){for(var r=-1,i=null==e?0:e.length;++r<i;)if(n(t,e[r]))return!0;return!1}function Zt(e,t){for(var n=-1,r=null==e?0:e.length,i=Array(r);++n<r;)i[n]=t(e[n],n,e);return i}function en(e,t){for(var n=-1,r=t.length,i=e.length;++n<r;)e[i+n]=t[n];return e}function tn(e,t,n,r){var i=-1,o=null==e?0:e.length;for(r&&o&&(n=e[++i]);++i<o;)n=t(n,e[i],i,e);return n}function nn(e,t,n,r){var i=null==e?0:e.length;for(r&&i&&(n=e[--i]);i--;)n=t(n,e[i],i,e);return n}function rn(e,t){for(var n=-1,r=null==e?0:e.length;++n<r;)if(t(e[n],n,e))return!0;return!1}var on=pn("length");function an(e,t,n){var r;return n(e,function(e,n,i){if(t(e,n,i))return r=n,!1}),r}function sn(e,t,n,r){for(var i=e.length,o=n+(r?1:-1);r?o--:++o<i;)if(t(e[o],o,e))return o;return-1}function un(e,t,n){return t==t?function(e,t,n){var r=n-1,i=e.length;for(;++r<i;)if(e[r]===t)return r;return-1}(e,t,n):sn(e,ln,n)}function cn(e,t,n,r){for(var i=n-1,o=e.length;++i<o;)if(r(e[i],t))return i;return-1}function ln(e){return e!=e}function fn(e,t){var n=null==e?0:e.length;return n?vn(e,t)/n:P}function pn(e){return function(t){return null==t?o:t[e]}}function dn(e){return function(t){return null==e?o:e[t]}}function hn(e,t,n,r,i){return i(e,function(e,i,o){n=r?(r=!1,e):t(n,e,i,o)}),n}function vn(e,t){for(var n,r=-1,i=e.length;++r<i;){var a=t(e[r]);a!==o&&(n=n===o?a:n+a)}return n}function gn(e,t){for(var n=-1,r=Array(e);++n<e;)r[n]=t(n);return r}function mn(e){return function(t){return e(t)}}function yn(e,t){return Zt(t,function(t){return e[t]})}function _n(e,t){return e.has(t)}function bn(e,t){for(var n=-1,r=e.length;++n<r&&un(t,e[n],0)>-1;);return n}function wn(e,t){for(var n=e.length;n--&&un(t,e[n],0)>-1;);return n}var xn=dn({"À":"A","Á":"A","Â":"A","Ã":"A","Ä":"A","Å":"A","à":"a","á":"a","â":"a","ã":"a","ä":"a","å":"a","Ç":"C","ç":"c","Ð":"D","ð":"d","È":"E","É":"E","Ê":"E","Ë":"E","è":"e","é":"e","ê":"e","ë":"e","Ì":"I","Í":"I","Î":"I","Ï":"I","ì":"i","í":"i","î":"i","ï":"i","Ñ":"N","ñ":"n","Ò":"O","Ó":"O","Ô":"O","Õ":"O","Ö":"O","Ø":"O","ò":"o","ó":"o","ô":"o","õ":"o","ö":"o","ø":"o","Ù":"U","Ú":"U","Û":"U","Ü":"U","ù":"u","ú":"u","û":"u","ü":"u","Ý":"Y","ý":"y","ÿ":"y","Æ":"Ae","æ":"ae","Þ":"Th","þ":"th","ß":"ss","Ā":"A","Ă":"A","Ą":"A","ā":"a","ă":"a","ą":"a","Ć":"C","Ĉ":"C","Ċ":"C","Č":"C","ć":"c","ĉ":"c","ċ":"c","č":"c","Ď":"D","Đ":"D","ď":"d","đ":"d","Ē":"E","Ĕ":"E","Ė":"E","Ę":"E","Ě":"E","ē":"e","ĕ":"e","ė":"e","ę":"e","ě":"e","Ĝ":"G","Ğ":"G","Ġ":"G","Ģ":"G","ĝ":"g","ğ":"g","ġ":"g","ģ":"g","Ĥ":"H","Ħ":"H","ĥ":"h","ħ":"h","Ĩ":"I","Ī":"I","Ĭ":"I","Į":"I","İ":"I","ĩ":"i","ī":"i","ĭ":"i","į":"i","ı":"i","Ĵ":"J","ĵ":"j","Ķ":"K","ķ":"k","ĸ":"k","Ĺ":"L","Ļ":"L","Ľ":"L","Ŀ":"L","Ł":"L","ĺ":"l","ļ":"l","ľ":"l","ŀ":"l","ł":"l","Ń":"N","Ņ":"N","Ň":"N","Ŋ":"N","ń":"n","ņ":"n","ň":"n","ŋ":"n","Ō":"O","Ŏ":"O","Ő":"O","ō":"o","ŏ":"o","ő":"o","Ŕ":"R","Ŗ":"R","Ř":"R","ŕ":"r","ŗ":"r","ř":"r","Ś":"S","Ŝ":"S","Ş":"S","Š":"S","ś":"s","ŝ":"s","ş":"s","š":"s","Ţ":"T","Ť":"T","Ŧ":"T","ţ":"t","ť":"t","ŧ":"t","Ũ":"U","Ū":"U","Ŭ":"U","Ů":"U","Ű":"U","Ų":"U","ũ":"u","ū":"u","ŭ":"u","ů":"u","ű":"u","ų":"u","Ŵ":"W","ŵ":"w","Ŷ":"Y","ŷ":"y","Ÿ":"Y","Ź":"Z","Ż":"Z","Ž":"Z","ź":"z","ż":"z","ž":"z","Ĳ":"IJ","ĳ":"ij","Œ":"Oe","œ":"oe","ŉ":"'n","ſ":"s"}),Cn=dn({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"});function En(e){return"\\"+kt[e]}function Tn(e){return xt.test(e)}function An(e){var t=-1,n=Array(e.size);return e.forEach(function(e,r){n[++t]=[r,e]}),n}function Sn(e,t){return function(n){return e(t(n))}}function kn(e,t){for(var n=-1,r=e.length,i=0,o=[];++n<r;){var a=e[n];a!==t&&a!==f||(e[n]=f,o[i++]=n)}return o}function On(e,t){return"__proto__"==t?o:e[t]}function Dn(e){var t=-1,n=Array(e.size);return e.forEach(function(e){n[++t]=e}),n}function In(e){var t=-1,n=Array(e.size);return e.forEach(function(e){n[++t]=[e,e]}),n}function Nn(e){return Tn(e)?function(e){var t=bt.lastIndex=0;for(;bt.test(e);)++t;return t}(e):on(e)}function jn(e){return Tn(e)?function(e){return e.match(bt)||[]}(e):function(e){return e.split("")}(e)}var Ln=dn({"&amp;":"&","&lt;":"<","&gt;":">","&quot;":'"',"&#39;":"'"});var $n=function e(t){var n,r=(t=null==t?jt:$n.defaults(jt.Object(),t,$n.pick(jt,Et))).Array,i=t.Date,Je=t.Error,Ze=t.Function,et=t.Math,tt=t.Object,nt=t.RegExp,rt=t.String,it=t.TypeError,ot=r.prototype,at=Ze.prototype,st=tt.prototype,ut=t["__core-js_shared__"],ct=at.toString,lt=st.hasOwnProperty,ft=0,pt=(n=/[^.]+$/.exec(ut&&ut.keys&&ut.keys.IE_PROTO||""))?"Symbol(src)_1."+n:"",dt=st.toString,ht=ct.call(tt),vt=jt._,gt=nt("^"+ct.call(lt).replace(Ne,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$"),mt=Pt?t.Buffer:o,bt=t.Symbol,xt=t.Uint8Array,kt=mt?mt.allocUnsafe:o,It=Sn(tt.getPrototypeOf,tt),Nt=tt.create,Lt=st.propertyIsEnumerable,$t=ot.splice,Rt=bt?bt.isConcatSpreadable:o,Mt=bt?bt.iterator:o,on=bt?bt.toStringTag:o,dn=function(){try{var e=Fo(tt,"defineProperty");return e({},"",{}),e}catch(e){}}(),Pn=t.clearTimeout!==jt.clearTimeout&&t.clearTimeout,Rn=i&&i.now!==jt.Date.now&&i.now,Mn=t.setTimeout!==jt.setTimeout&&t.setTimeout,Hn=et.ceil,Fn=et.floor,qn=tt.getOwnPropertySymbols,Bn=mt?mt.isBuffer:o,Wn=t.isFinite,Un=ot.join,zn=Sn(tt.keys,tt),Vn=et.max,Kn=et.min,Qn=i.now,Yn=t.parseInt,Xn=et.random,Gn=ot.reverse,Jn=Fo(t,"DataView"),Zn=Fo(t,"Map"),er=Fo(t,"Promise"),tr=Fo(t,"Set"),nr=Fo(t,"WeakMap"),rr=Fo(tt,"create"),ir=nr&&new nr,or={},ar=fa(Jn),sr=fa(Zn),ur=fa(er),cr=fa(tr),lr=fa(nr),fr=bt?bt.prototype:o,pr=fr?fr.valueOf:o,dr=fr?fr.toString:o;function hr(e){if(ks(e)&&!ms(e)&&!(e instanceof yr)){if(e instanceof mr)return e;if(lt.call(e,"__wrapped__"))return pa(e)}return new mr(e)}var vr=function(){function e(){}return function(t){if(!Ss(t))return{};if(Nt)return Nt(t);e.prototype=t;var n=new e;return e.prototype=o,n}}();function gr(){}function mr(e,t){this.__wrapped__=e,this.__actions__=[],this.__chain__=!!t,this.__index__=0,this.__values__=o}function yr(e){this.__wrapped__=e,this.__actions__=[],this.__dir__=1,this.__filtered__=!1,this.__iteratees__=[],this.__takeCount__=R,this.__views__=[]}function _r(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}function br(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}function wr(e){var t=-1,n=null==e?0:e.length;for(this.clear();++t<n;){var r=e[t];this.set(r[0],r[1])}}function xr(e){var t=-1,n=null==e?0:e.length;for(this.__data__=new wr;++t<n;)this.add(e[t])}function Cr(e){var t=this.__data__=new br(e);this.size=t.size}function Er(e,t){var n=ms(e),r=!n&&gs(e),i=!n&&!r&&ws(e),o=!n&&!r&&!i&&Ps(e),a=n||r||i||o,s=a?gn(e.length,rt):[],u=s.length;for(var c in e)!t&&!lt.call(e,c)||a&&("length"==c||i&&("offset"==c||"parent"==c)||o&&("buffer"==c||"byteLength"==c||"byteOffset"==c)||Ko(c,u))||s.push(c);return s}function Tr(e){var t=e.length;return t?e[xi(0,t-1)]:o}function Ar(e,t){return ua(ro(e),$r(t,0,e.length))}function Sr(e){return ua(ro(e))}function kr(e,t,n){(n===o||ds(e[t],n))&&(n!==o||t in e)||jr(e,t,n)}function Or(e,t,n){var r=e[t];lt.call(e,t)&&ds(r,n)&&(n!==o||t in e)||jr(e,t,n)}function Dr(e,t){for(var n=e.length;n--;)if(ds(e[n][0],t))return n;return-1}function Ir(e,t,n,r){return Fr(e,function(e,i,o){t(r,e,n(e),o)}),r}function Nr(e,t){return e&&io(t,iu(t),e)}function jr(e,t,n){"__proto__"==t&&dn?dn(e,t,{configurable:!0,enumerable:!0,value:n,writable:!0}):e[t]=n}function Lr(e,t){for(var n=-1,i=t.length,a=r(i),s=null==e;++n<i;)a[n]=s?o:Zs(e,t[n]);return a}function $r(e,t,n){return e==e&&(n!==o&&(e=e<=n?e:n),t!==o&&(e=e>=t?e:t)),e}function Pr(e,t,n,r,i,a){var s,u=t&p,c=t&d,l=t&h;if(n&&(s=i?n(e,r,i,a):n(e)),s!==o)return s;if(!Ss(e))return e;var f=ms(e);if(f){if(s=function(e){var t=e.length,n=new e.constructor(t);return t&&"string"==typeof e[0]&&lt.call(e,"index")&&(n.index=e.index,n.input=e.input),n}(e),!u)return ro(e,s)}else{var v=Wo(e),g=v==Q||v==Y;if(ws(e))return Gi(e,u);if(v==Z||v==q||g&&!i){if(s=c||g?{}:zo(e),!u)return c?function(e,t){return io(e,Bo(e),t)}(e,function(e,t){return e&&io(t,ou(t),e)}(s,e)):function(e,t){return io(e,qo(e),t)}(e,Nr(s,e))}else{if(!St[v])return i?e:{};s=function(e,t,n){var r,i,o,a=e.constructor;switch(t){case ue:return Ji(e);case U:case z:return new a(+e);case ce:return function(e,t){var n=t?Ji(e.buffer):e.buffer;return new e.constructor(n,e.byteOffset,e.byteLength)}(e,n);case le:case fe:case pe:case de:case he:case ve:case ge:case me:case ye:return Zi(e,n);case X:return new a;case G:case re:return new a(e);case te:return(o=new(i=e).constructor(i.source,We.exec(i))).lastIndex=i.lastIndex,o;case ne:return new a;case ie:return r=e,pr?tt(pr.call(r)):{}}}(e,v,u)}}a||(a=new Cr);var m=a.get(e);if(m)return m;if(a.set(e,s),js(e))return e.forEach(function(r){s.add(Pr(r,t,n,r,e,a))}),s;if(Os(e))return e.forEach(function(r,i){s.set(i,Pr(r,t,n,i,e,a))}),s;var y=f?o:(l?c?jo:No:c?ou:iu)(e);return Kt(y||e,function(r,i){y&&(r=e[i=r]),Or(s,i,Pr(r,t,n,i,e,a))}),s}function Rr(e,t,n){var r=n.length;if(null==e)return!r;for(e=tt(e);r--;){var i=n[r],a=t[i],s=e[i];if(s===o&&!(i in e)||!a(s))return!1}return!0}function Mr(e,t,n){if("function"!=typeof e)throw new it(u);return ia(function(){e.apply(o,n)},t)}function Hr(e,t,n,r){var i=-1,o=Gt,s=!0,u=e.length,c=[],l=t.length;if(!u)return c;n&&(t=Zt(t,mn(n))),r?(o=Jt,s=!1):t.length>=a&&(o=_n,s=!1,t=new xr(t));e:for(;++i<u;){var f=e[i],p=null==n?f:n(f);if(f=r||0!==f?f:0,s&&p==p){for(var d=l;d--;)if(t[d]===p)continue e;c.push(f)}else o(t,p,r)||c.push(f)}return c}hr.templateSettings={escape:Ae,evaluate:Se,interpolate:ke,variable:"",imports:{_:hr}},hr.prototype=gr.prototype,hr.prototype.constructor=hr,mr.prototype=vr(gr.prototype),mr.prototype.constructor=mr,yr.prototype=vr(gr.prototype),yr.prototype.constructor=yr,_r.prototype.clear=function(){this.__data__=rr?rr(null):{},this.size=0},_r.prototype.delete=function(e){var t=this.has(e)&&delete this.__data__[e];return this.size-=t?1:0,t},_r.prototype.get=function(e){var t=this.__data__;if(rr){var n=t[e];return n===c?o:n}return lt.call(t,e)?t[e]:o},_r.prototype.has=function(e){var t=this.__data__;return rr?t[e]!==o:lt.call(t,e)},_r.prototype.set=function(e,t){var n=this.__data__;return this.size+=this.has(e)?0:1,n[e]=rr&&t===o?c:t,this},br.prototype.clear=function(){this.__data__=[],this.size=0},br.prototype.delete=function(e){var t=this.__data__,n=Dr(t,e);return!(n<0||(n==t.length-1?t.pop():$t.call(t,n,1),--this.size,0))},br.prototype.get=function(e){var t=this.__data__,n=Dr(t,e);return n<0?o:t[n][1]},br.prototype.has=function(e){return Dr(this.__data__,e)>-1},br.prototype.set=function(e,t){var n=this.__data__,r=Dr(n,e);return r<0?(++this.size,n.push([e,t])):n[r][1]=t,this},wr.prototype.clear=function(){this.size=0,this.__data__={hash:new _r,map:new(Zn||br),string:new _r}},wr.prototype.delete=function(e){var t=Mo(this,e).delete(e);return this.size-=t?1:0,t},wr.prototype.get=function(e){return Mo(this,e).get(e)},wr.prototype.has=function(e){return Mo(this,e).has(e)},wr.prototype.set=function(e,t){var n=Mo(this,e),r=n.size;return n.set(e,t),this.size+=n.size==r?0:1,this},xr.prototype.add=xr.prototype.push=function(e){return this.__data__.set(e,c),this},xr.prototype.has=function(e){return this.__data__.has(e)},Cr.prototype.clear=function(){this.__data__=new br,this.size=0},Cr.prototype.delete=function(e){var t=this.__data__,n=t.delete(e);return this.size=t.size,n},Cr.prototype.get=function(e){return this.__data__.get(e)},Cr.prototype.has=function(e){return this.__data__.has(e)},Cr.prototype.set=function(e,t){var n=this.__data__;if(n instanceof br){var r=n.__data__;if(!Zn||r.length<a-1)return r.push([e,t]),this.size=++n.size,this;n=this.__data__=new wr(r)}return n.set(e,t),this.size=n.size,this};var Fr=so(Qr),qr=so(Yr,!0);function Br(e,t){var n=!0;return Fr(e,function(e,r,i){return n=!!t(e,r,i)}),n}function Wr(e,t,n){for(var r=-1,i=e.length;++r<i;){var a=e[r],s=t(a);if(null!=s&&(u===o?s==s&&!$s(s):n(s,u)))var u=s,c=a}return c}function Ur(e,t){var n=[];return Fr(e,function(e,r,i){t(e,r,i)&&n.push(e)}),n}function zr(e,t,n,r,i){var o=-1,a=e.length;for(n||(n=Vo),i||(i=[]);++o<a;){var s=e[o];t>0&&n(s)?t>1?zr(s,t-1,n,r,i):en(i,s):r||(i[i.length]=s)}return i}var Vr=uo(),Kr=uo(!0);function Qr(e,t){return e&&Vr(e,t,iu)}function Yr(e,t){return e&&Kr(e,t,iu)}function Xr(e,t){return Xt(t,function(t){return Es(e[t])})}function Gr(e,t){for(var n=0,r=(t=Ki(t,e)).length;null!=e&&n<r;)e=e[la(t[n++])];return n&&n==r?e:o}function Jr(e,t,n){var r=t(e);return ms(e)?r:en(r,n(e))}function Zr(e){return null==e?e===o?oe:J:on&&on in tt(e)?function(e){var t=lt.call(e,on),n=e[on];try{e[on]=o;var r=!0}catch(e){}var i=dt.call(e);return r&&(t?e[on]=n:delete e[on]),i}(e):function(e){return dt.call(e)}(e)}function ei(e,t){return e>t}function ti(e,t){return null!=e&&lt.call(e,t)}function ni(e,t){return null!=e&&t in tt(e)}function ri(e,t,n){for(var i=n?Jt:Gt,a=e[0].length,s=e.length,u=s,c=r(s),l=1/0,f=[];u--;){var p=e[u];u&&t&&(p=Zt(p,mn(t))),l=Kn(p.length,l),c[u]=!n&&(t||a>=120&&p.length>=120)?new xr(u&&p):o}p=e[0];var d=-1,h=c[0];e:for(;++d<a&&f.length<l;){var v=p[d],g=t?t(v):v;if(v=n||0!==v?v:0,!(h?_n(h,g):i(f,g,n))){for(u=s;--u;){var m=c[u];if(!(m?_n(m,g):i(e[u],g,n)))continue e}h&&h.push(g),f.push(v)}}return f}function ii(e,t,n){var r=null==(e=na(e,t=Ki(t,e)))?e:e[la(Ca(t))];return null==r?o:zt(r,e,n)}function oi(e){return ks(e)&&Zr(e)==q}function ai(e,t,n,r,i){return e===t||(null==e||null==t||!ks(e)&&!ks(t)?e!=e&&t!=t:function(e,t,n,r,i,a){var s=ms(e),u=ms(t),c=s?B:Wo(e),l=u?B:Wo(t),f=(c=c==q?Z:c)==Z,p=(l=l==q?Z:l)==Z,d=c==l;if(d&&ws(e)){if(!ws(t))return!1;s=!0,f=!1}if(d&&!f)return a||(a=new Cr),s||Ps(e)?Do(e,t,n,r,i,a):function(e,t,n,r,i,o,a){switch(n){case ce:if(e.byteLength!=t.byteLength||e.byteOffset!=t.byteOffset)return!1;e=e.buffer,t=t.buffer;case ue:return!(e.byteLength!=t.byteLength||!o(new xt(e),new xt(t)));case U:case z:case G:return ds(+e,+t);case K:return e.name==t.name&&e.message==t.message;case te:case re:return e==t+"";case X:var s=An;case ne:var u=r&v;if(s||(s=Dn),e.size!=t.size&&!u)return!1;var c=a.get(e);if(c)return c==t;r|=g,a.set(e,t);var l=Do(s(e),s(t),r,i,o,a);return a.delete(e),l;case ie:if(pr)return pr.call(e)==pr.call(t)}return!1}(e,t,c,n,r,i,a);if(!(n&v)){var h=f&&lt.call(e,"__wrapped__"),m=p&&lt.call(t,"__wrapped__");if(h||m){var y=h?e.value():e,_=m?t.value():t;return a||(a=new Cr),i(y,_,n,r,a)}}return!!d&&(a||(a=new Cr),function(e,t,n,r,i,a){var s=n&v,u=No(e),c=u.length,l=No(t).length;if(c!=l&&!s)return!1;for(var f=c;f--;){var p=u[f];if(!(s?p in t:lt.call(t,p)))return!1}var d=a.get(e);if(d&&a.get(t))return d==t;var h=!0;a.set(e,t),a.set(t,e);for(var g=s;++f<c;){p=u[f];var m=e[p],y=t[p];if(r)var _=s?r(y,m,p,t,e,a):r(m,y,p,e,t,a);if(!(_===o?m===y||i(m,y,n,r,a):_)){h=!1;break}g||(g="constructor"==p)}if(h&&!g){var b=e.constructor,w=t.constructor;b!=w&&"constructor"in e&&"constructor"in t&&!("function"==typeof b&&b instanceof b&&"function"==typeof w&&w instanceof w)&&(h=!1)}return a.delete(e),a.delete(t),h}(e,t,n,r,i,a))}(e,t,n,r,ai,i))}function si(e,t,n,r){var i=n.length,a=i,s=!r;if(null==e)return!a;for(e=tt(e);i--;){var u=n[i];if(s&&u[2]?u[1]!==e[u[0]]:!(u[0]in e))return!1}for(;++i<a;){var c=(u=n[i])[0],l=e[c],f=u[1];if(s&&u[2]){if(l===o&&!(c in e))return!1}else{var p=new Cr;if(r)var d=r(l,f,c,e,t,p);if(!(d===o?ai(f,l,v|g,r,p):d))return!1}}return!0}function ui(e){return!(!Ss(e)||pt&&pt in e)&&(Es(e)?gt:Ve).test(fa(e))}function ci(e){return"function"==typeof e?e:null==e?Du:"object"==typeof e?ms(e)?vi(e[0],e[1]):hi(e):Hu(e)}function li(e){if(!Jo(e))return zn(e);var t=[];for(var n in tt(e))lt.call(e,n)&&"constructor"!=n&&t.push(n);return t}function fi(e){if(!Ss(e))return function(e){var t=[];if(null!=e)for(var n in tt(e))t.push(n);return t}(e);var t=Jo(e),n=[];for(var r in e)("constructor"!=r||!t&&lt.call(e,r))&&n.push(r);return n}function pi(e,t){return e<t}function di(e,t){var n=-1,i=_s(e)?r(e.length):[];return Fr(e,function(e,r,o){i[++n]=t(e,r,o)}),i}function hi(e){var t=Ho(e);return 1==t.length&&t[0][2]?ea(t[0][0],t[0][1]):function(n){return n===e||si(n,e,t)}}function vi(e,t){return Yo(e)&&Zo(t)?ea(la(e),t):function(n){var r=Zs(n,e);return r===o&&r===t?eu(n,e):ai(t,r,v|g)}}function gi(e,t,n,r,i){e!==t&&Vr(t,function(a,s){if(Ss(a))i||(i=new Cr),function(e,t,n,r,i,a,s){var u=On(e,n),c=On(t,n),l=s.get(c);if(l)kr(e,n,l);else{var f=a?a(u,c,n+"",e,t,s):o,p=f===o;if(p){var d=ms(c),h=!d&&ws(c),v=!d&&!h&&Ps(c);f=c,d||h||v?ms(u)?f=u:bs(u)?f=ro(u):h?(p=!1,f=Gi(c,!0)):v?(p=!1,f=Zi(c,!0)):f=[]:Is(c)||gs(c)?(f=u,gs(u)?f=Us(u):(!Ss(u)||r&&Es(u))&&(f=zo(c))):p=!1}p&&(s.set(c,f),i(f,c,r,a,s),s.delete(c)),kr(e,n,f)}}(e,t,s,n,gi,r,i);else{var u=r?r(On(e,s),a,s+"",e,t,i):o;u===o&&(u=a),kr(e,s,u)}},ou)}function mi(e,t){var n=e.length;if(n)return Ko(t+=t<0?n:0,n)?e[t]:o}function yi(e,t,n){var r=-1;return t=Zt(t.length?t:[Du],mn(Ro())),function(e,t){var n=e.length;for(e.sort(t);n--;)e[n]=e[n].value;return e}(di(e,function(e,n,i){return{criteria:Zt(t,function(t){return t(e)}),index:++r,value:e}}),function(e,t){return function(e,t,n){for(var r=-1,i=e.criteria,o=t.criteria,a=i.length,s=n.length;++r<a;){var u=eo(i[r],o[r]);if(u){if(r>=s)return u;var c=n[r];return u*("desc"==c?-1:1)}}return e.index-t.index}(e,t,n)})}function _i(e,t,n){for(var r=-1,i=t.length,o={};++r<i;){var a=t[r],s=Gr(e,a);n(s,a)&&Si(o,Ki(a,e),s)}return o}function bi(e,t,n,r){var i=r?cn:un,o=-1,a=t.length,s=e;for(e===t&&(t=ro(t)),n&&(s=Zt(e,mn(n)));++o<a;)for(var u=0,c=t[o],l=n?n(c):c;(u=i(s,l,u,r))>-1;)s!==e&&$t.call(s,u,1),$t.call(e,u,1);return e}function wi(e,t){for(var n=e?t.length:0,r=n-1;n--;){var i=t[n];if(n==r||i!==o){var o=i;Ko(i)?$t.call(e,i,1):Hi(e,i)}}return e}function xi(e,t){return e+Fn(Xn()*(t-e+1))}function Ci(e,t){var n="";if(!e||t<1||t>L)return n;do{t%2&&(n+=e),(t=Fn(t/2))&&(e+=e)}while(t);return n}function Ei(e,t){return oa(ta(e,t,Du),e+"")}function Ti(e){return Tr(du(e))}function Ai(e,t){var n=du(e);return ua(n,$r(t,0,n.length))}function Si(e,t,n,r){if(!Ss(e))return e;for(var i=-1,a=(t=Ki(t,e)).length,s=a-1,u=e;null!=u&&++i<a;){var c=la(t[i]),l=n;if(i!=s){var f=u[c];(l=r?r(f,c,u):o)===o&&(l=Ss(f)?f:Ko(t[i+1])?[]:{})}Or(u,c,l),u=u[c]}return e}var ki=ir?function(e,t){return ir.set(e,t),e}:Du,Oi=dn?function(e,t){return dn(e,"toString",{configurable:!0,enumerable:!1,value:Su(t),writable:!0})}:Du;function Di(e){return ua(du(e))}function Ii(e,t,n){var i=-1,o=e.length;t<0&&(t=-t>o?0:o+t),(n=n>o?o:n)<0&&(n+=o),o=t>n?0:n-t>>>0,t>>>=0;for(var a=r(o);++i<o;)a[i]=e[i+t];return a}function Ni(e,t){var n;return Fr(e,function(e,r,i){return!(n=t(e,r,i))}),!!n}function ji(e,t,n){var r=0,i=null==e?r:e.length;if("number"==typeof t&&t==t&&i<=H){for(;r<i;){var o=r+i>>>1,a=e[o];null!==a&&!$s(a)&&(n?a<=t:a<t)?r=o+1:i=o}return i}return Li(e,t,Du,n)}function Li(e,t,n,r){t=n(t);for(var i=0,a=null==e?0:e.length,s=t!=t,u=null===t,c=$s(t),l=t===o;i<a;){var f=Fn((i+a)/2),p=n(e[f]),d=p!==o,h=null===p,v=p==p,g=$s(p);if(s)var m=r||v;else m=l?v&&(r||d):u?v&&d&&(r||!h):c?v&&d&&!h&&(r||!g):!h&&!g&&(r?p<=t:p<t);m?i=f+1:a=f}return Kn(a,M)}function $i(e,t){for(var n=-1,r=e.length,i=0,o=[];++n<r;){var a=e[n],s=t?t(a):a;if(!n||!ds(s,u)){var u=s;o[i++]=0===a?0:a}}return o}function Pi(e){return"number"==typeof e?e:$s(e)?P:+e}function Ri(e){if("string"==typeof e)return e;if(ms(e))return Zt(e,Ri)+"";if($s(e))return dr?dr.call(e):"";var t=e+"";return"0"==t&&1/e==-j?"-0":t}function Mi(e,t,n){var r=-1,i=Gt,o=e.length,s=!0,u=[],c=u;if(n)s=!1,i=Jt;else if(o>=a){var l=t?null:Eo(e);if(l)return Dn(l);s=!1,i=_n,c=new xr}else c=t?[]:u;e:for(;++r<o;){var f=e[r],p=t?t(f):f;if(f=n||0!==f?f:0,s&&p==p){for(var d=c.length;d--;)if(c[d]===p)continue e;t&&c.push(p),u.push(f)}else i(c,p,n)||(c!==u&&c.push(p),u.push(f))}return u}function Hi(e,t){return null==(e=na(e,t=Ki(t,e)))||delete e[la(Ca(t))]}function Fi(e,t,n,r){return Si(e,t,n(Gr(e,t)),r)}function qi(e,t,n,r){for(var i=e.length,o=r?i:-1;(r?o--:++o<i)&&t(e[o],o,e););return n?Ii(e,r?0:o,r?o+1:i):Ii(e,r?o+1:0,r?i:o)}function Bi(e,t){var n=e;return n instanceof yr&&(n=n.value()),tn(t,function(e,t){return t.func.apply(t.thisArg,en([e],t.args))},n)}function Wi(e,t,n){var i=e.length;if(i<2)return i?Mi(e[0]):[];for(var o=-1,a=r(i);++o<i;)for(var s=e[o],u=-1;++u<i;)u!=o&&(a[o]=Hr(a[o]||s,e[u],t,n));return Mi(zr(a,1),t,n)}function Ui(e,t,n){for(var r=-1,i=e.length,a=t.length,s={};++r<i;){var u=r<a?t[r]:o;n(s,e[r],u)}return s}function zi(e){return bs(e)?e:[]}function Vi(e){return"function"==typeof e?e:Du}function Ki(e,t){return ms(e)?e:Yo(e,t)?[e]:ca(zs(e))}var Qi=Ei;function Yi(e,t,n){var r=e.length;return n=n===o?r:n,!t&&n>=r?e:Ii(e,t,n)}var Xi=Pn||function(e){return jt.clearTimeout(e)};function Gi(e,t){if(t)return e.slice();var n=e.length,r=kt?kt(n):new e.constructor(n);return e.copy(r),r}function Ji(e){var t=new e.constructor(e.byteLength);return new xt(t).set(new xt(e)),t}function Zi(e,t){var n=t?Ji(e.buffer):e.buffer;return new e.constructor(n,e.byteOffset,e.length)}function eo(e,t){if(e!==t){var n=e!==o,r=null===e,i=e==e,a=$s(e),s=t!==o,u=null===t,c=t==t,l=$s(t);if(!u&&!l&&!a&&e>t||a&&s&&c&&!u&&!l||r&&s&&c||!n&&c||!i)return 1;if(!r&&!a&&!l&&e<t||l&&n&&i&&!r&&!a||u&&n&&i||!s&&i||!c)return-1}return 0}function to(e,t,n,i){for(var o=-1,a=e.length,s=n.length,u=-1,c=t.length,l=Vn(a-s,0),f=r(c+l),p=!i;++u<c;)f[u]=t[u];for(;++o<s;)(p||o<a)&&(f[n[o]]=e[o]);for(;l--;)f[u++]=e[o++];return f}function no(e,t,n,i){for(var o=-1,a=e.length,s=-1,u=n.length,c=-1,l=t.length,f=Vn(a-u,0),p=r(f+l),d=!i;++o<f;)p[o]=e[o];for(var h=o;++c<l;)p[h+c]=t[c];for(;++s<u;)(d||o<a)&&(p[h+n[s]]=e[o++]);return p}function ro(e,t){var n=-1,i=e.length;for(t||(t=r(i));++n<i;)t[n]=e[n];return t}function io(e,t,n,r){var i=!n;n||(n={});for(var a=-1,s=t.length;++a<s;){var u=t[a],c=r?r(n[u],e[u],u,n,e):o;c===o&&(c=e[u]),i?jr(n,u,c):Or(n,u,c)}return n}function oo(e,t){return function(n,r){var i=ms(n)?Vt:Ir,o=t?t():{};return i(n,e,Ro(r,2),o)}}function ao(e){return Ei(function(t,n){var r=-1,i=n.length,a=i>1?n[i-1]:o,s=i>2?n[2]:o;for(a=e.length>3&&"function"==typeof a?(i--,a):o,s&&Qo(n[0],n[1],s)&&(a=i<3?o:a,i=1),t=tt(t);++r<i;){var u=n[r];u&&e(t,u,r,a)}return t})}function so(e,t){return function(n,r){if(null==n)return n;if(!_s(n))return e(n,r);for(var i=n.length,o=t?i:-1,a=tt(n);(t?o--:++o<i)&&!1!==r(a[o],o,a););return n}}function uo(e){return function(t,n,r){for(var i=-1,o=tt(t),a=r(t),s=a.length;s--;){var u=a[e?s:++i];if(!1===n(o[u],u,o))break}return t}}function co(e){return function(t){var n=Tn(t=zs(t))?jn(t):o,r=n?n[0]:t.charAt(0),i=n?Yi(n,1).join(""):t.slice(1);return r[e]()+i}}function lo(e){return function(t){return tn(Eu(gu(t).replace(yt,"")),e,"")}}function fo(e){return function(){var t=arguments;switch(t.length){case 0:return new e;case 1:return new e(t[0]);case 2:return new e(t[0],t[1]);case 3:return new e(t[0],t[1],t[2]);case 4:return new e(t[0],t[1],t[2],t[3]);case 5:return new e(t[0],t[1],t[2],t[3],t[4]);case 6:return new e(t[0],t[1],t[2],t[3],t[4],t[5]);case 7:return new e(t[0],t[1],t[2],t[3],t[4],t[5],t[6])}var n=vr(e.prototype),r=e.apply(n,t);return Ss(r)?r:n}}function po(e){return function(t,n,r){var i=tt(t);if(!_s(t)){var a=Ro(n,3);t=iu(t),n=function(e){return a(i[e],e,i)}}var s=e(t,n,r);return s>-1?i[a?t[s]:s]:o}}function ho(e){return Io(function(t){var n=t.length,r=n,i=mr.prototype.thru;for(e&&t.reverse();r--;){var a=t[r];if("function"!=typeof a)throw new it(u);if(i&&!s&&"wrapper"==$o(a))var s=new mr([],!0)}for(r=s?r:n;++r<n;){var c=$o(a=t[r]),l="wrapper"==c?Lo(a):o;s=l&&Xo(l[0])&&l[1]==(E|b|x|T)&&!l[4].length&&1==l[9]?s[$o(l[0])].apply(s,l[3]):1==a.length&&Xo(a)?s[c]():s.thru(a)}return function(){var e=arguments,r=e[0];if(s&&1==e.length&&ms(r))return s.plant(r).value();for(var i=0,o=n?t[i].apply(this,e):r;++i<n;)o=t[i].call(this,o);return o}})}function vo(e,t,n,i,a,s,u,c,l,f){var p=t&E,d=t&m,h=t&y,v=t&(b|w),g=t&A,_=h?o:fo(e);return function m(){for(var y=arguments.length,b=r(y),w=y;w--;)b[w]=arguments[w];if(v)var x=Po(m),C=function(e,t){for(var n=e.length,r=0;n--;)e[n]===t&&++r;return r}(b,x);if(i&&(b=to(b,i,a,v)),s&&(b=no(b,s,u,v)),y-=C,v&&y<f){var E=kn(b,x);return xo(e,t,vo,m.placeholder,n,b,E,c,l,f-y)}var T=d?n:this,A=h?T[e]:e;return y=b.length,c?b=function(e,t){for(var n=e.length,r=Kn(t.length,n),i=ro(e);r--;){var a=t[r];e[r]=Ko(a,n)?i[a]:o}return e}(b,c):g&&y>1&&b.reverse(),p&&l<y&&(b.length=l),this&&this!==jt&&this instanceof m&&(A=_||fo(A)),A.apply(T,b)}}function go(e,t){return function(n,r){return function(e,t,n,r){return Qr(e,function(e,i,o){t(r,n(e),i,o)}),r}(n,e,t(r),{})}}function mo(e,t){return function(n,r){var i;if(n===o&&r===o)return t;if(n!==o&&(i=n),r!==o){if(i===o)return r;"string"==typeof n||"string"==typeof r?(n=Ri(n),r=Ri(r)):(n=Pi(n),r=Pi(r)),i=e(n,r)}return i}}function yo(e){return Io(function(t){return t=Zt(t,mn(Ro())),Ei(function(n){var r=this;return e(t,function(e){return zt(e,r,n)})})})}function _o(e,t){var n=(t=t===o?" ":Ri(t)).length;if(n<2)return n?Ci(t,e):t;var r=Ci(t,Hn(e/Nn(t)));return Tn(t)?Yi(jn(r),0,e).join(""):r.slice(0,e)}function bo(e){return function(t,n,i){return i&&"number"!=typeof i&&Qo(t,n,i)&&(n=i=o),t=Fs(t),n===o?(n=t,t=0):n=Fs(n),function(e,t,n,i){for(var o=-1,a=Vn(Hn((t-e)/(n||1)),0),s=r(a);a--;)s[i?a:++o]=e,e+=n;return s}(t,n,i=i===o?t<n?1:-1:Fs(i),e)}}function wo(e){return function(t,n){return"string"==typeof t&&"string"==typeof n||(t=Ws(t),n=Ws(n)),e(t,n)}}function xo(e,t,n,r,i,a,s,u,c,l){var f=t&b;t|=f?x:C,(t&=~(f?C:x))&_||(t&=~(m|y));var p=[e,t,i,f?a:o,f?s:o,f?o:a,f?o:s,u,c,l],d=n.apply(o,p);return Xo(e)&&ra(d,p),d.placeholder=r,aa(d,e,t)}function Co(e){var t=et[e];return function(e,n){if(e=Ws(e),n=null==n?0:Kn(qs(n),292)){var r=(zs(e)+"e").split("e");return+((r=(zs(t(r[0]+"e"+(+r[1]+n)))+"e").split("e"))[0]+"e"+(+r[1]-n))}return t(e)}}var Eo=tr&&1/Dn(new tr([,-0]))[1]==j?function(e){return new tr(e)}:$u;function To(e){return function(t){var n=Wo(t);return n==X?An(t):n==ne?In(t):function(e,t){return Zt(t,function(t){return[t,e[t]]})}(t,e(t))}}function Ao(e,t,n,i,a,s,c,l){var p=t&y;if(!p&&"function"!=typeof e)throw new it(u);var d=i?i.length:0;if(d||(t&=~(x|C),i=a=o),c=c===o?c:Vn(qs(c),0),l=l===o?l:qs(l),d-=a?a.length:0,t&C){var h=i,v=a;i=a=o}var g=p?o:Lo(e),A=[e,t,n,i,a,h,v,s,c,l];if(g&&function(e,t){var n=e[1],r=t[1],i=n|r,o=i<(m|y|E),a=r==E&&n==b||r==E&&n==T&&e[7].length<=t[8]||r==(E|T)&&t[7].length<=t[8]&&n==b;if(!o&&!a)return e;r&m&&(e[2]=t[2],i|=n&m?0:_);var s=t[3];if(s){var u=e[3];e[3]=u?to(u,s,t[4]):s,e[4]=u?kn(e[3],f):t[4]}(s=t[5])&&(u=e[5],e[5]=u?no(u,s,t[6]):s,e[6]=u?kn(e[5],f):t[6]),(s=t[7])&&(e[7]=s),r&E&&(e[8]=null==e[8]?t[8]:Kn(e[8],t[8])),null==e[9]&&(e[9]=t[9]),e[0]=t[0],e[1]=i}(A,g),e=A[0],t=A[1],n=A[2],i=A[3],a=A[4],!(l=A[9]=A[9]===o?p?0:e.length:Vn(A[9]-d,0))&&t&(b|w)&&(t&=~(b|w)),t&&t!=m)S=t==b||t==w?function(e,t,n){var i=fo(e);return function a(){for(var s=arguments.length,u=r(s),c=s,l=Po(a);c--;)u[c]=arguments[c];var f=s<3&&u[0]!==l&&u[s-1]!==l?[]:kn(u,l);return(s-=f.length)<n?xo(e,t,vo,a.placeholder,o,u,f,o,o,n-s):zt(this&&this!==jt&&this instanceof a?i:e,this,u)}}(e,t,l):t!=x&&t!=(m|x)||a.length?vo.apply(o,A):function(e,t,n,i){var o=t&m,a=fo(e);return function t(){for(var s=-1,u=arguments.length,c=-1,l=i.length,f=r(l+u),p=this&&this!==jt&&this instanceof t?a:e;++c<l;)f[c]=i[c];for(;u--;)f[c++]=arguments[++s];return zt(p,o?n:this,f)}}(e,t,n,i);else var S=function(e,t,n){var r=t&m,i=fo(e);return function t(){return(this&&this!==jt&&this instanceof t?i:e).apply(r?n:this,arguments)}}(e,t,n);return aa((g?ki:ra)(S,A),e,t)}function So(e,t,n,r){return e===o||ds(e,st[n])&&!lt.call(r,n)?t:e}function ko(e,t,n,r,i,a){return Ss(e)&&Ss(t)&&(a.set(t,e),gi(e,t,o,ko,a),a.delete(t)),e}function Oo(e){return Is(e)?o:e}function Do(e,t,n,r,i,a){var s=n&v,u=e.length,c=t.length;if(u!=c&&!(s&&c>u))return!1;var l=a.get(e);if(l&&a.get(t))return l==t;var f=-1,p=!0,d=n&g?new xr:o;for(a.set(e,t),a.set(t,e);++f<u;){var h=e[f],m=t[f];if(r)var y=s?r(m,h,f,t,e,a):r(h,m,f,e,t,a);if(y!==o){if(y)continue;p=!1;break}if(d){if(!rn(t,function(e,t){if(!_n(d,t)&&(h===e||i(h,e,n,r,a)))return d.push(t)})){p=!1;break}}else if(h!==m&&!i(h,m,n,r,a)){p=!1;break}}return a.delete(e),a.delete(t),p}function Io(e){return oa(ta(e,o,ya),e+"")}function No(e){return Jr(e,iu,qo)}function jo(e){return Jr(e,ou,Bo)}var Lo=ir?function(e){return ir.get(e)}:$u;function $o(e){for(var t=e.name+"",n=or[t],r=lt.call(or,t)?n.length:0;r--;){var i=n[r],o=i.func;if(null==o||o==e)return i.name}return t}function Po(e){return(lt.call(hr,"placeholder")?hr:e).placeholder}function Ro(){var e=hr.iteratee||Iu;return e=e===Iu?ci:e,arguments.length?e(arguments[0],arguments[1]):e}function Mo(e,t){var n,r,i=e.__data__;return("string"==(r=typeof(n=t))||"number"==r||"symbol"==r||"boolean"==r?"__proto__"!==n:null===n)?i["string"==typeof t?"string":"hash"]:i.map}function Ho(e){for(var t=iu(e),n=t.length;n--;){var r=t[n],i=e[r];t[n]=[r,i,Zo(i)]}return t}function Fo(e,t){var n=function(e,t){return null==e?o:e[t]}(e,t);return ui(n)?n:o}var qo=qn?function(e){return null==e?[]:(e=tt(e),Xt(qn(e),function(t){return Lt.call(e,t)}))}:Bu,Bo=qn?function(e){for(var t=[];e;)en(t,qo(e)),e=It(e);return t}:Bu,Wo=Zr;function Uo(e,t,n){for(var r=-1,i=(t=Ki(t,e)).length,o=!1;++r<i;){var a=la(t[r]);if(!(o=null!=e&&n(e,a)))break;e=e[a]}return o||++r!=i?o:!!(i=null==e?0:e.length)&&As(i)&&Ko(a,i)&&(ms(e)||gs(e))}function zo(e){return"function"!=typeof e.constructor||Jo(e)?{}:vr(It(e))}function Vo(e){return ms(e)||gs(e)||!!(Rt&&e&&e[Rt])}function Ko(e,t){var n=typeof e;return!!(t=null==t?L:t)&&("number"==n||"symbol"!=n&&Qe.test(e))&&e>-1&&e%1==0&&e<t}function Qo(e,t,n){if(!Ss(n))return!1;var r=typeof t;return!!("number"==r?_s(n)&&Ko(t,n.length):"string"==r&&t in n)&&ds(n[t],e)}function Yo(e,t){if(ms(e))return!1;var n=typeof e;return!("number"!=n&&"symbol"!=n&&"boolean"!=n&&null!=e&&!$s(e))||De.test(e)||!Oe.test(e)||null!=t&&e in tt(t)}function Xo(e){var t=$o(e),n=hr[t];if("function"!=typeof n||!(t in yr.prototype))return!1;if(e===n)return!0;var r=Lo(n);return!!r&&e===r[0]}(Jn&&Wo(new Jn(new ArrayBuffer(1)))!=ce||Zn&&Wo(new Zn)!=X||er&&"[object Promise]"!=Wo(er.resolve())||tr&&Wo(new tr)!=ne||nr&&Wo(new nr)!=ae)&&(Wo=function(e){var t=Zr(e),n=t==Z?e.constructor:o,r=n?fa(n):"";if(r)switch(r){case ar:return ce;case sr:return X;case ur:return"[object Promise]";case cr:return ne;case lr:return ae}return t});var Go=ut?Es:Wu;function Jo(e){var t=e&&e.constructor;return e===("function"==typeof t&&t.prototype||st)}function Zo(e){return e==e&&!Ss(e)}function ea(e,t){return function(n){return null!=n&&n[e]===t&&(t!==o||e in tt(n))}}function ta(e,t,n){return t=Vn(t===o?e.length-1:t,0),function(){for(var i=arguments,o=-1,a=Vn(i.length-t,0),s=r(a);++o<a;)s[o]=i[t+o];o=-1;for(var u=r(t+1);++o<t;)u[o]=i[o];return u[t]=n(s),zt(e,this,u)}}function na(e,t){return t.length<2?e:Gr(e,Ii(t,0,-1))}var ra=sa(ki),ia=Mn||function(e,t){return jt.setTimeout(e,t)},oa=sa(Oi);function aa(e,t,n){var r=t+"";return oa(e,function(e,t){var n=t.length;if(!n)return e;var r=n-1;return t[r]=(n>1?"& ":"")+t[r],t=t.join(n>2?", ":" "),e.replace(Re,"{\n/* [wrapped with "+t+"] */\n")}(r,function(e,t){return Kt(F,function(n){var r="_."+n[0];t&n[1]&&!Gt(e,r)&&e.push(r)}),e.sort()}(function(e){var t=e.match(Me);return t?t[1].split(He):[]}(r),n)))}function sa(e){var t=0,n=0;return function(){var r=Qn(),i=D-(r-n);if(n=r,i>0){if(++t>=O)return arguments[0]}else t=0;return e.apply(o,arguments)}}function ua(e,t){var n=-1,r=e.length,i=r-1;for(t=t===o?r:t;++n<t;){var a=xi(n,i),s=e[a];e[a]=e[n],e[n]=s}return e.length=t,e}var ca=function(e){var t=ss(e,function(e){return n.size===l&&n.clear(),e}),n=t.cache;return t}(function(e){var t=[];return 46===e.charCodeAt(0)&&t.push(""),e.replace(Ie,function(e,n,r,i){t.push(r?i.replace(qe,"$1"):n||e)}),t});function la(e){if("string"==typeof e||$s(e))return e;var t=e+"";return"0"==t&&1/e==-j?"-0":t}function fa(e){if(null!=e){try{return ct.call(e)}catch(e){}try{return e+""}catch(e){}}return""}function pa(e){if(e instanceof yr)return e.clone();var t=new mr(e.__wrapped__,e.__chain__);return t.__actions__=ro(e.__actions__),t.__index__=e.__index__,t.__values__=e.__values__,t}var da=Ei(function(e,t){return bs(e)?Hr(e,zr(t,1,bs,!0)):[]}),ha=Ei(function(e,t){var n=Ca(t);return bs(n)&&(n=o),bs(e)?Hr(e,zr(t,1,bs,!0),Ro(n,2)):[]}),va=Ei(function(e,t){var n=Ca(t);return bs(n)&&(n=o),bs(e)?Hr(e,zr(t,1,bs,!0),o,n):[]});function ga(e,t,n){var r=null==e?0:e.length;if(!r)return-1;var i=null==n?0:qs(n);return i<0&&(i=Vn(r+i,0)),sn(e,Ro(t,3),i)}function ma(e,t,n){var r=null==e?0:e.length;if(!r)return-1;var i=r-1;return n!==o&&(i=qs(n),i=n<0?Vn(r+i,0):Kn(i,r-1)),sn(e,Ro(t,3),i,!0)}function ya(e){return null!=e&&e.length?zr(e,1):[]}function _a(e){return e&&e.length?e[0]:o}var ba=Ei(function(e){var t=Zt(e,zi);return t.length&&t[0]===e[0]?ri(t):[]}),wa=Ei(function(e){var t=Ca(e),n=Zt(e,zi);return t===Ca(n)?t=o:n.pop(),n.length&&n[0]===e[0]?ri(n,Ro(t,2)):[]}),xa=Ei(function(e){var t=Ca(e),n=Zt(e,zi);return(t="function"==typeof t?t:o)&&n.pop(),n.length&&n[0]===e[0]?ri(n,o,t):[]});function Ca(e){var t=null==e?0:e.length;return t?e[t-1]:o}var Ea=Ei(Ta);function Ta(e,t){return e&&e.length&&t&&t.length?bi(e,t):e}var Aa=Io(function(e,t){var n=null==e?0:e.length,r=Lr(e,t);return wi(e,Zt(t,function(e){return Ko(e,n)?+e:e}).sort(eo)),r});function Sa(e){return null==e?e:Gn.call(e)}var ka=Ei(function(e){return Mi(zr(e,1,bs,!0))}),Oa=Ei(function(e){var t=Ca(e);return bs(t)&&(t=o),Mi(zr(e,1,bs,!0),Ro(t,2))}),Da=Ei(function(e){var t=Ca(e);return t="function"==typeof t?t:o,Mi(zr(e,1,bs,!0),o,t)});function Ia(e){if(!e||!e.length)return[];var t=0;return e=Xt(e,function(e){if(bs(e))return t=Vn(e.length,t),!0}),gn(t,function(t){return Zt(e,pn(t))})}function Na(e,t){if(!e||!e.length)return[];var n=Ia(e);return null==t?n:Zt(n,function(e){return zt(t,o,e)})}var ja=Ei(function(e,t){return bs(e)?Hr(e,t):[]}),La=Ei(function(e){return Wi(Xt(e,bs))}),$a=Ei(function(e){var t=Ca(e);return bs(t)&&(t=o),Wi(Xt(e,bs),Ro(t,2))}),Pa=Ei(function(e){var t=Ca(e);return t="function"==typeof t?t:o,Wi(Xt(e,bs),o,t)}),Ra=Ei(Ia);var Ma=Ei(function(e){var t=e.length,n=t>1?e[t-1]:o;return Na(e,n="function"==typeof n?(e.pop(),n):o)});function Ha(e){var t=hr(e);return t.__chain__=!0,t}function Fa(e,t){return t(e)}var qa=Io(function(e){var t=e.length,n=t?e[0]:0,r=this.__wrapped__,i=function(t){return Lr(t,e)};return!(t>1||this.__actions__.length)&&r instanceof yr&&Ko(n)?((r=r.slice(n,+n+(t?1:0))).__actions__.push({func:Fa,args:[i],thisArg:o}),new mr(r,this.__chain__).thru(function(e){return t&&!e.length&&e.push(o),e})):this.thru(i)});var Ba=oo(function(e,t,n){lt.call(e,n)?++e[n]:jr(e,n,1)});var Wa=po(ga),Ua=po(ma);function za(e,t){return(ms(e)?Kt:Fr)(e,Ro(t,3))}function Va(e,t){return(ms(e)?Qt:qr)(e,Ro(t,3))}var Ka=oo(function(e,t,n){lt.call(e,n)?e[n].push(t):jr(e,n,[t])});var Qa=Ei(function(e,t,n){var i=-1,o="function"==typeof t,a=_s(e)?r(e.length):[];return Fr(e,function(e){a[++i]=o?zt(t,e,n):ii(e,t,n)}),a}),Ya=oo(function(e,t,n){jr(e,n,t)});function Xa(e,t){return(ms(e)?Zt:di)(e,Ro(t,3))}var Ga=oo(function(e,t,n){e[n?0:1].push(t)},function(){return[[],[]]});var Ja=Ei(function(e,t){if(null==e)return[];var n=t.length;return n>1&&Qo(e,t[0],t[1])?t=[]:n>2&&Qo(t[0],t[1],t[2])&&(t=[t[0]]),yi(e,zr(t,1),[])}),Za=Rn||function(){return jt.Date.now()};function es(e,t,n){return t=n?o:t,t=e&&null==t?e.length:t,Ao(e,E,o,o,o,o,t)}function ts(e,t){var n;if("function"!=typeof t)throw new it(u);return e=qs(e),function(){return--e>0&&(n=t.apply(this,arguments)),e<=1&&(t=o),n}}var ns=Ei(function(e,t,n){var r=m;if(n.length){var i=kn(n,Po(ns));r|=x}return Ao(e,r,t,n,i)}),rs=Ei(function(e,t,n){var r=m|y;if(n.length){var i=kn(n,Po(rs));r|=x}return Ao(t,r,e,n,i)});function is(e,t,n){var r,i,a,s,c,l,f=0,p=!1,d=!1,h=!0;if("function"!=typeof e)throw new it(u);function v(t){var n=r,a=i;return r=i=o,f=t,s=e.apply(a,n)}function g(e){var n=e-l;return l===o||n>=t||n<0||d&&e-f>=a}function m(){var e=Za();if(g(e))return y(e);c=ia(m,function(e){var n=t-(e-l);return d?Kn(n,a-(e-f)):n}(e))}function y(e){return c=o,h&&r?v(e):(r=i=o,s)}function _(){var e=Za(),n=g(e);if(r=arguments,i=this,l=e,n){if(c===o)return function(e){return f=e,c=ia(m,t),p?v(e):s}(l);if(d)return c=ia(m,t),v(l)}return c===o&&(c=ia(m,t)),s}return t=Ws(t)||0,Ss(n)&&(p=!!n.leading,a=(d="maxWait"in n)?Vn(Ws(n.maxWait)||0,t):a,h="trailing"in n?!!n.trailing:h),_.cancel=function(){c!==o&&Xi(c),f=0,r=l=i=c=o},_.flush=function(){return c===o?s:y(Za())},_}var os=Ei(function(e,t){return Mr(e,1,t)}),as=Ei(function(e,t,n){return Mr(e,Ws(t)||0,n)});function ss(e,t){if("function"!=typeof e||null!=t&&"function"!=typeof t)throw new it(u);var n=function(){var r=arguments,i=t?t.apply(this,r):r[0],o=n.cache;if(o.has(i))return o.get(i);var a=e.apply(this,r);return n.cache=o.set(i,a)||o,a};return n.cache=new(ss.Cache||wr),n}function us(e){if("function"!=typeof e)throw new it(u);return function(){var t=arguments;switch(t.length){case 0:return!e.call(this);case 1:return!e.call(this,t[0]);case 2:return!e.call(this,t[0],t[1]);case 3:return!e.call(this,t[0],t[1],t[2])}return!e.apply(this,t)}}ss.Cache=wr;var cs=Qi(function(e,t){var n=(t=1==t.length&&ms(t[0])?Zt(t[0],mn(Ro())):Zt(zr(t,1),mn(Ro()))).length;return Ei(function(r){for(var i=-1,o=Kn(r.length,n);++i<o;)r[i]=t[i].call(this,r[i]);return zt(e,this,r)})}),ls=Ei(function(e,t){var n=kn(t,Po(ls));return Ao(e,x,o,t,n)}),fs=Ei(function(e,t){var n=kn(t,Po(fs));return Ao(e,C,o,t,n)}),ps=Io(function(e,t){return Ao(e,T,o,o,o,t)});function ds(e,t){return e===t||e!=e&&t!=t}var hs=wo(ei),vs=wo(function(e,t){return e>=t}),gs=oi(function(){return arguments}())?oi:function(e){return ks(e)&&lt.call(e,"callee")&&!Lt.call(e,"callee")},ms=r.isArray,ys=Ht?mn(Ht):function(e){return ks(e)&&Zr(e)==ue};function _s(e){return null!=e&&As(e.length)&&!Es(e)}function bs(e){return ks(e)&&_s(e)}var ws=Bn||Wu,xs=Ft?mn(Ft):function(e){return ks(e)&&Zr(e)==z};function Cs(e){if(!ks(e))return!1;var t=Zr(e);return t==K||t==V||"string"==typeof e.message&&"string"==typeof e.name&&!Is(e)}function Es(e){if(!Ss(e))return!1;var t=Zr(e);return t==Q||t==Y||t==W||t==ee}function Ts(e){return"number"==typeof e&&e==qs(e)}function As(e){return"number"==typeof e&&e>-1&&e%1==0&&e<=L}function Ss(e){var t=typeof e;return null!=e&&("object"==t||"function"==t)}function ks(e){return null!=e&&"object"==typeof e}var Os=qt?mn(qt):function(e){return ks(e)&&Wo(e)==X};function Ds(e){return"number"==typeof e||ks(e)&&Zr(e)==G}function Is(e){if(!ks(e)||Zr(e)!=Z)return!1;var t=It(e);if(null===t)return!0;var n=lt.call(t,"constructor")&&t.constructor;return"function"==typeof n&&n instanceof n&&ct.call(n)==ht}var Ns=Bt?mn(Bt):function(e){return ks(e)&&Zr(e)==te};var js=Wt?mn(Wt):function(e){return ks(e)&&Wo(e)==ne};function Ls(e){return"string"==typeof e||!ms(e)&&ks(e)&&Zr(e)==re}function $s(e){return"symbol"==typeof e||ks(e)&&Zr(e)==ie}var Ps=Ut?mn(Ut):function(e){return ks(e)&&As(e.length)&&!!At[Zr(e)]};var Rs=wo(pi),Ms=wo(function(e,t){return e<=t});function Hs(e){if(!e)return[];if(_s(e))return Ls(e)?jn(e):ro(e);if(Mt&&e[Mt])return function(e){for(var t,n=[];!(t=e.next()).done;)n.push(t.value);return n}(e[Mt]());var t=Wo(e);return(t==X?An:t==ne?Dn:du)(e)}function Fs(e){return e?(e=Ws(e))===j||e===-j?(e<0?-1:1)*$:e==e?e:0:0===e?e:0}function qs(e){var t=Fs(e),n=t%1;return t==t?n?t-n:t:0}function Bs(e){return e?$r(qs(e),0,R):0}function Ws(e){if("number"==typeof e)return e;if($s(e))return P;if(Ss(e)){var t="function"==typeof e.valueOf?e.valueOf():e;e=Ss(t)?t+"":t}if("string"!=typeof e)return 0===e?e:+e;e=e.replace(Le,"");var n=ze.test(e);return n||Ke.test(e)?Dt(e.slice(2),n?2:8):Ue.test(e)?P:+e}function Us(e){return io(e,ou(e))}function zs(e){return null==e?"":Ri(e)}var Vs=ao(function(e,t){if(Jo(t)||_s(t))io(t,iu(t),e);else for(var n in t)lt.call(t,n)&&Or(e,n,t[n])}),Ks=ao(function(e,t){io(t,ou(t),e)}),Qs=ao(function(e,t,n,r){io(t,ou(t),e,r)}),Ys=ao(function(e,t,n,r){io(t,iu(t),e,r)}),Xs=Io(Lr);var Gs=Ei(function(e,t){e=tt(e);var n=-1,r=t.length,i=r>2?t[2]:o;for(i&&Qo(t[0],t[1],i)&&(r=1);++n<r;)for(var a=t[n],s=ou(a),u=-1,c=s.length;++u<c;){var l=s[u],f=e[l];(f===o||ds(f,st[l])&&!lt.call(e,l))&&(e[l]=a[l])}return e}),Js=Ei(function(e){return e.push(o,ko),zt(su,o,e)});function Zs(e,t,n){var r=null==e?o:Gr(e,t);return r===o?n:r}function eu(e,t){return null!=e&&Uo(e,t,ni)}var tu=go(function(e,t,n){null!=t&&"function"!=typeof t.toString&&(t=dt.call(t)),e[t]=n},Su(Du)),nu=go(function(e,t,n){null!=t&&"function"!=typeof t.toString&&(t=dt.call(t)),lt.call(e,t)?e[t].push(n):e[t]=[n]},Ro),ru=Ei(ii);function iu(e){return _s(e)?Er(e):li(e)}function ou(e){return _s(e)?Er(e,!0):fi(e)}var au=ao(function(e,t,n){gi(e,t,n)}),su=ao(function(e,t,n,r){gi(e,t,n,r)}),uu=Io(function(e,t){var n={};if(null==e)return n;var r=!1;t=Zt(t,function(t){return t=Ki(t,e),r||(r=t.length>1),t}),io(e,jo(e),n),r&&(n=Pr(n,p|d|h,Oo));for(var i=t.length;i--;)Hi(n,t[i]);return n});var cu=Io(function(e,t){return null==e?{}:function(e,t){return _i(e,t,function(t,n){return eu(e,n)})}(e,t)});function lu(e,t){if(null==e)return{};var n=Zt(jo(e),function(e){return[e]});return t=Ro(t),_i(e,n,function(e,n){return t(e,n[0])})}var fu=To(iu),pu=To(ou);function du(e){return null==e?[]:yn(e,iu(e))}var hu=lo(function(e,t,n){return t=t.toLowerCase(),e+(n?vu(t):t)});function vu(e){return Cu(zs(e).toLowerCase())}function gu(e){return(e=zs(e))&&e.replace(Ye,xn).replace(_t,"")}var mu=lo(function(e,t,n){return e+(n?"-":"")+t.toLowerCase()}),yu=lo(function(e,t,n){return e+(n?" ":"")+t.toLowerCase()}),_u=co("toLowerCase");var bu=lo(function(e,t,n){return e+(n?"_":"")+t.toLowerCase()});var wu=lo(function(e,t,n){return e+(n?" ":"")+Cu(t)});var xu=lo(function(e,t,n){return e+(n?" ":"")+t.toUpperCase()}),Cu=co("toUpperCase");function Eu(e,t,n){return e=zs(e),(t=n?o:t)===o?function(e){return Ct.test(e)}(e)?function(e){return e.match(wt)||[]}(e):function(e){return e.match(Fe)||[]}(e):e.match(t)||[]}var Tu=Ei(function(e,t){try{return zt(e,o,t)}catch(e){return Cs(e)?e:new Je(e)}}),Au=Io(function(e,t){return Kt(t,function(t){t=la(t),jr(e,t,ns(e[t],e))}),e});function Su(e){return function(){return e}}var ku=ho(),Ou=ho(!0);function Du(e){return e}function Iu(e){return ci("function"==typeof e?e:Pr(e,p))}var Nu=Ei(function(e,t){return function(n){return ii(n,e,t)}}),ju=Ei(function(e,t){return function(n){return ii(e,n,t)}});function Lu(e,t,n){var r=iu(t),i=Xr(t,r);null!=n||Ss(t)&&(i.length||!r.length)||(n=t,t=e,e=this,i=Xr(t,iu(t)));var o=!(Ss(n)&&"chain"in n&&!n.chain),a=Es(e);return Kt(i,function(n){var r=t[n];e[n]=r,a&&(e.prototype[n]=function(){var t=this.__chain__;if(o||t){var n=e(this.__wrapped__);return(n.__actions__=ro(this.__actions__)).push({func:r,args:arguments,thisArg:e}),n.__chain__=t,n}return r.apply(e,en([this.value()],arguments))})}),e}function $u(){}var Pu=yo(Zt),Ru=yo(Yt),Mu=yo(rn);function Hu(e){return Yo(e)?pn(la(e)):function(e){return function(t){return Gr(t,e)}}(e)}var Fu=bo(),qu=bo(!0);function Bu(){return[]}function Wu(){return!1}var Uu=mo(function(e,t){return e+t},0),zu=Co("ceil"),Vu=mo(function(e,t){return e/t},1),Ku=Co("floor");var Qu,Yu=mo(function(e,t){return e*t},1),Xu=Co("round"),Gu=mo(function(e,t){return e-t},0);return hr.after=function(e,t){if("function"!=typeof t)throw new it(u);return e=qs(e),function(){if(--e<1)return t.apply(this,arguments)}},hr.ary=es,hr.assign=Vs,hr.assignIn=Ks,hr.assignInWith=Qs,hr.assignWith=Ys,hr.at=Xs,hr.before=ts,hr.bind=ns,hr.bindAll=Au,hr.bindKey=rs,hr.castArray=function(){if(!arguments.length)return[];var e=arguments[0];return ms(e)?e:[e]},hr.chain=Ha,hr.chunk=function(e,t,n){t=(n?Qo(e,t,n):t===o)?1:Vn(qs(t),0);var i=null==e?0:e.length;if(!i||t<1)return[];for(var a=0,s=0,u=r(Hn(i/t));a<i;)u[s++]=Ii(e,a,a+=t);return u},hr.compact=function(e){for(var t=-1,n=null==e?0:e.length,r=0,i=[];++t<n;){var o=e[t];o&&(i[r++]=o)}return i},hr.concat=function(){var e=arguments.length;if(!e)return[];for(var t=r(e-1),n=arguments[0],i=e;i--;)t[i-1]=arguments[i];return en(ms(n)?ro(n):[n],zr(t,1))},hr.cond=function(e){var t=null==e?0:e.length,n=Ro();return e=t?Zt(e,function(e){if("function"!=typeof e[1])throw new it(u);return[n(e[0]),e[1]]}):[],Ei(function(n){for(var r=-1;++r<t;){var i=e[r];if(zt(i[0],this,n))return zt(i[1],this,n)}})},hr.conforms=function(e){return function(e){var t=iu(e);return function(n){return Rr(n,e,t)}}(Pr(e,p))},hr.constant=Su,hr.countBy=Ba,hr.create=function(e,t){var n=vr(e);return null==t?n:Nr(n,t)},hr.curry=function e(t,n,r){var i=Ao(t,b,o,o,o,o,o,n=r?o:n);return i.placeholder=e.placeholder,i},hr.curryRight=function e(t,n,r){var i=Ao(t,w,o,o,o,o,o,n=r?o:n);return i.placeholder=e.placeholder,i},hr.debounce=is,hr.defaults=Gs,hr.defaultsDeep=Js,hr.defer=os,hr.delay=as,hr.difference=da,hr.differenceBy=ha,hr.differenceWith=va,hr.drop=function(e,t,n){var r=null==e?0:e.length;return r?Ii(e,(t=n||t===o?1:qs(t))<0?0:t,r):[]},hr.dropRight=function(e,t,n){var r=null==e?0:e.length;return r?Ii(e,0,(t=r-(t=n||t===o?1:qs(t)))<0?0:t):[]},hr.dropRightWhile=function(e,t){return e&&e.length?qi(e,Ro(t,3),!0,!0):[]},hr.dropWhile=function(e,t){return e&&e.length?qi(e,Ro(t,3),!0):[]},hr.fill=function(e,t,n,r){var i=null==e?0:e.length;return i?(n&&"number"!=typeof n&&Qo(e,t,n)&&(n=0,r=i),function(e,t,n,r){var i=e.length;for((n=qs(n))<0&&(n=-n>i?0:i+n),(r=r===o||r>i?i:qs(r))<0&&(r+=i),r=n>r?0:Bs(r);n<r;)e[n++]=t;return e}(e,t,n,r)):[]},hr.filter=function(e,t){return(ms(e)?Xt:Ur)(e,Ro(t,3))},hr.flatMap=function(e,t){return zr(Xa(e,t),1)},hr.flatMapDeep=function(e,t){return zr(Xa(e,t),j)},hr.flatMapDepth=function(e,t,n){return n=n===o?1:qs(n),zr(Xa(e,t),n)},hr.flatten=ya,hr.flattenDeep=function(e){return null!=e&&e.length?zr(e,j):[]},hr.flattenDepth=function(e,t){return null!=e&&e.length?zr(e,t=t===o?1:qs(t)):[]},hr.flip=function(e){return Ao(e,A)},hr.flow=ku,hr.flowRight=Ou,hr.fromPairs=function(e){for(var t=-1,n=null==e?0:e.length,r={};++t<n;){var i=e[t];r[i[0]]=i[1]}return r},hr.functions=function(e){return null==e?[]:Xr(e,iu(e))},hr.functionsIn=function(e){return null==e?[]:Xr(e,ou(e))},hr.groupBy=Ka,hr.initial=function(e){return null!=e&&e.length?Ii(e,0,-1):[]},hr.intersection=ba,hr.intersectionBy=wa,hr.intersectionWith=xa,hr.invert=tu,hr.invertBy=nu,hr.invokeMap=Qa,hr.iteratee=Iu,hr.keyBy=Ya,hr.keys=iu,hr.keysIn=ou,hr.map=Xa,hr.mapKeys=function(e,t){var n={};return t=Ro(t,3),Qr(e,function(e,r,i){jr(n,t(e,r,i),e)}),n},hr.mapValues=function(e,t){var n={};return t=Ro(t,3),Qr(e,function(e,r,i){jr(n,r,t(e,r,i))}),n},hr.matches=function(e){return hi(Pr(e,p))},hr.matchesProperty=function(e,t){return vi(e,Pr(t,p))},hr.memoize=ss,hr.merge=au,hr.mergeWith=su,hr.method=Nu,hr.methodOf=ju,hr.mixin=Lu,hr.negate=us,hr.nthArg=function(e){return e=qs(e),Ei(function(t){return mi(t,e)})},hr.omit=uu,hr.omitBy=function(e,t){return lu(e,us(Ro(t)))},hr.once=function(e){return ts(2,e)},hr.orderBy=function(e,t,n,r){return null==e?[]:(ms(t)||(t=null==t?[]:[t]),ms(n=r?o:n)||(n=null==n?[]:[n]),yi(e,t,n))},hr.over=Pu,hr.overArgs=cs,hr.overEvery=Ru,hr.overSome=Mu,hr.partial=ls,hr.partialRight=fs,hr.partition=Ga,hr.pick=cu,hr.pickBy=lu,hr.property=Hu,hr.propertyOf=function(e){return function(t){return null==e?o:Gr(e,t)}},hr.pull=Ea,hr.pullAll=Ta,hr.pullAllBy=function(e,t,n){return e&&e.length&&t&&t.length?bi(e,t,Ro(n,2)):e},hr.pullAllWith=function(e,t,n){return e&&e.length&&t&&t.length?bi(e,t,o,n):e},hr.pullAt=Aa,hr.range=Fu,hr.rangeRight=qu,hr.rearg=ps,hr.reject=function(e,t){return(ms(e)?Xt:Ur)(e,us(Ro(t,3)))},hr.remove=function(e,t){var n=[];if(!e||!e.length)return n;var r=-1,i=[],o=e.length;for(t=Ro(t,3);++r<o;){var a=e[r];t(a,r,e)&&(n.push(a),i.push(r))}return wi(e,i),n},hr.rest=function(e,t){if("function"!=typeof e)throw new it(u);return Ei(e,t=t===o?t:qs(t))},hr.reverse=Sa,hr.sampleSize=function(e,t,n){return t=(n?Qo(e,t,n):t===o)?1:qs(t),(ms(e)?Ar:Ai)(e,t)},hr.set=function(e,t,n){return null==e?e:Si(e,t,n)},hr.setWith=function(e,t,n,r){return r="function"==typeof r?r:o,null==e?e:Si(e,t,n,r)},hr.shuffle=function(e){return(ms(e)?Sr:Di)(e)},hr.slice=function(e,t,n){var r=null==e?0:e.length;return r?(n&&"number"!=typeof n&&Qo(e,t,n)?(t=0,n=r):(t=null==t?0:qs(t),n=n===o?r:qs(n)),Ii(e,t,n)):[]},hr.sortBy=Ja,hr.sortedUniq=function(e){return e&&e.length?$i(e):[]},hr.sortedUniqBy=function(e,t){return e&&e.length?$i(e,Ro(t,2)):[]},hr.split=function(e,t,n){return n&&"number"!=typeof n&&Qo(e,t,n)&&(t=n=o),(n=n===o?R:n>>>0)?(e=zs(e))&&("string"==typeof t||null!=t&&!Ns(t))&&!(t=Ri(t))&&Tn(e)?Yi(jn(e),0,n):e.split(t,n):[]},hr.spread=function(e,t){if("function"!=typeof e)throw new it(u);return t=null==t?0:Vn(qs(t),0),Ei(function(n){var r=n[t],i=Yi(n,0,t);return r&&en(i,r),zt(e,this,i)})},hr.tail=function(e){var t=null==e?0:e.length;return t?Ii(e,1,t):[]},hr.take=function(e,t,n){return e&&e.length?Ii(e,0,(t=n||t===o?1:qs(t))<0?0:t):[]},hr.takeRight=function(e,t,n){var r=null==e?0:e.length;return r?Ii(e,(t=r-(t=n||t===o?1:qs(t)))<0?0:t,r):[]},hr.takeRightWhile=function(e,t){return e&&e.length?qi(e,Ro(t,3),!1,!0):[]},hr.takeWhile=function(e,t){return e&&e.length?qi(e,Ro(t,3)):[]},hr.tap=function(e,t){return t(e),e},hr.throttle=function(e,t,n){var r=!0,i=!0;if("function"!=typeof e)throw new it(u);return Ss(n)&&(r="leading"in n?!!n.leading:r,i="trailing"in n?!!n.trailing:i),is(e,t,{leading:r,maxWait:t,trailing:i})},hr.thru=Fa,hr.toArray=Hs,hr.toPairs=fu,hr.toPairsIn=pu,hr.toPath=function(e){return ms(e)?Zt(e,la):$s(e)?[e]:ro(ca(zs(e)))},hr.toPlainObject=Us,hr.transform=function(e,t,n){var r=ms(e),i=r||ws(e)||Ps(e);if(t=Ro(t,4),null==n){var o=e&&e.constructor;n=i?r?new o:[]:Ss(e)&&Es(o)?vr(It(e)):{}}return(i?Kt:Qr)(e,function(e,r,i){return t(n,e,r,i)}),n},hr.unary=function(e){return es(e,1)},hr.union=ka,hr.unionBy=Oa,hr.unionWith=Da,hr.uniq=function(e){return e&&e.length?Mi(e):[]},hr.uniqBy=function(e,t){return e&&e.length?Mi(e,Ro(t,2)):[]},hr.uniqWith=function(e,t){return t="function"==typeof t?t:o,e&&e.length?Mi(e,o,t):[]},hr.unset=function(e,t){return null==e||Hi(e,t)},hr.unzip=Ia,hr.unzipWith=Na,hr.update=function(e,t,n){return null==e?e:Fi(e,t,Vi(n))},hr.updateWith=function(e,t,n,r){return r="function"==typeof r?r:o,null==e?e:Fi(e,t,Vi(n),r)},hr.values=du,hr.valuesIn=function(e){return null==e?[]:yn(e,ou(e))},hr.without=ja,hr.words=Eu,hr.wrap=function(e,t){return ls(Vi(t),e)},hr.xor=La,hr.xorBy=$a,hr.xorWith=Pa,hr.zip=Ra,hr.zipObject=function(e,t){return Ui(e||[],t||[],Or)},hr.zipObjectDeep=function(e,t){return Ui(e||[],t||[],Si)},hr.zipWith=Ma,hr.entries=fu,hr.entriesIn=pu,hr.extend=Ks,hr.extendWith=Qs,Lu(hr,hr),hr.add=Uu,hr.attempt=Tu,hr.camelCase=hu,hr.capitalize=vu,hr.ceil=zu,hr.clamp=function(e,t,n){return n===o&&(n=t,t=o),n!==o&&(n=(n=Ws(n))==n?n:0),t!==o&&(t=(t=Ws(t))==t?t:0),$r(Ws(e),t,n)},hr.clone=function(e){return Pr(e,h)},hr.cloneDeep=function(e){return Pr(e,p|h)},hr.cloneDeepWith=function(e,t){return Pr(e,p|h,t="function"==typeof t?t:o)},hr.cloneWith=function(e,t){return Pr(e,h,t="function"==typeof t?t:o)},hr.conformsTo=function(e,t){return null==t||Rr(e,t,iu(t))},hr.deburr=gu,hr.defaultTo=function(e,t){return null==e||e!=e?t:e},hr.divide=Vu,hr.endsWith=function(e,t,n){e=zs(e),t=Ri(t);var r=e.length,i=n=n===o?r:$r(qs(n),0,r);return(n-=t.length)>=0&&e.slice(n,i)==t},hr.eq=ds,hr.escape=function(e){return(e=zs(e))&&Te.test(e)?e.replace(Ce,Cn):e},hr.escapeRegExp=function(e){return(e=zs(e))&&je.test(e)?e.replace(Ne,"\\$&"):e},hr.every=function(e,t,n){var r=ms(e)?Yt:Br;return n&&Qo(e,t,n)&&(t=o),r(e,Ro(t,3))},hr.find=Wa,hr.findIndex=ga,hr.findKey=function(e,t){return an(e,Ro(t,3),Qr)},hr.findLast=Ua,hr.findLastIndex=ma,hr.findLastKey=function(e,t){return an(e,Ro(t,3),Yr)},hr.floor=Ku,hr.forEach=za,hr.forEachRight=Va,hr.forIn=function(e,t){return null==e?e:Vr(e,Ro(t,3),ou)},hr.forInRight=function(e,t){return null==e?e:Kr(e,Ro(t,3),ou)},hr.forOwn=function(e,t){return e&&Qr(e,Ro(t,3))},hr.forOwnRight=function(e,t){return e&&Yr(e,Ro(t,3))},hr.get=Zs,hr.gt=hs,hr.gte=vs,hr.has=function(e,t){return null!=e&&Uo(e,t,ti)},hr.hasIn=eu,hr.head=_a,hr.identity=Du,hr.includes=function(e,t,n,r){e=_s(e)?e:du(e),n=n&&!r?qs(n):0;var i=e.length;return n<0&&(n=Vn(i+n,0)),Ls(e)?n<=i&&e.indexOf(t,n)>-1:!!i&&un(e,t,n)>-1},hr.indexOf=function(e,t,n){var r=null==e?0:e.length;if(!r)return-1;var i=null==n?0:qs(n);return i<0&&(i=Vn(r+i,0)),un(e,t,i)},hr.inRange=function(e,t,n){return t=Fs(t),n===o?(n=t,t=0):n=Fs(n),function(e,t,n){return e>=Kn(t,n)&&e<Vn(t,n)}(e=Ws(e),t,n)},hr.invoke=ru,hr.isArguments=gs,hr.isArray=ms,hr.isArrayBuffer=ys,hr.isArrayLike=_s,hr.isArrayLikeObject=bs,hr.isBoolean=function(e){return!0===e||!1===e||ks(e)&&Zr(e)==U},hr.isBuffer=ws,hr.isDate=xs,hr.isElement=function(e){return ks(e)&&1===e.nodeType&&!Is(e)},hr.isEmpty=function(e){if(null==e)return!0;if(_s(e)&&(ms(e)||"string"==typeof e||"function"==typeof e.splice||ws(e)||Ps(e)||gs(e)))return!e.length;var t=Wo(e);if(t==X||t==ne)return!e.size;if(Jo(e))return!li(e).length;for(var n in e)if(lt.call(e,n))return!1;return!0},hr.isEqual=function(e,t){return ai(e,t)},hr.isEqualWith=function(e,t,n){var r=(n="function"==typeof n?n:o)?n(e,t):o;return r===o?ai(e,t,o,n):!!r},hr.isError=Cs,hr.isFinite=function(e){return"number"==typeof e&&Wn(e)},hr.isFunction=Es,hr.isInteger=Ts,hr.isLength=As,hr.isMap=Os,hr.isMatch=function(e,t){return e===t||si(e,t,Ho(t))},hr.isMatchWith=function(e,t,n){return n="function"==typeof n?n:o,si(e,t,Ho(t),n)},hr.isNaN=function(e){return Ds(e)&&e!=+e},hr.isNative=function(e){if(Go(e))throw new Je(s);return ui(e)},hr.isNil=function(e){return null==e},hr.isNull=function(e){return null===e},hr.isNumber=Ds,hr.isObject=Ss,hr.isObjectLike=ks,hr.isPlainObject=Is,hr.isRegExp=Ns,hr.isSafeInteger=function(e){return Ts(e)&&e>=-L&&e<=L},hr.isSet=js,hr.isString=Ls,hr.isSymbol=$s,hr.isTypedArray=Ps,hr.isUndefined=function(e){return e===o},hr.isWeakMap=function(e){return ks(e)&&Wo(e)==ae},hr.isWeakSet=function(e){return ks(e)&&Zr(e)==se},hr.join=function(e,t){return null==e?"":Un.call(e,t)},hr.kebabCase=mu,hr.last=Ca,hr.lastIndexOf=function(e,t,n){var r=null==e?0:e.length;if(!r)return-1;var i=r;return n!==o&&(i=(i=qs(n))<0?Vn(r+i,0):Kn(i,r-1)),t==t?function(e,t,n){for(var r=n+1;r--;)if(e[r]===t)return r;return r}(e,t,i):sn(e,ln,i,!0)},hr.lowerCase=yu,hr.lowerFirst=_u,hr.lt=Rs,hr.lte=Ms,hr.max=function(e){return e&&e.length?Wr(e,Du,ei):o},hr.maxBy=function(e,t){return e&&e.length?Wr(e,Ro(t,2),ei):o},hr.mean=function(e){return fn(e,Du)},hr.meanBy=function(e,t){return fn(e,Ro(t,2))},hr.min=function(e){return e&&e.length?Wr(e,Du,pi):o},hr.minBy=function(e,t){return e&&e.length?Wr(e,Ro(t,2),pi):o},hr.stubArray=Bu,hr.stubFalse=Wu,hr.stubObject=function(){return{}},hr.stubString=function(){return""},hr.stubTrue=function(){return!0},hr.multiply=Yu,hr.nth=function(e,t){return e&&e.length?mi(e,qs(t)):o},hr.noConflict=function(){return jt._===this&&(jt._=vt),this},hr.noop=$u,hr.now=Za,hr.pad=function(e,t,n){e=zs(e);var r=(t=qs(t))?Nn(e):0;if(!t||r>=t)return e;var i=(t-r)/2;return _o(Fn(i),n)+e+_o(Hn(i),n)},hr.padEnd=function(e,t,n){e=zs(e);var r=(t=qs(t))?Nn(e):0;return t&&r<t?e+_o(t-r,n):e},hr.padStart=function(e,t,n){e=zs(e);var r=(t=qs(t))?Nn(e):0;return t&&r<t?_o(t-r,n)+e:e},hr.parseInt=function(e,t,n){return n||null==t?t=0:t&&(t=+t),Yn(zs(e).replace($e,""),t||0)},hr.random=function(e,t,n){if(n&&"boolean"!=typeof n&&Qo(e,t,n)&&(t=n=o),n===o&&("boolean"==typeof t?(n=t,t=o):"boolean"==typeof e&&(n=e,e=o)),e===o&&t===o?(e=0,t=1):(e=Fs(e),t===o?(t=e,e=0):t=Fs(t)),e>t){var r=e;e=t,t=r}if(n||e%1||t%1){var i=Xn();return Kn(e+i*(t-e+Ot("1e-"+((i+"").length-1))),t)}return xi(e,t)},hr.reduce=function(e,t,n){var r=ms(e)?tn:hn,i=arguments.length<3;return r(e,Ro(t,4),n,i,Fr)},hr.reduceRight=function(e,t,n){var r=ms(e)?nn:hn,i=arguments.length<3;return r(e,Ro(t,4),n,i,qr)},hr.repeat=function(e,t,n){return t=(n?Qo(e,t,n):t===o)?1:qs(t),Ci(zs(e),t)},hr.replace=function(){var e=arguments,t=zs(e[0]);return e.length<3?t:t.replace(e[1],e[2])},hr.result=function(e,t,n){var r=-1,i=(t=Ki(t,e)).length;for(i||(i=1,e=o);++r<i;){var a=null==e?o:e[la(t[r])];a===o&&(r=i,a=n),e=Es(a)?a.call(e):a}return e},hr.round=Xu,hr.runInContext=e,hr.sample=function(e){return(ms(e)?Tr:Ti)(e)},hr.size=function(e){if(null==e)return 0;if(_s(e))return Ls(e)?Nn(e):e.length;var t=Wo(e);return t==X||t==ne?e.size:li(e).length},hr.snakeCase=bu,hr.some=function(e,t,n){var r=ms(e)?rn:Ni;return n&&Qo(e,t,n)&&(t=o),r(e,Ro(t,3))},hr.sortedIndex=function(e,t){return ji(e,t)},hr.sortedIndexBy=function(e,t,n){return Li(e,t,Ro(n,2))},hr.sortedIndexOf=function(e,t){var n=null==e?0:e.length;if(n){var r=ji(e,t);if(r<n&&ds(e[r],t))return r}return-1},hr.sortedLastIndex=function(e,t){return ji(e,t,!0)},hr.sortedLastIndexBy=function(e,t,n){return Li(e,t,Ro(n,2),!0)},hr.sortedLastIndexOf=function(e,t){if(null!=e&&e.length){var n=ji(e,t,!0)-1;if(ds(e[n],t))return n}return-1},hr.startCase=wu,hr.startsWith=function(e,t,n){return e=zs(e),n=null==n?0:$r(qs(n),0,e.length),t=Ri(t),e.slice(n,n+t.length)==t},hr.subtract=Gu,hr.sum=function(e){return e&&e.length?vn(e,Du):0},hr.sumBy=function(e,t){return e&&e.length?vn(e,Ro(t,2)):0},hr.template=function(e,t,n){var r=hr.templateSettings;n&&Qo(e,t,n)&&(t=o),e=zs(e),t=Qs({},t,r,So);var i,a,s=Qs({},t.imports,r.imports,So),u=iu(s),c=yn(s,u),l=0,f=t.interpolate||Xe,p="__p += '",d=nt((t.escape||Xe).source+"|"+f.source+"|"+(f===ke?Be:Xe).source+"|"+(t.evaluate||Xe).source+"|$","g"),h="//# sourceURL="+("sourceURL"in t?t.sourceURL:"lodash.templateSources["+ ++Tt+"]")+"\n";e.replace(d,function(t,n,r,o,s,u){return r||(r=o),p+=e.slice(l,u).replace(Ge,En),n&&(i=!0,p+="' +\n__e("+n+") +\n'"),s&&(a=!0,p+="';\n"+s+";\n__p += '"),r&&(p+="' +\n((__t = ("+r+")) == null ? '' : __t) +\n'"),l=u+t.length,t}),p+="';\n";var v=t.variable;v||(p="with (obj) {\n"+p+"\n}\n"),p=(a?p.replace(_e,""):p).replace(be,"$1").replace(we,"$1;"),p="function("+(v||"obj")+") {\n"+(v?"":"obj || (obj = {});\n")+"var __t, __p = ''"+(i?", __e = _.escape":"")+(a?", __j = Array.prototype.join;\nfunction print() { __p += __j.call(arguments, '') }\n":";\n")+p+"return __p\n}";var g=Tu(function(){return Ze(u,h+"return "+p).apply(o,c)});if(g.source=p,Cs(g))throw g;return g},hr.times=function(e,t){if((e=qs(e))<1||e>L)return[];var n=R,r=Kn(e,R);t=Ro(t),e-=R;for(var i=gn(r,t);++n<e;)t(n);return i},hr.toFinite=Fs,hr.toInteger=qs,hr.toLength=Bs,hr.toLower=function(e){return zs(e).toLowerCase()},hr.toNumber=Ws,hr.toSafeInteger=function(e){return e?$r(qs(e),-L,L):0===e?e:0},hr.toString=zs,hr.toUpper=function(e){return zs(e).toUpperCase()},hr.trim=function(e,t,n){if((e=zs(e))&&(n||t===o))return e.replace(Le,"");if(!e||!(t=Ri(t)))return e;var r=jn(e),i=jn(t);return Yi(r,bn(r,i),wn(r,i)+1).join("")},hr.trimEnd=function(e,t,n){if((e=zs(e))&&(n||t===o))return e.replace(Pe,"");if(!e||!(t=Ri(t)))return e;var r=jn(e);return Yi(r,0,wn(r,jn(t))+1).join("")},hr.trimStart=function(e,t,n){if((e=zs(e))&&(n||t===o))return e.replace($e,"");if(!e||!(t=Ri(t)))return e;var r=jn(e);return Yi(r,bn(r,jn(t))).join("")},hr.truncate=function(e,t){var n=S,r=k;if(Ss(t)){var i="separator"in t?t.separator:i;n="length"in t?qs(t.length):n,r="omission"in t?Ri(t.omission):r}var a=(e=zs(e)).length;if(Tn(e)){var s=jn(e);a=s.length}if(n>=a)return e;var u=n-Nn(r);if(u<1)return r;var c=s?Yi(s,0,u).join(""):e.slice(0,u);if(i===o)return c+r;if(s&&(u+=c.length-u),Ns(i)){if(e.slice(u).search(i)){var l,f=c;for(i.global||(i=nt(i.source,zs(We.exec(i))+"g")),i.lastIndex=0;l=i.exec(f);)var p=l.index;c=c.slice(0,p===o?u:p)}}else if(e.indexOf(Ri(i),u)!=u){var d=c.lastIndexOf(i);d>-1&&(c=c.slice(0,d))}return c+r},hr.unescape=function(e){return(e=zs(e))&&Ee.test(e)?e.replace(xe,Ln):e},hr.uniqueId=function(e){var t=++ft;return zs(e)+t},hr.upperCase=xu,hr.upperFirst=Cu,hr.each=za,hr.eachRight=Va,hr.first=_a,Lu(hr,(Qu={},Qr(hr,function(e,t){lt.call(hr.prototype,t)||(Qu[t]=e)}),Qu),{chain:!1}),hr.VERSION="4.17.10",Kt(["bind","bindKey","curry","curryRight","partial","partialRight"],function(e){hr[e].placeholder=hr}),Kt(["drop","take"],function(e,t){yr.prototype[e]=function(n){n=n===o?1:Vn(qs(n),0);var r=this.__filtered__&&!t?new yr(this):this.clone();return r.__filtered__?r.__takeCount__=Kn(n,r.__takeCount__):r.__views__.push({size:Kn(n,R),type:e+(r.__dir__<0?"Right":"")}),r},yr.prototype[e+"Right"]=function(t){return this.reverse()[e](t).reverse()}}),Kt(["filter","map","takeWhile"],function(e,t){var n=t+1,r=n==I||3==n;yr.prototype[e]=function(e){var t=this.clone();return t.__iteratees__.push({iteratee:Ro(e,3),type:n}),t.__filtered__=t.__filtered__||r,t}}),Kt(["head","last"],function(e,t){var n="take"+(t?"Right":"");yr.prototype[e]=function(){return this[n](1).value()[0]}}),Kt(["initial","tail"],function(e,t){var n="drop"+(t?"":"Right");yr.prototype[e]=function(){return this.__filtered__?new yr(this):this[n](1)}}),yr.prototype.compact=function(){return this.filter(Du)},yr.prototype.find=function(e){return this.filter(e).head()},yr.prototype.findLast=function(e){return this.reverse().find(e)},yr.prototype.invokeMap=Ei(function(e,t){return"function"==typeof e?new yr(this):this.map(function(n){return ii(n,e,t)})}),yr.prototype.reject=function(e){return this.filter(us(Ro(e)))},yr.prototype.slice=function(e,t){e=qs(e);var n=this;return n.__filtered__&&(e>0||t<0)?new yr(n):(e<0?n=n.takeRight(-e):e&&(n=n.drop(e)),t!==o&&(n=(t=qs(t))<0?n.dropRight(-t):n.take(t-e)),n)},yr.prototype.takeRightWhile=function(e){return this.reverse().takeWhile(e).reverse()},yr.prototype.toArray=function(){return this.take(R)},Qr(yr.prototype,function(e,t){var n=/^(?:filter|find|map|reject)|While$/.test(t),r=/^(?:head|last)$/.test(t),i=hr[r?"take"+("last"==t?"Right":""):t],a=r||/^find/.test(t);i&&(hr.prototype[t]=function(){var t=this.__wrapped__,s=r?[1]:arguments,u=t instanceof yr,c=s[0],l=u||ms(t),f=function(e){var t=i.apply(hr,en([e],s));return r&&p?t[0]:t};l&&n&&"function"==typeof c&&1!=c.length&&(u=l=!1);var p=this.__chain__,d=!!this.__actions__.length,h=a&&!p,v=u&&!d;if(!a&&l){t=v?t:new yr(this);var g=e.apply(t,s);return g.__actions__.push({func:Fa,args:[f],thisArg:o}),new mr(g,p)}return h&&v?e.apply(this,s):(g=this.thru(f),h?r?g.value()[0]:g.value():g)})}),Kt(["pop","push","shift","sort","splice","unshift"],function(e){var t=ot[e],n=/^(?:push|sort|unshift)$/.test(e)?"tap":"thru",r=/^(?:pop|shift)$/.test(e);hr.prototype[e]=function(){var e=arguments;if(r&&!this.__chain__){var i=this.value();return t.apply(ms(i)?i:[],e)}return this[n](function(n){return t.apply(ms(n)?n:[],e)})}}),Qr(yr.prototype,function(e,t){var n=hr[t];if(n){var r=n.name+"";(or[r]||(or[r]=[])).push({name:t,func:n})}}),or[vo(o,y).name]=[{name:"wrapper",func:o}],yr.prototype.clone=function(){var e=new yr(this.__wrapped__);return e.__actions__=ro(this.__actions__),e.__dir__=this.__dir__,e.__filtered__=this.__filtered__,e.__iteratees__=ro(this.__iteratees__),e.__takeCount__=this.__takeCount__,e.__views__=ro(this.__views__),e},yr.prototype.reverse=function(){if(this.__filtered__){var e=new yr(this);e.__dir__=-1,e.__filtered__=!0}else(e=this.clone()).__dir__*=-1;return e},yr.prototype.value=function(){var e=this.__wrapped__.value(),t=this.__dir__,n=ms(e),r=t<0,i=n?e.length:0,o=function(e,t,n){for(var r=-1,i=n.length;++r<i;){var o=n[r],a=o.size;switch(o.type){case"drop":e+=a;break;case"dropRight":t-=a;break;case"take":t=Kn(t,e+a);break;case"takeRight":e=Vn(e,t-a)}}return{start:e,end:t}}(0,i,this.__views__),a=o.start,s=o.end,u=s-a,c=r?s:a-1,l=this.__iteratees__,f=l.length,p=0,d=Kn(u,this.__takeCount__);if(!n||!r&&i==u&&d==u)return Bi(e,this.__actions__);var h=[];e:for(;u--&&p<d;){for(var v=-1,g=e[c+=t];++v<f;){var m=l[v],y=m.iteratee,_=m.type,b=y(g);if(_==N)g=b;else if(!b){if(_==I)continue e;break e}}h[p++]=g}return h},hr.prototype.at=qa,hr.prototype.chain=function(){return Ha(this)},hr.prototype.commit=function(){return new mr(this.value(),this.__chain__)},hr.prototype.next=function(){this.__values__===o&&(this.__values__=Hs(this.value()));var e=this.__index__>=this.__values__.length;return{done:e,value:e?o:this.__values__[this.__index__++]}},hr.prototype.plant=function(e){for(var t,n=this;n instanceof gr;){var r=pa(n);r.__index__=0,r.__values__=o,t?i.__wrapped__=r:t=r;var i=r;n=n.__wrapped__}return i.__wrapped__=e,t},hr.prototype.reverse=function(){var e=this.__wrapped__;if(e instanceof yr){var t=e;return this.__actions__.length&&(t=new yr(this)),(t=t.reverse()).__actions__.push({func:Fa,args:[Sa],thisArg:o}),new mr(t,this.__chain__)}return this.thru(Sa)},hr.prototype.toJSON=hr.prototype.valueOf=hr.prototype.value=function(){return Bi(this.__wrapped__,this.__actions__)},hr.prototype.first=hr.prototype.head,Mt&&(hr.prototype[Mt]=function(){return this}),hr}();jt._=$n,(i=function(){return $n}.call(t,n,t,r))===o||(r.exports=i)}).call(this)}).call(t,n(1),n(15)(e))},function(e,t){e.exports=function(e){return e.webpackPolyfill||(e.deprecate=function(){},e.paths=[],e.children||(e.children=[]),Object.defineProperty(e,"loaded",{enumerable:!0,get:function(){return e.l}}),Object.defineProperty(e,"id",{enumerable:!0,get:function(){return e.i}}),e.webpackPolyfill=1),e}},function(e,t,n){(function(e,t,n){"use strict";function r(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function i(e,t,n){return t&&r(e.prototype,t),n&&r(e,n),e}function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{},r=Object.keys(n);"function"==typeof Object.getOwnPropertySymbols&&(r=r.concat(Object.getOwnPropertySymbols(n).filter(function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),r.forEach(function(t){o(e,t,n[t])})}return e}t=t&&t.hasOwnProperty("default")?t.default:t,n=n&&n.hasOwnProperty("default")?n.default:n;var s=function(e){var t="transitionend";function n(t){var n=this,i=!1;return e(this).one(r.TRANSITION_END,function(){i=!0}),setTimeout(function(){i||r.triggerTransitionEnd(n)},t),this}var r={TRANSITION_END:"bsTransitionEnd",getUID:function(e){do{e+=~~(1e6*Math.random())}while(document.getElementById(e));return e},getSelectorFromElement:function(e){var t=e.getAttribute("data-target");t&&"#"!==t||(t=e.getAttribute("href")||"");try{return document.querySelector(t)?t:null}catch(e){return null}},getTransitionDurationFromElement:function(t){if(!t)return 0;var n=e(t).css("transition-duration");return parseFloat(n)?(n=n.split(",")[0],1e3*parseFloat(n)):0},reflow:function(e){return e.offsetHeight},triggerTransitionEnd:function(n){e(n).trigger(t)},supportsTransitionEnd:function(){return Boolean(t)},isElement:function(e){return(e[0]||e).nodeType},typeCheckConfig:function(e,t,n){for(var i in n)if(Object.prototype.hasOwnProperty.call(n,i)){var o=n[i],a=t[i],s=a&&r.isElement(a)?"element":(u=a,{}.toString.call(u).match(/\s([a-z]+)/i)[1].toLowerCase());if(!new RegExp(o).test(s))throw new Error(e.toUpperCase()+': Option "'+i+'" provided type "'+s+'" but expected type "'+o+'".')}var u}};return e.fn.emulateTransitionEnd=n,e.event.special[r.TRANSITION_END]={bindType:t,delegateType:t,handle:function(t){if(e(t.target).is(this))return t.handleObj.handler.apply(this,arguments)}},r}(t),u=function(e){var t=e.fn.alert,n={CLOSE:"close.bs.alert",CLOSED:"closed.bs.alert",CLICK_DATA_API:"click.bs.alert.data-api"},r="alert",o="fade",a="show",u=function(){function t(e){this._element=e}var u=t.prototype;return u.close=function(e){var t=this._element;e&&(t=this._getRootElement(e)),this._triggerCloseEvent(t).isDefaultPrevented()||this._removeElement(t)},u.dispose=function(){e.removeData(this._element,"bs.alert"),this._element=null},u._getRootElement=function(t){var n=s.getSelectorFromElement(t),i=!1;return n&&(i=document.querySelector(n)),i||(i=e(t).closest("."+r)[0]),i},u._triggerCloseEvent=function(t){var r=e.Event(n.CLOSE);return e(t).trigger(r),r},u._removeElement=function(t){var n=this;if(e(t).removeClass(a),e(t).hasClass(o)){var r=s.getTransitionDurationFromElement(t);e(t).one(s.TRANSITION_END,function(e){return n._destroyElement(t,e)}).emulateTransitionEnd(r)}else this._destroyElement(t)},u._destroyElement=function(t){e(t).detach().trigger(n.CLOSED).remove()},t._jQueryInterface=function(n){return this.each(function(){var r=e(this),i=r.data("bs.alert");i||(i=new t(this),r.data("bs.alert",i)),"close"===n&&i[n](this)})},t._handleDismiss=function(e){return function(t){t&&t.preventDefault(),e.close(this)}},i(t,null,[{key:"VERSION",get:function(){return"4.1.2"}}]),t}();return e(document).on(n.CLICK_DATA_API,'[data-dismiss="alert"]',u._handleDismiss(new u)),e.fn.alert=u._jQueryInterface,e.fn.alert.Constructor=u,e.fn.alert.noConflict=function(){return e.fn.alert=t,u._jQueryInterface},u}(t),c=function(e){var t="button",n=e.fn[t],r="active",o="btn",a="focus",s='[data-toggle^="button"]',u='[data-toggle="buttons"]',c="input",l=".active",f=".btn",p={CLICK_DATA_API:"click.bs.button.data-api",FOCUS_BLUR_DATA_API:"focus.bs.button.data-api blur.bs.button.data-api"},d=function(){function t(e){this._element=e}var n=t.prototype;return n.toggle=function(){var t=!0,n=!0,i=e(this._element).closest(u)[0];if(i){var o=this._element.querySelector(c);if(o){if("radio"===o.type)if(o.checked&&this._element.classList.contains(r))t=!1;else{var a=i.querySelector(l);a&&e(a).removeClass(r)}if(t){if(o.hasAttribute("disabled")||i.hasAttribute("disabled")||o.classList.contains("disabled")||i.classList.contains("disabled"))return;o.checked=!this._element.classList.contains(r),e(o).trigger("change")}o.focus(),n=!1}}n&&this._element.setAttribute("aria-pressed",!this._element.classList.contains(r)),t&&e(this._element).toggleClass(r)},n.dispose=function(){e.removeData(this._element,"bs.button"),this._element=null},t._jQueryInterface=function(n){return this.each(function(){var r=e(this).data("bs.button");r||(r=new t(this),e(this).data("bs.button",r)),"toggle"===n&&r[n]()})},i(t,null,[{key:"VERSION",get:function(){return"4.1.2"}}]),t}();return e(document).on(p.CLICK_DATA_API,s,function(t){t.preventDefault();var n=t.target;e(n).hasClass(o)||(n=e(n).closest(f)),d._jQueryInterface.call(e(n),"toggle")}).on(p.FOCUS_BLUR_DATA_API,s,function(t){var n=e(t.target).closest(f)[0];e(n).toggleClass(a,/^focus(in)?$/.test(t.type))}),e.fn[t]=d._jQueryInterface,e.fn[t].Constructor=d,e.fn[t].noConflict=function(){return e.fn[t]=n,d._jQueryInterface},d}(t),l=function(e){var t="carousel",n="bs.carousel",r="."+n,o=e.fn[t],u={interval:5e3,keyboard:!0,slide:!1,pause:"hover",wrap:!0},c={interval:"(number|boolean)",keyboard:"boolean",slide:"(boolean|string)",pause:"(string|boolean)",wrap:"boolean"},l="next",f="prev",p="left",d="right",h={SLIDE:"slide"+r,SLID:"slid"+r,KEYDOWN:"keydown"+r,MOUSEENTER:"mouseenter"+r,MOUSELEAVE:"mouseleave"+r,TOUCHEND:"touchend"+r,LOAD_DATA_API:"load.bs.carousel.data-api",CLICK_DATA_API:"click.bs.carousel.data-api"},v="carousel",g="active",m="slide",y="carousel-item-right",_="carousel-item-left",b="carousel-item-next",w="carousel-item-prev",x={ACTIVE:".active",ACTIVE_ITEM:".active.carousel-item",ITEM:".carousel-item",NEXT_PREV:".carousel-item-next, .carousel-item-prev",INDICATORS:".carousel-indicators",DATA_SLIDE:"[data-slide], [data-slide-to]",DATA_RIDE:'[data-ride="carousel"]'},C=function(){function o(t,n){this._items=null,this._interval=null,this._activeElement=null,this._isPaused=!1,this._isSliding=!1,this.touchTimeout=null,this._config=this._getConfig(n),this._element=e(t)[0],this._indicatorsElement=this._element.querySelector(x.INDICATORS),this._addEventListeners()}var C=o.prototype;return C.next=function(){this._isSliding||this._slide(l)},C.nextWhenVisible=function(){!document.hidden&&e(this._element).is(":visible")&&"hidden"!==e(this._element).css("visibility")&&this.next()},C.prev=function(){this._isSliding||this._slide(f)},C.pause=function(e){e||(this._isPaused=!0),this._element.querySelector(x.NEXT_PREV)&&(s.triggerTransitionEnd(this._element),this.cycle(!0)),clearInterval(this._interval),this._interval=null},C.cycle=function(e){e||(this._isPaused=!1),this._interval&&(clearInterval(this._interval),this._interval=null),this._config.interval&&!this._isPaused&&(this._interval=setInterval((document.visibilityState?this.nextWhenVisible:this.next).bind(this),this._config.interval))},C.to=function(t){var n=this;this._activeElement=this._element.querySelector(x.ACTIVE_ITEM);var r=this._getItemIndex(this._activeElement);if(!(t>this._items.length-1||t<0))if(this._isSliding)e(this._element).one(h.SLID,function(){return n.to(t)});else{if(r===t)return this.pause(),void this.cycle();var i=t>r?l:f;this._slide(i,this._items[t])}},C.dispose=function(){e(this._element).off(r),e.removeData(this._element,n),this._items=null,this._config=null,this._element=null,this._interval=null,this._isPaused=null,this._isSliding=null,this._activeElement=null,this._indicatorsElement=null},C._getConfig=function(e){return e=a({},u,e),s.typeCheckConfig(t,e,c),e},C._addEventListeners=function(){var t=this;this._config.keyboard&&e(this._element).on(h.KEYDOWN,function(e){return t._keydown(e)}),"hover"===this._config.pause&&(e(this._element).on(h.MOUSEENTER,function(e){return t.pause(e)}).on(h.MOUSELEAVE,function(e){return t.cycle(e)}),"ontouchstart"in document.documentElement&&e(this._element).on(h.TOUCHEND,function(){t.pause(),t.touchTimeout&&clearTimeout(t.touchTimeout),t.touchTimeout=setTimeout(function(e){return t.cycle(e)},500+t._config.interval)}))},C._keydown=function(e){if(!/input|textarea/i.test(e.target.tagName))switch(e.which){case 37:e.preventDefault(),this.prev();break;case 39:e.preventDefault(),this.next()}},C._getItemIndex=function(e){return this._items=e&&e.parentNode?[].slice.call(e.parentNode.querySelectorAll(x.ITEM)):[],this._items.indexOf(e)},C._getItemByDirection=function(e,t){var n=e===l,r=e===f,i=this._getItemIndex(t),o=this._items.length-1;if((r&&0===i||n&&i===o)&&!this._config.wrap)return t;var a=(i+(e===f?-1:1))%this._items.length;return-1===a?this._items[this._items.length-1]:this._items[a]},C._triggerSlideEvent=function(t,n){var r=this._getItemIndex(t),i=this._getItemIndex(this._element.querySelector(x.ACTIVE_ITEM)),o=e.Event(h.SLIDE,{relatedTarget:t,direction:n,from:i,to:r});return e(this._element).trigger(o),o},C._setActiveIndicatorElement=function(t){if(this._indicatorsElement){var n=[].slice.call(this._indicatorsElement.querySelectorAll(x.ACTIVE));e(n).removeClass(g);var r=this._indicatorsElement.children[this._getItemIndex(t)];r&&e(r).addClass(g)}},C._slide=function(t,n){var r,i,o,a=this,u=this._element.querySelector(x.ACTIVE_ITEM),c=this._getItemIndex(u),f=n||u&&this._getItemByDirection(t,u),v=this._getItemIndex(f),C=Boolean(this._interval);if(t===l?(r=_,i=b,o=p):(r=y,i=w,o=d),f&&e(f).hasClass(g))this._isSliding=!1;else if(!this._triggerSlideEvent(f,o).isDefaultPrevented()&&u&&f){this._isSliding=!0,C&&this.pause(),this._setActiveIndicatorElement(f);var E=e.Event(h.SLID,{relatedTarget:f,direction:o,from:c,to:v});if(e(this._element).hasClass(m)){e(f).addClass(i),s.reflow(f),e(u).addClass(r),e(f).addClass(r);var T=s.getTransitionDurationFromElement(u);e(u).one(s.TRANSITION_END,function(){e(f).removeClass(r+" "+i).addClass(g),e(u).removeClass(g+" "+i+" "+r),a._isSliding=!1,setTimeout(function(){return e(a._element).trigger(E)},0)}).emulateTransitionEnd(T)}else e(u).removeClass(g),e(f).addClass(g),this._isSliding=!1,e(this._element).trigger(E);C&&this.cycle()}},o._jQueryInterface=function(t){return this.each(function(){var r=e(this).data(n),i=a({},u,e(this).data());"object"==typeof t&&(i=a({},i,t));var s="string"==typeof t?t:i.slide;if(r||(r=new o(this,i),e(this).data(n,r)),"number"==typeof t)r.to(t);else if("string"==typeof s){if(void 0===r[s])throw new TypeError('No method named "'+s+'"');r[s]()}else i.interval&&(r.pause(),r.cycle())})},o._dataApiClickHandler=function(t){var r=s.getSelectorFromElement(this);if(r){var i=e(r)[0];if(i&&e(i).hasClass(v)){var u=a({},e(i).data(),e(this).data()),c=this.getAttribute("data-slide-to");c&&(u.interval=!1),o._jQueryInterface.call(e(i),u),c&&e(i).data(n).to(c),t.preventDefault()}}},i(o,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return u}}]),o}();return e(document).on(h.CLICK_DATA_API,x.DATA_SLIDE,C._dataApiClickHandler),e(window).on(h.LOAD_DATA_API,function(){for(var t=[].slice.call(document.querySelectorAll(x.DATA_RIDE)),n=0,r=t.length;n<r;n++){var i=e(t[n]);C._jQueryInterface.call(i,i.data())}}),e.fn[t]=C._jQueryInterface,e.fn[t].Constructor=C,e.fn[t].noConflict=function(){return e.fn[t]=o,C._jQueryInterface},C}(t),f=function(e){var t="collapse",n="bs.collapse",r=e.fn[t],o={toggle:!0,parent:""},u={toggle:"boolean",parent:"(string|element)"},c={SHOW:"show.bs.collapse",SHOWN:"shown.bs.collapse",HIDE:"hide.bs.collapse",HIDDEN:"hidden.bs.collapse",CLICK_DATA_API:"click.bs.collapse.data-api"},l="show",f="collapse",p="collapsing",d="collapsed",h="width",v="height",g={ACTIVES:".show, .collapsing",DATA_TOGGLE:'[data-toggle="collapse"]'},m=function(){function r(t,n){this._isTransitioning=!1,this._element=t,this._config=this._getConfig(n),this._triggerArray=e.makeArray(document.querySelectorAll('[data-toggle="collapse"][href="#'+t.id+'"],[data-toggle="collapse"][data-target="#'+t.id+'"]'));for(var r=[].slice.call(document.querySelectorAll(g.DATA_TOGGLE)),i=0,o=r.length;i<o;i++){var a=r[i],u=s.getSelectorFromElement(a),c=[].slice.call(document.querySelectorAll(u)).filter(function(e){return e===t});null!==u&&c.length>0&&(this._selector=u,this._triggerArray.push(a))}this._parent=this._config.parent?this._getParent():null,this._config.parent||this._addAriaAndCollapsedClass(this._element,this._triggerArray),this._config.toggle&&this.toggle()}var m=r.prototype;return m.toggle=function(){e(this._element).hasClass(l)?this.hide():this.show()},m.show=function(){var t,i,o=this;if(!this._isTransitioning&&!e(this._element).hasClass(l)&&(this._parent&&0===(t=[].slice.call(this._parent.querySelectorAll(g.ACTIVES)).filter(function(e){return e.getAttribute("data-parent")===o._config.parent})).length&&(t=null),!(t&&(i=e(t).not(this._selector).data(n))&&i._isTransitioning))){var a=e.Event(c.SHOW);if(e(this._element).trigger(a),!a.isDefaultPrevented()){t&&(r._jQueryInterface.call(e(t).not(this._selector),"hide"),i||e(t).data(n,null));var u=this._getDimension();e(this._element).removeClass(f).addClass(p),this._element.style[u]=0,this._triggerArray.length&&e(this._triggerArray).removeClass(d).attr("aria-expanded",!0),this.setTransitioning(!0);var h="scroll"+(u[0].toUpperCase()+u.slice(1)),v=s.getTransitionDurationFromElement(this._element);e(this._element).one(s.TRANSITION_END,function(){e(o._element).removeClass(p).addClass(f).addClass(l),o._element.style[u]="",o.setTransitioning(!1),e(o._element).trigger(c.SHOWN)}).emulateTransitionEnd(v),this._element.style[u]=this._element[h]+"px"}}},m.hide=function(){var t=this;if(!this._isTransitioning&&e(this._element).hasClass(l)){var n=e.Event(c.HIDE);if(e(this._element).trigger(n),!n.isDefaultPrevented()){var r=this._getDimension();this._element.style[r]=this._element.getBoundingClientRect()[r]+"px",s.reflow(this._element),e(this._element).addClass(p).removeClass(f).removeClass(l);var i=this._triggerArray.length;if(i>0)for(var o=0;o<i;o++){var a=this._triggerArray[o],u=s.getSelectorFromElement(a);if(null!==u)e([].slice.call(document.querySelectorAll(u))).hasClass(l)||e(a).addClass(d).attr("aria-expanded",!1)}this.setTransitioning(!0);this._element.style[r]="";var h=s.getTransitionDurationFromElement(this._element);e(this._element).one(s.TRANSITION_END,function(){t.setTransitioning(!1),e(t._element).removeClass(p).addClass(f).trigger(c.HIDDEN)}).emulateTransitionEnd(h)}}},m.setTransitioning=function(e){this._isTransitioning=e},m.dispose=function(){e.removeData(this._element,n),this._config=null,this._parent=null,this._element=null,this._triggerArray=null,this._isTransitioning=null},m._getConfig=function(e){return(e=a({},o,e)).toggle=Boolean(e.toggle),s.typeCheckConfig(t,e,u),e},m._getDimension=function(){return e(this._element).hasClass(h)?h:v},m._getParent=function(){var t=this,n=null;s.isElement(this._config.parent)?(n=this._config.parent,void 0!==this._config.parent.jquery&&(n=this._config.parent[0])):n=document.querySelector(this._config.parent);var i='[data-toggle="collapse"][data-parent="'+this._config.parent+'"]',o=[].slice.call(n.querySelectorAll(i));return e(o).each(function(e,n){t._addAriaAndCollapsedClass(r._getTargetFromElement(n),[n])}),n},m._addAriaAndCollapsedClass=function(t,n){if(t){var r=e(t).hasClass(l);n.length&&e(n).toggleClass(d,!r).attr("aria-expanded",r)}},r._getTargetFromElement=function(e){var t=s.getSelectorFromElement(e);return t?document.querySelector(t):null},r._jQueryInterface=function(t){return this.each(function(){var i=e(this),s=i.data(n),u=a({},o,i.data(),"object"==typeof t&&t?t:{});if(!s&&u.toggle&&/show|hide/.test(t)&&(u.toggle=!1),s||(s=new r(this,u),i.data(n,s)),"string"==typeof t){if(void 0===s[t])throw new TypeError('No method named "'+t+'"');s[t]()}})},i(r,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return o}}]),r}();return e(document).on(c.CLICK_DATA_API,g.DATA_TOGGLE,function(t){"A"===t.currentTarget.tagName&&t.preventDefault();var r=e(this),i=s.getSelectorFromElement(this),o=[].slice.call(document.querySelectorAll(i));e(o).each(function(){var t=e(this),i=t.data(n)?"toggle":r.data();m._jQueryInterface.call(t,i)})}),e.fn[t]=m._jQueryInterface,e.fn[t].Constructor=m,e.fn[t].noConflict=function(){return e.fn[t]=r,m._jQueryInterface},m}(t),p=function(e){var t="dropdown",r="bs.dropdown",o="."+r,u=e.fn[t],c=new RegExp("38|40|27"),l={HIDE:"hide"+o,HIDDEN:"hidden"+o,SHOW:"show"+o,SHOWN:"shown"+o,CLICK:"click"+o,CLICK_DATA_API:"click.bs.dropdown.data-api",KEYDOWN_DATA_API:"keydown.bs.dropdown.data-api",KEYUP_DATA_API:"keyup.bs.dropdown.data-api"},f="disabled",p="show",d="dropup",h="dropright",v="dropleft",g="dropdown-menu-right",m="position-static",y='[data-toggle="dropdown"]',_=".dropdown form",b=".dropdown-menu",w=".navbar-nav",x=".dropdown-menu .dropdown-item:not(.disabled):not(:disabled)",C="top-start",E="top-end",T="bottom-start",A="bottom-end",S="right-start",k="left-start",O={offset:0,flip:!0,boundary:"scrollParent",reference:"toggle",display:"dynamic"},D={offset:"(number|string|function)",flip:"boolean",boundary:"(string|element)",reference:"(string|element)",display:"string"},I=function(){function u(e,t){this._element=e,this._popper=null,this._config=this._getConfig(t),this._menu=this._getMenuElement(),this._inNavbar=this._detectNavbar(),this._addEventListeners()}var _=u.prototype;return _.toggle=function(){if(!this._element.disabled&&!e(this._element).hasClass(f)){var t=u._getParentFromElement(this._element),r=e(this._menu).hasClass(p);if(u._clearMenus(),!r){var i={relatedTarget:this._element},o=e.Event(l.SHOW,i);if(e(t).trigger(o),!o.isDefaultPrevented()){if(!this._inNavbar){if(void 0===n)throw new TypeError("Bootstrap dropdown require Popper.js (https://popper.js.org)");var a=this._element;"parent"===this._config.reference?a=t:s.isElement(this._config.reference)&&(a=this._config.reference,void 0!==this._config.reference.jquery&&(a=this._config.reference[0])),"scrollParent"!==this._config.boundary&&e(t).addClass(m),this._popper=new n(a,this._menu,this._getPopperConfig())}"ontouchstart"in document.documentElement&&0===e(t).closest(w).length&&e(document.body).children().on("mouseover",null,e.noop),this._element.focus(),this._element.setAttribute("aria-expanded",!0),e(this._menu).toggleClass(p),e(t).toggleClass(p).trigger(e.Event(l.SHOWN,i))}}}},_.dispose=function(){e.removeData(this._element,r),e(this._element).off(o),this._element=null,this._menu=null,null!==this._popper&&(this._popper.destroy(),this._popper=null)},_.update=function(){this._inNavbar=this._detectNavbar(),null!==this._popper&&this._popper.scheduleUpdate()},_._addEventListeners=function(){var t=this;e(this._element).on(l.CLICK,function(e){e.preventDefault(),e.stopPropagation(),t.toggle()})},_._getConfig=function(n){return n=a({},this.constructor.Default,e(this._element).data(),n),s.typeCheckConfig(t,n,this.constructor.DefaultType),n},_._getMenuElement=function(){if(!this._menu){var e=u._getParentFromElement(this._element);e&&(this._menu=e.querySelector(b))}return this._menu},_._getPlacement=function(){var t=e(this._element.parentNode),n=T;return t.hasClass(d)?(n=C,e(this._menu).hasClass(g)&&(n=E)):t.hasClass(h)?n=S:t.hasClass(v)?n=k:e(this._menu).hasClass(g)&&(n=A),n},_._detectNavbar=function(){return e(this._element).closest(".navbar").length>0},_._getPopperConfig=function(){var e=this,t={};"function"==typeof this._config.offset?t.fn=function(t){return t.offsets=a({},t.offsets,e._config.offset(t.offsets)||{}),t}:t.offset=this._config.offset;var n={placement:this._getPlacement(),modifiers:{offset:t,flip:{enabled:this._config.flip},preventOverflow:{boundariesElement:this._config.boundary}}};return"static"===this._config.display&&(n.modifiers.applyStyle={enabled:!1}),n},u._jQueryInterface=function(t){return this.each(function(){var n=e(this).data(r);if(n||(n=new u(this,"object"==typeof t?t:null),e(this).data(r,n)),"string"==typeof t){if(void 0===n[t])throw new TypeError('No method named "'+t+'"');n[t]()}})},u._clearMenus=function(t){if(!t||3!==t.which&&("keyup"!==t.type||9===t.which))for(var n=[].slice.call(document.querySelectorAll(y)),i=0,o=n.length;i<o;i++){var a=u._getParentFromElement(n[i]),s=e(n[i]).data(r),c={relatedTarget:n[i]};if(t&&"click"===t.type&&(c.clickEvent=t),s){var f=s._menu;if(e(a).hasClass(p)&&!(t&&("click"===t.type&&/input|textarea/i.test(t.target.tagName)||"keyup"===t.type&&9===t.which)&&e.contains(a,t.target))){var d=e.Event(l.HIDE,c);e(a).trigger(d),d.isDefaultPrevented()||("ontouchstart"in document.documentElement&&e(document.body).children().off("mouseover",null,e.noop),n[i].setAttribute("aria-expanded","false"),e(f).removeClass(p),e(a).removeClass(p).trigger(e.Event(l.HIDDEN,c)))}}}},u._getParentFromElement=function(e){var t,n=s.getSelectorFromElement(e);return n&&(t=document.querySelector(n)),t||e.parentNode},u._dataApiKeydownHandler=function(t){if((/input|textarea/i.test(t.target.tagName)?!(32===t.which||27!==t.which&&(40!==t.which&&38!==t.which||e(t.target).closest(b).length)):c.test(t.which))&&(t.preventDefault(),t.stopPropagation(),!this.disabled&&!e(this).hasClass(f))){var n=u._getParentFromElement(this),r=e(n).hasClass(p);if((r||27===t.which&&32===t.which)&&(!r||27!==t.which&&32!==t.which)){var i=[].slice.call(n.querySelectorAll(x));if(0!==i.length){var o=i.indexOf(t.target);38===t.which&&o>0&&o--,40===t.which&&o<i.length-1&&o++,o<0&&(o=0),i[o].focus()}}else{if(27===t.which){var a=n.querySelector(y);e(a).trigger("focus")}e(this).trigger("click")}}},i(u,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return O}},{key:"DefaultType",get:function(){return D}}]),u}();return e(document).on(l.KEYDOWN_DATA_API,y,I._dataApiKeydownHandler).on(l.KEYDOWN_DATA_API,b,I._dataApiKeydownHandler).on(l.CLICK_DATA_API+" "+l.KEYUP_DATA_API,I._clearMenus).on(l.CLICK_DATA_API,y,function(t){t.preventDefault(),t.stopPropagation(),I._jQueryInterface.call(e(this),"toggle")}).on(l.CLICK_DATA_API,_,function(e){e.stopPropagation()}),e.fn[t]=I._jQueryInterface,e.fn[t].Constructor=I,e.fn[t].noConflict=function(){return e.fn[t]=u,I._jQueryInterface},I}(t),d=function(e){var t="modal",n=".bs.modal",r=e.fn.modal,o={backdrop:!0,keyboard:!0,focus:!0,show:!0},u={backdrop:"(boolean|string)",keyboard:"boolean",focus:"boolean",show:"boolean"},c={HIDE:"hide.bs.modal",HIDDEN:"hidden.bs.modal",SHOW:"show.bs.modal",SHOWN:"shown.bs.modal",FOCUSIN:"focusin.bs.modal",RESIZE:"resize.bs.modal",CLICK_DISMISS:"click.dismiss.bs.modal",KEYDOWN_DISMISS:"keydown.dismiss.bs.modal",MOUSEUP_DISMISS:"mouseup.dismiss.bs.modal",MOUSEDOWN_DISMISS:"mousedown.dismiss.bs.modal",CLICK_DATA_API:"click.bs.modal.data-api"},l="modal-scrollbar-measure",f="modal-backdrop",p="modal-open",d="fade",h="show",v={DIALOG:".modal-dialog",DATA_TOGGLE:'[data-toggle="modal"]',DATA_DISMISS:'[data-dismiss="modal"]',FIXED_CONTENT:".fixed-top, .fixed-bottom, .is-fixed, .sticky-top",STICKY_CONTENT:".sticky-top"},g=function(){function r(e,t){this._config=this._getConfig(t),this._element=e,this._dialog=e.querySelector(v.DIALOG),this._backdrop=null,this._isShown=!1,this._isBodyOverflowing=!1,this._ignoreBackdropClick=!1,this._scrollbarWidth=0}var g=r.prototype;return g.toggle=function(e){return this._isShown?this.hide():this.show(e)},g.show=function(t){var n=this;if(!this._isTransitioning&&!this._isShown){e(this._element).hasClass(d)&&(this._isTransitioning=!0);var r=e.Event(c.SHOW,{relatedTarget:t});e(this._element).trigger(r),this._isShown||r.isDefaultPrevented()||(this._isShown=!0,this._checkScrollbar(),this._setScrollbar(),this._adjustDialog(),e(document.body).addClass(p),this._setEscapeEvent(),this._setResizeEvent(),e(this._element).on(c.CLICK_DISMISS,v.DATA_DISMISS,function(e){return n.hide(e)}),e(this._dialog).on(c.MOUSEDOWN_DISMISS,function(){e(n._element).one(c.MOUSEUP_DISMISS,function(t){e(t.target).is(n._element)&&(n._ignoreBackdropClick=!0)})}),this._showBackdrop(function(){return n._showElement(t)}))}},g.hide=function(t){var n=this;if(t&&t.preventDefault(),!this._isTransitioning&&this._isShown){var r=e.Event(c.HIDE);if(e(this._element).trigger(r),this._isShown&&!r.isDefaultPrevented()){this._isShown=!1;var i=e(this._element).hasClass(d);if(i&&(this._isTransitioning=!0),this._setEscapeEvent(),this._setResizeEvent(),e(document).off(c.FOCUSIN),e(this._element).removeClass(h),e(this._element).off(c.CLICK_DISMISS),e(this._dialog).off(c.MOUSEDOWN_DISMISS),i){var o=s.getTransitionDurationFromElement(this._element);e(this._element).one(s.TRANSITION_END,function(e){return n._hideModal(e)}).emulateTransitionEnd(o)}else this._hideModal()}}},g.dispose=function(){e.removeData(this._element,"bs.modal"),e(window,document,this._element,this._backdrop).off(n),this._config=null,this._element=null,this._dialog=null,this._backdrop=null,this._isShown=null,this._isBodyOverflowing=null,this._ignoreBackdropClick=null,this._scrollbarWidth=null},g.handleUpdate=function(){this._adjustDialog()},g._getConfig=function(e){return e=a({},o,e),s.typeCheckConfig(t,e,u),e},g._showElement=function(t){var n=this,r=e(this._element).hasClass(d);this._element.parentNode&&this._element.parentNode.nodeType===Node.ELEMENT_NODE||document.body.appendChild(this._element),this._element.style.display="block",this._element.removeAttribute("aria-hidden"),this._element.scrollTop=0,r&&s.reflow(this._element),e(this._element).addClass(h),this._config.focus&&this._enforceFocus();var i=e.Event(c.SHOWN,{relatedTarget:t}),o=function(){n._config.focus&&n._element.focus(),n._isTransitioning=!1,e(n._element).trigger(i)};if(r){var a=s.getTransitionDurationFromElement(this._element);e(this._dialog).one(s.TRANSITION_END,o).emulateTransitionEnd(a)}else o()},g._enforceFocus=function(){var t=this;e(document).off(c.FOCUSIN).on(c.FOCUSIN,function(n){document!==n.target&&t._element!==n.target&&0===e(t._element).has(n.target).length&&t._element.focus()})},g._setEscapeEvent=function(){var t=this;this._isShown&&this._config.keyboard?e(this._element).on(c.KEYDOWN_DISMISS,function(e){27===e.which&&(e.preventDefault(),t.hide())}):this._isShown||e(this._element).off(c.KEYDOWN_DISMISS)},g._setResizeEvent=function(){var t=this;this._isShown?e(window).on(c.RESIZE,function(e){return t.handleUpdate(e)}):e(window).off(c.RESIZE)},g._hideModal=function(){var t=this;this._element.style.display="none",this._element.setAttribute("aria-hidden",!0),this._isTransitioning=!1,this._showBackdrop(function(){e(document.body).removeClass(p),t._resetAdjustments(),t._resetScrollbar(),e(t._element).trigger(c.HIDDEN)})},g._removeBackdrop=function(){this._backdrop&&(e(this._backdrop).remove(),this._backdrop=null)},g._showBackdrop=function(t){var n=this,r=e(this._element).hasClass(d)?d:"";if(this._isShown&&this._config.backdrop){if(this._backdrop=document.createElement("div"),this._backdrop.className=f,r&&this._backdrop.classList.add(r),e(this._backdrop).appendTo(document.body),e(this._element).on(c.CLICK_DISMISS,function(e){n._ignoreBackdropClick?n._ignoreBackdropClick=!1:e.target===e.currentTarget&&("static"===n._config.backdrop?n._element.focus():n.hide())}),r&&s.reflow(this._backdrop),e(this._backdrop).addClass(h),!t)return;if(!r)return void t();var i=s.getTransitionDurationFromElement(this._backdrop);e(this._backdrop).one(s.TRANSITION_END,t).emulateTransitionEnd(i)}else if(!this._isShown&&this._backdrop){e(this._backdrop).removeClass(h);var o=function(){n._removeBackdrop(),t&&t()};if(e(this._element).hasClass(d)){var a=s.getTransitionDurationFromElement(this._backdrop);e(this._backdrop).one(s.TRANSITION_END,o).emulateTransitionEnd(a)}else o()}else t&&t()},g._adjustDialog=function(){var e=this._element.scrollHeight>document.documentElement.clientHeight;!this._isBodyOverflowing&&e&&(this._element.style.paddingLeft=this._scrollbarWidth+"px"),this._isBodyOverflowing&&!e&&(this._element.style.paddingRight=this._scrollbarWidth+"px")},g._resetAdjustments=function(){this._element.style.paddingLeft="",this._element.style.paddingRight=""},g._checkScrollbar=function(){var e=document.body.getBoundingClientRect();this._isBodyOverflowing=e.left+e.right<window.innerWidth,this._scrollbarWidth=this._getScrollbarWidth()},g._setScrollbar=function(){var t=this;if(this._isBodyOverflowing){var n=[].slice.call(document.querySelectorAll(v.FIXED_CONTENT)),r=[].slice.call(document.querySelectorAll(v.STICKY_CONTENT));e(n).each(function(n,r){var i=r.style.paddingRight,o=e(r).css("padding-right");e(r).data("padding-right",i).css("padding-right",parseFloat(o)+t._scrollbarWidth+"px")}),e(r).each(function(n,r){var i=r.style.marginRight,o=e(r).css("margin-right");e(r).data("margin-right",i).css("margin-right",parseFloat(o)-t._scrollbarWidth+"px")});var i=document.body.style.paddingRight,o=e(document.body).css("padding-right");e(document.body).data("padding-right",i).css("padding-right",parseFloat(o)+this._scrollbarWidth+"px")}},g._resetScrollbar=function(){var t=[].slice.call(document.querySelectorAll(v.FIXED_CONTENT));e(t).each(function(t,n){var r=e(n).data("padding-right");e(n).removeData("padding-right"),n.style.paddingRight=r||""});var n=[].slice.call(document.querySelectorAll(""+v.STICKY_CONTENT));e(n).each(function(t,n){var r=e(n).data("margin-right");void 0!==r&&e(n).css("margin-right",r).removeData("margin-right")});var r=e(document.body).data("padding-right");e(document.body).removeData("padding-right"),document.body.style.paddingRight=r||""},g._getScrollbarWidth=function(){var e=document.createElement("div");e.className=l,document.body.appendChild(e);var t=e.getBoundingClientRect().width-e.clientWidth;return document.body.removeChild(e),t},r._jQueryInterface=function(t,n){return this.each(function(){var i=e(this).data("bs.modal"),s=a({},o,e(this).data(),"object"==typeof t&&t?t:{});if(i||(i=new r(this,s),e(this).data("bs.modal",i)),"string"==typeof t){if(void 0===i[t])throw new TypeError('No method named "'+t+'"');i[t](n)}else s.show&&i.show(n)})},i(r,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return o}}]),r}();return e(document).on(c.CLICK_DATA_API,v.DATA_TOGGLE,function(t){var n,r=this,i=s.getSelectorFromElement(this);i&&(n=document.querySelector(i));var o=e(n).data("bs.modal")?"toggle":a({},e(n).data(),e(this).data());"A"!==this.tagName&&"AREA"!==this.tagName||t.preventDefault();var u=e(n).one(c.SHOW,function(t){t.isDefaultPrevented()||u.one(c.HIDDEN,function(){e(r).is(":visible")&&r.focus()})});g._jQueryInterface.call(e(n),o,this)}),e.fn.modal=g._jQueryInterface,e.fn.modal.Constructor=g,e.fn.modal.noConflict=function(){return e.fn.modal=r,g._jQueryInterface},g}(t),h=function(e){var t="tooltip",r=".bs.tooltip",o=e.fn[t],u=new RegExp("(^|\\s)bs-tooltip\\S+","g"),c={animation:"boolean",template:"string",title:"(string|element|function)",trigger:"string",delay:"(number|object)",html:"boolean",selector:"(string|boolean)",placement:"(string|function)",offset:"(number|string)",container:"(string|element|boolean)",fallbackPlacement:"(string|array)",boundary:"(string|element)"},l={AUTO:"auto",TOP:"top",RIGHT:"right",BOTTOM:"bottom",LEFT:"left"},f={animation:!0,template:'<div class="tooltip" role="tooltip"><div class="arrow"></div><div class="tooltip-inner"></div></div>',trigger:"hover focus",title:"",delay:0,html:!1,selector:!1,placement:"top",offset:0,container:!1,fallbackPlacement:"flip",boundary:"scrollParent"},p="show",d="out",h={HIDE:"hide"+r,HIDDEN:"hidden"+r,SHOW:"show"+r,SHOWN:"shown"+r,INSERTED:"inserted"+r,CLICK:"click"+r,FOCUSIN:"focusin"+r,FOCUSOUT:"focusout"+r,MOUSEENTER:"mouseenter"+r,MOUSELEAVE:"mouseleave"+r},v="fade",g="show",m=".tooltip-inner",y=".arrow",_="hover",b="focus",w="click",x="manual",C=function(){function o(e,t){if(void 0===n)throw new TypeError("Bootstrap tooltips require Popper.js (https://popper.js.org)");this._isEnabled=!0,this._timeout=0,this._hoverState="",this._activeTrigger={},this._popper=null,this.element=e,this.config=this._getConfig(t),this.tip=null,this._setListeners()}var C=o.prototype;return C.enable=function(){this._isEnabled=!0},C.disable=function(){this._isEnabled=!1},C.toggleEnabled=function(){this._isEnabled=!this._isEnabled},C.toggle=function(t){if(this._isEnabled)if(t){var n=this.constructor.DATA_KEY,r=e(t.currentTarget).data(n);r||(r=new this.constructor(t.currentTarget,this._getDelegateConfig()),e(t.currentTarget).data(n,r)),r._activeTrigger.click=!r._activeTrigger.click,r._isWithActiveTrigger()?r._enter(null,r):r._leave(null,r)}else{if(e(this.getTipElement()).hasClass(g))return void this._leave(null,this);this._enter(null,this)}},C.dispose=function(){clearTimeout(this._timeout),e.removeData(this.element,this.constructor.DATA_KEY),e(this.element).off(this.constructor.EVENT_KEY),e(this.element).closest(".modal").off("hide.bs.modal"),this.tip&&e(this.tip).remove(),this._isEnabled=null,this._timeout=null,this._hoverState=null,this._activeTrigger=null,null!==this._popper&&this._popper.destroy(),this._popper=null,this.element=null,this.config=null,this.tip=null},C.show=function(){var t=this;if("none"===e(this.element).css("display"))throw new Error("Please use show on visible elements");var r=e.Event(this.constructor.Event.SHOW);if(this.isWithContent()&&this._isEnabled){e(this.element).trigger(r);var i=e.contains(this.element.ownerDocument.documentElement,this.element);if(r.isDefaultPrevented()||!i)return;var o=this.getTipElement(),a=s.getUID(this.constructor.NAME);o.setAttribute("id",a),this.element.setAttribute("aria-describedby",a),this.setContent(),this.config.animation&&e(o).addClass(v);var u="function"==typeof this.config.placement?this.config.placement.call(this,o,this.element):this.config.placement,c=this._getAttachment(u);this.addAttachmentClass(c);var l=!1===this.config.container?document.body:e(document).find(this.config.container);e(o).data(this.constructor.DATA_KEY,this),e.contains(this.element.ownerDocument.documentElement,this.tip)||e(o).appendTo(l),e(this.element).trigger(this.constructor.Event.INSERTED),this._popper=new n(this.element,o,{placement:c,modifiers:{offset:{offset:this.config.offset},flip:{behavior:this.config.fallbackPlacement},arrow:{element:y},preventOverflow:{boundariesElement:this.config.boundary}},onCreate:function(e){e.originalPlacement!==e.placement&&t._handlePopperPlacementChange(e)},onUpdate:function(e){t._handlePopperPlacementChange(e)}}),e(o).addClass(g),"ontouchstart"in document.documentElement&&e(document.body).children().on("mouseover",null,e.noop);var f=function(){t.config.animation&&t._fixTransition();var n=t._hoverState;t._hoverState=null,e(t.element).trigger(t.constructor.Event.SHOWN),n===d&&t._leave(null,t)};if(e(this.tip).hasClass(v)){var p=s.getTransitionDurationFromElement(this.tip);e(this.tip).one(s.TRANSITION_END,f).emulateTransitionEnd(p)}else f()}},C.hide=function(t){var n=this,r=this.getTipElement(),i=e.Event(this.constructor.Event.HIDE),o=function(){n._hoverState!==p&&r.parentNode&&r.parentNode.removeChild(r),n._cleanTipClass(),n.element.removeAttribute("aria-describedby"),e(n.element).trigger(n.constructor.Event.HIDDEN),null!==n._popper&&n._popper.destroy(),t&&t()};if(e(this.element).trigger(i),!i.isDefaultPrevented()){if(e(r).removeClass(g),"ontouchstart"in document.documentElement&&e(document.body).children().off("mouseover",null,e.noop),this._activeTrigger[w]=!1,this._activeTrigger[b]=!1,this._activeTrigger[_]=!1,e(this.tip).hasClass(v)){var a=s.getTransitionDurationFromElement(r);e(r).one(s.TRANSITION_END,o).emulateTransitionEnd(a)}else o();this._hoverState=""}},C.update=function(){null!==this._popper&&this._popper.scheduleUpdate()},C.isWithContent=function(){return Boolean(this.getTitle())},C.addAttachmentClass=function(t){e(this.getTipElement()).addClass("bs-tooltip-"+t)},C.getTipElement=function(){return this.tip=this.tip||e(this.config.template)[0],this.tip},C.setContent=function(){var t=this.getTipElement();this.setElementContent(e(t.querySelectorAll(m)),this.getTitle()),e(t).removeClass(v+" "+g)},C.setElementContent=function(t,n){var r=this.config.html;"object"==typeof n&&(n.nodeType||n.jquery)?r?e(n).parent().is(t)||t.empty().append(n):t.text(e(n).text()):t[r?"html":"text"](n)},C.getTitle=function(){var e=this.element.getAttribute("data-original-title");return e||(e="function"==typeof this.config.title?this.config.title.call(this.element):this.config.title),e},C._getAttachment=function(e){return l[e.toUpperCase()]},C._setListeners=function(){var t=this;this.config.trigger.split(" ").forEach(function(n){if("click"===n)e(t.element).on(t.constructor.Event.CLICK,t.config.selector,function(e){return t.toggle(e)});else if(n!==x){var r=n===_?t.constructor.Event.MOUSEENTER:t.constructor.Event.FOCUSIN,i=n===_?t.constructor.Event.MOUSELEAVE:t.constructor.Event.FOCUSOUT;e(t.element).on(r,t.config.selector,function(e){return t._enter(e)}).on(i,t.config.selector,function(e){return t._leave(e)})}e(t.element).closest(".modal").on("hide.bs.modal",function(){return t.hide()})}),this.config.selector?this.config=a({},this.config,{trigger:"manual",selector:""}):this._fixTitle()},C._fixTitle=function(){var e=typeof this.element.getAttribute("data-original-title");(this.element.getAttribute("title")||"string"!==e)&&(this.element.setAttribute("data-original-title",this.element.getAttribute("title")||""),this.element.setAttribute("title",""))},C._enter=function(t,n){var r=this.constructor.DATA_KEY;(n=n||e(t.currentTarget).data(r))||(n=new this.constructor(t.currentTarget,this._getDelegateConfig()),e(t.currentTarget).data(r,n)),t&&(n._activeTrigger["focusin"===t.type?b:_]=!0),e(n.getTipElement()).hasClass(g)||n._hoverState===p?n._hoverState=p:(clearTimeout(n._timeout),n._hoverState=p,n.config.delay&&n.config.delay.show?n._timeout=setTimeout(function(){n._hoverState===p&&n.show()},n.config.delay.show):n.show())},C._leave=function(t,n){var r=this.constructor.DATA_KEY;(n=n||e(t.currentTarget).data(r))||(n=new this.constructor(t.currentTarget,this._getDelegateConfig()),e(t.currentTarget).data(r,n)),t&&(n._activeTrigger["focusout"===t.type?b:_]=!1),n._isWithActiveTrigger()||(clearTimeout(n._timeout),n._hoverState=d,n.config.delay&&n.config.delay.hide?n._timeout=setTimeout(function(){n._hoverState===d&&n.hide()},n.config.delay.hide):n.hide())},C._isWithActiveTrigger=function(){for(var e in this._activeTrigger)if(this._activeTrigger[e])return!0;return!1},C._getConfig=function(n){return"number"==typeof(n=a({},this.constructor.Default,e(this.element).data(),"object"==typeof n&&n?n:{})).delay&&(n.delay={show:n.delay,hide:n.delay}),"number"==typeof n.title&&(n.title=n.title.toString()),"number"==typeof n.content&&(n.content=n.content.toString()),s.typeCheckConfig(t,n,this.constructor.DefaultType),n},C._getDelegateConfig=function(){var e={};if(this.config)for(var t in this.config)this.constructor.Default[t]!==this.config[t]&&(e[t]=this.config[t]);return e},C._cleanTipClass=function(){var t=e(this.getTipElement()),n=t.attr("class").match(u);null!==n&&n.length&&t.removeClass(n.join(""))},C._handlePopperPlacementChange=function(e){var t=e.instance;this.tip=t.popper,this._cleanTipClass(),this.addAttachmentClass(this._getAttachment(e.placement))},C._fixTransition=function(){var t=this.getTipElement(),n=this.config.animation;null===t.getAttribute("x-placement")&&(e(t).removeClass(v),this.config.animation=!1,this.hide(),this.show(),this.config.animation=n)},o._jQueryInterface=function(t){return this.each(function(){var n=e(this).data("bs.tooltip"),r="object"==typeof t&&t;if((n||!/dispose|hide/.test(t))&&(n||(n=new o(this,r),e(this).data("bs.tooltip",n)),"string"==typeof t)){if(void 0===n[t])throw new TypeError('No method named "'+t+'"');n[t]()}})},i(o,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return f}},{key:"NAME",get:function(){return t}},{key:"DATA_KEY",get:function(){return"bs.tooltip"}},{key:"Event",get:function(){return h}},{key:"EVENT_KEY",get:function(){return r}},{key:"DefaultType",get:function(){return c}}]),o}();return e.fn[t]=C._jQueryInterface,e.fn[t].Constructor=C,e.fn[t].noConflict=function(){return e.fn[t]=o,C._jQueryInterface},C}(t),v=function(e){var t="popover",n=".bs.popover",r=e.fn[t],o=new RegExp("(^|\\s)bs-popover\\S+","g"),s=a({},h.Default,{placement:"right",trigger:"click",content:"",template:'<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div></div>'}),u=a({},h.DefaultType,{content:"(string|element|function)"}),c="fade",l="show",f=".popover-header",p=".popover-body",d={HIDE:"hide"+n,HIDDEN:"hidden"+n,SHOW:"show"+n,SHOWN:"shown"+n,INSERTED:"inserted"+n,CLICK:"click"+n,FOCUSIN:"focusin"+n,FOCUSOUT:"focusout"+n,MOUSEENTER:"mouseenter"+n,MOUSELEAVE:"mouseleave"+n},v=function(r){var a,h;function v(){return r.apply(this,arguments)||this}h=r,(a=v).prototype=Object.create(h.prototype),a.prototype.constructor=a,a.__proto__=h;var g=v.prototype;return g.isWithContent=function(){return this.getTitle()||this._getContent()},g.addAttachmentClass=function(t){e(this.getTipElement()).addClass("bs-popover-"+t)},g.getTipElement=function(){return this.tip=this.tip||e(this.config.template)[0],this.tip},g.setContent=function(){var t=e(this.getTipElement());this.setElementContent(t.find(f),this.getTitle());var n=this._getContent();"function"==typeof n&&(n=n.call(this.element)),this.setElementContent(t.find(p),n),t.removeClass(c+" "+l)},g._getContent=function(){return this.element.getAttribute("data-content")||this.config.content},g._cleanTipClass=function(){var t=e(this.getTipElement()),n=t.attr("class").match(o);null!==n&&n.length>0&&t.removeClass(n.join(""))},v._jQueryInterface=function(t){return this.each(function(){var n=e(this).data("bs.popover"),r="object"==typeof t?t:null;if((n||!/destroy|hide/.test(t))&&(n||(n=new v(this,r),e(this).data("bs.popover",n)),"string"==typeof t)){if(void 0===n[t])throw new TypeError('No method named "'+t+'"');n[t]()}})},i(v,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return s}},{key:"NAME",get:function(){return t}},{key:"DATA_KEY",get:function(){return"bs.popover"}},{key:"Event",get:function(){return d}},{key:"EVENT_KEY",get:function(){return n}},{key:"DefaultType",get:function(){return u}}]),v}(h);return e.fn[t]=v._jQueryInterface,e.fn[t].Constructor=v,e.fn[t].noConflict=function(){return e.fn[t]=r,v._jQueryInterface},v}(t),g=function(e){var t="scrollspy",n=e.fn[t],r={offset:10,method:"auto",target:""},o={offset:"number",method:"string",target:"(string|element)"},u={ACTIVATE:"activate.bs.scrollspy",SCROLL:"scroll.bs.scrollspy",LOAD_DATA_API:"load.bs.scrollspy.data-api"},c="dropdown-item",l="active",f={DATA_SPY:'[data-spy="scroll"]',ACTIVE:".active",NAV_LIST_GROUP:".nav, .list-group",NAV_LINKS:".nav-link",NAV_ITEMS:".nav-item",LIST_ITEMS:".list-group-item",DROPDOWN:".dropdown",DROPDOWN_ITEMS:".dropdown-item",DROPDOWN_TOGGLE:".dropdown-toggle"},p="offset",d="position",h=function(){function n(t,n){var r=this;this._element=t,this._scrollElement="BODY"===t.tagName?window:t,this._config=this._getConfig(n),this._selector=this._config.target+" "+f.NAV_LINKS+","+this._config.target+" "+f.LIST_ITEMS+","+this._config.target+" "+f.DROPDOWN_ITEMS,this._offsets=[],this._targets=[],this._activeTarget=null,this._scrollHeight=0,e(this._scrollElement).on(u.SCROLL,function(e){return r._process(e)}),this.refresh(),this._process()}var h=n.prototype;return h.refresh=function(){var t=this,n=this._scrollElement===this._scrollElement.window?p:d,r="auto"===this._config.method?n:this._config.method,i=r===d?this._getScrollTop():0;this._offsets=[],this._targets=[],this._scrollHeight=this._getScrollHeight(),[].slice.call(document.querySelectorAll(this._selector)).map(function(t){var n,o=s.getSelectorFromElement(t);if(o&&(n=document.querySelector(o)),n){var a=n.getBoundingClientRect();if(a.width||a.height)return[e(n)[r]().top+i,o]}return null}).filter(function(e){return e}).sort(function(e,t){return e[0]-t[0]}).forEach(function(e){t._offsets.push(e[0]),t._targets.push(e[1])})},h.dispose=function(){e.removeData(this._element,"bs.scrollspy"),e(this._scrollElement).off(".bs.scrollspy"),this._element=null,this._scrollElement=null,this._config=null,this._selector=null,this._offsets=null,this._targets=null,this._activeTarget=null,this._scrollHeight=null},h._getConfig=function(n){if("string"!=typeof(n=a({},r,"object"==typeof n&&n?n:{})).target){var i=e(n.target).attr("id");i||(i=s.getUID(t),e(n.target).attr("id",i)),n.target="#"+i}return s.typeCheckConfig(t,n,o),n},h._getScrollTop=function(){return this._scrollElement===window?this._scrollElement.pageYOffset:this._scrollElement.scrollTop},h._getScrollHeight=function(){return this._scrollElement.scrollHeight||Math.max(document.body.scrollHeight,document.documentElement.scrollHeight)},h._getOffsetHeight=function(){return this._scrollElement===window?window.innerHeight:this._scrollElement.getBoundingClientRect().height},h._process=function(){var e=this._getScrollTop()+this._config.offset,t=this._getScrollHeight(),n=this._config.offset+t-this._getOffsetHeight();if(this._scrollHeight!==t&&this.refresh(),e>=n){var r=this._targets[this._targets.length-1];this._activeTarget!==r&&this._activate(r)}else{if(this._activeTarget&&e<this._offsets[0]&&this._offsets[0]>0)return this._activeTarget=null,void this._clear();for(var i=this._offsets.length;i--;){this._activeTarget!==this._targets[i]&&e>=this._offsets[i]&&(void 0===this._offsets[i+1]||e<this._offsets[i+1])&&this._activate(this._targets[i])}}},h._activate=function(t){this._activeTarget=t,this._clear();var n=this._selector.split(",");n=n.map(function(e){return e+'[data-target="'+t+'"],'+e+'[href="'+t+'"]'});var r=e([].slice.call(document.querySelectorAll(n.join(","))));r.hasClass(c)?(r.closest(f.DROPDOWN).find(f.DROPDOWN_TOGGLE).addClass(l),r.addClass(l)):(r.addClass(l),r.parents(f.NAV_LIST_GROUP).prev(f.NAV_LINKS+", "+f.LIST_ITEMS).addClass(l),r.parents(f.NAV_LIST_GROUP).prev(f.NAV_ITEMS).children(f.NAV_LINKS).addClass(l)),e(this._scrollElement).trigger(u.ACTIVATE,{relatedTarget:t})},h._clear=function(){var t=[].slice.call(document.querySelectorAll(this._selector));e(t).filter(f.ACTIVE).removeClass(l)},n._jQueryInterface=function(t){return this.each(function(){var r=e(this).data("bs.scrollspy");if(r||(r=new n(this,"object"==typeof t&&t),e(this).data("bs.scrollspy",r)),"string"==typeof t){if(void 0===r[t])throw new TypeError('No method named "'+t+'"');r[t]()}})},i(n,null,[{key:"VERSION",get:function(){return"4.1.2"}},{key:"Default",get:function(){return r}}]),n}();return e(window).on(u.LOAD_DATA_API,function(){for(var t=[].slice.call(document.querySelectorAll(f.DATA_SPY)),n=t.length;n--;){var r=e(t[n]);h._jQueryInterface.call(r,r.data())}}),e.fn[t]=h._jQueryInterface,e.fn[t].Constructor=h,e.fn[t].noConflict=function(){return e.fn[t]=n,h._jQueryInterface},h}(t),m=function(e){var t=e.fn.tab,n={HIDE:"hide.bs.tab",HIDDEN:"hidden.bs.tab",SHOW:"show.bs.tab",SHOWN:"shown.bs.tab",CLICK_DATA_API:"click.bs.tab.data-api"},r="dropdown-menu",o="active",a="disabled",u="fade",c="show",l=".dropdown",f=".nav, .list-group",p=".active",d="> li > .active",h='[data-toggle="tab"], [data-toggle="pill"], [data-toggle="list"]',v=".dropdown-toggle",g="> .dropdown-menu .active",m=function(){function t(e){this._element=e}var h=t.prototype;return h.show=function(){var t=this;if(!(this._element.parentNode&&this._element.parentNode.nodeType===Node.ELEMENT_NODE&&e(this._element).hasClass(o)||e(this._element).hasClass(a))){var r,i,u=e(this._element).closest(f)[0],c=s.getSelectorFromElement(this._element);if(u){var l="UL"===u.nodeName?d:p;i=(i=e.makeArray(e(u).find(l)))[i.length-1]}var h=e.Event(n.HIDE,{relatedTarget:this._element}),v=e.Event(n.SHOW,{relatedTarget:i});if(i&&e(i).trigger(h),e(this._element).trigger(v),!v.isDefaultPrevented()&&!h.isDefaultPrevented()){c&&(r=document.querySelector(c)),this._activate(this._element,u);var g=function(){var r=e.Event(n.HIDDEN,{relatedTarget:t._element}),o=e.Event(n.SHOWN,{relatedTarget:i});e(i).trigger(r),e(t._element).trigger(o)};r?this._activate(r,r.parentNode,g):g()}}},h.dispose=function(){e.removeData(this._element,"bs.tab"),this._element=null},h._activate=function(t,n,r){var i=this,o=("UL"===n.nodeName?e(n).find(d):e(n).children(p))[0],a=r&&o&&e(o).hasClass(u),c=function(){return i._transitionComplete(t,o,r)};if(o&&a){var l=s.getTransitionDurationFromElement(o);e(o).one(s.TRANSITION_END,c).emulateTransitionEnd(l)}else c()},h._transitionComplete=function(t,n,i){if(n){e(n).removeClass(c+" "+o);var a=e(n.parentNode).find(g)[0];a&&e(a).removeClass(o),"tab"===n.getAttribute("role")&&n.setAttribute("aria-selected",!1)}if(e(t).addClass(o),"tab"===t.getAttribute("role")&&t.setAttribute("aria-selected",!0),s.reflow(t),e(t).addClass(c),t.parentNode&&e(t.parentNode).hasClass(r)){var u=e(t).closest(l)[0];if(u){var f=[].slice.call(u.querySelectorAll(v));e(f).addClass(o)}t.setAttribute("aria-expanded",!0)}i&&i()},t._jQueryInterface=function(n){return this.each(function(){var r=e(this),i=r.data("bs.tab");if(i||(i=new t(this),r.data("bs.tab",i)),"string"==typeof n){if(void 0===i[n])throw new TypeError('No method named "'+n+'"');i[n]()}})},i(t,null,[{key:"VERSION",get:function(){return"4.1.2"}}]),t}();return e(document).on(n.CLICK_DATA_API,h,function(t){t.preventDefault(),m._jQueryInterface.call(e(this),"show")}),e.fn.tab=m._jQueryInterface,e.fn.tab.Constructor=m,e.fn.tab.noConflict=function(){return e.fn.tab=t,m._jQueryInterface},m}(t);!function(e){if(void 0===e)throw new TypeError("Bootstrap's JavaScript requires jQuery. jQuery must be included before Bootstrap's JavaScript.");var t=e.fn.jquery.split(" ")[0].split(".");if(t[0]<2&&t[1]<9||1===t[0]&&9===t[1]&&t[2]<1||t[0]>=4)throw new Error("Bootstrap's JavaScript requires at least jQuery v1.9.1 but less than v4.0.0")}(t),e.Util=s,e.Alert=u,e.Button=c,e.Carousel=l,e.Collapse=f,e.Dropdown=p,e.Modal=d,e.Popover=v,e.Scrollspy=g,e.Tab=m,e.Tooltip=h,Object.defineProperty(e,"__esModule",{value:!0})})(t,n(4),n(3))},function(e,t,n){e.exports=n(18)},function(e,t,n){"use strict";var r=n(0),i=n(5),o=n(20),a=n(2);function s(e){var t=new o(e),n=i(o.prototype.request,t);return r.extend(n,o.prototype,t),r.extend(n,t),n}var u=s(a);u.Axios=o,u.create=function(e){return s(r.merge(a,e))},u.Cancel=n(10),u.CancelToken=n(34),u.isCancel=n(9),u.all=function(e){return Promise.all(e)},u.spread=n(35),e.exports=u,e.exports.default=u},function(e,t){function n(e){return!!e.constructor&&"function"==typeof e.constructor.isBuffer&&e.constructor.isBuffer(e)}e.exports=function(e){return null!=e&&(n(e)||function(e){return"function"==typeof e.readFloatLE&&"function"==typeof e.slice&&n(e.slice(0,0))}(e)||!!e._isBuffer)}},function(e,t,n){"use strict";var r=n(2),i=n(0),o=n(29),a=n(30);function s(e){this.defaults=e,this.interceptors={request:new o,response:new o}}s.prototype.request=function(e){"string"==typeof e&&(e=i.merge({url:arguments[0]},arguments[1])),(e=i.merge(r,{method:"get"},this.defaults,e)).method=e.method.toLowerCase();var t=[a,void 0],n=Promise.resolve(e);for(this.interceptors.request.forEach(function(e){t.unshift(e.fulfilled,e.rejected)}),this.interceptors.response.forEach(function(e){t.push(e.fulfilled,e.rejected)});t.length;)n=n.then(t.shift(),t.shift());return n},i.forEach(["delete","get","head","options"],function(e){s.prototype[e]=function(t,n){return this.request(i.merge(n||{},{method:e,url:t}))}}),i.forEach(["post","put","patch"],function(e){s.prototype[e]=function(t,n,r){return this.request(i.merge(r||{},{method:e,url:t,data:n}))}}),e.exports=s},function(e,t,n){"use strict";var r=n(0);e.exports=function(e,t){r.forEach(e,function(n,r){r!==t&&r.toUpperCase()===t.toUpperCase()&&(e[t]=n,delete e[r])})}},function(e,t,n){"use strict";var r=n(8);e.exports=function(e,t,n){var i=n.config.validateStatus;n.status&&i&&!i(n.status)?t(r("Request failed with status code "+n.status,n.config,null,n.request,n)):e(n)}},function(e,t,n){"use strict";e.exports=function(e,t,n,r,i){return e.config=t,n&&(e.code=n),e.request=r,e.response=i,e}},function(e,t,n){"use strict";var r=n(0);function i(e){return encodeURIComponent(e).replace(/%40/gi,"@").replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}e.exports=function(e,t,n){if(!t)return e;var o;if(n)o=n(t);else if(r.isURLSearchParams(t))o=t.toString();else{var a=[];r.forEach(t,function(e,t){null!=e&&(r.isArray(e)?t+="[]":e=[e],r.forEach(e,function(e){r.isDate(e)?e=e.toISOString():r.isObject(e)&&(e=JSON.stringify(e)),a.push(i(t)+"="+i(e))}))}),o=a.join("&")}return o&&(e+=(-1===e.indexOf("?")?"?":"&")+o),e}},function(e,t,n){"use strict";var r=n(0),i=["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"];e.exports=function(e){var t,n,o,a={};return e?(r.forEach(e.split("\n"),function(e){if(o=e.indexOf(":"),t=r.trim(e.substr(0,o)).toLowerCase(),n=r.trim(e.substr(o+1)),t){if(a[t]&&i.indexOf(t)>=0)return;a[t]="set-cookie"===t?(a[t]?a[t]:[]).concat([n]):a[t]?a[t]+", "+n:n}}),a):a}},function(e,t,n){"use strict";var r=n(0);e.exports=r.isStandardBrowserEnv()?function(){var e,t=/(msie|trident)/i.test(navigator.userAgent),n=document.createElement("a");function i(e){var r=e;return t&&(n.setAttribute("href",r),r=n.href),n.setAttribute("href",r),{href:n.href,protocol:n.protocol?n.protocol.replace(/:$/,""):"",host:n.host,search:n.search?n.search.replace(/^\?/,""):"",hash:n.hash?n.hash.replace(/^#/,""):"",hostname:n.hostname,port:n.port,pathname:"/"===n.pathname.charAt(0)?n.pathname:"/"+n.pathname}}return e=i(window.location.href),function(t){var n=r.isString(t)?i(t):t;return n.protocol===e.protocol&&n.host===e.host}}():function(){return!0}},function(e,t,n){"use strict";var r="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";function i(){this.message="String contains an invalid character"}i.prototype=new Error,i.prototype.code=5,i.prototype.name="InvalidCharacterError",e.exports=function(e){for(var t,n,o=String(e),a="",s=0,u=r;o.charAt(0|s)||(u="=",s%1);a+=u.charAt(63&t>>8-s%1*8)){if((n=o.charCodeAt(s+=.75))>255)throw new i;t=t<<8|n}return a}},function(e,t,n){"use strict";var r=n(0);e.exports=r.isStandardBrowserEnv()?{write:function(e,t,n,i,o,a){var s=[];s.push(e+"="+encodeURIComponent(t)),r.isNumber(n)&&s.push("expires="+new Date(n).toGMTString()),r.isString(i)&&s.push("path="+i),r.isString(o)&&s.push("domain="+o),!0===a&&s.push("secure"),document.cookie=s.join("; ")},read:function(e){var t=document.cookie.match(new RegExp("(^|;\\s*)("+e+")=([^;]*)"));return t?decodeURIComponent(t[3]):null},remove:function(e){this.write(e,"",Date.now()-864e5)}}:{write:function(){},read:function(){return null},remove:function(){}}},function(e,t,n){"use strict";var r=n(0);function i(){this.handlers=[]}i.prototype.use=function(e,t){return this.handlers.push({fulfilled:e,rejected:t}),this.handlers.length-1},i.prototype.eject=function(e){this.handlers[e]&&(this.handlers[e]=null)},i.prototype.forEach=function(e){r.forEach(this.handlers,function(t){null!==t&&e(t)})},e.exports=i},function(e,t,n){"use strict";var r=n(0),i=n(31),o=n(9),a=n(2),s=n(32),u=n(33);function c(e){e.cancelToken&&e.cancelToken.throwIfRequested()}e.exports=function(e){return c(e),e.baseURL&&!s(e.url)&&(e.url=u(e.baseURL,e.url)),e.headers=e.headers||{},e.data=i(e.data,e.headers,e.transformRequest),e.headers=r.merge(e.headers.common||{},e.headers[e.method]||{},e.headers||{}),r.forEach(["delete","get","head","post","put","patch","common"],function(t){delete e.headers[t]}),(e.adapter||a.adapter)(e).then(function(t){return c(e),t.data=i(t.data,t.headers,e.transformResponse),t},function(t){return o(t)||(c(e),t&&t.response&&(t.response.data=i(t.response.data,t.response.headers,e.transformResponse))),Promise.reject(t)})}},function(e,t,n){"use strict";var r=n(0);e.exports=function(e,t,n){return r.forEach(n,function(n){e=n(e,t)}),e}},function(e,t,n){"use strict";e.exports=function(e){return/^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(e)}},function(e,t,n){"use strict";e.exports=function(e,t){return t?e.replace(/\/+$/,"")+"/"+t.replace(/^\/+/,""):e}},function(e,t,n){"use strict";var r=n(10);function i(e){if("function"!=typeof e)throw new TypeError("executor must be a function.");var t;this.promise=new Promise(function(e){t=e});var n=this;e(function(e){n.reason||(n.reason=new r(e),t(n.reason))})}i.prototype.throwIfRequested=function(){if(this.reason)throw this.reason},i.source=function(){var e;return{token:new i(function(t){e=t}),cancel:e}},e.exports=i},function(e,t,n){"use strict";e.exports=function(e){return function(t){return e.apply(null,t)}}},function(e,t,n){"use strict";(function(t,n){var r=Object.freeze({});function i(e){return null==e}function o(e){return null!=e}function a(e){return!0===e}function s(e){return"string"==typeof e||"number"==typeof e||"symbol"==typeof e||"boolean"==typeof e}function u(e){return null!==e&&"object"==typeof e}var c=Object.prototype.toString;function l(e){return"[object Object]"===c.call(e)}function f(e){return"[object RegExp]"===c.call(e)}function p(e){var t=parseFloat(String(e));return t>=0&&Math.floor(t)===t&&isFinite(e)}function d(e){return null==e?"":"object"==typeof e?JSON.stringify(e,null,2):String(e)}function h(e){var t=parseFloat(e);return isNaN(t)?e:t}function v(e,t){for(var n=Object.create(null),r=e.split(","),i=0;i<r.length;i++)n[r[i]]=!0;return t?function(e){return n[e.toLowerCase()]}:function(e){return n[e]}}var g=v("slot,component",!0),m=v("key,ref,slot,slot-scope,is");function y(e,t){if(e.length){var n=e.indexOf(t);if(n>-1)return e.splice(n,1)}}var _=Object.prototype.hasOwnProperty;function b(e,t){return _.call(e,t)}function w(e){var t=Object.create(null);return function(n){return t[n]||(t[n]=e(n))}}var x=/-(\w)/g,C=w(function(e){return e.replace(x,function(e,t){return t?t.toUpperCase():""})}),E=w(function(e){return e.charAt(0).toUpperCase()+e.slice(1)}),T=/\B([A-Z])/g,A=w(function(e){return e.replace(T,"-$1").toLowerCase()});var S=Function.prototype.bind?function(e,t){return e.bind(t)}:function(e,t){function n(n){var r=arguments.length;return r?r>1?e.apply(t,arguments):e.call(t,n):e.call(t)}return n._length=e.length,n};function k(e,t){t=t||0;for(var n=e.length-t,r=new Array(n);n--;)r[n]=e[n+t];return r}function O(e,t){for(var n in t)e[n]=t[n];return e}function D(e){for(var t={},n=0;n<e.length;n++)e[n]&&O(t,e[n]);return t}function I(e,t,n){}var N=function(e,t,n){return!1},j=function(e){return e};function L(e,t){if(e===t)return!0;var n=u(e),r=u(t);if(!n||!r)return!n&&!r&&String(e)===String(t);try{var i=Array.isArray(e),o=Array.isArray(t);if(i&&o)return e.length===t.length&&e.every(function(e,n){return L(e,t[n])});if(i||o)return!1;var a=Object.keys(e),s=Object.keys(t);return a.length===s.length&&a.every(function(n){return L(e[n],t[n])})}catch(e){return!1}}function $(e,t){for(var n=0;n<e.length;n++)if(L(e[n],t))return n;return-1}function P(e){var t=!1;return function(){t||(t=!0,e.apply(this,arguments))}}var R="data-server-rendered",M=["component","directive","filter"],H=["beforeCreate","created","beforeMount","mounted","beforeUpdate","updated","beforeDestroy","destroyed","activated","deactivated","errorCaptured"],F={optionMergeStrategies:Object.create(null),silent:!1,productionTip:!1,devtools:!1,performance:!1,errorHandler:null,warnHandler:null,ignoredElements:[],keyCodes:Object.create(null),isReservedTag:N,isReservedAttr:N,isUnknownElement:N,getTagNamespace:I,parsePlatformTagName:j,mustUseProp:N,_lifecycleHooks:H};function q(e){var t=(e+"").charCodeAt(0);return 36===t||95===t}function B(e,t,n,r){Object.defineProperty(e,t,{value:n,enumerable:!!r,writable:!0,configurable:!0})}var W=/[^\w.$]/;var U,z="__proto__"in{},V="undefined"!=typeof window,K="undefined"!=typeof WXEnvironment&&!!WXEnvironment.platform,Q=K&&WXEnvironment.platform.toLowerCase(),Y=V&&window.navigator.userAgent.toLowerCase(),X=Y&&/msie|trident/.test(Y),G=Y&&Y.indexOf("msie 9.0")>0,J=Y&&Y.indexOf("edge/")>0,Z=(Y&&Y.indexOf("android"),Y&&/iphone|ipad|ipod|ios/.test(Y)||"ios"===Q),ee=(Y&&/chrome\/\d+/.test(Y),{}.watch),te=!1;if(V)try{var ne={};Object.defineProperty(ne,"passive",{get:function(){te=!0}}),window.addEventListener("test-passive",null,ne)}catch(e){}var re=function(){return void 0===U&&(U=!V&&!K&&void 0!==t&&"server"===t.process.env.VUE_ENV),U},ie=V&&window.__VUE_DEVTOOLS_GLOBAL_HOOK__;function oe(e){return"function"==typeof e&&/native code/.test(e.toString())}var ae,se="undefined"!=typeof Symbol&&oe(Symbol)&&"undefined"!=typeof Reflect&&oe(Reflect.ownKeys);ae="undefined"!=typeof Set&&oe(Set)?Set:function(){function e(){this.set=Object.create(null)}return e.prototype.has=function(e){return!0===this.set[e]},e.prototype.add=function(e){this.set[e]=!0},e.prototype.clear=function(){this.set=Object.create(null)},e}();var ue=I,ce=0,le=function(){this.id=ce++,this.subs=[]};le.prototype.addSub=function(e){this.subs.push(e)},le.prototype.removeSub=function(e){y(this.subs,e)},le.prototype.depend=function(){le.target&&le.target.addDep(this)},le.prototype.notify=function(){for(var e=this.subs.slice(),t=0,n=e.length;t<n;t++)e[t].update()},le.target=null;var fe=[];function pe(e){le.target&&fe.push(le.target),le.target=e}function de(){le.target=fe.pop()}var he=function(e,t,n,r,i,o,a,s){this.tag=e,this.data=t,this.children=n,this.text=r,this.elm=i,this.ns=void 0,this.context=o,this.fnContext=void 0,this.fnOptions=void 0,this.fnScopeId=void 0,this.key=t&&t.key,this.componentOptions=a,this.componentInstance=void 0,this.parent=void 0,this.raw=!1,this.isStatic=!1,this.isRootInsert=!0,this.isComment=!1,this.isCloned=!1,this.isOnce=!1,this.asyncFactory=s,this.asyncMeta=void 0,this.isAsyncPlaceholder=!1},ve={child:{configurable:!0}};ve.child.get=function(){return this.componentInstance},Object.defineProperties(he.prototype,ve);var ge=function(e){void 0===e&&(e="");var t=new he;return t.text=e,t.isComment=!0,t};function me(e){return new he(void 0,void 0,void 0,String(e))}function ye(e){var t=new he(e.tag,e.data,e.children,e.text,e.elm,e.context,e.componentOptions,e.asyncFactory);return t.ns=e.ns,t.isStatic=e.isStatic,t.key=e.key,t.isComment=e.isComment,t.fnContext=e.fnContext,t.fnOptions=e.fnOptions,t.fnScopeId=e.fnScopeId,t.isCloned=!0,t}var _e=Array.prototype,be=Object.create(_e);["push","pop","shift","unshift","splice","sort","reverse"].forEach(function(e){var t=_e[e];B(be,e,function(){for(var n=[],r=arguments.length;r--;)n[r]=arguments[r];var i,o=t.apply(this,n),a=this.__ob__;switch(e){case"push":case"unshift":i=n;break;case"splice":i=n.slice(2)}return i&&a.observeArray(i),a.dep.notify(),o})});var we=Object.getOwnPropertyNames(be),xe=!0;function Ce(e){xe=e}var Ee=function(e){(this.value=e,this.dep=new le,this.vmCount=0,B(e,"__ob__",this),Array.isArray(e))?((z?Te:Ae)(e,be,we),this.observeArray(e)):this.walk(e)};function Te(e,t,n){e.__proto__=t}function Ae(e,t,n){for(var r=0,i=n.length;r<i;r++){var o=n[r];B(e,o,t[o])}}function Se(e,t){var n;if(u(e)&&!(e instanceof he))return b(e,"__ob__")&&e.__ob__ instanceof Ee?n=e.__ob__:xe&&!re()&&(Array.isArray(e)||l(e))&&Object.isExtensible(e)&&!e._isVue&&(n=new Ee(e)),t&&n&&n.vmCount++,n}function ke(e,t,n,r,i){var o=new le,a=Object.getOwnPropertyDescriptor(e,t);if(!a||!1!==a.configurable){var s=a&&a.get;s||2!==arguments.length||(n=e[t]);var u=a&&a.set,c=!i&&Se(n);Object.defineProperty(e,t,{enumerable:!0,configurable:!0,get:function(){var t=s?s.call(e):n;return le.target&&(o.depend(),c&&(c.dep.depend(),Array.isArray(t)&&function e(t){for(var n=void 0,r=0,i=t.length;r<i;r++)(n=t[r])&&n.__ob__&&n.__ob__.dep.depend(),Array.isArray(n)&&e(n)}(t))),t},set:function(t){var r=s?s.call(e):n;t===r||t!=t&&r!=r||(u?u.call(e,t):n=t,c=!i&&Se(t),o.notify())}})}}function Oe(e,t,n){if(Array.isArray(e)&&p(t))return e.length=Math.max(e.length,t),e.splice(t,1,n),n;if(t in e&&!(t in Object.prototype))return e[t]=n,n;var r=e.__ob__;return e._isVue||r&&r.vmCount?n:r?(ke(r.value,t,n),r.dep.notify(),n):(e[t]=n,n)}function De(e,t){if(Array.isArray(e)&&p(t))e.splice(t,1);else{var n=e.__ob__;e._isVue||n&&n.vmCount||b(e,t)&&(delete e[t],n&&n.dep.notify())}}Ee.prototype.walk=function(e){for(var t=Object.keys(e),n=0;n<t.length;n++)ke(e,t[n])},Ee.prototype.observeArray=function(e){for(var t=0,n=e.length;t<n;t++)Se(e[t])};var Ie=F.optionMergeStrategies;function Ne(e,t){if(!t)return e;for(var n,r,i,o=Object.keys(t),a=0;a<o.length;a++)r=e[n=o[a]],i=t[n],b(e,n)?l(r)&&l(i)&&Ne(r,i):Oe(e,n,i);return e}function je(e,t,n){return n?function(){var r="function"==typeof t?t.call(n,n):t,i="function"==typeof e?e.call(n,n):e;return r?Ne(r,i):i}:t?e?function(){return Ne("function"==typeof t?t.call(this,this):t,"function"==typeof e?e.call(this,this):e)}:t:e}function Le(e,t){return t?e?e.concat(t):Array.isArray(t)?t:[t]:e}function $e(e,t,n,r){var i=Object.create(e||null);return t?O(i,t):i}Ie.data=function(e,t,n){return n?je(e,t,n):t&&"function"!=typeof t?e:je(e,t)},H.forEach(function(e){Ie[e]=Le}),M.forEach(function(e){Ie[e+"s"]=$e}),Ie.watch=function(e,t,n,r){if(e===ee&&(e=void 0),t===ee&&(t=void 0),!t)return Object.create(e||null);if(!e)return t;var i={};for(var o in O(i,e),t){var a=i[o],s=t[o];a&&!Array.isArray(a)&&(a=[a]),i[o]=a?a.concat(s):Array.isArray(s)?s:[s]}return i},Ie.props=Ie.methods=Ie.inject=Ie.computed=function(e,t,n,r){if(!e)return t;var i=Object.create(null);return O(i,e),t&&O(i,t),i},Ie.provide=je;var Pe=function(e,t){return void 0===t?e:t};function Re(e,t,n){"function"==typeof t&&(t=t.options),function(e,t){var n=e.props;if(n){var r,i,o={};if(Array.isArray(n))for(r=n.length;r--;)"string"==typeof(i=n[r])&&(o[C(i)]={type:null});else if(l(n))for(var a in n)i=n[a],o[C(a)]=l(i)?i:{type:i};e.props=o}}(t),function(e,t){var n=e.inject;if(n){var r=e.inject={};if(Array.isArray(n))for(var i=0;i<n.length;i++)r[n[i]]={from:n[i]};else if(l(n))for(var o in n){var a=n[o];r[o]=l(a)?O({from:o},a):{from:a}}}}(t),function(e){var t=e.directives;if(t)for(var n in t){var r=t[n];"function"==typeof r&&(t[n]={bind:r,update:r})}}(t);var r=t.extends;if(r&&(e=Re(e,r,n)),t.mixins)for(var i=0,o=t.mixins.length;i<o;i++)e=Re(e,t.mixins[i],n);var a,s={};for(a in e)u(a);for(a in t)b(e,a)||u(a);function u(r){var i=Ie[r]||Pe;s[r]=i(e[r],t[r],n,r)}return s}function Me(e,t,n,r){if("string"==typeof n){var i=e[t];if(b(i,n))return i[n];var o=C(n);if(b(i,o))return i[o];var a=E(o);return b(i,a)?i[a]:i[n]||i[o]||i[a]}}function He(e,t,n,r){var i=t[e],o=!b(n,e),a=n[e],s=Be(Boolean,i.type);if(s>-1)if(o&&!b(i,"default"))a=!1;else if(""===a||a===A(e)){var u=Be(String,i.type);(u<0||s<u)&&(a=!0)}if(void 0===a){a=function(e,t,n){if(!b(t,"default"))return;var r=t.default;0;if(e&&e.$options.propsData&&void 0===e.$options.propsData[n]&&void 0!==e._props[n])return e._props[n];return"function"==typeof r&&"Function"!==Fe(t.type)?r.call(e):r}(r,i,e);var c=xe;Ce(!0),Se(a),Ce(c)}return a}function Fe(e){var t=e&&e.toString().match(/^\s*function (\w+)/);return t?t[1]:""}function qe(e,t){return Fe(e)===Fe(t)}function Be(e,t){if(!Array.isArray(t))return qe(t,e)?0:-1;for(var n=0,r=t.length;n<r;n++)if(qe(t[n],e))return n;return-1}function We(e,t,n){if(t)for(var r=t;r=r.$parent;){var i=r.$options.errorCaptured;if(i)for(var o=0;o<i.length;o++)try{if(!1===i[o].call(r,e,t,n))return}catch(e){Ue(e,r,"errorCaptured hook")}}Ue(e,t,n)}function Ue(e,t,n){if(F.errorHandler)try{return F.errorHandler.call(null,e,t,n)}catch(e){ze(e,null,"config.errorHandler")}ze(e,t,n)}function ze(e,t,n){if(!V&&!K||"undefined"==typeof console)throw e;console.error(e)}var Ve,Ke,Qe=[],Ye=!1;function Xe(){Ye=!1;var e=Qe.slice(0);Qe.length=0;for(var t=0;t<e.length;t++)e[t]()}var Ge=!1;if(void 0!==n&&oe(n))Ke=function(){n(Xe)};else if("undefined"==typeof MessageChannel||!oe(MessageChannel)&&"[object MessageChannelConstructor]"!==MessageChannel.toString())Ke=function(){setTimeout(Xe,0)};else{var Je=new MessageChannel,Ze=Je.port2;Je.port1.onmessage=Xe,Ke=function(){Ze.postMessage(1)}}if("undefined"!=typeof Promise&&oe(Promise)){var et=Promise.resolve();Ve=function(){et.then(Xe),Z&&setTimeout(I)}}else Ve=Ke;function tt(e,t){var n;if(Qe.push(function(){if(e)try{e.call(t)}catch(e){We(e,t,"nextTick")}else n&&n(t)}),Ye||(Ye=!0,Ge?Ke():Ve()),!e&&"undefined"!=typeof Promise)return new Promise(function(e){n=e})}var nt=new ae;function rt(e){!function e(t,n){var r,i;var o=Array.isArray(t);if(!o&&!u(t)||Object.isFrozen(t)||t instanceof he)return;if(t.__ob__){var a=t.__ob__.dep.id;if(n.has(a))return;n.add(a)}if(o)for(r=t.length;r--;)e(t[r],n);else for(i=Object.keys(t),r=i.length;r--;)e(t[i[r]],n)}(e,nt),nt.clear()}var it,ot=w(function(e){var t="&"===e.charAt(0),n="~"===(e=t?e.slice(1):e).charAt(0),r="!"===(e=n?e.slice(1):e).charAt(0);return{name:e=r?e.slice(1):e,once:n,capture:r,passive:t}});function at(e){function t(){var e=arguments,n=t.fns;if(!Array.isArray(n))return n.apply(null,arguments);for(var r=n.slice(),i=0;i<r.length;i++)r[i].apply(null,e)}return t.fns=e,t}function st(e,t,n,r,o){var a,s,u,c;for(a in e)s=e[a],u=t[a],c=ot(a),i(s)||(i(u)?(i(s.fns)&&(s=e[a]=at(s)),n(c.name,s,c.once,c.capture,c.passive,c.params)):s!==u&&(u.fns=s,e[a]=u));for(a in t)i(e[a])&&r((c=ot(a)).name,t[a],c.capture)}function ut(e,t,n){var r;e instanceof he&&(e=e.data.hook||(e.data.hook={}));var s=e[t];function u(){n.apply(this,arguments),y(r.fns,u)}i(s)?r=at([u]):o(s.fns)&&a(s.merged)?(r=s).fns.push(u):r=at([s,u]),r.merged=!0,e[t]=r}function ct(e,t,n,r,i){if(o(t)){if(b(t,n))return e[n]=t[n],i||delete t[n],!0;if(b(t,r))return e[n]=t[r],i||delete t[r],!0}return!1}function lt(e){return s(e)?[me(e)]:Array.isArray(e)?function e(t,n){var r=[];var u,c,l,f;for(u=0;u<t.length;u++)i(c=t[u])||"boolean"==typeof c||(l=r.length-1,f=r[l],Array.isArray(c)?c.length>0&&(ft((c=e(c,(n||"")+"_"+u))[0])&&ft(f)&&(r[l]=me(f.text+c[0].text),c.shift()),r.push.apply(r,c)):s(c)?ft(f)?r[l]=me(f.text+c):""!==c&&r.push(me(c)):ft(c)&&ft(f)?r[l]=me(f.text+c.text):(a(t._isVList)&&o(c.tag)&&i(c.key)&&o(n)&&(c.key="__vlist"+n+"_"+u+"__"),r.push(c)));return r}(e):void 0}function ft(e){return o(e)&&o(e.text)&&!1===e.isComment}function pt(e,t){return(e.__esModule||se&&"Module"===e[Symbol.toStringTag])&&(e=e.default),u(e)?t.extend(e):e}function dt(e){return e.isComment&&e.asyncFactory}function ht(e){if(Array.isArray(e))for(var t=0;t<e.length;t++){var n=e[t];if(o(n)&&(o(n.componentOptions)||dt(n)))return n}}function vt(e,t,n){n?it.$once(e,t):it.$on(e,t)}function gt(e,t){it.$off(e,t)}function mt(e,t,n){it=e,st(t,n||{},vt,gt),it=void 0}function yt(e,t){var n={};if(!e)return n;for(var r=0,i=e.length;r<i;r++){var o=e[r],a=o.data;if(a&&a.attrs&&a.attrs.slot&&delete a.attrs.slot,o.context!==t&&o.fnContext!==t||!a||null==a.slot)(n.default||(n.default=[])).push(o);else{var s=a.slot,u=n[s]||(n[s]=[]);"template"===o.tag?u.push.apply(u,o.children||[]):u.push(o)}}for(var c in n)n[c].every(_t)&&delete n[c];return n}function _t(e){return e.isComment&&!e.asyncFactory||" "===e.text}function bt(e,t){t=t||{};for(var n=0;n<e.length;n++)Array.isArray(e[n])?bt(e[n],t):t[e[n].key]=e[n].fn;return t}var wt=null;function xt(e){for(;e&&(e=e.$parent);)if(e._inactive)return!0;return!1}function Ct(e,t){if(t){if(e._directInactive=!1,xt(e))return}else if(e._directInactive)return;if(e._inactive||null===e._inactive){e._inactive=!1;for(var n=0;n<e.$children.length;n++)Ct(e.$children[n]);Et(e,"activated")}}function Et(e,t){pe();var n=e.$options[t];if(n)for(var r=0,i=n.length;r<i;r++)try{n[r].call(e)}catch(n){We(n,e,t+" hook")}e._hasHookEvent&&e.$emit("hook:"+t),de()}var Tt=[],At=[],St={},kt=!1,Ot=!1,Dt=0;function It(){var e,t;for(Ot=!0,Tt.sort(function(e,t){return e.id-t.id}),Dt=0;Dt<Tt.length;Dt++)t=(e=Tt[Dt]).id,St[t]=null,e.run();var n=At.slice(),r=Tt.slice();Dt=Tt.length=At.length=0,St={},kt=Ot=!1,function(e){for(var t=0;t<e.length;t++)e[t]._inactive=!0,Ct(e[t],!0)}(n),function(e){var t=e.length;for(;t--;){var n=e[t],r=n.vm;r._watcher===n&&r._isMounted&&Et(r,"updated")}}(r),ie&&F.devtools&&ie.emit("flush")}var Nt=0,jt=function(e,t,n,r,i){this.vm=e,i&&(e._watcher=this),e._watchers.push(this),r?(this.deep=!!r.deep,this.user=!!r.user,this.lazy=!!r.lazy,this.sync=!!r.sync):this.deep=this.user=this.lazy=this.sync=!1,this.cb=n,this.id=++Nt,this.active=!0,this.dirty=this.lazy,this.deps=[],this.newDeps=[],this.depIds=new ae,this.newDepIds=new ae,this.expression="","function"==typeof t?this.getter=t:(this.getter=function(e){if(!W.test(e)){var t=e.split(".");return function(e){for(var n=0;n<t.length;n++){if(!e)return;e=e[t[n]]}return e}}}(t),this.getter||(this.getter=function(){})),this.value=this.lazy?void 0:this.get()};jt.prototype.get=function(){var e;pe(this);var t=this.vm;try{e=this.getter.call(t,t)}catch(e){if(!this.user)throw e;We(e,t,'getter for watcher "'+this.expression+'"')}finally{this.deep&&rt(e),de(),this.cleanupDeps()}return e},jt.prototype.addDep=function(e){var t=e.id;this.newDepIds.has(t)||(this.newDepIds.add(t),this.newDeps.push(e),this.depIds.has(t)||e.addSub(this))},jt.prototype.cleanupDeps=function(){for(var e=this.deps.length;e--;){var t=this.deps[e];this.newDepIds.has(t.id)||t.removeSub(this)}var n=this.depIds;this.depIds=this.newDepIds,this.newDepIds=n,this.newDepIds.clear(),n=this.deps,this.deps=this.newDeps,this.newDeps=n,this.newDeps.length=0},jt.prototype.update=function(){this.lazy?this.dirty=!0:this.sync?this.run():function(e){var t=e.id;if(null==St[t]){if(St[t]=!0,Ot){for(var n=Tt.length-1;n>Dt&&Tt[n].id>e.id;)n--;Tt.splice(n+1,0,e)}else Tt.push(e);kt||(kt=!0,tt(It))}}(this)},jt.prototype.run=function(){if(this.active){var e=this.get();if(e!==this.value||u(e)||this.deep){var t=this.value;if(this.value=e,this.user)try{this.cb.call(this.vm,e,t)}catch(e){We(e,this.vm,'callback for watcher "'+this.expression+'"')}else this.cb.call(this.vm,e,t)}}},jt.prototype.evaluate=function(){this.value=this.get(),this.dirty=!1},jt.prototype.depend=function(){for(var e=this.deps.length;e--;)this.deps[e].depend()},jt.prototype.teardown=function(){if(this.active){this.vm._isBeingDestroyed||y(this.vm._watchers,this);for(var e=this.deps.length;e--;)this.deps[e].removeSub(this);this.active=!1}};var Lt={enumerable:!0,configurable:!0,get:I,set:I};function $t(e,t,n){Lt.get=function(){return this[t][n]},Lt.set=function(e){this[t][n]=e},Object.defineProperty(e,n,Lt)}function Pt(e){e._watchers=[];var t=e.$options;t.props&&function(e,t){var n=e.$options.propsData||{},r=e._props={},i=e.$options._propKeys=[];e.$parent&&Ce(!1);var o=function(o){i.push(o);var a=He(o,t,n,e);ke(r,o,a),o in e||$t(e,"_props",o)};for(var a in t)o(a);Ce(!0)}(e,t.props),t.methods&&function(e,t){e.$options.props;for(var n in t)e[n]=null==t[n]?I:S(t[n],e)}(e,t.methods),t.data?function(e){var t=e.$options.data;l(t=e._data="function"==typeof t?function(e,t){pe();try{return e.call(t,t)}catch(e){return We(e,t,"data()"),{}}finally{de()}}(t,e):t||{})||(t={});var n=Object.keys(t),r=e.$options.props,i=(e.$options.methods,n.length);for(;i--;){var o=n[i];0,r&&b(r,o)||q(o)||$t(e,"_data",o)}Se(t,!0)}(e):Se(e._data={},!0),t.computed&&function(e,t){var n=e._computedWatchers=Object.create(null),r=re();for(var i in t){var o=t[i],a="function"==typeof o?o:o.get;0,r||(n[i]=new jt(e,a||I,I,Rt)),i in e||Mt(e,i,o)}}(e,t.computed),t.watch&&t.watch!==ee&&function(e,t){for(var n in t){var r=t[n];if(Array.isArray(r))for(var i=0;i<r.length;i++)Ft(e,n,r[i]);else Ft(e,n,r)}}(e,t.watch)}var Rt={lazy:!0};function Mt(e,t,n){var r=!re();"function"==typeof n?(Lt.get=r?Ht(t):n,Lt.set=I):(Lt.get=n.get?r&&!1!==n.cache?Ht(t):n.get:I,Lt.set=n.set?n.set:I),Object.defineProperty(e,t,Lt)}function Ht(e){return function(){var t=this._computedWatchers&&this._computedWatchers[e];if(t)return t.dirty&&t.evaluate(),le.target&&t.depend(),t.value}}function Ft(e,t,n,r){return l(n)&&(r=n,n=n.handler),"string"==typeof n&&(n=e[n]),e.$watch(t,n,r)}function qt(e,t){if(e){for(var n=Object.create(null),r=se?Reflect.ownKeys(e).filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}):Object.keys(e),i=0;i<r.length;i++){for(var o=r[i],a=e[o].from,s=t;s;){if(s._provided&&b(s._provided,a)){n[o]=s._provided[a];break}s=s.$parent}if(!s)if("default"in e[o]){var u=e[o].default;n[o]="function"==typeof u?u.call(t):u}else 0}return n}}function Bt(e,t){var n,r,i,a,s;if(Array.isArray(e)||"string"==typeof e)for(n=new Array(e.length),r=0,i=e.length;r<i;r++)n[r]=t(e[r],r);else if("number"==typeof e)for(n=new Array(e),r=0;r<e;r++)n[r]=t(r+1,r);else if(u(e))for(a=Object.keys(e),n=new Array(a.length),r=0,i=a.length;r<i;r++)s=a[r],n[r]=t(e[s],s,r);return o(n)&&(n._isVList=!0),n}function Wt(e,t,n,r){var i,o=this.$scopedSlots[e];if(o)n=n||{},r&&(n=O(O({},r),n)),i=o(n)||t;else{var a=this.$slots[e];a&&(a._rendered=!0),i=a||t}var s=n&&n.slot;return s?this.$createElement("template",{slot:s},i):i}function Ut(e){return Me(this.$options,"filters",e)||j}function zt(e,t){return Array.isArray(e)?-1===e.indexOf(t):e!==t}function Vt(e,t,n,r,i){var o=F.keyCodes[t]||n;return i&&r&&!F.keyCodes[t]?zt(i,r):o?zt(o,e):r?A(r)!==t:void 0}function Kt(e,t,n,r,i){if(n)if(u(n)){var o;Array.isArray(n)&&(n=D(n));var a=function(a){if("class"===a||"style"===a||m(a))o=e;else{var s=e.attrs&&e.attrs.type;o=r||F.mustUseProp(t,s,a)?e.domProps||(e.domProps={}):e.attrs||(e.attrs={})}a in o||(o[a]=n[a],i&&((e.on||(e.on={}))["update:"+a]=function(e){n[a]=e}))};for(var s in n)a(s)}else;return e}function Qt(e,t){var n=this._staticTrees||(this._staticTrees=[]),r=n[e];return r&&!t?r:(Xt(r=n[e]=this.$options.staticRenderFns[e].call(this._renderProxy,null,this),"__static__"+e,!1),r)}function Yt(e,t,n){return Xt(e,"__once__"+t+(n?"_"+n:""),!0),e}function Xt(e,t,n){if(Array.isArray(e))for(var r=0;r<e.length;r++)e[r]&&"string"!=typeof e[r]&&Gt(e[r],t+"_"+r,n);else Gt(e,t,n)}function Gt(e,t,n){e.isStatic=!0,e.key=t,e.isOnce=n}function Jt(e,t){if(t)if(l(t)){var n=e.on=e.on?O({},e.on):{};for(var r in t){var i=n[r],o=t[r];n[r]=i?[].concat(i,o):o}}else;return e}function Zt(e){e._o=Yt,e._n=h,e._s=d,e._l=Bt,e._t=Wt,e._q=L,e._i=$,e._m=Qt,e._f=Ut,e._k=Vt,e._b=Kt,e._v=me,e._e=ge,e._u=bt,e._g=Jt}function en(e,t,n,i,o){var s,u=o.options;b(i,"_uid")?(s=Object.create(i))._original=i:(s=i,i=i._original);var c=a(u._compiled),l=!c;this.data=e,this.props=t,this.children=n,this.parent=i,this.listeners=e.on||r,this.injections=qt(u.inject,i),this.slots=function(){return yt(n,i)},c&&(this.$options=u,this.$slots=this.slots(),this.$scopedSlots=e.scopedSlots||r),u._scopeId?this._c=function(e,t,n,r){var o=cn(s,e,t,n,r,l);return o&&!Array.isArray(o)&&(o.fnScopeId=u._scopeId,o.fnContext=i),o}:this._c=function(e,t,n,r){return cn(s,e,t,n,r,l)}}function tn(e,t,n,r){var i=ye(e);return i.fnContext=n,i.fnOptions=r,t.slot&&((i.data||(i.data={})).slot=t.slot),i}function nn(e,t){for(var n in t)e[C(n)]=t[n]}Zt(en.prototype);var rn={init:function(e,t,n,r){if(e.componentInstance&&!e.componentInstance._isDestroyed&&e.data.keepAlive){var i=e;rn.prepatch(i,i)}else{(e.componentInstance=function(e,t,n,r){var i={_isComponent:!0,parent:t,_parentVnode:e,_parentElm:n||null,_refElm:r||null},a=e.data.inlineTemplate;o(a)&&(i.render=a.render,i.staticRenderFns=a.staticRenderFns);return new e.componentOptions.Ctor(i)}(e,wt,n,r)).$mount(t?e.elm:void 0,t)}},prepatch:function(e,t){var n=t.componentOptions;!function(e,t,n,i,o){var a=!!(o||e.$options._renderChildren||i.data.scopedSlots||e.$scopedSlots!==r);if(e.$options._parentVnode=i,e.$vnode=i,e._vnode&&(e._vnode.parent=i),e.$options._renderChildren=o,e.$attrs=i.data.attrs||r,e.$listeners=n||r,t&&e.$options.props){Ce(!1);for(var s=e._props,u=e.$options._propKeys||[],c=0;c<u.length;c++){var l=u[c],f=e.$options.props;s[l]=He(l,f,t,e)}Ce(!0),e.$options.propsData=t}n=n||r;var p=e.$options._parentListeners;e.$options._parentListeners=n,mt(e,n,p),a&&(e.$slots=yt(o,i.context),e.$forceUpdate())}(t.componentInstance=e.componentInstance,n.propsData,n.listeners,t,n.children)},insert:function(e){var t,n=e.context,r=e.componentInstance;r._isMounted||(r._isMounted=!0,Et(r,"mounted")),e.data.keepAlive&&(n._isMounted?((t=r)._inactive=!1,At.push(t)):Ct(r,!0))},destroy:function(e){var t=e.componentInstance;t._isDestroyed||(e.data.keepAlive?function e(t,n){if(!(n&&(t._directInactive=!0,xt(t))||t._inactive)){t._inactive=!0;for(var r=0;r<t.$children.length;r++)e(t.$children[r]);Et(t,"deactivated")}}(t,!0):t.$destroy())}},on=Object.keys(rn);function an(e,t,n,s,c){if(!i(e)){var l=n.$options._base;if(u(e)&&(e=l.extend(e)),"function"==typeof e){var f;if(i(e.cid)&&void 0===(e=function(e,t,n){if(a(e.error)&&o(e.errorComp))return e.errorComp;if(o(e.resolved))return e.resolved;if(a(e.loading)&&o(e.loadingComp))return e.loadingComp;if(!o(e.contexts)){var r=e.contexts=[n],s=!0,c=function(){for(var e=0,t=r.length;e<t;e++)r[e].$forceUpdate()},l=P(function(n){e.resolved=pt(n,t),s||c()}),f=P(function(t){o(e.errorComp)&&(e.error=!0,c())}),p=e(l,f);return u(p)&&("function"==typeof p.then?i(e.resolved)&&p.then(l,f):o(p.component)&&"function"==typeof p.component.then&&(p.component.then(l,f),o(p.error)&&(e.errorComp=pt(p.error,t)),o(p.loading)&&(e.loadingComp=pt(p.loading,t),0===p.delay?e.loading=!0:setTimeout(function(){i(e.resolved)&&i(e.error)&&(e.loading=!0,c())},p.delay||200)),o(p.timeout)&&setTimeout(function(){i(e.resolved)&&f(null)},p.timeout))),s=!1,e.loading?e.loadingComp:e.resolved}e.contexts.push(n)}(f=e,l,n)))return function(e,t,n,r,i){var o=ge();return o.asyncFactory=e,o.asyncMeta={data:t,context:n,children:r,tag:i},o}(f,t,n,s,c);t=t||{},fn(e),o(t.model)&&function(e,t){var n=e.model&&e.model.prop||"value",r=e.model&&e.model.event||"input";(t.props||(t.props={}))[n]=t.model.value;var i=t.on||(t.on={});o(i[r])?i[r]=[t.model.callback].concat(i[r]):i[r]=t.model.callback}(e.options,t);var p=function(e,t,n){var r=t.options.props;if(!i(r)){var a={},s=e.attrs,u=e.props;if(o(s)||o(u))for(var c in r){var l=A(c);ct(a,u,c,l,!0)||ct(a,s,c,l,!1)}return a}}(t,e);if(a(e.options.functional))return function(e,t,n,i,a){var s=e.options,u={},c=s.props;if(o(c))for(var l in c)u[l]=He(l,c,t||r);else o(n.attrs)&&nn(u,n.attrs),o(n.props)&&nn(u,n.props);var f=new en(n,u,a,i,e),p=s.render.call(null,f._c,f);if(p instanceof he)return tn(p,n,f.parent,s);if(Array.isArray(p)){for(var d=lt(p)||[],h=new Array(d.length),v=0;v<d.length;v++)h[v]=tn(d[v],n,f.parent,s);return h}}(e,p,t,n,s);var d=t.on;if(t.on=t.nativeOn,a(e.options.abstract)){var h=t.slot;t={},h&&(t.slot=h)}!function(e){for(var t=e.hook||(e.hook={}),n=0;n<on.length;n++){var r=on[n];t[r]=rn[r]}}(t);var v=e.options.name||c;return new he("vue-component-"+e.cid+(v?"-"+v:""),t,void 0,void 0,void 0,n,{Ctor:e,propsData:p,listeners:d,tag:c,children:s},f)}}}var sn=1,un=2;function cn(e,t,n,r,c,l){return(Array.isArray(n)||s(n))&&(c=r,r=n,n=void 0),a(l)&&(c=un),function(e,t,n,r,s){if(o(n)&&o(n.__ob__))return ge();o(n)&&o(n.is)&&(t=n.is);if(!t)return ge();0;Array.isArray(r)&&"function"==typeof r[0]&&((n=n||{}).scopedSlots={default:r[0]},r.length=0);s===un?r=lt(r):s===sn&&(r=function(e){for(var t=0;t<e.length;t++)if(Array.isArray(e[t]))return Array.prototype.concat.apply([],e);return e}(r));var c,l;if("string"==typeof t){var f;l=e.$vnode&&e.$vnode.ns||F.getTagNamespace(t),c=F.isReservedTag(t)?new he(F.parsePlatformTagName(t),n,r,void 0,void 0,e):o(f=Me(e.$options,"components",t))?an(f,n,e,r,t):new he(t,n,r,void 0,void 0,e)}else c=an(t,n,e,r);return Array.isArray(c)?c:o(c)?(o(l)&&function e(t,n,r){t.ns=n;"foreignObject"===t.tag&&(n=void 0,r=!0);if(o(t.children))for(var s=0,u=t.children.length;s<u;s++){var c=t.children[s];o(c.tag)&&(i(c.ns)||a(r)&&"svg"!==c.tag)&&e(c,n,r)}}(c,l),o(n)&&function(e){u(e.style)&&rt(e.style);u(e.class)&&rt(e.class)}(n),c):ge()}(e,t,n,r,c)}var ln=0;function fn(e){var t=e.options;if(e.super){var n=fn(e.super);if(n!==e.superOptions){e.superOptions=n;var r=function(e){var t,n=e.options,r=e.extendOptions,i=e.sealedOptions;for(var o in n)n[o]!==i[o]&&(t||(t={}),t[o]=pn(n[o],r[o],i[o]));return t}(e);r&&O(e.extendOptions,r),(t=e.options=Re(n,e.extendOptions)).name&&(t.components[t.name]=e)}}return t}function pn(e,t,n){if(Array.isArray(e)){var r=[];n=Array.isArray(n)?n:[n],t=Array.isArray(t)?t:[t];for(var i=0;i<e.length;i++)(t.indexOf(e[i])>=0||n.indexOf(e[i])<0)&&r.push(e[i]);return r}return e}function dn(e){this._init(e)}function hn(e){e.cid=0;var t=1;e.extend=function(e){e=e||{};var n=this,r=n.cid,i=e._Ctor||(e._Ctor={});if(i[r])return i[r];var o=e.name||n.options.name;var a=function(e){this._init(e)};return(a.prototype=Object.create(n.prototype)).constructor=a,a.cid=t++,a.options=Re(n.options,e),a.super=n,a.options.props&&function(e){var t=e.options.props;for(var n in t)$t(e.prototype,"_props",n)}(a),a.options.computed&&function(e){var t=e.options.computed;for(var n in t)Mt(e.prototype,n,t[n])}(a),a.extend=n.extend,a.mixin=n.mixin,a.use=n.use,M.forEach(function(e){a[e]=n[e]}),o&&(a.options.components[o]=a),a.superOptions=n.options,a.extendOptions=e,a.sealedOptions=O({},a.options),i[r]=a,a}}function vn(e){return e&&(e.Ctor.options.name||e.tag)}function gn(e,t){return Array.isArray(e)?e.indexOf(t)>-1:"string"==typeof e?e.split(",").indexOf(t)>-1:!!f(e)&&e.test(t)}function mn(e,t){var n=e.cache,r=e.keys,i=e._vnode;for(var o in n){var a=n[o];if(a){var s=vn(a.componentOptions);s&&!t(s)&&yn(n,o,r,i)}}}function yn(e,t,n,r){var i=e[t];!i||r&&i.tag===r.tag||i.componentInstance.$destroy(),e[t]=null,y(n,t)}!function(e){e.prototype._init=function(e){var t=this;t._uid=ln++,t._isVue=!0,e&&e._isComponent?function(e,t){var n=e.$options=Object.create(e.constructor.options),r=t._parentVnode;n.parent=t.parent,n._parentVnode=r,n._parentElm=t._parentElm,n._refElm=t._refElm;var i=r.componentOptions;n.propsData=i.propsData,n._parentListeners=i.listeners,n._renderChildren=i.children,n._componentTag=i.tag,t.render&&(n.render=t.render,n.staticRenderFns=t.staticRenderFns)}(t,e):t.$options=Re(fn(t.constructor),e||{},t),t._renderProxy=t,t._self=t,function(e){var t=e.$options,n=t.parent;if(n&&!t.abstract){for(;n.$options.abstract&&n.$parent;)n=n.$parent;n.$children.push(e)}e.$parent=n,e.$root=n?n.$root:e,e.$children=[],e.$refs={},e._watcher=null,e._inactive=null,e._directInactive=!1,e._isMounted=!1,e._isDestroyed=!1,e._isBeingDestroyed=!1}(t),function(e){e._events=Object.create(null),e._hasHookEvent=!1;var t=e.$options._parentListeners;t&&mt(e,t)}(t),function(e){e._vnode=null,e._staticTrees=null;var t=e.$options,n=e.$vnode=t._parentVnode,i=n&&n.context;e.$slots=yt(t._renderChildren,i),e.$scopedSlots=r,e._c=function(t,n,r,i){return cn(e,t,n,r,i,!1)},e.$createElement=function(t,n,r,i){return cn(e,t,n,r,i,!0)};var o=n&&n.data;ke(e,"$attrs",o&&o.attrs||r,null,!0),ke(e,"$listeners",t._parentListeners||r,null,!0)}(t),Et(t,"beforeCreate"),function(e){var t=qt(e.$options.inject,e);t&&(Ce(!1),Object.keys(t).forEach(function(n){ke(e,n,t[n])}),Ce(!0))}(t),Pt(t),function(e){var t=e.$options.provide;t&&(e._provided="function"==typeof t?t.call(e):t)}(t),Et(t,"created"),t.$options.el&&t.$mount(t.$options.el)}}(dn),function(e){var t={get:function(){return this._data}},n={get:function(){return this._props}};Object.defineProperty(e.prototype,"$data",t),Object.defineProperty(e.prototype,"$props",n),e.prototype.$set=Oe,e.prototype.$delete=De,e.prototype.$watch=function(e,t,n){if(l(t))return Ft(this,e,t,n);(n=n||{}).user=!0;var r=new jt(this,e,t,n);return n.immediate&&t.call(this,r.value),function(){r.teardown()}}}(dn),function(e){var t=/^hook:/;e.prototype.$on=function(e,n){if(Array.isArray(e))for(var r=0,i=e.length;r<i;r++)this.$on(e[r],n);else(this._events[e]||(this._events[e]=[])).push(n),t.test(e)&&(this._hasHookEvent=!0);return this},e.prototype.$once=function(e,t){var n=this;function r(){n.$off(e,r),t.apply(n,arguments)}return r.fn=t,n.$on(e,r),n},e.prototype.$off=function(e,t){var n=this;if(!arguments.length)return n._events=Object.create(null),n;if(Array.isArray(e)){for(var r=0,i=e.length;r<i;r++)this.$off(e[r],t);return n}var o=n._events[e];if(!o)return n;if(!t)return n._events[e]=null,n;if(t)for(var a,s=o.length;s--;)if((a=o[s])===t||a.fn===t){o.splice(s,1);break}return n},e.prototype.$emit=function(e){var t=this,n=t._events[e];if(n){n=n.length>1?k(n):n;for(var r=k(arguments,1),i=0,o=n.length;i<o;i++)try{n[i].apply(t,r)}catch(n){We(n,t,'event handler for "'+e+'"')}}return t}}(dn),function(e){e.prototype._update=function(e,t){var n=this;n._isMounted&&Et(n,"beforeUpdate");var r=n.$el,i=n._vnode,o=wt;wt=n,n._vnode=e,i?n.$el=n.__patch__(i,e):(n.$el=n.__patch__(n.$el,e,t,!1,n.$options._parentElm,n.$options._refElm),n.$options._parentElm=n.$options._refElm=null),wt=o,r&&(r.__vue__=null),n.$el&&(n.$el.__vue__=n),n.$vnode&&n.$parent&&n.$vnode===n.$parent._vnode&&(n.$parent.$el=n.$el)},e.prototype.$forceUpdate=function(){this._watcher&&this._watcher.update()},e.prototype.$destroy=function(){var e=this;if(!e._isBeingDestroyed){Et(e,"beforeDestroy"),e._isBeingDestroyed=!0;var t=e.$parent;!t||t._isBeingDestroyed||e.$options.abstract||y(t.$children,e),e._watcher&&e._watcher.teardown();for(var n=e._watchers.length;n--;)e._watchers[n].teardown();e._data.__ob__&&e._data.__ob__.vmCount--,e._isDestroyed=!0,e.__patch__(e._vnode,null),Et(e,"destroyed"),e.$off(),e.$el&&(e.$el.__vue__=null),e.$vnode&&(e.$vnode.parent=null)}}}(dn),function(e){Zt(e.prototype),e.prototype.$nextTick=function(e){return tt(e,this)},e.prototype._render=function(){var e,t=this,n=t.$options,i=n.render,o=n._parentVnode;o&&(t.$scopedSlots=o.data.scopedSlots||r),t.$vnode=o;try{e=i.call(t._renderProxy,t.$createElement)}catch(n){We(n,t,"render"),e=t._vnode}return e instanceof he||(e=ge()),e.parent=o,e}}(dn);var _n=[String,RegExp,Array],bn={KeepAlive:{name:"keep-alive",abstract:!0,props:{include:_n,exclude:_n,max:[String,Number]},created:function(){this.cache=Object.create(null),this.keys=[]},destroyed:function(){for(var e in this.cache)yn(this.cache,e,this.keys)},mounted:function(){var e=this;this.$watch("include",function(t){mn(e,function(e){return gn(t,e)})}),this.$watch("exclude",function(t){mn(e,function(e){return!gn(t,e)})})},render:function(){var e=this.$slots.default,t=ht(e),n=t&&t.componentOptions;if(n){var r=vn(n),i=this.include,o=this.exclude;if(i&&(!r||!gn(i,r))||o&&r&&gn(o,r))return t;var a=this.cache,s=this.keys,u=null==t.key?n.Ctor.cid+(n.tag?"::"+n.tag:""):t.key;a[u]?(t.componentInstance=a[u].componentInstance,y(s,u),s.push(u)):(a[u]=t,s.push(u),this.max&&s.length>parseInt(this.max)&&yn(a,s[0],s,this._vnode)),t.data.keepAlive=!0}return t||e&&e[0]}}};!function(e){var t={get:function(){return F}};Object.defineProperty(e,"config",t),e.util={warn:ue,extend:O,mergeOptions:Re,defineReactive:ke},e.set=Oe,e.delete=De,e.nextTick=tt,e.options=Object.create(null),M.forEach(function(t){e.options[t+"s"]=Object.create(null)}),e.options._base=e,O(e.options.components,bn),function(e){e.use=function(e){var t=this._installedPlugins||(this._installedPlugins=[]);if(t.indexOf(e)>-1)return this;var n=k(arguments,1);return n.unshift(this),"function"==typeof e.install?e.install.apply(e,n):"function"==typeof e&&e.apply(null,n),t.push(e),this}}(e),function(e){e.mixin=function(e){return this.options=Re(this.options,e),this}}(e),hn(e),function(e){M.forEach(function(t){e[t]=function(e,n){return n?("component"===t&&l(n)&&(n.name=n.name||e,n=this.options._base.extend(n)),"directive"===t&&"function"==typeof n&&(n={bind:n,update:n}),this.options[t+"s"][e]=n,n):this.options[t+"s"][e]}})}(e)}(dn),Object.defineProperty(dn.prototype,"$isServer",{get:re}),Object.defineProperty(dn.prototype,"$ssrContext",{get:function(){return this.$vnode&&this.$vnode.ssrContext}}),Object.defineProperty(dn,"FunctionalRenderContext",{value:en}),dn.version="2.5.16";var wn=v("style,class"),xn=v("input,textarea,option,select,progress"),Cn=function(e,t,n){return"value"===n&&xn(e)&&"button"!==t||"selected"===n&&"option"===e||"checked"===n&&"input"===e||"muted"===n&&"video"===e},En=v("contenteditable,draggable,spellcheck"),Tn=v("allowfullscreen,async,autofocus,autoplay,checked,compact,controls,declare,default,defaultchecked,defaultmuted,defaultselected,defer,disabled,enabled,formnovalidate,hidden,indeterminate,inert,ismap,itemscope,loop,multiple,muted,nohref,noresize,noshade,novalidate,nowrap,open,pauseonexit,readonly,required,reversed,scoped,seamless,selected,sortable,translate,truespeed,typemustmatch,visible"),An="http://www.w3.org/1999/xlink",Sn=function(e){return":"===e.charAt(5)&&"xlink"===e.slice(0,5)},kn=function(e){return Sn(e)?e.slice(6,e.length):""},On=function(e){return null==e||!1===e};function Dn(e){for(var t=e.data,n=e,r=e;o(r.componentInstance);)(r=r.componentInstance._vnode)&&r.data&&(t=In(r.data,t));for(;o(n=n.parent);)n&&n.data&&(t=In(t,n.data));return function(e,t){if(o(e)||o(t))return Nn(e,jn(t));return""}(t.staticClass,t.class)}function In(e,t){return{staticClass:Nn(e.staticClass,t.staticClass),class:o(e.class)?[e.class,t.class]:t.class}}function Nn(e,t){return e?t?e+" "+t:e:t||""}function jn(e){return Array.isArray(e)?function(e){for(var t,n="",r=0,i=e.length;r<i;r++)o(t=jn(e[r]))&&""!==t&&(n&&(n+=" "),n+=t);return n}(e):u(e)?function(e){var t="";for(var n in e)e[n]&&(t&&(t+=" "),t+=n);return t}(e):"string"==typeof e?e:""}var Ln={svg:"http://www.w3.org/2000/svg",math:"http://www.w3.org/1998/Math/MathML"},$n=v("html,body,base,head,link,meta,style,title,address,article,aside,footer,header,h1,h2,h3,h4,h5,h6,hgroup,nav,section,div,dd,dl,dt,figcaption,figure,picture,hr,img,li,main,ol,p,pre,ul,a,b,abbr,bdi,bdo,br,cite,code,data,dfn,em,i,kbd,mark,q,rp,rt,rtc,ruby,s,samp,small,span,strong,sub,sup,time,u,var,wbr,area,audio,map,track,video,embed,object,param,source,canvas,script,noscript,del,ins,caption,col,colgroup,table,thead,tbody,td,th,tr,button,datalist,fieldset,form,input,label,legend,meter,optgroup,option,output,progress,select,textarea,details,dialog,menu,menuitem,summary,content,element,shadow,template,blockquote,iframe,tfoot"),Pn=v("svg,animate,circle,clippath,cursor,defs,desc,ellipse,filter,font-face,foreignObject,g,glyph,image,line,marker,mask,missing-glyph,path,pattern,polygon,polyline,rect,switch,symbol,text,textpath,tspan,use,view",!0),Rn=function(e){return $n(e)||Pn(e)};function Mn(e){return Pn(e)?"svg":"math"===e?"math":void 0}var Hn=Object.create(null);var Fn=v("text,number,password,search,email,tel,url");function qn(e){if("string"==typeof e){var t=document.querySelector(e);return t||document.createElement("div")}return e}var Bn=Object.freeze({createElement:function(e,t){var n=document.createElement(e);return"select"!==e?n:(t.data&&t.data.attrs&&void 0!==t.data.attrs.multiple&&n.setAttribute("multiple","multiple"),n)},createElementNS:function(e,t){return document.createElementNS(Ln[e],t)},createTextNode:function(e){return document.createTextNode(e)},createComment:function(e){return document.createComment(e)},insertBefore:function(e,t,n){e.insertBefore(t,n)},removeChild:function(e,t){e.removeChild(t)},appendChild:function(e,t){e.appendChild(t)},parentNode:function(e){return e.parentNode},nextSibling:function(e){return e.nextSibling},tagName:function(e){return e.tagName},setTextContent:function(e,t){e.textContent=t},setStyleScope:function(e,t){e.setAttribute(t,"")}}),Wn={create:function(e,t){Un(t)},update:function(e,t){e.data.ref!==t.data.ref&&(Un(e,!0),Un(t))},destroy:function(e){Un(e,!0)}};function Un(e,t){var n=e.data.ref;if(o(n)){var r=e.context,i=e.componentInstance||e.elm,a=r.$refs;t?Array.isArray(a[n])?y(a[n],i):a[n]===i&&(a[n]=void 0):e.data.refInFor?Array.isArray(a[n])?a[n].indexOf(i)<0&&a[n].push(i):a[n]=[i]:a[n]=i}}var zn=new he("",{},[]),Vn=["create","activate","update","remove","destroy"];function Kn(e,t){return e.key===t.key&&(e.tag===t.tag&&e.isComment===t.isComment&&o(e.data)===o(t.data)&&function(e,t){if("input"!==e.tag)return!0;var n,r=o(n=e.data)&&o(n=n.attrs)&&n.type,i=o(n=t.data)&&o(n=n.attrs)&&n.type;return r===i||Fn(r)&&Fn(i)}(e,t)||a(e.isAsyncPlaceholder)&&e.asyncFactory===t.asyncFactory&&i(t.asyncFactory.error))}function Qn(e,t,n){var r,i,a={};for(r=t;r<=n;++r)o(i=e[r].key)&&(a[i]=r);return a}var Yn={create:Xn,update:Xn,destroy:function(e){Xn(e,zn)}};function Xn(e,t){(e.data.directives||t.data.directives)&&function(e,t){var n,r,i,o=e===zn,a=t===zn,s=Jn(e.data.directives,e.context),u=Jn(t.data.directives,t.context),c=[],l=[];for(n in u)r=s[n],i=u[n],r?(i.oldValue=r.value,er(i,"update",t,e),i.def&&i.def.componentUpdated&&l.push(i)):(er(i,"bind",t,e),i.def&&i.def.inserted&&c.push(i));if(c.length){var f=function(){for(var n=0;n<c.length;n++)er(c[n],"inserted",t,e)};o?ut(t,"insert",f):f()}l.length&&ut(t,"postpatch",function(){for(var n=0;n<l.length;n++)er(l[n],"componentUpdated",t,e)});if(!o)for(n in s)u[n]||er(s[n],"unbind",e,e,a)}(e,t)}var Gn=Object.create(null);function Jn(e,t){var n,r,i=Object.create(null);if(!e)return i;for(n=0;n<e.length;n++)(r=e[n]).modifiers||(r.modifiers=Gn),i[Zn(r)]=r,r.def=Me(t.$options,"directives",r.name);return i}function Zn(e){return e.rawName||e.name+"."+Object.keys(e.modifiers||{}).join(".")}function er(e,t,n,r,i){var o=e.def&&e.def[t];if(o)try{o(n.elm,e,n,r,i)}catch(r){We(r,n.context,"directive "+e.name+" "+t+" hook")}}var tr=[Wn,Yn];function nr(e,t){var n=t.componentOptions;if(!(o(n)&&!1===n.Ctor.options.inheritAttrs||i(e.data.attrs)&&i(t.data.attrs))){var r,a,s=t.elm,u=e.data.attrs||{},c=t.data.attrs||{};for(r in o(c.__ob__)&&(c=t.data.attrs=O({},c)),c)a=c[r],u[r]!==a&&rr(s,r,a);for(r in(X||J)&&c.value!==u.value&&rr(s,"value",c.value),u)i(c[r])&&(Sn(r)?s.removeAttributeNS(An,kn(r)):En(r)||s.removeAttribute(r))}}function rr(e,t,n){e.tagName.indexOf("-")>-1?ir(e,t,n):Tn(t)?On(n)?e.removeAttribute(t):(n="allowfullscreen"===t&&"EMBED"===e.tagName?"true":t,e.setAttribute(t,n)):En(t)?e.setAttribute(t,On(n)||"false"===n?"false":"true"):Sn(t)?On(n)?e.removeAttributeNS(An,kn(t)):e.setAttributeNS(An,t,n):ir(e,t,n)}function ir(e,t,n){if(On(n))e.removeAttribute(t);else{if(X&&!G&&"TEXTAREA"===e.tagName&&"placeholder"===t&&!e.__ieph){var r=function(t){t.stopImmediatePropagation(),e.removeEventListener("input",r)};e.addEventListener("input",r),e.__ieph=!0}e.setAttribute(t,n)}}var or={create:nr,update:nr};function ar(e,t){var n=t.elm,r=t.data,a=e.data;if(!(i(r.staticClass)&&i(r.class)&&(i(a)||i(a.staticClass)&&i(a.class)))){var s=Dn(t),u=n._transitionClasses;o(u)&&(s=Nn(s,jn(u))),s!==n._prevClass&&(n.setAttribute("class",s),n._prevClass=s)}}var sr,ur,cr,lr,fr,pr,dr={create:ar,update:ar},hr=/[\w).+\-_$\]]/;function vr(e){var t,n,r,i,o,a=!1,s=!1,u=!1,c=!1,l=0,f=0,p=0,d=0;for(r=0;r<e.length;r++)if(n=t,t=e.charCodeAt(r),a)39===t&&92!==n&&(a=!1);else if(s)34===t&&92!==n&&(s=!1);else if(u)96===t&&92!==n&&(u=!1);else if(c)47===t&&92!==n&&(c=!1);else if(124!==t||124===e.charCodeAt(r+1)||124===e.charCodeAt(r-1)||l||f||p){switch(t){case 34:s=!0;break;case 39:a=!0;break;case 96:u=!0;break;case 40:p++;break;case 41:p--;break;case 91:f++;break;case 93:f--;break;case 123:l++;break;case 125:l--}if(47===t){for(var h=r-1,v=void 0;h>=0&&" "===(v=e.charAt(h));h--);v&&hr.test(v)||(c=!0)}}else void 0===i?(d=r+1,i=e.slice(0,r).trim()):g();function g(){(o||(o=[])).push(e.slice(d,r).trim()),d=r+1}if(void 0===i?i=e.slice(0,r).trim():0!==d&&g(),o)for(r=0;r<o.length;r++)i=gr(i,o[r]);return i}function gr(e,t){var n=t.indexOf("(");if(n<0)return'_f("'+t+'")('+e+")";var r=t.slice(0,n),i=t.slice(n+1);return'_f("'+r+'")('+e+(")"!==i?","+i:i)}function mr(e){console.error("[Vue compiler]: "+e)}function yr(e,t){return e?e.map(function(e){return e[t]}).filter(function(e){return e}):[]}function _r(e,t,n){(e.props||(e.props=[])).push({name:t,value:n}),e.plain=!1}function br(e,t,n){(e.attrs||(e.attrs=[])).push({name:t,value:n}),e.plain=!1}function wr(e,t,n){e.attrsMap[t]=n,e.attrsList.push({name:t,value:n})}function xr(e,t,n,r,i,o){(e.directives||(e.directives=[])).push({name:t,rawName:n,value:r,arg:i,modifiers:o}),e.plain=!1}function Cr(e,t,n,i,o,a){var s;(i=i||r).capture&&(delete i.capture,t="!"+t),i.once&&(delete i.once,t="~"+t),i.passive&&(delete i.passive,t="&"+t),"click"===t&&(i.right?(t="contextmenu",delete i.right):i.middle&&(t="mouseup")),i.native?(delete i.native,s=e.nativeEvents||(e.nativeEvents={})):s=e.events||(e.events={});var u={value:n.trim()};i!==r&&(u.modifiers=i);var c=s[t];Array.isArray(c)?o?c.unshift(u):c.push(u):s[t]=c?o?[u,c]:[c,u]:u,e.plain=!1}function Er(e,t,n){var r=Tr(e,":"+t)||Tr(e,"v-bind:"+t);if(null!=r)return vr(r);if(!1!==n){var i=Tr(e,t);if(null!=i)return JSON.stringify(i)}}function Tr(e,t,n){var r;if(null!=(r=e.attrsMap[t]))for(var i=e.attrsList,o=0,a=i.length;o<a;o++)if(i[o].name===t){i.splice(o,1);break}return n&&delete e.attrsMap[t],r}function Ar(e,t,n){var r=n||{},i=r.number,o="$$v";r.trim&&(o="(typeof $$v === 'string'? $$v.trim(): $$v)"),i&&(o="_n("+o+")");var a=Sr(t,o);e.model={value:"("+t+")",expression:'"'+t+'"',callback:"function ($$v) {"+a+"}"}}function Sr(e,t){var n=function(e){if(e=e.trim(),sr=e.length,e.indexOf("[")<0||e.lastIndexOf("]")<sr-1)return(lr=e.lastIndexOf("."))>-1?{exp:e.slice(0,lr),key:'"'+e.slice(lr+1)+'"'}:{exp:e,key:null};ur=e,lr=fr=pr=0;for(;!Or();)Dr(cr=kr())?Nr(cr):91===cr&&Ir(cr);return{exp:e.slice(0,fr),key:e.slice(fr+1,pr)}}(e);return null===n.key?e+"="+t:"$set("+n.exp+", "+n.key+", "+t+")"}function kr(){return ur.charCodeAt(++lr)}function Or(){return lr>=sr}function Dr(e){return 34===e||39===e}function Ir(e){var t=1;for(fr=lr;!Or();)if(Dr(e=kr()))Nr(e);else if(91===e&&t++,93===e&&t--,0===t){pr=lr;break}}function Nr(e){for(var t=e;!Or()&&(e=kr())!==t;);}var jr,Lr="__r",$r="__c";function Pr(e,t,n,r,i){var o;t=(o=t)._withTask||(o._withTask=function(){Ge=!0;var e=o.apply(null,arguments);return Ge=!1,e}),n&&(t=function(e,t,n){var r=jr;return function i(){null!==e.apply(null,arguments)&&Rr(t,i,n,r)}}(t,e,r)),jr.addEventListener(e,t,te?{capture:r,passive:i}:r)}function Rr(e,t,n,r){(r||jr).removeEventListener(e,t._withTask||t,n)}function Mr(e,t){if(!i(e.data.on)||!i(t.data.on)){var n=t.data.on||{},r=e.data.on||{};jr=t.elm,function(e){if(o(e[Lr])){var t=X?"change":"input";e[t]=[].concat(e[Lr],e[t]||[]),delete e[Lr]}o(e[$r])&&(e.change=[].concat(e[$r],e.change||[]),delete e[$r])}(n),st(n,r,Pr,Rr,t.context),jr=void 0}}var Hr={create:Mr,update:Mr};function Fr(e,t){if(!i(e.data.domProps)||!i(t.data.domProps)){var n,r,a=t.elm,s=e.data.domProps||{},u=t.data.domProps||{};for(n in o(u.__ob__)&&(u=t.data.domProps=O({},u)),s)i(u[n])&&(a[n]="");for(n in u){if(r=u[n],"textContent"===n||"innerHTML"===n){if(t.children&&(t.children.length=0),r===s[n])continue;1===a.childNodes.length&&a.removeChild(a.childNodes[0])}if("value"===n){a._value=r;var c=i(r)?"":String(r);qr(a,c)&&(a.value=c)}else a[n]=r}}}function qr(e,t){return!e.composing&&("OPTION"===e.tagName||function(e,t){var n=!0;try{n=document.activeElement!==e}catch(e){}return n&&e.value!==t}(e,t)||function(e,t){var n=e.value,r=e._vModifiers;if(o(r)){if(r.lazy)return!1;if(r.number)return h(n)!==h(t);if(r.trim)return n.trim()!==t.trim()}return n!==t}(e,t))}var Br={create:Fr,update:Fr},Wr=w(function(e){var t={},n=/:(.+)/;return e.split(/;(?![^(]*\))/g).forEach(function(e){if(e){var r=e.split(n);r.length>1&&(t[r[0].trim()]=r[1].trim())}}),t});function Ur(e){var t=zr(e.style);return e.staticStyle?O(e.staticStyle,t):t}function zr(e){return Array.isArray(e)?D(e):"string"==typeof e?Wr(e):e}var Vr,Kr=/^--/,Qr=/\s*!important$/,Yr=function(e,t,n){if(Kr.test(t))e.style.setProperty(t,n);else if(Qr.test(n))e.style.setProperty(t,n.replace(Qr,""),"important");else{var r=Gr(t);if(Array.isArray(n))for(var i=0,o=n.length;i<o;i++)e.style[r]=n[i];else e.style[r]=n}},Xr=["Webkit","Moz","ms"],Gr=w(function(e){if(Vr=Vr||document.createElement("div").style,"filter"!==(e=C(e))&&e in Vr)return e;for(var t=e.charAt(0).toUpperCase()+e.slice(1),n=0;n<Xr.length;n++){var r=Xr[n]+t;if(r in Vr)return r}});function Jr(e,t){var n=t.data,r=e.data;if(!(i(n.staticStyle)&&i(n.style)&&i(r.staticStyle)&&i(r.style))){var a,s,u=t.elm,c=r.staticStyle,l=r.normalizedStyle||r.style||{},f=c||l,p=zr(t.data.style)||{};t.data.normalizedStyle=o(p.__ob__)?O({},p):p;var d=function(e,t){var n,r={};if(t)for(var i=e;i.componentInstance;)(i=i.componentInstance._vnode)&&i.data&&(n=Ur(i.data))&&O(r,n);(n=Ur(e.data))&&O(r,n);for(var o=e;o=o.parent;)o.data&&(n=Ur(o.data))&&O(r,n);return r}(t,!0);for(s in f)i(d[s])&&Yr(u,s,"");for(s in d)(a=d[s])!==f[s]&&Yr(u,s,null==a?"":a)}}var Zr={create:Jr,update:Jr};function ei(e,t){if(t&&(t=t.trim()))if(e.classList)t.indexOf(" ")>-1?t.split(/\s+/).forEach(function(t){return e.classList.add(t)}):e.classList.add(t);else{var n=" "+(e.getAttribute("class")||"")+" ";n.indexOf(" "+t+" ")<0&&e.setAttribute("class",(n+t).trim())}}function ti(e,t){if(t&&(t=t.trim()))if(e.classList)t.indexOf(" ")>-1?t.split(/\s+/).forEach(function(t){return e.classList.remove(t)}):e.classList.remove(t),e.classList.length||e.removeAttribute("class");else{for(var n=" "+(e.getAttribute("class")||"")+" ",r=" "+t+" ";n.indexOf(r)>=0;)n=n.replace(r," ");(n=n.trim())?e.setAttribute("class",n):e.removeAttribute("class")}}function ni(e){if(e){if("object"==typeof e){var t={};return!1!==e.css&&O(t,ri(e.name||"v")),O(t,e),t}return"string"==typeof e?ri(e):void 0}}var ri=w(function(e){return{enterClass:e+"-enter",enterToClass:e+"-enter-to",enterActiveClass:e+"-enter-active",leaveClass:e+"-leave",leaveToClass:e+"-leave-to",leaveActiveClass:e+"-leave-active"}}),ii=V&&!G,oi="transition",ai="animation",si="transition",ui="transitionend",ci="animation",li="animationend";ii&&(void 0===window.ontransitionend&&void 0!==window.onwebkittransitionend&&(si="WebkitTransition",ui="webkitTransitionEnd"),void 0===window.onanimationend&&void 0!==window.onwebkitanimationend&&(ci="WebkitAnimation",li="webkitAnimationEnd"));var fi=V?window.requestAnimationFrame?window.requestAnimationFrame.bind(window):setTimeout:function(e){return e()};function pi(e){fi(function(){fi(e)})}function di(e,t){var n=e._transitionClasses||(e._transitionClasses=[]);n.indexOf(t)<0&&(n.push(t),ei(e,t))}function hi(e,t){e._transitionClasses&&y(e._transitionClasses,t),ti(e,t)}function vi(e,t,n){var r=mi(e,t),i=r.type,o=r.timeout,a=r.propCount;if(!i)return n();var s=i===oi?ui:li,u=0,c=function(){e.removeEventListener(s,l),n()},l=function(t){t.target===e&&++u>=a&&c()};setTimeout(function(){u<a&&c()},o+1),e.addEventListener(s,l)}var gi=/\b(transform|all)(,|$)/;function mi(e,t){var n,r=window.getComputedStyle(e),i=r[si+"Delay"].split(", "),o=r[si+"Duration"].split(", "),a=yi(i,o),s=r[ci+"Delay"].split(", "),u=r[ci+"Duration"].split(", "),c=yi(s,u),l=0,f=0;return t===oi?a>0&&(n=oi,l=a,f=o.length):t===ai?c>0&&(n=ai,l=c,f=u.length):f=(n=(l=Math.max(a,c))>0?a>c?oi:ai:null)?n===oi?o.length:u.length:0,{type:n,timeout:l,propCount:f,hasTransform:n===oi&&gi.test(r[si+"Property"])}}function yi(e,t){for(;e.length<t.length;)e=e.concat(e);return Math.max.apply(null,t.map(function(t,n){return _i(t)+_i(e[n])}))}function _i(e){return 1e3*Number(e.slice(0,-1))}function bi(e,t){var n=e.elm;o(n._leaveCb)&&(n._leaveCb.cancelled=!0,n._leaveCb());var r=ni(e.data.transition);if(!i(r)&&!o(n._enterCb)&&1===n.nodeType){for(var a=r.css,s=r.type,c=r.enterClass,l=r.enterToClass,f=r.enterActiveClass,p=r.appearClass,d=r.appearToClass,v=r.appearActiveClass,g=r.beforeEnter,m=r.enter,y=r.afterEnter,_=r.enterCancelled,b=r.beforeAppear,w=r.appear,x=r.afterAppear,C=r.appearCancelled,E=r.duration,T=wt,A=wt.$vnode;A&&A.parent;)T=(A=A.parent).context;var S=!T._isMounted||!e.isRootInsert;if(!S||w||""===w){var k=S&&p?p:c,O=S&&v?v:f,D=S&&d?d:l,I=S&&b||g,N=S&&"function"==typeof w?w:m,j=S&&x||y,L=S&&C||_,$=h(u(E)?E.enter:E);0;var R=!1!==a&&!G,M=Ci(N),H=n._enterCb=P(function(){R&&(hi(n,D),hi(n,O)),H.cancelled?(R&&hi(n,k),L&&L(n)):j&&j(n),n._enterCb=null});e.data.show||ut(e,"insert",function(){var t=n.parentNode,r=t&&t._pending&&t._pending[e.key];r&&r.tag===e.tag&&r.elm._leaveCb&&r.elm._leaveCb(),N&&N(n,H)}),I&&I(n),R&&(di(n,k),di(n,O),pi(function(){hi(n,k),H.cancelled||(di(n,D),M||(xi($)?setTimeout(H,$):vi(n,s,H)))})),e.data.show&&(t&&t(),N&&N(n,H)),R||M||H()}}}function wi(e,t){var n=e.elm;o(n._enterCb)&&(n._enterCb.cancelled=!0,n._enterCb());var r=ni(e.data.transition);if(i(r)||1!==n.nodeType)return t();if(!o(n._leaveCb)){var a=r.css,s=r.type,c=r.leaveClass,l=r.leaveToClass,f=r.leaveActiveClass,p=r.beforeLeave,d=r.leave,v=r.afterLeave,g=r.leaveCancelled,m=r.delayLeave,y=r.duration,_=!1!==a&&!G,b=Ci(d),w=h(u(y)?y.leave:y);0;var x=n._leaveCb=P(function(){n.parentNode&&n.parentNode._pending&&(n.parentNode._pending[e.key]=null),_&&(hi(n,l),hi(n,f)),x.cancelled?(_&&hi(n,c),g&&g(n)):(t(),v&&v(n)),n._leaveCb=null});m?m(C):C()}function C(){x.cancelled||(e.data.show||((n.parentNode._pending||(n.parentNode._pending={}))[e.key]=e),p&&p(n),_&&(di(n,c),di(n,f),pi(function(){hi(n,c),x.cancelled||(di(n,l),b||(xi(w)?setTimeout(x,w):vi(n,s,x)))})),d&&d(n,x),_||b||x())}}function xi(e){return"number"==typeof e&&!isNaN(e)}function Ci(e){if(i(e))return!1;var t=e.fns;return o(t)?Ci(Array.isArray(t)?t[0]:t):(e._length||e.length)>1}function Ei(e,t){!0!==t.data.show&&bi(t)}var Ti=function(e){var t,n,r={},u=e.modules,c=e.nodeOps;for(t=0;t<Vn.length;++t)for(r[Vn[t]]=[],n=0;n<u.length;++n)o(u[n][Vn[t]])&&r[Vn[t]].push(u[n][Vn[t]]);function l(e){var t=c.parentNode(e);o(t)&&c.removeChild(t,e)}function f(e,t,n,i,s,u,l){if(o(e.elm)&&o(u)&&(e=u[l]=ye(e)),e.isRootInsert=!s,!function(e,t,n,i){var s=e.data;if(o(s)){var u=o(e.componentInstance)&&s.keepAlive;if(o(s=s.hook)&&o(s=s.init)&&s(e,!1,n,i),o(e.componentInstance))return p(e,t),a(u)&&function(e,t,n,i){for(var a,s=e;s.componentInstance;)if(s=s.componentInstance._vnode,o(a=s.data)&&o(a=a.transition)){for(a=0;a<r.activate.length;++a)r.activate[a](zn,s);t.push(s);break}d(n,e.elm,i)}(e,t,n,i),!0}}(e,t,n,i)){var f=e.data,v=e.children,g=e.tag;o(g)?(e.elm=e.ns?c.createElementNS(e.ns,g):c.createElement(g,e),y(e),h(e,v,t),o(f)&&m(e,t),d(n,e.elm,i)):a(e.isComment)?(e.elm=c.createComment(e.text),d(n,e.elm,i)):(e.elm=c.createTextNode(e.text),d(n,e.elm,i))}}function p(e,t){o(e.data.pendingInsert)&&(t.push.apply(t,e.data.pendingInsert),e.data.pendingInsert=null),e.elm=e.componentInstance.$el,g(e)?(m(e,t),y(e)):(Un(e),t.push(e))}function d(e,t,n){o(e)&&(o(n)?n.parentNode===e&&c.insertBefore(e,t,n):c.appendChild(e,t))}function h(e,t,n){if(Array.isArray(t))for(var r=0;r<t.length;++r)f(t[r],n,e.elm,null,!0,t,r);else s(e.text)&&c.appendChild(e.elm,c.createTextNode(String(e.text)))}function g(e){for(;e.componentInstance;)e=e.componentInstance._vnode;return o(e.tag)}function m(e,n){for(var i=0;i<r.create.length;++i)r.create[i](zn,e);o(t=e.data.hook)&&(o(t.create)&&t.create(zn,e),o(t.insert)&&n.push(e))}function y(e){var t;if(o(t=e.fnScopeId))c.setStyleScope(e.elm,t);else for(var n=e;n;)o(t=n.context)&&o(t=t.$options._scopeId)&&c.setStyleScope(e.elm,t),n=n.parent;o(t=wt)&&t!==e.context&&t!==e.fnContext&&o(t=t.$options._scopeId)&&c.setStyleScope(e.elm,t)}function _(e,t,n,r,i,o){for(;r<=i;++r)f(n[r],o,e,t,!1,n,r)}function b(e){var t,n,i=e.data;if(o(i))for(o(t=i.hook)&&o(t=t.destroy)&&t(e),t=0;t<r.destroy.length;++t)r.destroy[t](e);if(o(t=e.children))for(n=0;n<e.children.length;++n)b(e.children[n])}function w(e,t,n,r){for(;n<=r;++n){var i=t[n];o(i)&&(o(i.tag)?(x(i),b(i)):l(i.elm))}}function x(e,t){if(o(t)||o(e.data)){var n,i=r.remove.length+1;for(o(t)?t.listeners+=i:t=function(e,t){function n(){0==--n.listeners&&l(e)}return n.listeners=t,n}(e.elm,i),o(n=e.componentInstance)&&o(n=n._vnode)&&o(n.data)&&x(n,t),n=0;n<r.remove.length;++n)r.remove[n](e,t);o(n=e.data.hook)&&o(n=n.remove)?n(e,t):t()}else l(e.elm)}function C(e,t,n,r){for(var i=n;i<r;i++){var a=t[i];if(o(a)&&Kn(e,a))return i}}function E(e,t,n,s){if(e!==t){var u=t.elm=e.elm;if(a(e.isAsyncPlaceholder))o(t.asyncFactory.resolved)?S(e.elm,t,n):t.isAsyncPlaceholder=!0;else if(a(t.isStatic)&&a(e.isStatic)&&t.key===e.key&&(a(t.isCloned)||a(t.isOnce)))t.componentInstance=e.componentInstance;else{var l,p=t.data;o(p)&&o(l=p.hook)&&o(l=l.prepatch)&&l(e,t);var d=e.children,h=t.children;if(o(p)&&g(t)){for(l=0;l<r.update.length;++l)r.update[l](e,t);o(l=p.hook)&&o(l=l.update)&&l(e,t)}i(t.text)?o(d)&&o(h)?d!==h&&function(e,t,n,r,a){for(var s,u,l,p=0,d=0,h=t.length-1,v=t[0],g=t[h],m=n.length-1,y=n[0],b=n[m],x=!a;p<=h&&d<=m;)i(v)?v=t[++p]:i(g)?g=t[--h]:Kn(v,y)?(E(v,y,r),v=t[++p],y=n[++d]):Kn(g,b)?(E(g,b,r),g=t[--h],b=n[--m]):Kn(v,b)?(E(v,b,r),x&&c.insertBefore(e,v.elm,c.nextSibling(g.elm)),v=t[++p],b=n[--m]):Kn(g,y)?(E(g,y,r),x&&c.insertBefore(e,g.elm,v.elm),g=t[--h],y=n[++d]):(i(s)&&(s=Qn(t,p,h)),i(u=o(y.key)?s[y.key]:C(y,t,p,h))?f(y,r,e,v.elm,!1,n,d):Kn(l=t[u],y)?(E(l,y,r),t[u]=void 0,x&&c.insertBefore(e,l.elm,v.elm)):f(y,r,e,v.elm,!1,n,d),y=n[++d]);p>h?_(e,i(n[m+1])?null:n[m+1].elm,n,d,m,r):d>m&&w(0,t,p,h)}(u,d,h,n,s):o(h)?(o(e.text)&&c.setTextContent(u,""),_(u,null,h,0,h.length-1,n)):o(d)?w(0,d,0,d.length-1):o(e.text)&&c.setTextContent(u,""):e.text!==t.text&&c.setTextContent(u,t.text),o(p)&&o(l=p.hook)&&o(l=l.postpatch)&&l(e,t)}}}function T(e,t,n){if(a(n)&&o(e.parent))e.parent.data.pendingInsert=t;else for(var r=0;r<t.length;++r)t[r].data.hook.insert(t[r])}var A=v("attrs,class,staticClass,staticStyle,key");function S(e,t,n,r){var i,s=t.tag,u=t.data,c=t.children;if(r=r||u&&u.pre,t.elm=e,a(t.isComment)&&o(t.asyncFactory))return t.isAsyncPlaceholder=!0,!0;if(o(u)&&(o(i=u.hook)&&o(i=i.init)&&i(t,!0),o(i=t.componentInstance)))return p(t,n),!0;if(o(s)){if(o(c))if(e.hasChildNodes())if(o(i=u)&&o(i=i.domProps)&&o(i=i.innerHTML)){if(i!==e.innerHTML)return!1}else{for(var l=!0,f=e.firstChild,d=0;d<c.length;d++){if(!f||!S(f,c[d],n,r)){l=!1;break}f=f.nextSibling}if(!l||f)return!1}else h(t,c,n);if(o(u)){var v=!1;for(var g in u)if(!A(g)){v=!0,m(t,n);break}!v&&u.class&&rt(u.class)}}else e.data!==t.text&&(e.data=t.text);return!0}return function(e,t,n,s,u,l){if(!i(t)){var p,d=!1,h=[];if(i(e))d=!0,f(t,h,u,l);else{var v=o(e.nodeType);if(!v&&Kn(e,t))E(e,t,h,s);else{if(v){if(1===e.nodeType&&e.hasAttribute(R)&&(e.removeAttribute(R),n=!0),a(n)&&S(e,t,h))return T(t,h,!0),e;p=e,e=new he(c.tagName(p).toLowerCase(),{},[],void 0,p)}var m=e.elm,y=c.parentNode(m);if(f(t,h,m._leaveCb?null:y,c.nextSibling(m)),o(t.parent))for(var _=t.parent,x=g(t);_;){for(var C=0;C<r.destroy.length;++C)r.destroy[C](_);if(_.elm=t.elm,x){for(var A=0;A<r.create.length;++A)r.create[A](zn,_);var k=_.data.hook.insert;if(k.merged)for(var O=1;O<k.fns.length;O++)k.fns[O]()}else Un(_);_=_.parent}o(y)?w(0,[e],0,0):o(e.tag)&&b(e)}}return T(t,h,d),t.elm}o(e)&&b(e)}}({nodeOps:Bn,modules:[or,dr,Hr,Br,Zr,V?{create:Ei,activate:Ei,remove:function(e,t){!0!==e.data.show?wi(e,t):t()}}:{}].concat(tr)});G&&document.addEventListener("selectionchange",function(){var e=document.activeElement;e&&e.vmodel&&ji(e,"input")});var Ai={inserted:function(e,t,n,r){"select"===n.tag?(r.elm&&!r.elm._vOptions?ut(n,"postpatch",function(){Ai.componentUpdated(e,t,n)}):Si(e,t,n.context),e._vOptions=[].map.call(e.options,Di)):("textarea"===n.tag||Fn(e.type))&&(e._vModifiers=t.modifiers,t.modifiers.lazy||(e.addEventListener("compositionstart",Ii),e.addEventListener("compositionend",Ni),e.addEventListener("change",Ni),G&&(e.vmodel=!0)))},componentUpdated:function(e,t,n){if("select"===n.tag){Si(e,t,n.context);var r=e._vOptions,i=e._vOptions=[].map.call(e.options,Di);if(i.some(function(e,t){return!L(e,r[t])}))(e.multiple?t.value.some(function(e){return Oi(e,i)}):t.value!==t.oldValue&&Oi(t.value,i))&&ji(e,"change")}}};function Si(e,t,n){ki(e,t,n),(X||J)&&setTimeout(function(){ki(e,t,n)},0)}function ki(e,t,n){var r=t.value,i=e.multiple;if(!i||Array.isArray(r)){for(var o,a,s=0,u=e.options.length;s<u;s++)if(a=e.options[s],i)o=$(r,Di(a))>-1,a.selected!==o&&(a.selected=o);else if(L(Di(a),r))return void(e.selectedIndex!==s&&(e.selectedIndex=s));i||(e.selectedIndex=-1)}}function Oi(e,t){return t.every(function(t){return!L(t,e)})}function Di(e){return"_value"in e?e._value:e.value}function Ii(e){e.target.composing=!0}function Ni(e){e.target.composing&&(e.target.composing=!1,ji(e.target,"input"))}function ji(e,t){var n=document.createEvent("HTMLEvents");n.initEvent(t,!0,!0),e.dispatchEvent(n)}function Li(e){return!e.componentInstance||e.data&&e.data.transition?e:Li(e.componentInstance._vnode)}var $i={model:Ai,show:{bind:function(e,t,n){var r=t.value,i=(n=Li(n)).data&&n.data.transition,o=e.__vOriginalDisplay="none"===e.style.display?"":e.style.display;r&&i?(n.data.show=!0,bi(n,function(){e.style.display=o})):e.style.display=r?o:"none"},update:function(e,t,n){var r=t.value;!r!=!t.oldValue&&((n=Li(n)).data&&n.data.transition?(n.data.show=!0,r?bi(n,function(){e.style.display=e.__vOriginalDisplay}):wi(n,function(){e.style.display="none"})):e.style.display=r?e.__vOriginalDisplay:"none")},unbind:function(e,t,n,r,i){i||(e.style.display=e.__vOriginalDisplay)}}},Pi={name:String,appear:Boolean,css:Boolean,mode:String,type:String,enterClass:String,leaveClass:String,enterToClass:String,leaveToClass:String,enterActiveClass:String,leaveActiveClass:String,appearClass:String,appearActiveClass:String,appearToClass:String,duration:[Number,String,Object]};function Ri(e){var t=e&&e.componentOptions;return t&&t.Ctor.options.abstract?Ri(ht(t.children)):e}function Mi(e){var t={},n=e.$options;for(var r in n.propsData)t[r]=e[r];var i=n._parentListeners;for(var o in i)t[C(o)]=i[o];return t}function Hi(e,t){if(/\d-keep-alive$/.test(t.tag))return e("keep-alive",{props:t.componentOptions.propsData})}var Fi={name:"transition",props:Pi,abstract:!0,render:function(e){var t=this,n=this.$slots.default;if(n&&(n=n.filter(function(e){return e.tag||dt(e)})).length){0;var r=this.mode;0;var i=n[0];if(function(e){for(;e=e.parent;)if(e.data.transition)return!0}(this.$vnode))return i;var o=Ri(i);if(!o)return i;if(this._leaving)return Hi(e,i);var a="__transition-"+this._uid+"-";o.key=null==o.key?o.isComment?a+"comment":a+o.tag:s(o.key)?0===String(o.key).indexOf(a)?o.key:a+o.key:o.key;var u=(o.data||(o.data={})).transition=Mi(this),c=this._vnode,l=Ri(c);if(o.data.directives&&o.data.directives.some(function(e){return"show"===e.name})&&(o.data.show=!0),l&&l.data&&!function(e,t){return t.key===e.key&&t.tag===e.tag}(o,l)&&!dt(l)&&(!l.componentInstance||!l.componentInstance._vnode.isComment)){var f=l.data.transition=O({},u);if("out-in"===r)return this._leaving=!0,ut(f,"afterLeave",function(){t._leaving=!1,t.$forceUpdate()}),Hi(e,i);if("in-out"===r){if(dt(o))return c;var p,d=function(){p()};ut(u,"afterEnter",d),ut(u,"enterCancelled",d),ut(f,"delayLeave",function(e){p=e})}}return i}}},qi=O({tag:String,moveClass:String},Pi);function Bi(e){e.elm._moveCb&&e.elm._moveCb(),e.elm._enterCb&&e.elm._enterCb()}function Wi(e){e.data.newPos=e.elm.getBoundingClientRect()}function Ui(e){var t=e.data.pos,n=e.data.newPos,r=t.left-n.left,i=t.top-n.top;if(r||i){e.data.moved=!0;var o=e.elm.style;o.transform=o.WebkitTransform="translate("+r+"px,"+i+"px)",o.transitionDuration="0s"}}delete qi.mode;var zi={Transition:Fi,TransitionGroup:{props:qi,render:function(e){for(var t=this.tag||this.$vnode.data.tag||"span",n=Object.create(null),r=this.prevChildren=this.children,i=this.$slots.default||[],o=this.children=[],a=Mi(this),s=0;s<i.length;s++){var u=i[s];if(u.tag)if(null!=u.key&&0!==String(u.key).indexOf("__vlist"))o.push(u),n[u.key]=u,(u.data||(u.data={})).transition=a;else;}if(r){for(var c=[],l=[],f=0;f<r.length;f++){var p=r[f];p.data.transition=a,p.data.pos=p.elm.getBoundingClientRect(),n[p.key]?c.push(p):l.push(p)}this.kept=e(t,null,c),this.removed=l}return e(t,null,o)},beforeUpdate:function(){this.__patch__(this._vnode,this.kept,!1,!0),this._vnode=this.kept},updated:function(){var e=this.prevChildren,t=this.moveClass||(this.name||"v")+"-move";e.length&&this.hasMove(e[0].elm,t)&&(e.forEach(Bi),e.forEach(Wi),e.forEach(Ui),this._reflow=document.body.offsetHeight,e.forEach(function(e){if(e.data.moved){var n=e.elm,r=n.style;di(n,t),r.transform=r.WebkitTransform=r.transitionDuration="",n.addEventListener(ui,n._moveCb=function e(r){r&&!/transform$/.test(r.propertyName)||(n.removeEventListener(ui,e),n._moveCb=null,hi(n,t))})}}))},methods:{hasMove:function(e,t){if(!ii)return!1;if(this._hasMove)return this._hasMove;var n=e.cloneNode();e._transitionClasses&&e._transitionClasses.forEach(function(e){ti(n,e)}),ei(n,t),n.style.display="none",this.$el.appendChild(n);var r=mi(n);return this.$el.removeChild(n),this._hasMove=r.hasTransform}}}};dn.config.mustUseProp=Cn,dn.config.isReservedTag=Rn,dn.config.isReservedAttr=wn,dn.config.getTagNamespace=Mn,dn.config.isUnknownElement=function(e){if(!V)return!0;if(Rn(e))return!1;if(e=e.toLowerCase(),null!=Hn[e])return Hn[e];var t=document.createElement(e);return e.indexOf("-")>-1?Hn[e]=t.constructor===window.HTMLUnknownElement||t.constructor===window.HTMLElement:Hn[e]=/HTMLUnknownElement/.test(t.toString())},O(dn.options.directives,$i),O(dn.options.components,zi),dn.prototype.__patch__=V?Ti:I,dn.prototype.$mount=function(e,t){return function(e,t,n){return e.$el=t,e.$options.render||(e.$options.render=ge),Et(e,"beforeMount"),new jt(e,function(){e._update(e._render(),n)},I,null,!0),n=!1,null==e.$vnode&&(e._isMounted=!0,Et(e,"mounted")),e}(this,e=e&&V?qn(e):void 0,t)},V&&setTimeout(function(){F.devtools&&ie&&ie.emit("init",dn)},0);var Vi=/\{\{((?:.|\n)+?)\}\}/g,Ki=/[-.*+?^${}()|[\]\/\\]/g,Qi=w(function(e){var t=e[0].replace(Ki,"\\$&"),n=e[1].replace(Ki,"\\$&");return new RegExp(t+"((?:.|\\n)+?)"+n,"g")});function Yi(e,t){var n=t?Qi(t):Vi;if(n.test(e)){for(var r,i,o,a=[],s=[],u=n.lastIndex=0;r=n.exec(e);){(i=r.index)>u&&(s.push(o=e.slice(u,i)),a.push(JSON.stringify(o)));var c=vr(r[1].trim());a.push("_s("+c+")"),s.push({"@binding":c}),u=i+r[0].length}return u<e.length&&(s.push(o=e.slice(u)),a.push(JSON.stringify(o))),{expression:a.join("+"),tokens:s}}}var Xi={staticKeys:["staticClass"],transformNode:function(e,t){t.warn;var n=Tr(e,"class");n&&(e.staticClass=JSON.stringify(n));var r=Er(e,"class",!1);r&&(e.classBinding=r)},genData:function(e){var t="";return e.staticClass&&(t+="staticClass:"+e.staticClass+","),e.classBinding&&(t+="class:"+e.classBinding+","),t}};var Gi,Ji={staticKeys:["staticStyle"],transformNode:function(e,t){t.warn;var n=Tr(e,"style");n&&(e.staticStyle=JSON.stringify(Wr(n)));var r=Er(e,"style",!1);r&&(e.styleBinding=r)},genData:function(e){var t="";return e.staticStyle&&(t+="staticStyle:"+e.staticStyle+","),e.styleBinding&&(t+="style:("+e.styleBinding+"),"),t}},Zi=function(e){return(Gi=Gi||document.createElement("div")).innerHTML=e,Gi.textContent},eo=v("area,base,br,col,embed,frame,hr,img,input,isindex,keygen,link,meta,param,source,track,wbr"),to=v("colgroup,dd,dt,li,options,p,td,tfoot,th,thead,tr,source"),no=v("address,article,aside,base,blockquote,body,caption,col,colgroup,dd,details,dialog,div,dl,dt,fieldset,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,head,header,hgroup,hr,html,legend,li,menuitem,meta,optgroup,option,param,rp,rt,source,style,summary,tbody,td,tfoot,th,thead,title,tr,track"),ro=/^\s*([^\s"'<>\/=]+)(?:\s*(=)\s*(?:"([^"]*)"+|'([^']*)'+|([^\s"'=<>`]+)))?/,io="[a-zA-Z_][\\w\\-\\.]*",oo="((?:"+io+"\\:)?"+io+")",ao=new RegExp("^<"+oo),so=/^\s*(\/?)>/,uo=new RegExp("^<\\/"+oo+"[^>]*>"),co=/^<!DOCTYPE [^>]+>/i,lo=/^<!\--/,fo=/^<!\[/,po=!1;"x".replace(/x(.)?/g,function(e,t){po=""===t});var ho=v("script,style,textarea",!0),vo={},go={"&lt;":"<","&gt;":">","&quot;":'"',"&amp;":"&","&#10;":"\n","&#9;":"\t"},mo=/&(?:lt|gt|quot|amp);/g,yo=/&(?:lt|gt|quot|amp|#10|#9);/g,_o=v("pre,textarea",!0),bo=function(e,t){return e&&_o(e)&&"\n"===t[0]};function wo(e,t){var n=t?yo:mo;return e.replace(n,function(e){return go[e]})}var xo,Co,Eo,To,Ao,So,ko,Oo,Do=/^@|^v-on:/,Io=/^v-|^@|^:/,No=/([^]*?)\s+(?:in|of)\s+([^]*)/,jo=/,([^,\}\]]*)(?:,([^,\}\]]*))?$/,Lo=/^\(|\)$/g,$o=/:(.*)$/,Po=/^:|^v-bind:/,Ro=/\.[^.]+/g,Mo=w(Zi);function Ho(e,t,n){return{type:1,tag:e,attrsList:t,attrsMap:function(e){for(var t={},n=0,r=e.length;n<r;n++)t[e[n].name]=e[n].value;return t}(t),parent:n,children:[]}}function Fo(e,t){xo=t.warn||mr,So=t.isPreTag||N,ko=t.mustUseProp||N,Oo=t.getTagNamespace||N,Eo=yr(t.modules,"transformNode"),To=yr(t.modules,"preTransformNode"),Ao=yr(t.modules,"postTransformNode"),Co=t.delimiters;var n,r,i=[],o=!1!==t.preserveWhitespace,a=!1,s=!1;function u(e){e.pre&&(a=!1),So(e.tag)&&(s=!1);for(var n=0;n<Ao.length;n++)Ao[n](e,t)}return function(e,t){for(var n,r,i=[],o=t.expectHTML,a=t.isUnaryTag||N,s=t.canBeLeftOpenTag||N,u=0;e;){if(n=e,r&&ho(r)){var c=0,l=r.toLowerCase(),f=vo[l]||(vo[l]=new RegExp("([\\s\\S]*?)(</"+l+"[^>]*>)","i")),p=e.replace(f,function(e,n,r){return c=r.length,ho(l)||"noscript"===l||(n=n.replace(/<!\--([\s\S]*?)-->/g,"$1").replace(/<!\[CDATA\[([\s\S]*?)]]>/g,"$1")),bo(l,n)&&(n=n.slice(1)),t.chars&&t.chars(n),""});u+=e.length-p.length,e=p,A(l,u-c,u)}else{var d=e.indexOf("<");if(0===d){if(lo.test(e)){var h=e.indexOf("--\x3e");if(h>=0){t.shouldKeepComment&&t.comment(e.substring(4,h)),C(h+3);continue}}if(fo.test(e)){var v=e.indexOf("]>");if(v>=0){C(v+2);continue}}var g=e.match(co);if(g){C(g[0].length);continue}var m=e.match(uo);if(m){var y=u;C(m[0].length),A(m[1],y,u);continue}var _=E();if(_){T(_),bo(r,e)&&C(1);continue}}var b=void 0,w=void 0,x=void 0;if(d>=0){for(w=e.slice(d);!(uo.test(w)||ao.test(w)||lo.test(w)||fo.test(w)||(x=w.indexOf("<",1))<0);)d+=x,w=e.slice(d);b=e.substring(0,d),C(d)}d<0&&(b=e,e=""),t.chars&&b&&t.chars(b)}if(e===n){t.chars&&t.chars(e);break}}function C(t){u+=t,e=e.substring(t)}function E(){var t=e.match(ao);if(t){var n,r,i={tagName:t[1],attrs:[],start:u};for(C(t[0].length);!(n=e.match(so))&&(r=e.match(ro));)C(r[0].length),i.attrs.push(r);if(n)return i.unarySlash=n[1],C(n[0].length),i.end=u,i}}function T(e){var n=e.tagName,u=e.unarySlash;o&&("p"===r&&no(n)&&A(r),s(n)&&r===n&&A(n));for(var c=a(n)||!!u,l=e.attrs.length,f=new Array(l),p=0;p<l;p++){var d=e.attrs[p];po&&-1===d[0].indexOf('""')&&(""===d[3]&&delete d[3],""===d[4]&&delete d[4],""===d[5]&&delete d[5]);var h=d[3]||d[4]||d[5]||"",v="a"===n&&"href"===d[1]?t.shouldDecodeNewlinesForHref:t.shouldDecodeNewlines;f[p]={name:d[1],value:wo(h,v)}}c||(i.push({tag:n,lowerCasedTag:n.toLowerCase(),attrs:f}),r=n),t.start&&t.start(n,f,c,e.start,e.end)}function A(e,n,o){var a,s;if(null==n&&(n=u),null==o&&(o=u),e&&(s=e.toLowerCase()),e)for(a=i.length-1;a>=0&&i[a].lowerCasedTag!==s;a--);else a=0;if(a>=0){for(var c=i.length-1;c>=a;c--)t.end&&t.end(i[c].tag,n,o);i.length=a,r=a&&i[a-1].tag}else"br"===s?t.start&&t.start(e,[],!0,n,o):"p"===s&&(t.start&&t.start(e,[],!1,n,o),t.end&&t.end(e,n,o))}A()}(e,{warn:xo,expectHTML:t.expectHTML,isUnaryTag:t.isUnaryTag,canBeLeftOpenTag:t.canBeLeftOpenTag,shouldDecodeNewlines:t.shouldDecodeNewlines,shouldDecodeNewlinesForHref:t.shouldDecodeNewlinesForHref,shouldKeepComment:t.comments,start:function(e,o,c){var l=r&&r.ns||Oo(e);X&&"svg"===l&&(o=function(e){for(var t=[],n=0;n<e.length;n++){var r=e[n];zo.test(r.name)||(r.name=r.name.replace(Vo,""),t.push(r))}return t}(o));var f,p=Ho(e,o,r);l&&(p.ns=l),"style"!==(f=p).tag&&("script"!==f.tag||f.attrsMap.type&&"text/javascript"!==f.attrsMap.type)||re()||(p.forbidden=!0);for(var d=0;d<To.length;d++)p=To[d](p,t)||p;function h(e){0}if(a||(!function(e){null!=Tr(e,"v-pre")&&(e.pre=!0)}(p),p.pre&&(a=!0)),So(p.tag)&&(s=!0),a?function(e){var t=e.attrsList.length;if(t)for(var n=e.attrs=new Array(t),r=0;r<t;r++)n[r]={name:e.attrsList[r].name,value:JSON.stringify(e.attrsList[r].value)};else e.pre||(e.plain=!0)}(p):p.processed||(Bo(p),function(e){var t=Tr(e,"v-if");if(t)e.if=t,Wo(e,{exp:t,block:e});else{null!=Tr(e,"v-else")&&(e.else=!0);var n=Tr(e,"v-else-if");n&&(e.elseif=n)}}(p),function(e){null!=Tr(e,"v-once")&&(e.once=!0)}(p),qo(p,t)),n?i.length||n.if&&(p.elseif||p.else)&&(h(),Wo(n,{exp:p.elseif,block:p})):(n=p,h()),r&&!p.forbidden)if(p.elseif||p.else)!function(e,t){var n=function(e){var t=e.length;for(;t--;){if(1===e[t].type)return e[t];e.pop()}}(t.children);n&&n.if&&Wo(n,{exp:e.elseif,block:e})}(p,r);else if(p.slotScope){r.plain=!1;var v=p.slotTarget||'"default"';(r.scopedSlots||(r.scopedSlots={}))[v]=p}else r.children.push(p),p.parent=r;c?u(p):(r=p,i.push(p))},end:function(){var e=i[i.length-1],t=e.children[e.children.length-1];t&&3===t.type&&" "===t.text&&!s&&e.children.pop(),i.length-=1,r=i[i.length-1],u(e)},chars:function(e){if(r&&(!X||"textarea"!==r.tag||r.attrsMap.placeholder!==e)){var t,n,i=r.children;if(e=s||e.trim()?"script"===(t=r).tag||"style"===t.tag?e:Mo(e):o&&i.length?" ":"")!a&&" "!==e&&(n=Yi(e,Co))?i.push({type:2,expression:n.expression,tokens:n.tokens,text:e}):" "===e&&i.length&&" "===i[i.length-1].text||i.push({type:3,text:e})}},comment:function(e){r.children.push({type:3,text:e,isComment:!0})}}),n}function qo(e,t){var n,r;(r=Er(n=e,"key"))&&(n.key=r),e.plain=!e.key&&!e.attrsList.length,function(e){var t=Er(e,"ref");t&&(e.ref=t,e.refInFor=function(e){var t=e;for(;t;){if(void 0!==t.for)return!0;t=t.parent}return!1}(e))}(e),function(e){if("slot"===e.tag)e.slotName=Er(e,"name");else{var t;"template"===e.tag?(t=Tr(e,"scope"),e.slotScope=t||Tr(e,"slot-scope")):(t=Tr(e,"slot-scope"))&&(e.slotScope=t);var n=Er(e,"slot");n&&(e.slotTarget='""'===n?'"default"':n,"template"===e.tag||e.slotScope||br(e,"slot",n))}}(e),function(e){var t;(t=Er(e,"is"))&&(e.component=t);null!=Tr(e,"inline-template")&&(e.inlineTemplate=!0)}(e);for(var i=0;i<Eo.length;i++)e=Eo[i](e,t)||e;!function(e){var t,n,r,i,o,a,s,u=e.attrsList;for(t=0,n=u.length;t<n;t++){if(r=i=u[t].name,o=u[t].value,Io.test(r))if(e.hasBindings=!0,(a=Uo(r))&&(r=r.replace(Ro,"")),Po.test(r))r=r.replace(Po,""),o=vr(o),s=!1,a&&(a.prop&&(s=!0,"innerHtml"===(r=C(r))&&(r="innerHTML")),a.camel&&(r=C(r)),a.sync&&Cr(e,"update:"+C(r),Sr(o,"$event"))),s||!e.component&&ko(e.tag,e.attrsMap.type,r)?_r(e,r,o):br(e,r,o);else if(Do.test(r))r=r.replace(Do,""),Cr(e,r,o,a,!1);else{var c=(r=r.replace(Io,"")).match($o),l=c&&c[1];l&&(r=r.slice(0,-(l.length+1))),xr(e,r,i,o,l,a)}else br(e,r,JSON.stringify(o)),!e.component&&"muted"===r&&ko(e.tag,e.attrsMap.type,r)&&_r(e,r,"true")}}(e)}function Bo(e){var t;if(t=Tr(e,"v-for")){var n=function(e){var t=e.match(No);if(!t)return;var n={};n.for=t[2].trim();var r=t[1].trim().replace(Lo,""),i=r.match(jo);i?(n.alias=r.replace(jo,""),n.iterator1=i[1].trim(),i[2]&&(n.iterator2=i[2].trim())):n.alias=r;return n}(t);n&&O(e,n)}}function Wo(e,t){e.ifConditions||(e.ifConditions=[]),e.ifConditions.push(t)}function Uo(e){var t=e.match(Ro);if(t){var n={};return t.forEach(function(e){n[e.slice(1)]=!0}),n}}var zo=/^xmlns:NS\d+/,Vo=/^NS\d+:/;function Ko(e){return Ho(e.tag,e.attrsList.slice(),e.parent)}var Qo=[Xi,Ji,{preTransformNode:function(e,t){if("input"===e.tag){var n,r=e.attrsMap;if(!r["v-model"])return;if((r[":type"]||r["v-bind:type"])&&(n=Er(e,"type")),r.type||n||!r["v-bind"]||(n="("+r["v-bind"]+").type"),n){var i=Tr(e,"v-if",!0),o=i?"&&("+i+")":"",a=null!=Tr(e,"v-else",!0),s=Tr(e,"v-else-if",!0),u=Ko(e);Bo(u),wr(u,"type","checkbox"),qo(u,t),u.processed=!0,u.if="("+n+")==='checkbox'"+o,Wo(u,{exp:u.if,block:u});var c=Ko(e);Tr(c,"v-for",!0),wr(c,"type","radio"),qo(c,t),Wo(u,{exp:"("+n+")==='radio'"+o,block:c});var l=Ko(e);return Tr(l,"v-for",!0),wr(l,":type",n),qo(l,t),Wo(u,{exp:i,block:l}),a?u.else=!0:s&&(u.elseif=s),u}}}}];var Yo,Xo,Go={expectHTML:!0,modules:Qo,directives:{model:function(e,t,n){n;var r=t.value,i=t.modifiers,o=e.tag,a=e.attrsMap.type;if(e.component)return Ar(e,r,i),!1;if("select"===o)!function(e,t,n){var r='var $$selectedVal = Array.prototype.filter.call($event.target.options,function(o){return o.selected}).map(function(o){var val = "_value" in o ? o._value : o.value;return '+(n&&n.number?"_n(val)":"val")+"});";r=r+" "+Sr(t,"$event.target.multiple ? $$selectedVal : $$selectedVal[0]"),Cr(e,"change",r,null,!0)}(e,r,i);else if("input"===o&&"checkbox"===a)!function(e,t,n){var r=n&&n.number,i=Er(e,"value")||"null",o=Er(e,"true-value")||"true",a=Er(e,"false-value")||"false";_r(e,"checked","Array.isArray("+t+")?_i("+t+","+i+")>-1"+("true"===o?":("+t+")":":_q("+t+","+o+")")),Cr(e,"change","var $$a="+t+",$$el=$event.target,$$c=$$el.checked?("+o+"):("+a+");if(Array.isArray($$a)){var $$v="+(r?"_n("+i+")":i)+",$$i=_i($$a,$$v);if($$el.checked){$$i<0&&("+Sr(t,"$$a.concat([$$v])")+")}else{$$i>-1&&("+Sr(t,"$$a.slice(0,$$i).concat($$a.slice($$i+1))")+")}}else{"+Sr(t,"$$c")+"}",null,!0)}(e,r,i);else if("input"===o&&"radio"===a)!function(e,t,n){var r=n&&n.number,i=Er(e,"value")||"null";_r(e,"checked","_q("+t+","+(i=r?"_n("+i+")":i)+")"),Cr(e,"change",Sr(t,i),null,!0)}(e,r,i);else if("input"===o||"textarea"===o)!function(e,t,n){var r=e.attrsMap.type,i=n||{},o=i.lazy,a=i.number,s=i.trim,u=!o&&"range"!==r,c=o?"change":"range"===r?Lr:"input",l="$event.target.value";s&&(l="$event.target.value.trim()"),a&&(l="_n("+l+")");var f=Sr(t,l);u&&(f="if($event.target.composing)return;"+f),_r(e,"value","("+t+")"),Cr(e,c,f,null,!0),(s||a)&&Cr(e,"blur","$forceUpdate()")}(e,r,i);else if(!F.isReservedTag(o))return Ar(e,r,i),!1;return!0},text:function(e,t){t.value&&_r(e,"textContent","_s("+t.value+")")},html:function(e,t){t.value&&_r(e,"innerHTML","_s("+t.value+")")}},isPreTag:function(e){return"pre"===e},isUnaryTag:eo,mustUseProp:Cn,canBeLeftOpenTag:to,isReservedTag:Rn,getTagNamespace:Mn,staticKeys:function(e){return e.reduce(function(e,t){return e.concat(t.staticKeys||[])},[]).join(",")}(Qo)},Jo=w(function(e){return v("type,tag,attrsList,attrsMap,plain,parent,children,attrs"+(e?","+e:""))});function Zo(e,t){e&&(Yo=Jo(t.staticKeys||""),Xo=t.isReservedTag||N,function e(t){t.static=function(e){if(2===e.type)return!1;if(3===e.type)return!0;return!(!e.pre&&(e.hasBindings||e.if||e.for||g(e.tag)||!Xo(e.tag)||function(e){for(;e.parent;){if("template"!==(e=e.parent).tag)return!1;if(e.for)return!0}return!1}(e)||!Object.keys(e).every(Yo)))}(t);if(1===t.type){if(!Xo(t.tag)&&"slot"!==t.tag&&null==t.attrsMap["inline-template"])return;for(var n=0,r=t.children.length;n<r;n++){var i=t.children[n];e(i),i.static||(t.static=!1)}if(t.ifConditions)for(var o=1,a=t.ifConditions.length;o<a;o++){var s=t.ifConditions[o].block;e(s),s.static||(t.static=!1)}}}(e),function e(t,n){if(1===t.type){if((t.static||t.once)&&(t.staticInFor=n),t.static&&t.children.length&&(1!==t.children.length||3!==t.children[0].type))return void(t.staticRoot=!0);if(t.staticRoot=!1,t.children)for(var r=0,i=t.children.length;r<i;r++)e(t.children[r],n||!!t.for);if(t.ifConditions)for(var o=1,a=t.ifConditions.length;o<a;o++)e(t.ifConditions[o].block,n)}}(e,!1))}var ea=/^([\w$_]+|\([^)]*?\))\s*=>|^function\s*\(/,ta=/^[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*|\['[^']*?']|\["[^"]*?"]|\[\d+]|\[[A-Za-z_$][\w$]*])*$/,na={esc:27,tab:9,enter:13,space:32,up:38,left:37,right:39,down:40,delete:[8,46]},ra={esc:"Escape",tab:"Tab",enter:"Enter",space:" ",up:["Up","ArrowUp"],left:["Left","ArrowLeft"],right:["Right","ArrowRight"],down:["Down","ArrowDown"],delete:["Backspace","Delete"]},ia=function(e){return"if("+e+")return null;"},oa={stop:"$event.stopPropagation();",prevent:"$event.preventDefault();",self:ia("$event.target !== $event.currentTarget"),ctrl:ia("!$event.ctrlKey"),shift:ia("!$event.shiftKey"),alt:ia("!$event.altKey"),meta:ia("!$event.metaKey"),left:ia("'button' in $event && $event.button !== 0"),middle:ia("'button' in $event && $event.button !== 1"),right:ia("'button' in $event && $event.button !== 2")};function aa(e,t,n){var r=t?"nativeOn:{":"on:{";for(var i in e)r+='"'+i+'":'+sa(i,e[i])+",";return r.slice(0,-1)+"}"}function sa(e,t){if(!t)return"function(){}";if(Array.isArray(t))return"["+t.map(function(t){return sa(e,t)}).join(",")+"]";var n=ta.test(t.value),r=ea.test(t.value);if(t.modifiers){var i="",o="",a=[];for(var s in t.modifiers)if(oa[s])o+=oa[s],na[s]&&a.push(s);else if("exact"===s){var u=t.modifiers;o+=ia(["ctrl","shift","alt","meta"].filter(function(e){return!u[e]}).map(function(e){return"$event."+e+"Key"}).join("||"))}else a.push(s);return a.length&&(i+=function(e){return"if(!('button' in $event)&&"+e.map(ua).join("&&")+")return null;"}(a)),o&&(i+=o),"function($event){"+i+(n?"return "+t.value+"($event)":r?"return ("+t.value+")($event)":t.value)+"}"}return n||r?t.value:"function($event){"+t.value+"}"}function ua(e){var t=parseInt(e,10);if(t)return"$event.keyCode!=="+t;var n=na[e],r=ra[e];return"_k($event.keyCode,"+JSON.stringify(e)+","+JSON.stringify(n)+",$event.key,"+JSON.stringify(r)+")"}var ca={on:function(e,t){e.wrapListeners=function(e){return"_g("+e+","+t.value+")"}},bind:function(e,t){e.wrapData=function(n){return"_b("+n+",'"+e.tag+"',"+t.value+","+(t.modifiers&&t.modifiers.prop?"true":"false")+(t.modifiers&&t.modifiers.sync?",true":"")+")"}},cloak:I},la=function(e){this.options=e,this.warn=e.warn||mr,this.transforms=yr(e.modules,"transformCode"),this.dataGenFns=yr(e.modules,"genData"),this.directives=O(O({},ca),e.directives);var t=e.isReservedTag||N;this.maybeComponent=function(e){return!t(e.tag)},this.onceId=0,this.staticRenderFns=[]};function fa(e,t){var n=new la(t);return{render:"with(this){return "+(e?pa(e,n):'_c("div")')+"}",staticRenderFns:n.staticRenderFns}}function pa(e,t){if(e.staticRoot&&!e.staticProcessed)return da(e,t);if(e.once&&!e.onceProcessed)return ha(e,t);if(e.for&&!e.forProcessed)return function(e,t,n,r){var i=e.for,o=e.alias,a=e.iterator1?","+e.iterator1:"",s=e.iterator2?","+e.iterator2:"";0;return e.forProcessed=!0,(r||"_l")+"(("+i+"),function("+o+a+s+"){return "+(n||pa)(e,t)+"})"}(e,t);if(e.if&&!e.ifProcessed)return va(e,t);if("template"!==e.tag||e.slotTarget){if("slot"===e.tag)return function(e,t){var n=e.slotName||'"default"',r=ya(e,t),i="_t("+n+(r?","+r:""),o=e.attrs&&"{"+e.attrs.map(function(e){return C(e.name)+":"+e.value}).join(",")+"}",a=e.attrsMap["v-bind"];!o&&!a||r||(i+=",null");o&&(i+=","+o);a&&(i+=(o?"":",null")+","+a);return i+")"}(e,t);var n;if(e.component)n=function(e,t,n){var r=t.inlineTemplate?null:ya(t,n,!0);return"_c("+e+","+ga(t,n)+(r?","+r:"")+")"}(e.component,e,t);else{var r=e.plain?void 0:ga(e,t),i=e.inlineTemplate?null:ya(e,t,!0);n="_c('"+e.tag+"'"+(r?","+r:"")+(i?","+i:"")+")"}for(var o=0;o<t.transforms.length;o++)n=t.transforms[o](e,n);return n}return ya(e,t)||"void 0"}function da(e,t){return e.staticProcessed=!0,t.staticRenderFns.push("with(this){return "+pa(e,t)+"}"),"_m("+(t.staticRenderFns.length-1)+(e.staticInFor?",true":"")+")"}function ha(e,t){if(e.onceProcessed=!0,e.if&&!e.ifProcessed)return va(e,t);if(e.staticInFor){for(var n="",r=e.parent;r;){if(r.for){n=r.key;break}r=r.parent}return n?"_o("+pa(e,t)+","+t.onceId+++","+n+")":pa(e,t)}return da(e,t)}function va(e,t,n,r){return e.ifProcessed=!0,function e(t,n,r,i){if(!t.length)return i||"_e()";var o=t.shift();return o.exp?"("+o.exp+")?"+a(o.block)+":"+e(t,n,r,i):""+a(o.block);function a(e){return r?r(e,n):e.once?ha(e,n):pa(e,n)}}(e.ifConditions.slice(),t,n,r)}function ga(e,t){var n="{",r=function(e,t){var n=e.directives;if(!n)return;var r,i,o,a,s="directives:[",u=!1;for(r=0,i=n.length;r<i;r++){o=n[r],a=!0;var c=t.directives[o.name];c&&(a=!!c(e,o,t.warn)),a&&(u=!0,s+='{name:"'+o.name+'",rawName:"'+o.rawName+'"'+(o.value?",value:("+o.value+"),expression:"+JSON.stringify(o.value):"")+(o.arg?',arg:"'+o.arg+'"':"")+(o.modifiers?",modifiers:"+JSON.stringify(o.modifiers):"")+"},")}if(u)return s.slice(0,-1)+"]"}(e,t);r&&(n+=r+","),e.key&&(n+="key:"+e.key+","),e.ref&&(n+="ref:"+e.ref+","),e.refInFor&&(n+="refInFor:true,"),e.pre&&(n+="pre:true,"),e.component&&(n+='tag:"'+e.tag+'",');for(var i=0;i<t.dataGenFns.length;i++)n+=t.dataGenFns[i](e);if(e.attrs&&(n+="attrs:{"+wa(e.attrs)+"},"),e.props&&(n+="domProps:{"+wa(e.props)+"},"),e.events&&(n+=aa(e.events,!1,t.warn)+","),e.nativeEvents&&(n+=aa(e.nativeEvents,!0,t.warn)+","),e.slotTarget&&!e.slotScope&&(n+="slot:"+e.slotTarget+","),e.scopedSlots&&(n+=function(e,t){return"scopedSlots:_u(["+Object.keys(e).map(function(n){return ma(n,e[n],t)}).join(",")+"])"}(e.scopedSlots,t)+","),e.model&&(n+="model:{value:"+e.model.value+",callback:"+e.model.callback+",expression:"+e.model.expression+"},"),e.inlineTemplate){var o=function(e,t){var n=e.children[0];0;if(1===n.type){var r=fa(n,t.options);return"inlineTemplate:{render:function(){"+r.render+"},staticRenderFns:["+r.staticRenderFns.map(function(e){return"function(){"+e+"}"}).join(",")+"]}"}}(e,t);o&&(n+=o+",")}return n=n.replace(/,$/,"")+"}",e.wrapData&&(n=e.wrapData(n)),e.wrapListeners&&(n=e.wrapListeners(n)),n}function ma(e,t,n){return t.for&&!t.forProcessed?function(e,t,n){var r=t.for,i=t.alias,o=t.iterator1?","+t.iterator1:"",a=t.iterator2?","+t.iterator2:"";return t.forProcessed=!0,"_l(("+r+"),function("+i+o+a+"){return "+ma(e,t,n)+"})"}(e,t,n):"{key:"+e+",fn:"+("function("+String(t.slotScope)+"){return "+("template"===t.tag?t.if?t.if+"?"+(ya(t,n)||"undefined")+":undefined":ya(t,n)||"undefined":pa(t,n))+"}")+"}"}function ya(e,t,n,r,i){var o=e.children;if(o.length){var a=o[0];if(1===o.length&&a.for&&"template"!==a.tag&&"slot"!==a.tag)return(r||pa)(a,t);var s=n?function(e,t){for(var n=0,r=0;r<e.length;r++){var i=e[r];if(1===i.type){if(_a(i)||i.ifConditions&&i.ifConditions.some(function(e){return _a(e.block)})){n=2;break}(t(i)||i.ifConditions&&i.ifConditions.some(function(e){return t(e.block)}))&&(n=1)}}return n}(o,t.maybeComponent):0,u=i||ba;return"["+o.map(function(e){return u(e,t)}).join(",")+"]"+(s?","+s:"")}}function _a(e){return void 0!==e.for||"template"===e.tag||"slot"===e.tag}function ba(e,t){return 1===e.type?pa(e,t):3===e.type&&e.isComment?(r=e,"_e("+JSON.stringify(r.text)+")"):"_v("+(2===(n=e).type?n.expression:xa(JSON.stringify(n.text)))+")";var n,r}function wa(e){for(var t="",n=0;n<e.length;n++){var r=e[n];t+='"'+r.name+'":'+xa(r.value)+","}return t.slice(0,-1)}function xa(e){return e.replace(/\u2028/g,"\\u2028").replace(/\u2029/g,"\\u2029")}new RegExp("\\b"+"do,if,for,let,new,try,var,case,else,with,await,break,catch,class,const,super,throw,while,yield,delete,export,import,return,switch,default,extends,finally,continue,debugger,function,arguments".split(",").join("\\b|\\b")+"\\b"),new RegExp("\\b"+"delete,typeof,void".split(",").join("\\s*\\([^\\)]*\\)|\\b")+"\\s*\\([^\\)]*\\)");function Ca(e,t){try{return new Function(e)}catch(n){return t.push({err:n,code:e}),I}}var Ea,Ta,Aa=(Ea=function(e,t){var n=Fo(e.trim(),t);!1!==t.optimize&&Zo(n,t);var r=fa(n,t);return{ast:n,render:r.render,staticRenderFns:r.staticRenderFns}},function(e){function t(t,n){var r=Object.create(e),i=[],o=[];if(r.warn=function(e,t){(t?o:i).push(e)},n)for(var a in n.modules&&(r.modules=(e.modules||[]).concat(n.modules)),n.directives&&(r.directives=O(Object.create(e.directives||null),n.directives)),n)"modules"!==a&&"directives"!==a&&(r[a]=n[a]);var s=Ea(t,r);return s.errors=i,s.tips=o,s}return{compile:t,compileToFunctions:function(e){var t=Object.create(null);return function(n,r,i){(r=O({},r)).warn,delete r.warn;var o=r.delimiters?String(r.delimiters)+n:n;if(t[o])return t[o];var a=e(n,r),s={},u=[];return s.render=Ca(a.render,u),s.staticRenderFns=a.staticRenderFns.map(function(e){return Ca(e,u)}),t[o]=s}}(t)}})(Go).compileToFunctions;function Sa(e){return(Ta=Ta||document.createElement("div")).innerHTML=e?'<a href="\n"/>':'<div a="\n"/>',Ta.innerHTML.indexOf("&#10;")>0}var ka=!!V&&Sa(!1),Oa=!!V&&Sa(!0),Da=w(function(e){var t=qn(e);return t&&t.innerHTML}),Ia=dn.prototype.$mount;dn.prototype.$mount=function(e,t){if((e=e&&qn(e))===document.body||e===document.documentElement)return this;var n=this.$options;if(!n.render){var r=n.template;if(r)if("string"==typeof r)"#"===r.charAt(0)&&(r=Da(r));else{if(!r.nodeType)return this;r=r.innerHTML}else e&&(r=function(e){if(e.outerHTML)return e.outerHTML;var t=document.createElement("div");return t.appendChild(e.cloneNode(!0)),t.innerHTML}(e));if(r){0;var i=Aa(r,{shouldDecodeNewlines:ka,shouldDecodeNewlinesForHref:Oa,delimiters:n.delimiters,comments:n.comments},this),o=i.render,a=i.staticRenderFns;n.render=o,n.staticRenderFns=a}}return Ia.call(this,e,t)},dn.compile=Aa,e.exports=dn}).call(t,n(1),n(37).setImmediate)},function(e,t,n){(function(e){var r=void 0!==e&&e||"undefined"!=typeof self&&self||window,i=Function.prototype.apply;function o(e,t){this._id=e,this._clearFn=t}t.setTimeout=function(){return new o(i.call(setTimeout,r,arguments),clearTimeout)},t.setInterval=function(){return new o(i.call(setInterval,r,arguments),clearInterval)},t.clearTimeout=t.clearInterval=function(e){e&&e.close()},o.prototype.unref=o.prototype.ref=function(){},o.prototype.close=function(){this._clearFn.call(r,this._id)},t.enroll=function(e,t){clearTimeout(e._idleTimeoutId),e._idleTimeout=t},t.unenroll=function(e){clearTimeout(e._idleTimeoutId),e._idleTimeout=-1},t._unrefActive=t.active=function(e){clearTimeout(e._idleTimeoutId);var t=e._idleTimeout;t>=0&&(e._idleTimeoutId=setTimeout(function(){e._onTimeout&&e._onTimeout()},t))},n(38),t.setImmediate="undefined"!=typeof self&&self.setImmediate||void 0!==e&&e.setImmediate||this&&this.setImmediate,t.clearImmediate="undefined"!=typeof self&&self.clearImmediate||void 0!==e&&e.clearImmediate||this&&this.clearImmediate}).call(t,n(1))},function(e,t,n){(function(e,t){!function(e,n){"use strict";if(!e.setImmediate){var r,i,o,a,s,u=1,c={},l=!1,f=e.document,p=Object.getPrototypeOf&&Object.getPrototypeOf(e);p=p&&p.setTimeout?p:e,"[object process]"==={}.toString.call(e.process)?r=function(e){t.nextTick(function(){h(e)})}:!function(){if(e.postMessage&&!e.importScripts){var t=!0,n=e.onmessage;return e.onmessage=function(){t=!1},e.postMessage("","*"),e.onmessage=n,t}}()?e.MessageChannel?((o=new MessageChannel).port1.onmessage=function(e){h(e.data)},r=function(e){o.port2.postMessage(e)}):f&&"onreadystatechange"in f.createElement("script")?(i=f.documentElement,r=function(e){var t=f.createElement("script");t.onreadystatechange=function(){h(e),t.onreadystatechange=null,i.removeChild(t),t=null},i.appendChild(t)}):r=function(e){setTimeout(h,0,e)}:(a="setImmediate$"+Math.random()+"$",s=function(t){t.source===e&&"string"==typeof t.data&&0===t.data.indexOf(a)&&h(+t.data.slice(a.length))},e.addEventListener?e.addEventListener("message",s,!1):e.attachEvent("onmessage",s),r=function(t){e.postMessage(a+t,"*")}),p.setImmediate=function(e){"function"!=typeof e&&(e=new Function(""+e));for(var t=new Array(arguments.length-1),n=0;n<t.length;n++)t[n]=arguments[n+1];var i={callback:e,args:t};return c[u]=i,r(u),u++},p.clearImmediate=d}function d(e){delete c[e]}function h(e){if(l)setTimeout(h,0,e);else{var t=c[e];if(t){l=!0;try{!function(e){var t=e.callback,r=e.args;switch(r.length){case 0:t();break;case 1:t(r[0]);break;case 2:t(r[0],r[1]);break;case 3:t(r[0],r[1],r[2]);break;default:t.apply(n,r)}}(t)}finally{d(e),l=!1}}}}}("undefined"==typeof self?void 0===e?this:e:self)}).call(t,n(1),n(6))},function(e,t,n){var r=n(40)(n(41),n(42),!1,null,null,null);e.exports=r.exports},function(e,t){e.exports=function(e,t,n,r,i,o){var a,s=e=e||{},u=typeof e.default;"object"!==u&&"function"!==u||(a=e,s=e.default);var c,l="function"==typeof s?s.options:s;if(t&&(l.render=t.render,l.staticRenderFns=t.staticRenderFns,l._compiled=!0),n&&(l.functional=!0),i&&(l._scopeId=i),o?(c=function(e){(e=e||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext)||"undefined"==typeof __VUE_SSR_CONTEXT__||(e=__VUE_SSR_CONTEXT__),r&&r.call(this,e),e&&e._registeredComponents&&e._registeredComponents.add(o)},l._ssrRegister=c):r&&(c=r),c){var f=l.functional,p=f?l.render:l.beforeCreate;f?(l._injectStyles=c,l.render=function(e,t){return c.call(t),p(e,t)}):l.beforeCreate=p?[].concat(p,c):[c]}return{esModule:a,exports:s,options:l}}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={mounted:function(){console.log("Component mounted.")}}},function(e,t){e.exports={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"container"},[t("div",{staticClass:"row justify-content-center"},[t("div",{staticClass:"col-md-8"},[t("div",{staticClass:"card card-default"},[t("div",{staticClass:"card-header"},[this._v("Example Component")]),this._v(" "),t("div",{staticClass:"card-body"},[this._v("\n                    I'm an example component.\n                ")])])])])])}]}},function(e,t){}]);

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
<p align="center"><img src="https://laravel.com/assets/img/components/logo-laravel.svg"></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://poser.pugx.org/laravel/framework/d/total.svg" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://poser.pugx.org/laravel/framework/v/stable.svg" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://poser.pugx.org/laravel/framework/license.svg" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel attempts to take the pain out of development by easing common tasks used in the majority of web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, yet powerful, providing tools needed for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of any modern web application framework, making it a breeze to get started learning the framework.

If you're not in the mood to read, [Laracasts](https://laracasts.com) contains over 1100 video tutorials on a range of topics including Laravel, modern PHP, unit testing, JavaScript, and more. Boost the skill level of yourself and your entire team by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for helping fund on-going Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell):

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[British Software Development](https://www.britishsoftware.co)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- [UserInsights](https://userinsights.com)
- [Fragrantica](https://www.fragrantica.com)
- [SOFTonSOFA](https://softonsofa.com/)
- [User10](https://user10.com)
- [Soumettre.fr](https://soumettre.fr/)
- [CodeBrisk](https://codebrisk.com)
- [1Forge](https://1forge.com)
- [TECPRESSO](https://tecpresso.co.jp/)
- [Runtime Converter](http://runtimeconverter.com/)
- [WebL'Agence](https://weblagence.com/)
- [Invoice Ninja](https://www.invoiceninja.com)
- [iMi digital](https://www.imi-digital.de/)
- [Earthlink](https://www.earthlink.ro/)
- [Steadfast Collective](https://steadfastcollective.com/)

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).


File: /resources\js\app.js

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

require('./bootstrap');

window.Vue = require('vue');

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

Vue.component('example-component', require('./components/ExampleComponent.vue'));

const app = new Vue({
    el: '#app'
});


File: /resources\js\bootstrap.js

window._ = require('lodash');
window.Popper = require('popper.js').default;

/**
 * We'll load jQuery and the Bootstrap jQuery plugin which provides support
 * for JavaScript based Bootstrap features such as modals and tabs. This
 * code may be modified to fit the specific needs of your application.
 */

try {
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (e) {}

/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Laravel back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

/**
 * Next we will register the CSRF Token as a common header with Axios so that
 * all outgoing HTTP requests automatically have it attached. This is just
 * a simple convenience so we don't have to attach every token manually.
 */

let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
} else {
    console.error('CSRF token not found: https://laravel.com/docs/csrf#csrf-x-csrf-token');
}

/**
 * Echo exposes an expressive API for subscribing to channels and listening
 * for events that are broadcast by Laravel. Echo and event broadcasting
 * allows your team to easily build robust real-time web applications.
 */

// import Echo from 'laravel-echo'

// window.Pusher = require('pusher-js');

// window.Echo = new Echo({
//     broadcaster: 'pusher',
//     key: process.env.MIX_PUSHER_APP_KEY,
//     cluster: process.env.MIX_PUSHER_APP_CLUSTER,
//     encrypted: true
// });


File: /resources\js\components\ExampleComponent.vue
<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">Example Component</div>

                    <div class="card-body">
                        I'm an example component.
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        }
    }
</script>


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

    'previous' => '« Previous',
    'next' => 'Next »',

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
    'after_or_equal'       => 'The :attribute must be a date after or equal to :date.',
    'alpha'                => 'The :attribute may only contain letters.',
    'alpha_dash'           => 'The :attribute may only contain letters, numbers, dashes and underscores.',
    'alpha_num'            => 'The :attribute may only contain letters and numbers.',
    'array'                => 'The :attribute must be an array.',
    'before'               => 'The :attribute must be a date before :date.',
    'before_or_equal'      => 'The :attribute must be a date before or equal to :date.',
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
    'dimensions'           => 'The :attribute has invalid image dimensions.',
    'distinct'             => 'The :attribute field has a duplicate value.',
    'email'                => 'The :attribute must be a valid email address.',
    'exists'               => 'The selected :attribute is invalid.',
    'file'                 => 'The :attribute must be a file.',
    'filled'               => 'The :attribute field must have a value.',
    'gt'                   => [
        'numeric' => 'The :attribute must be greater than :value.',
        'file'    => 'The :attribute must be greater than :value kilobytes.',
        'string'  => 'The :attribute must be greater than :value characters.',
        'array'   => 'The :attribute must have more than :value items.',
    ],
    'gte'                  => [
        'numeric' => 'The :attribute must be greater than or equal :value.',
        'file'    => 'The :attribute must be greater than or equal :value kilobytes.',
        'string'  => 'The :attribute must be greater than or equal :value characters.',
        'array'   => 'The :attribute must have :value items or more.',
    ],
    'image'                => 'The :attribute must be an image.',
    'in'                   => 'The selected :attribute is invalid.',
    'in_array'             => 'The :attribute field does not exist in :other.',
    'integer'              => 'The :attribute must be an integer.',
    'ip'                   => 'The :attribute must be a valid IP address.',
    'ipv4'                 => 'The :attribute must be a valid IPv4 address.',
    'ipv6'                 => 'The :attribute must be a valid IPv6 address.',
    'json'                 => 'The :attribute must be a valid JSON string.',
    'lt'                   => [
        'numeric' => 'The :attribute must be less than :value.',
        'file'    => 'The :attribute must be less than :value kilobytes.',
        'string'  => 'The :attribute must be less than :value characters.',
        'array'   => 'The :attribute must have less than :value items.',
    ],
    'lte'                  => [
        'numeric' => 'The :attribute must be less than or equal :value.',
        'file'    => 'The :attribute must be less than or equal :value kilobytes.',
        'string'  => 'The :attribute must be less than or equal :value characters.',
        'array'   => 'The :attribute must not have more than :value items.',
    ],
    'max'                  => [
        'numeric' => 'The :attribute may not be greater than :max.',
        'file'    => 'The :attribute may not be greater than :max kilobytes.',
        'string'  => 'The :attribute may not be greater than :max characters.',
        'array'   => 'The :attribute may not have more than :max items.',
    ],
    'mimes'                => 'The :attribute must be a file of type: :values.',
    'mimetypes'            => 'The :attribute must be a file of type: :values.',
    'min'                  => [
        'numeric' => 'The :attribute must be at least :min.',
        'file'    => 'The :attribute must be at least :min kilobytes.',
        'string'  => 'The :attribute must be at least :min characters.',
        'array'   => 'The :attribute must have at least :min items.',
    ],
    'not_in'               => 'The selected :attribute is invalid.',
    'not_regex'            => 'The :attribute format is invalid.',
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
    'uploaded'             => 'The :attribute failed to upload.',
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


File: /resources\sass\app.scss

// Fonts
@import url('https://fonts.googleapis.com/css?family=Nunito');

// Variables
@import 'variables';

// Bootstrap
@import '~bootstrap/scss/bootstrap';

.navbar-laravel {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
}


File: /resources\sass\_variables.scss

// Body
$body-bg: #f8fafc;

// Typography
$font-family-sans-serif: "Nunito", sans-serif;
$font-size-base: 0.9rem;
$line-height-base: 1.6;

// Colors
$blue: #3490dc;
$indigo: #6574cd;
$purple: #9561e2;
$pink: #f66D9b;
$red: #e3342f;
$orange: #f6993f;
$yellow: #ffed4a;
$green: #38c172;
$teal: #4dc0b5;
$cyan: #6cb2eb;


File: /resources\views\welcome.blade.php
<!doctype html>
<html lang="{{ app()->getLocale() }}">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet" type="text/css">

        <!-- Styles -->
        <style>
            html, body {
                background-color: #fff;
                color: #636b6f;
                font-family: 'Nunito', sans-serif;
                font-weight: 200;
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;
            }

            .links > a {
                color: #636b6f;
                padding: 0 25px;
                font-size: 12px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
            }

            .m-b-md {
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <div class="flex-center position-ref full-height">
            @if (Route::has('login'))
                <div class="top-right links">
                    @auth
                        <a href="{{ url('/home') }}">Home</a>
                    @else
                        <a href="{{ route('login') }}">Login</a>
                        <a href="{{ route('register') }}">Register</a>
                    @endauth
                </div>
            @endif

            <div class="content">
                <div class="title m-b-md">
                    Laravel
                </div>

                <div class="links">
                    <a href="https://laravel.com/docs">Documentation</a>
                    <a href="https://laracasts.com">Laracasts</a>
                    <a href="https://laravel-news.com">News</a>
                    <a href="https://nova.laravel.com">Nova</a>
                    <a href="https://forge.laravel.com">Forge</a>
                    <a href="https://github.com/laravel/laravel">GitHub</a>
                </div>
            </div>
        </div>
    </body>
</html>


File: /routes\api.php
<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});


File: /routes\channels.php
<?php

/*
|--------------------------------------------------------------------------
| Broadcast Channels
|--------------------------------------------------------------------------
|
| Here you may register all of the event broadcasting channels that your
| application supports. The given channel authorization callbacks are
| used to check if an authenticated user can listen to the channel.
|
*/

Broadcast::channel('App.User.{id}', function ($user, $id) {
    return (int) $user->id === (int) $id;
});


File: /routes\console.php
<?php

use Illuminate\Foundation\Inspiring;

/*
|--------------------------------------------------------------------------
| Console Routes
|--------------------------------------------------------------------------
|
| This file is where you may define all of your Closure based console
| commands. Each Closure is bound to a command instance allowing a
| simple approach to interacting with each command's IO methods.
|
*/

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->describe('Display an inspiring quote');


File: /routes\web.php
<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/','BelajarController@tes_koneksi');
Route::get('/ping','BelajarController@ping');


File: /server.php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylor@laravel.com>
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


File: /storage\framework\testing\.gitignore
*
!.gitignore


File: /storage\framework\views\.gitignore
*
!.gitignore


File: /storage\logs\.gitignore
*
!.gitignore


File: /tests\CreatesApplication.php
<?php

namespace Tests;

use Illuminate\Contracts\Console\Kernel;

trait CreatesApplication
{
    /**
     * Creates the application.
     *
     * @return \Illuminate\Foundation\Application
     */
    public function createApplication()
    {
        $app = require __DIR__.'/../bootstrap/app.php';

        $app->make(Kernel::class)->bootstrap();

        return $app;
    }
}


File: /tests\Feature\ExampleTest.php
<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testBasicTest()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }
}


File: /tests\TestCase.php
<?php

namespace Tests;

use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    use CreatesApplication;
}


File: /tests\Unit\ExampleTest.php
<?php

namespace Tests\Unit;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testBasicTest()
    {
        $this->assertTrue(true);
    }
}


File: /webpack.mix.js
const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/js/app.js', 'public/js')
   .sass('resources/sass/app.scss', 'public/css');


