# Repository Information
Name: ipriver_mikrotik_config_generator

# Directory Structure
Directory structure:
└── github_repos/ipriver_mikrotik_config_generator/
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
    │   │       ├── pack-bc89e712fde29db97bcc7a7c76d5fe7b083caca9.idx
    │   │       └── pack-bc89e712fde29db97bcc7a7c76d5fe7b083caca9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    │   ├── .generators
    │   ├── .rakeTasks
    │   ├── dataSources/
    │   │   ├── 134b62c8-28e1-41ba-a12f-db159a3fd8ea/
    │   │   │   └── storage.xml
    │   │   └── 134b62c8-28e1-41ba-a12f-db159a3fd8ea.xml
    │   ├── dataSources.xml
    │   ├── encodings.xml
    │   ├── ipriver_mikrotik_config_generator.iml
    │   ├── misc.xml
    │   ├── modules.xml
    │   ├── runConfigurations/
    │   │   ├── Development__ipriver_mikrotik_config_generator.xml
    │   │   ├── Production__ipriver_mikrotik_config_generator.xml
    │   │   ├── spec__ipriver_mikrotik_config_generator.xml
    │   │   └── test__ipriver_mikrotik_config_generator.xml
    │   ├── vagrant.xml
    │   └── vcs.xml
    ├── app/
    │   ├── assets/
    │   │   ├── config/
    │   │   │   └── manifest.js
    │   │   ├── images/
    │   │   │   └── .keep
    │   │   ├── javascripts/
    │   │   │   ├── application.js
    │   │   │   ├── cable.js
    │   │   │   ├── channels/
    │   │   │   │   └── .keep
    │   │   │   ├── configs.coffee
    │   │   │   ├── config_templates.coffee
    │   │   │   ├── home.coffee
    │   │   │   └── interfaces.coffee
    │   │   └── stylesheets/
    │   │       ├── application.css
    │   │       ├── configs.scss
    │   │       ├── config_templates.scss
    │   │       ├── custom.css
    │   │       ├── home.scss
    │   │       ├── interfaces.scss
    │   │       └── scaffolds.scss
    │   ├── channels/
    │   │   └── application_cable/
    │   │       ├── channel.rb
    │   │       └── connection.rb
    │   ├── controllers/
    │   │   ├── application_controller.rb
    │   │   ├── concerns/
    │   │   │   ├── .keep
    │   │   │   └── config_generator.rb
    │   │   ├── configs_controller.rb
    │   │   ├── config_templates_controller.rb
    │   │   ├── home_controller.rb
    │   │   └── interfaces_controller.rb
    │   ├── helpers/
    │   │   ├── application_helper.rb
    │   │   ├── configs_helper.rb
    │   │   ├── config_templates_helper.rb
    │   │   ├── home_helper.rb
    │   │   └── interfaces_helper.rb
    │   ├── jobs/
    │   │   └── application_job.rb
    │   ├── mailers/
    │   │   └── application_mailer.rb
    │   ├── models/
    │   │   ├── application_record.rb
    │   │   ├── concerns/
    │   │   │   └── .keep
    │   │   ├── config.rb
    │   │   ├── config_template.rb
    │   │   └── interface.rb
    │   └── views/
    │       ├── configs/
    │       │   ├── edit.html.erb
    │       │   ├── index.html.erb
    │       │   ├── index.json.jbuilder
    │       │   ├── new.html.erb
    │       │   ├── show.html.erb
    │       │   ├── show.json.jbuilder
    │       │   ├── _config.json.jbuilder
    │       │   └── _form.html.erb
    │       ├── config_templates/
    │       │   ├── edit.html.erb
    │       │   ├── index.html.erb
    │       │   ├── index.json.jbuilder
    │       │   ├── new.html.erb
    │       │   ├── show.html.erb
    │       │   ├── show.json.jbuilder
    │       │   ├── _config_template.json.jbuilder
    │       │   └── _form.html.erb
    │       ├── home/
    │       │   └── index.html.erb
    │       ├── interfaces/
    │       │   ├── edit.html.erb
    │       │   ├── index.html.erb
    │       │   ├── index.json.jbuilder
    │       │   ├── new.html.erb
    │       │   ├── show.html.erb
    │       │   ├── show.json.jbuilder
    │       │   ├── _form.html.erb
    │       │   └── _interface.json.jbuilder
    │       └── layouts/
    │           ├── application.html.erb
    │           ├── mailer.html.erb
    │           └── mailer.text.erb
    ├── bin/
    │   ├── bundle
    │   ├── rails
    │   ├── rake
    │   ├── setup
    │   ├── spring
    │   └── update
    ├── config/
    │   ├── application.rb
    │   ├── boot.rb
    │   ├── cable.yml
    │   ├── database.yml
    │   ├── environment.rb
    │   ├── environments/
    │   │   ├── development.rb
    │   │   ├── production.rb
    │   │   └── test.rb
    │   ├── initializers/
    │   │   ├── application_controller_renderer.rb
    │   │   ├── assets.rb
    │   │   ├── backtrace_silencers.rb
    │   │   ├── cookies_serializer.rb
    │   │   ├── filter_parameter_logging.rb
    │   │   ├── inflections.rb
    │   │   ├── mime_types.rb
    │   │   ├── new_framework_defaults.rb
    │   │   ├── session_store.rb
    │   │   └── wrap_parameters.rb
    │   ├── locales/
    │   │   └── en.yml
    │   ├── puma.rb
    │   ├── routes.rb
    │   ├── secrets.yml
    │   └── spring.rb
    ├── config.ru
    ├── db/
    │   ├── migrate/
    │   │   ├── 20170117180244_create_interfaces.rb
    │   │   ├── 20170117180319_create_config_templates.rb
    │   │   ├── 20170117180428_create_configs.rb
    │   │   ├── 20170117180733_add_config_to_interface.rb
    │   │   ├── 20170117180948_add_config_template_to_config.rb
    │   │   └── 20170117235021_add_type_to_interface.rb
    │   ├── schema.rb
    │   └── seeds.rb
    ├── Gemfile
    ├── Gemfile.lock
    ├── lib/
    │   ├── assets/
    │   │   └── .keep
    │   └── tasks/
    │       └── .keep
    ├── log/
    │   └── .keep
    ├── public/
    │   ├── 404.html
    │   ├── 422.html
    │   ├── 500.html
    │   └── robots.txt
    ├── Rakefile
    ├── README.md
    ├── test/
    │   ├── controllers/
    │   │   ├── .keep
    │   │   ├── configs_controller_test.rb
    │   │   ├── config_templates_controller_test.rb
    │   │   ├── home_controller_test.rb
    │   │   └── interfaces_controller_test.rb
    │   ├── fixtures/
    │   │   ├── .keep
    │   │   ├── configs.yml
    │   │   ├── config_templates.yml
    │   │   ├── files/
    │   │   │   └── .keep
    │   │   └── interfaces.yml
    │   ├── helpers/
    │   │   └── .keep
    │   ├── integration/
    │   │   └── .keep
    │   ├── mailers/
    │   │   └── .keep
    │   ├── models/
    │   │   ├── .keep
    │   │   ├── config_template_test.rb
    │   │   ├── config_test.rb
    │   │   └── interface_test.rb
    │   └── test_helper.rb
    ├── tmp/
    │   └── .keep
    └── vendor/
        └── assets/
            ├── javascripts/
            │   └── .keep
            └── stylesheets/
                └── .keep


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
	url = https://github.com/deephack1982/ipriver_mikrotik_config_generator.git
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
0000000000000000000000000000000000000000 7950aa98642e9e7b3ce1114ded8b21645d152aad vivek-dodia <vivek.dodia@icloud.com> 1738606457 -0500	clone: from https://github.com/deephack1982/ipriver_mikrotik_config_generator.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 7950aa98642e9e7b3ce1114ded8b21645d152aad vivek-dodia <vivek.dodia@icloud.com> 1738606457 -0500	clone: from https://github.com/deephack1982/ipriver_mikrotik_config_generator.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7950aa98642e9e7b3ce1114ded8b21645d152aad vivek-dodia <vivek.dodia@icloud.com> 1738606457 -0500	clone: from https://github.com/deephack1982/ipriver_mikrotik_config_generator.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8532d88d9ff427bf09ac06a75376978c7016fe24 refs/remotes/origin/deploy
7950aa98642e9e7b3ce1114ded8b21645d152aad refs/remotes/origin/master
bd8fcc3eecb9911ffa1a9855fb2466220a6c7a8c refs/tags/v1.0
^cfb801df8e46c3cd2d253fb868e7a1e450586714


File: /.git\refs\heads\master
7950aa98642e9e7b3ce1114ded8b21645d152aad


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# See https://help.github.com/articles/ignoring-files for more about ignoring files.
#
# If you find yourself ignoring temporary files generated by your text editor
# or operating system, you probably want to add a global ignore instead:
#   git config --global core.excludesfile '~/.gitignore_global'

# Ignore bundler config.
/.bundle

