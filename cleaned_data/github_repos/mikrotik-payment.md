# Repository Information
Name: mikrotik-payment

# Directory Structure
Directory structure:
└── github_repos/mikrotik-payment/
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
    │   │       ├── pack-fa29a253c29d17c245d88ee99cd2b1332a5fd537.idx
    │   │       └── pack-fa29a253c29d17c245d88ee99cd2b1332a5fd537.pack
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
    ├── .styleci.yml
    ├── app/
    │   ├── Console/
    │   │   └── Kernel.php
    │   ├── Exceptions/
    │   │   └── Handler.php
    │   ├── Http/
    │   │   ├── Controllers/
    │   │   │   ├── Controller.php
    │   │   │   └── MpesaController.php
    │   │   ├── Kernel.php
    │   │   └── Middleware/
    │   │       ├── Authenticate.php
    │   │       ├── EncryptCookies.php
    │   │       ├── PreventRequestsDuringMaintenance.php
    │   │       ├── RedirectIfAuthenticated.php
    │   │       ├── TrimStrings.php
    │   │       ├── TrustHosts.php
    │   │       ├── TrustProxies.php
    │   │       └── VerifyCsrfToken.php
    │   ├── Models/
    │   │   └── User.php
    │   └── Providers/
    │       ├── AppServiceProvider.php
    │       ├── AuthServiceProvider.php
    │       ├── BroadcastServiceProvider.php
    │       ├── EventServiceProvider.php
    │       └── RouteServiceProvider.php
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
    │   ├── cors.php
    │   ├── database.php
    │   ├── filesystems.php
    │   ├── hashing.php
    │   ├── logging.php
    │   ├── mail.php
    │   ├── queue.php
    │   ├── sanctum.php
    │   ├── services.php
    │   ├── session.php
    │   └── view.php
    ├── database/
    │   ├── .gitignore
    │   ├── factories/
    │   │   └── UserFactory.php
    │   ├── migrations/
    │   │   ├── 2014_10_12_000000_create_users_table.php
    │   │   ├── 2014_10_12_100000_create_password_resets_table.php
    │   │   ├── 2019_08_19_000000_create_failed_jobs_table.php
    │   │   └── 2019_12_14_000001_create_personal_access_tokens_table.php
    │   └── seeders/
    │       └── DatabaseSeeder.php
    ├── mikrotik-payment/
    │   ├── .editorconfig
    │   ├── .env.example
    │   ├── .gitattributes
    │   ├── .gitignore
    │   ├── .styleci.yml
    │   ├── app/
    │   │   ├── Console/
    │   │   │   └── Kernel.php
    │   │   ├── Exceptions/
    │   │   │   └── Handler.php
    │   │   ├── Http/
    │   │   │   ├── Controllers/
    │   │   │   │   └── Controller.php
    │   │   │   ├── Kernel.php
    │   │   │   └── Middleware/
    │   │   │       ├── Authenticate.php
    │   │   │       ├── EncryptCookies.php
    │   │   │       ├── PreventRequestsDuringMaintenance.php
    │   │   │       ├── RedirectIfAuthenticated.php
    │   │   │       ├── TrimStrings.php
    │   │   │       ├── TrustHosts.php
    │   │   │       ├── TrustProxies.php
    │   │   │       └── VerifyCsrfToken.php
    │   │   ├── Models/
    │   │   │   └── User.php
    │   │   └── Providers/
    │   │       ├── AppServiceProvider.php
    │   │       ├── AuthServiceProvider.php
    │   │       ├── BroadcastServiceProvider.php
    │   │       ├── EventServiceProvider.php
    │   │       └── RouteServiceProvider.php
    │   ├── artisan
    │   ├── bootstrap/
    │   │   ├── app.php
    │   │   └── cache/
    │   │       └── .gitignore
    │   ├── composer.json
    │   ├── composer.lock
    │   ├── config/
    │   │   ├── app.php
    │   │   ├── auth.php
    │   │   ├── broadcasting.php
    │   │   ├── cache.php
    │   │   ├── cors.php
    │   │   ├── database.php
    │   │   ├── filesystems.php
    │   │   ├── hashing.php
    │   │   ├── logging.php
    │   │   ├── mail.php
    │   │   ├── queue.php
    │   │   ├── sanctum.php
    │   │   ├── services.php
    │   │   ├── session.php
    │   │   └── view.php
    │   ├── database/
    │   │   ├── .gitignore
    │   │   ├── factories/
    │   │   │   └── UserFactory.php
    │   │   ├── migrations/
    │   │   │   ├── 2014_10_12_000000_create_users_table.php
    │   │   │   ├── 2014_10_12_100000_create_password_resets_table.php
    │   │   │   ├── 2019_08_19_000000_create_failed_jobs_table.php
    │   │   │   └── 2019_12_14_000001_create_personal_access_tokens_table.php
    │   │   └── seeders/
    │   │       └── DatabaseSeeder.php
    │   ├── package.json
    │   ├── phpunit.xml
    │   ├── public/
    │   │   ├── .htaccess
    │   │   ├── index.php
    │   │   ├── robots.txt
    │   │   └── web.config
    │   ├── README.md
    │   ├── resources/
    │   │   ├── css/
    │   │   │   └── app.css
    │   │   ├── js/
    │   │   │   ├── app.js
    │   │   │   └── bootstrap.js
    │   │   ├── lang/
    │   │   │   └── en/
    │   │   │       ├── auth.php
    │   │   │       ├── pagination.php
    │   │   │       ├── passwords.php
    │   │   │       └── validation.php
    │   │   └── views/
    │   │       └── welcome.blade.php
    │   ├── routes/
    │   │   ├── api.php
    │   │   ├── channels.php
    │   │   ├── console.php
    │   │   └── web.php
    │   ├── server.php
    │   ├── storage/
    │   │   ├── app/
    │   │   │   ├── .gitignore
    │   │   │   └── public/
    │   │   │       └── .gitignore
    │   │   ├── framework/
    │   │   │   ├── .gitignore
    │   │   │   ├── cache/
    │   │   │   │   ├── .gitignore
    │   │   │   │   └── data/
    │   │   │   │       └── .gitignore
    │   │   │   ├── sessions/
    │   │   │   │   └── .gitignore
    │   │   │   ├── testing/
    │   │   │   │   └── .gitignore
    │   │   │   └── views/
    │   │   │       └── .gitignore
    │   │   └── logs/
    │   │       └── .gitignore
    │   ├── tests/
    │   │   ├── CreatesApplication.php
    │   │   ├── Feature/
    │   │   │   └── ExampleTest.php
    │   │   ├── TestCase.php
    │   │   └── Unit/
    │   │       └── ExampleTest.php
    │   └── webpack.mix.js
    ├── package.json
    ├── phpunit.xml
    ├── Procfile
    ├── public/
    │   ├── .htaccess
    │   ├── index.php
    │   ├── robots.txt
    │   └── web.config
    ├── README.md
    ├── resources/
    │   ├── css/
    │   │   └── app.css
    │   ├── js/
    │   │   ├── app.js
    │   │   └── bootstrap.js
    │   ├── lang/
    │   │   └── en/
    │   │       ├── auth.php
    │   │       ├── pagination.php
    │   │       ├── passwords.php
    │   │       └── validation.php
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
    │   │   │   ├── .gitignore
    │   │   │   └── data/
    │   │   │       └── .gitignore
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

[*.{yml,yaml}]
indent_size = 2

[docker-compose.yml]
indent_size = 4


File: /.env.example
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
FILESYSTEM_DRIVER=local
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=null
MAIL_FROM_NAME="${APP_NAME}"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=
AWS_USE_PATH_STYLE_ENDPOINT=false

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
	url = https://github.com/MarkDann/mikrotik-payment.git
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
0000000000000000000000000000000000000000 37df3ed062e0181aff8b9ea56021682f8b50dbe4 vivek-dodia <vivek.dodia@icloud.com> 1738606400 -0500	clone: from https://github.com/MarkDann/mikrotik-payment.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 37df3ed062e0181aff8b9ea56021682f8b50dbe4 vivek-dodia <vivek.dodia@icloud.com> 1738606400 -0500	clone: from https://github.com/MarkDann/mikrotik-payment.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 37df3ed062e0181aff8b9ea56021682f8b50dbe4 vivek-dodia <vivek.dodia@icloud.com> 1738606400 -0500	clone: from https://github.com/MarkDann/mikrotik-payment.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
37df3ed062e0181aff8b9ea56021682f8b50dbe4 refs/remotes/origin/master


File: /.git\refs\heads\master
37df3ed062e0181aff8b9ea56021682f8b50dbe4


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
.env
.env.backup
.phpunit.result.cache
docker-compose.override.yml
Homestead.json
Homestead.yaml
File: /.styleci.yml
php:
  preset: laravel
  version: 8
  disabled:
    - no_unused_imports
  finder:
    not-name:
      - index.php
      - server.php
js:
  finder:
    not-name:
      - webpack.mix.js
css: true


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
        // $schedule->command('inspire')->hourly();
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

use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Throwable;

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
        'current_password',
        'password',
        'password_confirmation',
    ];

    /**
     * Register the exception handling callbacks for the application.
     *
     * @return void
     */
    public function register()
    {
        $this->reportable(function (Throwable $e) {
            //
        });
    }
}


File: /app\Http\Controllers\Controller.php
<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
}


File: /app\Http\Controllers\MpesaController.php
<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Mpesa;


class MpesaController extends Controller
{ //function to initiate a transaction
    public function stkSimulation( Request $request){
        //to check all the datas dumped from the form
        //if your want to get single element,someName in this case
        $amount = $request->amount; 
        $phone=$request->phone;
        //dd($phone,$amount);

    $mpesa= new \Safaricom\Mpesa\Mpesa();

    $BusinessShortCode =174379;
    $LipaNaMpesaPasskey="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919";
    $TransactionType="CustomerPayBillOnline";
    $Amount=$amount;
    $PartyA=$phone;
    $PartyB=174379; 
    $PhoneNumber=$phone;
    $CallBackURL="https://fbbd-105-163-175-148.ngrok.io/api/mpesa/stkpush/response";
    $AccountReference="Legendwifi";
    $TransactionDesc="Internet Payment";
    $Remarks="Thank you for choosing us";


    $stkPushSimulation=$mpesa->STKPushSimulation(
        $BusinessShortCode, 
        $LipaNaMpesaPasskey, 
        $TransactionType, 
        $Amount,
        $PartyA,
        $PartyB, 
        $PhoneNumber, 
        $CallBackURL,
        $AccountReference,
        $TransactionDesc,
        $Remarks
    );
dd($stkPushSimulation);
    
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
        // \App\Http\Middleware\TrustHosts::class,
        \App\Http\Middleware\TrustProxies::class,
        \Fruitcake\Cors\HandleCors::class,
        \App\Http\Middleware\PreventRequestsDuringMaintenance::class,
        \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
        \App\Http\Middleware\TrimStrings::class,
        \Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull::class,
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
            // \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
            'throttle:api',
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
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
        'cache.headers' => \Illuminate\Http\Middleware\SetCacheHeaders::class,
        'can' => \Illuminate\Auth\Middleware\Authorize::class,
        'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
        'password.confirm' => \Illuminate\Auth\Middleware\RequirePassword::class,
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
     * @return string|null
     */
    protected function redirectTo($request)
    {
        if (! $request->expectsJson()) {
            return route('login');
        }
    }
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


File: /app\Http\Middleware\PreventRequestsDuringMaintenance.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance as Middleware;

class PreventRequestsDuringMaintenance extends Middleware
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


File: /app\Http\Middleware\RedirectIfAuthenticated.php
<?php

namespace App\Http\Middleware;

use App\Providers\RouteServiceProvider;
use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class RedirectIfAuthenticated
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @param  string|null  ...$guards
     * @return mixed
     */
    public function handle(Request $request, Closure $next, ...$guards)
    {
        $guards = empty($guards) ? [null] : $guards;

        foreach ($guards as $guard) {
            if (Auth::guard($guard)->check()) {
                return redirect(RouteServiceProvider::HOME);
            }
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
        'current_password',
        'password',
        'password_confirmation',
    ];
}


File: /app\Http\Middleware\TrustHosts.php
<?php

namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustHosts as Middleware;

class TrustHosts extends Middleware
{
    /**
     * Get the host patterns that should be trusted.
     *
     * @return array
     */
    public function hosts()
    {
        return [
            $this->allSubdomainsOfApplicationUrl(),
        ];
    }
}


File: /app\Http\Middleware\TrustProxies.php
<?php

namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustProxies as Middleware;
use Illuminate\Http\Request;

class TrustProxies extends Middleware
{
    /**
     * The trusted proxies for this application.
     *
     * @var array|string|null
     */
    protected $proxies;

    /**
     * The headers that should be used to detect proxies.
     *
     * @var int
     */
    protected $headers = Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_HOST | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO | Request::HEADER_X_FORWARDED_AWS_ELB;
}


File: /app\Http\Middleware\VerifyCsrfToken.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
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


File: /app\Models\User.php
<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];
}


File: /app\Providers\AppServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    }

    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }
}


File: /app\Providers\AuthServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Gate;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array
     */
    protected $policies = [
        // 'App\Models\Model' => 'App\Policies\ModelPolicy',
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

use Illuminate\Support\Facades\Broadcast;
use Illuminate\Support\ServiceProvider;

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

use Illuminate\Auth\Events\Registered;
use Illuminate\Auth\Listeners\SendEmailVerificationNotification;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Event;

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
        //
    }
}