# Ignore all logfiles and tempfiles.
/log/*
/tmp/*
!/log/.keep
!/tmp/.keep

# Ignore Byebug command history file.
.byebug_history


File: /.idea\.generators
<?xml version="1.0" encoding="UTF-8"?>
<Settings><!--This file was automatically generated by Ruby plugin.
You are allowed to: 
1. Reorder generators
2. Remove generators
3. Add installed generators
To add new installed generators automatically delete this file and reload the project.
--><GeneratorsGroup><Generator name="assets" /><Generator name="channel" /><Generator name="coffee:assets" /><Generator name="controller" /><Generator name="generator" /><Generator name="helper" /><Generator name="integration_test" /><Generator name="jbuilder" /><Generator name="job" /><Generator name="js:assets" /><Generator name="mailer" /><Generator name="migration" /><Generator name="model" /><Generator name="resource" /><Generator name="scaffold" /><Generator name="scaffold_controller" /><Generator name="task" /><Generator name="test_unit:generator" /><Generator name="test_unit:plugin" /></GeneratorsGroup></Settings>


File: /.idea\.rakeTasks
<?xml version="1.0" encoding="UTF-8"?>
<Settings><!--This file was automatically generated by Ruby plugin.
You are allowed to: 
1. Remove rake task
2. Add existing rake tasks
To add existing rake tasks automatically delete this file and reload the project.
--><RakeGroup description="" fullCmd="" taksId="rake"><RakeTask description="List versions of all Rails frameworks and the environment" fullCmd="about" taksId="about" /><RakeGroup description="" fullCmd="" taksId="app"><RakeTask description="Applies the template supplied by LOCATION=(/path/to/template) or URL" fullCmd="app:template" taksId="template" /><RakeTask description="Update configs and some other initially generated files (or use just update:configs or update:bin)" fullCmd="app:update" taksId="update" /><RakeGroup description="" fullCmd="" taksId="templates"><RakeTask description="" fullCmd="app:templates:copy" taksId="copy" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="update"><RakeTask description="" fullCmd="app:update:bin" taksId="bin" /><RakeTask description="" fullCmd="app:update:configs" taksId="configs" /><RakeTask description="" fullCmd="app:update:upgrade_guide_info" taksId="upgrade_guide_info" /></RakeGroup></RakeGroup><RakeGroup description="" fullCmd="" taksId="assets"><RakeTask description="Remove old compiled assets" fullCmd="assets:clean[keep]" taksId="clean[keep]" /><RakeTask description="Remove compiled assets" fullCmd="assets:clobber" taksId="clobber" /><RakeTask description="Load asset compile environment" fullCmd="assets:environment" taksId="environment" /><RakeTask description="Compile all the assets named in config.assets.precompile" fullCmd="assets:precompile" taksId="precompile" /><RakeTask description="" fullCmd="assets:clean" taksId="clean" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="cache_digests"><RakeTask description="Lookup first-level dependencies for TEMPLATE (like messages/show or comments/_comment.html)" fullCmd="cache_digests:dependencies" taksId="dependencies" /><RakeTask description="Lookup nested dependencies for TEMPLATE (like messages/show or comments/_comment.html)" fullCmd="cache_digests:nested_dependencies" taksId="nested_dependencies" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="db"><RakeTask description="Creates the database from DATABASE_URL or config/database.yml for the current RAILS_ENV (use db:create:all to create all databases in the config). Without RAILS_ENV or when RAILS_ENV is development, it defaults to creating the development and test databases" fullCmd="db:create" taksId="create" /><RakeTask description="Drops the database from DATABASE_URL or config/database.yml for the current RAILS_ENV (use db:drop:all to drop all databases in the config). Without RAILS_ENV or when RAILS_ENV is development, it defaults to dropping the development and test databases" fullCmd="db:drop" taksId="drop" /><RakeGroup description="" fullCmd="" taksId="environment"><RakeTask description="Set the environment value for the database" fullCmd="db:environment:set" taksId="set" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="fixtures"><RakeTask description="Loads fixtures into the current environment's database" fullCmd="db:fixtures:load" taksId="load" /><RakeTask description="" fullCmd="db:fixtures:identify" taksId="identify" /></RakeGroup><RakeTask description="Migrate the database (options: VERSION=x, VERBOSE=false, SCOPE=blog)" fullCmd="db:migrate" taksId="migrate" /><RakeGroup description="" fullCmd="" taksId="migrate"><RakeTask description="Display status of migrations" fullCmd="db:migrate:status" taksId="status" /><RakeTask description="" fullCmd="db:migrate:down" taksId="down" /><RakeTask description="" fullCmd="db:migrate:redo" taksId="redo" /><RakeTask description="" fullCmd="db:migrate:reset" taksId="reset" /><RakeTask description="" fullCmd="db:migrate:up" taksId="up" /></RakeGroup><RakeTask description="Rolls the schema back to the previous version (specify steps w/ STEP=n)" fullCmd="db:rollback" taksId="rollback" /><RakeGroup description="" fullCmd="" taksId="schema"><RakeGroup description="" fullCmd="" taksId="cache"><RakeTask description="Clears a db/schema_cache.dump file" fullCmd="db:schema:cache:clear" taksId="clear" /><RakeTask description="Creates a db/schema_cache.dump file" fullCmd="db:schema:cache:dump" taksId="dump" /></RakeGroup><RakeTask description="Creates a db/schema.rb file that is portable against any DB supported by Active Record" fullCmd="db:schema:dump" taksId="dump" /><RakeTask description="Loads a schema.rb file into the database" fullCmd="db:schema:load" taksId="load" /><RakeTask description="" fullCmd="db:schema:load_if_ruby" taksId="load_if_ruby" /></RakeGroup><RakeTask description="Loads the seed data from db/seeds.rb" fullCmd="db:seed" taksId="seed" /><RakeTask description="Creates the database, loads the schema, and initializes with the seed data (use db:reset to also drop the database first)" fullCmd="db:setup" taksId="setup" /><RakeGroup description="" fullCmd="" taksId="structure"><RakeTask description="Dumps the database structure to db/structure.sql" fullCmd="db:structure:dump" taksId="dump" /><RakeTask description="Recreates the databases from the structure.sql file" fullCmd="db:structure:load" taksId="load" /><RakeTask description="" fullCmd="db:structure:load_if_sql" taksId="load_if_sql" /></RakeGroup><RakeTask description="Retrieves the current schema version number" fullCmd="db:version" taksId="version" /><RakeTask description="" fullCmd="db:_dump" taksId="_dump" /><RakeTask description="" fullCmd="db:abort_if_pending_migrations" taksId="abort_if_pending_migrations" /><RakeTask description="" fullCmd="db:charset" taksId="charset" /><RakeTask description="" fullCmd="db:check_protected_environments" taksId="check_protected_environments" /><RakeTask description="" fullCmd="db:collation" taksId="collation" /><RakeGroup description="" fullCmd="" taksId="create"><RakeTask description="" fullCmd="db:create:all" taksId="all" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="drop"><RakeTask description="" fullCmd="db:drop:_unsafe" taksId="_unsafe" /><RakeTask description="" fullCmd="db:drop:all" taksId="all" /></RakeGroup><RakeTask description="" fullCmd="db:forward" taksId="forward" /><RakeTask description="" fullCmd="db:load_config" taksId="load_config" /><RakeTask description="" fullCmd="db:purge" taksId="purge" /><RakeGroup description="" fullCmd="" taksId="purge"><RakeTask description="" fullCmd="db:purge:all" taksId="all" /></RakeGroup><RakeTask description="" fullCmd="db:reset" taksId="reset" /><RakeGroup description="" fullCmd="" taksId="test"><RakeTask description="" fullCmd="db:test:clone" taksId="clone" /><RakeTask description="" fullCmd="db:test:clone_schema" taksId="clone_schema" /><RakeTask description="" fullCmd="db:test:clone_structure" taksId="clone_structure" /><RakeTask description="" fullCmd="db:test:deprecated" taksId="deprecated" /><RakeTask description="" fullCmd="db:test:load" taksId="load" /><RakeTask description="" fullCmd="db:test:load_schema" taksId="load_schema" /><RakeTask description="" fullCmd="db:test:load_structure" taksId="load_structure" /><RakeTask description="" fullCmd="db:test:prepare" taksId="prepare" /><RakeTask description="" fullCmd="db:test:purge" taksId="purge" /></RakeGroup></RakeGroup><RakeGroup description="" fullCmd="" taksId="dev"><RakeTask description="Toggle development mode caching on/off" fullCmd="dev:cache" taksId="cache" /></RakeGroup><RakeTask description="Print out all defined initializers in the order they are invoked by Rails" fullCmd="initializers" taksId="initializers" /><RakeGroup description="" fullCmd="" taksId="log"><RakeTask description="Truncates all/specified *.log files in log/ to zero bytes (specify which logs with LOGS=test,development)" fullCmd="log:clear" taksId="clear" /></RakeGroup><RakeTask description="Prints out your Rack middleware stack" fullCmd="middleware" taksId="middleware" /><RakeTask description="Enumerate all annotations (use notes:optimize, :fixme, :todo for focus)" fullCmd="notes" taksId="notes" /><RakeGroup description="" fullCmd="" taksId="notes"><RakeTask description="Enumerate a custom annotation, specify with ANNOTATION=CUSTOM" fullCmd="notes:custom" taksId="custom" /><RakeTask description="" fullCmd="notes:fixme" taksId="fixme" /><RakeTask description="" fullCmd="notes:optimize" taksId="optimize" /><RakeTask description="" fullCmd="notes:todo" taksId="todo" /></RakeGroup><RakeTask description="Restart app by touching tmp/restart.txt" fullCmd="restart" taksId="restart" /><RakeTask description="Print out all defined routes in match order, with names" fullCmd="routes" taksId="routes" /><RakeTask description="Generate a cryptographically secure secret key (this is typically used to generate a secret for cookie sessions)" fullCmd="secret" taksId="secret" /><RakeTask description="Report code statistics (KLOCs, etc) from the application or engine" fullCmd="stats" taksId="stats" /><RakeTask description="Runs all tests in test folder" fullCmd="test" taksId="test" /><RakeGroup description="" fullCmd="" taksId="test"><RakeTask description="Run tests quickly, but also reset db" fullCmd="test:db" taksId="db" /><RakeTask description="" fullCmd="test:controllers" taksId="controllers" /><RakeTask description="" fullCmd="test:functionals" taksId="functionals" /><RakeTask description="" fullCmd="test:generators" taksId="generators" /><RakeTask description="" fullCmd="test:helpers" taksId="helpers" /><RakeTask description="" fullCmd="test:integration" taksId="integration" /><RakeTask description="" fullCmd="test:jobs" taksId="jobs" /><RakeTask description="" fullCmd="test:mailers" taksId="mailers" /><RakeTask description="" fullCmd="test:models" taksId="models" /><RakeTask description="" fullCmd="test:prepare" taksId="prepare" /><RakeTask description="" fullCmd="test:run" taksId="run" /><RakeTask description="" fullCmd="test:units" taksId="units" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="time"><RakeTask description="List all time zones, list by two-letter country code (`rails time:zones[US]`), or list by UTC offset (`rails time:zones[-8]`)" fullCmd="time:zones[country_or_offset]" taksId="zones[country_or_offset]" /><RakeTask description="" fullCmd="time:zones" taksId="zones" /><RakeGroup description="" fullCmd="" taksId="zones"><RakeTask description="" fullCmd="time:zones:all" taksId="all" /><RakeTask description="" fullCmd="time:zones:local" taksId="local" /><RakeTask description="" fullCmd="time:zones:us" taksId="us" /></RakeGroup></RakeGroup><RakeGroup description="" fullCmd="" taksId="tmp"><RakeTask description="Clear cache and socket files from tmp/ (narrow w/ tmp:cache:clear, tmp:sockets:clear)" fullCmd="tmp:clear" taksId="clear" /><RakeTask description="Creates tmp directories for cache, sockets, and pids" fullCmd="tmp:create" taksId="create" /><RakeGroup description="" fullCmd="" taksId="cache"><RakeTask description="" fullCmd="tmp:cache:clear" taksId="clear" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="pids"><RakeTask description="" fullCmd="tmp:pids:clear" taksId="clear" /></RakeGroup><RakeGroup description="" fullCmd="" taksId="sockets"><RakeTask description="" fullCmd="tmp:sockets:clear" taksId="clear" /></RakeGroup></RakeGroup><RakeTask description="" fullCmd="default" taksId="default" /><RakeTask description="" fullCmd="environment" taksId="environment" /><RakeGroup description="" fullCmd="" taksId="rails"><RakeTask description="" fullCmd="rails:template" taksId="template" /><RakeGroup description="" fullCmd="" taksId="templates"><RakeTask description="" fullCmd="rails:templates:copy" taksId="copy" /></RakeGroup><RakeTask description="" fullCmd="rails:update" taksId="update" /><RakeGroup description="" fullCmd="" taksId="update"><RakeTask description="" fullCmd="rails:update:bin" taksId="bin" /><RakeTask description="" fullCmd="rails:update:configs" taksId="configs" /></RakeGroup></RakeGroup><RakeGroup description="" fullCmd="" taksId="railties"><RakeGroup description="" fullCmd="" taksId="install"><RakeTask description="" fullCmd="railties:install:migrations" taksId="migrations" /></RakeGroup></RakeGroup><RakeTask description="" fullCmd="tmp" taksId="tmp" /><RakeTask description="" fullCmd="tmp/cache" taksId="tmp/cache" /><RakeTask description="" fullCmd="tmp/cache/assets" taksId="tmp/cache/assets" /><RakeTask description="" fullCmd="tmp/pids" taksId="tmp/pids" /><RakeTask description="" fullCmd="tmp/sockets" taksId="tmp/sockets" /></RakeGroup></Settings>


File: /.idea\dataSources\134b62c8-28e1-41ba-a12f-db159a3fd8ea\storage.xml
<?xml version="1.0" encoding="UTF-8"?>
<storage-settings staging-layout="plain" base-layout="schema-zip" language="MySQL"/>

File: /.idea\dataSources\134b62c8-28e1-41ba-a12f-db159a3fd8ea.xml
<?xml version="1.0" encoding="UTF-8"?>
<dataSource name="ipriver_mikrotik_config_generator_development@localhost">
  <database-model serializer="dbm" rdbms="MYSQL" format-version="4.0">
    <root id="1"/>
    <schema id="2" parent="1" name="ipriver_mikrotik_config_generator_development">
      <Current>1</Current>
      <Visible>1</Visible>
    </schema>
    <schema id="3" parent="1" name="information_schema"/>
    <schema id="4" parent="1" name="ipriver_mikrotik_config_generator_test"/>
    <schema id="5" parent="1" name="mavencp_development"/>
    <schema id="6" parent="1" name="mavencp_test"/>
    <schema id="7" parent="1" name="mysql"/>
    <schema id="8" parent="1" name="performance_schema"/>
    <schema id="9" parent="1" name="vaf_development"/>
    <schema id="10" parent="1" name="vaf_test"/>
    <table id="11" parent="2" name="ar_internal_metadata"/>
    <table id="12" parent="2" name="config_templates"/>
    <table id="13" parent="2" name="configs"/>
    <table id="14" parent="2" name="interfaces"/>
    <table id="15" parent="2" name="schema_migrations"/>
    <column id="16" parent="11" name="key">
      <Position>1</Position>
      <DataType>varchar(255)|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="17" parent="11" name="value">
      <Position>2</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="18" parent="11" name="created_at">
      <Position>3</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="19" parent="11" name="updated_at">
      <Position>4</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <key id="20" parent="11" name="PRIMARY">
      <ColNames>key</ColNames>
      <Primary>1</Primary>
    </key>
    <column id="21" parent="12" name="id">
      <Position>1</Position>
      <DataType>int(11)|0</DataType>
      <NotNull>1</NotNull>
      <SequenceIdentity>1</SequenceIdentity>
    </column>
    <column id="22" parent="12" name="name">
      <Position>2</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="23" parent="12" name="description">
      <Position>3</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="24" parent="12" name="config_text">
      <Position>4</Position>
      <DataType>text|0</DataType>
    </column>
    <column id="25" parent="12" name="created_at">
      <Position>5</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="26" parent="12" name="updated_at">
      <Position>6</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <key id="27" parent="12" name="PRIMARY">
      <ColNames>id</ColNames>
      <Primary>1</Primary>
    </key>
    <column id="28" parent="13" name="id">
      <Position>1</Position>
      <DataType>int(11)|0</DataType>
      <NotNull>1</NotNull>
      <SequenceIdentity>1</SequenceIdentity>
    </column>
    <column id="29" parent="13" name="system_name">
      <Position>2</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="30" parent="13" name="password">
      <Position>3</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="31" parent="13" name="snmp_community">
      <Position>4</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="32" parent="13" name="snmp_address">
      <Position>5</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="33" parent="13" name="snmp_contact">
      <Position>6</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="34" parent="13" name="snmp_location">
      <Position>7</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="35" parent="13" name="created_at">
      <Position>8</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="36" parent="13" name="updated_at">
      <Position>9</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="37" parent="13" name="template_id">
      <Position>10</Position>
      <DataType>int(11)|0</DataType>
    </column>
    <column id="38" parent="13" name="config_template_id">
      <Position>11</Position>
      <DataType>int(11)|0</DataType>
    </column>
    <index id="39" parent="13" name="index_configs_on_config_template_id">
      <ColNames>config_template_id</ColNames>
    </index>
    <index id="40" parent="13" name="index_configs_on_template_id">
      <ColNames>template_id</ColNames>
    </index>
    <key id="41" parent="13" name="PRIMARY">
      <ColNames>id</ColNames>
      <Primary>1</Primary>
    </key>
    <foreign-key id="42" parent="13" name="fk_rails_2d7a2705ff">
      <ColNames>config_template_id</ColNames>
      <RefSchemaName>ipriver_mikrotik_config_generator_development</RefSchemaName>
      <RefTableName>config_templates</RefTableName>
      <RefColNames>id</RefColNames>
    </foreign-key>
    <column id="43" parent="14" name="id">
      <Position>1</Position>
      <DataType>int(11)|0</DataType>
      <NotNull>1</NotNull>
      <SequenceIdentity>1</SequenceIdentity>
    </column>
    <column id="44" parent="14" name="name">
      <Position>2</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="45" parent="14" name="ip">
      <Position>3</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="46" parent="14" name="subnet">
      <Position>4</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="47" parent="14" name="gateway">
      <Position>5</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="48" parent="14" name="username">
      <Position>6</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="49" parent="14" name="password">
      <Position>7</Position>
      <DataType>varchar(255)|0</DataType>
    </column>
    <column id="50" parent="14" name="created_at">
      <Position>8</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="51" parent="14" name="updated_at">
      <Position>9</Position>
      <DataType>datetime|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <column id="52" parent="14" name="config_id">
      <Position>10</Position>
      <DataType>int(11)|0</DataType>
    </column>
    <index id="53" parent="14" name="index_interfaces_on_config_id">
      <ColNames>config_id</ColNames>
    </index>
    <key id="54" parent="14" name="PRIMARY">
      <ColNames>id</ColNames>
      <Primary>1</Primary>
    </key>
    <foreign-key id="55" parent="14" name="fk_rails_87ce365f4e">
      <ColNames>config_id</ColNames>
      <RefSchemaName>ipriver_mikrotik_config_generator_development</RefSchemaName>
      <RefTableName>configs</RefTableName>
      <RefColNames>id</RefColNames>
    </foreign-key>
    <column id="56" parent="15" name="version">
      <Position>1</Position>
      <DataType>varchar(255)|0</DataType>
      <NotNull>1</NotNull>
    </column>
    <key id="57" parent="15" name="PRIMARY">
      <ColNames>version</ColNames>
      <Primary>1</Primary>
    </key>
  </database-model>
</dataSource>

File: /.idea\dataSources.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="DataSourceManagerImpl" format="xml" multifile-model="true">
    <data-source source="LOCAL" name="ipriver_mikrotik_config_generator_development@localhost" uuid="134b62c8-28e1-41ba-a12f-db159a3fd8ea">
      <driver-ref>mysql</driver-ref>
      <synchronize>true</synchronize>
      <jdbc-driver>com.mysql.jdbc.Driver</jdbc-driver>
      <jdbc-url>jdbc:mysql://localhost:3306/ipriver_mikrotik_config_generator_development</jdbc-url>
      <driver-properties>
        <property name="autoReconnect" value="true" />
        <property name="zeroDateTimeBehavior" value="convertToNull" />
        <property name="tinyInt1isBit" value="false" />
        <property name="characterEncoding" value="utf8" />
        <property name="characterSetResults" value="utf8" />
        <property name="yearIsDateType" value="false" />
      </driver-properties>
    </data-source>
  </component>
</project>

File: /.idea\encodings.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Encoding">
    <file url="PROJECT" charset="UTF-8" />
  </component>
</project>

File: /.idea\ipriver_mikrotik_config_generator.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="RUBY_MODULE" version="4">
  <component name="FacetManager">
    <facet type="RailsFacetType" name="Ruby on Rails">
      <configuration>
        <RAILS_FACET_CONFIG_ID NAME="RAILS_FACET_SUPPORT_REMOVED" VALUE="false" />
        <RAILS_FACET_CONFIG_ID NAME="RAILS_TESTS_SOURCES_PATCHED" VALUE="true" />
        <RAILS_FACET_CONFIG_ID NAME="RAILS_FACET_APPLICATION_ROOT" VALUE="$MODULE_DIR$" />
      </configuration>
    </facet>
  </component>
  <component name="ModuleRunConfigurationManager">
    <configuration default="false" name="test: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs>
        <env name="RAILS_ENV" value="test" />
      </envs>
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="test" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE=":test_unit " />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="spec: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs />
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="spec" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE=":rspec " />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="Production: ipriver_mikrotik_config_generator" type="RailsRunConfigurationType" factoryName="Rails">
      <predefined_log_file id="RUBY_RAILS_SERVER" enabled="true" />
      <module name="ipriver_mikrotik_config_generator" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs />
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SCRIPT_ARGS" VALUE="" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="PORT" VALUE="3000" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="IP" VALUE="0.0.0.0" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="DUMMY_APP" VALUE="test/dummy" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RAILS_SERVER_TYPE" VALUE="Default" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ENVIRONMENT_TYPE" VALUE="production" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="LAUNCH_JS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="Development: ipriver_mikrotik_config_generator" type="RailsRunConfigurationType" factoryName="Rails">
      <predefined_log_file id="RUBY_RAILS_SERVER" enabled="true" />
      <module name="ipriver_mikrotik_config_generator" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs />
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SCRIPT_ARGS" VALUE="" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="PORT" VALUE="3000" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="IP" VALUE="0.0.0.0" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="DUMMY_APP" VALUE="test/dummy" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RAILS_SERVER_TYPE" VALUE="Default" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ENVIRONMENT_TYPE" VALUE="development" />
      <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="LAUNCH_JS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="db:create: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake" temporary="true">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs>
        <env name="RAILS_ENV" value="development" />
      </envs>
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="db:create" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="db:drop: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake" temporary="true">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs>
        <env name="RAILS_ENV" value="development" />
      </envs>
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="db:drop" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="db:seed: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake" temporary="true">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs />
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="db:seed" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="db:schema:load: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake" temporary="true">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs>
        <env name="RAILS_ENV" value="development" />
      </envs>
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="db:schema:load" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
    <configuration default="false" name="db:setup: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake" temporary="true">
      <module name="ipriver_mikrotik_config_generator" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
      <envs />
      <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
      <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
      <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
        <COVERAGE_PATTERN ENABLED="true">
          <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
        </COVERAGE_PATTERN>
      </EXTENSION>
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="db:setup" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE="" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
      <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
      <method />
    </configuration>
  </component>
  <component name="NewModuleRootManager">
    <content url="file://$MODULE_DIR$">
      <sourceFolder url="file://$MODULE_DIR$/test" isTestSource="true" />
      <sourceFolder url="file://$MODULE_DIR$/spec" isTestSource="true" />
      <excludeFolder url="file://$MODULE_DIR$/.bundle" />
      <excludeFolder url="file://$MODULE_DIR$/components" />
      <excludeFolder url="file://$MODULE_DIR$/public/system" />
      <excludeFolder url="file://$MODULE_DIR$/tmp" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/bundle" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
    <orderEntry type="library" scope="PROVIDED" name="actioncable (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="actionmailer (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="actionpack (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="actionview (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="activejob (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="activemodel (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="activerecord (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="activesupport (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="arel (v7.1.4, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="builder (v3.2.3, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="bundler (v1.11.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="coffee-rails (v4.2.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="coffee-script (v2.4.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="coffee-script-source (v1.12.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="concurrent-ruby (v1.0.4, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="erubis (v2.7.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="execjs (v2.7.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="ffi (v1.9.17, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="globalid (v0.3.7, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="i18n (v0.7.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="ipaddress (v0.8.3, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="jquery-rails (v4.2.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="listen (v3.0.8, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="loofah (v2.0.3, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="mail (v2.6.4, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="method_source (v0.8.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="mime-types (v3.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="mime-types-data (v3.2016.0521, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="mini_portile2 (v2.1.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="multi_json (v1.12.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="mysql2 (v0.4.5, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="nio4r (v1.2.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="nokogiri (v1.7.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="puma (v3.6.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rack (v2.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rack-test (v0.6.3, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rails (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rails-dom-testing (v2.0.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rails-html-sanitizer (v1.0.3, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="railties (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rb-fsevent (v0.9.8, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="rb-inotify (v0.9.7, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="ref (v2.0.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="sass (v3.4.23, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="sass-rails (v5.0.6, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="spring (v2.0.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="spring-watcher-listen (v2.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="sprockets (v3.7.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="sprockets-rails (v3.2.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="thread_safe (v0.3.5, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="tilt (v2.0.5, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="turbolinks (v5.0.1, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="turbolinks-source (v5.0.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="tzinfo (v1.2.2, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="web-console (v3.4.0, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="websocket-driver (v0.6.4, RVM: ruby-2.3.3) [gem]" level="application" />
    <orderEntry type="library" scope="PROVIDED" name="websocket-extensions (v0.1.2, RVM: ruby-2.3.3) [gem]" level="application" />
  </component>
  <component name="RModuleSettingsStorage">
    <LOAD_PATH number="0" />
    <I18N_FOLDERS number="1" string0="$MODULE_DIR$/config/locales" />
  </component>
  <component name="Warbler" number="1" string0="true" />
</module>

File: /.idea\misc.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectRootManager" version="2" project-jdk-name="RVM: ruby-2.3.3" project-jdk-type="RUBY_SDK" />
</project>

File: /.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /.idea\runConfigurations\Development__ipriver_mikrotik_config_generator.xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Development: ipriver_mikrotik_config_generator" type="RailsRunConfigurationType" factoryName="Rails">
    <predefined_log_file id="RUBY_RAILS_SERVER" enabled="true" />
    <module name="ipriver_mikrotik_config_generator" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
    <envs />
    <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
    <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
    <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
      <COVERAGE_PATTERN ENABLED="true">
        <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
      </COVERAGE_PATTERN>
    </EXTENSION>
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SCRIPT_ARGS" VALUE="" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="PORT" VALUE="3000" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="IP" VALUE="0.0.0.0" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="DUMMY_APP" VALUE="test/dummy" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RAILS_SERVER_TYPE" VALUE="Default" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ENVIRONMENT_TYPE" VALUE="development" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="LAUNCH_JS" VALUE="false" />
    <method />
  </configuration>
</component>

File: /.idea\runConfigurations\Production__ipriver_mikrotik_config_generator.xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Production: ipriver_mikrotik_config_generator" type="RailsRunConfigurationType" factoryName="Rails">
    <predefined_log_file id="RUBY_RAILS_SERVER" enabled="true" />
    <module name="ipriver_mikrotik_config_generator" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
    <envs />
    <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
    <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
    <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
      <COVERAGE_PATTERN ENABLED="true">
        <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
      </COVERAGE_PATTERN>
    </EXTENSION>
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="SCRIPT_ARGS" VALUE="" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="PORT" VALUE="3000" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="IP" VALUE="0.0.0.0" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="DUMMY_APP" VALUE="test/dummy" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="RAILS_SERVER_TYPE" VALUE="Default" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="ENVIRONMENT_TYPE" VALUE="production" />
    <RAILS_SERVER_CONFIG_SETTINGS_ID NAME="LAUNCH_JS" VALUE="false" />
    <method />
  </configuration>
</component>

File: /.idea\runConfigurations\spec__ipriver_mikrotik_config_generator.xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="spec: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake">
    <module name="ipriver_mikrotik_config_generator" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
    <envs />
    <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
    <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
    <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
      <COVERAGE_PATTERN ENABLED="true">
        <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
      </COVERAGE_PATTERN>
    </EXTENSION>
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="spec" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE=":rspec " />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
    <method />
  </configuration>
</component>

File: /.idea\runConfigurations\test__ipriver_mikrotik_config_generator.xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="test: ipriver_mikrotik_config_generator" type="RakeRunConfigurationType" factoryName="Rake">
    <module name="ipriver_mikrotik_config_generator" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RUBY_ARGS" VALUE="-e $stdout.sync=true;$stderr.sync=true;load($0=ARGV.shift)" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="WORK DIR" VALUE="$MODULE_DIR$" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="SHOULD_USE_SDK" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="ALTERN_SDK_NAME" VALUE="" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="myPassParentEnvs" VALUE="true" />
    <envs>
      <env name="RAILS_ENV" value="test" />
    </envs>
    <EXTENSION ID="BundlerRunConfigurationExtension" bundleExecEnabled="false" />
    <EXTENSION ID="JRubyRunConfigurationExtension" NailgunExecEnabled="false" />
    <EXTENSION ID="RubyCoverageRunConfigurationExtension" enabled="false" sample_coverage="true" track_test_folders="true" runner="rcov">
      <COVERAGE_PATTERN ENABLED="true">
        <PATTERN REGEXPS="/.rvm/" INCLUDED="false" />
      </COVERAGE_PATTERN>
    </EXTENSION>
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_NAME" VALUE="test" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ARGS" VALUE="" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_ATTACHED_TEST_FRAMEWORKS" VALUE=":test_unit " />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_TRACE" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_DRYRUN" VALUE="false" />
    <RAKE_RUN_CONFIG_SETTINGS_ID NAME="RAKE_TASK_OPTION_PREREQS" VALUE="false" />
    <method />
  </configuration>
</component>

File: /.idea\vagrant.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VagrantProjectSettings">
    <option name="instanceFolder" value="" />
    <option name="provider" value="" />
  </component>
</project>

File: /.idea\vcs.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="$PROJECT_DIR$" vcs="Git" />
  </component>
</project>

File: /app\assets\config\manifest.js
//= link_tree ../images
//= link_directory ../javascripts .js
//= link_directory ../stylesheets .css


File: /app\assets\javascripts\application.js
// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or any plugin's vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file. JavaScript code in this file should be added after the last require_* statement.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require turbolinks
//= require_tree .


File: /app\assets\javascripts\cable.js
// Action Cable provides the framework to deal with WebSockets in Rails.
// You can generate new channels where WebSocket features live using the rails generate channel command.
//
//= require action_cable
//= require_self
//= require_tree ./channels

(function() {
  this.App || (this.App = {});

  App.cable = ActionCable.createConsumer();

}).call(this);


File: /app\assets\javascripts\configs.coffee
# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/
$(document).on "turbolinks:load", ->
    console.log("Script loaded")
    $("#config_interfaces_attributes_0_interface_type,#config_interfaces_attributes_1_interface_type,#config_interfaces_attributes_2_interface_type").on "change", ->
      console.log("Interface type changed")
      i = 0
      while (i < 3)
        if $("#config_interfaces_attributes_#{i}_interface_type").val() is "ppp"
          console.log("Interface #{$(this).id} type is PPP")
          $("#config_interfaces_attributes_#{i}_ip").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_subnet").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_gateway").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_username").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_password").attr("disabled", false)
        if $("#config_interfaces_attributes_#{i}_interface_type").val() in ['ethernet-wan','sfp-wan']
          console.log("Interface #{$(this).id} type is ethernet-wan")
          $("#config_interfaces_attributes_#{i}_ip").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_subnet").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_gateway").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_username").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_password").attr("disabled", true)
        if $("#config_interfaces_attributes_#{i}_interface_type").val() is "ethernet-lan"
          console.log("Interface #{$(this).id} type is ethernet-lan")
          $("#config_interfaces_attributes_#{i}_ip").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_subnet").attr("disabled", false)
          $("#config_interfaces_attributes_#{i}_gateway").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_username").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_password").attr("disabled", true)
        if $("#config_interfaces_attributes_#{i}_interface_type").val() is "unused"
          console.log("Interface #{$(this).id} type is unused")
          $("#config_interfaces_attributes_#{i}_ip").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_subnet").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_gateway").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_username").attr("disabled", true)
          $("#config_interfaces_attributes_#{i}_password").attr("disabled", true)
        i++
return

File: /app\assets\javascripts\config_templates.coffee
# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/


File: /app\assets\javascripts\home.coffee
# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/


File: /app\assets\javascripts\interfaces.coffee
# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/


File: /app\assets\stylesheets\application.css
/*
 * This is a manifest file that'll be compiled into application.css, which will include all the files
 * listed below.
 *
 * Any CSS and SCSS file within this directory, lib/assets/stylesheets, vendor/assets/stylesheets,
 * or any plugin's vendor/assets/stylesheets directory can be referenced here using a relative path.
 *
 * You're free to add application-wide styles to this file and they'll appear at the bottom of the
 * compiled file so the styles you add here take precedence over styles defined in any other CSS/SCSS
 * files in this directory. Styles in this file should be added after the last require_* statement.
 * It is generally better to create a new file per style scope.
 *
 *= require_tree .
 *= require_self
 */


File: /app\assets\stylesheets\configs.scss
// Place all the styles related to the Configs controller here.
// They will automatically be included in application.css.
// You can use Sass (SCSS) here: http://sass-lang.com/


File: /app\assets\stylesheets\config_templates.scss
// Place all the styles related to the ConfigTemplates controller here.
// They will automatically be included in application.css.
// You can use Sass (SCSS) here: http://sass-lang.com/


File: /app\assets\stylesheets\custom.css
footer {
    width: 100%;
    bottom: 0;
    position: fixed;
    background-color: #999999;
}

File: /app\assets\stylesheets\home.scss
// Place all the styles related to the home controller here.
// They will automatically be included in application.css.
// You can use Sass (SCSS) here: http://sass-lang.com/


File: /app\assets\stylesheets\interfaces.scss
// Place all the styles related to the Interfaces controller here.
// They will automatically be included in application.css.
// You can use Sass (SCSS) here: http://sass-lang.com/


File: /app\assets\stylesheets\scaffolds.scss
body {
  background-color: #fff;
  color: #333;
  font-family: verdana, arial, helvetica, sans-serif;
  font-size: 13px;
  line-height: 18px;
  margin: 33px;
}

p, ol, ul, td {
  font-family: verdana, arial, helvetica, sans-serif;
  font-size: 13px;
  line-height: 18px;
  margin: 33px;
}