File: /app\Providers\RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Illuminate\Support\Facades\Route;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * The path to the "home" route for your application.
     *
     * This is used by Laravel authentication to redirect users after login.
     *
     * @var string
     */
    public const HOME = '/home';

    /**
     * The controller namespace for the application.
     *
     * When present, controller route declarations will automatically be prefixed with this namespace.
     *
     * @var string|null
     */
    // protected $namespace = 'App\\Http\\Controllers';

    /**
     * Define your route model bindings, pattern filters, etc.
     *
     * @return void
     */
    public function boot()
    {
        $this->configureRateLimiting();

        $this->routes(function () {
            Route::prefix('api')
                ->middleware('api')
                ->namespace($this->namespace)
                ->group(base_path('routes/api.php'));

            Route::middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/web.php'));
        });
    }

    /**
     * Configure the rate limiters for the application.
     *
     * @return void
     */
    protected function configureRateLimiting()
    {
        RateLimiter::for('api', function (Request $request) {
            return Limit::perMinute(60)->by(optional($request->user())->id ?: $request->ip());
        });
    }
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
| loading of any of our classes manually. It's great to relax.
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
    $_ENV['APP_BASE_PATH'] ?? dirname(__DIR__)
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
    "type": "project",
    "description": "The Laravel Framework.",
    "keywords": ["framework", "laravel"],
    "license": "MIT",
    "require": {
        "php": "^7.3|^8.0",
        "fruitcake/laravel-cors": "^2.0",
        "guzzlehttp/guzzle": "^7.0.1",
        "laravel/framework": "^8.54",
        "laravel/sanctum": "^2.11",
        "laravel/tinker": "^2.5",
        "safaricom/mpesa": "^1.0"
    },
    "require-dev": {
        "facade/ignition": "^2.5",
        "fakerphp/faker": "^1.9.1",
        "laravel/sail": "^1.0.1",
        "mockery/mockery": "^1.4.2",
        "nunomaduro/collision": "^5.0",
        "phpunit/phpunit": "^9.3.3"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true
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
    "content-hash": "5b6c203a028fadb9e08a8431b99b134d",
    "packages": [
        {
            "name": "asm89/stack-cors",
            "version": "v2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/asm89/stack-cors.git",
                "reference": "9cb795bf30988e8c96dd3c40623c48a877bc6714"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/asm89/stack-cors/zipball/9cb795bf30988e8c96dd3c40623c48a877bc6714",
                "reference": "9cb795bf30988e8c96dd3c40623c48a877bc6714",
                "shasum": ""
            },
            "require": {
                "php": "^7.0|^8.0",
                "symfony/http-foundation": "~2.7|~3.0|~4.0|~5.0",
                "symfony/http-kernel": "~2.7|~3.0|~4.0|~5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6|^7|^8|^9",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Asm89\\Stack\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alexander",
                    "email": "iam.asm89@gmail.com"
                }
            ],
            "description": "Cross-origin resource sharing library and stack middleware",
            "homepage": "https://github.com/asm89/stack-cors",
            "keywords": [
                "cors",
                "stack"
            ],
            "support": {
                "issues": "https://github.com/asm89/stack-cors/issues",
                "source": "https://github.com/asm89/stack-cors/tree/v2.0.3"
            },
            "time": "2021-03-11T06:42:03+00:00"
        },
        {
            "name": "brick/math",
            "version": "0.9.3",
            "source": {
                "type": "git",
                "url": "https://github.com/brick/math.git",
                "reference": "ca57d18f028f84f777b2168cd1911b0dee2343ae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/brick/math/zipball/ca57d18f028f84f777b2168cd1911b0dee2343ae",
                "reference": "ca57d18f028f84f777b2168cd1911b0dee2343ae",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.2",
                "phpunit/phpunit": "^7.5.15 || ^8.5 || ^9.0",
                "vimeo/psalm": "4.9.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Brick\\Math\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Arbitrary-precision arithmetic library",
            "keywords": [
                "Arbitrary-precision",
                "BigInteger",
                "BigRational",
                "arithmetic",
                "bigdecimal",
                "bignum",
                "brick",
                "math"
            ],
            "support": {
                "issues": "https://github.com/brick/math/issues",
                "source": "https://github.com/brick/math/tree/0.9.3"
            },
            "funding": [
                {
                    "url": "https://github.com/BenMorel",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/brick/math",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-15T20:50:18+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "9cf661f4eb38f7c881cac67c75ea9b00bf97b210"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/9cf661f4eb38f7c881cac67c75ea9b00bf97b210",
                "reference": "9cf661f4eb38f7c881cac67c75ea9b00bf97b210",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^7.0",
                "phpstan/phpstan": "^0.11",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpstan/phpstan-strict-rules": "^0.11",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Inflector\\": "lib/Doctrine/Inflector"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
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
            "description": "PHP Doctrine Inflector is a small library that can perform string manipulations with regard to upper/lowercase and singular/plural forms of words.",
            "homepage": "https://www.doctrine-project.org/projects/inflector.html",
            "keywords": [
                "inflection",
                "inflector",
                "lowercase",
                "manipulation",
                "php",
                "plural",
                "singular",
                "strings",
                "uppercase",
                "words"
            ],
            "support": {
                "issues": "https://github.com/doctrine/inflector/issues",
                "source": "https://github.com/doctrine/inflector/tree/2.0.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finflector",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-29T15:13:26+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/e864bbf5904cb8f5bb334f99209b48018522f042",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.11.8",
                "phpunit/phpunit": "^8.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Lexer\\": "lib/Doctrine/Common/Lexer"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Lexer parser library that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "https://www.doctrine-project.org/projects/lexer.html",
            "keywords": [
                "annotations",
                "docblock",
                "lexer",
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/lexer/issues",
                "source": "https://github.com/doctrine/lexer/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Flexer",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-25T17:44:05+00:00"
        },
        {
            "name": "dragonmantank/cron-expression",
            "version": "v3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/dragonmantank/cron-expression.git",
                "reference": "7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dragonmantank/cron-expression/zipball/7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c",
                "reference": "7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c",
                "shasum": ""
            },
            "require": {
                "php": "^7.2|^8.0",
                "webmozart/assert": "^1.7.0"
            },
            "replace": {
                "mtdowling/cron-expression": "^1.0"
            },
            "require-dev": {
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-webmozart-assert": "^0.12.7",
                "phpunit/phpunit": "^7.0|^8.0|^9.0"
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
            "support": {
                "issues": "https://github.com/dragonmantank/cron-expression/issues",
                "source": "https://github.com/dragonmantank/cron-expression/tree/v3.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/dragonmantank",
                    "type": "github"
                }
            ],
            "time": "2020-11-24T19:55:57+00:00"
        },
        {
            "name": "egulias/email-validator",
            "version": "2.1.25",
            "source": {
                "type": "git",
                "url": "https://github.com/egulias/EmailValidator.git",
                "reference": "0dbf5d78455d4d6a41d186da50adc1122ec066f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/egulias/EmailValidator/zipball/0dbf5d78455d4d6a41d186da50adc1122ec066f4",
                "reference": "0dbf5d78455d4d6a41d186da50adc1122ec066f4",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "^1.0.1",
                "php": ">=5.5",
                "symfony/polyfill-intl-idn": "^1.10"
            },
            "require-dev": {
                "dominicsayers/isemail": "^3.0.7",
                "phpunit/phpunit": "^4.8.36|^7.5.15",
                "satooshi/php-coveralls": "^1.0.1"
            },
            "suggest": {
                "ext-intl": "PHP Internationalization Libraries are required to use the SpoofChecking validation"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Egulias\\EmailValidator\\": "src"
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
            "support": {
                "issues": "https://github.com/egulias/EmailValidator/issues",
                "source": "https://github.com/egulias/EmailValidator/tree/2.1.25"
            },
            "funding": [
                {
                    "url": "https://github.com/egulias",
                    "type": "github"
                }
            ],
            "time": "2020-12-29T14:50:06+00:00"
        },
        {
            "name": "fruitcake/laravel-cors",
            "version": "v2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/fruitcake/laravel-cors.git",
                "reference": "a8ccedc7ca95189ead0e407c43b530dc17791d6a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fruitcake/laravel-cors/zipball/a8ccedc7ca95189ead0e407c43b530dc17791d6a",
                "reference": "a8ccedc7ca95189ead0e407c43b530dc17791d6a",
                "shasum": ""
            },
            "require": {
                "asm89/stack-cors": "^2.0.1",
                "illuminate/contracts": "^6|^7|^8|^9",
                "illuminate/support": "^6|^7|^8|^9",
                "php": ">=7.2",
                "symfony/http-foundation": "^4|^5",
                "symfony/http-kernel": "^4.3.4|^5"
            },
            "require-dev": {
                "laravel/framework": "^6|^7|^8",
                "orchestra/testbench-dusk": "^4|^5|^6|^7",
                "phpunit/phpunit": "^6|^7|^8|^9",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                },
                "laravel": {
                    "providers": [
                        "Fruitcake\\Cors\\CorsServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Fruitcake\\Cors\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fruitcake",
                    "homepage": "https://fruitcake.nl"
                },
                {
                    "name": "Barry vd. Heuvel",
                    "email": "barryvdh@gmail.com"
                }
            ],
            "description": "Adds CORS (Cross-Origin Resource Sharing) headers support in your Laravel application",
            "keywords": [
                "api",
                "cors",
                "crossdomain",
                "laravel"
            ],
            "support": {
                "issues": "https://github.com/fruitcake/laravel-cors/issues",
                "source": "https://github.com/fruitcake/laravel-cors/tree/v2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/barryvdh",
                    "type": "github"
                }
            ],
            "time": "2021-04-26T11:24:25+00:00"
        },
        {
            "name": "graham-campbell/result-type",
            "version": "v1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/GrahamCampbell/Result-Type.git",
                "reference": "7e279d2cd5d7fbb156ce46daada972355cea27bb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/GrahamCampbell/Result-Type/zipball/7e279d2cd5d7fbb156ce46daada972355cea27bb",
                "reference": "7e279d2cd5d7fbb156ce46daada972355cea27bb",
                "shasum": ""
            },
            "require": {
                "php": "^7.0|^8.0",
                "phpoption/phpoption": "^1.7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.5|^7.5|^8.5|^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GrahamCampbell\\ResultType\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com"
                }
            ],
            "description": "An Implementation Of The Result Type",
            "keywords": [
                "Graham Campbell",
                "GrahamCampbell",
                "Result Type",
                "Result-Type",
                "result"
            ],
            "support": {
                "issues": "https://github.com/GrahamCampbell/Result-Type/issues",
                "source": "https://github.com/GrahamCampbell/Result-Type/tree/v1.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/graham-campbell/result-type",
                    "type": "tidelift"
                }
            ],
            "time": "2020-04-13T13:17:36+00:00"
        },
        {
            "name": "guzzlehttp/guzzle",
            "version": "7.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/guzzle.git",
                "reference": "7008573787b430c1c1f650e3722d9bba59967628"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/guzzle/zipball/7008573787b430c1c1f650e3722d9bba59967628",
                "reference": "7008573787b430c1c1f650e3722d9bba59967628",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "guzzlehttp/promises": "^1.4",
                "guzzlehttp/psr7": "^1.7 || ^2.0",
                "php": "^7.2.5 || ^8.0",
                "psr/http-client": "^1.0"
            },
            "provide": {
                "psr/http-client-implementation": "1.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-curl": "*",
                "php-http/client-integration-tests": "^3.0",
                "phpunit/phpunit": "^8.5.5 || ^9.3.5",
                "psr/log": "^1.1"
            },
            "suggest": {
                "ext-curl": "Required for CURL handler support",
                "ext-intl": "Required for Internationalized Domain Name (IDN) support",
                "psr/log": "Required for using the Log middleware"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "7.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://sagikazarmark.hu"
                }
            ],
            "description": "Guzzle is a PHP HTTP client library",
            "homepage": "http://guzzlephp.org/",
            "keywords": [
                "client",
                "curl",
                "framework",
                "http",
                "http client",
                "psr-18",
                "psr-7",
                "rest",
                "web service"
            ],
            "support": {
                "issues": "https://github.com/guzzle/guzzle/issues",
                "source": "https://github.com/guzzle/guzzle/tree/7.3.0"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://github.com/Nyholm",
                    "type": "github"
                },
                {
                    "url": "https://github.com/alexeyshockov",
                    "type": "github"
                },
                {
                    "url": "https://github.com/gmponos",
                    "type": "github"
                }
            ],
            "time": "2021-03-23T11:33:13+00:00"
        },
        {
            "name": "guzzlehttp/promises",
            "version": "1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/promises.git",
                "reference": "8e7d04f1f6450fef59366c399cfad4b9383aa30d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/promises/zipball/8e7d04f1f6450fef59366c399cfad4b9383aa30d",
                "reference": "8e7d04f1f6450fef59366c399cfad4b9383aa30d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "symfony/phpunit-bridge": "^4.4 || ^5.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Promise\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
            "description": "Guzzle promises library",
            "keywords": [
                "promise"
            ],
            "support": {
                "issues": "https://github.com/guzzle/promises/issues",
                "source": "https://github.com/guzzle/promises/tree/1.4.1"
            },
            "time": "2021-03-07T09:25:29+00:00"
        },
        {
            "name": "guzzlehttp/psr7",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/psr7.git",
                "reference": "1dc8d9cba3897165e16d12bb13d813afb1eb3fe7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/psr7/zipball/1dc8d9cba3897165e16d12bb13d813afb1eb3fe7",
                "reference": "1dc8d9cba3897165e16d12bb13d813afb1eb3fe7",
                "shasum": ""
            },
            "require": {
                "php": "^7.2.5 || ^8.0",
                "psr/http-factory": "^1.0",
                "psr/http-message": "^1.0",
                "ralouphie/getallheaders": "^3.0"
            },
            "provide": {
                "psr/http-factory-implementation": "1.0",
                "psr/http-message-implementation": "1.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "http-interop/http-factory-tests": "^0.9",
                "phpunit/phpunit": "^8.5.8 || ^9.3.10"
            },
            "suggest": {
                "laminas/laminas-httphandlerrunner": "Emit PSR-7 responses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Psr7\\": "src/"
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
                    "name": "Tobias Schultze",
                    "homepage": "https://github.com/Tobion"
                },
                {
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://sagikazarmark.hu"
                }
            ],
            "description": "PSR-7 message implementation that also provides common utility methods",
            "keywords": [
                "http",
                "message",
                "psr-7",
                "request",
                "response",
                "stream",
                "uri",
                "url"
            ],
            "support": {
                "issues": "https://github.com/guzzle/psr7/issues",
                "source": "https://github.com/guzzle/psr7/tree/2.0.0"
            },
            "time": "2021-06-30T20:03:07+00:00"
        },
        {
            "name": "laravel/framework",
            "version": "v8.55.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/framework.git",
                "reference": "997e2aa23e9103137715018ae926c52f8a1703f2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/framework/zipball/997e2aa23e9103137715018ae926c52f8a1703f2",
                "reference": "997e2aa23e9103137715018ae926c52f8a1703f2",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.4|^2.0",
                "dragonmantank/cron-expression": "^3.0.2",
                "egulias/email-validator": "^2.1.10",
                "ext-json": "*",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "league/commonmark": "^1.3|^2.0",
                "league/flysystem": "^1.1",
                "monolog/monolog": "^2.0",
                "nesbot/carbon": "^2.31",
                "opis/closure": "^3.6",
                "php": "^7.3|^8.0",
                "psr/container": "^1.0",
                "psr/simple-cache": "^1.0",
                "ramsey/uuid": "^4.0",
                "swiftmailer/swiftmailer": "^6.0",
                "symfony/console": "^5.1.4",
                "symfony/error-handler": "^5.1.4",
                "symfony/finder": "^5.1.4",
                "symfony/http-foundation": "^5.1.4",
                "symfony/http-kernel": "^5.1.4",
                "symfony/mime": "^5.1.4",
                "symfony/process": "^5.1.4",
                "symfony/routing": "^5.1.4",
                "symfony/var-dumper": "^5.1.4",
                "tijsverkoyen/css-to-inline-styles": "^2.2.2",
                "vlucas/phpdotenv": "^5.2",
                "voku/portable-ascii": "^1.4.8"
            },
            "conflict": {
                "tightenco/collect": "<5.5.33"
            },
            "provide": {
                "psr/container-implementation": "1.0"
            },
            "replace": {
                "illuminate/auth": "self.version",
                "illuminate/broadcasting": "self.version",
                "illuminate/bus": "self.version",
                "illuminate/cache": "self.version",
                "illuminate/collections": "self.version",
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
                "illuminate/macroable": "self.version",
                "illuminate/mail": "self.version",
                "illuminate/notifications": "self.version",
                "illuminate/pagination": "self.version",
                "illuminate/pipeline": "self.version",
                "illuminate/queue": "self.version",
                "illuminate/redis": "self.version",
                "illuminate/routing": "self.version",
                "illuminate/session": "self.version",
                "illuminate/support": "self.version",
                "illuminate/testing": "self.version",
                "illuminate/translation": "self.version",
                "illuminate/validation": "self.version",
                "illuminate/view": "self.version"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^3.189.0",
                "doctrine/dbal": "^2.6|^3.0",
                "filp/whoops": "^2.8",
                "guzzlehttp/guzzle": "^6.5.5|^7.0.1",
                "league/flysystem-cached-adapter": "^1.0",
                "mockery/mockery": "^1.4.2",
                "orchestra/testbench-core": "^6.23",
                "pda/pheanstalk": "^4.0",
                "phpunit/phpunit": "^8.5.8|^9.3.3",
                "predis/predis": "^1.1.2",
                "symfony/cache": "^5.1.4"
            },
            "suggest": {
                "aws/aws-sdk-php": "Required to use the SQS queue driver, DynamoDb failed job storage and SES mail driver (^3.189.0).",
                "brianium/paratest": "Required to run tests in parallel (^6.0).",
                "doctrine/dbal": "Required to rename columns and drop SQLite columns (^2.6|^3.0).",
                "ext-ftp": "Required to use the Flysystem FTP driver.",
                "ext-gd": "Required to use Illuminate\\Http\\Testing\\FileFactory::image().",
                "ext-memcached": "Required to use the memcache cache driver.",
                "ext-pcntl": "Required to use all features of the queue worker.",
                "ext-posix": "Required to use all features of the queue worker.",
                "ext-redis": "Required to use the Redis cache and queue drivers (^4.0|^5.0).",
                "fakerphp/faker": "Required to use the eloquent factory builder (^1.9.1).",
                "filp/whoops": "Required for friendly error pages in development (^2.8).",
                "guzzlehttp/guzzle": "Required to use the HTTP Client, Mailgun mail driver and the ping methods on schedules (^6.5.5|^7.0.1).",
                "laravel/tinker": "Required to use the tinker console command (^2.0).",
                "league/flysystem-aws-s3-v3": "Required to use the Flysystem S3 driver (^1.0).",
                "league/flysystem-cached-adapter": "Required to use the Flysystem cache (^1.0).",
                "league/flysystem-sftp": "Required to use the Flysystem SFTP driver (^1.0).",
                "mockery/mockery": "Required to use mocking (^1.4.2).",
                "nyholm/psr7": "Required to use PSR-7 bridging features (^1.2).",
                "pda/pheanstalk": "Required to use the beanstalk queue driver (^4.0).",
                "phpunit/phpunit": "Required to use assertions and run tests (^8.5.8|^9.3.3).",
                "predis/predis": "Required to use the predis connector (^1.1.2).",
                "psr/http-message": "Required to allow Storage::put to accept a StreamInterface (^1.0).",
                "pusher/pusher-php-server": "Required to use the Pusher broadcast driver (^4.0|^5.0|^6.0).",
                "symfony/cache": "Required to PSR-6 cache bridge (^5.1.4).",
                "symfony/filesystem": "Required to enable support for relative symbolic links (^5.1.4).",
                "symfony/psr-http-message-bridge": "Required to use PSR-7 bridging features (^2.0).",
                "wildbit/swiftmailer-postmark": "Required to use Postmark mail driver (^3.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "8.x-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/Illuminate/Collections/helpers.php",
                    "src/Illuminate/Events/functions.php",
                    "src/Illuminate/Foundation/helpers.php",
                    "src/Illuminate/Support/helpers.php"
                ],
                "psr-4": {
                    "Illuminate\\": "src/Illuminate/",
                    "Illuminate\\Support\\": [
                        "src/Illuminate/Macroable/",
                        "src/Illuminate/Collections/"
                    ]
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
            "support": {
                "issues": "https://github.com/laravel/framework/issues",
                "source": "https://github.com/laravel/framework"
            },
            "time": "2021-08-17T14:13:34+00:00"
        },
        {
            "name": "laravel/sanctum",
            "version": "v2.11.2",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/sanctum.git",
                "reference": "b21e65cbe13896946986cb0868180cd69e1bd5d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/sanctum/zipball/b21e65cbe13896946986cb0868180cd69e1bd5d3",
                "reference": "b21e65cbe13896946986cb0868180cd69e1bd5d3",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "illuminate/contracts": "^6.9|^7.0|^8.0",
                "illuminate/database": "^6.9|^7.0|^8.0",
                "illuminate/support": "^6.9|^7.0|^8.0",
                "php": "^7.2|^8.0"
            },
            "require-dev": {
                "mockery/mockery": "^1.0",
                "orchestra/testbench": "^4.0|^5.0|^6.0",
                "phpunit/phpunit": "^8.0|^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Laravel\\Sanctum\\SanctumServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Laravel\\Sanctum\\": "src/"
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
            "description": "Laravel Sanctum provides a featherweight authentication system for SPAs and simple APIs.",
            "keywords": [
                "auth",
                "laravel",
                "sanctum"
            ],
            "support": {
                "issues": "https://github.com/laravel/sanctum/issues",
                "source": "https://github.com/laravel/sanctum"
            },
            "time": "2021-06-15T15:56:21+00:00"
        },
        {
            "name": "laravel/tinker",
            "version": "v2.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/tinker.git",
                "reference": "04ad32c1a3328081097a181875733fa51f402083"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/tinker/zipball/04ad32c1a3328081097a181875733fa51f402083",
                "reference": "04ad32c1a3328081097a181875733fa51f402083",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "^6.0|^7.0|^8.0",
                "illuminate/contracts": "^6.0|^7.0|^8.0",
                "illuminate/support": "^6.0|^7.0|^8.0",
                "php": "^7.2.5|^8.0",
                "psy/psysh": "^0.10.4",
                "symfony/var-dumper": "^4.3.4|^5.0"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.3|^1.4.2",
                "phpunit/phpunit": "^8.5.8|^9.3.3"
            },
            "suggest": {
                "illuminate/database": "The Illuminate Database package (^6.0|^7.0|^8.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
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
            "support": {
                "issues": "https://github.com/laravel/tinker/issues",
                "source": "https://github.com/laravel/tinker/tree/v2.6.1"
            },
            "time": "2021-03-02T16:53:12+00:00"
        },
        {
            "name": "league/commonmark",
            "version": "1.6.6",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/commonmark.git",
                "reference": "c4228d11e30d7493c6836d20872f9582d8ba6dcf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/commonmark/zipball/c4228d11e30d7493c6836d20872f9582d8ba6dcf",
                "reference": "c4228d11e30d7493c6836d20872f9582d8ba6dcf",
                "shasum": ""
            },
            "require": {
                "ext-mbstring": "*",
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "scrutinizer/ocular": "1.7.*"
            },
            "require-dev": {
                "cebe/markdown": "~1.0",
                "commonmark/commonmark.js": "0.29.2",
                "erusev/parsedown": "~1.0",
                "ext-json": "*",
                "github/gfm": "0.29.0",
                "michelf/php-markdown": "~1.4",
                "mikehaertl/php-shellcommand": "^1.4",
                "phpstan/phpstan": "^0.12.90",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.2",
                "scrutinizer/ocular": "^1.5",
                "symfony/finder": "^4.2"
            },
            "bin": [
                "bin/commonmark"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\CommonMark\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Colin O'Dell",
                    "email": "colinodell@gmail.com",
                    "homepage": "https://www.colinodell.com",
                    "role": "Lead Developer"
                }
            ],
            "description": "Highly-extensible PHP Markdown parser which fully supports the CommonMark spec and Github-Flavored Markdown (GFM)",
            "homepage": "https://commonmark.thephpleague.com",
            "keywords": [
                "commonmark",
                "flavored",
                "gfm",
                "github",
                "github-flavored",
                "markdown",
                "md",
                "parser"
            ],
            "support": {
                "docs": "https://commonmark.thephpleague.com/",
                "issues": "https://github.com/thephpleague/commonmark/issues",
                "rss": "https://github.com/thephpleague/commonmark/releases.atom",
                "source": "https://github.com/thephpleague/commonmark"
            },
            "funding": [
                {
                    "url": "https://enjoy.gitstore.app/repositories/thephpleague/commonmark",
                    "type": "custom"
                },
                {
                    "url": "https://www.colinodell.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://www.paypal.me/colinpodell/10.00",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/colinodell",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/colinodell",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/league/commonmark",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-17T17:13:23+00:00"
        },
        {
            "name": "league/flysystem",
            "version": "1.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/flysystem.git",
                "reference": "18634df356bfd4119fe3d6156bdb990c414c14ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/flysystem/zipball/18634df356bfd4119fe3d6156bdb990c414c14ea",
                "reference": "18634df356bfd4119fe3d6156bdb990c414c14ea",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "league/mime-type-detection": "^1.3",
                "php": "^7.2.5 || ^8.0"
            },
            "conflict": {
                "league/flysystem-sftp": "<1.0.6"
            },
            "require-dev": {
                "phpspec/prophecy": "^1.11.1",
                "phpunit/phpunit": "^8.5.8"
            },
            "suggest": {
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
            "support": {
                "issues": "https://github.com/thephpleague/flysystem/issues",
                "source": "https://github.com/thephpleague/flysystem/tree/1.1.5"
            },
            "funding": [
                {
                    "url": "https://offset.earth/frankdejonge",
                    "type": "other"
                }
            ],
            "time": "2021-08-17T13:49:42+00:00"
        },
        {
            "name": "league/mime-type-detection",
            "version": "1.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/mime-type-detection.git",
                "reference": "3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/mime-type-detection/zipball/3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3",
                "reference": "3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.18",
                "phpstan/phpstan": "^0.12.68",
                "phpunit/phpunit": "^8.5.8 || ^9.3"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\MimeTypeDetection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Frank de Jonge",
                    "email": "info@frankdejonge.nl"
                }
            ],
            "description": "Mime-type detection for Flysystem",
            "support": {
                "issues": "https://github.com/thephpleague/mime-type-detection/issues",
                "source": "https://github.com/thephpleague/mime-type-detection/tree/1.7.0"
            },
            "funding": [
                {
                    "url": "https://github.com/frankdejonge",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/league/flysystem",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-18T20:58:21+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "2.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "71312564759a7db5b789296369c1a264efc43aad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/71312564759a7db5b789296369c1a264efc43aad",
                "reference": "71312564759a7db5b789296369c1a264efc43aad",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2",
                "psr/log": "^1.0.1"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "elasticsearch/elasticsearch": "^7",
                "graylog2/gelf-php": "^1.4.2",
                "mongodb/mongodb": "^1.8",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpspec/prophecy": "^1.6.1",
                "phpstan/phpstan": "^0.12.91",
                "phpunit/phpunit": "^8.5",
                "predis/predis": "^1.1",
                "rollbar/rollbar": "^1.3",
                "ruflin/elastica": ">=0.90 <7.0.1",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "elasticsearch/elasticsearch": "Allow sending log messages to an Elasticsearch server via official client",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mbstring": "Allow to work properly with unicode symbols",
                "ext-mongodb": "Allow sending log messages to a MongoDB server (via driver)",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server (via library)",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.x-dev"
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
                    "homepage": "https://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "https://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "support": {
                "issues": "https://github.com/Seldaek/monolog/issues",
                "source": "https://github.com/Seldaek/monolog/tree/2.3.2"
            },
            "funding": [
                {
                    "url": "https://github.com/Seldaek",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/monolog/monolog",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T07:42:52+00:00"
        },
        {
            "name": "nesbot/carbon",
            "version": "2.52.0",
            "source": {
                "type": "git",
                "url": "https://github.com/briannesbitt/Carbon.git",
                "reference": "369c0e2737c56a0f39c946dd261855255a6fccbe"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/briannesbitt/Carbon/zipball/369c0e2737c56a0f39c946dd261855255a6fccbe",
                "reference": "369c0e2737c56a0f39c946dd261855255a6fccbe",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.1.8 || ^8.0",
                "symfony/polyfill-mbstring": "^1.0",
                "symfony/polyfill-php80": "^1.16",
                "symfony/translation": "^3.4 || ^4.0 || ^5.0"
            },
            "require-dev": {
                "doctrine/orm": "^2.7",
                "friendsofphp/php-cs-fixer": "^2.14 || ^3.0",
                "kylekatarnls/multi-tester": "^2.0",
                "phpmd/phpmd": "^2.9",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12.54",
                "phpunit/phpunit": "^7.5.20 || ^8.5.14",
                "squizlabs/php_codesniffer": "^3.4"
            },
            "bin": [
                "bin/carbon"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-3.x": "3.x-dev",
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Carbon\\Laravel\\ServiceProvider"
                    ]
                },
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                }
            },
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
                    "homepage": "https://markido.com"
                },
                {
                    "name": "kylekatarnls",
                    "homepage": "https://github.com/kylekatarnls"
                }
            ],
            "description": "An API extension for DateTime that supports 281 different languages.",
            "homepage": "https://carbon.nesbot.com",
            "keywords": [
                "date",
                "datetime",
                "time"
            ],
            "support": {
                "issues": "https://github.com/briannesbitt/Carbon/issues",
                "source": "https://github.com/briannesbitt/Carbon"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/Carbon",
                    "type": "open_collective"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/nesbot/carbon",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-14T19:10:52+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.12.0",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "6608f01670c3cc5079e18c1dab1104e002579143"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/6608f01670c3cc5079e18c1dab1104e002579143",
                "reference": "6608f01670c3cc5079e18c1dab1104e002579143",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "ircmaxell/php-yacc": "^0.0.7",
                "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0 || ^9.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.9-dev"
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
            "support": {
                "issues": "https://github.com/nikic/PHP-Parser/issues",
                "source": "https://github.com/nikic/PHP-Parser/tree/v4.12.0"
            },
            "time": "2021-07-21T10:44:31+00:00"
        },
        {
            "name": "opis/closure",
            "version": "3.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/opis/closure.git",
                "reference": "06e2ebd25f2869e54a306dda991f7db58066f7f6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/opis/closure/zipball/06e2ebd25f2869e54a306dda991f7db58066f7f6",
                "reference": "06e2ebd25f2869e54a306dda991f7db58066f7f6",
                "shasum": ""
            },
            "require": {
                "php": "^5.4 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "jeremeamia/superclosure": "^2.0",
                "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0 || ^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.6.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Opis\\Closure\\": "src/"
                },
                "files": [
                    "functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marius Sarca",
                    "email": "marius.sarca@gmail.com"
                },
                {
                    "name": "Sorin Sarca",
                    "email": "sarca_sorin@hotmail.com"
                }
            ],
            "description": "A library that can be used to serialize closures (anonymous functions) and arbitrary objects.",
            "homepage": "https://opis.io/closure",
            "keywords": [
                "anonymous functions",
                "closure",
                "function",
                "serializable",
                "serialization",
                "serialize"
            ],
            "support": {
                "issues": "https://github.com/opis/closure/issues",
                "source": "https://github.com/opis/closure/tree/3.6.2"
            },
            "time": "2021-04-09T13:42:10+00:00"
        },
        {
            "name": "phpoption/phpoption",
            "version": "1.7.5",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/php-option.git",
                "reference": "994ecccd8f3283ecf5ac33254543eb0ac946d525"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/php-option/zipball/994ecccd8f3283ecf5ac33254543eb0ac946d525",
                "reference": "994ecccd8f3283ecf5ac33254543eb0ac946d525",
                "shasum": ""
            },
            "require": {
                "php": "^5.5.9 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "phpunit/phpunit": "^4.8.35 || ^5.7.27 || ^6.5.6 || ^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.7-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpOption\\": "src/PhpOption/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com"
                }
            ],
            "description": "Option Type for PHP",
            "keywords": [
                "language",
                "option",
                "php",
                "type"
            ],
            "support": {
                "issues": "https://github.com/schmittjoh/php-option/issues",
                "source": "https://github.com/schmittjoh/php-option/tree/1.7.5"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpoption/phpoption",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-20T17:29:33+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/8622567409010282b7aeebe4bb841fe98b58dcaf",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
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
                    "homepage": "https://www.php-fig.org/"
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
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/1.1.1"
            },
            "time": "2021-03-05T17:36:06+00:00"
        },
        {
            "name": "psr/event-dispatcher",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/event-dispatcher.git",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/event-dispatcher/zipball/dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\EventDispatcher\\": "src/"
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
            "description": "Standard interfaces for event handling.",
            "keywords": [
                "events",
                "psr",
                "psr-14"
            ],
            "support": {
                "issues": "https://github.com/php-fig/event-dispatcher/issues",
                "source": "https://github.com/php-fig/event-dispatcher/tree/1.0.0"
            },
            "time": "2019-01-08T18:20:26+00:00"
        },
        {
            "name": "psr/http-client",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-client.git",
                "reference": "2dfb5f6c5eff0e91e20e913f8c5452ed95b86621"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-client/zipball/2dfb5f6c5eff0e91e20e913f8c5452ed95b86621",
                "reference": "2dfb5f6c5eff0e91e20e913f8c5452ed95b86621",
                "shasum": ""
            },
            "require": {
                "php": "^7.0 || ^8.0",
                "psr/http-message": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Client\\": "src/"
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
            "description": "Common interface for HTTP clients",
            "homepage": "https://github.com/php-fig/http-client",
            "keywords": [
                "http",
                "http-client",
                "psr",
                "psr-18"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-client/tree/master"
            },
            "time": "2020-06-29T06:28:15+00:00"
        },
        {
            "name": "psr/http-factory",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-factory.git",
                "reference": "12ac7fcd07e5b077433f5f2bee95b3a771bf61be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-factory/zipball/12ac7fcd07e5b077433f5f2bee95b3a771bf61be",
                "reference": "12ac7fcd07e5b077433f5f2bee95b3a771bf61be",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0.0",
                "psr/http-message": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Message\\": "src/"
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
            "description": "Common interfaces for PSR-7 HTTP message factories",
            "keywords": [
                "factory",
                "http",
                "message",
                "psr",
                "psr-17",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-factory/tree/master"
            },
            "time": "2019-04-30T12:38:16+00:00"
        },
        {
            "name": "psr/http-message",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-message.git",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-message/zipball/f6561bf28d520154e4b0ec72be95418abe6d9363",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363",
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
                    "Psr\\Http\\Message\\": "src/"
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
            "description": "Common interface for HTTP messages",
            "homepage": "https://github.com/php-fig/http-message",
            "keywords": [
                "http",
                "http-message",
                "psr",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-message/tree/master"
            },
            "time": "2016-08-06T14:39:51+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "d49695b909c3b7628b6289db5479a1c204601f11"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/d49695b909c3b7628b6289db5479a1c204601f11",
                "reference": "d49695b909c3b7628b6289db5479a1c204601f11",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
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
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "support": {
                "source": "https://github.com/php-fig/log/tree/1.1.4"
            },
            "time": "2021-05-03T11:20:27+00:00"
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
            "support": {
                "source": "https://github.com/php-fig/simple-cache/tree/master"
            },
            "time": "2017-10-23T01:57:42+00:00"
        },
        {
            "name": "psy/psysh",
            "version": "v0.10.8",
            "source": {
                "type": "git",
                "url": "https://github.com/bobthecow/psysh.git",
                "reference": "e4573f47750dd6c92dca5aee543fa77513cbd8d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/bobthecow/psysh/zipball/e4573f47750dd6c92dca5aee543fa77513cbd8d3",
                "reference": "e4573f47750dd6c92dca5aee543fa77513cbd8d3",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-tokenizer": "*",
                "nikic/php-parser": "~4.0|~3.0|~2.0|~1.3",
                "php": "^8.0 || ^7.0 || ^5.5.9",
                "symfony/console": "~5.0|~4.0|~3.0|^2.4.2|~2.3.10",
                "symfony/var-dumper": "~5.0|~4.0|~3.0|~2.7"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.2",
                "hoa/console": "3.17.*"
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
                    "dev-main": "0.10.x-dev"
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
            "support": {
                "issues": "https://github.com/bobthecow/psysh/issues",
                "source": "https://github.com/bobthecow/psysh/tree/v0.10.8"
            },
            "time": "2021-04-10T16:23:39+00:00"
        },
        {
            "name": "ralouphie/getallheaders",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/ralouphie/getallheaders.git",
                "reference": "120b605dfeb996808c31b6477290a714d356e822"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ralouphie/getallheaders/zipball/120b605dfeb996808c31b6477290a714d356e822",
                "reference": "120b605dfeb996808c31b6477290a714d356e822",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.1",
                "phpunit/phpunit": "^5 || ^6.5"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/getallheaders.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ralph Khattar",
                    "email": "ralph.khattar@gmail.com"
                }
            ],
            "description": "A polyfill for getallheaders.",
            "support": {
                "issues": "https://github.com/ralouphie/getallheaders/issues",
                "source": "https://github.com/ralouphie/getallheaders/tree/develop"
            },
            "time": "2019-03-08T08:55:37+00:00"
        },
        {
            "name": "ramsey/collection",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/collection.git",
                "reference": "eaca1dc1054ddd10cbd83c1461907bee6fb528fa"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/collection/zipball/eaca1dc1054ddd10cbd83c1461907bee6fb528fa",
                "reference": "eaca1dc1054ddd10cbd83c1461907bee6fb528fa",
                "shasum": ""
            },
            "require": {
                "php": "^7.3 || ^8",
                "symfony/polyfill-php81": "^1.23"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
                "ergebnis/composer-normalize": "^2.6",
                "fakerphp/faker": "^1.5",
                "hamcrest/hamcrest-php": "^2",
                "jangregor/phpstan-prophecy": "^0.8",
                "mockery/mockery": "^1.3",
                "phpspec/prophecy-phpunit": "^2.0",
                "phpstan/extension-installer": "^1",
                "phpstan/phpstan": "^0.12.32",
                "phpstan/phpstan-mockery": "^0.12.5",
                "phpstan/phpstan-phpunit": "^0.12.11",
                "phpunit/phpunit": "^8.5 || ^9",
                "psy/psysh": "^0.10.4",
                "slevomat/coding-standard": "^6.3",
                "squizlabs/php_codesniffer": "^3.5",
                "vimeo/psalm": "^4.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Ramsey\\Collection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "A PHP library for representing and manipulating collections.",
            "keywords": [
                "array",
                "collection",
                "hash",
                "map",
                "queue",
                "set"
            ],
            "support": {
                "issues": "https://github.com/ramsey/collection/issues",
                "source": "https://github.com/ramsey/collection/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/collection",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-06T03:41:06+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "4.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "fe665a03df4f056aa65af552a96e1976df8c8dae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/fe665a03df4f056aa65af552a96e1976df8c8dae",
                "reference": "fe665a03df4f056aa65af552a96e1976df8c8dae",
                "shasum": ""
            },
            "require": {
                "brick/math": "^0.8 || ^0.9",
                "ext-json": "*",
                "php": "^7.2 || ^8",
                "ramsey/collection": "^1.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.10",
                "captainhook/plugin-composer": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
                "doctrine/annotations": "^1.8",
                "ergebnis/composer-normalize": "^2.15",
                "mockery/mockery": "^1.3",
                "moontoast/math": "^1.1",
                "paragonie/random-lib": "^2",
                "php-mock/php-mock": "^2.2",
                "php-mock/php-mock-mockery": "^1.3",
                "php-parallel-lint/php-parallel-lint": "^1.1",
                "phpbench/phpbench": "^1.0",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-mockery": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^8.5 || ^9",
                "slevomat/coding-standard": "^7.0",
                "squizlabs/php_codesniffer": "^3.5",
                "vimeo/psalm": "^4.9"
            },
            "suggest": {
                "ext-bcmath": "Enables faster math with arbitrary-precision integers using BCMath.",
                "ext-ctype": "Enables faster processing of character classification using ctype functions.",
                "ext-gmp": "Enables faster math with arbitrary-precision integers using GMP.",
                "ext-uuid": "Enables the use of PeclUuidTimeGenerator and PeclUuidRandomGenerator.",
                "paragonie/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.x-dev"
                },
                "captainhook": {
                    "force-install": true
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                },
                "files": [
                    "src/functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A PHP library for generating and working with universally unique identifiers (UUIDs).",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "support": {
                "issues": "https://github.com/ramsey/uuid/issues",
                "source": "https://github.com/ramsey/uuid/tree/4.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/uuid",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-11T01:06:55+00:00"
        },
        {
            "name": "safaricom/mpesa",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/safaricom/mpesa-php-sdk.git",
                "reference": "c66895dcdec8df1f496e017708c557fc252340c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/safaricom/mpesa-php-sdk/zipball/c66895dcdec8df1f496e017708c557fc252340c5",
                "reference": "c66895dcdec8df1f496e017708c557fc252340c5",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "symfony/dotenv": "^4.3@dev"
            },
            "type": "package",
            "autoload": {
                "psr-4": {
                    "Safaricom\\Mpesa\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "mit"
            ],
            "authors": [
                {
                    "name": "Moses Nandwa",
                    "email": "mnandwa@safaricom.co.ke"
                }
            ],
            "description": "A PHP package for Mpesa API",
            "support": {
                "issues": "https://github.com/safaricom/mpesa-php-sdk/issues",
                "source": "https://github.com/safaricom/mpesa-php-sdk/tree/master"
            },
            "time": "2019-01-06T16:01:21+00:00"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "v6.2.7",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "15f7faf8508e04471f666633addacf54c0ab5933"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/15f7faf8508e04471f666633addacf54c0ab5933",
                "reference": "15f7faf8508e04471f666633addacf54c0ab5933",
                "shasum": ""
            },
            "require": {
                "egulias/email-validator": "^2.0|^3.1",
                "php": ">=7.0.0",
                "symfony/polyfill-iconv": "^1.0",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^1.0",
                "symfony/phpunit-bridge": "^4.4|^5.0"
            },
            "suggest": {
                "ext-intl": "Needed to support internationalized email addresses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.2-dev"
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
            "support": {
                "issues": "https://github.com/swiftmailer/swiftmailer/issues",
                "source": "https://github.com/swiftmailer/swiftmailer/tree/v6.2.7"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/swiftmailer/swiftmailer",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-09T12:30:35+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "51b71afd6d2dc8f5063199357b9880cea8d8bfe2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/51b71afd6d2dc8f5063199357b9880cea8d8bfe2",
                "reference": "51b71afd6d2dc8f5063199357b9880cea8d8bfe2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/polyfill-php80": "^1.16",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/string": "^5.1"
            },
            "conflict": {
                "psr/log": ">=3",
                "symfony/dependency-injection": "<4.4",
                "symfony/dotenv": "<5.1",
                "symfony/event-dispatcher": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/process": "<4.4"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0"
            },
            "require-dev": {
                "psr/log": "^1|^2",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
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
            "description": "Eases the creation of beautiful and testable command line interfaces",
            "homepage": "https://symfony.com",
            "keywords": [
                "cli",
                "command line",
                "console",
                "terminal"
            ],
            "support": {
                "source": "https://github.com/symfony/console/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T19:10:22+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "7fb120adc7f600a59027775b224c13a33530dd90"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/7fb120adc7f600a59027775b224c13a33530dd90",
                "reference": "7fb120adc7f600a59027775b224c13a33530dd90",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Converts CSS selectors to XPath expressions",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/css-selector/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-21T12:38:00+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
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
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "281f6c4660bcf5844bb0346fe3a4664722fe4c73"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/281f6c4660bcf5844bb0346fe3a4664722fe4c73",
                "reference": "281f6c4660bcf5844bb0346fe3a4664722fe4c73",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1|^2|^3",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.1",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\ErrorHandler\\": ""
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
            "description": "Provides tools to manage errors and ease debugging PHP code",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/error-handler/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "f2fd2208157553874560f3645d4594303058c4bd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/f2fd2208157553874560f3645d4594303058c4bd",
                "reference": "f2fd2208157553874560f3645d4594303058c4bd",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/event-dispatcher-contracts": "^2",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "2.0"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/stopwatch": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
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
            "description": "Provides tools that allow your application components to communicate with each other by dispatching events and listening to them",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/event-dispatcher/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/event-dispatcher": "^1"
            },
            "suggest": {
                "symfony/event-dispatcher-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
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
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "17f50e06018baec41551a71a15731287dbaab186"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/17f50e06018baec41551a71a15731287dbaab186",
                "reference": "17f50e06018baec41551a71a15731287dbaab186",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
            "description": "Finds files and directories via an intuitive fluent interface",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/finder/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:54:19+00:00"
        },
        {
            "name": "symfony/http-client-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-client-contracts.git",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-client-contracts/zipball/7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/http-client-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\HttpClient\\": ""
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
            "description": "Generic abstractions related to HTTP clients",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/http-client-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-11T23:07:08+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "a8388f7b7054a7401997008ce9cd8c6b0ab7ac75"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/a8388f7b7054a7401997008ce9cd8c6b0ab7ac75",
                "reference": "a8388f7b7054a7401997008ce9cd8c6b0ab7ac75",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.1",
                "symfony/polyfill-php80": "^1.16"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/mime": "To use the file extension guesser"
            },
            "type": "library",
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
            "description": "Defines an object-oriented layer for the HTTP specification",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-foundation/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T17:08:17+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "60030f209018356b3b553b9dbd84ad2071c1b7e0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/60030f209018356b3b553b9dbd84ad2071c1b7e0",
                "reference": "60030f209018356b3b553b9dbd84ad2071c1b7e0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1|^2",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/event-dispatcher": "^5.0",
                "symfony/http-client-contracts": "^1.1|^2",
                "symfony/http-foundation": "^5.3",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-php73": "^1.9",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "symfony/browser-kit": "<4.4",
                "symfony/cache": "<5.0",
                "symfony/config": "<5.0",
                "symfony/console": "<4.4",
                "symfony/dependency-injection": "<5.3",
                "symfony/doctrine-bridge": "<5.0",
                "symfony/form": "<5.0",
                "symfony/http-client": "<5.0",
                "symfony/mailer": "<5.0",
                "symfony/messenger": "<5.0",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<5.0",
                "symfony/validator": "<5.0",
                "twig/twig": "<2.13"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/config": "^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dependency-injection": "^5.3",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "twig/twig": "^2.13|^3.0.4"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": ""
            },
            "type": "library",
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
            "description": "Provides a structured process for converting a Request into a Response",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-kernel/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-29T07:06:27+00:00"
        },
        {
            "name": "symfony/mime",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/mime.git",
                "reference": "633e4e8afe9e529e5599d71238849a4218dd497b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/mime/zipball/633e4e8afe9e529e5599d71238849a4218dd497b",
                "reference": "633e4e8afe9e529e5599d71238849a4218dd497b",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "egulias/email-validator": "~3.0.0",
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "symfony/mailer": "<4.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10|^3.1",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.1",
                "symfony/property-info": "^4.4|^5.1",
                "symfony/serializer": "^5.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Mime\\": ""
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
            "description": "Allows manipulating MIME messages",
            "homepage": "https://symfony.com",
            "keywords": [
                "mime",
                "mime-type"
            ],
            "support": {
                "source": "https://github.com/symfony/mime/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-21T12:40:44+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "46cd95797e9df938fdd2b03693b5fca5e64b01ce"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/46cd95797e9df938fdd2b03693b5fca5e64b01ce",
                "reference": "46cd95797e9df938fdd2b03693b5fca5e64b01ce",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-ctype/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-iconv",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-iconv.git",
                "reference": "63b5bb7db83e5673936d6e3b8b3e022ff6474933"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-iconv/zipball/63b5bb7db83e5673936d6e3b8b3e022ff6474933",
                "reference": "63b5bb7db83e5673936d6e3b8b3e022ff6474933",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-iconv": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Iconv\\": ""
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
            "description": "Symfony polyfill for the Iconv extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "iconv",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-iconv/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:27:20+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "16880ba9c5ebe3642d1995ab866db29270b36535"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/16880ba9c5ebe3642d1995ab866db29270b36535",
                "reference": "16880ba9c5ebe3642d1995ab866db29270b36535",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Grapheme\\": ""
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
            "description": "Symfony polyfill for intl's grapheme_* functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "grapheme",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T12:26:48+00:00"
        },
        {
            "name": "symfony/polyfill-intl-idn",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-idn.git",
                "reference": "65bd267525e82759e7d8c4e8ceea44f398838e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-idn/zipball/65bd267525e82759e7d8c4e8ceea44f398838e65",
                "reference": "65bd267525e82759e7d8c4e8ceea44f398838e65",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "symfony/polyfill-intl-normalizer": "^1.10",
                "symfony/polyfill-php72": "^1.10"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Idn\\": ""
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
                    "name": "Laurent Bassin",
                    "email": "laurent@bassin.info"
                },
                {
                    "name": "Trevor Rowbotham",
                    "email": "trevor.rowbotham@pm.me"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's idn_to_ascii and idn_to_utf8 functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "idn",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-idn/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:27:20+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "8590a5f561694770bdcd3f9b5c69dde6945028e8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/8590a5f561694770bdcd3f9b5c69dde6945028e8",
                "reference": "8590a5f561694770bdcd3f9b5c69dde6945028e8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "9174a3d80210dca8daa7f31fec659150bbeabfc6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/9174a3d80210dca8daa7f31fec659150bbeabfc6",
                "reference": "9174a3d80210dca8daa7f31fec659150bbeabfc6",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T12:26:48+00:00"
        },
        {
            "name": "symfony/polyfill-php72",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php72.git",
                "reference": "9a142215a36a3888e30d0a9eeea9766764e96976"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php72/zipball/9a142215a36a3888e30d0a9eeea9766764e96976",
                "reference": "9a142215a36a3888e30d0a9eeea9766764e96976",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-php72/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:17:38+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "fba8933c384d6476ab14fb7b8526e5287ca7e010"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/fba8933c384d6476ab14fb7b8526e5287ca7e010",
                "reference": "fba8933c384d6476ab14fb7b8526e5287ca7e010",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php73/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "1100343ed1a92e3a38f9ae122fc0eb21602547be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/1100343ed1a92e3a38f9ae122fc0eb21602547be",
                "reference": "1100343ed1a92e3a38f9ae122fc0eb21602547be",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-28T13:41:28+00:00"
        },
        {
            "name": "symfony/polyfill-php81",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php81.git",
                "reference": "e66119f3de95efc359483f810c4c3e6436279436"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php81/zipball/e66119f3de95efc359483f810c4c3e6436279436",
                "reference": "e66119f3de95efc359483f810c4c3e6436279436",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php81\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill backporting some PHP 8.1+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php81/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-21T13:25:03+00:00"
        },
        {
            "name": "symfony/process",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/process.git",
                "reference": "d16634ee55b895bd85ec714dadc58e4428ecf030"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/process/zipball/d16634ee55b895bd85ec714dadc58e4428ecf030",
                "reference": "d16634ee55b895bd85ec714dadc58e4428ecf030",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
            "description": "Executes commands in sub-processes",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/process/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:54:19+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "0a35d2f57d73c46ab6d042ced783b81d09a624c4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/0a35d2f57d73c46ab6d042ced783b81d09a624c4",
                "reference": "0a35d2f57d73c46ab6d042ced783b81d09a624c4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "doctrine/annotations": "<1.12",
                "symfony/config": "<5.3",
                "symfony/dependency-injection": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "^1.12",
                "psr/log": "^1|^2|^3",
                "symfony/config": "^5.3",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
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
            "description": "Maps an HTTP request to a set of configuration variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "support": {
                "source": "https://github.com/symfony/routing/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.1"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
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
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-01T10:43:52+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v5.3.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1",
                "reference": "bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.0",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "~1.15"
            },
            "require-dev": {
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\String\\": ""
                },
                "files": [
                    "Resources/functions.php"
                ],
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
            "description": "Provides an object-oriented API to strings and deals with bytes, UTF-8 code points and grapheme clusters in a unified way",
            "homepage": "https://symfony.com",
            "keywords": [
                "grapheme",
                "i18n",
                "string",
                "unicode",
                "utf-8",
                "utf8"
            ],
            "support": {
                "source": "https://github.com/symfony/string/tree/v5.3.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-06-27T11:44:38+00:00"
        },
        {
            "name": "symfony/translation",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "d89ad7292932c2699cbe4af98d72c5c6bbc504c1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/d89ad7292932c2699cbe4af98d72c5c6bbc504c1",
                "reference": "d89ad7292932c2699cbe4af98d72c5c6bbc504c1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.16",
                "symfony/translation-contracts": "^2.3"
            },
            "conflict": {
                "symfony/config": "<4.4",
                "symfony/dependency-injection": "<5.0",
                "symfony/http-kernel": "<5.0",
                "symfony/twig-bundle": "<5.0",
                "symfony/yaml": "<4.4"
            },
            "provide": {
                "symfony/translation-implementation": "2.3"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/dependency-injection": "^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/intl": "^4.4|^5.0",
                "symfony/polyfill-intl-icu": "^1.21",
                "symfony/service-contracts": "^1.1.2|^2",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log-implementation": "To use logging capability in translator",
                "symfony/config": "",
                "symfony/yaml": ""
            },
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions.php"
                ],
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
            "description": "Provides tools to internationalize your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/translation/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-25T09:39:16+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "95c812666f3e91db75385749fe219c5e494c7f95"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/95c812666f3e91db75385749fe219c5e494c7f95",
                "reference": "95c812666f3e91db75385749fe219c5e494c7f95",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/translation-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Translation\\": ""
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
            "description": "Generic abstractions related to translation",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/translation-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0",
                "reference": "3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "twig/twig": "^2.13|^3.0.4"
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
            "description": "Provides mechanisms for walking through any arbitrary PHP variable",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T01:56:02+00:00"
        },
        {
            "name": "tijsverkoyen/css-to-inline-styles",
            "version": "2.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/tijsverkoyen/CssToInlineStyles.git",
                "reference": "b43b05cf43c1b6d849478965062b6ef73e223bb5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/tijsverkoyen/CssToInlineStyles/zipball/b43b05cf43c1b6d849478965062b6ef73e223bb5",
                "reference": "b43b05cf43c1b6d849478965062b6ef73e223bb5",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "php": "^5.5 || ^7.0 || ^8.0",
                "symfony/css-selector": "^2.7 || ^3.0 || ^4.0 || ^5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0 || ^7.5"
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
            "support": {
                "issues": "https://github.com/tijsverkoyen/CssToInlineStyles/issues",
                "source": "https://github.com/tijsverkoyen/CssToInlineStyles/tree/2.2.3"
            },
            "time": "2020-07-13T06:12:54+00:00"
        },
        {
            "name": "vlucas/phpdotenv",
            "version": "v5.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/vlucas/phpdotenv.git",
                "reference": "b3eac5c7ac896e52deab4a99068e3f4ab12d9e56"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vlucas/phpdotenv/zipball/b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
                "reference": "b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
                "shasum": ""
            },
            "require": {
                "ext-pcre": "*",
                "graham-campbell/result-type": "^1.0.1",
                "php": "^7.1.3 || ^8.0",
                "phpoption/phpoption": "^1.7.4",
                "symfony/polyfill-ctype": "^1.17",
                "symfony/polyfill-mbstring": "^1.17",
                "symfony/polyfill-php80": "^1.17"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-filter": "*",
                "phpunit/phpunit": "^7.5.20 || ^8.5.14 || ^9.5.1"
            },
            "suggest": {
                "ext-filter": "Required to use the boolean validator."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.3-dev"
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
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com",
                    "homepage": "https://gjcampbell.co.uk/"
                },
                {
                    "name": "Vance Lucas",
                    "email": "vance@vancelucas.com",
                    "homepage": "https://vancelucas.com/"
                }
            ],
            "description": "Loads environment variables from `.env` to `getenv()`, `$_ENV` and `$_SERVER` automagically.",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "support": {
                "issues": "https://github.com/vlucas/phpdotenv/issues",
                "source": "https://github.com/vlucas/phpdotenv/tree/v5.3.0"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/vlucas/phpdotenv",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-20T15:23:13+00:00"
        },
        {
            "name": "voku/portable-ascii",
            "version": "1.5.6",
            "source": {
                "type": "git",
                "url": "https://github.com/voku/portable-ascii.git",
                "reference": "80953678b19901e5165c56752d087fc11526017c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/voku/portable-ascii/zipball/80953678b19901e5165c56752d087fc11526017c",
                "reference": "80953678b19901e5165c56752d087fc11526017c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~6.0 || ~7.0 || ~9.0"
            },
            "suggest": {
                "ext-intl": "Use Intl for transliterator_transliterate() support"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "voku\\": "src/voku/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Lars Moelleken",
                    "homepage": "http://www.moelleken.org/"
                }
            ],
            "description": "Portable ASCII library - performance optimized (ascii) string functions for php.",
            "homepage": "https://github.com/voku/portable-ascii",
            "keywords": [
                "ascii",
                "clean",
                "php"
            ],
            "support": {
                "issues": "https://github.com/voku/portable-ascii/issues",
                "source": "https://github.com/voku/portable-ascii/tree/1.5.6"
            },
            "funding": [
                {
                    "url": "https://www.paypal.me/moelleken",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/voku",
                    "type": "github"
                },
                {
                    "url": "https://opencollective.com/portable-ascii",
                    "type": "open_collective"
                },
                {
                    "url": "https://www.patreon.com/voku",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/voku/portable-ascii",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-12T00:07:28+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozarts/assert.git",
                "reference": "6964c76c7804814a842473e0c8fd15bab0f18e25"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozarts/assert/zipball/6964c76c7804814a842473e0c8fd15bab0f18e25",
                "reference": "6964c76c7804814a842473e0c8fd15bab0f18e25",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "phpstan/phpstan": "<0.12.20",
                "vimeo/psalm": "<4.6.1 || 4.6.2"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5.13"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.10-dev"
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
            "support": {
                "issues": "https://github.com/webmozarts/assert/issues",
                "source": "https://github.com/webmozarts/assert/tree/1.10.0"
            },
            "time": "2021-03-09T10:59:23+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "doctrine/instantiator",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.0",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpbench/phpbench": "^0.13 || 1.0.0-alpha2",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
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
                    "homepage": "https://ocramius.github.io/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://www.doctrine-project.org/projects/instantiator.html",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "support": {
                "issues": "https://github.com/doctrine/instantiator/issues",
                "source": "https://github.com/doctrine/instantiator/tree/1.4.0"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finstantiator",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-10T18:47:58+00:00"
        },
        {
            "name": "facade/flare-client-php",
            "version": "1.8.1",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/flare-client-php.git",
                "reference": "47b639dc02bcfdfc4ebb83de703856fa01e35f5f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/flare-client-php/zipball/47b639dc02bcfdfc4ebb83de703856fa01e35f5f",
                "reference": "47b639dc02bcfdfc4ebb83de703856fa01e35f5f",
                "shasum": ""
            },
            "require": {
                "facade/ignition-contracts": "~1.0",
                "illuminate/pipeline": "^5.5|^6.0|^7.0|^8.0",
                "php": "^7.1|^8.0",
                "symfony/http-foundation": "^3.3|^4.1|^5.0",
                "symfony/mime": "^3.4|^4.0|^5.1",
                "symfony/var-dumper": "^3.4|^4.0|^5.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.14",
                "phpunit/phpunit": "^7.5.16",
                "spatie/phpunit-snapshot-assertions": "^2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Facade\\FlareClient\\": "src"
                },
                "files": [
                    "src/helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Send PHP errors to Flare",
            "homepage": "https://github.com/facade/flare-client-php",
            "keywords": [
                "exception",
                "facade",
                "flare",
                "reporting"
            ],
            "support": {
                "issues": "https://github.com/facade/flare-client-php/issues",
                "source": "https://github.com/facade/flare-client-php/tree/1.8.1"
            },
            "funding": [
                {
                    "url": "https://github.com/spatie",
                    "type": "github"
                }
            ],
            "time": "2021-05-31T19:23:29+00:00"
        },
        {
            "name": "facade/ignition",
            "version": "2.11.4",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/ignition.git",
                "reference": "1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/ignition/zipball/1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2",
                "reference": "1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-mbstring": "*",
                "facade/flare-client-php": "^1.6",
                "facade/ignition-contracts": "^1.0.2",
                "illuminate/support": "^7.0|^8.0",
                "monolog/monolog": "^2.0",
                "php": "^7.2.5|^8.0",
                "symfony/console": "^5.0",
                "symfony/var-dumper": "^5.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.14",
                "mockery/mockery": "^1.3",
                "orchestra/testbench": "^5.0|^6.0",
                "psalm/plugin-laravel": "^1.2"
            },
            "suggest": {
                "laravel/telescope": "^3.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Facade\\Ignition\\IgnitionServiceProvider"
                    ],
                    "aliases": {
                        "Flare": "Facade\\Ignition\\Facades\\Flare"
                    }
                }
            },
            "autoload": {
                "psr-4": {
                    "Facade\\Ignition\\": "src"
                },
                "files": [
                    "src/helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A beautiful error page for Laravel applications.",
            "homepage": "https://github.com/facade/ignition",
            "keywords": [
                "error",
                "flare",
                "laravel",
                "page"
            ],
            "support": {
                "docs": "https://flareapp.io/docs/ignition-for-laravel/introduction",
                "forum": "https://twitter.com/flareappio",
                "issues": "https://github.com/facade/ignition/issues",
                "source": "https://github.com/facade/ignition"
            },
            "time": "2021-08-17T11:45:33+00:00"
        },
        {
            "name": "facade/ignition-contracts",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/ignition-contracts.git",
                "reference": "3c921a1cdba35b68a7f0ccffc6dffc1995b18267"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/ignition-contracts/zipball/3c921a1cdba35b68a7f0ccffc6dffc1995b18267",
                "reference": "3c921a1cdba35b68a7f0ccffc6dffc1995b18267",
                "shasum": ""
            },
            "require": {
                "php": "^7.3|^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^v2.15.8",
                "phpunit/phpunit": "^9.3.11",
                "vimeo/psalm": "^3.17.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Facade\\IgnitionContracts\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Freek Van der Herten",
                    "email": "freek@spatie.be",
                    "homepage": "https://flareapp.io",
                    "role": "Developer"
                }
            ],
            "description": "Solution contracts for Ignition",
            "homepage": "https://github.com/facade/ignition-contracts",
            "keywords": [
                "contracts",
                "flare",
                "ignition"
            ],
            "support": {
                "issues": "https://github.com/facade/ignition-contracts/issues",
                "source": "https://github.com/facade/ignition-contracts/tree/1.0.2"
            },
            "time": "2020-10-16T08:27:54+00:00"
        },
        {
            "name": "fakerphp/faker",
            "version": "v1.15.0",
            "source": {
                "type": "git",
                "url": "https://github.com/FakerPHP/Faker.git",
                "reference": "89c6201c74db25fa759ff16e78a4d8f32547770e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FakerPHP/Faker/zipball/89c6201c74db25fa759ff16e78a4d8f32547770e",
                "reference": "89c6201c74db25fa759ff16e78a4d8f32547770e",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "psr/container": "^1.0",
                "symfony/deprecation-contracts": "^2.2"
            },
            "conflict": {
                "fzaninotto/faker": "*"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-intl": "*",
                "symfony/phpunit-bridge": "^4.4 || ^5.2"
            },
            "suggest": {
                "ext-curl": "Required by Faker\\Provider\\Image to download images.",
                "ext-dom": "Required by Faker\\Provider\\HtmlLorem for generating random HTML.",
                "ext-iconv": "Required by Faker\\Provider\\ru_RU\\Text::realText() for generating real Russian text.",
                "ext-mbstring": "Required for multibyte Unicode string functionality."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "v1.15-dev"
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
            "support": {
                "issues": "https://github.com/FakerPHP/Faker/issues",
                "source": "https://github.com/FakerPHP/Faker/tree/v1.15.0"
            },
            "time": "2021-07-06T20:39:40+00:00"
        },
        {
            "name": "filp/whoops",
            "version": "2.14.0",
            "source": {
                "type": "git",
                "url": "https://github.com/filp/whoops.git",
                "reference": "fdf92f03e150ed84d5967a833ae93abffac0315b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/filp/whoops/zipball/fdf92f03e150ed84d5967a833ae93abffac0315b",
                "reference": "fdf92f03e150ed84d5967a833ae93abffac0315b",
                "shasum": ""
            },
            "require": {
                "php": "^5.5.9 || ^7.0 || ^8.0",
                "psr/log": "^1.0.1"
            },
            "require-dev": {
                "mockery/mockery": "^0.9 || ^1.0",
                "phpunit/phpunit": "^4.8.36 || ^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.5.8 || ^9.3.3",
                "symfony/var-dumper": "^2.6 || ^3.0 || ^4.0 || ^5.0"
            },
            "suggest": {
                "symfony/var-dumper": "Pretty print complex values better with var-dumper available",
                "whoops/soap": "Formats errors as SOAP responses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7-dev"
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
            "support": {
                "issues": "https://github.com/filp/whoops/issues",
                "source": "https://github.com/filp/whoops/tree/2.14.0"
            },
            "funding": [
                {
                    "url": "https://github.com/denis-sokolov",
                    "type": "github"
                }
            ],
            "time": "2021-07-13T12:00:00+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "shasum": ""
            },
            "require": {
                "php": "^5.3|^7.0|^8.0"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "^1.4 || ^2.0",
                "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "hamcrest"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "support": {
                "issues": "https://github.com/hamcrest/hamcrest-php/issues",
                "source": "https://github.com/hamcrest/hamcrest-php/tree/v2.0.1"
            },
            "time": "2020-07-09T08:09:16+00:00"
        },
        {
            "name": "laravel/sail",
            "version": "v1.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/sail.git",
                "reference": "05cf80b1365a0b556f6c21ed5c71a27971d06ec8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/sail/zipball/05cf80b1365a0b556f6c21ed5c71a27971d06ec8",
                "reference": "05cf80b1365a0b556f6c21ed5c71a27971d06ec8",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "^8.0|^9.0",
                "illuminate/contracts": "^8.0|^9.0",
                "illuminate/support": "^8.0|^9.0",
                "php": "^7.3|^8.0"
            },
            "bin": [
                "bin/sail"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Laravel\\Sail\\SailServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Laravel\\Sail\\": "src/"
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
            "description": "Docker files for running a basic Laravel application.",
            "keywords": [
                "docker",
                "laravel"
            ],
            "support": {
                "issues": "https://github.com/laravel/sail/issues",
                "source": "https://github.com/laravel/sail"
            },
            "time": "2021-08-17T16:00:47+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "1.4.3",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "d1339f64479af1bee0e82a0413813fe5345a54ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/d1339f64479af1bee0e82a0413813fe5345a54ea",
                "reference": "d1339f64479af1bee0e82a0413813fe5345a54ea",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "^2.0.1",
                "lib-pcre": ">=7.0",
                "php": "^7.3 || ^8.0"
            },
            "conflict": {
                "phpunit/phpunit": "<8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5 || ^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4.x-dev"
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
            "support": {
                "issues": "https://github.com/mockery/mockery/issues",
                "source": "https://github.com/mockery/mockery/tree/1.4.3"
            },
            "time": "2021-02-24T09:51:49+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.10.2",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
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
            "support": {
                "issues": "https://github.com/myclabs/DeepCopy/issues",
                "source": "https://github.com/myclabs/DeepCopy/tree/1.10.2"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/deep-copy",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-13T09:40:50+00:00"
        },
        {
            "name": "nunomaduro/collision",
            "version": "v5.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/nunomaduro/collision.git",
                "reference": "0c3c393462eada1233513664e2d22bb9f69ca393"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nunomaduro/collision/zipball/0c3c393462eada1233513664e2d22bb9f69ca393",
                "reference": "0c3c393462eada1233513664e2d22bb9f69ca393",
                "shasum": ""
            },
            "require": {
                "facade/ignition-contracts": "^1.0",
                "filp/whoops": "^2.7.2",
                "php": "^7.3 || ^8.0",
                "symfony/console": "^5.0"
            },
            "require-dev": {
                "brianium/paratest": "^6.1",
                "fideloper/proxy": "^4.4.1",
                "friendsofphp/php-cs-fixer": "^3.0",
                "fruitcake/laravel-cors": "^2.0.3",
                "laravel/framework": "^8.0 || ^9.0",
                "nunomaduro/larastan": "^0.6.2",
                "nunomaduro/mock-final-classes": "^1.0",
                "orchestra/testbench": "^6.0 || ^7.0",
                "phpstan/phpstan": "^0.12.64",
                "phpunit/phpunit": "^9.5.0"
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
            "support": {
                "issues": "https://github.com/nunomaduro/collision/issues",
                "source": "https://github.com/nunomaduro/collision"
            },
            "funding": [
                {
                    "url": "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=66BYDWAT92N6L",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/nunomaduro",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/nunomaduro",
                    "type": "patreon"
                }
            ],
            "time": "2021-08-13T14:23:01+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "97803eca37d319dfa7826cc2437fc020857acb53"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/97803eca37d319dfa7826cc2437fc020857acb53",
                "reference": "97803eca37d319dfa7826cc2437fc020857acb53",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "ext-xmlwriter": "*",
                "phar-io/version": "^3.0.1",
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/phar-io/manifest/issues",
                "source": "https://github.com/phar-io/manifest/tree/2.0.3"
            },
            "time": "2021-07-20T11:28:43+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "bae7c545bef187884426f042434e561ab1ddb182"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/bae7c545bef187884426f042434e561ab1ddb182",
                "reference": "bae7c545bef187884426f042434e561ab1ddb182",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/phar-io/version/issues",
                "source": "https://github.com/phar-io/version/tree/3.1.0"
            },
            "time": "2021-02-23T14:00:09+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-2.x": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src/"
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
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionCommon/issues",
                "source": "https://github.com/phpDocumentor/ReflectionCommon/tree/2.x"
            },
            "time": "2020-06-27T09:03:43+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "5.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/069a785b2141f5bcf49f3e353548dc1cce6df556",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556",
                "shasum": ""
            },
            "require": {
                "ext-filter": "*",
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.2",
                "phpdocumentor/type-resolver": "^1.3",
                "webmozart/assert": "^1.9.1"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
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
                },
                {
                    "name": "Jaap van Otterdijk",
                    "email": "account@ijaap.nl"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionDocBlock/issues",
                "source": "https://github.com/phpDocumentor/ReflectionDocBlock/tree/master"
            },
            "time": "2020-09-03T19:13:55+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.0"
            },
            "require-dev": {
                "ext-tokenizer": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-1.x": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
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
            "description": "A PSR-5 based resolver of Class names, Types and Structural Element Names",
            "support": {
                "issues": "https://github.com/phpDocumentor/TypeResolver/issues",
                "source": "https://github.com/phpDocumentor/TypeResolver/tree/1.4.0"
            },
            "time": "2020-09-17T18:55:26+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "1.13.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "be1996ed8adc35c3fd795488a653f4b518be70ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/be1996ed8adc35c3fd795488a653f4b518be70ea",
                "reference": "be1996ed8adc35c3fd795488a653f4b518be70ea",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.2",
                "php": "^7.2 || ~8.0, <8.1",
                "phpdocumentor/reflection-docblock": "^5.2",
                "sebastian/comparator": "^3.0 || ^4.0",
                "sebastian/recursion-context": "^3.0 || ^4.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^6.0",
                "phpunit/phpunit": "^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Prophecy\\": "src/Prophecy"
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
            "support": {
                "issues": "https://github.com/phpspec/prophecy/issues",
                "source": "https://github.com/phpspec/prophecy/tree/1.13.0"
            },
            "time": "2021-03-17T13:42:18+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "9.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "f6293e1b30a2354e8428e004689671b83871edde"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/f6293e1b30a2354e8428e004689671b83871edde",
                "reference": "f6293e1b30a2354e8428e004689671b83871edde",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "ext-xmlwriter": "*",
                "nikic/php-parser": "^4.10.2",
                "php": ">=7.3",
                "phpunit/php-file-iterator": "^3.0.3",
                "phpunit/php-text-template": "^2.0.2",
                "sebastian/code-unit-reverse-lookup": "^2.0.2",
                "sebastian/complexity": "^2.0",
                "sebastian/environment": "^5.1.2",
                "sebastian/lines-of-code": "^1.0.3",
                "sebastian/version": "^3.0.1",
                "theseer/tokenizer": "^1.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcov": "*",
                "ext-xdebug": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.2-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-code-coverage/issues",
                "source": "https://github.com/sebastianbergmann/php-code-coverage/tree/9.2.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-03-28T07:26:59+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "3.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/aa4be8575f26070b100fccb67faabb28f21f66f8",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-file-iterator/issues",
                "source": "https://github.com/sebastianbergmann/php-file-iterator/tree/3.0.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:57:25+00:00"
        },
        {
            "name": "phpunit/php-invoker",
            "version": "3.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-invoker.git",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-invoker/zipball/5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "ext-pcntl": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcntl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1-dev"
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
            "description": "Invoke callables with a timeout",
            "homepage": "https://github.com/sebastianbergmann/php-invoker/",
            "keywords": [
                "process"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-invoker/issues",
                "source": "https://github.com/sebastianbergmann/php-invoker/tree/3.1.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:58:55+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-text-template/issues",
                "source": "https://github.com/sebastianbergmann/php-text-template/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T05:33:50+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "5.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-timer/issues",
                "source": "https://github.com/sebastianbergmann/php-timer/tree/5.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:16:10+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "9.5.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "191768ccd5c85513b4068bdbe99bb6390c7d54fb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/191768ccd5c85513b4068bdbe99bb6390c7d54fb",
                "reference": "191768ccd5c85513b4068bdbe99bb6390c7d54fb",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.3.1",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "ext-xmlwriter": "*",
                "myclabs/deep-copy": "^1.10.1",
                "phar-io/manifest": "^2.0.3",
                "phar-io/version": "^3.0.2",
                "php": ">=7.3",
                "phpspec/prophecy": "^1.12.1",
                "phpunit/php-code-coverage": "^9.2.3",
                "phpunit/php-file-iterator": "^3.0.5",
                "phpunit/php-invoker": "^3.1.1",
                "phpunit/php-text-template": "^2.0.3",
                "phpunit/php-timer": "^5.0.2",
                "sebastian/cli-parser": "^1.0.1",
                "sebastian/code-unit": "^1.0.6",
                "sebastian/comparator": "^4.0.5",
                "sebastian/diff": "^4.0.3",
                "sebastian/environment": "^5.1.3",
                "sebastian/exporter": "^4.0.3",
                "sebastian/global-state": "^5.0.1",
                "sebastian/object-enumerator": "^4.0.3",
                "sebastian/resource-operations": "^3.0.3",
                "sebastian/type": "^2.3.4",
                "sebastian/version": "^3.0.2"
            },
            "require-dev": {
                "ext-pdo": "*",
                "phpspec/prophecy-phpunit": "^2.0.1"
            },
            "suggest": {
                "ext-soap": "*",
                "ext-xdebug": "*"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.5-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ],
                "files": [
                    "src/Framework/Assert/Functions.php"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/phpunit/issues",
                "source": "https://github.com/sebastianbergmann/phpunit/tree/9.5.8"
            },
            "funding": [
                {
                    "url": "https://phpunit.de/donate.html",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-07-31T15:17:34+00:00"
        },
        {
            "name": "sebastian/cli-parser",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/cli-parser.git",
                "reference": "442e7c7e687e42adc03470c7b668bc4b2402c0b2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/cli-parser/zipball/442e7c7e687e42adc03470c7b668bc4b2402c0b2",
                "reference": "442e7c7e687e42adc03470c7b668bc4b2402c0b2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for parsing CLI options",
            "homepage": "https://github.com/sebastianbergmann/cli-parser",
            "support": {
                "issues": "https://github.com/sebastianbergmann/cli-parser/issues",
                "source": "https://github.com/sebastianbergmann/cli-parser/tree/1.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:08:49+00:00"
        },
        {
            "name": "sebastian/code-unit",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit.git",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit/zipball/1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the PHP code units",
            "homepage": "https://github.com/sebastianbergmann/code-unit",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit/issues",
                "source": "https://github.com/sebastianbergmann/code-unit/tree/1.0.8"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:08:54+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/issues",
                "source": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/tree/2.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:30:19+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "4.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/55f4261989e546dc112258c7a75935a81a7ce382",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/diff": "^4.0",
                "sebastian/exporter": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
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
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/comparator/issues",
                "source": "https://github.com/sebastianbergmann/comparator/tree/4.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T15:49:45+00:00"
        },
        {
            "name": "sebastian/complexity",
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/complexity.git",
                "reference": "739b35e53379900cc9ac327b2147867b8b6efd88"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/complexity/zipball/739b35e53379900cc9ac327b2147867b8b6efd88",
                "reference": "739b35e53379900cc9ac327b2147867b8b6efd88",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.7",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Library for calculating the complexity of PHP code units",
            "homepage": "https://github.com/sebastianbergmann/complexity",
            "support": {
                "issues": "https://github.com/sebastianbergmann/complexity/issues",
                "source": "https://github.com/sebastianbergmann/complexity/tree/2.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T15:52:27+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3",
                "symfony/process": "^4.2 || ^5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/diff/issues",
                "source": "https://github.com/sebastianbergmann/diff/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:10:38+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "5.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/388b6ced16caa751030f6a69e588299fa09200ac",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.1-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/environment/issues",
                "source": "https://github.com/sebastianbergmann/environment/tree/5.1.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:52:38+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "4.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/exporter/issues",
                "source": "https://github.com/sebastianbergmann/exporter/tree/4.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:24:23+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "5.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "23bd5951f7ff26f12d4e3242864df3e08dec4e49"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/23bd5951f7ff26f12d4e3242864df3e08dec4e49",
                "reference": "23bd5951f7ff26f12d4e3242864df3e08dec4e49",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-dom": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/global-state/issues",
                "source": "https://github.com/sebastianbergmann/global-state/tree/5.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-06-11T13:31:12+00:00"
        },
        {
            "name": "sebastian/lines-of-code",
            "version": "1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/lines-of-code.git",
                "reference": "c1c2e997aa3146983ed888ad08b15470a2e22ecc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/lines-of-code/zipball/c1c2e997aa3146983ed888ad08b15470a2e22ecc",
                "reference": "c1c2e997aa3146983ed888ad08b15470a2e22ecc",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.6",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for counting the lines of code in PHP source code",
            "homepage": "https://github.com/sebastianbergmann/lines-of-code",
            "support": {
                "issues": "https://github.com/sebastianbergmann/lines-of-code/issues",
                "source": "https://github.com/sebastianbergmann/lines-of-code/tree/1.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-11-28T06:42:11+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/5c9eeac41b290a3712d88851518825ad78f45c71",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-enumerator/issues",
                "source": "https://github.com/sebastianbergmann/object-enumerator/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:12:34+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-reflector/issues",
                "source": "https://github.com/sebastianbergmann/object-reflector/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:14:26+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/cd9d8cf3c5804de4341c283ed787f099f5506172",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "support": {
                "issues": "https://github.com/sebastianbergmann/recursion-context/issues",
                "source": "https://github.com/sebastianbergmann/recursion-context/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:17:30+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
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
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "support": {
                "issues": "https://github.com/sebastianbergmann/resource-operations/issues",
                "source": "https://github.com/sebastianbergmann/resource-operations/tree/3.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:45:17+00:00"
        },
        {
            "name": "sebastian/type",
            "version": "2.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/type.git",
                "reference": "b8cd8a1c753c90bc1a0f5372170e3e489136f914"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/type/zipball/b8cd8a1c753c90bc1a0f5372170e3e489136f914",
                "reference": "b8cd8a1c753c90bc1a0f5372170e3e489136f914",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
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
            "description": "Collection of value objects that represent the types of the PHP type system",
            "homepage": "https://github.com/sebastianbergmann/type",
            "support": {
                "issues": "https://github.com/sebastianbergmann/type/issues",
                "source": "https://github.com/sebastianbergmann/type/tree/2.3.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-06-15T12:49:02+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "c6c1022351a901512170118436c764e473f6de8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/c6c1022351a901512170118436c764e473f6de8c",
                "reference": "c6c1022351a901512170118436c764e473f6de8c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "support": {
                "issues": "https://github.com/sebastianbergmann/version/issues",
                "source": "https://github.com/sebastianbergmann/version/tree/3.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:39:44+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "34a41e998c2183e22995f158c581e7b5e755ab9e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/34a41e998c2183e22995f158c581e7b5e755ab9e",
                "reference": "34a41e998c2183e22995f158c581e7b5e755ab9e",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/theseer/tokenizer/issues",
                "source": "https://github.com/theseer/tokenizer/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2021-07-28T10:34:58+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "dev",
    "stability-flags": [],
    "prefer-stable": true,
    "prefer-lowest": false,
    "platform": {
        "php": "^7.3|^8.0"
    },
    "platform-dev": [],
    "plugin-api-version": "2.1.0"
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

    'debug' => (bool) env('APP_DEBUG', false),

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

    'asset_url' => env('ASSET_URL', null),

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
    | Faker Locale
    |--------------------------------------------------------------------------
    |
    | This locale will be used by the Faker PHP library when generating fake
    | data for your database seeds. For example, this will be used to get
    | localized telephone numbers, street address information and more.
    |
    */

    'faker_locale' => 'en_US',

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
        \Safaricom\Mpesa\MpesaServiceProvider::class,


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
        'Arr' => Illuminate\Support\Arr::class,
        'Artisan' => Illuminate\Support\Facades\Artisan::class,
        'Auth' => Illuminate\Support\Facades\Auth::class,
        'Blade' => Illuminate\Support\Facades\Blade::class,
        'Broadcast' => Illuminate\Support\Facades\Broadcast::class,
        'Bus' => Illuminate\Support\Facades\Bus::class,
        'Cache' => Illuminate\Support\Facades\Cache::class,
        'Config' => Illuminate\Support\Facades\Config::class,
        'Cookie' => Illuminate\Support\Facades\Cookie::class,
        'Crypt' => Illuminate\Support\Facades\Crypt::class,
        'Date' => Illuminate\Support\Facades\Date::class,
        'DB' => Illuminate\Support\Facades\DB::class,
        'Eloquent' => Illuminate\Database\Eloquent\Model::class,
        'Event' => Illuminate\Support\Facades\Event::class,
        'File' => Illuminate\Support\Facades\File::class,
        'Gate' => Illuminate\Support\Facades\Gate::class,
        'Hash' => Illuminate\Support\Facades\Hash::class,
        'Http' => Illuminate\Support\Facades\Http::class,
        'Lang' => Illuminate\Support\Facades\Lang::class,
        'Log' => Illuminate\Support\Facades\Log::class,
        'Mail' => Illuminate\Support\Facades\Mail::class,
        'Notification' => Illuminate\Support\Facades\Notification::class,
        'Password' => Illuminate\Support\Facades\Password::class,
        'Queue' => Illuminate\Support\Facades\Queue::class,
        'RateLimiter' => Illuminate\Support\Facades\RateLimiter::class,
        'Redirect' => Illuminate\Support\Facades\Redirect::class,
        // 'Redis' => Illuminate\Support\Facades\Redis::class,
        'Request' => Illuminate\Support\Facades\Request::class,
        'Response' => Illuminate\Support\Facades\Response::class,
        'Route' => Illuminate\Support\Facades\Route::class,
        'Schema' => Illuminate\Support\Facades\Schema::class,
        'Session' => Illuminate\Support\Facades\Session::class,
        'Storage' => Illuminate\Support\Facades\Storage::class,
        'Str' => Illuminate\Support\Str::class,
        'URL' => Illuminate\Support\Facades\URL::class,
        'Validator' => Illuminate\Support\Facades\Validator::class,
        'View' => Illuminate\Support\Facades\View::class,
        'Mpesa'=> \Safaricom\Mpesa\MpesaServiceProvider::class,


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
    | Supported: "session"
    |
    */

    'guards' => [
        'web' => [
            'driver' => 'session',
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
            'model' => App\Models\User::class,
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
            'throttle' => 60,
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Password Confirmation Timeout
    |--------------------------------------------------------------------------
    |
    | Here you may define the amount of seconds before a password confirmation
    | times out and the user is prompted to re-enter their password via the
    | confirmation screen. By default, the timeout lasts for three hours.
    |
    */

    'password_timeout' => 10800,

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
    | Supported: "pusher", "ably", "redis", "log", "null"
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
                'useTLS' => true,
            ],
        ],

        'ably' => [
            'driver' => 'ably',
            'key' => env('ABLY_KEY'),
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

use Illuminate\Support\Str;

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
    | Supported drivers: "apc", "array", "database", "file",
    |         "memcached", "redis", "dynamodb", "octane", "null"
    |
    */

    'stores' => [

        'apc' => [
            'driver' => 'apc',
        ],

        'array' => [
            'driver' => 'array',
            'serialize' => false,
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'cache',
            'connection' => null,
            'lock_connection' => null,
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
                // Memcached::OPT_CONNECT_TIMEOUT => 2000,
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
            'lock_connection' => 'default',
        ],

        'dynamodb' => [
            'driver' => 'dynamodb',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
            'table' => env('DYNAMODB_CACHE_TABLE', 'cache'),
            'endpoint' => env('DYNAMODB_ENDPOINT'),
        ],

        'octane' => [
            'driver' => 'octane',
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

    'prefix' => env('CACHE_PREFIX', Str::slug(env('APP_NAME', 'laravel'), '_').'_cache'),

];


File: /config\cors.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Cross-Origin Resource Sharing (CORS) Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may configure your settings for cross-origin resource sharing
    | or "CORS". This determines what cross-origin operations may execute
    | in web browsers. You are free to adjust these settings as needed.
    |
    | To learn more: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    |
    */

    'paths' => ['api/*', 'sanctum/csrf-cookie'],

    'allowed_methods' => ['*'],

    'allowed_origins' => ['*'],

    'allowed_origins_patterns' => [],

    'allowed_headers' => ['*'],

    'exposed_headers' => [],

    'max_age' => 0,

    'supports_credentials' => false,

];


File: /config\database.php
<?php

use Illuminate\Support\Str;

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
            'url' => env('DATABASE_URL'),
            'database' => env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' => '',
            'foreign_key_constraints' => env('DB_FOREIGN_KEYS', true),
        ],

        'mysql' => [
            'driver' => 'mysql',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'prefix_indexes' => true,
            'strict' => true,
            'engine' => null,
            'options' => extension_loaded('pdo_mysql') ? array_filter([
                PDO::MYSQL_ATTR_SSL_CA => env('MYSQL_ATTR_SSL_CA'),
            ]) : [],
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'prefix_indexes' => true,
            'schema' => 'public',
            'sslmode' => 'prefer',
        ],

        'sqlsrv' => [
            'driver' => 'sqlsrv',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '1433'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'prefix_indexes' => true,
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
    | provides a richer body of commands than a typical key-value system
    | such as APC or Memcached. Laravel makes it easy to dig right in.
    |
    */

    'redis' => [

        'client' => env('REDIS_CLIENT', 'phpredis'),

        'options' => [
            'cluster' => env('REDIS_CLUSTER', 'redis'),
            'prefix' => env('REDIS_PREFIX', Str::slug(env('APP_NAME', 'laravel'), '_').'_database_'),
        ],

        'default' => [
            'url' => env('REDIS_URL'),
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', '6379'),
            'database' => env('REDIS_DB', '0'),
        ],

        'cache' => [
            'url' => env('REDIS_URL'),
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', '6379'),
            'database' => env('REDIS_CACHE_DB', '1'),
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
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Here you may configure as many filesystem "disks" as you wish, and you
    | may even configure multiple disks of the same driver. Defaults have
    | been setup for each driver as an example of the required options.
    |
    | Supported Drivers: "local", "ftp", "sftp", "s3"
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
            'endpoint' => env('AWS_ENDPOINT'),
            'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Symbolic Links
    |--------------------------------------------------------------------------
    |
    | Here you may configure the symbolic links that will be created when the
    | `storage:link` Artisan command is executed. The array keys should be
    | the locations of the links and the values should be their targets.
    |
    */

    'links' => [
        public_path('storage') => storage_path('app/public'),
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

use Monolog\Handler\NullHandler;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\SyslogUdpHandler;

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
            'ignore_exceptions' => false,
        ],

        'single' => [
            'driver' => 'single',
            'path' => storage_path('logs/laravel.log'),
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'daily' => [
            'driver' => 'daily',
            'path' => storage_path('logs/laravel.log'),
            'level' => env('LOG_LEVEL', 'debug'),
            'days' => 14,
        ],

        'slack' => [
            'driver' => 'slack',
            'url' => env('LOG_SLACK_WEBHOOK_URL'),
            'username' => 'Laravel Log',
            'emoji' => ':boom:',
            'level' => env('LOG_LEVEL', 'critical'),
        ],

        'papertrail' => [
            'driver' => 'monolog',
            'level' => env('LOG_LEVEL', 'debug'),
            'handler' => SyslogUdpHandler::class,
            'handler_with' => [
                'host' => env('PAPERTRAIL_URL'),
                'port' => env('PAPERTRAIL_PORT'),
            ],
        ],

        'stderr' => [
            'driver' => 'monolog',
            'level' => env('LOG_LEVEL', 'debug'),
            'handler' => StreamHandler::class,
            'formatter' => env('LOG_STDERR_FORMATTER'),
            'with' => [
                'stream' => 'php://stderr',
            ],
        ],

        'syslog' => [
            'driver' => 'syslog',
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'errorlog' => [
            'driver' => 'errorlog',
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'null' => [
            'driver' => 'monolog',
            'handler' => NullHandler::class,
        ],

        'emergency' => [
            'path' => storage_path('logs/laravel.log'),
        ],
    ],

];


File: /config\mail.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Mailer
    |--------------------------------------------------------------------------
    |
    | This option controls the default mailer that is used to send any email
    | messages sent by your application. Alternative mailers may be setup
    | and used as needed; however, this mailer will be used by default.
    |
    */

    'default' => env('MAIL_MAILER', 'smtp'),

    /*
    |--------------------------------------------------------------------------
    | Mailer Configurations
    |--------------------------------------------------------------------------
    |
    | Here you may configure all of the mailers used by your application plus
    | their respective settings. Several examples have been configured for
    | you and you are free to add your own as your application requires.
    |
    | Laravel supports a variety of mail "transport" drivers to be used while
    | sending an e-mail. You will specify which one you are using for your
    | mailers below. You are free to add additional mailers as required.
    |
    | Supported: "smtp", "sendmail", "mailgun", "ses",
    |            "postmark", "log", "array"
    |
    */

    'mailers' => [
        'smtp' => [
            'transport' => 'smtp',
            'host' => env('MAIL_HOST', 'smtp.mailgun.org'),
            'port' => env('MAIL_PORT', 587),
            'encryption' => env('MAIL_ENCRYPTION', 'tls'),
            'username' => env('MAIL_USERNAME'),
            'password' => env('MAIL_PASSWORD'),
            'timeout' => null,
            'auth_mode' => null,
        ],

        'ses' => [
            'transport' => 'ses',
        ],

        'mailgun' => [
            'transport' => 'mailgun',
        ],

        'postmark' => [
            'transport' => 'postmark',
        ],

        'sendmail' => [
            'transport' => 'sendmail',
            'path' => '/usr/sbin/sendmail -bs',
        ],

        'log' => [
            'transport' => 'log',
            'channel' => env('MAIL_LOG_CHANNEL'),
        ],

        'array' => [
            'transport' => 'array',
        ],
    ],

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
            'after_commit' => false,
        ],

        'beanstalkd' => [
            'driver' => 'beanstalkd',
            'host' => 'localhost',
            'queue' => 'default',
            'retry_after' => 90,
            'block_for' => 0,
            'after_commit' => false,
        ],

        'sqs' => [
            'driver' => 'sqs',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'prefix' => env('SQS_PREFIX', 'https://sqs.us-east-1.amazonaws.com/your-account-id'),
            'queue' => env('SQS_QUEUE', 'default'),
            'suffix' => env('SQS_SUFFIX'),
            'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
            'after_commit' => false,
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => env('REDIS_QUEUE', 'default'),
            'retry_after' => 90,
            'block_for' => null,
            'after_commit' => false,
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
        'driver' => env('QUEUE_FAILED_DRIVER', 'database-uuids'),
        'database' => env('DB_CONNECTION', 'mysql'),
        'table' => 'failed_jobs',
    ],

];


File: /config\sanctum.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Stateful Domains
    |--------------------------------------------------------------------------
    |
    | Requests from the following domains / hosts will receive stateful API
    | authentication cookies. Typically, these should include your local
    | and production domains which access your API via a frontend SPA.
    |
    */

    'stateful' => explode(',', env('SANCTUM_STATEFUL_DOMAINS', sprintf(
        '%s%s',
        'localhost,localhost:3000,127.0.0.1,127.0.0.1:8000,::1',
        env('APP_URL') ? ','.parse_url(env('APP_URL'), PHP_URL_HOST) : ''
    ))),

    /*
    |--------------------------------------------------------------------------
    | Expiration Minutes
    |--------------------------------------------------------------------------
    |
    | This value controls the number of minutes until an issued token will be
    | considered expired. If this value is null, personal access tokens do
    | not expire. This won't tweak the lifetime of first-party sessions.
    |
    */

    'expiration' => null,

    /*
    |--------------------------------------------------------------------------
    | Sanctum Middleware
    |--------------------------------------------------------------------------
    |
    | When authenticating your first-party SPA with Sanctum you may need to
    | customize some of the middleware Sanctum uses while processing the
    | request. You may change the middleware listed below as required.
    |
    */

    'middleware' => [
        'verify_csrf_token' => App\Http\Middleware\VerifyCsrfToken::class,
        'encrypt_cookies' => App\Http\Middleware\EncryptCookies::class,
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
    | as Mailgun, Postmark, AWS and more. This file provides the de facto
    | location for this type of information, allowing packages to have
    | a conventional file to locate the various service credentials.
    |
    */

    'mailgun' => [
        'domain' => env('MAILGUN_DOMAIN'),
        'secret' => env('MAILGUN_SECRET'),
        'endpoint' => env('MAILGUN_ENDPOINT', 'api.mailgun.net'),
    ],

    'postmark' => [
        'token' => env('POSTMARK_TOKEN'),
    ],

    'ses' => [
        'key' => env('AWS_ACCESS_KEY_ID'),
        'secret' => env('AWS_SECRET_ACCESS_KEY'),
        'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    ],

];


File: /config\session.php
<?php

use Illuminate\Support\Str;

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
    |            "memcached", "redis", "dynamodb", "array"
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
    | While using one of the framework's cache driven session backends you may
    | list a cache store that should be used for these sessions. This value
    | must match with one of the application's configured cache "stores".
    |
    | Affects: "apc", "dynamodb", "memcached", "redis"
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
        Str::slug(env('APP_NAME', 'laravel'), '_').'_session'
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
    | the cookie from being sent to you when it can't be done securely.
    |
    */

    'secure' => env('SESSION_SECURE_COOKIE'),

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
    | will set this value to "lax" since this is a secure default value.
    |
    | Supported: "lax", "strict", "none", null
    |
    */

    'same_site' => 'lax',

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

    'compiled' => env(
        'VIEW_COMPILED_PATH',
        realpath(storage_path('framework/views'))
    ),

];


File: /database\.gitignore
*.sqlite*


File: /database\factories\UserFactory.php
<?php

namespace Database\Factories;

use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

class UserFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = User::class;

    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'name' => $this->faker->name(),
            'email' => $this->faker->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', // password
            'remember_token' => Str::random(10),
        ];
    }

    /**
     * Indicate that the model's email address should be unverified.
     *
     * @return \Illuminate\Database\Eloquent\Factories\Factory
     */
    public function unverified()
    {
        return $this->state(function (array $attributes) {
            return [
                'email_verified_at' => null,
            ];
        });
    }
}


File: /database\migrations\2014_10_12_000000_create_users_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

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
            $table->id();
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

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

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


File: /database\migrations\2019_08_19_000000_create_failed_jobs_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateFailedJobsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('failed_jobs', function (Blueprint $table) {
            $table->id();
            $table->string('uuid')->unique();
            $table->text('connection');
            $table->text('queue');
            $table->longText('payload');
            $table->longText('exception');
            $table->timestamp('failed_at')->useCurrent();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('failed_jobs');
    }
}


File: /database\migrations\2019_12_14_000001_create_personal_access_tokens_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePersonalAccessTokensTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('personal_access_tokens', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->morphs('tokenable');
            $table->string('name');
            $table->string('token', 64)->unique();
            $table->text('abilities')->nullable();
            $table->timestamp('last_used_at')->nullable();
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
        Schema::dropIfExists('personal_access_tokens');
    }
}


File: /database\seeders\DatabaseSeeder.php
<?php

namespace Database\Seeders;

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
        // \App\Models\User::factory(10)->create();
    }
}


File: /mikrotik-payment\.editorconfig
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

[*.{yml,yaml}]
indent_size = 2

[docker-compose.yml]
indent_size = 4


File: /mikrotik-payment\.env.example
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
FILESYSTEM_DRIVER=local
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=null
MAIL_FROM_NAME="${APP_NAME}"

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=
AWS_USE_PATH_STYLE_ENDPOINT=false

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"


File: /mikrotik-payment\.gitattributes
* text=auto
*.css linguist-vendored
*.scss linguist-vendored
*.js linguist-vendored
CHANGELOG.md export-ignore


File: /mikrotik-payment\.gitignore
/node_modules
/public/hot
/public/storage
/storage/*.key
/vendor
.env
.env.backup
.phpunit.result.cache
docker-compose.override.yml
Homestead.json
Homestead.yaml
File: /mikrotik-payment\.styleci.yml
php:
  preset: laravel
  version: 8
  disabled:
    - no_unused_imports
  finder:
    not-name:
      - index.php
      - server.php
js:
  finder:
    not-name:
      - webpack.mix.js
css: true


File: /mikrotik-payment\app\Console\Kernel.php
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
        // $schedule->command('inspire')->hourly();
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


File: /mikrotik-payment\app\Exceptions\Handler.php
<?php

namespace App\Exceptions;

use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Throwable;

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
        'current_password',
        'password',
        'password_confirmation',
    ];

    /**
     * Register the exception handling callbacks for the application.
     *
     * @return void
     */
    public function register()
    {
        $this->reportable(function (Throwable $e) {
            //
        });
    }
}


File: /mikrotik-payment\app\Http\Controllers\Controller.php
<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;
}


File: /mikrotik-payment\app\Http\Kernel.php
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
        // \App\Http\Middleware\TrustHosts::class,
        \App\Http\Middleware\TrustProxies::class,
        \Fruitcake\Cors\HandleCors::class,
        \App\Http\Middleware\PreventRequestsDuringMaintenance::class,
        \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
        \App\Http\Middleware\TrimStrings::class,
        \Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull::class,
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
            // \Laravel\Sanctum\Http\Middleware\EnsureFrontendRequestsAreStateful::class,
            'throttle:api',
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
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
        'cache.headers' => \Illuminate\Http\Middleware\SetCacheHeaders::class,
        'can' => \Illuminate\Auth\Middleware\Authorize::class,
        'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
        'password.confirm' => \Illuminate\Auth\Middleware\RequirePassword::class,
        'signed' => \Illuminate\Routing\Middleware\ValidateSignature::class,
        'throttle' => \Illuminate\Routing\Middleware\ThrottleRequests::class,
        'verified' => \Illuminate\Auth\Middleware\EnsureEmailIsVerified::class,
    ];
}


File: /mikrotik-payment\app\Http\Middleware\Authenticate.php
<?php

namespace App\Http\Middleware;

use Illuminate\Auth\Middleware\Authenticate as Middleware;

class Authenticate extends Middleware
{
    /**
     * Get the path the user should be redirected to when they are not authenticated.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return string|null
     */
    protected function redirectTo($request)
    {
        if (! $request->expectsJson()) {
            return route('login');
        }
    }
}


File: /mikrotik-payment\app\Http\Middleware\EncryptCookies.php
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


File: /mikrotik-payment\app\Http\Middleware\PreventRequestsDuringMaintenance.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance as Middleware;

class PreventRequestsDuringMaintenance extends Middleware
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


File: /mikrotik-payment\app\Http\Middleware\RedirectIfAuthenticated.php
<?php

namespace App\Http\Middleware;

use App\Providers\RouteServiceProvider;
use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class RedirectIfAuthenticated
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @param  string|null  ...$guards
     * @return mixed
     */
    public function handle(Request $request, Closure $next, ...$guards)
    {
        $guards = empty($guards) ? [null] : $guards;

        foreach ($guards as $guard) {
            if (Auth::guard($guard)->check()) {
                return redirect(RouteServiceProvider::HOME);
            }
        }

        return $next($request);
    }
}