pre {
  background-color: #eee;
  padding: 10px;
  font-size: 11px;
}

a {
  color: #000;

  &:visited {
    color: #666;
  }

  &:hover {
    color: #fff;
    background-color: #000;
  }
}

th {
  padding-bottom: 5px;
}

td {
  padding-bottom: 7px;
  padding-left: 5px;
  padding-right: 5px;
}

div {
  &.field, &.actions {
    margin-bottom: 10px;
  }
}

#notice {
  color: green;
}

.field_with_errors {
  padding: 2px;
  background-color: red;
  display: table;
}

#error_explanation {
  width: 450px;
  border: 2px solid red;
  padding: 7px;
  padding-bottom: 0;
  margin-bottom: 20px;
  background-color: #f0f0f0;

  h2 {
    text-align: left;
    font-weight: bold;
    padding: 5px 5px 5px 15px;
    font-size: 12px;
    margin: -7px;
    margin-bottom: 0;
    background-color: #c00;
    color: #fff;
  }

  ul li {
    font-size: 12px;
    list-style: square;
  }
}

label {
  display: block;
}


File: /app\channels\application_cable\channel.rb
module ApplicationCable
  class Channel < ActionCable::Channel::Base
  end
end


File: /app\channels\application_cable\connection.rb
module ApplicationCable
  class Connection < ActionCable::Connection::Base
  end
end


File: /app\controllers\application_controller.rb
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
end


File: /app\controllers\concerns\config_generator.rb
module ConfigGenerator
  def generate_rsc(config)
    @config = Config.find(config)
    @output = "/system identity set name=#{@config.system_name}\n"
    @output << "/user set admin password=#{@config.password}\n"
    @output << "/snmp\nset contact=\"#{@config.snmp_contact}\"\nset enabled=yes\nset location=\"#{@config.snmp_location}\"\ncommunity\nset numbers=0 address=\"#{@config.snmp_address}\"\nset numbers=0 name=\"#{@config.snmp_community}\"\n"
    @output << @config.config_template.config_text + "\n"
    # First interface definition
    if @config.interfaces.first.interface_type == 'ethernet-wan' || @config.interfaces.first.interface_type == 'sfp-wan'
      @output << "/ip address add address=#{@config.interfaces.first.ip}/#{@config.interfaces.first.subnet} comment=WAN interface=ether1\n"
      @output << "/ip route add dst-address=0.0.0.0 gateway=#{@config.interfaces.first.gateway}\n"
      @output << "/ip firewall filter\n"
      @output << "add action=accept chain=input comment=\"Remote admin\" dst-port=8291 protocol=tcp in-interface=ether1\n"
      @output << "add action=accept chain=input comment=\"SNMP\" dst-port=161 protocol=udp in-interface=ether1\n"
      @output << "add action=drop chain=input comment=\"defconf: drop all from WAN\" in-interface=ether1\n"
    elsif @config.interfaces.first.interface_type == 'ppp'
      @output << "/interface pppoe-client add name=WAN user=#{@config.interfaces.first.username} password=#{@config.interfaces.first.password} interface=ether1 disabled=no add-default-route=yes\n"
      @output << "/ip address add address=#{@config.interfaces.second.ip}/#{@config.interfaces.second.subnet} comment=LAN interface=ether2-master\n"
      @output << "/ip dns static add address=#{@config.interfaces.second.ip} name=router\n"
      @output << "/ip firewall filter\n"
      @output << "add action=accept chain=input comment=\"Remote admin\" dst-port=8291 protocol=tcp in-interface=WAN\n"
      @output << "add action=accept chain=input comment=\"SNMP\" dst-port=161 protocol=udp in-interface=WAN\n"
      @output << "add action=drop chain=input comment=\"defconf: drop all from WAN\" in-interface=WAN\n"
    end
    # Second interface definition
    if @config.interfaces.second.interface_type == 'ethernet-lan'
      @output << "/ip address add address=#{@config.interfaces.second.ip}/#{@config.interfaces.second.subnet} comment=LAN interface=ether2-master\n"
      @output << "/ip dns static add address=#{@config.interfaces.second.ip} name=router\n"
    end
    # Third interface definition
    if @config.interfaces.third.interface_type == 'ethernet-lan'
      @output << "/ip address add address=#{@config.interfaces.third.ip}/#{@config.interfaces.third.subnet} comment=LAN interface=ether3\n"
      @output << "/ip dns static add address=#{@config.interfaces.third.ip} name=router\n"
    end
    return @output
  end
end

File: /app\controllers\configs_controller.rb
class ConfigsController < ApplicationController
  before_action :set_config, only: [:show, :edit, :update, :destroy, :generate]
  include ConfigGenerator

  # GET /configs
  # GET /configs.json
  def index
    @configs = Config.all
  end

  # GET /configs/1
  # GET /configs/1.json
  def show
  end

  # GET /configs/new
  def new
    @config = Config.new
    3.times do
      @config.interfaces.build
    end
  end

  # GET /configs/1/edit
  def edit
  end

  # POST /configs
  # POST /configs.json
  def create
    @config = Config.new(config_params)

    respond_to do |format|
      if @config.save
        format.html { redirect_to @config, notice: 'Config was successfully created.' }
        format.json { render :show, status: :created, location: @config }
      else
        format.html { render :new }
        format.json { render json: @config.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /configs/1
  # PATCH/PUT /configs/1.json
  def update
    respond_to do |format|
      if @config.update(config_params)
        format.html { redirect_to @config, notice: 'Config was successfully updated.' }
        format.json { render :show, status: :ok, location: @config }
      else
        format.html { render :edit }
        format.json { render json: @config.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /configs/1
  # DELETE /configs/1.json
  def destroy
    @config.destroy
    respond_to do |format|
      format.html { redirect_to configs_url, notice: 'Config was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  # GENERATE /configs/1/generate
  def generate
    send_data generate_rsc(@config), :filename => "#{@config.system_name}.rsc"
    # redirect_to @config, notice: 'Config generated'
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_config
      @config = Config.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def config_params
      params.require(:config).permit(:config_template_id, :system_name, :password, :snmp_community, :snmp_address, :snmp_contact, :snmp_location, interfaces_attributes: [:id, :name, :config_id, :interface_type, :ip, :subnet, :gateway, :username, :password])
    end
end


File: /app\controllers\config_templates_controller.rb
class ConfigTemplatesController < ApplicationController
  before_action :set_config_template, only: [:show, :edit, :update, :destroy]

  # GET /config_templates
  # GET /config_templates.json
  def index
    @config_templates = ConfigTemplate.all
  end

  # GET /config_templates/1
  # GET /config_templates/1.json
  def show
  end

  # GET /config_templates/new
  def new
    @config_template = ConfigTemplate.new
  end

  # GET /config_templates/1/edit
  def edit
  end

  # POST /config_templates
  # POST /config_templates.json
  def create
    @config_template = ConfigTemplate.new(config_template_params)

    respond_to do |format|
      if @config_template.save
        format.html { redirect_to @config_template, notice: 'Config template was successfully created.' }
        format.json { render :show, status: :created, location: @config_template }
      else
        format.html { render :new }
        format.json { render json: @config_template.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /config_templates/1
  # PATCH/PUT /config_templates/1.json
  def update
    respond_to do |format|
      if @config_template.update(config_template_params)
        format.html { redirect_to @config_template, notice: 'Config template was successfully updated.' }
        format.json { render :show, status: :ok, location: @config_template }
      else
        format.html { render :edit }
        format.json { render json: @config_template.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /config_templates/1
  # DELETE /config_templates/1.json
  def destroy
    @config_template.destroy
    respond_to do |format|
      format.html { redirect_to config_templates_url, notice: 'Config template was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_config_template
      @config_template = ConfigTemplate.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def config_template_params
      params.require(:config_template).permit(:name, :description, :config_text)
    end
end


File: /app\controllers\home_controller.rb
class HomeController < ApplicationController
  def index
  end
end


File: /app\controllers\interfaces_controller.rb
class InterfacesController < ApplicationController
  before_action :set_interface, only: [:show, :edit, :update, :destroy]

  # GET /interfaces
  # GET /interfaces.json
  def index
    @interfaces = Interface.all
  end

  # GET /interfaces/1
  # GET /interfaces/1.json
  def show
  end

  # GET /interfaces/new
  def new
    @interface = Interface.new
  end

  # GET /interfaces/1/edit
  def edit
  end

  # POST /interfaces
  # POST /interfaces.json
  def create
    @interface = Interface.new(interface_params)

    respond_to do |format|
      if @interface.save
        format.html { redirect_to @interface, notice: 'Interface was successfully created.' }
        format.json { render :show, status: :created, location: @interface }
      else
        format.html { render :new }
        format.json { render json: @interface.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /interfaces/1
  # PATCH/PUT /interfaces/1.json
  def update
    respond_to do |format|
      if @interface.update(interface_params)
        format.html { redirect_to @interface, notice: 'Interface was successfully updated.' }
        format.json { render :show, status: :ok, location: @interface }
      else
        format.html { render :edit }
        format.json { render json: @interface.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /interfaces/1
  # DELETE /interfaces/1.json
  def destroy
    @interface.destroy
    respond_to do |format|
      format.html { redirect_to interfaces_url, notice: 'Interface was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_interface
      @interface = Interface.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def interface_params
      params.require(:interface).permit(:config_id, :interface_type, :name, :ip, :subnet, :gateway, :username, :password)
    end
end


File: /app\helpers\application_helper.rb
module ApplicationHelper
end


File: /app\helpers\configs_helper.rb
module ConfigsHelper
end


File: /app\helpers\config_templates_helper.rb
module ConfigTemplatesHelper
end


File: /app\helpers\home_helper.rb
module HomeHelper
end


File: /app\helpers\interfaces_helper.rb
module InterfacesHelper
end


File: /app\jobs\application_job.rb
class ApplicationJob < ActiveJob::Base
end


File: /app\mailers\application_mailer.rb
class ApplicationMailer < ActionMailer::Base
  default from: 'from@example.com'
  layout 'mailer'
end


File: /app\models\application_record.rb
class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true
end


File: /app\models\config.rb
class Config < ApplicationRecord
  belongs_to :config_template
  has_many :interfaces, autosave: true, :inverse_of => :config, dependent: :destroy

  accepts_nested_attributes_for :interfaces

  validate :real_snmp_address

  validates :snmp_community, :snmp_contact, :snmp_location, :password, :system_name, presence: true

  def real_snmp_address
    if snmp_address.present? and not IPAddress.valid? snmp_address
      errors.add(:snmp_address, "Not valid SNMP address")
    end
  end
end


File: /app\models\config_template.rb
class ConfigTemplate < ApplicationRecord
  has_many :configs

  validates :name, :description, :config_text, presence: true
end


File: /app\models\interface.rb
class Interface < ApplicationRecord
  belongs_to :config

  TYPE = ['unused','ppp','ethernet-wan','ethernet-lan','sfp-wan']

  with_options if: "interface_type == 'ethernet-wan'" || "interface_type == 'sfp-wan'" do |ethernet|
    ethernet.validates :ip, :subnet, :gateway, presence: true
  end

  with_options if: "interface_type == 'ethernet-lan'" do |ethernet|
    ethernet.validates :ip, :subnet, presence: true
  end

  with_options if: "interface_type == 'ppp'" do |ppp|
      ppp.validates :username, :password, presence: true
  end

  validate :real_ip_address, :real_gateway_address, :real_subnet_definition

  def real_ip_address
    if ip.present? and not IPAddress.valid? ip
      errors.add(:ip, "Not valid IP address")
    end
  end

  def real_gateway_address
    if gateway.present? and not IPAddress.valid? gateway
      errors.add(:gateway, "Not valid gateway address")
    end
  end

  def real_subnet_definition
    if subnet.present? and not subnet.is_a? Integer and not subnet.length == 2
      errors.add(:subnet, "Not a valid subnet, use CIDR notation")
    end
  end
end


File: /app\views\configs\edit.html.erb
<h1>Editing Config</h1>

<%= render 'form', config: @config %>

<%= link_to 'Show', @config %> |
<%= link_to 'Back', configs_path %>


File: /app\views\configs\index.html.erb
<p id="notice"><%= notice %></p>

<h1>Configs</h1>

<table>
  <thead>
    <tr>
      <th>System name</th>
      <th>Password</th>
      <th>Snmp community</th>
      <th>Snmp address</th>
      <th>Snmp contact</th>
      <th>Snmp location</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @configs.each do |config| %>
      <tr>
        <td><%= config.system_name %></td>
        <td><%= config.password %></td>
        <td><%= config.snmp_community %></td>
        <td><%= config.snmp_address %></td>
        <td><%= config.snmp_contact %></td>
        <td><%= config.snmp_location %></td>
        <td><%= link_to 'Show', config %></td>
        <td><%= link_to 'Edit', edit_config_path(config) %></td>
        <td><%= link_to 'Delete', config, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<br>

<%= link_to 'New Config', new_config_path %>


File: /app\views\configs\index.json.jbuilder
json.array! @configs, partial: 'configs/config', as: :config

File: /app\views\configs\new.html.erb
<h1>New Config</h1>

<%= render 'form', config: @config %>

<%= link_to 'Back', configs_path %>


File: /app\views\configs\show.html.erb
<p id="notice"><%= notice %></p>

<p>
  <strong>System name:</strong>
  <%= @config.system_name %>
</p>

<p>
  <strong>Password:</strong>
  <%= @config.password %>
</p>

<p>
  <strong>Snmp community:</strong>
  <%= @config.snmp_community %>
</p>

<p>
  <strong>Snmp address:</strong>
  <%= @config.snmp_address %>
</p>

<p>
  <strong>Snmp contact:</strong>
  <%= @config.snmp_contact %>
</p>

<p>
  <strong>Snmp location:</strong>
  <%= @config.snmp_location %>
</p>

<table><tr>
  <th>Name</th>
  <th>Type</th>
  <th>IP</th>
  <th>Subnet</th>
  <th>Gateway</th>
  <th>Username</th>
  <th>Password</th>
</tr>
  <% @config.interfaces.each do |i| %>
      <tr>
        <td><%= i.name %></td>
        <td><%= i.interface_type %></td>
        <td><%= i.ip %></td>
        <td><%= i.subnet %></td>
        <td><%= i.gateway %></td>
        <td><%= i.username %></td>
        <td><%= i.password %></td>
      </tr>
  <% end %>
</table>
</table>

<%= link_to 'Edit', edit_config_path(@config) %> |
<%= link_to 'Back', configs_path %> |
<%= link_to 'Generate', generate_config_path %>


File: /app\views\configs\show.json.jbuilder
json.partial! "configs/config", config: @config

File: /app\views\configs\_config.json.jbuilder
json.extract! config, :id, :system_name, :password, :snmp_community, :snmp_address, :snmp_contact, :snmp_location, :created_at, :updated_at
json.url config_url(config, format: :json)

File: /app\views\configs\_form.html.erb
<%= form_for(config) do |f| %>
  <% if config.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(config.errors.count, "error") %> prohibited this config from being saved:</h2>

      <ul>
      <% config.errors.full_messages.each do |message| %>
        <li><%= message %></li>
      <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= f.label :config_template_id %>
    <%= f.collection_select :config_template_id, ConfigTemplate.all, :id, :name, :prompt => "Select a template" %>
  </div>

  <div class="field">
    <%= f.label :system_name %>
    <%= f.text_field :system_name %>
  </div>

  <div class="field">
    <%= f.label :password %>
    <%= f.text_field :password %>
  </div>

  <div class="field">
    <%= f.label :snmp_community %>
    <%= f.text_field :snmp_community %>
  </div>

  <div class="field">
    <%= f.label :snmp_address %>
    <%= f.text_field :snmp_address %>
  </div>

  <div class="field">
    <%= f.label :snmp_contact %>
    <%= f.text_field :snmp_contact %>
  </div>

  <div class="field">
    <%= f.label :snmp_location %>
    <%= f.text_field :snmp_location %>
  </div>

  <fieldset>
    <table>
    <%= f.fields_for :interfaces do |q| %>
      <tr>
        <td><%= "ether#{q.index + 1}" %></td>
        <%= q.hidden_field :name, :value => "ether#{q.index + 1}" %>
        <td><%= q.label :interface_type %></td>
        <td><%= q.select :interface_type, Interface::TYPE, :prompt => "Select interface type" %></td>
        <td><%= q.label :ip %></td>
        <td><%= q.text_field :ip %></td>
        <td><%= q.label :subnet %></td>
        <td><%= q.text_field :subnet %></td>
        <td><%= q.label :gateway %></td>
        <td><%= q.text_field :gateway %></td>
        <td><%= q.label :username %></td>
        <td><%= q.text_field :username %></td>
        <td><%= q.label :password %></td>
        <td><%= q.text_field :password %></td>
      </tr>
    <% end %>
    </table>
  </fieldset>
  <br>
  <div class="actions">
    <%= f.submit %>
  </div>
<% end %>


File: /app\views\config_templates\edit.html.erb
<h1>Editing Config Template</h1>

<%= render 'form', config_template: @config_template %>

<%= link_to 'Show', @config_template %> |
<%= link_to 'Back', config_templates_path %>


File: /app\views\config_templates\index.html.erb
<p id="notice"><%= notice %></p>

<h1>Config Templates</h1>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @config_templates.each do |config_template| %>
      <tr>
        <td><%= config_template.name %></td>
        <td><%= config_template.description %></td>
        <td><%= link_to 'Show', config_template %></td>
        <td><%= link_to 'Edit', edit_config_template_path(config_template) %></td>
        <td><%= link_to 'Delete', config_template, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<br>

<%= link_to 'New Config Template', new_config_template_path %>


File: /app\views\config_templates\index.json.jbuilder
json.array! @config_templates, partial: 'config_templates/config_template', as: :config_template

File: /app\views\config_templates\new.html.erb
<h1>New Config Template</h1>

<%= render 'form', config_template: @config_template %>

<%= link_to 'Back', config_templates_path %>


File: /app\views\config_templates\show.html.erb
<p id="notice"><%= notice %></p>

<p>
  <strong>Name:</strong>
  <%= @config_template.name %>
</p>

<p>
  <strong>Description:</strong>
  <%= @config_template.description %>
</p>

<p>
  <strong>Config text:</strong>
  <%= simple_format(@config_template.config_text) %>
</p>

<%= link_to 'Edit', edit_config_template_path(@config_template) %> |
<%= link_to 'Back', config_templates_path %>


File: /app\views\config_templates\show.json.jbuilder
json.partial! "config_templates/config_template", config_template: @config_template

File: /app\views\config_templates\_config_template.json.jbuilder
json.extract! config_template, :id, :name, :description, :config_text, :created_at, :updated_at
json.url config_template_url(config_template, format: :json)

File: /app\views\config_templates\_form.html.erb
<%= form_for(config_template) do |f| %>
  <% if config_template.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(config_template.errors.count, "error") %> prohibited this config_template from being saved:</h2>

      <ul>
      <% config_template.errors.full_messages.each do |message| %>
        <li><%= message %></li>
      <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= f.label :name %>
    <%= f.text_field :name %>
  </div>

  <div class="field">
    <%= f.label :description %>
    <%= f.text_field :description %>
  </div>

  <div class="field">
    <%= f.label :config_text %>
    <%= f.text_area :config_text, cols: "80", rows: "60" %>
  </div>

  <div class="actions">
    <%= f.submit %>
  </div>
<% end %>


File: /app\views\home\index.html.erb
<h2><%= link_to 'Configs', configs_path %> | <%= link_to 'Templates', config_templates_path %></h2>
<h1>IP River Router Config Generator</h1>
<p>Choose a tab from above</p>


File: /app\views\interfaces\edit.html.erb
<h1>Editing Interface</h1>

<%= render 'form', interface: @interface %>

<%= link_to 'Show', @interface %> |
<%= link_to 'Back', interfaces_path %>


File: /app\views\interfaces\index.html.erb
<p id="notice"><%= notice %></p>

<h1>Interfaces</h1>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Ip</th>
      <th>Subnet</th>
      <th>Gateway</th>
      <th>Username</th>
      <th>Password</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @interfaces.each do |interface| %>
      <tr>
        <td><%= interface.name %></td>
        <td><%= interface.ip %></td>
        <td><%= interface.subnet %></td>
        <td><%= interface.gateway %></td>
        <td><%= interface.username %></td>
        <td><%= interface.password %></td>
        <td><%= link_to 'Show', interface %></td>
        <td><%= link_to 'Edit', edit_interface_path(interface) %></td>
        <td><%= link_to 'Destroy', interface, method: :delete, data: { confirm: 'Are you sure?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<br>

<%= link_to 'New Interface', new_interface_path %>


File: /app\views\interfaces\index.json.jbuilder
json.array! @interfaces, partial: 'interfaces/interface', as: :interface

File: /app\views\interfaces\new.html.erb
<h1>New Interface</h1>

<%= render 'form', interface: @interface %>

<%= link_to 'Back', interfaces_path %>


File: /app\views\interfaces\show.html.erb
<p id="notice"><%= notice %></p>

<p>
  <strong>Name:</strong>
  <%= @interface.name %>
</p>

<p>
  <strong>Ip:</strong>
  <%= @interface.ip %>
</p>

<p>
  <strong>Subnet:</strong>
  <%= @interface.subnet %>
</p>

<p>
  <strong>Gateway:</strong>
  <%= @interface.gateway %>
</p>

<p>
  <strong>Username:</strong>
  <%= @interface.username %>
</p>

<p>
  <strong>Password:</strong>
  <%= @interface.password %>
</p>

<%= link_to 'Edit', edit_interface_path(@interface) %> |
<%= link_to 'Back', interfaces_path %>


File: /app\views\interfaces\show.json.jbuilder
json.partial! "interfaces/interface", interface: @interface

File: /app\views\interfaces\_form.html.erb
<%= form_for(interface) do |f| %>
  <% if interface.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(interface.errors.count, "error") %> prohibited this interface from being saved:</h2>

      <ul>
      <% interface.errors.full_messages.each do |message| %>
        <li><%= message %></li>
      <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= f.label :name %>
    <%= f.text_field :name %>
  </div>

  <div class="field">
    <%= f.label :ip %>
    <%= f.text_field :ip %>
  </div>

  <div class="field">
    <%= f.label :subnet %>
    <%= f.text_field :subnet %>
  </div>

  <div class="field">
    <%= f.label :gateway %>
    <%= f.text_field :gateway %>
  </div>

  <div class="field">
    <%= f.label :username %>
    <%= f.text_field :username %>
  </div>

  <div class="field">
    <%= f.label :password %>
    <%= f.text_field :password %>
  </div>

  <div class="actions">
    <%= f.submit %>
  </div>
<% end %>


File: /app\views\interfaces\_interface.json.jbuilder
json.extract! interface, :id, :name, :ip, :subnet, :gateway, :username, :password, :created_at, :updated_at
json.url interface_url(interface, format: :json)

File: /app\views\layouts\application.html.erb
<!DOCTYPE html>
<html>
  <head>
    <title>IP River Mikrotik Config Generator</title>
    <%= csrf_meta_tags %>

    <%= stylesheet_link_tag    'application', media: 'all', 'data-turbolinks-track': 'reload' %>
    <%= javascript_include_tag 'application', 'data-turbolinks-track': 'reload' %>
  </head>

  <body>
  <% unless controller.controller_name == 'home' %>
    <%= link_to 'back', home_index_path %>
  <% end %>
    <%= yield %>
  </body>
  <footer>
    &copy; 2017, IP River
  </footer>
</html>


File: /app\views\layouts\mailer.html.erb
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style>
      /* Email styles need to be inline */
    </style>
  </head>

  <body>
    <%= yield %>
  </body>
</html>


File: /app\views\layouts\mailer.text.erb
<%= yield %>


File: /bin\bundle
#!/usr/bin/env ruby
ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../../Gemfile', __FILE__)
load Gem.bin_path('bundler', 'bundle')


File: /bin\rails
#!/usr/bin/env ruby
begin
  load File.expand_path('../spring', __FILE__)
rescue LoadError => e
  raise unless e.message.include?('spring')
end
APP_PATH = File.expand_path('../config/application', __dir__)
require_relative '../config/boot'
require 'rails/commands'


File: /bin\rake
#!/usr/bin/env ruby
begin
  load File.expand_path('../spring', __FILE__)
rescue LoadError => e
  raise unless e.message.include?('spring')
end
require_relative '../config/boot'
require 'rake'
Rake.application.run


File: /bin\setup
#!/usr/bin/env ruby
require 'pathname'
require 'fileutils'
include FileUtils

# path to your application root.
APP_ROOT = Pathname.new File.expand_path('../../', __FILE__)

def system!(*args)
  system(*args) || abort("\n== Command #{args} failed ==")
end

chdir APP_ROOT do
  # This script is a starting point to setup your application.
  # Add necessary setup steps to this file.

  puts '== Installing dependencies =='
  system! 'gem install bundler --conservative'
  system('bundle check') || system!('bundle install')

  # puts "\n== Copying sample files =="
  # unless File.exist?('config/database.yml')
  #   cp 'config/database.yml.sample', 'config/database.yml'
  # end

  puts "\n== Preparing database =="
  system! 'bin/rails db:setup'

  puts "\n== Removing old logs and tempfiles =="
  system! 'bin/rails log:clear tmp:clear'

  puts "\n== Restarting application server =="
  system! 'bin/rails restart'
end


File: /bin\spring
#!/usr/bin/env ruby

# This file loads spring without using Bundler, in order to be fast.
# It gets overwritten when you run the `spring binstub` command.

unless defined?(Spring)
  require 'rubygems'
  require 'bundler'

  lockfile = Bundler::LockfileParser.new(Bundler.default_lockfile.read)
  if spring = lockfile.specs.detect { |spec| spec.name == "spring" }
    Gem.use_paths Gem.dir, Bundler.bundle_path.to_s, *Gem.path
    gem 'spring', spring.version
    require 'spring/binstub'
  end
end


File: /bin\update
#!/usr/bin/env ruby
require 'pathname'
require 'fileutils'
include FileUtils

# path to your application root.
APP_ROOT = Pathname.new File.expand_path('../../', __FILE__)

def system!(*args)
  system(*args) || abort("\n== Command #{args} failed ==")
end

chdir APP_ROOT do
  # This script is a way to update your development environment automatically.
  # Add necessary update steps to this file.

  puts '== Installing dependencies =='
  system! 'gem install bundler --conservative'
  system('bundle check') || system!('bundle install')

  puts "\n== Updating database =="
  system! 'bin/rails db:migrate'

  puts "\n== Removing old logs and tempfiles =="
  system! 'bin/rails log:clear tmp:clear'

  puts "\n== Restarting application server =="
  system! 'bin/rails restart'
end


File: /config\application.rb
require_relative 'boot'

require 'rails/all'

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module IpriverMikrotikConfigGenerator
  class Application < Rails::Application
    # Settings in config/environments/* take precedence over those specified here.
    # Application configuration should go into files in config/initializers
    # -- all .rb files in that directory are automatically loaded.
  end
end


File: /config\boot.rb
ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../Gemfile', __dir__)

require 'bundler/setup' # Set up gems listed in the Gemfile.


File: /config\cable.yml
development:
  adapter: async

test:
  adapter: async

production:
  adapter: redis
  url: redis://localhost:6379/1


File: /config\database.yml
# MySQL. Versions 5.0 and up are supported.
#
# Install the MySQL driver
#   gem install mysql2
#
# Ensure the MySQL gem is defined in your Gemfile
#   gem 'mysql2'
#
# And be sure to use new-style password hashing:
#   http://dev.mysql.com/doc/refman/5.7/en/old-client.html
#
default: &default
  adapter: mysql2
  encoding: utf8
  pool: 5
  username: root
  password: xerxes2002
  socket: /var/run/mysqld/mysqld.sock

development:
  <<: *default
  database: ipriver_mikrotik_config_generator_development

# Warning: The database defined as "test" will be erased and
# re-generated from your development database when you run "rake".
# Do not set this db to the same as development or production.
test:
  <<: *default
  database: ipriver_mikrotik_config_generator_test

# As with config/secrets.yml, you never want to store sensitive information,
# like your database password, in your source code. If your source code is
# ever seen by anyone, they now have access to your database.
#
# Instead, provide the password as a unix environment variable when you boot
# the app. Read http://guides.rubyonrails.org/configuring.html#configuring-a-database
# for a full rundown on how to provide these environment variables in a
# production deployment.
#
# On Heroku and other platform providers, you may have a full connection URL
# available as an environment variable. For example:
#
#   DATABASE_URL="mysql2://myuser:mypass@localhost/somedatabase"
#
# You can use this database configuration with:
#
#   production:
#     url: <%= ENV['DATABASE_URL'] %>
#
production:
  <<: *default
  database: ipriver_mikrotik_config_generator_production
  username: ipriver_mikrotik_config_generator
  password: <%= ENV['IPRIVER_MIKROTIK_CONFIG_GENERATOR_DATABASE_PASSWORD'] %>


File: /config\environment.rb
# Load the Rails application.
require_relative 'application'

# Initialize the Rails application.
Rails.application.initialize!


File: /config\environments\development.rb
Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.

  # In the development environment your application's code is reloaded on
  # every request. This slows down response time but is perfect for development
  # since you don't have to restart the web server when you make code changes.
  config.cache_classes = false

  # Do not eager load code on boot.
  config.eager_load = false

  # Show full error reports.
  config.consider_all_requests_local = true

  # Enable/disable caching. By default caching is disabled.
  if Rails.root.join('tmp/caching-dev.txt').exist?
    config.action_controller.perform_caching = true

    config.cache_store = :memory_store
    config.public_file_server.headers = {
      'Cache-Control' => 'public, max-age=172800'
    }
  else
    config.action_controller.perform_caching = false

    config.cache_store = :null_store
  end

  # Don't care if the mailer can't send.
  config.action_mailer.raise_delivery_errors = false

  config.action_mailer.perform_caching = false

  # Print deprecation notices to the Rails logger.
  config.active_support.deprecation = :log

  # Raise an error on page load if there are pending migrations.
  config.active_record.migration_error = :page_load

  # Debug mode disables concatenation and preprocessing of assets.
  # This option may cause significant delays in view rendering with a large
  # number of complex assets.
  config.assets.debug = true

  # Suppress logger output for asset requests.
  config.assets.quiet = true

  # Raises error for missing translations
  # config.action_view.raise_on_missing_translations = true

  # Use an evented file watcher to asynchronously detect changes in source code,
  # routes, locales, etc. This feature depends on the listen gem.
  config.file_watcher = ActiveSupport::EventedFileUpdateChecker
end


File: /config\environments\production.rb
Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.

  # Code is not reloaded between requests.
  config.cache_classes = true

  # Eager load code on boot. This eager loads most of Rails and
  # your application in memory, allowing both threaded web servers
  # and those relying on copy on write to perform better.
  # Rake tasks automatically ignore this option for performance.
  config.eager_load = true

  # Full error reports are disabled and caching is turned on.
  config.consider_all_requests_local       = false
  config.action_controller.perform_caching = true

  # Disable serving static files from the `/public` folder by default since
  # Apache or NGINX already handles this.
  config.public_file_server.enabled = ENV['RAILS_SERVE_STATIC_FILES'].present?

  # Compress JavaScripts and CSS.
  config.assets.js_compressor = :uglifier
  # config.assets.css_compressor = :sass

  # Do not fallback to assets pipeline if a precompiled asset is missed.
  config.assets.compile = false

  # `config.assets.precompile` and `config.assets.version` have moved to config/initializers/assets.rb

  # Enable serving of images, stylesheets, and JavaScripts from an asset server.
  # config.action_controller.asset_host = 'http://assets.example.com'

  # Specifies the header that your server uses for sending files.
  # config.action_dispatch.x_sendfile_header = 'X-Sendfile' # for Apache
  # config.action_dispatch.x_sendfile_header = 'X-Accel-Redirect' # for NGINX

  # Mount Action Cable outside main process or domain
  # config.action_cable.mount_path = nil
  # config.action_cable.url = 'wss://example.com/cable'
  # config.action_cable.allowed_request_origins = [ 'http://example.com', /http:\/\/example.*/ ]

  # Force all access to the app over SSL, use Strict-Transport-Security, and use secure cookies.
  # config.force_ssl = true

  # Use the lowest log level to ensure availability of diagnostic information
  # when problems arise.
  config.log_level = :debug

  # Prepend all log lines with the following tags.
  config.log_tags = [ :request_id ]

  # Use a different cache store in production.
  # config.cache_store = :mem_cache_store

  # Use a real queuing backend for Active Job (and separate queues per environment)
  # config.active_job.queue_adapter     = :resque
  # config.active_job.queue_name_prefix = "ipriver_mikrotik_config_generator_#{Rails.env}"
  config.action_mailer.perform_caching = false

  # Ignore bad email addresses and do not raise email delivery errors.
  # Set this to true and configure the email server for immediate delivery to raise delivery errors.
  # config.action_mailer.raise_delivery_errors = false

  # Enable locale fallbacks for I18n (makes lookups for any locale fall back to
  # the I18n.default_locale when a translation cannot be found).
  config.i18n.fallbacks = true

  # Send deprecation notices to registered listeners.
  config.active_support.deprecation = :notify

  # Use default logging formatter so that PID and timestamp are not suppressed.
  config.log_formatter = ::Logger::Formatter.new

  # Use a different logger for distributed setups.
  # require 'syslog/logger'
  # config.logger = ActiveSupport::TaggedLogging.new(Syslog::Logger.new 'app-name')

  if ENV["RAILS_LOG_TO_STDOUT"].present?
    logger           = ActiveSupport::Logger.new(STDOUT)
    logger.formatter = config.log_formatter
    config.logger = ActiveSupport::TaggedLogging.new(logger)
  end

  # Do not dump schema after migrations.
  config.active_record.dump_schema_after_migration = false
end


File: /config\environments\test.rb
Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.

  # The test environment is used exclusively to run your application's
  # test suite. You never need to work with it otherwise. Remember that
  # your test database is "scratch space" for the test suite and is wiped
  # and recreated between test runs. Don't rely on the data there!
  config.cache_classes = true

  # Do not eager load code on boot. This avoids loading your whole application
  # just for the purpose of running a single test. If you are using a tool that
  # preloads Rails for running tests, you may have to set it to true.
  config.eager_load = false

  # Configure public file server for tests with Cache-Control for performance.
  config.public_file_server.enabled = true
  config.public_file_server.headers = {
    'Cache-Control' => 'public, max-age=3600'
  }

  # Show full error reports and disable caching.
  config.consider_all_requests_local       = true
  config.action_controller.perform_caching = false

  # Raise exceptions instead of rendering exception templates.
  config.action_dispatch.show_exceptions = false

  # Disable request forgery protection in test environment.
  config.action_controller.allow_forgery_protection = false
  config.action_mailer.perform_caching = false

  # Tell Action Mailer not to deliver emails to the real world.
  # The :test delivery method accumulates sent emails in the
  # ActionMailer::Base.deliveries array.
  config.action_mailer.delivery_method = :test

  # Print deprecation notices to the stderr.
  config.active_support.deprecation = :stderr

  # Raises error for missing translations
  # config.action_view.raise_on_missing_translations = true
end


File: /config\initializers\application_controller_renderer.rb
# Be sure to restart your server when you modify this file.

# ApplicationController.renderer.defaults.merge!(
#   http_host: 'example.org',
#   https: false
# )


File: /config\initializers\assets.rb
# Be sure to restart your server when you modify this file.

# Version of your assets, change this if you want to expire all your assets.
Rails.application.config.assets.version = '1.0'

# Add additional assets to the asset load path
# Rails.application.config.assets.paths << Emoji.images_path

# Precompile additional assets.
# application.js, application.css, and all non-JS/CSS in app/assets folder are already added.
# Rails.application.config.assets.precompile += %w( search.js )


File: /config\initializers\backtrace_silencers.rb
# Be sure to restart your server when you modify this file.

# You can add backtrace silencers for libraries that you're using but don't wish to see in your backtraces.
# Rails.backtrace_cleaner.add_silencer { |line| line =~ /my_noisy_library/ }

# You can also remove all the silencers if you're trying to debug a problem that might stem from framework code.
# Rails.backtrace_cleaner.remove_silencers!


File: /config\initializers\cookies_serializer.rb
# Be sure to restart your server when you modify this file.

# Specify a serializer for the signed and encrypted cookie jars.
# Valid options are :json, :marshal, and :hybrid.
Rails.application.config.action_dispatch.cookies_serializer = :json


File: /config\initializers\filter_parameter_logging.rb
# Be sure to restart your server when you modify this file.

# Configure sensitive parameters which will be filtered from the log file.
Rails.application.config.filter_parameters += [:password]


File: /config\initializers\inflections.rb
# Be sure to restart your server when you modify this file.

# Add new inflection rules using the following format. Inflections
# are locale specific, and you may define rules for as many different
# locales as you wish. All of these examples are active by default:
# ActiveSupport::Inflector.inflections(:en) do |inflect|
#   inflect.plural /^(ox)$/i, '\1en'
#   inflect.singular /^(ox)en/i, '\1'
#   inflect.irregular 'person', 'people'
#   inflect.uncountable %w( fish sheep )
# end

# These inflection rules are supported but not enabled by default:
# ActiveSupport::Inflector.inflections(:en) do |inflect|
#   inflect.acronym 'RESTful'
# end


File: /config\initializers\mime_types.rb
# Be sure to restart your server when you modify this file.

# Add new mime types for use in respond_to blocks:
# Mime::Type.register "text/richtext", :rtf


File: /config\initializers\new_framework_defaults.rb
# Be sure to restart your server when you modify this file.
#
# This file contains migration options to ease your Rails 5.0 upgrade.
#
# Read the Guide for Upgrading Ruby on Rails for more info on each option.

# Enable per-form CSRF tokens. Previous versions had false.
Rails.application.config.action_controller.per_form_csrf_tokens = true

# Enable origin-checking CSRF mitigation. Previous versions had false.
Rails.application.config.action_controller.forgery_protection_origin_check = true

# Make Ruby 2.4 preserve the timezone of the receiver when calling `to_time`.
# Previous versions had false.
ActiveSupport.to_time_preserves_timezone = true

# Require `belongs_to` associations by default. Previous versions had false.
Rails.application.config.active_record.belongs_to_required_by_default = true

# Do not halt callback chains when a callback returns false. Previous versions had true.
ActiveSupport.halt_callback_chains_on_return_false = false

# Configure SSL options to enable HSTS with subdomains. Previous versions had false.
Rails.application.config.ssl_options = { hsts: { subdomains: true } }


File: /config\initializers\session_store.rb
# Be sure to restart your server when you modify this file.

Rails.application.config.session_store :cookie_store, key: '_ipriver_mikrotik_config_generator_session'


File: /config\initializers\wrap_parameters.rb
# Be sure to restart your server when you modify this file.

# This file contains settings for ActionController::ParamsWrapper which
# is enabled by default.

# Enable parameter wrapping for JSON. You can disable this by setting :format to an empty array.
ActiveSupport.on_load(:action_controller) do
  wrap_parameters format: [:json]
end

# To enable root element in JSON for ActiveRecord objects.
# ActiveSupport.on_load(:active_record) do
#   self.include_root_in_json = true
# end


File: /config\locales\en.yml
# Files in the config/locales directory are used for internationalization
# and are automatically loaded by Rails. If you want to use locales other
# than English, add the necessary files in this directory.
#
# To use the locales, use `I18n.t`:
#
#     I18n.t 'hello'
#
# In views, this is aliased to just `t`:
#
#     <%= t('hello') %>
#
# To use a different locale, set it with `I18n.locale`:
#
#     I18n.locale = :es
#
# This would use the information in config/locales/es.yml.
#
# To learn more, please read the Rails Internationalization guide
# available at http://guides.rubyonrails.org/i18n.html.

en:
  hello: "Hello world"


File: /config\puma.rb
# Puma can serve each request in a thread from an internal thread pool.
# The `threads` method setting takes two numbers a minimum and maximum.
# Any libraries that use thread pools should be configured to match
# the maximum value specified for Puma. Default is set to 5 threads for minimum
# and maximum, this matches the default thread size of Active Record.
#
threads_count = ENV.fetch("RAILS_MAX_THREADS") { 5 }.to_i
threads threads_count, threads_count

# Specifies the `port` that Puma will listen on to receive requests, default is 3000.
#
port        ENV.fetch("PORT") { 3000 }

# Specifies the `environment` that Puma will run in.
#
environment ENV.fetch("RAILS_ENV") { "development" }

# Specifies the number of `workers` to boot in clustered mode.
# Workers are forked webserver processes. If using threads and workers together
# the concurrency of the application would be max `threads` * `workers`.
# Workers do not work on JRuby or Windows (both of which do not support
# processes).
#
# workers ENV.fetch("WEB_CONCURRENCY") { 2 }

# Use the `preload_app!` method when specifying a `workers` number.
# This directive tells Puma to first boot the application and load code
# before forking the application. This takes advantage of Copy On Write
# process behavior so workers use less memory. If you use this option
# you need to make sure to reconnect any threads in the `on_worker_boot`
# block.
#
# preload_app!

# The code in the `on_worker_boot` will be called if you are using
# clustered mode by specifying a number of `workers`. After each worker
# process is booted this block will be run, if you are using `preload_app!`
# option you will want to use this block to reconnect to any threads
# or connections that may have been created at application boot, Ruby
# cannot share connections between processes.
#
# on_worker_boot do
#   ActiveRecord::Base.establish_connection if defined?(ActiveRecord)
# end

# Allow puma to be restarted by `rails restart` command.
plugin :tmp_restart


File: /config\routes.rb
Rails.application.routes.draw do
  get 'home/index'
  root 'home#index'

  resources :configs do
    member do
      get 'generate'
    end
  end
  resources :config_templates
  resources :interfaces
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end


File: /config\secrets.yml
# Be sure to restart your server when you modify this file.

# Your secret key is used for verifying the integrity of signed cookies.
# If you change this key, all old signed cookies will become invalid!

# Make sure the secret is at least 30 characters and all random,
# no regular words or you'll be exposed to dictionary attacks.
# You can use `rails secret` to generate a secure secret key.

# Make sure the secrets in this file are kept private
# if you're sharing your code publicly.

development:
  secret_key_base: 3d23ba5a4fda0202b6ac8ad0202beeedd91f6e3bb996749187aa2dc3c1213863dac2668aef5759260d5cd7fad1ba4b6df663901f6f95766d3b9d072f9be0e950

test:
  secret_key_base: 094925e6acf67d4c633f973dafbf589af116d962f01a3984c0b476f247a44fa305344815c870187fc3543e5d1d3d433f9f2f1122abeb61d74fa76f7a4551c6bd

# Do not keep production secrets in the repository,
# instead read values from the environment.
production:
  secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>


File: /config\spring.rb
%w(
  .ruby-version
  .rbenv-vars
  tmp/restart.txt
  tmp/caching-dev.txt
).each { |path| Spring.watch(path) }


File: /config.ru
# This file is used by Rack-based servers to start the application.

require_relative 'config/environment'

run Rails.application


File: /db\migrate\20170117180244_create_interfaces.rb
class CreateInterfaces < ActiveRecord::Migration[5.0]
  def change
    create_table :interfaces do |t|
      t.string :name
      t.string :ip
      t.string :subnet
      t.string :gateway
      t.string :username
      t.string :password

      t.timestamps
    end
  end
end


File: /db\migrate\20170117180319_create_config_templates.rb
class CreateConfigTemplates < ActiveRecord::Migration[5.0]
  def change
    create_table :config_templates do |t|
      t.string :name
      t.string :description
      t.text :config_text

      t.timestamps
    end
  end
end


File: /db\migrate\20170117180428_create_configs.rb
class CreateConfigs < ActiveRecord::Migration[5.0]
  def change
    create_table :configs do |t|
      t.string :system_name
      t.string :password
      t.string :snmp_community
      t.string :snmp_address
      t.string :snmp_contact
      t.string :snmp_location

      t.timestamps
    end
  end
end


File: /db\migrate\20170117180733_add_config_to_interface.rb
class AddConfigToInterface < ActiveRecord::Migration[5.0]
  def change
    add_reference :interfaces, :config, foreign_key: true
  end
end


File: /db\migrate\20170117180948_add_config_template_to_config.rb
class AddConfigTemplateToConfig < ActiveRecord::Migration[5.0]
  def change
    add_reference :configs, :config_template, foreign_key: true
  end
end


File: /db\migrate\20170117235021_add_type_to_interface.rb
class AddTypeToInterface < ActiveRecord::Migration[5.0]
  def change
    add_column :interfaces, :interface_type, :string
  end
end


File: /db\schema.rb
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170117235021) do

  create_table "config_templates", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "name"
    t.string   "description"
    t.text     "config_text", limit: 65535
    t.datetime "created_at",                null: false
    t.datetime "updated_at",                null: false
  end

  create_table "configs", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "system_name"
    t.string   "password"
    t.string   "snmp_community"
    t.string   "snmp_address"
    t.string   "snmp_contact"
    t.string   "snmp_location"
    t.datetime "created_at",         null: false
    t.datetime "updated_at",         null: false
    t.integer  "config_template_id"
    t.index ["config_template_id"], name: "index_configs_on_config_template_id", using: :btree
  end

  create_table "interfaces", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
    t.string   "name"
    t.string   "ip"
    t.string   "subnet"
    t.string   "gateway"
    t.string   "username"
    t.string   "password"
    t.datetime "created_at",     null: false
    t.datetime "updated_at",     null: false
    t.integer  "config_id"
    t.string   "interface_type"
    t.index ["config_id"], name: "index_interfaces_on_config_id", using: :btree
  end

  add_foreign_key "configs", "config_templates"
  add_foreign_key "interfaces", "configs"
end


File: /db\seeds.rb
# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

ConfigTemplate.create(name: 'Ethernet Standard', description: 'Ethernet standard, 2 ethernet ports WAN/LAN', config_text: "/interface ethernet\r\nset [ find default-name=ether2 ] name=ether2-master\r\nset [ find default-name=ether3 ] master-port=ether2-master\r\nset [ find default-name=ether4 ] master-port=ether2-master\r\nset [ find default-name=ether5 ] master-port=ether2-master\r\nset [ find default-name=ether6 ] name=ether6-master\r\nset [ find default-name=ether7 ] master-port=ether6-master\r\nset [ find default-name=ether8 ] master-port=ether6-master\r\nset [ find default-name=ether9 ] master-port=ether6-master\r\nset [ find default-name=ether10 ] master-port=ether6-master\r\n/ip neighbor discovery\r\nset ether1 discover=no\r\n/ip dns set allow-remote-requests=yes\r\n/ip firewall filter\r\nadd chain=input comment=\"defconf: accept ICMP\" protocol=icmp\r\nadd chain=input comment=\"defconf: accept establieshed,related\" \\\r\n    connection-state=established,related\r\nadd action=fasttrack-connection chain=forward comment=\"defconf: fasttrack\" \\\r\n    connection-state=established,related\r\nadd chain=forward comment=\"defconf: accept established,related\" \\\r\n    connection-state=established,related\r\nadd action=drop chain=forward comment=\"defconf: drop invalid\" \\\r\n    connection-state=invalid\r\n/tool mac-server\r\nset [ find default=yes ] disabled=yes\r\nadd interface=ether2-master\r\n/tool mac-server mac-winbox\r\nset [ find default=yes ] disabled=yes\r\nadd interface=ether2-master\r\n/ip service disable 0,1,2,3,4,5,7\r\n/ip service set winbox address=5.157.64.37,185.113.80.137,5.157.64.38,192.168.88.100\r\n/system clock set time-zone-name=Europe/London\r\n/system ntp client set enabled=yes server-dns-names=0.uk.pool.ntp.org\r\n/system package update set channel=bugfix\r\n/lcd\nset read-only-mode=yes\nset default-screen=stat-slideshow\nscreen disable numbers=1,2,3,4,5\ninterface disable 0,3,4,5,6,7,8,9,10")

File: /Gemfile
source 'https://rubygems.org'

git_source(:github) do |repo_name|
  repo_name = "#{repo_name}/#{repo_name}" unless repo_name.include?("/")
  "https://github.com/#{repo_name}.git"
end


# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 5.0.1'
# Use mysql as the database for Active Record
gem 'mysql2', '>= 0.3.18', '< 0.5'
# Use Puma as the app server
gem 'puma', '~> 3.0'
# Use SCSS for stylesheets
gem 'sass-rails', '~> 5.0'
# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'
# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 4.2'
# See https://github.com/rails/execjs#readme for more supported runtimes
gem 'therubyracer', platforms: :ruby

# Use jquery as the JavaScript library
gem 'jquery-rails'
# Turbolinks makes navigating your web application faster. Read more: https://github.com/turbolinks/turbolinks
gem 'turbolinks', '~> 5'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.5'
# Use Redis adapter to run Action Cable in production
# gem 'redis', '~> 3.0'
# Use ActiveModel has_secure_password
# gem 'bcrypt', '~> 3.1.7'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

gem 'ipaddress'

group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platform: :mri
end

group :development do
  # Access an IRB console on exception pages or by using <%= console %> anywhere in the code.
  gem 'web-console', '>= 3.3.0'
  gem 'listen', '~> 3.0.5'
  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]


File: /Gemfile.lock
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (5.0.1)
      actionpack (= 5.0.1)
      nio4r (~> 1.2)
      websocket-driver (~> 0.6.1)
    actionmailer (5.0.1)
      actionpack (= 5.0.1)
      actionview (= 5.0.1)
      activejob (= 5.0.1)
      mail (~> 2.5, >= 2.5.4)
      rails-dom-testing (~> 2.0)
    actionpack (5.0.1)
      actionview (= 5.0.1)
      activesupport (= 5.0.1)
      rack (~> 2.0)
      rack-test (~> 0.6.3)
      rails-dom-testing (~> 2.0)
      rails-html-sanitizer (~> 1.0, >= 1.0.2)
    actionview (5.0.1)
      activesupport (= 5.0.1)
      builder (~> 3.1)
      erubis (~> 2.7.0)
      rails-dom-testing (~> 2.0)
      rails-html-sanitizer (~> 1.0, >= 1.0.2)
    activejob (5.0.1)
      activesupport (= 5.0.1)
      globalid (>= 0.3.6)
    activemodel (5.0.1)
      activesupport (= 5.0.1)
    activerecord (5.0.1)
      activemodel (= 5.0.1)
      activesupport (= 5.0.1)
      arel (~> 7.0)
    activesupport (5.0.1)
      concurrent-ruby (~> 1.0, >= 1.0.2)
      i18n (~> 0.7)
      minitest (~> 5.1)
      tzinfo (~> 1.1)
    arel (7.1.4)
    builder (3.2.3)
    byebug (9.0.6)
    coffee-rails (4.2.1)
      coffee-script (>= 2.2.0)
      railties (>= 4.0.0, < 5.2.x)
    coffee-script (2.4.1)
      coffee-script-source
      execjs
    coffee-script-source (1.12.2)
    concurrent-ruby (1.0.4)
    debug_inspector (0.0.2)
    erubis (2.7.0)
    execjs (2.7.0)
    ffi (1.9.17)
    globalid (0.3.7)
      activesupport (>= 4.1.0)
    i18n (0.7.0)
    ipaddress (0.8.3)
    jbuilder (2.6.1)
      activesupport (>= 3.0.0, < 5.1)
      multi_json (~> 1.2)
    jquery-rails (4.2.2)
      rails-dom-testing (>= 1, < 3)
      railties (>= 4.2.0)
      thor (>= 0.14, < 2.0)
    libv8 (3.16.14.17)
    listen (3.0.8)
      rb-fsevent (~> 0.9, >= 0.9.4)
      rb-inotify (~> 0.9, >= 0.9.7)
    loofah (2.0.3)
      nokogiri (>= 1.5.9)
    mail (2.6.4)
      mime-types (>= 1.16, < 4)
    method_source (0.8.2)
    mime-types (3.1)
      mime-types-data (~> 3.2015)
    mime-types-data (3.2016.0521)
    mini_portile2 (2.1.0)
    minitest (5.10.1)
    multi_json (1.12.1)
    mysql2 (0.4.5)
    nio4r (1.2.1)
    nokogiri (1.7.0.1)
      mini_portile2 (~> 2.1.0)
    puma (3.6.2)
    rack (2.0.1)
    rack-test (0.6.3)
      rack (>= 1.0)
    rails (5.0.1)
      actioncable (= 5.0.1)
      actionmailer (= 5.0.1)
      actionpack (= 5.0.1)
      actionview (= 5.0.1)
      activejob (= 5.0.1)
      activemodel (= 5.0.1)
      activerecord (= 5.0.1)
      activesupport (= 5.0.1)
      bundler (>= 1.3.0, < 2.0)
      railties (= 5.0.1)
      sprockets-rails (>= 2.0.0)
    rails-dom-testing (2.0.2)
      activesupport (>= 4.2.0, < 6.0)
      nokogiri (~> 1.6)
    rails-html-sanitizer (1.0.3)
      loofah (~> 2.0)
    railties (5.0.1)
      actionpack (= 5.0.1)
      activesupport (= 5.0.1)
      method_source
      rake (>= 0.8.7)
      thor (>= 0.18.1, < 2.0)
    rake (12.0.0)
    rb-fsevent (0.9.8)
    rb-inotify (0.9.7)
      ffi (>= 0.5.0)
    ref (2.0.0)
    sass (3.4.23)
    sass-rails (5.0.6)
      railties (>= 4.0.0, < 6)
      sass (~> 3.1)
      sprockets (>= 2.8, < 4.0)
      sprockets-rails (>= 2.0, < 4.0)
      tilt (>= 1.1, < 3)
    spring (2.0.0)
      activesupport (>= 4.2)
    spring-watcher-listen (2.0.1)
      listen (>= 2.7, < 4.0)
      spring (>= 1.2, < 3.0)
    sprockets (3.7.1)
      concurrent-ruby (~> 1.0)
      rack (> 1, < 3)
    sprockets-rails (3.2.0)
      actionpack (>= 4.0)
      activesupport (>= 4.0)
      sprockets (>= 3.0.0)
    therubyracer (0.12.2)
      libv8 (~> 3.16.14.0)
      ref
    thor (0.19.4)
    thread_safe (0.3.5)
    tilt (2.0.5)
    turbolinks (5.0.1)
      turbolinks-source (~> 5)
    turbolinks-source (5.0.0)
    tzinfo (1.2.2)
      thread_safe (~> 0.1)
    uglifier (3.0.4)
      execjs (>= 0.3.0, < 3)
    web-console (3.4.0)
      actionview (>= 5.0)
      activemodel (>= 5.0)
      debug_inspector
      railties (>= 5.0)
    websocket-driver (0.6.4)
      websocket-extensions (>= 0.1.0)
    websocket-extensions (0.1.2)

PLATFORMS
  ruby

DEPENDENCIES
  byebug
  coffee-rails (~> 4.2)
  ipaddress
  jbuilder (~> 2.5)
  jquery-rails
  listen (~> 3.0.5)
  mysql2 (>= 0.3.18, < 0.5)
  puma (~> 3.0)
  rails (~> 5.0.1)
  sass-rails (~> 5.0)
  spring
  spring-watcher-listen (~> 2.0.0)
  therubyracer
  turbolinks (~> 5)
  tzinfo-data
  uglifier (>= 1.3.0)
  web-console (>= 3.3.0)

BUNDLED WITH
   1.11.2


File: /public\404.html
<!DOCTYPE html>
<html>
<head>
  <title>The page you were looking for doesn't exist (404)</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
  body {
    background-color: #EFEFEF;
    color: #2E2F30;
    text-align: center;
    font-family: arial, sans-serif;
    margin: 0;
  }

  div.dialog {
    width: 95%;
    max-width: 33em;
    margin: 4em auto 0;
  }

  div.dialog > div {
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #BBB;
    border-top: #B00100 solid 4px;
    border-top-left-radius: 9px;
    border-top-right-radius: 9px;
    background-color: white;
    padding: 7px 12% 0;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }

  h1 {
    font-size: 100%;
    color: #730E15;
    line-height: 1.5em;
  }

  div.dialog > p {
    margin: 0 0 1em;
    padding: 1em;
    background-color: #F7F7F7;
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #999;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    border-top-color: #DADADA;
    color: #666;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }
  </style>
</head>

<body>
  <!-- This file lives in public/404.html -->
  <div class="dialog">
    <div>
      <h1>The page you were looking for doesn't exist.</h1>
      <p>You may have mistyped the address or the page may have moved.</p>
    </div>
    <p>If you are the application owner check the logs for more information.</p>
  </div>
</body>
</html>


File: /public\422.html
<!DOCTYPE html>
<html>
<head>
  <title>The change you wanted was rejected (422)</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
  body {
    background-color: #EFEFEF;
    color: #2E2F30;
    text-align: center;
    font-family: arial, sans-serif;
    margin: 0;
  }

  div.dialog {
    width: 95%;
    max-width: 33em;
    margin: 4em auto 0;
  }

  div.dialog > div {
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #BBB;
    border-top: #B00100 solid 4px;
    border-top-left-radius: 9px;
    border-top-right-radius: 9px;
    background-color: white;
    padding: 7px 12% 0;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }

  h1 {
    font-size: 100%;
    color: #730E15;
    line-height: 1.5em;
  }

  div.dialog > p {
    margin: 0 0 1em;
    padding: 1em;
    background-color: #F7F7F7;
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #999;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    border-top-color: #DADADA;
    color: #666;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }
  </style>
</head>

<body>
  <!-- This file lives in public/422.html -->
  <div class="dialog">
    <div>
      <h1>The change you wanted was rejected.</h1>
      <p>Maybe you tried to change something you didn't have access to.</p>
    </div>
    <p>If you are the application owner check the logs for more information.</p>
  </div>
</body>
</html>


File: /public\500.html
<!DOCTYPE html>
<html>
<head>
  <title>We're sorry, but something went wrong (500)</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
  body {
    background-color: #EFEFEF;
    color: #2E2F30;
    text-align: center;
    font-family: arial, sans-serif;
    margin: 0;
  }

  div.dialog {
    width: 95%;
    max-width: 33em;
    margin: 4em auto 0;
  }

  div.dialog > div {
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #BBB;
    border-top: #B00100 solid 4px;
    border-top-left-radius: 9px;
    border-top-right-radius: 9px;
    background-color: white;
    padding: 7px 12% 0;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }

  h1 {
    font-size: 100%;
    color: #730E15;
    line-height: 1.5em;
  }

  div.dialog > p {
    margin: 0 0 1em;
    padding: 1em;
    background-color: #F7F7F7;
    border: 1px solid #CCC;
    border-right-color: #999;
    border-left-color: #999;
    border-bottom-color: #999;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    border-top-color: #DADADA;
    color: #666;
    box-shadow: 0 3px 8px rgba(50, 50, 50, 0.17);
  }
  </style>
</head>

<body>
  <!-- This file lives in public/500.html -->
  <div class="dialog">
    <div>
      <h1>We're sorry, but something went wrong.</h1>
    </div>
    <p>If you are the application owner check the logs for more information.</p>
  </div>
</body>
</html>


File: /public\robots.txt
# See http://www.robotstxt.org/robotstxt.html for documentation on how to use the robots.txt file
#
# To ban all spiders from the entire site uncomment the next two lines:
# User-agent: *
# Disallow: /


File: /Rakefile
# Add your own tasks in files placed in lib/tasks ending in .rake,
# for example lib/tasks/capistrano.rake, and they will automatically be available to Rake.

require_relative 'config/application'

Rails.application.load_tasks


File: /README.md
# README

IP River Mikrotik config generator is a web application which stores router configurations and configurations templates and can generate .rsc files with which to apply these configurations. Presently it supports RB2011 and RB3011 series routers.

Tested with Ruby 2.3.3, Rails 5.0.1, MariaDB 15.1

To deploy simply clone from the deploy branch and run the following from the project directory.

gem install bundle
bundle install
rake db:setup
rake db:schema:load db:seed RAILS_ENV=development
rails s -d

# USAGE

## CREATING A TEMPLATE

Click templates at the top of the interface and then click the link at the bottom to create a new config template. All fields are mandatory. Name and description should assist users in selecting the correct template when making a new config. Config text is where your template configuration goes. Make sure to not enter any interface specific settings or firewall rules as these will be automatically created.

## CREATING A CONFIG

Click configs at the top of the interface and then click the link at the bottom to create a new config. Choose a config template from the drop down at the top and then enter your config parameters. All of the fields are mandatory with the exception of the interfaces. In interfaces select the type of interface and enter it's corresponding settings. Any unused interfaces should be set to unused. PPP interfaces must have a username and password, ethernet interfaces must have an IP and subnet, gateway is optional. If you make a mistake then the page will prompt you.
 
## GENERATE A CONFIG FILE
 
To generate a config file which you can load on to your router click on configs at the top of the interface and then click show next to the config you would like to use. Ensure that the settings are the ones you want to apply and then click the generate link at the bottom of the screen. This will download the rsc file. To apply to your router log in to it via winbox and click on Files, then click on the Upload button and select your configuration file. Now click System -> Reset Configuration. In the popup which appears select the options "No Default Configuration" and "Do Not Backup", in the run after reset drop down select your configuration file. Click OK and confirm to proceed, the router will reboot and apply your configuration. If you need to log in to the router again note that it will only accept winbox connections from IP addresses in the security list.

File: /test\controllers\configs_controller_test.rb
require 'test_helper'

class ConfigsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @config = configs(:one)
  end

  test "should get index" do
    get configs_url
    assert_response :success
  end

  test "should get new" do
    get new_config_url
    assert_response :success
  end

  test "should create config" do
    assert_difference('Config.count') do
      post configs_url, params: { config: { password: @config.password, snmp_address: @config.snmp_address, snmp_community: @config.snmp_community, snmp_contact: @config.snmp_contact, snmp_location: @config.snmp_location, system_name: @config.system_name } }
    end

    assert_redirected_to config_url(Config.last)
  end

  test "should show config" do
    get config_url(@config)
    assert_response :success
  end

  test "should get edit" do
    get edit_config_url(@config)
    assert_response :success
  end

  test "should update config" do
    patch config_url(@config), params: { config: { password: @config.password, snmp_address: @config.snmp_address, snmp_community: @config.snmp_community, snmp_contact: @config.snmp_contact, snmp_location: @config.snmp_location, system_name: @config.system_name } }
    assert_redirected_to config_url(@config)
  end

  test "should destroy config" do
    assert_difference('Config.count', -1) do
      delete config_url(@config)
    end

    assert_redirected_to configs_url
  end
end


File: /test\controllers\config_templates_controller_test.rb
require 'test_helper'

class ConfigTemplatesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @config_template = config_templates(:one)
  end

  test "should get index" do
    get config_templates_url
    assert_response :success
  end

  test "should get new" do
    get new_config_template_url
    assert_response :success
  end

  test "should create config_template" do
    assert_difference('ConfigTemplate.count') do
      post config_templates_url, params: { config_template: { config_text: @config_template.config_text, description: @config_template.description, name: @config_template.name } }
    end

    assert_redirected_to config_template_url(ConfigTemplate.last)
  end

  test "should show config_template" do
    get config_template_url(@config_template)
    assert_response :success
  end

  test "should get edit" do
    get edit_config_template_url(@config_template)
    assert_response :success
  end

  test "should update config_template" do
    patch config_template_url(@config_template), params: { config_template: { config_text: @config_template.config_text, description: @config_template.description, name: @config_template.name } }
    assert_redirected_to config_template_url(@config_template)
  end

  test "should destroy config_template" do
    assert_difference('ConfigTemplate.count', -1) do
      delete config_template_url(@config_template)
    end

    assert_redirected_to config_templates_url
  end
end


File: /test\controllers\home_controller_test.rb
require 'test_helper'

class HomeControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get home_index_url
    assert_response :success
  end

end


File: /test\controllers\interfaces_controller_test.rb
require 'test_helper'

class InterfacesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @interface = interfaces(:one)
  end

  test "should get index" do
    get interfaces_url
    assert_response :success
  end

  test "should get new" do
    get new_interface_url
    assert_response :success
  end

  test "should create interface" do
    assert_difference('Interface.count') do
      post interfaces_url, params: { interface: { gateway: @interface.gateway, ip: @interface.ip, name: @interface.name, password: @interface.password, subnet: @interface.subnet, username: @interface.username } }
    end

    assert_redirected_to interface_url(Interface.last)
  end

  test "should show interface" do
    get interface_url(@interface)
    assert_response :success
  end

  test "should get edit" do
    get edit_interface_url(@interface)
    assert_response :success
  end

  test "should update interface" do
    patch interface_url(@interface), params: { interface: { gateway: @interface.gateway, ip: @interface.ip, name: @interface.name, password: @interface.password, subnet: @interface.subnet, username: @interface.username } }
    assert_redirected_to interface_url(@interface)
  end

  test "should destroy interface" do
    assert_difference('Interface.count', -1) do
      delete interface_url(@interface)
    end

    assert_redirected_to interfaces_url
  end
end


File: /test\fixtures\configs.yml
# Read about fixtures at http://api.rubyonrails.org/classes/ActiveRecord/FixtureSet.html

one:
  system_name: MyString
  password: MyString
  snmp_community: MyString
  snmp_address: MyString
  snmp_contact: MyString
  snmp_location: MyString

two:
  system_name: MyString
  password: MyString
  snmp_community: MyString
  snmp_address: MyString
  snmp_contact: MyString
  snmp_location: MyString


File: /test\fixtures\config_templates.yml
# Read about fixtures at http://api.rubyonrails.org/classes/ActiveRecord/FixtureSet.html

one:
  name: MyString
  description: MyString
  config_text: MyText

two:
  name: MyString
  description: MyString
  config_text: MyText


File: /test\fixtures\interfaces.yml
# Read about fixtures at http://api.rubyonrails.org/classes/ActiveRecord/FixtureSet.html

one:
  name: MyString
  ip: MyString
  subnet: MyString
  gateway: MyString
  username: MyString
  password: MyString

two:
  name: MyString
  ip: MyString
  subnet: MyString
  gateway: MyString
  username: MyString
  password: MyString


File: /test\models\config_template_test.rb
require 'test_helper'

class ConfigTemplateTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
end


File: /test\models\config_test.rb
require 'test_helper'

class ConfigTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
end


File: /test\models\interface_test.rb
require 'test_helper'

class InterfaceTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
end


File: /test\test_helper.rb
ENV['RAILS_ENV'] ||= 'test'
require File.expand_path('../../config/environment', __FILE__)
require 'rails/test_help'

class ActiveSupport::TestCase
  # Setup all fixtures in test/fixtures/*.yml for all tests in alphabetical order.
  fixtures :all

  # Add more helper methods to be used by all tests here...
end