File: /mikrotik-payment\app\Http\Middleware\TrimStrings.php
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
        'current_password',
        'password',
        'password_confirmation',
    ];
}


File: /mikrotik-payment\app\Http\Middleware\TrustHosts.php
<?php

namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustHosts as Middleware;

class TrustHosts extends Middleware
{
    /**
     * Get the host patterns that should be trusted.
     *
     * @return array
     */
    public function hosts()
    {
        return [
            $this->allSubdomainsOfApplicationUrl(),
        ];
    }
}


File: /mikrotik-payment\app\Http\Middleware\TrustProxies.php
<?php

namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustProxies as Middleware;
use Illuminate\Http\Request;

class TrustProxies extends Middleware
{
    /**
     * The trusted proxies for this application.
     *
     * @var array|string|null
     */
    protected $proxies;

    /**
     * The headers that should be used to detect proxies.
     *
     * @var int
     */
    protected $headers = Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_HOST | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO | Request::HEADER_X_FORWARDED_AWS_ELB;
}


File: /mikrotik-payment\app\Http\Middleware\VerifyCsrfToken.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
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


File: /mikrotik-payment\app\Models\User.php
<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];
}


File: /mikrotik-payment\app\Providers\AppServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    }

    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }
}


File: /mikrotik-payment\app\Providers\AuthServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Gate;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array
     */
    protected $policies = [
        // 'App\Models\Model' => 'App\Policies\ModelPolicy',
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


File: /mikrotik-payment\app\Providers\BroadcastServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\Facades\Broadcast;
use Illuminate\Support\ServiceProvider;

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


File: /mikrotik-payment\app\Providers\EventServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Auth\Events\Registered;
use Illuminate\Auth\Listeners\SendEmailVerificationNotification;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;
use Illuminate\Support\Facades\Event;

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
        //
    }
}


File: /mikrotik-payment\app\Providers\RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Illuminate\Support\Facades\Route;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * The path to the "home" route for your application.
     *
     * This is used by Laravel authentication to redirect users after login.
     *
     * @var string
     */
    public const HOME = '/home';

    /**
     * The controller namespace for the application.
     *
     * When present, controller route declarations will automatically be prefixed with this namespace.
     *
     * @var string|null
     */
    // protected $namespace = 'App\\Http\\Controllers';

    /**
     * Define your route model bindings, pattern filters, etc.
     *
     * @return void
     */
    public function boot()
    {
        $this->configureRateLimiting();

        $this->routes(function () {
            Route::prefix('api')
                ->middleware('api')
                ->namespace($this->namespace)
                ->group(base_path('routes/api.php'));

            Route::middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/web.php'));
        });
    }

    /**
     * Configure the rate limiters for the application.
     *
     * @return void
     */
    protected function configureRateLimiting()
    {
        RateLimiter::for('api', function (Request $request) {
            return Limit::perMinute(60)->by(optional($request->user())->id ?: $request->ip());
        });
    }
}


File: /mikrotik-payment\artisan
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
| loading of any of our classes manually. It's great to relax.
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


File: /mikrotik-payment\bootstrap\app.php
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
    $_ENV['APP_BASE_PATH'] ?? dirname(__DIR__)
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


File: /mikrotik-payment\bootstrap\cache\.gitignore
*
!.gitignore


File: /mikrotik-payment\composer.json
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The Laravel Framework.",
    "keywords": ["framework", "laravel"],
    "license": "MIT",
    "require": {
        "php": "^7.3|^8.0",
        "fruitcake/laravel-cors": "^2.0",
        "guzzlehttp/guzzle": "^7.0.1",
        "laravel/framework": "^8.54",
        "laravel/sanctum": "^2.11",
        "laravel/tinker": "^2.5"
    },
    "require-dev": {
        "facade/ignition": "^2.5",
        "fakerphp/faker": "^1.9.1",
        "laravel/sail": "^1.0.1",
        "mockery/mockery": "^1.4.2",
        "nunomaduro/collision": "^5.0",
        "phpunit/phpunit": "^9.3.3"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true
    },
    "minimum-stability": "dev",
    "prefer-stable": true
}


File: /mikrotik-payment\composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "6cadd819a6415b190ae2704ced6e6c8b",
    "packages": [
        {
            "name": "asm89/stack-cors",
            "version": "v2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/asm89/stack-cors.git",
                "reference": "9cb795bf30988e8c96dd3c40623c48a877bc6714"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/asm89/stack-cors/zipball/9cb795bf30988e8c96dd3c40623c48a877bc6714",
                "reference": "9cb795bf30988e8c96dd3c40623c48a877bc6714",
                "shasum": ""
            },
            "require": {
                "php": "^7.0|^8.0",
                "symfony/http-foundation": "~2.7|~3.0|~4.0|~5.0",
                "symfony/http-kernel": "~2.7|~3.0|~4.0|~5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6|^7|^8|^9",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Asm89\\Stack\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alexander",
                    "email": "iam.asm89@gmail.com"
                }
            ],
            "description": "Cross-origin resource sharing library and stack middleware",
            "homepage": "https://github.com/asm89/stack-cors",
            "keywords": [
                "cors",
                "stack"
            ],
            "support": {
                "issues": "https://github.com/asm89/stack-cors/issues",
                "source": "https://github.com/asm89/stack-cors/tree/v2.0.3"
            },
            "time": "2021-03-11T06:42:03+00:00"
        },
        {
            "name": "brick/math",
            "version": "0.9.3",
            "source": {
                "type": "git",
                "url": "https://github.com/brick/math.git",
                "reference": "ca57d18f028f84f777b2168cd1911b0dee2343ae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/brick/math/zipball/ca57d18f028f84f777b2168cd1911b0dee2343ae",
                "reference": "ca57d18f028f84f777b2168cd1911b0dee2343ae",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.2",
                "phpunit/phpunit": "^7.5.15 || ^8.5 || ^9.0",
                "vimeo/psalm": "4.9.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Brick\\Math\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Arbitrary-precision arithmetic library",
            "keywords": [
                "Arbitrary-precision",
                "BigInteger",
                "BigRational",
                "arithmetic",
                "bigdecimal",
                "bignum",
                "brick",
                "math"
            ],
            "support": {
                "issues": "https://github.com/brick/math/issues",
                "source": "https://github.com/brick/math/tree/0.9.3"
            },
            "funding": [
                {
                    "url": "https://github.com/BenMorel",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/brick/math",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-15T20:50:18+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "9cf661f4eb38f7c881cac67c75ea9b00bf97b210"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/9cf661f4eb38f7c881cac67c75ea9b00bf97b210",
                "reference": "9cf661f4eb38f7c881cac67c75ea9b00bf97b210",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^7.0",
                "phpstan/phpstan": "^0.11",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpstan/phpstan-strict-rules": "^0.11",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Inflector\\": "lib/Doctrine/Inflector"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
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
            "description": "PHP Doctrine Inflector is a small library that can perform string manipulations with regard to upper/lowercase and singular/plural forms of words.",
            "homepage": "https://www.doctrine-project.org/projects/inflector.html",
            "keywords": [
                "inflection",
                "inflector",
                "lowercase",
                "manipulation",
                "php",
                "plural",
                "singular",
                "strings",
                "uppercase",
                "words"
            ],
            "support": {
                "issues": "https://github.com/doctrine/inflector/issues",
                "source": "https://github.com/doctrine/inflector/tree/2.0.x"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finflector",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-29T15:13:26+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/e864bbf5904cb8f5bb334f99209b48018522f042",
                "reference": "e864bbf5904cb8f5bb334f99209b48018522f042",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.11.8",
                "phpunit/phpunit": "^8.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Lexer\\": "lib/Doctrine/Common/Lexer"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Lexer parser library that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "https://www.doctrine-project.org/projects/lexer.html",
            "keywords": [
                "annotations",
                "docblock",
                "lexer",
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/lexer/issues",
                "source": "https://github.com/doctrine/lexer/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Flexer",
                    "type": "tidelift"
                }
            ],
            "time": "2020-05-25T17:44:05+00:00"
        },
        {
            "name": "dragonmantank/cron-expression",
            "version": "v3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/dragonmantank/cron-expression.git",
                "reference": "7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dragonmantank/cron-expression/zipball/7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c",
                "reference": "7a8c6e56ab3ffcc538d05e8155bb42269abf1a0c",
                "shasum": ""
            },
            "require": {
                "php": "^7.2|^8.0",
                "webmozart/assert": "^1.7.0"
            },
            "replace": {
                "mtdowling/cron-expression": "^1.0"
            },
            "require-dev": {
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-webmozart-assert": "^0.12.7",
                "phpunit/phpunit": "^7.0|^8.0|^9.0"
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
            "support": {
                "issues": "https://github.com/dragonmantank/cron-expression/issues",
                "source": "https://github.com/dragonmantank/cron-expression/tree/v3.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/dragonmantank",
                    "type": "github"
                }
            ],
            "time": "2020-11-24T19:55:57+00:00"
        },
        {
            "name": "egulias/email-validator",
            "version": "2.1.25",
            "source": {
                "type": "git",
                "url": "https://github.com/egulias/EmailValidator.git",
                "reference": "0dbf5d78455d4d6a41d186da50adc1122ec066f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/egulias/EmailValidator/zipball/0dbf5d78455d4d6a41d186da50adc1122ec066f4",
                "reference": "0dbf5d78455d4d6a41d186da50adc1122ec066f4",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "^1.0.1",
                "php": ">=5.5",
                "symfony/polyfill-intl-idn": "^1.10"
            },
            "require-dev": {
                "dominicsayers/isemail": "^3.0.7",
                "phpunit/phpunit": "^4.8.36|^7.5.15",
                "satooshi/php-coveralls": "^1.0.1"
            },
            "suggest": {
                "ext-intl": "PHP Internationalization Libraries are required to use the SpoofChecking validation"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Egulias\\EmailValidator\\": "src"
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
            "support": {
                "issues": "https://github.com/egulias/EmailValidator/issues",
                "source": "https://github.com/egulias/EmailValidator/tree/2.1.25"
            },
            "funding": [
                {
                    "url": "https://github.com/egulias",
                    "type": "github"
                }
            ],
            "time": "2020-12-29T14:50:06+00:00"
        },
        {
            "name": "fruitcake/laravel-cors",
            "version": "v2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/fruitcake/laravel-cors.git",
                "reference": "a8ccedc7ca95189ead0e407c43b530dc17791d6a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fruitcake/laravel-cors/zipball/a8ccedc7ca95189ead0e407c43b530dc17791d6a",
                "reference": "a8ccedc7ca95189ead0e407c43b530dc17791d6a",
                "shasum": ""
            },
            "require": {
                "asm89/stack-cors": "^2.0.1",
                "illuminate/contracts": "^6|^7|^8|^9",
                "illuminate/support": "^6|^7|^8|^9",
                "php": ">=7.2",
                "symfony/http-foundation": "^4|^5",
                "symfony/http-kernel": "^4.3.4|^5"
            },
            "require-dev": {
                "laravel/framework": "^6|^7|^8",
                "orchestra/testbench-dusk": "^4|^5|^6|^7",
                "phpunit/phpunit": "^6|^7|^8|^9",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                },
                "laravel": {
                    "providers": [
                        "Fruitcake\\Cors\\CorsServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Fruitcake\\Cors\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fruitcake",
                    "homepage": "https://fruitcake.nl"
                },
                {
                    "name": "Barry vd. Heuvel",
                    "email": "barryvdh@gmail.com"
                }
            ],
            "description": "Adds CORS (Cross-Origin Resource Sharing) headers support in your Laravel application",
            "keywords": [
                "api",
                "cors",
                "crossdomain",
                "laravel"
            ],
            "support": {
                "issues": "https://github.com/fruitcake/laravel-cors/issues",
                "source": "https://github.com/fruitcake/laravel-cors/tree/v2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/barryvdh",
                    "type": "github"
                }
            ],
            "time": "2021-04-26T11:24:25+00:00"
        },
        {
            "name": "graham-campbell/result-type",
            "version": "v1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/GrahamCampbell/Result-Type.git",
                "reference": "7e279d2cd5d7fbb156ce46daada972355cea27bb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/GrahamCampbell/Result-Type/zipball/7e279d2cd5d7fbb156ce46daada972355cea27bb",
                "reference": "7e279d2cd5d7fbb156ce46daada972355cea27bb",
                "shasum": ""
            },
            "require": {
                "php": "^7.0|^8.0",
                "phpoption/phpoption": "^1.7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.5|^7.5|^8.5|^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GrahamCampbell\\ResultType\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com"
                }
            ],
            "description": "An Implementation Of The Result Type",
            "keywords": [
                "Graham Campbell",
                "GrahamCampbell",
                "Result Type",
                "Result-Type",
                "result"
            ],
            "support": {
                "issues": "https://github.com/GrahamCampbell/Result-Type/issues",
                "source": "https://github.com/GrahamCampbell/Result-Type/tree/v1.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/graham-campbell/result-type",
                    "type": "tidelift"
                }
            ],
            "time": "2020-04-13T13:17:36+00:00"
        },
        {
            "name": "guzzlehttp/guzzle",
            "version": "7.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/guzzle.git",
                "reference": "7008573787b430c1c1f650e3722d9bba59967628"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/guzzle/zipball/7008573787b430c1c1f650e3722d9bba59967628",
                "reference": "7008573787b430c1c1f650e3722d9bba59967628",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "guzzlehttp/promises": "^1.4",
                "guzzlehttp/psr7": "^1.7 || ^2.0",
                "php": "^7.2.5 || ^8.0",
                "psr/http-client": "^1.0"
            },
            "provide": {
                "psr/http-client-implementation": "1.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-curl": "*",
                "php-http/client-integration-tests": "^3.0",
                "phpunit/phpunit": "^8.5.5 || ^9.3.5",
                "psr/log": "^1.1"
            },
            "suggest": {
                "ext-curl": "Required for CURL handler support",
                "ext-intl": "Required for Internationalized Domain Name (IDN) support",
                "psr/log": "Required for using the Log middleware"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "7.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://sagikazarmark.hu"
                }
            ],
            "description": "Guzzle is a PHP HTTP client library",
            "homepage": "http://guzzlephp.org/",
            "keywords": [
                "client",
                "curl",
                "framework",
                "http",
                "http client",
                "psr-18",
                "psr-7",
                "rest",
                "web service"
            ],
            "support": {
                "issues": "https://github.com/guzzle/guzzle/issues",
                "source": "https://github.com/guzzle/guzzle/tree/7.3.0"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://github.com/Nyholm",
                    "type": "github"
                },
                {
                    "url": "https://github.com/alexeyshockov",
                    "type": "github"
                },
                {
                    "url": "https://github.com/gmponos",
                    "type": "github"
                }
            ],
            "time": "2021-03-23T11:33:13+00:00"
        },
        {
            "name": "guzzlehttp/promises",
            "version": "1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/promises.git",
                "reference": "8e7d04f1f6450fef59366c399cfad4b9383aa30d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/promises/zipball/8e7d04f1f6450fef59366c399cfad4b9383aa30d",
                "reference": "8e7d04f1f6450fef59366c399cfad4b9383aa30d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "symfony/phpunit-bridge": "^4.4 || ^5.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Promise\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
            "description": "Guzzle promises library",
            "keywords": [
                "promise"
            ],
            "support": {
                "issues": "https://github.com/guzzle/promises/issues",
                "source": "https://github.com/guzzle/promises/tree/1.4.1"
            },
            "time": "2021-03-07T09:25:29+00:00"
        },
        {
            "name": "guzzlehttp/psr7",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/psr7.git",
                "reference": "1dc8d9cba3897165e16d12bb13d813afb1eb3fe7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/psr7/zipball/1dc8d9cba3897165e16d12bb13d813afb1eb3fe7",
                "reference": "1dc8d9cba3897165e16d12bb13d813afb1eb3fe7",
                "shasum": ""
            },
            "require": {
                "php": "^7.2.5 || ^8.0",
                "psr/http-factory": "^1.0",
                "psr/http-message": "^1.0",
                "ralouphie/getallheaders": "^3.0"
            },
            "provide": {
                "psr/http-factory-implementation": "1.0",
                "psr/http-message-implementation": "1.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "http-interop/http-factory-tests": "^0.9",
                "phpunit/phpunit": "^8.5.8 || ^9.3.10"
            },
            "suggest": {
                "laminas/laminas-httphandlerrunner": "Emit PSR-7 responses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Psr7\\": "src/"
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
                    "name": "Tobias Schultze",
                    "homepage": "https://github.com/Tobion"
                },
                {
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://sagikazarmark.hu"
                }
            ],
            "description": "PSR-7 message implementation that also provides common utility methods",
            "keywords": [
                "http",
                "message",
                "psr-7",
                "request",
                "response",
                "stream",
                "uri",
                "url"
            ],
            "support": {
                "issues": "https://github.com/guzzle/psr7/issues",
                "source": "https://github.com/guzzle/psr7/tree/2.0.0"
            },
            "time": "2021-06-30T20:03:07+00:00"
        },
        {
            "name": "laravel/framework",
            "version": "v8.55.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/framework.git",
                "reference": "997e2aa23e9103137715018ae926c52f8a1703f2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/framework/zipball/997e2aa23e9103137715018ae926c52f8a1703f2",
                "reference": "997e2aa23e9103137715018ae926c52f8a1703f2",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.4|^2.0",
                "dragonmantank/cron-expression": "^3.0.2",
                "egulias/email-validator": "^2.1.10",
                "ext-json": "*",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "league/commonmark": "^1.3|^2.0",
                "league/flysystem": "^1.1",
                "monolog/monolog": "^2.0",
                "nesbot/carbon": "^2.31",
                "opis/closure": "^3.6",
                "php": "^7.3|^8.0",
                "psr/container": "^1.0",
                "psr/simple-cache": "^1.0",
                "ramsey/uuid": "^4.0",
                "swiftmailer/swiftmailer": "^6.0",
                "symfony/console": "^5.1.4",
                "symfony/error-handler": "^5.1.4",
                "symfony/finder": "^5.1.4",
                "symfony/http-foundation": "^5.1.4",
                "symfony/http-kernel": "^5.1.4",
                "symfony/mime": "^5.1.4",
                "symfony/process": "^5.1.4",
                "symfony/routing": "^5.1.4",
                "symfony/var-dumper": "^5.1.4",
                "tijsverkoyen/css-to-inline-styles": "^2.2.2",
                "vlucas/phpdotenv": "^5.2",
                "voku/portable-ascii": "^1.4.8"
            },
            "conflict": {
                "tightenco/collect": "<5.5.33"
            },
            "provide": {
                "psr/container-implementation": "1.0"
            },
            "replace": {
                "illuminate/auth": "self.version",
                "illuminate/broadcasting": "self.version",
                "illuminate/bus": "self.version",
                "illuminate/cache": "self.version",
                "illuminate/collections": "self.version",
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
                "illuminate/macroable": "self.version",
                "illuminate/mail": "self.version",
                "illuminate/notifications": "self.version",
                "illuminate/pagination": "self.version",
                "illuminate/pipeline": "self.version",
                "illuminate/queue": "self.version",
                "illuminate/redis": "self.version",
                "illuminate/routing": "self.version",
                "illuminate/session": "self.version",
                "illuminate/support": "self.version",
                "illuminate/testing": "self.version",
                "illuminate/translation": "self.version",
                "illuminate/validation": "self.version",
                "illuminate/view": "self.version"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^3.189.0",
                "doctrine/dbal": "^2.6|^3.0",
                "filp/whoops": "^2.8",
                "guzzlehttp/guzzle": "^6.5.5|^7.0.1",
                "league/flysystem-cached-adapter": "^1.0",
                "mockery/mockery": "^1.4.2",
                "orchestra/testbench-core": "^6.23",
                "pda/pheanstalk": "^4.0",
                "phpunit/phpunit": "^8.5.8|^9.3.3",
                "predis/predis": "^1.1.2",
                "symfony/cache": "^5.1.4"
            },
            "suggest": {
                "aws/aws-sdk-php": "Required to use the SQS queue driver, DynamoDb failed job storage and SES mail driver (^3.189.0).",
                "brianium/paratest": "Required to run tests in parallel (^6.0).",
                "doctrine/dbal": "Required to rename columns and drop SQLite columns (^2.6|^3.0).",
                "ext-ftp": "Required to use the Flysystem FTP driver.",
                "ext-gd": "Required to use Illuminate\\Http\\Testing\\FileFactory::image().",
                "ext-memcached": "Required to use the memcache cache driver.",
                "ext-pcntl": "Required to use all features of the queue worker.",
                "ext-posix": "Required to use all features of the queue worker.",
                "ext-redis": "Required to use the Redis cache and queue drivers (^4.0|^5.0).",
                "fakerphp/faker": "Required to use the eloquent factory builder (^1.9.1).",
                "filp/whoops": "Required for friendly error pages in development (^2.8).",
                "guzzlehttp/guzzle": "Required to use the HTTP Client, Mailgun mail driver and the ping methods on schedules (^6.5.5|^7.0.1).",
                "laravel/tinker": "Required to use the tinker console command (^2.0).",
                "league/flysystem-aws-s3-v3": "Required to use the Flysystem S3 driver (^1.0).",
                "league/flysystem-cached-adapter": "Required to use the Flysystem cache (^1.0).",
                "league/flysystem-sftp": "Required to use the Flysystem SFTP driver (^1.0).",
                "mockery/mockery": "Required to use mocking (^1.4.2).",
                "nyholm/psr7": "Required to use PSR-7 bridging features (^1.2).",
                "pda/pheanstalk": "Required to use the beanstalk queue driver (^4.0).",
                "phpunit/phpunit": "Required to use assertions and run tests (^8.5.8|^9.3.3).",
                "predis/predis": "Required to use the predis connector (^1.1.2).",
                "psr/http-message": "Required to allow Storage::put to accept a StreamInterface (^1.0).",
                "pusher/pusher-php-server": "Required to use the Pusher broadcast driver (^4.0|^5.0|^6.0).",
                "symfony/cache": "Required to PSR-6 cache bridge (^5.1.4).",
                "symfony/filesystem": "Required to enable support for relative symbolic links (^5.1.4).",
                "symfony/psr-http-message-bridge": "Required to use PSR-7 bridging features (^2.0).",
                "wildbit/swiftmailer-postmark": "Required to use Postmark mail driver (^3.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "8.x-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/Illuminate/Collections/helpers.php",
                    "src/Illuminate/Events/functions.php",
                    "src/Illuminate/Foundation/helpers.php",
                    "src/Illuminate/Support/helpers.php"
                ],
                "psr-4": {
                    "Illuminate\\": "src/Illuminate/",
                    "Illuminate\\Support\\": [
                        "src/Illuminate/Macroable/",
                        "src/Illuminate/Collections/"
                    ]
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
            "support": {
                "issues": "https://github.com/laravel/framework/issues",
                "source": "https://github.com/laravel/framework"
            },
            "time": "2021-08-17T14:13:34+00:00"
        },
        {
            "name": "laravel/sanctum",
            "version": "v2.11.2",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/sanctum.git",
                "reference": "b21e65cbe13896946986cb0868180cd69e1bd5d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/sanctum/zipball/b21e65cbe13896946986cb0868180cd69e1bd5d3",
                "reference": "b21e65cbe13896946986cb0868180cd69e1bd5d3",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "illuminate/contracts": "^6.9|^7.0|^8.0",
                "illuminate/database": "^6.9|^7.0|^8.0",
                "illuminate/support": "^6.9|^7.0|^8.0",
                "php": "^7.2|^8.0"
            },
            "require-dev": {
                "mockery/mockery": "^1.0",
                "orchestra/testbench": "^4.0|^5.0|^6.0",
                "phpunit/phpunit": "^8.0|^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Laravel\\Sanctum\\SanctumServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Laravel\\Sanctum\\": "src/"
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
            "description": "Laravel Sanctum provides a featherweight authentication system for SPAs and simple APIs.",
            "keywords": [
                "auth",
                "laravel",
                "sanctum"
            ],
            "support": {
                "issues": "https://github.com/laravel/sanctum/issues",
                "source": "https://github.com/laravel/sanctum"
            },
            "time": "2021-06-15T15:56:21+00:00"
        },
        {
            "name": "laravel/tinker",
            "version": "v2.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/tinker.git",
                "reference": "04ad32c1a3328081097a181875733fa51f402083"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/tinker/zipball/04ad32c1a3328081097a181875733fa51f402083",
                "reference": "04ad32c1a3328081097a181875733fa51f402083",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "^6.0|^7.0|^8.0",
                "illuminate/contracts": "^6.0|^7.0|^8.0",
                "illuminate/support": "^6.0|^7.0|^8.0",
                "php": "^7.2.5|^8.0",
                "psy/psysh": "^0.10.4",
                "symfony/var-dumper": "^4.3.4|^5.0"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.3|^1.4.2",
                "phpunit/phpunit": "^8.5.8|^9.3.3"
            },
            "suggest": {
                "illuminate/database": "The Illuminate Database package (^6.0|^7.0|^8.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
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
            "support": {
                "issues": "https://github.com/laravel/tinker/issues",
                "source": "https://github.com/laravel/tinker/tree/v2.6.1"
            },
            "time": "2021-03-02T16:53:12+00:00"
        },
        {
            "name": "league/commonmark",
            "version": "1.6.6",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/commonmark.git",
                "reference": "c4228d11e30d7493c6836d20872f9582d8ba6dcf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/commonmark/zipball/c4228d11e30d7493c6836d20872f9582d8ba6dcf",
                "reference": "c4228d11e30d7493c6836d20872f9582d8ba6dcf",
                "shasum": ""
            },
            "require": {
                "ext-mbstring": "*",
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "scrutinizer/ocular": "1.7.*"
            },
            "require-dev": {
                "cebe/markdown": "~1.0",
                "commonmark/commonmark.js": "0.29.2",
                "erusev/parsedown": "~1.0",
                "ext-json": "*",
                "github/gfm": "0.29.0",
                "michelf/php-markdown": "~1.4",
                "mikehaertl/php-shellcommand": "^1.4",
                "phpstan/phpstan": "^0.12.90",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.2",
                "scrutinizer/ocular": "^1.5",
                "symfony/finder": "^4.2"
            },
            "bin": [
                "bin/commonmark"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\CommonMark\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Colin O'Dell",
                    "email": "colinodell@gmail.com",
                    "homepage": "https://www.colinodell.com",
                    "role": "Lead Developer"
                }
            ],
            "description": "Highly-extensible PHP Markdown parser which fully supports the CommonMark spec and Github-Flavored Markdown (GFM)",
            "homepage": "https://commonmark.thephpleague.com",
            "keywords": [
                "commonmark",
                "flavored",
                "gfm",
                "github",
                "github-flavored",
                "markdown",
                "md",
                "parser"
            ],
            "support": {
                "docs": "https://commonmark.thephpleague.com/",
                "issues": "https://github.com/thephpleague/commonmark/issues",
                "rss": "https://github.com/thephpleague/commonmark/releases.atom",
                "source": "https://github.com/thephpleague/commonmark"
            },
            "funding": [
                {
                    "url": "https://enjoy.gitstore.app/repositories/thephpleague/commonmark",
                    "type": "custom"
                },
                {
                    "url": "https://www.colinodell.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://www.paypal.me/colinpodell/10.00",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/colinodell",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/colinodell",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/league/commonmark",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-17T17:13:23+00:00"
        },
        {
            "name": "league/flysystem",
            "version": "1.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/flysystem.git",
                "reference": "18634df356bfd4119fe3d6156bdb990c414c14ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/flysystem/zipball/18634df356bfd4119fe3d6156bdb990c414c14ea",
                "reference": "18634df356bfd4119fe3d6156bdb990c414c14ea",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "league/mime-type-detection": "^1.3",
                "php": "^7.2.5 || ^8.0"
            },
            "conflict": {
                "league/flysystem-sftp": "<1.0.6"
            },
            "require-dev": {
                "phpspec/prophecy": "^1.11.1",
                "phpunit/phpunit": "^8.5.8"
            },
            "suggest": {
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
            "support": {
                "issues": "https://github.com/thephpleague/flysystem/issues",
                "source": "https://github.com/thephpleague/flysystem/tree/1.1.5"
            },
            "funding": [
                {
                    "url": "https://offset.earth/frankdejonge",
                    "type": "other"
                }
            ],
            "time": "2021-08-17T13:49:42+00:00"
        },
        {
            "name": "league/mime-type-detection",
            "version": "1.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/mime-type-detection.git",
                "reference": "3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/mime-type-detection/zipball/3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3",
                "reference": "3b9dff8aaf7323590c1d2e443db701eb1f9aa0d3",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.18",
                "phpstan/phpstan": "^0.12.68",
                "phpunit/phpunit": "^8.5.8 || ^9.3"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\MimeTypeDetection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Frank de Jonge",
                    "email": "info@frankdejonge.nl"
                }
            ],
            "description": "Mime-type detection for Flysystem",
            "support": {
                "issues": "https://github.com/thephpleague/mime-type-detection/issues",
                "source": "https://github.com/thephpleague/mime-type-detection/tree/1.7.0"
            },
            "funding": [
                {
                    "url": "https://github.com/frankdejonge",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/league/flysystem",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-18T20:58:21+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "2.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "71312564759a7db5b789296369c1a264efc43aad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/71312564759a7db5b789296369c1a264efc43aad",
                "reference": "71312564759a7db5b789296369c1a264efc43aad",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2",
                "psr/log": "^1.0.1"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "elasticsearch/elasticsearch": "^7",
                "graylog2/gelf-php": "^1.4.2",
                "mongodb/mongodb": "^1.8",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpspec/prophecy": "^1.6.1",
                "phpstan/phpstan": "^0.12.91",
                "phpunit/phpunit": "^8.5",
                "predis/predis": "^1.1",
                "rollbar/rollbar": "^1.3",
                "ruflin/elastica": ">=0.90 <7.0.1",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "elasticsearch/elasticsearch": "Allow sending log messages to an Elasticsearch server via official client",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mbstring": "Allow to work properly with unicode symbols",
                "ext-mongodb": "Allow sending log messages to a MongoDB server (via driver)",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server (via library)",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.x-dev"
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
                    "homepage": "https://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "https://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "support": {
                "issues": "https://github.com/Seldaek/monolog/issues",
                "source": "https://github.com/Seldaek/monolog/tree/2.3.2"
            },
            "funding": [
                {
                    "url": "https://github.com/Seldaek",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/monolog/monolog",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T07:42:52+00:00"
        },
        {
            "name": "nesbot/carbon",
            "version": "2.52.0",
            "source": {
                "type": "git",
                "url": "https://github.com/briannesbitt/Carbon.git",
                "reference": "369c0e2737c56a0f39c946dd261855255a6fccbe"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/briannesbitt/Carbon/zipball/369c0e2737c56a0f39c946dd261855255a6fccbe",
                "reference": "369c0e2737c56a0f39c946dd261855255a6fccbe",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.1.8 || ^8.0",
                "symfony/polyfill-mbstring": "^1.0",
                "symfony/polyfill-php80": "^1.16",
                "symfony/translation": "^3.4 || ^4.0 || ^5.0"
            },
            "require-dev": {
                "doctrine/orm": "^2.7",
                "friendsofphp/php-cs-fixer": "^2.14 || ^3.0",
                "kylekatarnls/multi-tester": "^2.0",
                "phpmd/phpmd": "^2.9",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12.54",
                "phpunit/phpunit": "^7.5.20 || ^8.5.14",
                "squizlabs/php_codesniffer": "^3.4"
            },
            "bin": [
                "bin/carbon"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-3.x": "3.x-dev",
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Carbon\\Laravel\\ServiceProvider"
                    ]
                },
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                }
            },
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
                    "homepage": "https://markido.com"
                },
                {
                    "name": "kylekatarnls",
                    "homepage": "https://github.com/kylekatarnls"
                }
            ],
            "description": "An API extension for DateTime that supports 281 different languages.",
            "homepage": "https://carbon.nesbot.com",
            "keywords": [
                "date",
                "datetime",
                "time"
            ],
            "support": {
                "issues": "https://github.com/briannesbitt/Carbon/issues",
                "source": "https://github.com/briannesbitt/Carbon"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/Carbon",
                    "type": "open_collective"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/nesbot/carbon",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-14T19:10:52+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.12.0",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "6608f01670c3cc5079e18c1dab1104e002579143"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/6608f01670c3cc5079e18c1dab1104e002579143",
                "reference": "6608f01670c3cc5079e18c1dab1104e002579143",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "ircmaxell/php-yacc": "^0.0.7",
                "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0 || ^9.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.9-dev"
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
            "support": {
                "issues": "https://github.com/nikic/PHP-Parser/issues",
                "source": "https://github.com/nikic/PHP-Parser/tree/v4.12.0"
            },
            "time": "2021-07-21T10:44:31+00:00"
        },
        {
            "name": "opis/closure",
            "version": "3.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/opis/closure.git",
                "reference": "06e2ebd25f2869e54a306dda991f7db58066f7f6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/opis/closure/zipball/06e2ebd25f2869e54a306dda991f7db58066f7f6",
                "reference": "06e2ebd25f2869e54a306dda991f7db58066f7f6",
                "shasum": ""
            },
            "require": {
                "php": "^5.4 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "jeremeamia/superclosure": "^2.0",
                "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0 || ^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.6.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Opis\\Closure\\": "src/"
                },
                "files": [
                    "functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marius Sarca",
                    "email": "marius.sarca@gmail.com"
                },
                {
                    "name": "Sorin Sarca",
                    "email": "sarca_sorin@hotmail.com"
                }
            ],
            "description": "A library that can be used to serialize closures (anonymous functions) and arbitrary objects.",
            "homepage": "https://opis.io/closure",
            "keywords": [
                "anonymous functions",
                "closure",
                "function",
                "serializable",
                "serialization",
                "serialize"
            ],
            "support": {
                "issues": "https://github.com/opis/closure/issues",
                "source": "https://github.com/opis/closure/tree/3.6.2"
            },
            "time": "2021-04-09T13:42:10+00:00"
        },
        {
            "name": "phpoption/phpoption",
            "version": "1.7.5",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/php-option.git",
                "reference": "994ecccd8f3283ecf5ac33254543eb0ac946d525"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/php-option/zipball/994ecccd8f3283ecf5ac33254543eb0ac946d525",
                "reference": "994ecccd8f3283ecf5ac33254543eb0ac946d525",
                "shasum": ""
            },
            "require": {
                "php": "^5.5.9 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "phpunit/phpunit": "^4.8.35 || ^5.7.27 || ^6.5.6 || ^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.7-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpOption\\": "src/PhpOption/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com"
                }
            ],
            "description": "Option Type for PHP",
            "keywords": [
                "language",
                "option",
                "php",
                "type"
            ],
            "support": {
                "issues": "https://github.com/schmittjoh/php-option/issues",
                "source": "https://github.com/schmittjoh/php-option/tree/1.7.5"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpoption/phpoption",
                    "type": "tidelift"
                }
            ],
            "time": "2020-07-20T17:29:33+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/8622567409010282b7aeebe4bb841fe98b58dcaf",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
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
                    "homepage": "https://www.php-fig.org/"
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
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/1.1.1"
            },
            "time": "2021-03-05T17:36:06+00:00"
        },
        {
            "name": "psr/event-dispatcher",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/event-dispatcher.git",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/event-dispatcher/zipball/dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\EventDispatcher\\": "src/"
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
            "description": "Standard interfaces for event handling.",
            "keywords": [
                "events",
                "psr",
                "psr-14"
            ],
            "support": {
                "issues": "https://github.com/php-fig/event-dispatcher/issues",
                "source": "https://github.com/php-fig/event-dispatcher/tree/1.0.0"
            },
            "time": "2019-01-08T18:20:26+00:00"
        },
        {
            "name": "psr/http-client",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-client.git",
                "reference": "2dfb5f6c5eff0e91e20e913f8c5452ed95b86621"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-client/zipball/2dfb5f6c5eff0e91e20e913f8c5452ed95b86621",
                "reference": "2dfb5f6c5eff0e91e20e913f8c5452ed95b86621",
                "shasum": ""
            },
            "require": {
                "php": "^7.0 || ^8.0",
                "psr/http-message": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Client\\": "src/"
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
            "description": "Common interface for HTTP clients",
            "homepage": "https://github.com/php-fig/http-client",
            "keywords": [
                "http",
                "http-client",
                "psr",
                "psr-18"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-client/tree/master"
            },
            "time": "2020-06-29T06:28:15+00:00"
        },
        {
            "name": "psr/http-factory",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-factory.git",
                "reference": "12ac7fcd07e5b077433f5f2bee95b3a771bf61be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-factory/zipball/12ac7fcd07e5b077433f5f2bee95b3a771bf61be",
                "reference": "12ac7fcd07e5b077433f5f2bee95b3a771bf61be",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0.0",
                "psr/http-message": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Message\\": "src/"
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
            "description": "Common interfaces for PSR-7 HTTP message factories",
            "keywords": [
                "factory",
                "http",
                "message",
                "psr",
                "psr-17",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-factory/tree/master"
            },
            "time": "2019-04-30T12:38:16+00:00"
        },
        {
            "name": "psr/http-message",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-message.git",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-message/zipball/f6561bf28d520154e4b0ec72be95418abe6d9363",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363",
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
                    "Psr\\Http\\Message\\": "src/"
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
            "description": "Common interface for HTTP messages",
            "homepage": "https://github.com/php-fig/http-message",
            "keywords": [
                "http",
                "http-message",
                "psr",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-message/tree/master"
            },
            "time": "2016-08-06T14:39:51+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "d49695b909c3b7628b6289db5479a1c204601f11"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/d49695b909c3b7628b6289db5479a1c204601f11",
                "reference": "d49695b909c3b7628b6289db5479a1c204601f11",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
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
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "support": {
                "source": "https://github.com/php-fig/log/tree/1.1.4"
            },
            "time": "2021-05-03T11:20:27+00:00"
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
            "support": {
                "source": "https://github.com/php-fig/simple-cache/tree/master"
            },
            "time": "2017-10-23T01:57:42+00:00"
        },
        {
            "name": "psy/psysh",
            "version": "v0.10.8",
            "source": {
                "type": "git",
                "url": "https://github.com/bobthecow/psysh.git",
                "reference": "e4573f47750dd6c92dca5aee543fa77513cbd8d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/bobthecow/psysh/zipball/e4573f47750dd6c92dca5aee543fa77513cbd8d3",
                "reference": "e4573f47750dd6c92dca5aee543fa77513cbd8d3",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-tokenizer": "*",
                "nikic/php-parser": "~4.0|~3.0|~2.0|~1.3",
                "php": "^8.0 || ^7.0 || ^5.5.9",
                "symfony/console": "~5.0|~4.0|~3.0|^2.4.2|~2.3.10",
                "symfony/var-dumper": "~5.0|~4.0|~3.0|~2.7"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.2",
                "hoa/console": "3.17.*"
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
                    "dev-main": "0.10.x-dev"
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
            "support": {
                "issues": "https://github.com/bobthecow/psysh/issues",
                "source": "https://github.com/bobthecow/psysh/tree/v0.10.8"
            },
            "time": "2021-04-10T16:23:39+00:00"
        },
        {
            "name": "ralouphie/getallheaders",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/ralouphie/getallheaders.git",
                "reference": "120b605dfeb996808c31b6477290a714d356e822"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ralouphie/getallheaders/zipball/120b605dfeb996808c31b6477290a714d356e822",
                "reference": "120b605dfeb996808c31b6477290a714d356e822",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.1",
                "phpunit/phpunit": "^5 || ^6.5"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/getallheaders.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ralph Khattar",
                    "email": "ralph.khattar@gmail.com"
                }
            ],
            "description": "A polyfill for getallheaders.",
            "support": {
                "issues": "https://github.com/ralouphie/getallheaders/issues",
                "source": "https://github.com/ralouphie/getallheaders/tree/develop"
            },
            "time": "2019-03-08T08:55:37+00:00"
        },
        {
            "name": "ramsey/collection",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/collection.git",
                "reference": "eaca1dc1054ddd10cbd83c1461907bee6fb528fa"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/collection/zipball/eaca1dc1054ddd10cbd83c1461907bee6fb528fa",
                "reference": "eaca1dc1054ddd10cbd83c1461907bee6fb528fa",
                "shasum": ""
            },
            "require": {
                "php": "^7.3 || ^8",
                "symfony/polyfill-php81": "^1.23"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
                "ergebnis/composer-normalize": "^2.6",
                "fakerphp/faker": "^1.5",
                "hamcrest/hamcrest-php": "^2",
                "jangregor/phpstan-prophecy": "^0.8",
                "mockery/mockery": "^1.3",
                "phpspec/prophecy-phpunit": "^2.0",
                "phpstan/extension-installer": "^1",
                "phpstan/phpstan": "^0.12.32",
                "phpstan/phpstan-mockery": "^0.12.5",
                "phpstan/phpstan-phpunit": "^0.12.11",
                "phpunit/phpunit": "^8.5 || ^9",
                "psy/psysh": "^0.10.4",
                "slevomat/coding-standard": "^6.3",
                "squizlabs/php_codesniffer": "^3.5",
                "vimeo/psalm": "^4.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Ramsey\\Collection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "A PHP library for representing and manipulating collections.",
            "keywords": [
                "array",
                "collection",
                "hash",
                "map",
                "queue",
                "set"
            ],
            "support": {
                "issues": "https://github.com/ramsey/collection/issues",
                "source": "https://github.com/ramsey/collection/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/collection",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-06T03:41:06+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "4.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "fe665a03df4f056aa65af552a96e1976df8c8dae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/fe665a03df4f056aa65af552a96e1976df8c8dae",
                "reference": "fe665a03df4f056aa65af552a96e1976df8c8dae",
                "shasum": ""
            },
            "require": {
                "brick/math": "^0.8 || ^0.9",
                "ext-json": "*",
                "php": "^7.2 || ^8",
                "ramsey/collection": "^1.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.10",
                "captainhook/plugin-composer": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
                "doctrine/annotations": "^1.8",
                "ergebnis/composer-normalize": "^2.15",
                "mockery/mockery": "^1.3",
                "moontoast/math": "^1.1",
                "paragonie/random-lib": "^2",
                "php-mock/php-mock": "^2.2",
                "php-mock/php-mock-mockery": "^1.3",
                "php-parallel-lint/php-parallel-lint": "^1.1",
                "phpbench/phpbench": "^1.0",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-mockery": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^8.5 || ^9",
                "slevomat/coding-standard": "^7.0",
                "squizlabs/php_codesniffer": "^3.5",
                "vimeo/psalm": "^4.9"
            },
            "suggest": {
                "ext-bcmath": "Enables faster math with arbitrary-precision integers using BCMath.",
                "ext-ctype": "Enables faster processing of character classification using ctype functions.",
                "ext-gmp": "Enables faster math with arbitrary-precision integers using GMP.",
                "ext-uuid": "Enables the use of PeclUuidTimeGenerator and PeclUuidRandomGenerator.",
                "paragonie/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.x-dev"
                },
                "captainhook": {
                    "force-install": true
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                },
                "files": [
                    "src/functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A PHP library for generating and working with universally unique identifiers (UUIDs).",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "support": {
                "issues": "https://github.com/ramsey/uuid/issues",
                "source": "https://github.com/ramsey/uuid/tree/4.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/uuid",
                    "type": "tidelift"
                }
            ],
            "time": "2021-08-11T01:06:55+00:00"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "v6.2.7",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "15f7faf8508e04471f666633addacf54c0ab5933"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/15f7faf8508e04471f666633addacf54c0ab5933",
                "reference": "15f7faf8508e04471f666633addacf54c0ab5933",
                "shasum": ""
            },
            "require": {
                "egulias/email-validator": "^2.0|^3.1",
                "php": ">=7.0.0",
                "symfony/polyfill-iconv": "^1.0",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^1.0",
                "symfony/phpunit-bridge": "^4.4|^5.0"
            },
            "suggest": {
                "ext-intl": "Needed to support internationalized email addresses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.2-dev"
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
            "support": {
                "issues": "https://github.com/swiftmailer/swiftmailer/issues",
                "source": "https://github.com/swiftmailer/swiftmailer/tree/v6.2.7"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/swiftmailer/swiftmailer",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-09T12:30:35+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "51b71afd6d2dc8f5063199357b9880cea8d8bfe2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/51b71afd6d2dc8f5063199357b9880cea8d8bfe2",
                "reference": "51b71afd6d2dc8f5063199357b9880cea8d8bfe2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/polyfill-php80": "^1.16",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/string": "^5.1"
            },
            "conflict": {
                "psr/log": ">=3",
                "symfony/dependency-injection": "<4.4",
                "symfony/dotenv": "<5.1",
                "symfony/event-dispatcher": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/process": "<4.4"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0"
            },
            "require-dev": {
                "psr/log": "^1|^2",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
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
            "description": "Eases the creation of beautiful and testable command line interfaces",
            "homepage": "https://symfony.com",
            "keywords": [
                "cli",
                "command line",
                "console",
                "terminal"
            ],
            "support": {
                "source": "https://github.com/symfony/console/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T19:10:22+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "7fb120adc7f600a59027775b224c13a33530dd90"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/7fb120adc7f600a59027775b224c13a33530dd90",
                "reference": "7fb120adc7f600a59027775b224c13a33530dd90",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Converts CSS selectors to XPath expressions",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/css-selector/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-21T12:38:00+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
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
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "281f6c4660bcf5844bb0346fe3a4664722fe4c73"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/281f6c4660bcf5844bb0346fe3a4664722fe4c73",
                "reference": "281f6c4660bcf5844bb0346fe3a4664722fe4c73",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1|^2|^3",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.1",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\ErrorHandler\\": ""
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
            "description": "Provides tools to manage errors and ease debugging PHP code",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/error-handler/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "f2fd2208157553874560f3645d4594303058c4bd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/f2fd2208157553874560f3645d4594303058c4bd",
                "reference": "f2fd2208157553874560f3645d4594303058c4bd",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/event-dispatcher-contracts": "^2",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "2.0"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/stopwatch": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
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
            "description": "Provides tools that allow your application components to communicate with each other by dispatching events and listening to them",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/event-dispatcher/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/event-dispatcher": "^1"
            },
            "suggest": {
                "symfony/event-dispatcher-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
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
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "17f50e06018baec41551a71a15731287dbaab186"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/17f50e06018baec41551a71a15731287dbaab186",
                "reference": "17f50e06018baec41551a71a15731287dbaab186",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
            "description": "Finds files and directories via an intuitive fluent interface",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/finder/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:54:19+00:00"
        },
        {
            "name": "symfony/http-client-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-client-contracts.git",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-client-contracts/zipball/7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/http-client-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\HttpClient\\": ""
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
            "description": "Generic abstractions related to HTTP clients",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/http-client-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-11T23:07:08+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "a8388f7b7054a7401997008ce9cd8c6b0ab7ac75"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/a8388f7b7054a7401997008ce9cd8c6b0ab7ac75",
                "reference": "a8388f7b7054a7401997008ce9cd8c6b0ab7ac75",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.1",
                "symfony/polyfill-php80": "^1.16"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/mime": "To use the file extension guesser"
            },
            "type": "library",
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
            "description": "Defines an object-oriented layer for the HTTP specification",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-foundation/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T17:08:17+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "60030f209018356b3b553b9dbd84ad2071c1b7e0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/60030f209018356b3b553b9dbd84ad2071c1b7e0",
                "reference": "60030f209018356b3b553b9dbd84ad2071c1b7e0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1|^2",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/event-dispatcher": "^5.0",
                "symfony/http-client-contracts": "^1.1|^2",
                "symfony/http-foundation": "^5.3",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-php73": "^1.9",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "symfony/browser-kit": "<4.4",
                "symfony/cache": "<5.0",
                "symfony/config": "<5.0",
                "symfony/console": "<4.4",
                "symfony/dependency-injection": "<5.3",
                "symfony/doctrine-bridge": "<5.0",
                "symfony/form": "<5.0",
                "symfony/http-client": "<5.0",
                "symfony/mailer": "<5.0",
                "symfony/messenger": "<5.0",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<5.0",
                "symfony/validator": "<5.0",
                "twig/twig": "<2.13"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/config": "^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dependency-injection": "^5.3",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "twig/twig": "^2.13|^3.0.4"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": ""
            },
            "type": "library",
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
            "description": "Provides a structured process for converting a Request into a Response",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-kernel/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-29T07:06:27+00:00"
        },
        {
            "name": "symfony/mime",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/mime.git",
                "reference": "633e4e8afe9e529e5599d71238849a4218dd497b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/mime/zipball/633e4e8afe9e529e5599d71238849a4218dd497b",
                "reference": "633e4e8afe9e529e5599d71238849a4218dd497b",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "egulias/email-validator": "~3.0.0",
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "symfony/mailer": "<4.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10|^3.1",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/property-access": "^4.4|^5.1",
                "symfony/property-info": "^4.4|^5.1",
                "symfony/serializer": "^5.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Mime\\": ""
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
            "description": "Allows manipulating MIME messages",
            "homepage": "https://symfony.com",
            "keywords": [
                "mime",
                "mime-type"
            ],
            "support": {
                "source": "https://github.com/symfony/mime/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-21T12:40:44+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "46cd95797e9df938fdd2b03693b5fca5e64b01ce"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/46cd95797e9df938fdd2b03693b5fca5e64b01ce",
                "reference": "46cd95797e9df938fdd2b03693b5fca5e64b01ce",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-ctype/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-iconv",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-iconv.git",
                "reference": "63b5bb7db83e5673936d6e3b8b3e022ff6474933"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-iconv/zipball/63b5bb7db83e5673936d6e3b8b3e022ff6474933",
                "reference": "63b5bb7db83e5673936d6e3b8b3e022ff6474933",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-iconv": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Iconv\\": ""
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
            "description": "Symfony polyfill for the Iconv extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "iconv",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-iconv/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:27:20+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "16880ba9c5ebe3642d1995ab866db29270b36535"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/16880ba9c5ebe3642d1995ab866db29270b36535",
                "reference": "16880ba9c5ebe3642d1995ab866db29270b36535",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Grapheme\\": ""
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
            "description": "Symfony polyfill for intl's grapheme_* functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "grapheme",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T12:26:48+00:00"
        },
        {
            "name": "symfony/polyfill-intl-idn",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-idn.git",
                "reference": "65bd267525e82759e7d8c4e8ceea44f398838e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-idn/zipball/65bd267525e82759e7d8c4e8ceea44f398838e65",
                "reference": "65bd267525e82759e7d8c4e8ceea44f398838e65",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "symfony/polyfill-intl-normalizer": "^1.10",
                "symfony/polyfill-php72": "^1.10"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Idn\\": ""
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
                    "name": "Laurent Bassin",
                    "email": "laurent@bassin.info"
                },
                {
                    "name": "Trevor Rowbotham",
                    "email": "trevor.rowbotham@pm.me"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's idn_to_ascii and idn_to_utf8 functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "idn",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-idn/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:27:20+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "8590a5f561694770bdcd3f9b5c69dde6945028e8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/8590a5f561694770bdcd3f9b5c69dde6945028e8",
                "reference": "8590a5f561694770bdcd3f9b5c69dde6945028e8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "9174a3d80210dca8daa7f31fec659150bbeabfc6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/9174a3d80210dca8daa7f31fec659150bbeabfc6",
                "reference": "9174a3d80210dca8daa7f31fec659150bbeabfc6",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T12:26:48+00:00"
        },
        {
            "name": "symfony/polyfill-php72",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php72.git",
                "reference": "9a142215a36a3888e30d0a9eeea9766764e96976"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php72/zipball/9a142215a36a3888e30d0a9eeea9766764e96976",
                "reference": "9a142215a36a3888e30d0a9eeea9766764e96976",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
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
            "support": {
                "source": "https://github.com/symfony/polyfill-php72/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-27T09:17:38+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "fba8933c384d6476ab14fb7b8526e5287ca7e010"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/fba8933c384d6476ab14fb7b8526e5287ca7e010",
                "reference": "fba8933c384d6476ab14fb7b8526e5287ca7e010",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php73/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-19T12:13:01+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "1100343ed1a92e3a38f9ae122fc0eb21602547be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/1100343ed1a92e3a38f9ae122fc0eb21602547be",
                "reference": "1100343ed1a92e3a38f9ae122fc0eb21602547be",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.23.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-28T13:41:28+00:00"
        },
        {
            "name": "symfony/polyfill-php81",
            "version": "v1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php81.git",
                "reference": "e66119f3de95efc359483f810c4c3e6436279436"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php81/zipball/e66119f3de95efc359483f810c4c3e6436279436",
                "reference": "e66119f3de95efc359483f810c4c3e6436279436",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.23-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php81\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
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
            "description": "Symfony polyfill backporting some PHP 8.1+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php81/tree/v1.23.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-05-21T13:25:03+00:00"
        },
        {
            "name": "symfony/process",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/process.git",
                "reference": "d16634ee55b895bd85ec714dadc58e4428ecf030"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/process/zipball/d16634ee55b895bd85ec714dadc58e4428ecf030",
                "reference": "d16634ee55b895bd85ec714dadc58e4428ecf030",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.16"
            },
            "type": "library",
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
            "description": "Executes commands in sub-processes",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/process/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:54:19+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "0a35d2f57d73c46ab6d042ced783b81d09a624c4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/0a35d2f57d73c46ab6d042ced783b81d09a624c4",
                "reference": "0a35d2f57d73c46ab6d042ced783b81d09a624c4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "doctrine/annotations": "<1.12",
                "symfony/config": "<5.3",
                "symfony/dependency-injection": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "^1.12",
                "psr/log": "^1|^2|^3",
                "symfony/config": "^5.3",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
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
            "description": "Maps an HTTP request to a set of configuration variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "support": {
                "source": "https://github.com/symfony/routing/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-23T15:55:36+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.1"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
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
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-01T10:43:52+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v5.3.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1",
                "reference": "bd53358e3eccec6a670b5f33ab680d8dbe1d4ae1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.0",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "~1.15"
            },
            "require-dev": {
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\String\\": ""
                },
                "files": [
                    "Resources/functions.php"
                ],
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
            "description": "Provides an object-oriented API to strings and deals with bytes, UTF-8 code points and grapheme clusters in a unified way",
            "homepage": "https://symfony.com",
            "keywords": [
                "grapheme",
                "i18n",
                "string",
                "unicode",
                "utf-8",
                "utf8"
            ],
            "support": {
                "source": "https://github.com/symfony/string/tree/v5.3.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-06-27T11:44:38+00:00"
        },
        {
            "name": "symfony/translation",
            "version": "v5.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "d89ad7292932c2699cbe4af98d72c5c6bbc504c1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/d89ad7292932c2699cbe4af98d72c5c6bbc504c1",
                "reference": "d89ad7292932c2699cbe4af98d72c5c6bbc504c1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.16",
                "symfony/translation-contracts": "^2.3"
            },
            "conflict": {
                "symfony/config": "<4.4",
                "symfony/dependency-injection": "<5.0",
                "symfony/http-kernel": "<5.0",
                "symfony/twig-bundle": "<5.0",
                "symfony/yaml": "<4.4"
            },
            "provide": {
                "symfony/translation-implementation": "2.3"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^4.4|^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/dependency-injection": "^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/http-kernel": "^5.0",
                "symfony/intl": "^4.4|^5.0",
                "symfony/polyfill-intl-icu": "^1.21",
                "symfony/service-contracts": "^1.1.2|^2",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log-implementation": "To use logging capability in translator",
                "symfony/config": "",
                "symfony/yaml": ""
            },
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions.php"
                ],
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
            "description": "Provides tools to internationalize your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/translation/tree/v5.3.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-25T09:39:16+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "95c812666f3e91db75385749fe219c5e494c7f95"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/95c812666f3e91db75385749fe219c5e494c7f95",
                "reference": "95c812666f3e91db75385749fe219c5e494c7f95",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/translation-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Translation\\": ""
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
            "description": "Generic abstractions related to translation",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/translation-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v5.3.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0",
                "reference": "3dd8ddd1e260e58ecc61bb78da3b6584b3bfcba0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "twig/twig": "^2.13|^3.0.4"
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
            "description": "Provides mechanisms for walking through any arbitrary PHP variable",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/v5.3.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-07-27T01:56:02+00:00"
        },
        {
            "name": "tijsverkoyen/css-to-inline-styles",
            "version": "2.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/tijsverkoyen/CssToInlineStyles.git",
                "reference": "b43b05cf43c1b6d849478965062b6ef73e223bb5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/tijsverkoyen/CssToInlineStyles/zipball/b43b05cf43c1b6d849478965062b6ef73e223bb5",
                "reference": "b43b05cf43c1b6d849478965062b6ef73e223bb5",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "php": "^5.5 || ^7.0 || ^8.0",
                "symfony/css-selector": "^2.7 || ^3.0 || ^4.0 || ^5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0 || ^7.5"
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
            "support": {
                "issues": "https://github.com/tijsverkoyen/CssToInlineStyles/issues",
                "source": "https://github.com/tijsverkoyen/CssToInlineStyles/tree/2.2.3"
            },
            "time": "2020-07-13T06:12:54+00:00"
        },
        {
            "name": "vlucas/phpdotenv",
            "version": "v5.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/vlucas/phpdotenv.git",
                "reference": "b3eac5c7ac896e52deab4a99068e3f4ab12d9e56"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vlucas/phpdotenv/zipball/b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
                "reference": "b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
                "shasum": ""
            },
            "require": {
                "ext-pcre": "*",
                "graham-campbell/result-type": "^1.0.1",
                "php": "^7.1.3 || ^8.0",
                "phpoption/phpoption": "^1.7.4",
                "symfony/polyfill-ctype": "^1.17",
                "symfony/polyfill-mbstring": "^1.17",
                "symfony/polyfill-php80": "^1.17"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-filter": "*",
                "phpunit/phpunit": "^7.5.20 || ^8.5.14 || ^9.5.1"
            },
            "suggest": {
                "ext-filter": "Required to use the boolean validator."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.3-dev"
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
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com",
                    "homepage": "https://gjcampbell.co.uk/"
                },
                {
                    "name": "Vance Lucas",
                    "email": "vance@vancelucas.com",
                    "homepage": "https://vancelucas.com/"
                }
            ],
            "description": "Loads environment variables from `.env` to `getenv()`, `$_ENV` and `$_SERVER` automagically.",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "support": {
                "issues": "https://github.com/vlucas/phpdotenv/issues",
                "source": "https://github.com/vlucas/phpdotenv/tree/v5.3.0"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/vlucas/phpdotenv",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-20T15:23:13+00:00"
        },
        {
            "name": "voku/portable-ascii",
            "version": "1.5.6",
            "source": {
                "type": "git",
                "url": "https://github.com/voku/portable-ascii.git",
                "reference": "80953678b19901e5165c56752d087fc11526017c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/voku/portable-ascii/zipball/80953678b19901e5165c56752d087fc11526017c",
                "reference": "80953678b19901e5165c56752d087fc11526017c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~6.0 || ~7.0 || ~9.0"
            },
            "suggest": {
                "ext-intl": "Use Intl for transliterator_transliterate() support"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "voku\\": "src/voku/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Lars Moelleken",
                    "homepage": "http://www.moelleken.org/"
                }
            ],
            "description": "Portable ASCII library - performance optimized (ascii) string functions for php.",
            "homepage": "https://github.com/voku/portable-ascii",
            "keywords": [
                "ascii",
                "clean",
                "php"
            ],
            "support": {
                "issues": "https://github.com/voku/portable-ascii/issues",
                "source": "https://github.com/voku/portable-ascii/tree/1.5.6"
            },
            "funding": [
                {
                    "url": "https://www.paypal.me/moelleken",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/voku",
                    "type": "github"
                },
                {
                    "url": "https://opencollective.com/portable-ascii",
                    "type": "open_collective"
                },
                {
                    "url": "https://www.patreon.com/voku",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/voku/portable-ascii",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-12T00:07:28+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozarts/assert.git",
                "reference": "6964c76c7804814a842473e0c8fd15bab0f18e25"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozarts/assert/zipball/6964c76c7804814a842473e0c8fd15bab0f18e25",
                "reference": "6964c76c7804814a842473e0c8fd15bab0f18e25",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "phpstan/phpstan": "<0.12.20",
                "vimeo/psalm": "<4.6.1 || 4.6.2"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5.13"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.10-dev"
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
            "support": {
                "issues": "https://github.com/webmozarts/assert/issues",
                "source": "https://github.com/webmozarts/assert/tree/1.10.0"
            },
            "time": "2021-03-09T10:59:23+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "doctrine/instantiator",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "reference": "d56bf6102915de5702778fe20f2de3b2fe570b5b",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^8.0",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpbench/phpbench": "^0.13 || 1.0.0-alpha2",
                "phpstan/phpstan": "^0.12",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "type": "library",
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
                    "homepage": "https://ocramius.github.io/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://www.doctrine-project.org/projects/instantiator.html",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "support": {
                "issues": "https://github.com/doctrine/instantiator/issues",
                "source": "https://github.com/doctrine/instantiator/tree/1.4.0"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finstantiator",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-10T18:47:58+00:00"
        },
        {
            "name": "facade/flare-client-php",
            "version": "1.8.1",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/flare-client-php.git",
                "reference": "47b639dc02bcfdfc4ebb83de703856fa01e35f5f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/flare-client-php/zipball/47b639dc02bcfdfc4ebb83de703856fa01e35f5f",
                "reference": "47b639dc02bcfdfc4ebb83de703856fa01e35f5f",
                "shasum": ""
            },
            "require": {
                "facade/ignition-contracts": "~1.0",
                "illuminate/pipeline": "^5.5|^6.0|^7.0|^8.0",
                "php": "^7.1|^8.0",
                "symfony/http-foundation": "^3.3|^4.1|^5.0",
                "symfony/mime": "^3.4|^4.0|^5.1",
                "symfony/var-dumper": "^3.4|^4.0|^5.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.14",
                "phpunit/phpunit": "^7.5.16",
                "spatie/phpunit-snapshot-assertions": "^2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Facade\\FlareClient\\": "src"
                },
                "files": [
                    "src/helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Send PHP errors to Flare",
            "homepage": "https://github.com/facade/flare-client-php",
            "keywords": [
                "exception",
                "facade",
                "flare",
                "reporting"
            ],
            "support": {
                "issues": "https://github.com/facade/flare-client-php/issues",
                "source": "https://github.com/facade/flare-client-php/tree/1.8.1"
            },
            "funding": [
                {
                    "url": "https://github.com/spatie",
                    "type": "github"
                }
            ],
            "time": "2021-05-31T19:23:29+00:00"
        },
        {
            "name": "facade/ignition",
            "version": "2.11.4",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/ignition.git",
                "reference": "1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/ignition/zipball/1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2",
                "reference": "1b8d83c5dac7c5ee8429daf284ce3f19b1d17ea2",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-mbstring": "*",
                "facade/flare-client-php": "^1.6",
                "facade/ignition-contracts": "^1.0.2",
                "illuminate/support": "^7.0|^8.0",
                "monolog/monolog": "^2.0",
                "php": "^7.2.5|^8.0",
                "symfony/console": "^5.0",
                "symfony/var-dumper": "^5.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.14",
                "mockery/mockery": "^1.3",
                "orchestra/testbench": "^5.0|^6.0",
                "psalm/plugin-laravel": "^1.2"
            },
            "suggest": {
                "laravel/telescope": "^3.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Facade\\Ignition\\IgnitionServiceProvider"
                    ],
                    "aliases": {
                        "Flare": "Facade\\Ignition\\Facades\\Flare"
                    }
                }
            },
            "autoload": {
                "psr-4": {
                    "Facade\\Ignition\\": "src"
                },
                "files": [
                    "src/helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A beautiful error page for Laravel applications.",
            "homepage": "https://github.com/facade/ignition",
            "keywords": [
                "error",
                "flare",
                "laravel",
                "page"
            ],
            "support": {
                "docs": "https://flareapp.io/docs/ignition-for-laravel/introduction",
                "forum": "https://twitter.com/flareappio",
                "issues": "https://github.com/facade/ignition/issues",
                "source": "https://github.com/facade/ignition"
            },
            "time": "2021-08-17T11:45:33+00:00"
        },
        {
            "name": "facade/ignition-contracts",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/facade/ignition-contracts.git",
                "reference": "3c921a1cdba35b68a7f0ccffc6dffc1995b18267"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/facade/ignition-contracts/zipball/3c921a1cdba35b68a7f0ccffc6dffc1995b18267",
                "reference": "3c921a1cdba35b68a7f0ccffc6dffc1995b18267",
                "shasum": ""
            },
            "require": {
                "php": "^7.3|^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^v2.15.8",
                "phpunit/phpunit": "^9.3.11",
                "vimeo/psalm": "^3.17.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Facade\\IgnitionContracts\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Freek Van der Herten",
                    "email": "freek@spatie.be",
                    "homepage": "https://flareapp.io",
                    "role": "Developer"
                }
            ],
            "description": "Solution contracts for Ignition",
            "homepage": "https://github.com/facade/ignition-contracts",
            "keywords": [
                "contracts",
                "flare",
                "ignition"
            ],
            "support": {
                "issues": "https://github.com/facade/ignition-contracts/issues",
                "source": "https://github.com/facade/ignition-contracts/tree/1.0.2"
            },
            "time": "2020-10-16T08:27:54+00:00"
        },
        {
            "name": "fakerphp/faker",
            "version": "v1.15.0",
            "source": {
                "type": "git",
                "url": "https://github.com/FakerPHP/Faker.git",
                "reference": "89c6201c74db25fa759ff16e78a4d8f32547770e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FakerPHP/Faker/zipball/89c6201c74db25fa759ff16e78a4d8f32547770e",
                "reference": "89c6201c74db25fa759ff16e78a4d8f32547770e",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "psr/container": "^1.0",
                "symfony/deprecation-contracts": "^2.2"
            },
            "conflict": {
                "fzaninotto/faker": "*"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "ext-intl": "*",
                "symfony/phpunit-bridge": "^4.4 || ^5.2"
            },
            "suggest": {
                "ext-curl": "Required by Faker\\Provider\\Image to download images.",
                "ext-dom": "Required by Faker\\Provider\\HtmlLorem for generating random HTML.",
                "ext-iconv": "Required by Faker\\Provider\\ru_RU\\Text::realText() for generating real Russian text.",
                "ext-mbstring": "Required for multibyte Unicode string functionality."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "v1.15-dev"
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
            "support": {
                "issues": "https://github.com/FakerPHP/Faker/issues",
                "source": "https://github.com/FakerPHP/Faker/tree/v1.15.0"
            },
            "time": "2021-07-06T20:39:40+00:00"
        },
        {
            "name": "filp/whoops",
            "version": "2.14.0",
            "source": {
                "type": "git",
                "url": "https://github.com/filp/whoops.git",
                "reference": "fdf92f03e150ed84d5967a833ae93abffac0315b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/filp/whoops/zipball/fdf92f03e150ed84d5967a833ae93abffac0315b",
                "reference": "fdf92f03e150ed84d5967a833ae93abffac0315b",
                "shasum": ""
            },
            "require": {
                "php": "^5.5.9 || ^7.0 || ^8.0",
                "psr/log": "^1.0.1"
            },
            "require-dev": {
                "mockery/mockery": "^0.9 || ^1.0",
                "phpunit/phpunit": "^4.8.36 || ^5.7.27 || ^6.5.14 || ^7.5.20 || ^8.5.8 || ^9.3.3",
                "symfony/var-dumper": "^2.6 || ^3.0 || ^4.0 || ^5.0"
            },
            "suggest": {
                "symfony/var-dumper": "Pretty print complex values better with var-dumper available",
                "whoops/soap": "Formats errors as SOAP responses"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7-dev"
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
            "support": {
                "issues": "https://github.com/filp/whoops/issues",
                "source": "https://github.com/filp/whoops/tree/2.14.0"
            },
            "funding": [
                {
                    "url": "https://github.com/denis-sokolov",
                    "type": "github"
                }
            ],
            "time": "2021-07-13T12:00:00+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "shasum": ""
            },
            "require": {
                "php": "^5.3|^7.0|^8.0"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "^1.4 || ^2.0",
                "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "hamcrest"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "support": {
                "issues": "https://github.com/hamcrest/hamcrest-php/issues",
                "source": "https://github.com/hamcrest/hamcrest-php/tree/v2.0.1"
            },
            "time": "2020-07-09T08:09:16+00:00"
        },
        {
            "name": "laravel/sail",
            "version": "v1.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/sail.git",
                "reference": "05cf80b1365a0b556f6c21ed5c71a27971d06ec8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/sail/zipball/05cf80b1365a0b556f6c21ed5c71a27971d06ec8",
                "reference": "05cf80b1365a0b556f6c21ed5c71a27971d06ec8",
                "shasum": ""
            },
            "require": {
                "illuminate/console": "^8.0|^9.0",
                "illuminate/contracts": "^8.0|^9.0",
                "illuminate/support": "^8.0|^9.0",
                "php": "^7.3|^8.0"
            },
            "bin": [
                "bin/sail"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                },
                "laravel": {
                    "providers": [
                        "Laravel\\Sail\\SailServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Laravel\\Sail\\": "src/"
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
            "description": "Docker files for running a basic Laravel application.",
            "keywords": [
                "docker",
                "laravel"
            ],
            "support": {
                "issues": "https://github.com/laravel/sail/issues",
                "source": "https://github.com/laravel/sail"
            },
            "time": "2021-08-17T16:00:47+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "1.4.3",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "d1339f64479af1bee0e82a0413813fe5345a54ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/d1339f64479af1bee0e82a0413813fe5345a54ea",
                "reference": "d1339f64479af1bee0e82a0413813fe5345a54ea",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "^2.0.1",
                "lib-pcre": ">=7.0",
                "php": "^7.3 || ^8.0"
            },
            "conflict": {
                "phpunit/phpunit": "<8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5 || ^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4.x-dev"
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
            "support": {
                "issues": "https://github.com/mockery/mockery/issues",
                "source": "https://github.com/mockery/mockery/tree/1.4.3"
            },
            "time": "2021-02-24T09:51:49+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.10.2",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "reference": "776f831124e9c62e1a2c601ecc52e776d8bb7220",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
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
            "support": {
                "issues": "https://github.com/myclabs/DeepCopy/issues",
                "source": "https://github.com/myclabs/DeepCopy/tree/1.10.2"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/deep-copy",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-13T09:40:50+00:00"
        },
        {
            "name": "nunomaduro/collision",
            "version": "v5.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/nunomaduro/collision.git",
                "reference": "0c3c393462eada1233513664e2d22bb9f69ca393"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nunomaduro/collision/zipball/0c3c393462eada1233513664e2d22bb9f69ca393",
                "reference": "0c3c393462eada1233513664e2d22bb9f69ca393",
                "shasum": ""
            },
            "require": {
                "facade/ignition-contracts": "^1.0",
                "filp/whoops": "^2.7.2",
                "php": "^7.3 || ^8.0",
                "symfony/console": "^5.0"
            },
            "require-dev": {
                "brianium/paratest": "^6.1",
                "fideloper/proxy": "^4.4.1",
                "friendsofphp/php-cs-fixer": "^3.0",
                "fruitcake/laravel-cors": "^2.0.3",
                "laravel/framework": "^8.0 || ^9.0",
                "nunomaduro/larastan": "^0.6.2",
                "nunomaduro/mock-final-classes": "^1.0",
                "orchestra/testbench": "^6.0 || ^7.0",
                "phpstan/phpstan": "^0.12.64",
                "phpunit/phpunit": "^9.5.0"
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
            "support": {
                "issues": "https://github.com/nunomaduro/collision/issues",
                "source": "https://github.com/nunomaduro/collision"
            },
            "funding": [
                {
                    "url": "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=66BYDWAT92N6L",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/nunomaduro",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/nunomaduro",
                    "type": "patreon"
                }
            ],
            "time": "2021-08-13T14:23:01+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "97803eca37d319dfa7826cc2437fc020857acb53"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/97803eca37d319dfa7826cc2437fc020857acb53",
                "reference": "97803eca37d319dfa7826cc2437fc020857acb53",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "ext-xmlwriter": "*",
                "phar-io/version": "^3.0.1",
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/phar-io/manifest/issues",
                "source": "https://github.com/phar-io/manifest/tree/2.0.3"
            },
            "time": "2021-07-20T11:28:43+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "bae7c545bef187884426f042434e561ab1ddb182"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/bae7c545bef187884426f042434e561ab1ddb182",
                "reference": "bae7c545bef187884426f042434e561ab1ddb182",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/phar-io/version/issues",
                "source": "https://github.com/phar-io/version/tree/3.1.0"
            },
            "time": "2021-02-23T14:00:09+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-2.x": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src/"
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
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionCommon/issues",
                "source": "https://github.com/phpDocumentor/ReflectionCommon/tree/2.x"
            },
            "time": "2020-06-27T09:03:43+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "5.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/069a785b2141f5bcf49f3e353548dc1cce6df556",
                "reference": "069a785b2141f5bcf49f3e353548dc1cce6df556",
                "shasum": ""
            },
            "require": {
                "ext-filter": "*",
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.2",
                "phpdocumentor/type-resolver": "^1.3",
                "webmozart/assert": "^1.9.1"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
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
                },
                {
                    "name": "Jaap van Otterdijk",
                    "email": "account@ijaap.nl"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionDocBlock/issues",
                "source": "https://github.com/phpDocumentor/ReflectionDocBlock/tree/master"
            },
            "time": "2020-09-03T19:13:55+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "reference": "6a467b8989322d92aa1c8bf2bebcc6e5c2ba55c0",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0",
                "phpdocumentor/reflection-common": "^2.0"
            },
            "require-dev": {
                "ext-tokenizer": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-1.x": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
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
            "description": "A PSR-5 based resolver of Class names, Types and Structural Element Names",
            "support": {
                "issues": "https://github.com/phpDocumentor/TypeResolver/issues",
                "source": "https://github.com/phpDocumentor/TypeResolver/tree/1.4.0"
            },
            "time": "2020-09-17T18:55:26+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "1.13.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "be1996ed8adc35c3fd795488a653f4b518be70ea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/be1996ed8adc35c3fd795488a653f4b518be70ea",
                "reference": "be1996ed8adc35c3fd795488a653f4b518be70ea",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.2",
                "php": "^7.2 || ~8.0, <8.1",
                "phpdocumentor/reflection-docblock": "^5.2",
                "sebastian/comparator": "^3.0 || ^4.0",
                "sebastian/recursion-context": "^3.0 || ^4.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^6.0",
                "phpunit/phpunit": "^8.0 || ^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Prophecy\\": "src/Prophecy"
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
            "support": {
                "issues": "https://github.com/phpspec/prophecy/issues",
                "source": "https://github.com/phpspec/prophecy/tree/1.13.0"
            },
            "time": "2021-03-17T13:42:18+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "9.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "f6293e1b30a2354e8428e004689671b83871edde"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/f6293e1b30a2354e8428e004689671b83871edde",
                "reference": "f6293e1b30a2354e8428e004689671b83871edde",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "ext-xmlwriter": "*",
                "nikic/php-parser": "^4.10.2",
                "php": ">=7.3",
                "phpunit/php-file-iterator": "^3.0.3",
                "phpunit/php-text-template": "^2.0.2",
                "sebastian/code-unit-reverse-lookup": "^2.0.2",
                "sebastian/complexity": "^2.0",
                "sebastian/environment": "^5.1.2",
                "sebastian/lines-of-code": "^1.0.3",
                "sebastian/version": "^3.0.1",
                "theseer/tokenizer": "^1.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcov": "*",
                "ext-xdebug": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.2-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-code-coverage/issues",
                "source": "https://github.com/sebastianbergmann/php-code-coverage/tree/9.2.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-03-28T07:26:59+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "3.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/aa4be8575f26070b100fccb67faabb28f21f66f8",
                "reference": "aa4be8575f26070b100fccb67faabb28f21f66f8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-file-iterator/issues",
                "source": "https://github.com/sebastianbergmann/php-file-iterator/tree/3.0.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:57:25+00:00"
        },
        {
            "name": "phpunit/php-invoker",
            "version": "3.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-invoker.git",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-invoker/zipball/5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "ext-pcntl": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcntl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1-dev"
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
            "description": "Invoke callables with a timeout",
            "homepage": "https://github.com/sebastianbergmann/php-invoker/",
            "keywords": [
                "process"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-invoker/issues",
                "source": "https://github.com/sebastianbergmann/php-invoker/tree/3.1.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:58:55+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-text-template/issues",
                "source": "https://github.com/sebastianbergmann/php-text-template/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T05:33:50+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "5.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-timer/issues",
                "source": "https://github.com/sebastianbergmann/php-timer/tree/5.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:16:10+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "9.5.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "191768ccd5c85513b4068bdbe99bb6390c7d54fb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/191768ccd5c85513b4068bdbe99bb6390c7d54fb",
                "reference": "191768ccd5c85513b4068bdbe99bb6390c7d54fb",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.3.1",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "ext-xmlwriter": "*",
                "myclabs/deep-copy": "^1.10.1",
                "phar-io/manifest": "^2.0.3",
                "phar-io/version": "^3.0.2",
                "php": ">=7.3",
                "phpspec/prophecy": "^1.12.1",
                "phpunit/php-code-coverage": "^9.2.3",
                "phpunit/php-file-iterator": "^3.0.5",
                "phpunit/php-invoker": "^3.1.1",
                "phpunit/php-text-template": "^2.0.3",
                "phpunit/php-timer": "^5.0.2",
                "sebastian/cli-parser": "^1.0.1",
                "sebastian/code-unit": "^1.0.6",
                "sebastian/comparator": "^4.0.5",
                "sebastian/diff": "^4.0.3",
                "sebastian/environment": "^5.1.3",
                "sebastian/exporter": "^4.0.3",
                "sebastian/global-state": "^5.0.1",
                "sebastian/object-enumerator": "^4.0.3",
                "sebastian/resource-operations": "^3.0.3",
                "sebastian/type": "^2.3.4",
                "sebastian/version": "^3.0.2"
            },
            "require-dev": {
                "ext-pdo": "*",
                "phpspec/prophecy-phpunit": "^2.0.1"
            },
            "suggest": {
                "ext-soap": "*",
                "ext-xdebug": "*"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.5-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ],
                "files": [
                    "src/Framework/Assert/Functions.php"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/phpunit/issues",
                "source": "https://github.com/sebastianbergmann/phpunit/tree/9.5.8"
            },
            "funding": [
                {
                    "url": "https://phpunit.de/donate.html",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-07-31T15:17:34+00:00"
        },
        {
            "name": "sebastian/cli-parser",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/cli-parser.git",
                "reference": "442e7c7e687e42adc03470c7b668bc4b2402c0b2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/cli-parser/zipball/442e7c7e687e42adc03470c7b668bc4b2402c0b2",
                "reference": "442e7c7e687e42adc03470c7b668bc4b2402c0b2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for parsing CLI options",
            "homepage": "https://github.com/sebastianbergmann/cli-parser",
            "support": {
                "issues": "https://github.com/sebastianbergmann/cli-parser/issues",
                "source": "https://github.com/sebastianbergmann/cli-parser/tree/1.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:08:49+00:00"
        },
        {
            "name": "sebastian/code-unit",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit.git",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit/zipball/1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the PHP code units",
            "homepage": "https://github.com/sebastianbergmann/code-unit",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit/issues",
                "source": "https://github.com/sebastianbergmann/code-unit/tree/1.0.8"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:08:54+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/issues",
                "source": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/tree/2.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:30:19+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "4.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/55f4261989e546dc112258c7a75935a81a7ce382",
                "reference": "55f4261989e546dc112258c7a75935a81a7ce382",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/diff": "^4.0",
                "sebastian/exporter": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
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
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/comparator/issues",
                "source": "https://github.com/sebastianbergmann/comparator/tree/4.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T15:49:45+00:00"
        },
        {
            "name": "sebastian/complexity",
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/complexity.git",
                "reference": "739b35e53379900cc9ac327b2147867b8b6efd88"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/complexity/zipball/739b35e53379900cc9ac327b2147867b8b6efd88",
                "reference": "739b35e53379900cc9ac327b2147867b8b6efd88",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.7",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Library for calculating the complexity of PHP code units",
            "homepage": "https://github.com/sebastianbergmann/complexity",
            "support": {
                "issues": "https://github.com/sebastianbergmann/complexity/issues",
                "source": "https://github.com/sebastianbergmann/complexity/tree/2.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T15:52:27+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "reference": "3461e3fccc7cfdfc2720be910d3bd73c69be590d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3",
                "symfony/process": "^4.2 || ^5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/diff/issues",
                "source": "https://github.com/sebastianbergmann/diff/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:10:38+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "5.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/388b6ced16caa751030f6a69e588299fa09200ac",
                "reference": "388b6ced16caa751030f6a69e588299fa09200ac",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.1-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/environment/issues",
                "source": "https://github.com/sebastianbergmann/environment/tree/5.1.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:52:38+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "4.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "reference": "d89cc98761b8cb5a1a235a6b703ae50d34080e65",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/exporter/issues",
                "source": "https://github.com/sebastianbergmann/exporter/tree/4.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:24:23+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "5.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "23bd5951f7ff26f12d4e3242864df3e08dec4e49"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/23bd5951f7ff26f12d4e3242864df3e08dec4e49",
                "reference": "23bd5951f7ff26f12d4e3242864df3e08dec4e49",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-dom": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/global-state/issues",
                "source": "https://github.com/sebastianbergmann/global-state/tree/5.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-06-11T13:31:12+00:00"
        },
        {
            "name": "sebastian/lines-of-code",
            "version": "1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/lines-of-code.git",
                "reference": "c1c2e997aa3146983ed888ad08b15470a2e22ecc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/lines-of-code/zipball/c1c2e997aa3146983ed888ad08b15470a2e22ecc",
                "reference": "c1c2e997aa3146983ed888ad08b15470a2e22ecc",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.6",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for counting the lines of code in PHP source code",
            "homepage": "https://github.com/sebastianbergmann/lines-of-code",
            "support": {
                "issues": "https://github.com/sebastianbergmann/lines-of-code/issues",
                "source": "https://github.com/sebastianbergmann/lines-of-code/tree/1.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-11-28T06:42:11+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/5c9eeac41b290a3712d88851518825ad78f45c71",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-enumerator/issues",
                "source": "https://github.com/sebastianbergmann/object-enumerator/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:12:34+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
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
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-reflector/issues",
                "source": "https://github.com/sebastianbergmann/object-reflector/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:14:26+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/cd9d8cf3c5804de4341c283ed787f099f5506172",
                "reference": "cd9d8cf3c5804de4341c283ed787f099f5506172",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
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
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "support": {
                "issues": "https://github.com/sebastianbergmann/recursion-context/issues",
                "source": "https://github.com/sebastianbergmann/recursion-context/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:17:30+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "reference": "0f4443cb3a1d92ce809899753bc0d5d5a8dd19a8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
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
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "support": {
                "issues": "https://github.com/sebastianbergmann/resource-operations/issues",
                "source": "https://github.com/sebastianbergmann/resource-operations/tree/3.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:45:17+00:00"
        },
        {
            "name": "sebastian/type",
            "version": "2.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/type.git",
                "reference": "b8cd8a1c753c90bc1a0f5372170e3e489136f914"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/type/zipball/b8cd8a1c753c90bc1a0f5372170e3e489136f914",
                "reference": "b8cd8a1c753c90bc1a0f5372170e3e489136f914",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
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
            "description": "Collection of value objects that represent the types of the PHP type system",
            "homepage": "https://github.com/sebastianbergmann/type",
            "support": {
                "issues": "https://github.com/sebastianbergmann/type/issues",
                "source": "https://github.com/sebastianbergmann/type/tree/2.3.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-06-15T12:49:02+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "c6c1022351a901512170118436c764e473f6de8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/c6c1022351a901512170118436c764e473f6de8c",
                "reference": "c6c1022351a901512170118436c764e473f6de8c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
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
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "support": {
                "issues": "https://github.com/sebastianbergmann/version/issues",
                "source": "https://github.com/sebastianbergmann/version/tree/3.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:39:44+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "34a41e998c2183e22995f158c581e7b5e755ab9e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/34a41e998c2183e22995f158c581e7b5e755ab9e",
                "reference": "34a41e998c2183e22995f158c581e7b5e755ab9e",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.2 || ^8.0"
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
            "support": {
                "issues": "https://github.com/theseer/tokenizer/issues",
                "source": "https://github.com/theseer/tokenizer/tree/1.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2021-07-28T10:34:58+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "dev",
    "stability-flags": [],
    "prefer-stable": true,
    "prefer-lowest": false,
    "platform": {
        "php": "^7.3|^8.0"
    },
    "platform-dev": [],
    "plugin-api-version": "2.1.0"
}


File: /mikrotik-payment\config\app.php
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

    'debug' => (bool) env('APP_DEBUG', false),

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

    'asset_url' => env('ASSET_URL', null),

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
    | Faker Locale
    |--------------------------------------------------------------------------
    |
    | This locale will be used by the Faker PHP library when generating fake
    | data for your database seeds. For example, this will be used to get
    | localized telephone numbers, street address information and more.
    |
    */

    'faker_locale' => 'en_US',

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
        'Arr' => Illuminate\Support\Arr::class,
        'Artisan' => Illuminate\Support\Facades\Artisan::class,
        'Auth' => Illuminate\Support\Facades\Auth::class,
        'Blade' => Illuminate\Support\Facades\Blade::class,
        'Broadcast' => Illuminate\Support\Facades\Broadcast::class,
        'Bus' => Illuminate\Support\Facades\Bus::class,
        'Cache' => Illuminate\Support\Facades\Cache::class,
        'Config' => Illuminate\Support\Facades\Config::class,
        'Cookie' => Illuminate\Support\Facades\Cookie::class,
        'Crypt' => Illuminate\Support\Facades\Crypt::class,
        'Date' => Illuminate\Support\Facades\Date::class,
        'DB' => Illuminate\Support\Facades\DB::class,
        'Eloquent' => Illuminate\Database\Eloquent\Model::class,
        'Event' => Illuminate\Support\Facades\Event::class,
        'File' => Illuminate\Support\Facades\File::class,
        'Gate' => Illuminate\Support\Facades\Gate::class,
        'Hash' => Illuminate\Support\Facades\Hash::class,
        'Http' => Illuminate\Support\Facades\Http::class,
        'Lang' => Illuminate\Support\Facades\Lang::class,
        'Log' => Illuminate\Support\Facades\Log::class,
        'Mail' => Illuminate\Support\Facades\Mail::class,
        'Notification' => Illuminate\Support\Facades\Notification::class,
        'Password' => Illuminate\Support\Facades\Password::class,
        'Queue' => Illuminate\Support\Facades\Queue::class,
        'RateLimiter' => Illuminate\Support\Facades\RateLimiter::class,
        'Redirect' => Illuminate\Support\Facades\Redirect::class,
        // 'Redis' => Illuminate\Support\Facades\Redis::class,
        'Request' => Illuminate\Support\Facades\Request::class,
        'Response' => Illuminate\Support\Facades\Response::class,
        'Route' => Illuminate\Support\Facades\Route::class,
        'Schema' => Illuminate\Support\Facades\Schema::class,
        'Session' => Illuminate\Support\Facades\Session::class,
        'Storage' => Illuminate\Support\Facades\Storage::class,
        'Str' => Illuminate\Support\Str::class,
        'URL' => Illuminate\Support\Facades\URL::class,
        'Validator' => Illuminate\Support\Facades\Validator::class,
        'View' => Illuminate\Support\Facades\View::class,

    ],

];


File: /mikrotik-payment\config\auth.php
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
    | Supported: "session"
    |
    */

    'guards' => [
        'web' => [
            'driver' => 'session',
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
            'model' => App\Models\User::class,
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
            'throttle' => 60,
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Password Confirmation Timeout
    |--------------------------------------------------------------------------
    |
    | Here you may define the amount of seconds before a password confirmation
    | times out and the user is prompted to re-enter their password via the
    | confirmation screen. By default, the timeout lasts for three hours.
    |
    */

    'password_timeout' => 10800,

];


File: /mikrotik-payment\config\broadcasting.php
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
    | Supported: "pusher", "ably", "redis", "log", "null"
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
                'useTLS' => true,
            ],
        ],

        'ably' => [
            'driver' => 'ably',
            'key' => env('ABLY_KEY'),
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


File: /mikrotik-payment\config\cache.php
<?php

use Illuminate\Support\Str;

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
    | Supported drivers: "apc", "array", "database", "file",
    |         "memcached", "redis", "dynamodb", "octane", "null"
    |
    */

    'stores' => [

        'apc' => [
            'driver' => 'apc',
        ],

        'array' => [
            'driver' => 'array',
            'serialize' => false,
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'cache',
            'connection' => null,
            'lock_connection' => null,
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
                // Memcached::OPT_CONNECT_TIMEOUT => 2000,
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
            'lock_connection' => 'default',
        ],

        'dynamodb' => [
            'driver' => 'dynamodb',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
            'table' => env('DYNAMODB_CACHE_TABLE', 'cache'),
            'endpoint' => env('DYNAMODB_ENDPOINT'),
        ],

        'octane' => [
            'driver' => 'octane',
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

    'prefix' => env('CACHE_PREFIX', Str::slug(env('APP_NAME', 'laravel'), '_').'_cache'),

];


File: /mikrotik-payment\config\cors.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Cross-Origin Resource Sharing (CORS) Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may configure your settings for cross-origin resource sharing
    | or "CORS". This determines what cross-origin operations may execute
    | in web browsers. You are free to adjust these settings as needed.
    |
    | To learn more: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    |
    */

    'paths' => ['api/*', 'sanctum/csrf-cookie'],

    'allowed_methods' => ['*'],

    'allowed_origins' => ['*'],

    'allowed_origins_patterns' => [],

    'allowed_headers' => ['*'],

    'exposed_headers' => [],

    'max_age' => 0,

    'supports_credentials' => false,

];


File: /mikrotik-payment\config\database.php
<?php

use Illuminate\Support\Str;

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
            'url' => env('DATABASE_URL'),
            'database' => env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' => '',
            'foreign_key_constraints' => env('DB_FOREIGN_KEYS', true),
        ],

        'mysql' => [
            'driver' => 'mysql',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'prefix_indexes' => true,
            'strict' => true,
            'engine' => null,
            'options' => extension_loaded('pdo_mysql') ? array_filter([
                PDO::MYSQL_ATTR_SSL_CA => env('MYSQL_ATTR_SSL_CA'),
            ]) : [],
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'prefix_indexes' => true,
            'schema' => 'public',
            'sslmode' => 'prefer',
        ],

        'sqlsrv' => [
            'driver' => 'sqlsrv',
            'url' => env('DATABASE_URL'),
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '1433'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'prefix_indexes' => true,
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
    | provides a richer body of commands than a typical key-value system
    | such as APC or Memcached. Laravel makes it easy to dig right in.
    |
    */

    'redis' => [

        'client' => env('REDIS_CLIENT', 'phpredis'),

        'options' => [
            'cluster' => env('REDIS_CLUSTER', 'redis'),
            'prefix' => env('REDIS_PREFIX', Str::slug(env('APP_NAME', 'laravel'), '_').'_database_'),
        ],

        'default' => [
            'url' => env('REDIS_URL'),
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', '6379'),
            'database' => env('REDIS_DB', '0'),
        ],

        'cache' => [
            'url' => env('REDIS_URL'),
            'host' => env('REDIS_HOST', '127.0.0.1'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', '6379'),
            'database' => env('REDIS_CACHE_DB', '1'),
        ],

    ],

];


File: /mikrotik-payment\config\filesystems.php
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
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Here you may configure as many filesystem "disks" as you wish, and you
    | may even configure multiple disks of the same driver. Defaults have
    | been setup for each driver as an example of the required options.
    |
    | Supported Drivers: "local", "ftp", "sftp", "s3"
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
            'endpoint' => env('AWS_ENDPOINT'),
            'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Symbolic Links
    |--------------------------------------------------------------------------
    |
    | Here you may configure the symbolic links that will be created when the
    | `storage:link` Artisan command is executed. The array keys should be
    | the locations of the links and the values should be their targets.
    |
    */

    'links' => [
        public_path('storage') => storage_path('app/public'),
    ],

];


File: /mikrotik-payment\config\hashing.php
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


File: /mikrotik-payment\config\logging.php
<?php

use Monolog\Handler\NullHandler;
use Monolog\Handler\StreamHandler;
use Monolog\Handler\SyslogUdpHandler;

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
            'ignore_exceptions' => false,
        ],

        'single' => [
            'driver' => 'single',
            'path' => storage_path('logs/laravel.log'),
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'daily' => [
            'driver' => 'daily',
            'path' => storage_path('logs/laravel.log'),
            'level' => env('LOG_LEVEL', 'debug'),
            'days' => 14,
        ],

        'slack' => [
            'driver' => 'slack',
            'url' => env('LOG_SLACK_WEBHOOK_URL'),
            'username' => 'Laravel Log',
            'emoji' => ':boom:',
            'level' => env('LOG_LEVEL', 'critical'),
        ],

        'papertrail' => [
            'driver' => 'monolog',
            'level' => env('LOG_LEVEL', 'debug'),
            'handler' => SyslogUdpHandler::class,
            'handler_with' => [
                'host' => env('PAPERTRAIL_URL'),
                'port' => env('PAPERTRAIL_PORT'),
            ],
        ],

        'stderr' => [
            'driver' => 'monolog',
            'level' => env('LOG_LEVEL', 'debug'),
            'handler' => StreamHandler::class,
            'formatter' => env('LOG_STDERR_FORMATTER'),
            'with' => [
                'stream' => 'php://stderr',
            ],
        ],

        'syslog' => [
            'driver' => 'syslog',
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'errorlog' => [
            'driver' => 'errorlog',
            'level' => env('LOG_LEVEL', 'debug'),
        ],

        'null' => [
            'driver' => 'monolog',
            'handler' => NullHandler::class,
        ],

        'emergency' => [
            'path' => storage_path('logs/laravel.log'),
        ],
    ],

];


File: /mikrotik-payment\config\mail.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Mailer
    |--------------------------------------------------------------------------
    |
    | This option controls the default mailer that is used to send any email
    | messages sent by your application. Alternative mailers may be setup
    | and used as needed; however, this mailer will be used by default.
    |
    */

    'default' => env('MAIL_MAILER', 'smtp'),

    /*
    |--------------------------------------------------------------------------
    | Mailer Configurations
    |--------------------------------------------------------------------------
    |
    | Here you may configure all of the mailers used by your application plus
    | their respective settings. Several examples have been configured for
    | you and you are free to add your own as your application requires.
    |
    | Laravel supports a variety of mail "transport" drivers to be used while
    | sending an e-mail. You will specify which one you are using for your
    | mailers below. You are free to add additional mailers as required.
    |
    | Supported: "smtp", "sendmail", "mailgun", "ses",
    |            "postmark", "log", "array"
    |
    */

    'mailers' => [
        'smtp' => [
            'transport' => 'smtp',
            'host' => env('MAIL_HOST', 'smtp.mailgun.org'),
            'port' => env('MAIL_PORT', 587),
            'encryption' => env('MAIL_ENCRYPTION', 'tls'),
            'username' => env('MAIL_USERNAME'),
            'password' => env('MAIL_PASSWORD'),
            'timeout' => null,
            'auth_mode' => null,
        ],

        'ses' => [
            'transport' => 'ses',
        ],

        'mailgun' => [
            'transport' => 'mailgun',
        ],

        'postmark' => [
            'transport' => 'postmark',
        ],

        'sendmail' => [
            'transport' => 'sendmail',
            'path' => '/usr/sbin/sendmail -bs',
        ],

        'log' => [
            'transport' => 'log',
            'channel' => env('MAIL_LOG_CHANNEL'),
        ],

        'array' => [
            'transport' => 'array',
        ],
    ],

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


File: /mikrotik-payment\config\queue.php
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
            'after_commit' => false,
        ],

        'beanstalkd' => [
            'driver' => 'beanstalkd',
            'host' => 'localhost',
            'queue' => 'default',
            'retry_after' => 90,
            'block_for' => 0,
            'after_commit' => false,
        ],

        'sqs' => [
            'driver' => 'sqs',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'prefix' => env('SQS_PREFIX', 'https://sqs.us-east-1.amazonaws.com/your-account-id'),
            'queue' => env('SQS_QUEUE', 'default'),
            'suffix' => env('SQS_SUFFIX'),
            'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
            'after_commit' => false,
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => env('REDIS_QUEUE', 'default'),
            'retry_after' => 90,
            'block_for' => null,
            'after_commit' => false,
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
        'driver' => env('QUEUE_FAILED_DRIVER', 'database-uuids'),
        'database' => env('DB_CONNECTION', 'mysql'),
        'table' => 'failed_jobs',
    ],

];


File: /mikrotik-payment\config\sanctum.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Stateful Domains
    |--------------------------------------------------------------------------
    |
    | Requests from the following domains / hosts will receive stateful API
    | authentication cookies. Typically, these should include your local
    | and production domains which access your API via a frontend SPA.
    |
    */

    'stateful' => explode(',', env('SANCTUM_STATEFUL_DOMAINS', sprintf(
        '%s%s',
        'localhost,localhost:3000,127.0.0.1,127.0.0.1:8000,::1',
        env('APP_URL') ? ','.parse_url(env('APP_URL'), PHP_URL_HOST) : ''
    ))),

    /*
    |--------------------------------------------------------------------------
    | Expiration Minutes
    |--------------------------------------------------------------------------
    |
    | This value controls the number of minutes until an issued token will be
    | considered expired. If this value is null, personal access tokens do
    | not expire. This won't tweak the lifetime of first-party sessions.
    |
    */

    'expiration' => null,

    /*
    |--------------------------------------------------------------------------
    | Sanctum Middleware
    |--------------------------------------------------------------------------
    |
    | When authenticating your first-party SPA with Sanctum you may need to
    | customize some of the middleware Sanctum uses while processing the
    | request. You may change the middleware listed below as required.
    |
    */

    'middleware' => [
        'verify_csrf_token' => App\Http\Middleware\VerifyCsrfToken::class,
        'encrypt_cookies' => App\Http\Middleware\EncryptCookies::class,
    ],

];


File: /mikrotik-payment\config\services.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Third Party Services
    |--------------------------------------------------------------------------
    |
    | This file is for storing the credentials for third party services such
    | as Mailgun, Postmark, AWS and more. This file provides the de facto
    | location for this type of information, allowing packages to have
    | a conventional file to locate the various service credentials.
    |
    */

    'mailgun' => [
        'domain' => env('MAILGUN_DOMAIN'),
        'secret' => env('MAILGUN_SECRET'),
        'endpoint' => env('MAILGUN_ENDPOINT', 'api.mailgun.net'),
    ],

    'postmark' => [
        'token' => env('POSTMARK_TOKEN'),
    ],

    'ses' => [
        'key' => env('AWS_ACCESS_KEY_ID'),
        'secret' => env('AWS_SECRET_ACCESS_KEY'),
        'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    ],

];


File: /mikrotik-payment\config\session.php
<?php

use Illuminate\Support\Str;

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
    |            "memcached", "redis", "dynamodb", "array"
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
    | While using one of the framework's cache driven session backends you may
    | list a cache store that should be used for these sessions. This value
    | must match with one of the application's configured cache "stores".
    |
    | Affects: "apc", "dynamodb", "memcached", "redis"
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
        Str::slug(env('APP_NAME', 'laravel'), '_').'_session'
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
    | the cookie from being sent to you when it can't be done securely.
    |
    */

    'secure' => env('SESSION_SECURE_COOKIE'),

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
    | will set this value to "lax" since this is a secure default value.
    |
    | Supported: "lax", "strict", "none", null
    |
    */

    'same_site' => 'lax',

];


File: /mikrotik-payment\config\view.php
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

    'compiled' => env(
        'VIEW_COMPILED_PATH',
        realpath(storage_path('framework/views'))
    ),

];


File: /mikrotik-payment\database\.gitignore
*.sqlite*


File: /mikrotik-payment\database\factories\UserFactory.php
<?php

namespace Database\Factories;

use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

class UserFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = User::class;

    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'name' => $this->faker->name(),
            'email' => $this->faker->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', // password
            'remember_token' => Str::random(10),
        ];
    }

    /**
     * Indicate that the model's email address should be unverified.
     *
     * @return \Illuminate\Database\Eloquent\Factories\Factory
     */
    public function unverified()
    {
        return $this->state(function (array $attributes) {
            return [
                'email_verified_at' => null,
            ];
        });
    }
}


File: /mikrotik-payment\database\migrations\2014_10_12_000000_create_users_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

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
            $table->id();
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


File: /mikrotik-payment\database\migrations\2014_10_12_100000_create_password_resets_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

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


File: /mikrotik-payment\database\migrations\2019_08_19_000000_create_failed_jobs_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateFailedJobsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('failed_jobs', function (Blueprint $table) {
            $table->id();
            $table->string('uuid')->unique();
            $table->text('connection');
            $table->text('queue');
            $table->longText('payload');
            $table->longText('exception');
            $table->timestamp('failed_at')->useCurrent();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('failed_jobs');
    }
}


File: /mikrotik-payment\database\migrations\2019_12_14_000001_create_personal_access_tokens_table.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePersonalAccessTokensTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('personal_access_tokens', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->morphs('tokenable');
            $table->string('name');
            $table->string('token', 64)->unique();
            $table->text('abilities')->nullable();
            $table->timestamp('last_used_at')->nullable();
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
        Schema::dropIfExists('personal_access_tokens');
    }
}


File: /mikrotik-payment\database\seeders\DatabaseSeeder.php
<?php

namespace Database\Seeders;

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
        // \App\Models\User::factory(10)->create();
    }
}


File: /mikrotik-payment\package.json
{
    "private": true,
    "scripts": {
        "dev": "npm run development",
        "development": "mix",
        "watch": "mix watch",
        "watch-poll": "mix watch -- --watch-options-poll=1000",
        "hot": "mix watch --hot",
        "prod": "npm run production",
        "production": "mix --production"
    },
    "devDependencies": {
        "axios": "^0.21",
        "laravel-mix": "^6.0.6",
        "lodash": "^4.17.19",
        "postcss": "^8.1.14"
    }
}


File: /mikrotik-payment\phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="./vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         colors="true"
>
    <testsuites>
        <testsuite name="Unit">
            <directory suffix="Test.php">./tests/Unit</directory>
        </testsuite>
        <testsuite name="Feature">
            <directory suffix="Test.php">./tests/Feature</directory>
        </testsuite>
    </testsuites>
    <coverage processUncoveredFiles="true">
        <include>
            <directory suffix=".php">./app</directory>
        </include>
    </coverage>
    <php>
        <server name="APP_ENV" value="testing"/>
        <server name="BCRYPT_ROUNDS" value="4"/>
        <server name="CACHE_DRIVER" value="array"/>
        <!-- <server name="DB_CONNECTION" value="sqlite"/> -->
        <!-- <server name="DB_DATABASE" value=":memory:"/> -->
        <server name="MAIL_MAILER" value="array"/>
        <server name="QUEUE_CONNECTION" value="sync"/>
        <server name="SESSION_DRIVER" value="array"/>
        <server name="TELESCOPE_ENABLED" value="false"/>
    </php>
</phpunit>


File: /mikrotik-payment\public\.htaccess
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

    # Send Requests To Front Controller...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [L]
</IfModule>


File: /mikrotik-payment\public\index.php
<?php

use Illuminate\Contracts\Http\Kernel;
use Illuminate\Http\Request;

define('LARAVEL_START', microtime(true));

/*
|--------------------------------------------------------------------------
| Check If The Application Is Under Maintenance
|--------------------------------------------------------------------------
|
| If the application is in maintenance / demo mode via the "down" command
| we will load this file so that any pre-rendered content can be shown
| instead of starting the framework, which could cause an exception.
|
*/

if (file_exists(__DIR__.'/../storage/framework/maintenance.php')) {
    require __DIR__.'/../storage/framework/maintenance.php';
}

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader for
| this application. We just need to utilize it! We'll simply require it
| into the script here so we don't need to manually load our classes.
|
*/

require __DIR__.'/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Run The Application
|--------------------------------------------------------------------------
|
| Once we have the application, we can handle the incoming request using
| the application's HTTP kernel. Then, we will send the response back
| to this client's browser, allowing them to enjoy our application.
|
*/

$app = require_once __DIR__.'/../bootstrap/app.php';

$kernel = $app->make(Kernel::class);

$response = tap($kernel->handle(
    $request = Request::capture()
))->send();

$kernel->terminate($request, $response);


File: /mikrotik-payment\public\robots.txt
User-agent: *
Disallow:


File: /mikrotik-payment\public\web.config
<!--
    Rewrites requires Microsoft URL Rewrite Module for IIS
    Download: https://www.iis.net/downloads/microsoft/url-rewrite
    Debug Help: https://docs.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-failed-request-tracing-to-trace-rewrite-rules
-->
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


File: /mikrotik-payment\README.md
<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains over 1500 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[Many](https://www.many.co.uk)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- **[DevSquad](https://devsquad.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[OP.GG](https://op.gg)**
- **[CMS Max](https://www.cmsmax.com/)**
- **[WebReinvent](https://webreinvent.com/?utm_source=laravel&utm_medium=github&utm_campaign=patreon-sponsors)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).


File: /mikrotik-payment\resources\js\app.js
require('./bootstrap');


File: /mikrotik-payment\resources\js\bootstrap.js
window._ = require('lodash');

/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Laravel back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

/**
 * Echo exposes an expressive API for subscribing to channels and listening
 * for events that are broadcast by Laravel. Echo and event broadcasting
 * allows your team to easily build robust real-time web applications.
 */

// import Echo from 'laravel-echo';

// window.Pusher = require('pusher-js');

// window.Echo = new Echo({
//     broadcaster: 'pusher',
//     key: process.env.MIX_PUSHER_APP_KEY,
//     cluster: process.env.MIX_PUSHER_APP_CLUSTER,
//     forceTLS: true
// });


File: /mikrotik-payment\resources\lang\en\auth.php
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
    'password' => 'The provided password is incorrect.',
    'throttle' => 'Too many login attempts. Please try again in :seconds seconds.',

];


File: /mikrotik-payment\resources\lang\en\pagination.php
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
    'next' => 'Next &raquo;',

];


File: /mikrotik-payment\resources\lang\en\passwords.php
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

    'reset' => 'Your password has been reset!',
    'sent' => 'We have emailed your password reset link!',
    'throttled' => 'Please wait before retrying.',
    'token' => 'This password reset token is invalid.',
    'user' => "We can't find a user with that email address.",

];


File: /mikrotik-payment\resources\lang\en\validation.php
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

    'accepted' => 'The :attribute must be accepted.',
    'accepted_if' => 'The :attribute must be accepted when :other is :value.',
    'active_url' => 'The :attribute is not a valid URL.',
    'after' => 'The :attribute must be a date after :date.',
    'after_or_equal' => 'The :attribute must be a date after or equal to :date.',
    'alpha' => 'The :attribute must only contain letters.',
    'alpha_dash' => 'The :attribute must only contain letters, numbers, dashes and underscores.',
    'alpha_num' => 'The :attribute must only contain letters and numbers.',
    'array' => 'The :attribute must be an array.',
    'before' => 'The :attribute must be a date before :date.',
    'before_or_equal' => 'The :attribute must be a date before or equal to :date.',
    'between' => [
        'numeric' => 'The :attribute must be between :min and :max.',
        'file' => 'The :attribute must be between :min and :max kilobytes.',
        'string' => 'The :attribute must be between :min and :max characters.',
        'array' => 'The :attribute must have between :min and :max items.',
    ],
    'boolean' => 'The :attribute field must be true or false.',
    'confirmed' => 'The :attribute confirmation does not match.',
    'current_password' => 'The password is incorrect.',
    'date' => 'The :attribute is not a valid date.',
    'date_equals' => 'The :attribute must be a date equal to :date.',
    'date_format' => 'The :attribute does not match the format :format.',
    'different' => 'The :attribute and :other must be different.',
    'digits' => 'The :attribute must be :digits digits.',
    'digits_between' => 'The :attribute must be between :min and :max digits.',
    'dimensions' => 'The :attribute has invalid image dimensions.',
    'distinct' => 'The :attribute field has a duplicate value.',
    'email' => 'The :attribute must be a valid email address.',
    'ends_with' => 'The :attribute must end with one of the following: :values.',
    'exists' => 'The selected :attribute is invalid.',
    'file' => 'The :attribute must be a file.',
    'filled' => 'The :attribute field must have a value.',
    'gt' => [
        'numeric' => 'The :attribute must be greater than :value.',
        'file' => 'The :attribute must be greater than :value kilobytes.',
        'string' => 'The :attribute must be greater than :value characters.',
        'array' => 'The :attribute must have more than :value items.',
    ],
    'gte' => [
        'numeric' => 'The :attribute must be greater than or equal :value.',
        'file' => 'The :attribute must be greater than or equal :value kilobytes.',
        'string' => 'The :attribute must be greater than or equal :value characters.',
        'array' => 'The :attribute must have :value items or more.',
    ],
    'image' => 'The :attribute must be an image.',
    'in' => 'The selected :attribute is invalid.',
    'in_array' => 'The :attribute field does not exist in :other.',
    'integer' => 'The :attribute must be an integer.',
    'ip' => 'The :attribute must be a valid IP address.',
    'ipv4' => 'The :attribute must be a valid IPv4 address.',
    'ipv6' => 'The :attribute must be a valid IPv6 address.',
    'json' => 'The :attribute must be a valid JSON string.',
    'lt' => [
        'numeric' => 'The :attribute must be less than :value.',
        'file' => 'The :attribute must be less than :value kilobytes.',
        'string' => 'The :attribute must be less than :value characters.',
        'array' => 'The :attribute must have less than :value items.',
    ],
    'lte' => [
        'numeric' => 'The :attribute must be less than or equal :value.',
        'file' => 'The :attribute must be less than or equal :value kilobytes.',
        'string' => 'The :attribute must be less than or equal :value characters.',
        'array' => 'The :attribute must not have more than :value items.',
    ],
    'max' => [
        'numeric' => 'The :attribute must not be greater than :max.',
        'file' => 'The :attribute must not be greater than :max kilobytes.',
        'string' => 'The :attribute must not be greater than :max characters.',
        'array' => 'The :attribute must not have more than :max items.',
    ],
    'mimes' => 'The :attribute must be a file of type: :values.',
    'mimetypes' => 'The :attribute must be a file of type: :values.',
    'min' => [
        'numeric' => 'The :attribute must be at least :min.',
        'file' => 'The :attribute must be at least :min kilobytes.',
        'string' => 'The :attribute must be at least :min characters.',
        'array' => 'The :attribute must have at least :min items.',
    ],
    'multiple_of' => 'The :attribute must be a multiple of :value.',
    'not_in' => 'The selected :attribute is invalid.',
    'not_regex' => 'The :attribute format is invalid.',
    'numeric' => 'The :attribute must be a number.',
    'password' => 'The password is incorrect.',
    'present' => 'The :attribute field must be present.',
    'regex' => 'The :attribute format is invalid.',
    'required' => 'The :attribute field is required.',
    'required_if' => 'The :attribute field is required when :other is :value.',
    'required_unless' => 'The :attribute field is required unless :other is in :values.',
    'required_with' => 'The :attribute field is required when :values is present.',
    'required_with_all' => 'The :attribute field is required when :values are present.',
    'required_without' => 'The :attribute field is required when :values is not present.',
    'required_without_all' => 'The :attribute field is required when none of :values are present.',
    'prohibited' => 'The :attribute field is prohibited.',
    'prohibited_if' => 'The :attribute field is prohibited when :other is :value.',
    'prohibited_unless' => 'The :attribute field is prohibited unless :other is in :values.',
    'same' => 'The :attribute and :other must match.',
    'size' => [
        'numeric' => 'The :attribute must be :size.',
        'file' => 'The :attribute must be :size kilobytes.',
        'string' => 'The :attribute must be :size characters.',
        'array' => 'The :attribute must contain :size items.',
    ],
    'starts_with' => 'The :attribute must start with one of the following: :values.',
    'string' => 'The :attribute must be a string.',
    'timezone' => 'The :attribute must be a valid timezone.',
    'unique' => 'The :attribute has already been taken.',
    'uploaded' => 'The :attribute failed to upload.',
    'url' => 'The :attribute must be a valid URL.',
    'uuid' => 'The :attribute must be a valid UUID.',

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
    | The following language lines are used to swap our attribute placeholder
    | with something more reader friendly such as "E-Mail Address" instead
    | of "email". This simply helps us make our message more expressive.
    |
    */

    'attributes' => [],

];


File: /mikrotik-payment\resources\views\welcome.blade.php
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

        <!-- Styles -->
        <style>
            /*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */html{line-height:1.15;-webkit-text-size-adjust:100%}body{margin:0}a{background-color:transparent}[hidden]{display:none}html{font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;line-height:1.5}*,:after,:before{box-sizing:border-box;border:0 solid #e2e8f0}a{color:inherit;text-decoration:inherit}svg,video{display:block;vertical-align:middle}video{max-width:100%;height:auto}.bg-white{--bg-opacity:1;background-color:#fff;background-color:rgba(255,255,255,var(--bg-opacity))}.bg-gray-100{--bg-opacity:1;background-color:#f7fafc;background-color:rgba(247,250,252,var(--bg-opacity))}.border-gray-200{--border-opacity:1;border-color:#edf2f7;border-color:rgba(237,242,247,var(--border-opacity))}.border-t{border-top-width:1px}.flex{display:flex}.grid{display:grid}.hidden{display:none}.items-center{align-items:center}.justify-center{justify-content:center}.font-semibold{font-weight:600}.h-5{height:1.25rem}.h-8{height:2rem}.h-16{height:4rem}.text-sm{font-size:.875rem}.text-lg{font-size:1.125rem}.leading-7{line-height:1.75rem}.mx-auto{margin-left:auto;margin-right:auto}.ml-1{margin-left:.25rem}.mt-2{margin-top:.5rem}.mr-2{margin-right:.5rem}.ml-2{margin-left:.5rem}.mt-4{margin-top:1rem}.ml-4{margin-left:1rem}.mt-8{margin-top:2rem}.ml-12{margin-left:3rem}.-mt-px{margin-top:-1px}.max-w-6xl{max-width:72rem}.min-h-screen{min-height:100vh}.overflow-hidden{overflow:hidden}.p-6{padding:1.5rem}.py-4{padding-top:1rem;padding-bottom:1rem}.px-6{padding-left:1.5rem;padding-right:1.5rem}.pt-8{padding-top:2rem}.fixed{position:fixed}.relative{position:relative}.top-0{top:0}.right-0{right:0}.shadow{box-shadow:0 1px 3px 0 rgba(0,0,0,.1),0 1px 2px 0 rgba(0,0,0,.06)}.text-center{text-align:center}.text-gray-200{--text-opacity:1;color:#edf2f7;color:rgba(237,242,247,var(--text-opacity))}.text-gray-300{--text-opacity:1;color:#e2e8f0;color:rgba(226,232,240,var(--text-opacity))}.text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}.text-gray-500{--text-opacity:1;color:#a0aec0;color:rgba(160,174,192,var(--text-opacity))}.text-gray-600{--text-opacity:1;color:#718096;color:rgba(113,128,150,var(--text-opacity))}.text-gray-700{--text-opacity:1;color:#4a5568;color:rgba(74,85,104,var(--text-opacity))}.text-gray-900{--text-opacity:1;color:#1a202c;color:rgba(26,32,44,var(--text-opacity))}.underline{text-decoration:underline}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.w-5{width:1.25rem}.w-8{width:2rem}.w-auto{width:auto}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}@media (min-width:640px){.sm\:rounded-lg{border-radius:.5rem}.sm\:block{display:block}.sm\:items-center{align-items:center}.sm\:justify-start{justify-content:flex-start}.sm\:justify-between{justify-content:space-between}.sm\:h-20{height:5rem}.sm\:ml-0{margin-left:0}.sm\:px-6{padding-left:1.5rem;padding-right:1.5rem}.sm\:pt-0{padding-top:0}.sm\:text-left{text-align:left}.sm\:text-right{text-align:right}}@media (min-width:768px){.md\:border-t-0{border-top-width:0}.md\:border-l{border-left-width:1px}.md\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (min-width:1024px){.lg\:px-8{padding-left:2rem;padding-right:2rem}}@media (prefers-color-scheme:dark){.dark\:bg-gray-800{--bg-opacity:1;background-color:#2d3748;background-color:rgba(45,55,72,var(--bg-opacity))}.dark\:bg-gray-900{--bg-opacity:1;background-color:#1a202c;background-color:rgba(26,32,44,var(--bg-opacity))}.dark\:border-gray-700{--border-opacity:1;border-color:#4a5568;border-color:rgba(74,85,104,var(--border-opacity))}.dark\:text-white{--text-opacity:1;color:#fff;color:rgba(255,255,255,var(--text-opacity))}.dark\:text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}}
        </style>

        <style>
            body {
                font-family: 'Nunito', sans-serif;
            }
        </style>
    </head>
    <body class="antialiased">
        <div class="relative flex items-top justify-center min-h-screen bg-gray-100 dark:bg-gray-900 sm:items-center py-4 sm:pt-0">
            @if (Route::has('login'))
                <div class="hidden fixed top-0 right-0 px-6 py-4 sm:block">
                    @auth
                        <a href="{{ url('/home') }}" class="text-sm text-gray-700 underline">Home</a>
                    @else
                        <a href="{{ route('login') }}" class="text-sm text-gray-700 underline">Log in</a>

                        @if (Route::has('register'))
                            <a href="{{ route('register') }}" class="ml-4 text-sm text-gray-700 underline">Register</a>
                        @endif
                    @endauth
                </div>
            @endif

            <div class="max-w-6xl mx-auto sm:px-6 lg:px-8">
                <div class="flex justify-center pt-8 sm:justify-start sm:pt-0">
                    <svg viewBox="0 0 651 192" fill="none" xmlns="http://www.w3.org/2000/svg" class="h-16 w-auto text-gray-700 sm:h-20">
                        <g clip-path="url(#clip0)" fill="#EF3B2D">
                            <path d="M248.032 44.676h-16.466v100.23h47.394v-14.748h-30.928V44.676zM337.091 87.202c-2.101-3.341-5.083-5.965-8.949-7.875-3.865-1.909-7.756-2.864-11.669-2.864-5.062 0-9.69.931-13.89 2.792-4.201 1.861-7.804 4.417-10.811 7.661-3.007 3.246-5.347 6.993-7.016 11.239-1.672 4.249-2.506 8.713-2.506 13.389 0 4.774.834 9.26 2.506 13.459 1.669 4.202 4.009 7.925 7.016 11.169 3.007 3.246 6.609 5.799 10.811 7.66 4.199 1.861 8.828 2.792 13.89 2.792 3.913 0 7.804-.955 11.669-2.863 3.866-1.908 6.849-4.533 8.949-7.875v9.021h15.607V78.182h-15.607v9.02zm-1.431 32.503c-.955 2.578-2.291 4.821-4.009 6.73-1.719 1.91-3.795 3.437-6.229 4.582-2.435 1.146-5.133 1.718-8.091 1.718-2.96 0-5.633-.572-8.019-1.718-2.387-1.146-4.438-2.672-6.156-4.582-1.719-1.909-3.032-4.152-3.938-6.73-.909-2.577-1.36-5.298-1.36-8.161 0-2.864.451-5.585 1.36-8.162.905-2.577 2.219-4.819 3.938-6.729 1.718-1.908 3.77-3.437 6.156-4.582 2.386-1.146 5.059-1.718 8.019-1.718 2.958 0 5.656.572 8.091 1.718 2.434 1.146 4.51 2.674 6.229 4.582 1.718 1.91 3.054 4.152 4.009 6.729.953 2.577 1.432 5.298 1.432 8.162-.001 2.863-.479 5.584-1.432 8.161zM463.954 87.202c-2.101-3.341-5.083-5.965-8.949-7.875-3.865-1.909-7.756-2.864-11.669-2.864-5.062 0-9.69.931-13.89 2.792-4.201 1.861-7.804 4.417-10.811 7.661-3.007 3.246-5.347 6.993-7.016 11.239-1.672 4.249-2.506 8.713-2.506 13.389 0 4.774.834 9.26 2.506 13.459 1.669 4.202 4.009 7.925 7.016 11.169 3.007 3.246 6.609 5.799 10.811 7.66 4.199 1.861 8.828 2.792 13.89 2.792 3.913 0 7.804-.955 11.669-2.863 3.866-1.908 6.849-4.533 8.949-7.875v9.021h15.607V78.182h-15.607v9.02zm-1.432 32.503c-.955 2.578-2.291 4.821-4.009 6.73-1.719 1.91-3.795 3.437-6.229 4.582-2.435 1.146-5.133 1.718-8.091 1.718-2.96 0-5.633-.572-8.019-1.718-2.387-1.146-4.438-2.672-6.156-4.582-1.719-1.909-3.032-4.152-3.938-6.73-.909-2.577-1.36-5.298-1.36-8.161 0-2.864.451-5.585 1.36-8.162.905-2.577 2.219-4.819 3.938-6.729 1.718-1.908 3.77-3.437 6.156-4.582 2.386-1.146 5.059-1.718 8.019-1.718 2.958 0 5.656.572 8.091 1.718 2.434 1.146 4.51 2.674 6.229 4.582 1.718 1.91 3.054 4.152 4.009 6.729.953 2.577 1.432 5.298 1.432 8.162 0 2.863-.479 5.584-1.432 8.161zM650.772 44.676h-15.606v100.23h15.606V44.676zM365.013 144.906h15.607V93.538h26.776V78.182h-42.383v66.724zM542.133 78.182l-19.616 51.096-19.616-51.096h-15.808l25.617 66.724h19.614l25.617-66.724h-15.808zM591.98 76.466c-19.112 0-34.239 15.706-34.239 35.079 0 21.416 14.641 35.079 36.239 35.079 12.088 0 19.806-4.622 29.234-14.688l-10.544-8.158c-.006.008-7.958 10.449-19.832 10.449-13.802 0-19.612-11.127-19.612-16.884h51.777c2.72-22.043-11.772-40.877-33.023-40.877zm-18.713 29.28c.12-1.284 1.917-16.884 18.589-16.884 16.671 0 18.697 15.598 18.813 16.884h-37.402zM184.068 43.892c-.024-.088-.073-.165-.104-.25-.058-.157-.108-.316-.191-.46-.056-.097-.137-.176-.203-.265-.087-.117-.161-.242-.265-.345-.085-.086-.194-.148-.29-.223-.109-.085-.206-.182-.327-.252l-.002-.001-.002-.002-35.648-20.524a2.971 2.971 0 00-2.964 0l-35.647 20.522-.002.002-.002.001c-.121.07-.219.167-.327.252-.096.075-.205.138-.29.223-.103.103-.178.228-.265.345-.066.089-.147.169-.203.265-.083.144-.133.304-.191.46-.031.085-.08.162-.104.25-.067.249-.103.51-.103.776v38.979l-29.706 17.103V24.493a3 3 0 00-.103-.776c-.024-.088-.073-.165-.104-.25-.058-.157-.108-.316-.191-.46-.056-.097-.137-.176-.203-.265-.087-.117-.161-.242-.265-.345-.085-.086-.194-.148-.29-.223-.109-.085-.206-.182-.327-.252l-.002-.001-.002-.002L40.098 1.396a2.971 2.971 0 00-2.964 0L1.487 21.919l-.002.002-.002.001c-.121.07-.219.167-.327.252-.096.075-.205.138-.29.223-.103.103-.178.228-.265.345-.066.089-.147.169-.203.265-.083.144-.133.304-.191.46-.031.085-.08.162-.104.25-.067.249-.103.51-.103.776v122.09c0 1.063.568 2.044 1.489 2.575l71.293 41.045c.156.089.324.143.49.202.078.028.15.074.23.095a2.98 2.98 0 001.524 0c.069-.018.132-.059.2-.083.176-.061.354-.119.519-.214l71.293-41.045a2.971 2.971 0 001.489-2.575v-38.979l34.158-19.666a2.971 2.971 0 001.489-2.575V44.666a3.075 3.075 0 00-.106-.774zM74.255 143.167l-29.648-16.779 31.136-17.926.001-.001 34.164-19.669 29.674 17.084-21.772 12.428-43.555 24.863zm68.329-76.259v33.841l-12.475-7.182-17.231-9.92V49.806l12.475 7.182 17.231 9.92zm2.97-39.335l29.693 17.095-29.693 17.095-29.693-17.095 29.693-17.095zM54.06 114.089l-12.475 7.182V46.733l17.231-9.92 12.475-7.182v74.537l-17.231 9.921zM38.614 7.398l29.693 17.095-29.693 17.095L8.921 24.493 38.614 7.398zM5.938 29.632l12.475 7.182 17.231 9.92v79.676l.001.005-.001.006c0 .114.032.221.045.333.017.146.021.294.059.434l.002.007c.032.117.094.222.14.334.051.124.088.255.156.371a.036.036 0 00.004.009c.061.105.149.191.222.288.081.105.149.22.244.314l.008.01c.084.083.19.142.284.215.106.083.202.178.32.247l.013.005.011.008 34.139 19.321v34.175L5.939 144.867V29.632h-.001zm136.646 115.235l-65.352 37.625V148.31l48.399-27.628 16.953-9.677v33.862zm35.646-61.22l-29.706 17.102V66.908l17.231-9.92 12.475-7.182v33.841z"/>
                        </g>
                    </svg>
                </div>

                <div class="mt-8 bg-white dark:bg-gray-800 overflow-hidden shadow sm:rounded-lg">
                    <div class="grid grid-cols-1 md:grid-cols-2">
                        <div class="p-6">
                            <div class="flex items-center">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" class="w-8 h-8 text-gray-500"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                                <div class="ml-4 text-lg leading-7 font-semibold"><a href="https://laravel.com/docs" class="underline text-gray-900 dark:text-white">Documentation</a></div>
                            </div>

                            <div class="ml-12">
                                <div class="mt-2 text-gray-600 dark:text-gray-400 text-sm">
                                    Laravel has wonderful, thorough documentation covering every aspect of the framework. Whether you are new to the framework or have previous experience with Laravel, we recommend reading all of the documentation from beginning to end.
                                </div>
                            </div>
                        </div>

                        <div class="p-6 border-t border-gray-200 dark:border-gray-700 md:border-t-0 md:border-l">
                            <div class="flex items-center">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" class="w-8 h-8 text-gray-500"><path d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                                <div class="ml-4 text-lg leading-7 font-semibold"><a href="https://laracasts.com" class="underline text-gray-900 dark:text-white">Laracasts</a></div>
                            </div>

                            <div class="ml-12">
                                <div class="mt-2 text-gray-600 dark:text-gray-400 text-sm">
                                    Laracasts offers thousands of video tutorials on Laravel, PHP, and JavaScript development. Check them out, see for yourself, and massively level up your development skills in the process.
                                </div>
                            </div>
                        </div>

                        <div class="p-6 border-t border-gray-200 dark:border-gray-700">
                            <div class="flex items-center">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" class="w-8 h-8 text-gray-500"><path d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
                                <div class="ml-4 text-lg leading-7 font-semibold"><a href="https://laravel-news.com/" class="underline text-gray-900 dark:text-white">Laravel News</a></div>
                            </div>

                            <div class="ml-12">
                                <div class="mt-2 text-gray-600 dark:text-gray-400 text-sm">
                                    Laravel News is a community driven portal and newsletter aggregating all of the latest and most important news in the Laravel ecosystem, including new package releases and tutorials.
                                </div>
                            </div>
                        </div>

                        <div class="p-6 border-t border-gray-200 dark:border-gray-700 md:border-l">
                            <div class="flex items-center">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" class="w-8 h-8 text-gray-500"><path d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                <div class="ml-4 text-lg leading-7 font-semibold text-gray-900 dark:text-white">Vibrant Ecosystem</div>
                            </div>

                            <div class="ml-12">
                                <div class="mt-2 text-gray-600 dark:text-gray-400 text-sm">
                                    Laravel's robust library of first-party tools and libraries, such as <a href="https://forge.laravel.com" class="underline">Forge</a>, <a href="https://vapor.laravel.com" class="underline">Vapor</a>, <a href="https://nova.laravel.com" class="underline">Nova</a>, and <a href="https://envoyer.io" class="underline">Envoyer</a> help you take your projects to the next level. Pair them with powerful open source libraries like <a href="https://laravel.com/docs/billing" class="underline">Cashier</a>, <a href="https://laravel.com/docs/dusk" class="underline">Dusk</a>, <a href="https://laravel.com/docs/broadcasting" class="underline">Echo</a>, <a href="https://laravel.com/docs/horizon" class="underline">Horizon</a>, <a href="https://laravel.com/docs/sanctum" class="underline">Sanctum</a>, <a href="https://laravel.com/docs/telescope" class="underline">Telescope</a>, and more.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex justify-center mt-4 sm:items-center sm:justify-between">
                    <div class="text-center text-sm text-gray-500 sm:text-left">
                        <div class="flex items-center">
                            <svg fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor" class="-mt-px w-5 h-5 text-gray-400">
                                <path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                            </svg>

                            <a href="https://laravel.bigcartel.com" class="ml-1 underline">
                                Shop
                            </a>

                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" class="ml-4 -mt-px w-5 h-5 text-gray-400">
                                <path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                            </svg>

                            <a href="https://github.com/sponsors/taylorotwell" class="ml-1 underline">
                                Sponsor
                            </a>
                        </div>
                    </div>

                    <div class="ml-4 text-center text-sm text-gray-500 sm:text-right sm:ml-0">
                        Laravel v{{ Illuminate\Foundation\Application::VERSION }} (PHP v{{ PHP_VERSION }})
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>


File: /mikrotik-payment\routes\api.php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

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

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});


File: /mikrotik-payment\routes\channels.php
<?php

use Illuminate\Support\Facades\Broadcast;

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

Broadcast::channel('App.Models.User.{id}', function ($user, $id) {
    return (int) $user->id === (int) $id;
});


File: /mikrotik-payment\routes\console.php
<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;

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
})->purpose('Display an inspiring quote');


File: /mikrotik-payment\routes\web.php
<?php

use Illuminate\Support\Facades\Route;

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

Route::get('/', function () {
    return view('welcome');
});


File: /mikrotik-payment\server.php
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


File: /mikrotik-payment\storage\app\.gitignore
*
!public/
!.gitignore


File: /mikrotik-payment\storage\app\public\.gitignore
*
!.gitignore


File: /mikrotik-payment\storage\framework\.gitignore
compiled.php
config.php
down
events.scanned.php
maintenance.php
routes.php
routes.scanned.php
schedule-*
services.json


File: /mikrotik-payment\storage\framework\cache\.gitignore
*
!data/
!.gitignore


File: /mikrotik-payment\storage\framework\cache\data\.gitignore
*
!.gitignore


File: /mikrotik-payment\storage\framework\sessions\.gitignore
*
!.gitignore


File: /mikrotik-payment\storage\framework\testing\.gitignore
*
!.gitignore


File: /mikrotik-payment\storage\framework\views\.gitignore
*
!.gitignore


File: /mikrotik-payment\storage\logs\.gitignore
*
!.gitignore


File: /mikrotik-payment\tests\CreatesApplication.php
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


File: /mikrotik-payment\tests\Feature\ExampleTest.php
<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function test_example()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }
}


File: /mikrotik-payment\tests\TestCase.php
<?php

namespace Tests;

use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    use CreatesApplication;
}


File: /mikrotik-payment\tests\Unit\ExampleTest.php
<?php

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function test_example()
    {
        $this->assertTrue(true);
    }
}


File: /mikrotik-payment\webpack.mix.js
const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/js/app.js', 'public/js')
    .postCss('resources/css/app.css', 'public/css', [
        //
    ]);


File: /package.json
{
    "private": true,
    "scripts": {
        "dev": "npm run development",
        "development": "mix",
        "watch": "mix watch",
        "watch-poll": "mix watch -- --watch-options-poll=1000",
        "hot": "mix watch --hot",
        "prod": "npm run production",
        "production": "mix --production"
    },
    "devDependencies": {
        "axios": "^0.21",
        "laravel-mix": "^6.0.6",
        "lodash": "^4.17.19",
        "postcss": "^8.1.14"
    }
}


File: /phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="./vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         colors="true"
>
    <testsuites>
        <testsuite name="Unit">
            <directory suffix="Test.php">./tests/Unit</directory>
        </testsuite>
        <testsuite name="Feature">
            <directory suffix="Test.php">./tests/Feature</directory>
        </testsuite>
    </testsuites>
    <coverage processUncoveredFiles="true">
        <include>
            <directory suffix=".php">./app</directory>
        </include>
    </coverage>
    <php>
        <server name="APP_ENV" value="testing"/>
        <server name="BCRYPT_ROUNDS" value="4"/>
        <server name="CACHE_DRIVER" value="array"/>
        <!-- <server name="DB_CONNECTION" value="sqlite"/> -->
        <!-- <server name="DB_DATABASE" value=":memory:"/> -->
        <server name="MAIL_MAILER" value="array"/>
        <server name="QUEUE_CONNECTION" value="sync"/>
        <server name="SESSION_DRIVER" value="array"/>
        <server name="TELESCOPE_ENABLED" value="false"/>
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

    # Send Requests To Front Controller...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [L]
</IfModule>


File: /public\index.php
<?php

use Illuminate\Contracts\Http\Kernel;
use Illuminate\Http\Request;

define('LARAVEL_START', microtime(true));

/*
|--------------------------------------------------------------------------
| Check If The Application Is Under Maintenance
|--------------------------------------------------------------------------
|
| If the application is in maintenance / demo mode via the "down" command
| we will load this file so that any pre-rendered content can be shown
| instead of starting the framework, which could cause an exception.
|
*/

if (file_exists(__DIR__.'/../storage/framework/maintenance.php')) {
    require __DIR__.'/../storage/framework/maintenance.php';
}

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader for
| this application. We just need to utilize it! We'll simply require it
| into the script here so we don't need to manually load our classes.
|
*/

require __DIR__.'/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Run The Application
|--------------------------------------------------------------------------
|
| Once we have the application, we can handle the incoming request using
| the application's HTTP kernel. Then, we will send the response back
| to this client's browser, allowing them to enjoy our application.
|
*/

$app = require_once __DIR__.'/../bootstrap/app.php';

$kernel = $app->make(Kernel::class);

$response = tap($kernel->handle(
    $request = Request::capture()
))->send();

$kernel->terminate($request, $response);


File: /public\robots.txt
User-agent: *
Disallow:


File: /public\web.config
<!--
    Rewrites requires Microsoft URL Rewrite Module for IIS
    Download: https://www.iis.net/downloads/microsoft/url-rewrite
    Debug Help: https://docs.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-failed-request-tracing-to-trace-rewrite-rules
-->
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


File: /README.md
<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## About Laravel

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

- [Simple, fast routing engine](https://laravel.com/docs/routing).
- [Powerful dependency injection container](https://laravel.com/docs/container).
- Multiple back-ends for [session](https://laravel.com/docs/session) and [cache](https://laravel.com/docs/cache) storage.
- Expressive, intuitive [database ORM](https://laravel.com/docs/eloquent).
- Database agnostic [schema migrations](https://laravel.com/docs/migrations).
- [Robust background job processing](https://laravel.com/docs/queues).
- [Real-time event broadcasting](https://laravel.com/docs/broadcasting).

Laravel is accessible, powerful, and provides tools required for large, robust applications.

## Learning Laravel

Laravel has the most extensive and thorough [documentation](https://laravel.com/docs) and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

If you don't feel like reading, [Laracasts](https://laracasts.com) can help. Laracasts contains over 1500 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

## Laravel Sponsors

We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel [Patreon page](https://patreon.com/taylorotwell).

### Premium Partners

- **[Vehikl](https://vehikl.com/)**
- **[Tighten Co.](https://tighten.co)**
- **[Kirschbaum Development Group](https://kirschbaumdevelopment.com)**
- **[64 Robots](https://64robots.com)**
- **[Cubet Techno Labs](https://cubettech.com)**
- **[Cyber-Duck](https://cyber-duck.co.uk)**
- **[Many](https://www.many.co.uk)**
- **[Webdock, Fast VPS Hosting](https://www.webdock.io/en)**
- **[DevSquad](https://devsquad.com)**
- **[Curotec](https://www.curotec.com/services/technologies/laravel/)**
- **[OP.GG](https://op.gg)**
- **[CMS Max](https://www.cmsmax.com/)**
- **[WebReinvent](https://webreinvent.com/?utm_source=laravel&utm_medium=github&utm_campaign=patreon-sponsors)**

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](https://laravel.com/docs/contributions).

## Code of Conduct

In order to ensure that the Laravel community is welcoming to all, please review and abide by the [Code of Conduct](https://laravel.com/docs/contributions#code-of-conduct).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via [taylor@laravel.com](mailto:taylor@laravel.com). All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).


File: /resources\js\app.js
require('./bootstrap');


File: /resources\js\bootstrap.js
window._ = require('lodash');

/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Laravel back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

/**
 * Echo exposes an expressive API for subscribing to channels and listening
 * for events that are broadcast by Laravel. Echo and event broadcasting
 * allows your team to easily build robust real-time web applications.
 */

// import Echo from 'laravel-echo';

// window.Pusher = require('pusher-js');

// window.Echo = new Echo({
//     broadcaster: 'pusher',
//     key: process.env.MIX_PUSHER_APP_KEY,
//     cluster: process.env.MIX_PUSHER_APP_CLUSTER,
//     forceTLS: true
// });


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
    'password' => 'The provided password is incorrect.',
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

    'previous' => '&laquo; Previous',
    'next' => 'Next &raquo;',

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

    'reset' => 'Your password has been reset!',
    'sent' => 'We have emailed your password reset link!',
    'throttled' => 'Please wait before retrying.',
    'token' => 'This password reset token is invalid.',
    'user' => "We can't find a user with that email address.",

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

    'accepted' => 'The :attribute must be accepted.',
    'accepted_if' => 'The :attribute must be accepted when :other is :value.',
    'active_url' => 'The :attribute is not a valid URL.',
    'after' => 'The :attribute must be a date after :date.',
    'after_or_equal' => 'The :attribute must be a date after or equal to :date.',
    'alpha' => 'The :attribute must only contain letters.',
    'alpha_dash' => 'The :attribute must only contain letters, numbers, dashes and underscores.',
    'alpha_num' => 'The :attribute must only contain letters and numbers.',
    'array' => 'The :attribute must be an array.',
    'before' => 'The :attribute must be a date before :date.',
    'before_or_equal' => 'The :attribute must be a date before or equal to :date.',
    'between' => [
        'numeric' => 'The :attribute must be between :min and :max.',
        'file' => 'The :attribute must be between :min and :max kilobytes.',
        'string' => 'The :attribute must be between :min and :max characters.',
        'array' => 'The :attribute must have between :min and :max items.',
    ],
    'boolean' => 'The :attribute field must be true or false.',
    'confirmed' => 'The :attribute confirmation does not match.',
    'current_password' => 'The password is incorrect.',
    'date' => 'The :attribute is not a valid date.',
    'date_equals' => 'The :attribute must be a date equal to :date.',
    'date_format' => 'The :attribute does not match the format :format.',
    'different' => 'The :attribute and :other must be different.',
    'digits' => 'The :attribute must be :digits digits.',
    'digits_between' => 'The :attribute must be between :min and :max digits.',
    'dimensions' => 'The :attribute has invalid image dimensions.',
    'distinct' => 'The :attribute field has a duplicate value.',
    'email' => 'The :attribute must be a valid email address.',
    'ends_with' => 'The :attribute must end with one of the following: :values.',
    'exists' => 'The selected :attribute is invalid.',
    'file' => 'The :attribute must be a file.',
    'filled' => 'The :attribute field must have a value.',
    'gt' => [
        'numeric' => 'The :attribute must be greater than :value.',
        'file' => 'The :attribute must be greater than :value kilobytes.',
        'string' => 'The :attribute must be greater than :value characters.',
        'array' => 'The :attribute must have more than :value items.',
    ],
    'gte' => [
        'numeric' => 'The :attribute must be greater than or equal :value.',
        'file' => 'The :attribute must be greater than or equal :value kilobytes.',
        'string' => 'The :attribute must be greater than or equal :value characters.',
        'array' => 'The :attribute must have :value items or more.',
    ],
    'image' => 'The :attribute must be an image.',
    'in' => 'The selected :attribute is invalid.',
    'in_array' => 'The :attribute field does not exist in :other.',
    'integer' => 'The :attribute must be an integer.',
    'ip' => 'The :attribute must be a valid IP address.',
    'ipv4' => 'The :attribute must be a valid IPv4 address.',
    'ipv6' => 'The :attribute must be a valid IPv6 address.',
    'json' => 'The :attribute must be a valid JSON string.',
    'lt' => [
        'numeric' => 'The :attribute must be less than :value.',
        'file' => 'The :attribute must be less than :value kilobytes.',
        'string' => 'The :attribute must be less than :value characters.',
        'array' => 'The :attribute must have less than :value items.',
    ],
    'lte' => [
        'numeric' => 'The :attribute must be less than or equal :value.',
        'file' => 'The :attribute must be less than or equal :value kilobytes.',
        'string' => 'The :attribute must be less than or equal :value characters.',
        'array' => 'The :attribute must not have more than :value items.',
    ],
    'max' => [
        'numeric' => 'The :attribute must not be greater than :max.',
        'file' => 'The :attribute must not be greater than :max kilobytes.',
        'string' => 'The :attribute must not be greater than :max characters.',
        'array' => 'The :attribute must not have more than :max items.',
    ],
    'mimes' => 'The :attribute must be a file of type: :values.',
    'mimetypes' => 'The :attribute must be a file of type: :values.',
    'min' => [
        'numeric' => 'The :attribute must be at least :min.',
        'file' => 'The :attribute must be at least :min kilobytes.',
        'string' => 'The :attribute must be at least :min characters.',
        'array' => 'The :attribute must have at least :min items.',
    ],
    'multiple_of' => 'The :attribute must be a multiple of :value.',
    'not_in' => 'The selected :attribute is invalid.',
    'not_regex' => 'The :attribute format is invalid.',
    'numeric' => 'The :attribute must be a number.',
    'password' => 'The password is incorrect.',
    'present' => 'The :attribute field must be present.',
    'regex' => 'The :attribute format is invalid.',
    'required' => 'The :attribute field is required.',
    'required_if' => 'The :attribute field is required when :other is :value.',
    'required_unless' => 'The :attribute field is required unless :other is in :values.',
    'required_with' => 'The :attribute field is required when :values is present.',
    'required_with_all' => 'The :attribute field is required when :values are present.',
    'required_without' => 'The :attribute field is required when :values is not present.',
    'required_without_all' => 'The :attribute field is required when none of :values are present.',
    'prohibited' => 'The :attribute field is prohibited.',
    'prohibited_if' => 'The :attribute field is prohibited when :other is :value.',
    'prohibited_unless' => 'The :attribute field is prohibited unless :other is in :values.',
    'same' => 'The :attribute and :other must match.',
    'size' => [
        'numeric' => 'The :attribute must be :size.',
        'file' => 'The :attribute must be :size kilobytes.',
        'string' => 'The :attribute must be :size characters.',
        'array' => 'The :attribute must contain :size items.',
    ],
    'starts_with' => 'The :attribute must start with one of the following: :values.',
    'string' => 'The :attribute must be a string.',
    'timezone' => 'The :attribute must be a valid timezone.',
    'unique' => 'The :attribute has already been taken.',
    'uploaded' => 'The :attribute failed to upload.',
    'url' => 'The :attribute must be a valid URL.',
    'uuid' => 'The :attribute must be a valid UUID.',

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
    | The following language lines are used to swap our attribute placeholder
    | with something more reader friendly such as "E-Mail Address" instead
    | of "email". This simply helps us make our message more expressive.
    |
    */

    'attributes' => [],

];


File: /resources\views\welcome.blade.php
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

        <!-- Styles -->
        <style>
            /*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */html{line-height:1.15;-webkit-text-size-adjust:100%}body{margin:0}a{background-color:transparent}[hidden]{display:none}html{font-family:system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;line-height:1.5}*,:after,:before{box-sizing:border-box;border:0 solid #e2e8f0}a{color:inherit;text-decoration:inherit}svg,video{display:block;vertical-align:middle}video{max-width:100%;height:auto}.bg-white{--bg-opacity:1;background-color:#fff;background-color:rgba(255,255,255,var(--bg-opacity))}.bg-gray-100{--bg-opacity:1;background-color:#f7fafc;background-color:rgba(247,250,252,var(--bg-opacity))}.border-gray-200{--border-opacity:1;border-color:#edf2f7;border-color:rgba(237,242,247,var(--border-opacity))}.border-t{border-top-width:1px}.flex{display:flex}.grid{display:grid}.hidden{display:none}.items-center{align-items:center}.justify-center{justify-content:center}.font-semibold{font-weight:600}.h-5{height:1.25rem}.h-8{height:2rem}.h-16{height:4rem}.text-sm{font-size:.875rem}.text-lg{font-size:1.125rem}.leading-7{line-height:1.75rem}.mx-auto{margin-left:auto;margin-right:auto}.ml-1{margin-left:.25rem}.mt-2{margin-top:.5rem}.mr-2{margin-right:.5rem}.ml-2{margin-left:.5rem}.mt-4{margin-top:1rem}.ml-4{margin-left:1rem}.mt-8{margin-top:2rem}.ml-12{margin-left:3rem}.-mt-px{margin-top:-1px}.max-w-6xl{max-width:72rem}.min-h-screen{min-height:100vh}.overflow-hidden{overflow:hidden}.p-6{padding:1.5rem}.py-4{padding-top:1rem;padding-bottom:1rem}.px-6{padding-left:1.5rem;padding-right:1.5rem}.pt-8{padding-top:2rem}.fixed{position:fixed}.relative{position:relative}.top-0{top:0}.right-0{right:0}.shadow{box-shadow:0 1px 3px 0 rgba(0,0,0,.1),0 1px 2px 0 rgba(0,0,0,.06)}.text-center{text-align:center}.text-gray-200{--text-opacity:1;color:#edf2f7;color:rgba(237,242,247,var(--text-opacity))}.text-gray-300{--text-opacity:1;color:#e2e8f0;color:rgba(226,232,240,var(--text-opacity))}.text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}.text-gray-500{--text-opacity:1;color:#a0aec0;color:rgba(160,174,192,var(--text-opacity))}.text-gray-600{--text-opacity:1;color:#718096;color:rgba(113,128,150,var(--text-opacity))}.text-gray-700{--text-opacity:1;color:#4a5568;color:rgba(74,85,104,var(--text-opacity))}.text-gray-900{--text-opacity:1;color:#1a202c;color:rgba(26,32,44,var(--text-opacity))}.underline{text-decoration:underline}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.w-5{width:1.25rem}.w-8{width:2rem}.w-auto{width:auto}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}@media (min-width:640px){.sm\:rounded-lg{border-radius:.5rem}.sm\:block{display:block}.sm\:items-center{align-items:center}.sm\:justify-start{justify-content:flex-start}.sm\:justify-between{justify-content:space-between}.sm\:h-20{height:5rem}.sm\:ml-0{margin-left:0}.sm\:px-6{padding-left:1.5rem;padding-right:1.5rem}.sm\:pt-0{padding-top:0}.sm\:text-left{text-align:left}.sm\:text-right{text-align:right}}@media (min-width:768px){.md\:border-t-0{border-top-width:0}.md\:border-l{border-left-width:1px}.md\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (min-width:1024px){.lg\:px-8{padding-left:2rem;padding-right:2rem}}@media (prefers-color-scheme:dark){.dark\:bg-gray-800{--bg-opacity:1;background-color:#2d3748;background-color:rgba(45,55,72,var(--bg-opacity))}.dark\:bg-gray-900{--bg-opacity:1;background-color:#1a202c;background-color:rgba(26,32,44,var(--bg-opacity))}.dark\:border-gray-700{--border-opacity:1;border-color:#4a5568;border-color:rgba(74,85,104,var(--border-opacity))}.dark\:text-white{--text-opacity:1;color:#fff;color:rgba(255,255,255,var(--text-opacity))}.dark\:text-gray-400{--text-opacity:1;color:#cbd5e0;color:rgba(203,213,224,var(--text-opacity))}}
        </style>

        <style>
            body {
                font-family: 'Nunito', sans-serif;
            }
        </style>
    </head>
    <body class="antialiased">
      <p>Hello this is Mpesa stk push, here we come</p>
    </body>
</html>


File: /routes\api.php
<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

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

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});


File: /routes\channels.php
<?php

use Illuminate\Support\Facades\Broadcast;

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

Broadcast::channel('App.Models.User.{id}', function ($user, $id) {
    return (int) $user->id === (int) $id;
});


File: /routes\console.php
<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;

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
})->purpose('Display an inspiring quote');


File: /routes\web.php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MpesaController;

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

Route::get('/', function () {
    return view('welcome');
});


Route::get('/simulation',[MpesaController::class,'stkSimulation']);

Route::get('/response',[MpesaController::class,'resData']);


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
compiled.php
config.php
down
events.scanned.php
maintenance.php
routes.php
routes.scanned.php
schedule-*
services.json


File: /storage\framework\cache\.gitignore
*
!data/
!.gitignore


File: /storage\framework\cache\data\.gitignore
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

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function test_example()
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

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function test_example()
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
 | for your Laravel applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/js/app.js', 'public/js')
    .postCss('resources/css/app.css', 'public/css', [
        //
    ]);


