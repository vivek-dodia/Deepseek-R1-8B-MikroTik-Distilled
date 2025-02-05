# Repository Information
Name: docker-freeradius-mysql-mikrotik

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/casudin.com/docker-freeradius-mysql-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .travis.yml
================================================
# travis.yml
sudo: required
services:
  - docker
env:
  - COMPOSE_VERSION=1.23.1
before_install:
  - curl -L https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
  - chmod +x docker-compose
  - sudo mv docker-compose /usr/local/bin
  - docker-compose --version
install:
  - docker build --pull --no-cache -t 2stacks/freeradius .
# Assist with ci test debugging:
#  - DEBUG=1
before_script:
  - image="2stacks/freeradius"
  - docker inspect "$image"
script: ./scripts/run-tests.sh
notifications:
  email:
    - 2stacks@2stacks.net
================================================

File: clients.conf
================================================
# -*- text -*-
##
## clients.conf -- client configuration directives
##
##	$Id: 76b300d3c55f1c5c052289b76bf28ac3a370bbb2 $
#######################################################################
#
#  Define RADIUS clients (usually a NAS, Access Point, etc.).
#
#  Defines a RADIUS client.
#
#  '127.0.0.1' is another name for 'localhost'.  It is enabled by default,
#  to allow testing of the server after an initial installation.  If you
#  are not going to be permitting RADIUS queries from localhost, we suggest
#  that you delete, or comment out, this entry.
#
#
#
#  Each client has a "short name" that is used to distinguish it from
#  other clients.
#
#  In version 1.x, the string after the word "client" was the IP
#  address of the client.  In 2.0, the IP address is configured via
#  the "ipaddr" or "ipv6addr" fields.  For compatibility, the 1.x
#  format is still accepted.
#
client localhost {
	#  Only *one* of ipaddr, ipv4addr, ipv6addr may be specified for
	#  a client.
	#
	#  ipaddr will accept IPv4 or IPv6 addresses with optional CIDR
	#  notation '/<mask>' to specify ranges.
	#
	#  ipaddr will accept domain names e.g. example.org resolving
	#  them via DNS.
	#
	#  If both A and AAAA records are found, A records will be
	#  used in preference to AAAA.
	ipaddr = 127.0.0.1
	#  Same as ipaddr but allows v4 addresses only. Requires A
	#  record for domain names.
#	ipv4addr = *	# any.  127.0.0.1 == localhost
	#  Same as ipaddr but allows v6 addresses only. Requires AAAA
	#  record for domain names.
#	ipv6addr = ::	# any.  ::1 == localhost
	#
	#  A note on DNS:  We STRONGLY recommend using IP addresses
	#  rather than host names.  Using host names means that the
	#  server will do DNS lookups when it starts, making it
	#  dependent on DNS.  i.e. If anything goes wrong with DNS,
	#  the server won't start!
	#
	#  The server also looks up the IP address from DNS once, and
	#  only once, when it starts.  If the DNS record is later
	#  updated, the server WILL NOT see that update.
	#
	#
	#  The transport protocol.
	#
	#  If unspecified, defaults to "udp", which is the traditional
	#  RADIUS transport.  It may also be "tcp", in which case the
	#  server will accept connections from this client ONLY over TCP.
	#
	proto = *
	#
	#  The shared secret use to "encrypt" and "sign" packets between
	#  the NAS and FreeRADIUS.  You MUST change this secret from the
	#  default, otherwise it's not a secret any more!
	#
	#  The secret can be any string, up to 8k characters in length.
	#
	#  Control codes can be entered vi octal encoding,
	#	e.g. "\101\102" == "AB"
	#  Quotation marks can be entered by escaping them,
	#	e.g. "foo\"bar"
	#
	#  A note on security:  The security of the RADIUS protocol
	#  depends COMPLETELY on this secret!  We recommend using a
	#  shared secret that is composed of:
	#
	#	upper case letters
	#	lower case letters
	#	numbers
	#
	#  And is at LEAST 8 characters long, preferably 16 characters in
	#  length.  The secret MUST be random, and should not be words,
	#  phrase, or anything else that is recognisable.
	#
	#  The default secret below is only for testing, and should
	#  not be used in any real environment.
	#
	secret = $ENV{RADIUS_KEY}
	#
	#  Old-style clients do not send a Message-Authenticator
	#  in an Access-Request.  RFC 5080 suggests that all clients
	#  SHOULD include it in an Access-Request.  The configuration
	#  item below allows the server to require it.  If a client
	#  is required to include a Message-Authenticator and it does
	#  not, then the packet will be silently discarded.
	#
	#  allowed values: yes, no
	require_message_authenticator = no
	#
	#  The short name is used as an alias for the fully qualified
	#  domain name, or the IP address.
	#
	#  It is accepted for compatibility with 1.x, but it is no
	#  longer necessary in >= 2.0
	#
#	shortname = localhost
	#
	# the following three fields are optional, but may be used by
	# checkrad.pl for simultaneous use checks
	#
	#
	# The nas_type tells 'checkrad.pl' which NAS-specific method to
	#  use to query the NAS for simultaneous use.
	#
	#  Permitted NAS types are:
	#
	#	cisco
	#	computone
	#	livingston
	#	juniper
	#	max40xx
	#	multitech
	#	netserver
	#	pathras
	#	patton
	#	portslave
	#	tc
	#	usrhiper
	#	other		# for all other types
	#
	nas_type	 = other	# localhost isn't usually a NAS...
	#
	#  The following two configurations are for future use.
	#  The 'naspasswd' file is currently used to store the NAS
	#  login name and password, which is used by checkrad.pl
	#  when querying the NAS for simultaneous use.
	#
#	login	   = !root
#	password	= someadminpas
	#
	#  As of 2.0, clients can also be tied to a virtual server.
	#  This is done by setting the "virtual_server" configuration
	#  item, as in the example below.
	#
#	virtual_server = home1
	#
	#  A pointer to the "home_server_pool" OR a "home_server"
	#  section that contains the CoA configuration for this
	#  client.  For an example of a coa home server or pool,
	#  see raddb/sites-available/originate-coa
#	coa_server = coa
	#
	#  Response window for proxied packets.  If non-zero,
	#  then the lower of (home, client) response_window
	#  will be used.
	#
	#  i.e. it can be used to lower the response_window
	#  packets from one client to a home server.  It cannot
	#  be used to raise the response_window.
	#
#	response_window = 10.0
	#
	#  Connection limiting for clients using "proto = tcp".
	#
	#  This section is ignored for clients sending UDP traffic
	#
	limit {
		#
		#  Limit the number of simultaneous TCP connections from a client
		#
		#  The default is 16.
		#  Setting this to 0 means "no limit"
		max_connections = 16
		#  The per-socket "max_requests" option does not exist.
		#
		#  The lifetime, in seconds, of a TCP connection.  After
		#  this lifetime, the connection will be closed.
		#
		#  Setting this to 0 means "forever".
		lifetime = 0
		#
		#  The idle timeout, in seconds, of a TCP connection.
		#  If no packets have been received over the connection for
		#  this time, the connection will be closed.
		#
		#  Setting this to 0 means "no timeout".
		#
		#  We STRONGLY RECOMMEND that you set an idle timeout.
		#
		idle_timeout = 30
	}
}
# IPv6 Client
client localhost_ipv6 {
	ipv6addr	= ::1
	secret		= $ENV{RADIUS_KEY}
}
# All IPv6 Site-local clients
#client sitelocal_ipv6 {
#	ipv6addr	= fe80::/16
#	secret		= testing123
#}
#client example.org {
#	ipaddr		= radius.example.org
#	secret		= testing123
#}
#
#  You can now specify one secret for a network of clients.
#  When a client request comes in, the BEST match is chosen.
#  i.e. The entry from the smallest possible network.
#
#client private-network-1 {
#	ipaddr		= 192.0.2.0/24
#	secret		= testing123-1
#}
#client private-network-2 {
#	ipaddr		= 198.51.100.0/24
#	secret		= testing123-2
#}
client  rad_clients {
	ipaddr          = $ENV{RAD_CLIENTS}
	secret          = $ENV{RADIUS_KEY}
	nas_type	= other
}
#######################################################################
#
#  Per-socket client lists.  The configuration entries are exactly
#  the same as above, but they are nested inside of a section.
#
#  You can have as many per-socket client lists as you have "listen"
#  sections, or you can re-use a list among multiple "listen" sections.
#
#  Un-comment this section, and edit a "listen" section to add:
#  "clients = per_socket_clients".  That IP address/port combination
#  will then accept ONLY the clients listed in this section.
#
#clients per_socket_clients {
#	client socket_client {
#		ipaddr = 192.0.2.4
#		secret = testing123
#	}
#}
================================================

File: queries.conf
================================================
# -*- text -*-
#location /etc/raddb/mods-config/sql/main/mysql/queries.conf
#  main/mysql/queries.conf-- MySQL configuration for default schema (schema.sql)
#
#  $Id: 40508024d5fd6a319bbb85775c3fe1e8388be656 $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Connection config
#######################################################################
# The character set is not configurable. The default character set of
# the mysql client library is used. To control the character set,
# create/edit my.cnf (typically in /etc/mysql/my.cnf or /etc/my.cnf)
# and enter
# [client]
# default-character-set = utf8
#
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'. '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#	Use Stripped-User-Name, if it's there.
#	Else use User-Name, if it's there,
#	Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
# Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming packets,
# not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
#default_user_profile = "DEFAULT"
#######################################################################
# NAS Query
#######################################################################
# This query retrieves the radius clients
#
# 0. Row ID (currently unused)
# 1. Name (or IP address)
# 2. Shortname
# 3. Type
# 4. Secret
# 5. Server
#######################################################################
client_query = "\
	SELECT nas_id,user_id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
# Authorization Queries
#######################################################################
# These queries compare the check items for the user
# in ${authcheck_table} and setup the reply items in
# ${authreply_table}. You can use any query/tables
# you want, but the return data for each row MUST
# be in the following order:
#
# 0. Row ID (currently unused)
# 1. UserName/GroupName
# 2. Item Attr Name
# 3. Item Attr Value
# 4. Item Attr Operation
#######################################################################
# Use these for case sensitive usernames.
#authorize_check_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authcheck_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#authorize_reply_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authreply_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#
#  The default queries are case insensitive. (for compatibility with
#  older versions of FreeRADIUS)
#
authorize_check_query = "\
	SELECT check_id,nas_id, username, attribute, value, op \
	FROM ${authcheck_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY check_id"
authorize_reply_query = "\
	SELECT reply_id,nas_id username, attribute, value, op \
	FROM ${authreply_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY reply_id"
#
#  Use these for case sensitive usernames.
#
#group_membership_query = "\
#	SELECT groupname \
#	FROM ${usergroup_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY priority"
group_membership_query = "\
	SELECT groupname \
	FROM ${usergroup_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY priority"
authorize_group_check_query = "\
	SELECT group_cek_id,nas_id, groupname, attribute, \
	Value, op \
	FROM ${groupcheck_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY group_cek_id"
authorize_group_reply_query = "\
	SELECT group_reply_id,nas_id, groupname, attribute, \
	value, op \
	FROM ${groupreply_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY group_reply_id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query	- query for the number of current connections
#			- If this is not defined, no simultaneous use checking
#			- will be performed by this module instance
# simul_verify_query	- query to return details of current connections
#				for verification
#			- Leave blank or commented out to disable verification step
#			- Note that the returned field order should not be changed.
#######################################################################
simul_count_query = "\
	SELECT COUNT(*) \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
simul_verify_query = "\
	SELECT \
		radacctid, acctsessionid, username, nasipaddress, nasportid, framedipaddress, \
		callingstationid, framedprotocol \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	column_list = "\
		acctsessionid,		acctuniqueid,		username, \
		realm,			nasipaddress,		nasportid, \
		nasporttype,		acctstarttime,		acctupdatetime, \
		acctstoptime,		acctsessiontime, 	acctauthentic, \
		connectinfo_start,	connectinfo_stop, 	acctinputoctets, \
		acctoutputoctets,	calledstationid, 	callingstationid, \
		acctterminatecause,	servicetype,		framedprotocol, \
		framedipaddress"
	type {
		accounting-on {
			#
			#  Bulk terminate all sessions associated with a given NAS
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctstoptime = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= '%{integer:Event-Timestamp}' \
						- UNIX_TIMESTAMP(acctstarttime), \
					acctterminatecause = '%{%{Acct-Terminate-Cause}:-NAS-Reboot}' \
				WHERE acctstoptime IS NULL \
				AND nasipaddress   = '%{NAS-IP-Address}' \
				AND acctstarttime <= FROM_UNIXTIME(\
					%{integer:Event-Timestamp})"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			#
			#  Insert a new record into the sessions table
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
			#
			#  Key constraints prevented us from inserting a new session,
			#  use the alternate query to update an existing session.
			#
			query = "\
				UPDATE ${....acct_table1} SET \
					acctstarttime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					acctupdatetime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					connectinfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		interim-update {
			#
			#  Update an existing session and calculate the interval
			#  between the last data we received for the session and this
			#  update. This can be used to find stale sessions.
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctupdatetime  = (@acctupdatetime_old:=acctupdatetime), \
					acctupdatetime  = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctinterval    = %{integer:Event-Timestamp} - \
						UNIX_TIMESTAMP(@acctupdatetime_old), \
					framedipaddress = '%{Framed-IP-Address}', \
					acctsessiontime = %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets = '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
		stop {
			#
			#  Session has terminated, update the stop time and statistics.
			#
			query = "\
				UPDATE ${....acct_table2} SET \
					acctstoptime	= FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets	= '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}', \
					acctterminatecause = '%{Acct-Terminate-Cause}', \
					connectinfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table2} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query	- Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query =	"\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES ( \
			'%{SQL-User-Name}', \
			'%{%{User-Password}:-%{Chap-Password}}', \
			'%{reply:Packet-Type}', \
			'%S')"
}
================================================

File: radiusd.conf
================================================
        #  'max_servers' doesn't seem to make much difference.
        #
        #  If this is the case, then the problem is MOST LIKELY that
        #  your back-end databases are taking too long to respond, and
        #  are preventing the server from responding in a timely manner.
        #
        #  The solution is NOT do keep increasing the 'max_servers'
        #  value, but instead to fix the underlying cause of the
        #  problem: slow database, or 'hostname_lookups=yes'.
        #
        #  For more information, see 'max_request_time', above.
        #
        max_servers = 32
        #  Server-pool size regulation.  Rather than making you guess
        #  how many servers you need, FreeRADIUS dynamically adapts to
        #  the load it sees, that is, it tries to maintain enough
        #  servers to handle the current load, plus a few spare
        #  servers to handle transient load spikes.
        #
        #  It does this by periodically checking how many servers are
        #  waiting for a request.  If there are fewer than
        #  min_spare_servers, it creates a new spare.  If there are
        #  more than max_spare_servers, some of the spares die off.
        #  The default values are probably OK for most sites.
        #
        min_spare_servers = 3
        max_spare_servers = 10
        #  When the server receives a packet, it places it onto an
        #  internal queue, where the worker threads (configured above)
        #  pick it up for processing.  The maximum size of that queue
        #  is given here.
        #
        #  When the queue is full, any new packets will be silently
        #  discarded.
        #
        #  The most common cause of the queue being full is that the
        #  server is dependent on a slow database, and it has received
        #  a large "spike" of traffic.  When that happens, there is
        #  very little you can do other than make sure the server
        #  receives less traffic, or make sure that the database can
        #  handle the load.
        #
#       max_queue_size = 65536
        #  Clean up old threads periodically.  For no reason other than
        #  it might be useful.
        #
        #  '0' is a special value meaning 'infinity', or 'the servers never
        #  exit'
        max_requests_per_server = 0
        #  Automatically limit the number of accounting requests.
        #  This configuration item tracks how many requests per second
        #  the server can handle.  It does this by tracking the
        #  packets/s received by the server for processing, and
        #  comparing that to the packets/s handled by the child
        #  threads.
        #
        #  If the received PPS is larger than the processed PPS, *and*
        #  the queue is more than half full, then new accounting
        #  requests are probabilistically discarded.  This lowers the
        #  number of packets that the server needs to process.  Over
        #  time, the server will "catch up" with the traffic.
        #
        #  Throwing away accounting packets is usually safe and low
        #  impact.  The NAS will retransmit them in a few seconds, or
        #  even a few minutes.  Vendors should read RFC 5080 Section 2.2.1
        #  to see how accounting packets should be retransmitted.  Using
        #  any other method is likely to cause network meltdowns.
        #
        auto_limit_acct = no
}
######################################################################
#
#  SNMP notifications.  Uncomment the following line to enable
#  snmptraps.  Note that you MUST also configure the full path
#  to the "snmptrap" command in the "trigger.conf" file.
#
#$INCLUDE trigger.conf
# MODULE CONFIGURATION
#
#  The names and configuration of each module is located in this section.
#
#  After the modules are defined here, they may be referred to by name,
#  in other sections of this configuration file.
#
modules {
        #
        #  Each module has a configuration as follows:
        #
        #       name [ instance ] {
        #               config_item = value
        #               ...
        #       }
        #
        #  The 'name' is used to load the 'rlm_name' library
        #  which implements the functionality of the module.
        #
        #  The 'instance' is optional.  To have two different instances
        #  of a module, it first must be referred to by 'name'.
        #  The different copies of the module are then created by
        #  inventing two 'instance' names, e.g. 'instance1' and 'instance2'
        #
        #  The instance names can then be used in later configuration
        #  INSTEAD of the original 'name'.  See the 'radutmp' configuration
        #  for an example.
        #
        #
        #  As of 3.0, modules are in mods-enabled/.  Files matching
        #  the regex /[a-zA-Z0-9_.]+/ are loaded.  The modules are
        #  initialized ONLY if they are referenced in a processing
        #  section, such as authorize, authenticate, accounting,
        #  pre/post-proxy, etc.
        #
        $INCLUDE mods-enabled/
}
# Instantiation
#
#  This section orders the loading of the modules.  Modules
#  listed here will get loaded BEFORE the later sections like
#  authorize, authenticate, etc. get examined.
#
#  This section is not strictly needed.  When a section like
#  authorize refers to a module, it's automatically loaded and
#  initialized.  However, some modules may not be listed in any
#  of the following sections, so they can be listed here.
#
#  Also, listing modules here ensures that you have control over
#  the order in which they are initialized.  If one module needs
#  something defined by another module, you can list them in order
#  here, and ensure that the configuration will be OK.
#
#  After the modules listed here have been loaded, all of the modules
#  in the "mods-enabled" directory will be loaded.  Loading the
#  "mods-enabled" directory means that unlike Version 2, you usually
#  don't need to list modules here.
#
instantiate {
        #
        # We list the counter module here so that it registers
        # the check_name attribute before any module which sets
        # it
#       daily
        # subsections here can be thought of as "virtual" modules.
        #
        # e.g. If you have two redundant SQL servers, and you want to
        # use them in the authorize and accounting sections, you could
        # place a "redundant" block in each section, containing the
        # exact same text.  Or, you could uncomment the following
        # lines, and list "redundant_sql" in the authorize and
        # accounting sections.
        #
        #  The "virtual" module defined here can also be used with
        #  dynamic expansions, under a few conditions:
        #
        #  * The section is "redundant", or "load-balance", or
        #    "redundant-load-balance"
        #  * The section contains modules ONLY, and no sub-sections
        #  * all modules in the section are using the same rlm_
        #    driver, e.g. They are all sql, or all ldap, etc.
        #
        #  When those conditions are satisfied, the server will
        #  automatically register a dynamic expansion, using the
        #  name of the "virtual" module.  In the example below,
        #  it will be "redundant_sql".  You can then use this expansion
        #  just like any other:
        #
        #       update reply {
        #               Filter-Id := "%{redundant_sql: ... }"
        #       }
        #
        #  In this example, the expansion is done via module "sql1",
        #  and if that expansion fails, using module "sql2".
        #
        #  For best results, configure the "pool" subsection of the
        #  module so that "retry_delay" is non-zero.  That will allow
        #  the redundant block to quickly ignore all "down" SQL
        #  databases.  If instead we have "retry_delay = 0", then
        #  every time the redundant block is used, the server will try
        #  to open a connection to every "down" database, causing
        #  problems.
        #
        #redundant redundant_sql {
        #       sql1
        #       sql2
        #}
}
######################################################################
#
#  Policies are virtual modules, similar to those defined in the
#  "instantiate" section above.
#
#  Defining a policy in one of the policy.d files means that it can be
#  referenced in multiple places as a *name*, rather than as a series of
#  conditions to match, and actions to take.
#
#  Policies are something like subroutines in a normal language, but
#  they cannot be called recursively. They MUST be defined in order.
#  If policy A calls policy B, then B MUST be defined before A.
#
######################################################################
policy {
        $INCLUDE policy.d/
}
######################################################################
#
#       Load virtual servers.
#
#       This next $INCLUDE line loads files in the directory that
#       match the regular expression: /[a-zA-Z0-9_.]+/
#
#       It allows you to define new virtual servers simply by placing
#       a file into the raddb/sites-enabled/ directory.
#
$INCLUDE sites-enabled/
bash-5.1# cat radiusd.conf 
# -*- text -*-
##
## radiusd.conf -- FreeRADIUS server configuration file - 3.0.17
##
##      http://www.freeradius.org/
##      $Id: 59e59f3ac443e75663333a5b7732664b67c5567d $
##
######################################################################
#
#       Read "man radiusd" before editing this file.  See the section
#       titled DEBUGGING.  It outlines a method where you can quickly
#       obtain the configuration you want, without running into
#       trouble.
#
#       Run the server in debugging mode, and READ the output.
#
#               $ radiusd -X
#
#       We cannot emphasize this point strongly enough.  The vast
#       majority of problems can be solved by carefully reading the
#       debugging output, which includes warnings about common issues,
#       and suggestions for how they may be fixed.
#
#       There may be a lot of output, but look carefully for words like:
#       "warning", "error", "reject", or "failure".  The messages there
#       will usually be enough to guide you to a solution.
#
#       If you are going to ask a question on the mailing list, then
#       explain what you are trying to do, and include the output from
#       debugging mode (radiusd -X).  Failure to do so means that all
#       of the responses to your question will be people telling you
#       to "post the output of radiusd -X".
######################################################################
#
#       The location of other config files and logfiles are declared
#       in this file.
#
#       Also general configuration for modules can be done in this
#       file, it is exported through the API to modules that ask for
#       it.
#
#       See "man radiusd.conf" for documentation on the format of this
#       file.  Note that the individual configuration items are NOT
#       documented in that "man" page.  They are only documented here,
#       in the comments.
#
#       The "unlang" policy language can be used to create complex
#       if / else policies.  See "man unlang" for details.
#
prefix = /usr
exec_prefix = ${prefix}
sysconfdir = /etc
localstatedir = /var
sbindir = ${exec_prefix}/sbin
logdir = /var/log/radius
raddbdir = ${sysconfdir}/raddb
radacctdir = /var/log/radius/radacct
#
#  name of the running server.  See also the "-n" command-line option.
name = radiusd
#  Location of config and logfiles.
confdir = ${raddbdir}
modconfdir = ${confdir}/mods-config
certdir = ${confdir}/certs
cadir   = ${confdir}/certs
run_dir = ${localstatedir}/run/${name}
# Should likely be ${localstatedir}/lib/radiusd
db_dir = ${raddbdir}
#
# libdir: Where to find the rlm_* modules.
#
#   This should be automatically set at configuration time.
#
#   If the server builds and installs, but fails at execution time
#   with an 'undefined symbol' error, then you can use the libdir
#   directive to work around the problem.
#
#   The cause is usually that a library has been installed on your
#   system in a place where the dynamic linker CANNOT find it.  When
#   executing as root (or another user), your personal environment MAY
#   be set up to allow the dynamic linker to find the library.  When
#   executing as a daemon, FreeRADIUS MAY NOT have the same
#   personalized configuration.
#
#   To work around the problem, find out which library contains that symbol,
#   and add the directory containing that library to the end of 'libdir',
#   with a colon separating the directory names.  NO spaces are allowed.
#
#   e.g. libdir = /usr/local/lib:/opt/package/lib
#
#   You can also try setting the LD_LIBRARY_PATH environment variable
#   in a script which starts the server.
#
#   If that does not work, then you can re-configure and re-build the
#   server to NOT use shared libraries, via:
#
#       ./configure --disable-shared
#       make
#       make install
#
libdir = /usr/lib/freeradius
#  pidfile: Where to place the PID of the RADIUS server.
#
#  The server may be signalled while it's running by using this
#  file.
#
#  This file is written when ONLY running in daemon mode.
#
#  e.g.:  kill -HUP `cat /var/run/radiusd/radiusd.pid`
#
pidfile = ${run_dir}/${name}.pid
#
#  correct_escapes: use correct backslash escaping
#
#  Prior to version 3.0.5, the handling of backslashes was a little
#  awkward, i.e. "wrong".  In some cases, to get one backslash into
#  a regex, you had to put 4 in the config files.
#
#  Version 3.0.5 fixes that.  However, for backwards compatibility,
#  the new method of escaping is DISABLED BY DEFAULT.  This means
#  that upgrading to 3.0.5 won't break your configuration.
#
#  If you don't have double backslashes (i.e. \\) in your configuration,
#  this won't matter to you.  If you do have them, fix that to use only
#  one backslash, and then set "correct_escapes = true".
#
#  You can check for this by doing:
#
#       $ grep '\\\\' $(find raddb -type f -print)
#
correct_escapes = true
#  panic_action: Command to execute if the server dies unexpectedly.
#
#  FOR PRODUCTION SYSTEMS, ACTIONS SHOULD ALWAYS EXIT.
#  AN INTERACTIVE ACTION MEANS THE SERVER IS NOT RESPONDING TO REQUESTS.
#  AN INTERACTICE ACTION MEANS THE SERVER WILL NOT RESTART.
#
#  THE SERVER MUST NOT BE ALLOWED EXECUTE UNTRUSTED PANIC ACTION CODE
#  PATTACH CAN BE USED AS AN ATTACK VECTOR.
#
#  The panic action is a command which will be executed if the server
#  receives a fatal, non user generated signal, i.e. SIGSEGV, SIGBUS,
#  SIGABRT or SIGFPE.
#
#  This can be used to start an interactive debugging session so
#  that information regarding the current state of the server can
#  be acquired.
#
#  The following string substitutions are available:
#  - %e   The currently executing program e.g. /sbin/radiusd
#  - %p   The PID of the currently executing program e.g. 12345
#
#  Standard ${} substitutions are also allowed.
#
#  An example panic action for opening an interactive session in GDB would be:
#
#panic_action = "gdb %e %p"
#
#  Again, don't use that on a production system.
#
#  An example panic action for opening an automated session in GDB would be:
#
#panic_action = "gdb -silent -x ${raddbdir}/panic.gdb %e %p 2>&1 | tee ${logdir}/gdb-${name}-%p.log"
#
#  That command can be used on a production system.
#
#  max_request_time: The maximum time (in seconds) to handle a request.
#
#  Requests which take more time than this to process may be killed, and
#  a REJECT message is returned.
#
#  WARNING: If you notice that requests take a long time to be handled,
#  then this MAY INDICATE a bug in the server, in one of the modules
#  used to handle a request, OR in your local configuration.
#
#  This problem is most often seen when using an SQL database.  If it takes
#  more than a second or two to receive an answer from the SQL database,
#  then it probably means that you haven't indexed the database.  See your
#  SQL server documentation for more information.
#
#  Useful range of values: 5 to 120
#
max_request_time = 30
#  cleanup_delay: The time to wait (in seconds) before cleaning up
#  a reply which was sent to the NAS.
#
#  The RADIUS request is normally cached internally for a short period
#  of time, after the reply is sent to the NAS.  The reply packet may be
#  lost in the network, and the NAS will not see it.  The NAS will then
#  re-send the request, and the server will respond quickly with the
#  cached reply.
#
#  If this value is set too low, then duplicate requests from the NAS
#  MAY NOT be detected, and will instead be handled as separate requests.
#
#  If this value is set too high, then the server will cache too many
#  requests, and some new requests may get blocked.  (See 'max_requests'.)
#
#  Useful range of values: 2 to 10
#
cleanup_delay = 5
#  max_requests: The maximum number of requests which the server keeps
#  track of.  This should be 256 multiplied by the number of clients.
#  e.g. With 4 clients, this number should be 1024.
#
#  If this number is too low, then when the server becomes busy,
#  it will not respond to any new requests, until the 'cleanup_delay'
#  time has passed, and it has removed the old requests.
#
#  If this number is set too high, then the server will use a bit more
#  memory for no real benefit.
#
#  If you aren't sure what it should be set to, it's better to set it
#  too high than too low.  Setting it to 1000 per client is probably
#  the highest it should be.
#
#  Useful range of values: 256 to infinity
#
max_requests = 16384
#  hostname_lookups: Log the names of clients or just their IP addresses
#  e.g., www.freeradius.org (on) or 206.47.27.232 (off).
#
#  The default is 'off' because it would be overall better for the net
#  if people had to knowingly turn this feature on, since enabling it
#  means that each client request will result in AT LEAST one lookup
#  request to the nameserver.   Enabling hostname_lookups will also
#  mean that your server may stop randomly for 30 seconds from time
#  to time, if the DNS requests take too long.
#
#  Turning hostname lookups off also means that the server won't block
#  for 30 seconds, if it sees an IP address which has no name associated
#  with it.
#
#  allowed values: {no, yes}
#
hostname_lookups = no
#
#  Logging section.  The various "log_*" configuration items
#  will eventually be moved here.
#
log {
        #
        #  Destination for log messages.  This can be one of:
        #
        #       files - log to "file", as defined below.
        #       syslog - to syslog (see also the "syslog_facility", below.
        #       stdout - standard output
        #       stderr - standard error.
        #
        #  The command-line option "-X" over-rides this option, and forces
        #  logging to go to stdout.
        #
        #destination = files
        destination = stdout
        #
        #  Highlight important messages sent to stderr and stdout.
        #
        #  Option will be ignored (disabled) if output if TERM is not
        #  an xterm or output is not to a TTY.
        #
        colourise = yes
        #
        #  The logging messages for the server are appended to the
        #  tail of this file if destination == "files"
        #
        #  If the server is running in debugging mode, this file is
        #  NOT used.
        #
        file = ${logdir}/radius.log
        #
        #  Which syslog facility to use, if ${destination} == "syslog"
        #
        #  The exact values permitted here are OS-dependent.  You probably
        #  don't want to change this.
        #
        syslog_facility = daemon
        #  Log the full User-Name attribute, as it was found in the request.
        #
        # allowed values: {no, yes}
        #
        stripped_names = no
        #  Log authentication requests to the log file.
        #
        #  allowed values: {no, yes}
        #
        #auth = yes
        auth = $ENV{RAD_DEBUG}
        #  Log passwords with the authentication requests.
        #  auth_badpass  - logs password if it's rejected
        #  auth_goodpass - logs password if it's correct
        #
        #  allowed values: {no, yes}
        #
        #auth_badpass = yes
        auth_badpass = $ENV{RAD_DEBUG}
        #auth_goodpass = yes
        auth_goodpass = $ENV{RAD_DEBUG}
        #  Log additional text at the end of the "Login OK" messages.
        #  for these to work, the "auth" and "auth_goodpass" or "auth_badpass"
        #  configurations above have to be set to "yes".
        #
        #  The strings below are dynamically expanded, which means that
        #  you can put anything you want in them.  However, note that
        #  this expansion can be slow, and can negatively impact server
        #  performance.
        #
#       msg_goodpass = ""
#       msg_badpass = ""
        #  The message when the user exceeds the Simultaneous-Use limit.
        #
        msg_denied = "You are already logged in - access denied"
}
#  The program to execute to do concurrency checks.
checkrad = ${sbindir}/checkrad
# SECURITY CONFIGURATION
#
#  There may be multiple methods of attacking on the server.  This
#  section holds the configuration items which minimize the impact
#  of those attacks
#
security {
        #  chroot: directory where the server does "chroot".
        #
        #  The chroot is done very early in the process of starting
        #  the server.  After the chroot has been performed it
        #  switches to the "user" listed below (which MUST be
        #  specified).  If "group" is specified, it switches to that
        #  group, too.  Any other groups listed for the specified
        #  "user" in "/etc/group" are also added as part of this
        #  process.
        #
        #  The current working directory (chdir / cd) is left
        #  *outside* of the chroot until all of the modules have been
        #  initialized.  This allows the "raddb" directory to be left
        #  outside of the chroot.  Once the modules have been
        #  initialized, it does a "chdir" to ${logdir}.  This means
        #  that it should be impossible to break out of the chroot.
        #
        #  If you are worried about security issues related to this
        #  use of chdir, then simply ensure that the "raddb" directory
        #  is inside of the chroot, end be sure to do "cd raddb"
        #  BEFORE starting the server.
        #
        #  If the server is statically linked, then the only files
        #  that have to exist in the chroot are ${run_dir} and
        #  ${logdir}.  If you do the "cd raddb" as discussed above,
        #  then the "raddb" directory has to be inside of the chroot
        #  directory, too.
        #
#       chroot = /path/to/chroot/directory
        # user/group: The name (or #number) of the user/group to run radiusd as.
        #
        #   If these are commented out, the server will run as the
        #   user/group that started it.  In order to change to a
        #   different user/group, you MUST be root ( or have root
        #   privileges ) to start the server.
        #
        #   We STRONGLY recommend that you run the server with as few
        #   permissions as possible.  That is, if you're not using
        #   shadow passwords, the user and group items below should be
        #   set to radius'.
        #
        #  NOTE that some kernels refuse to setgid(group) when the
        #  value of (unsigned)group is above 60000; don't use group
        #  "nobody" on these systems!
        #
        #  On systems with shadow passwords, you might have to set
        #  'group = shadow' for the server to be able to read the
        #  shadow password file.  If you can authenticate users while
        #  in debug mode, but not in daemon mode, it may be that the
        #  debugging mode server is running as a user that can read
        #  the shadow info, and the user listed below can not.
        #
        #  The server will also try to use "initgroups" to read
        #  /etc/groups.  It will join all groups where "user" is a
        #  member.  This can allow for some finer-grained access
        #  controls.
        #
        user = radius
        group = radius
        #  Core dumps are a bad thing.  This should only be set to
        #  'yes' if you're debugging a problem with the server.
        #
        #  allowed values: {no, yes}
        #
        allow_core_dumps = no
        #
        #  max_attributes: The maximum number of attributes
        #  permitted in a RADIUS packet.  Packets which have MORE
        #  than this number of attributes in them will be dropped.
        #
        #  If this number is set too low, then no RADIUS packets
        #  will be accepted.
        #
        #  If this number is set too high, then an attacker may be
        #  able to send a small number of packets which will cause
        #  the server to use all available memory on the machine.
        #
        #  Setting this number to 0 means "allow any number of attributes"
        max_attributes = 200
        #
        #  reject_delay: When sending an Access-Reject, it can be
        #  delayed for a few seconds.  This may help slow down a DoS
        #  attack.  It also helps to slow down people trying to brute-force
        #  crack a users password.
        #
        #  Setting this number to 0 means "send rejects immediately"
        #
        #  If this number is set higher than 'cleanup_delay', then the
        #  rejects will be sent at 'cleanup_delay' time, when the request
        #  is deleted from the internal cache of requests.
        #
        #  As of Version 3.0.5, "reject_delay" has sub-second resolution.
        #  e.g. "reject_delay =  1.4" seconds is possible.
        #
        #  Useful ranges: 1 to 5
        reject_delay = 1
        #
        #  status_server: Whether or not the server will respond
        #  to Status-Server requests.
        #
        #  When sent a Status-Server message, the server responds with
        #  an Access-Accept or Accounting-Response packet.
        #
        #  This is mainly useful for administrators who want to "ping"
        #  the server, without adding test users, or creating fake
        #  accounting packets.
        #
        #  It's also useful when a NAS marks a RADIUS server "dead".
        #  The NAS can periodically "ping" the server with a Status-Server
        #  packet.  If the server responds, it must be alive, and the
        #  NAS can start using it for real requests.
        #
        #  See also raddb/sites-available/status
        #
        status_server = yes
        #
        #  allow_vulnerable_openssl: Allow the server to start with
        #  versions of OpenSSL known to have critical vulnerabilities.
        #
        #  This check is based on the version number reported by libssl
        #  and may not reflect patches applied to libssl by
        #  distribution maintainers.
        # Alpine 3.9 switched to openssl v1.1.1a-r1
        # CVE-2016-6309 was patch in openssl v1.1.0b
        allow_vulnerable_openssl = 'CVE-2016-6309'
}
# PROXY CONFIGURATION
#
#  proxy_requests: Turns proxying of RADIUS requests on or off.
#
#  The server has proxying turned on by default.  If your system is NOT
#  set up to proxy requests to another server, then you can turn proxying
#  off here.  This will save a small amount of resources on the server.
#
#  If you have proxying turned off, and your configuration files say
#  to proxy a request, then an error message will be logged.
#
#  To disable proxying, change the "yes" to "no", and comment the
#  $INCLUDE line.
#
#  allowed values: {no, yes}
#
#proxy_requests  = yes
proxy_requests  = no
#$INCLUDE proxy.conf
# CLIENTS CONFIGURATION
#
#  Client configuration is defined in "clients.conf".
#
#  The 'clients.conf' file contains all of the information from the old
#  'clients' and 'naslist' configuration files.  We recommend that you
#  do NOT use 'client's or 'naslist', although they are still
#  supported.
#
#  Anything listed in 'clients.conf' will take precedence over the
#  information from the old-style configuration files.
#
$INCLUDE clients.conf
# THREAD POOL CONFIGURATION
#
#  The thread pool is a long-lived group of threads which
#  take turns (round-robin) handling any incoming requests.
#
#  You probably want to have a few spare threads around,
#  so that high-load situations can be handled immediately.  If you
#  don't have any spare threads, then the request handling will
#  be delayed while a new thread is created, and added to the pool.
#
#  You probably don't want too many spare threads around,
#  otherwise they'll be sitting there taking up resources, and
#  not doing anything productive.
#
#  The numbers given below should be adequate for most situations.
#
thread pool {
        #  Number of servers to start initially --- should be a reasonable
        #  ballpark figure.
        start_servers = 5
        #  Limit on the total number of servers running.
        #
        #  If this limit is ever reached, clients will be LOCKED OUT, so it
        #  should NOT BE SET TOO LOW.  It is intended mainly as a brake to
        #  keep a runaway server from taking the system with it as it spirals
        #  down...
        #
        #  You may find that the server is regularly reaching the
        #  'max_servers' number of threads, and that increasing
        #  'max_servers' doesn't seem to make much difference.
        #
        #  If this is the case, then the problem is MOST LIKELY that
        #  your back-end databases are taking too long to respond, and
        #  are preventing the server from responding in a timely manner.
        #
        #  The solution is NOT do keep increasing the 'max_servers'
        #  value, but instead to fix the underlying cause of the
        #  problem: slow database, or 'hostname_lookups=yes'.
        #
        #  For more information, see 'max_request_time', above.
        #
        max_servers = 32
        #  Server-pool size regulation.  Rather than making you guess
        #  how many servers you need, FreeRADIUS dynamically adapts to
        #  the load it sees, that is, it tries to maintain enough
        #  servers to handle the current load, plus a few spare
        #  servers to handle transient load spikes.
        #
        #  It does this by periodically checking how many servers are
        #  waiting for a request.  If there are fewer than
        #  min_spare_servers, it creates a new spare.  If there are
        #  more than max_spare_servers, some of the spares die off.
        #  The default values are probably OK for most sites.
        #
        min_spare_servers = 3
        max_spare_servers = 10
        #  When the server receives a packet, it places it onto an
        #  internal queue, where the worker threads (configured above)
        #  pick it up for processing.  The maximum size of that queue
        #  is given here.
        #
        #  When the queue is full, any new packets will be silently
        #  discarded.
        #
        #  The most common cause of the queue being full is that the
        #  server is dependent on a slow database, and it has received
        #  a large "spike" of traffic.  When that happens, there is
        #  very little you can do other than make sure the server
        #  receives less traffic, or make sure that the database can
        #  handle the load.
        #
#       max_queue_size = 65536
        #  Clean up old threads periodically.  For no reason other than
        #  it might be useful.
        #
        #  '0' is a special value meaning 'infinity', or 'the servers never
        #  exit'
        max_requests_per_server = 0
        #  Automatically limit the number of accounting requests.
        #  This configuration item tracks how many requests per second
        #  the server can handle.  It does this by tracking the
        #  packets/s received by the server for processing, and
        #  comparing that to the packets/s handled by the child
        #  threads.
        #
        #  If the received PPS is larger than the processed PPS, *and*
        #  the queue is more than half full, then new accounting
        #  requests are probabilistically discarded.  This lowers the
        #  number of packets that the server needs to process.  Over
        #  time, the server will "catch up" with the traffic.
        #
        #  Throwing away accounting packets is usually safe and low
        #  impact.  The NAS will retransmit them in a few seconds, or
        #  even a few minutes.  Vendors should read RFC 5080 Section 2.2.1
        #  to see how accounting packets should be retransmitted.  Using
        #  any other method is likely to cause network meltdowns.
        #
        auto_limit_acct = no
}
######################################################################
#
#  SNMP notifications.  Uncomment the following line to enable
#  snmptraps.  Note that you MUST also configure the full path
#  to the "snmptrap" command in the "trigger.conf" file.
#
#$INCLUDE trigger.conf
# MODULE CONFIGURATION
#
#  The names and configuration of each module is located in this section.
#
#  After the modules are defined here, they may be referred to by name,
#  in other sections of this configuration file.
#
modules {
        #
        #  Each module has a configuration as follows:
        #
        #       name [ instance ] {
        #               config_item = value
        #               ...
        #       }
        #
        #  The 'name' is used to load the 'rlm_name' library
        #  which implements the functionality of the module.
        #
        #  The 'instance' is optional.  To have two different instances
        #  of a module, it first must be referred to by 'name'.
        #  The different copies of the module are then created by
        #  inventing two 'instance' names, e.g. 'instance1' and 'instance2'
        #
        #  The instance names can then be used in later configuration
        #  INSTEAD of the original 'name'.  See the 'radutmp' configuration
        #  for an example.
        #
        #
        #  As of 3.0, modules are in mods-enabled/.  Files matching
        #  the regex /[a-zA-Z0-9_.]+/ are loaded.  The modules are
        #  initialized ONLY if they are referenced in a processing
        #  section, such as authorize, authenticate, accounting,
        #  pre/post-proxy, etc.
        #
        $INCLUDE mods-enabled/
}
# Instantiation
#
#  This section orders the loading of the modules.  Modules
#  listed here will get loaded BEFORE the later sections like
#  authorize, authenticate, etc. get examined.
#
#  This section is not strictly needed.  When a section like
#  authorize refers to a module, it's automatically loaded and
#  initialized.  However, some modules may not be listed in any
#  of the following sections, so they can be listed here.
#
#  Also, listing modules here ensures that you have control over
#  the order in which they are initialized.  If one module needs
#  something defined by another module, you can list them in order
#  here, and ensure that the configuration will be OK.
#
#  After the modules listed here have been loaded, all of the modules
#  in the "mods-enabled" directory will be loaded.  Loading the
#  "mods-enabled" directory means that unlike Version 2, you usually
#  don't need to list modules here.
#
instantiate {
        #
        # We list the counter module here so that it registers
        # the check_name attribute before any module which sets
        # it
#       daily
        # subsections here can be thought of as "virtual" modules.
        #
        # e.g. If you have two redundant SQL servers, and you want to
        # use them in the authorize and accounting sections, you could
        # place a "redundant" block in each section, containing the
        # exact same text.  Or, you could uncomment the following
        # lines, and list "redundant_sql" in the authorize and
        # accounting sections.
        #
        #  The "virtual" module defined here can also be used with
        #  dynamic expansions, under a few conditions:
        #
        #  * The section is "redundant", or "load-balance", or
        #    "redundant-load-balance"
        #  * The section contains modules ONLY, and no sub-sections
        #  * all modules in the section are using the same rlm_
        #    driver, e.g. They are all sql, or all ldap, etc.
        #
        #  When those conditions are satisfied, the server will
        #  automatically register a dynamic expansion, using the
        #  name of the "virtual" module.  In the example below,
        #  it will be "redundant_sql".  You can then use this expansion
        #  just like any other:
        #
        #       update reply {
        #               Filter-Id := "%{redundant_sql: ... }"
        #       }
        #
        #  In this example, the expansion is done via module "sql1",
        #  and if that expansion fails, using module "sql2".
        #
        #  For best results, configure the "pool" subsection of the
        #  module so that "retry_delay" is non-zero.  That will allow
        #  the redundant block to quickly ignore all "down" SQL
        #  databases.  If instead we have "retry_delay = 0", then
        #  every time the redundant block is used, the server will try
        #  to open a connection to every "down" database, causing
        #  problems.
        #
        #redundant redundant_sql {
        #       sql1
        #       sql2
        #}
}
######################################################################
#
#  Policies are virtual modules, similar to those defined in the
#  "instantiate" section above.
#
#  Defining a policy in one of the policy.d files means that it can be
#  referenced in multiple places as a *name*, rather than as a series of
#  conditions to match, and actions to take.
#
#  Policies are something like subroutines in a normal language, but
#  they cannot be called recursively. They MUST be defined in order.
#  If policy A calls policy B, then B MUST be defined before A.
#
######################################################################
policy {
        $INCLUDE policy.d/
}
######################################################################
#
#       Load virtual servers.
#
#       This next $INCLUDE line loads files in the directory that
#       match the regular expression: /[a-zA-Z0-9_.]+/
#
#       It allows you to define new virtual servers simply by placing
#       a file into the raddb/sites-enabled/ directory.
#
$INCLUDE sites-enabled/
######################################################################
#
#       All of the other configuration sections like "authorize {}",
#       "authenticate {}", "accounting {}", have been moved to the
#       the file:
#
#               raddb/sites-available/default
#
#       This is the "default" virtual server that has the same
#       configuration as in version 1.0.x and 1.1.x.  The default
#       installation enables this virtual server.  You should
#       edit it to create policies for your local site.
#
#       For more documentation on virtual servers, see:
#
#               raddb/sites-available/README
#
######################################################################
================================================

File: sql.conf
================================================
#location /etc/raddb/mods-available/sql no extention
# -*- text -*-
##
## sql.conf -- SQL modules
##
##      $Id: 4a59483c35c77f573fb177919e19ba4434cc3da1 $
######################################################################
#
#  Configuration for the SQL module
#
#  The database schemas and queries are located in subdirectories:
#
#       sql/<DB>/main/schema.sql        Schema
#       sql/<DB>/main/queries.conf      Authorisation and Accounting queries
#
#  Where "DB" is mysql, mssql, oracle, or postgresql.
#
#
sql {
        # The sub-module to use to execute queries. This should match
        # the database you're attempting to connect to.
        #
        #    * rlm_sql_mysql
        #    * rlm_sql_mssql
        #    * rlm_sql_oracle
        #    * rlm_sql_postgresql
        #    * rlm_sql_sqlite
        #    * rlm_sql_null (log queries to disk)
        #
        driver = "rlm_sql_mysql"
        #
        #       Several drivers accept specific options, to set them, a
        #       config section with the the name as the driver should be added
        #       to the sql instance.
        #
        #       Driver specific options are:
        #
        #       sqlite {
        #               # Path to the sqlite database
        #               filename = "/tmp/freeradius.db"
        #
        #               # How long to wait for write locks on the database to be
        #               # released (in ms) before giving up.
        #               busy_timeout = 200
        #
        #               # If the file above does not exist and bootstrap is set
        #               # a new database file will be created, and the SQL statements
        #               # contained within the bootstrap file will be executed.
        #               bootstrap = "${modconfdir}/${..:name}/main/sqlite/schema.sql"
        #       }
        #
        #       mysql {
        #               # If any of the files below are set, TLS encryption is enabled
        #               tls {
        #                       ca_file = "/etc/ssl/certs/my_ca.crt"
        #                       ca_path = "/etc/ssl/certs/"
        #                       certificate_file = "/etc/ssl/certs/private/client.crt"
        #                       private_key_file = "/etc/ssl/certs/private/client.key"
        #                       cipher = "DHE-RSA-AES256-SHA:AES128-SHA"
        #               }
        #
        #               # If yes, (or auto and libmysqlclient reports warnings are
        #               # available), will retrieve and log additional warnings from
        #               # the server if an error has occured. Defaults to 'auto'
        #               warnings = auto
        #       }
        #
        #       postgresql {
        #
        #               # unlike MySQL, which has a tls{} connection configuration, postgresql
        #               # uses its connection parameters - see the radius_db option below in
        #               # this file
        #
        #               # Send application_name to the postgres server
        #               # Only supported in PG 9.0 and greater. Defaults to no.
        #               send_application_name = yes
        #       }
        #
        # The dialect of SQL you want to use, this should usually match
        # the driver you selected above.
        #
        # If you're using rlm_sql_null, then it should be the type of
        # database the logged queries are going to be executed against.
        dialect = "mysql"
        # Connection info:
        #
        server = $ENV{DB_HOST}
        port = $ENV{DB_PORT}
        login = $ENV{DB_USER}
        password = $ENV{DB_PASS}
        # Database table configuration for everything except Oracle
        radius_db = $ENV{DB_NAME}
        # If you are using Oracle then use this instead
#       radius_db = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=your_sid)))"
        # If you're using postgresql this can also be used instead of the connection info parameters
#       radius_db = "dbname=radius host=localhost user=radius password=raddpass"
        # Postgreql doesn't take tls{} options in its module config like mysql does - if you want to
        # use SSL connections then use this form of connection info parameter
#        radius_db = "host=localhost port=5432 dbname=radius user=radius password=raddpass sslmode=verify-full sslcert=/etc/ssl/client.crt sslkey=/etc/ssl/client.key sslrootcert=/etc/ssl/ca.crt" 
        # If you want both stop and start records logged to the
        # same SQL table, leave this as is.  If you want them in
        # different tables, put the start table in acct_table1
        # and stop table in acct_table2
        acct_table1 = "radacct"
        acct_table2 = "radacct"
        # Allow for storing data after authentication
        postauth_table = "radpostauth"
        # Tables containing 'check' items
        authcheck_table = "radcheck"
        groupcheck_table = "radgroupcheck"
        # Tables containing 'reply' items
        authreply_table = "radreply"
        groupreply_table = "radgroupreply"
        # Table to keep group info
        usergroup_table = "radusergroup"
        # If set to 'yes' (default) we read the group tables unless Fall-Through = no in the reply table.
        # If set to 'no' we do not read the group tables unless Fall-Through = yes in the reply table.
#       read_groups = yes
        # If set to 'yes' (default) we read profiles unless Fall-Through = no in the groupreply table.
        # If set to 'no' we do not read profiles unless Fall-Through = yes in the groupreply table.
#       read_profiles = yes
        # Remove stale session if checkrad does not see a double login
        delete_stale_sessions = yes
        # Write SQL queries to a logfile. This is potentially useful for tracing
        # issues with authorization queries.  See also "logfile" directives in
        # mods-config/sql/main/*/queries.conf.  You can enable per-section logging
        # by enabling "logfile" there, or global logging by enabling "logfile" here.
        #
        # Per-section logging can be disabled by setting "logfile = ''"
         logfile = ${logdir}/sqllog.sql
        #  Set the maximum query duration and connection timeout
        #  for rlm_sql_mysql.
#       query_timeout = 5
        #  As of version 3.0, the "pool" section has replaced the
        #  following configuration items:
        #
        #  num_sql_socks
        #  connect_failure_retry_delay
        #  lifetime
        #  max_queries
        #
        #  The connection pool is new for 3.0, and will be used in many
        #  modules, for all kinds of connection-related activity.
        #
        # When the server is not threaded, the connection pool
        # limits are ignored, and only one connection is used.
        #
        # If you want to have multiple SQL modules re-use the same
        # connection pool, use "pool = name" instead of a "pool"
        # section.  e.g.
        #
        #       sql1 {
        #           ...
        #           pool {
        #                ...
        #           }
        #       }
        #
        #       # sql2 will use the connection pool from sql1
        #       sql2 {
        #            ...
        #            pool = sql1
        #       }
        #
        pool {
                #  Connections to create during module instantiation.
                #  If the server cannot create specified number of
                #  connections during instantiation it will exit.
                #  Set to 0 to allow the server to start without the
                #  database being available.
                start = ${thread[pool].start_servers}
                #  Minimum number of connections to keep open
                min = ${thread[pool].min_spare_servers}
                #  Maximum number of connections
                #
                #  If these connections are all in use and a new one
                #  is requested, the request will NOT get a connection.
                #
                #  Setting 'max' to LESS than the number of threads means
                #  that some threads may starve, and you will see errors
                #  like 'No connections available and at max connection limit'
                #
                #  Setting 'max' to MORE than the number of threads means
                #  that there are more connections than necessary.
                max = ${thread[pool].max_servers}
                #  Spare connections to be left idle
                #
                #  NOTE: Idle connections WILL be closed if "idle_timeout"
                #  is set.  This should be less than or equal to "max" above.
                spare = ${thread[pool].max_spare_servers}
                #  Number of uses before the connection is closed
                #
                #  0 means "infinite"
                uses = 0
                #  The number of seconds to wait after the server tries
                #  to open a connection, and fails.  During this time,
                #  no new connections will be opened.
                retry_delay = 30
                # The lifetime (in seconds) of the connection
                lifetime = 0
                #  idle timeout (in seconds).  A connection which is
                #  unused for this length of time will be closed.
                idle_timeout = 60
                #  NOTE: All configuration settings are enforced.  If a
                #  connection is closed because of "idle_timeout",
                #  "uses", or "lifetime", then the total number of
                #  connections MAY fall below "min".  When that
                #  happens, it will open a new connection.  It will
                #  also log a WARNING message.
                #
                #  The solution is to either lower the "min" connections,
                #  or increase lifetime/idle_timeout.
        }
        # Set to 'yes' to read radius clients from the database ('nas' table)
        # Clients will ONLY be read on server startup.
        read_clients = yes
        # Table to keep radius client info
        client_table = "nas"
        #
        # The group attribute specific to this instance of rlm_sql
        #
        # This entry should be used for additional instances (sql foo {})
        # of the SQL module.
#       group_attribute = "${.:instance}-SQL-Group"
        # This entry should be used for the default instance (sql {})
        # of the SQL module.
        group_attribute = "SQL-Group"
        # Read database-specific queries
        $INCLUDE ${modconfdir}/${.:name}/main/${dialect}/queries.conf
}
================================================

File: queries.conf
================================================
# -*- text -*-
#location /etc/raddb/mods-config/sql/main/mysql/queries.conf
#  main/mysql/queries.conf-- MySQL configuration for default schema (schema.sql)
#
#  $Id: 40508024d5fd6a319bbb85775c3fe1e8388be656 $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Connection config
#######################################################################
# The character set is not configurable. The default character set of
# the mysql client library is used. To control the character set,
# create/edit my.cnf (typically in /etc/mysql/my.cnf or /etc/my.cnf)
# and enter
# [client]
# default-character-set = utf8
#
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'. '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#	Use Stripped-User-Name, if it's there.
#	Else use User-Name, if it's there,
#	Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
# Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming packets,
# not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
#default_user_profile = "DEFAULT"
#######################################################################
# NAS Query
#######################################################################
# This query retrieves the radius clients
#
# 0. Row ID (currently unused)
# 1. Name (or IP address)
# 2. Shortname
# 3. Type
# 4. Secret
# 5. Server
#######################################################################
client_query = "\
	SELECT nas_id,user_id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
# Authorization Queries
#######################################################################
# These queries compare the check items for the user
# in ${authcheck_table} and setup the reply items in
# ${authreply_table}. You can use any query/tables
# you want, but the return data for each row MUST
# be in the following order:
#
# 0. Row ID (currently unused)
# 1. UserName/GroupName
# 2. Item Attr Name
# 3. Item Attr Value
# 4. Item Attr Operation
#######################################################################
# Use these for case sensitive usernames.
#authorize_check_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authcheck_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#authorize_reply_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authreply_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#
#  The default queries are case insensitive. (for compatibility with
#  older versions of FreeRADIUS)
#
authorize_check_query = "\
	SELECT check_id,nas_id, username, attribute, value, op \
	FROM ${authcheck_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY check_id"
authorize_reply_query = "\
	SELECT reply_id,nas_id username, attribute, value, op \
	FROM ${authreply_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY reply_id"
#
#  Use these for case sensitive usernames.
#
#group_membership_query = "\
#	SELECT groupname \
#	FROM ${usergroup_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY priority"
group_membership_query = "\
	SELECT groupname \
	FROM ${usergroup_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY priority"
authorize_group_check_query = "\
	SELECT group_cek_id,nas_id, groupname, attribute, \
	Value, op \
	FROM ${groupcheck_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY group_cek_id"
authorize_group_reply_query = "\
	SELECT group_reply_id,nas_id, groupname, attribute, \
	value, op \
	FROM ${groupreply_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY group_reply_id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query	- query for the number of current connections
#			- If this is not defined, no simultaneous use checking
#			- will be performed by this module instance
# simul_verify_query	- query to return details of current connections
#				for verification
#			- Leave blank or commented out to disable verification step
#			- Note that the returned field order should not be changed.
#######################################################################
simul_count_query = "\
	SELECT COUNT(*) \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
simul_verify_query = "\
	SELECT \
		radacctid, acctsessionid, username, nasipaddress, nasportid, framedipaddress, \
		callingstationid, framedprotocol \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	column_list = "\
		acctsessionid,		acctuniqueid,		username, \
		realm,			nasipaddress,		nasportid, \
		nasporttype,		acctstarttime,		acctupdatetime, \
		acctstoptime,		acctsessiontime, 	acctauthentic, \
		connectinfo_start,	connectinfo_stop, 	acctinputoctets, \
		acctoutputoctets,	calledstationid, 	callingstationid, \
		acctterminatecause,	servicetype,		framedprotocol, \
		framedipaddress"
	type {
		accounting-on {
			#
			#  Bulk terminate all sessions associated with a given NAS
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctstoptime = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= '%{integer:Event-Timestamp}' \
						- UNIX_TIMESTAMP(acctstarttime), \
					acctterminatecause = '%{%{Acct-Terminate-Cause}:-NAS-Reboot}' \
				WHERE acctstoptime IS NULL \
				AND nasipaddress   = '%{NAS-IP-Address}' \
				AND acctstarttime <= FROM_UNIXTIME(\
					%{integer:Event-Timestamp})"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			#
			#  Insert a new record into the sessions table
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
			#
			#  Key constraints prevented us from inserting a new session,
			#  use the alternate query to update an existing session.
			#
			query = "\
				UPDATE ${....acct_table1} SET \
					acctstarttime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					acctupdatetime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					connectinfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		interim-update {
			#
			#  Update an existing session and calculate the interval
			#  between the last data we received for the session and this
			#  update. This can be used to find stale sessions.
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctupdatetime  = (@acctupdatetime_old:=acctupdatetime), \
					acctupdatetime  = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctinterval    = %{integer:Event-Timestamp} - \
						UNIX_TIMESTAMP(@acctupdatetime_old), \
					framedipaddress = '%{Framed-IP-Address}', \
					acctsessiontime = %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets = '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
		stop {
			#
			#  Session has terminated, update the stop time and statistics.
			#
			query = "\
				UPDATE ${....acct_table2} SET \
					acctstoptime	= FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets	= '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}', \
					acctterminatecause = '%{Acct-Terminate-Cause}', \
					connectinfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table2} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query	- Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query =	"\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES ( \
			'%{SQL-User-Name}', \
			'%{%{User-Password}:-%{Chap-Password}}', \
			'%{reply:Packet-Type}', \
			'%S')"
}
================================================

File: radiusd.conf
================================================
        #  'max_servers' doesn't seem to make much difference.
        #
        #  If this is the case, then the problem is MOST LIKELY that
        #  your back-end databases are taking too long to respond, and
        #  are preventing the server from responding in a timely manner.
        #
        #  The solution is NOT do keep increasing the 'max_servers'
        #  value, but instead to fix the underlying cause of the
        #  problem: slow database, or 'hostname_lookups=yes'.
        #
        #  For more information, see 'max_request_time', above.
        #
        max_servers = 32
        #  Server-pool size regulation.  Rather than making you guess
        #  how many servers you need, FreeRADIUS dynamically adapts to
        #  the load it sees, that is, it tries to maintain enough
        #  servers to handle the current load, plus a few spare
        #  servers to handle transient load spikes.
        #
        #  It does this by periodically checking how many servers are
        #  waiting for a request.  If there are fewer than
        #  min_spare_servers, it creates a new spare.  If there are
        #  more than max_spare_servers, some of the spares die off.
        #  The default values are probably OK for most sites.
        #
        min_spare_servers = 3
        max_spare_servers = 10
        #  When the server receives a packet, it places it onto an
        #  internal queue, where the worker threads (configured above)
        #  pick it up for processing.  The maximum size of that queue
        #  is given here.
        #
        #  When the queue is full, any new packets will be silently
        #  discarded.
        #
        #  The most common cause of the queue being full is that the
        #  server is dependent on a slow database, and it has received
        #  a large "spike" of traffic.  When that happens, there is
        #  very little you can do other than make sure the server
        #  receives less traffic, or make sure that the database can
        #  handle the load.
        #
#       max_queue_size = 65536
        #  Clean up old threads periodically.  For no reason other than
        #  it might be useful.
        #
        #  '0' is a special value meaning 'infinity', or 'the servers never
        #  exit'
        max_requests_per_server = 0
        #  Automatically limit the number of accounting requests.
        #  This configuration item tracks how many requests per second
        #  the server can handle.  It does this by tracking the
        #  packets/s received by the server for processing, and
        #  comparing that to the packets/s handled by the child
        #  threads.
        #
        #  If the received PPS is larger than the processed PPS, *and*
        #  the queue is more than half full, then new accounting
        #  requests are probabilistically discarded.  This lowers the
        #  number of packets that the server needs to process.  Over
        #  time, the server will "catch up" with the traffic.
        #
        #  Throwing away accounting packets is usually safe and low
        #  impact.  The NAS will retransmit them in a few seconds, or
        #  even a few minutes.  Vendors should read RFC 5080 Section 2.2.1
        #  to see how accounting packets should be retransmitted.  Using
        #  any other method is likely to cause network meltdowns.
        #
        auto_limit_acct = no
}
######################################################################
#
#  SNMP notifications.  Uncomment the following line to enable
#  snmptraps.  Note that you MUST also configure the full path
#  to the "snmptrap" command in the "trigger.conf" file.
#
#$INCLUDE trigger.conf
# MODULE CONFIGURATION
#
#  The names and configuration of each module is located in this section.
#
#  After the modules are defined here, they may be referred to by name,
#  in other sections of this configuration file.
#
modules {
        #
        #  Each module has a configuration as follows:
        #
        #       name [ instance ] {
        #               config_item = value
        #               ...
        #       }
        #
        #  The 'name' is used to load the 'rlm_name' library
        #  which implements the functionality of the module.
        #
        #  The 'instance' is optional.  To have two different instances
        #  of a module, it first must be referred to by 'name'.
        #  The different copies of the module are then created by
        #  inventing two 'instance' names, e.g. 'instance1' and 'instance2'
        #
        #  The instance names can then be used in later configuration
        #  INSTEAD of the original 'name'.  See the 'radutmp' configuration
        #  for an example.
        #
        #
        #  As of 3.0, modules are in mods-enabled/.  Files matching
        #  the regex /[a-zA-Z0-9_.]+/ are loaded.  The modules are
        #  initialized ONLY if they are referenced in a processing
        #  section, such as authorize, authenticate, accounting,
        #  pre/post-proxy, etc.
        #
        $INCLUDE mods-enabled/
}
# Instantiation
#
#  This section orders the loading of the modules.  Modules
#  listed here will get loaded BEFORE the later sections like
#  authorize, authenticate, etc. get examined.
#
#  This section is not strictly needed.  When a section like
#  authorize refers to a module, it's automatically loaded and
#  initialized.  However, some modules may not be listed in any
#  of the following sections, so they can be listed here.
#
#  Also, listing modules here ensures that you have control over
#  the order in which they are initialized.  If one module needs
#  something defined by another module, you can list them in order
#  here, and ensure that the configuration will be OK.
#
#  After the modules listed here have been loaded, all of the modules
#  in the "mods-enabled" directory will be loaded.  Loading the
#  "mods-enabled" directory means that unlike Version 2, you usually
#  don't need to list modules here.
#
instantiate {
        #
        # We list the counter module here so that it registers
        # the check_name attribute before any module which sets
        # it
#       daily
        # subsections here can be thought of as "virtual" modules.
        #
        # e.g. If you have two redundant SQL servers, and you want to
        # use them in the authorize and accounting sections, you could
        # place a "redundant" block in each section, containing the
        # exact same text.  Or, you could uncomment the following
        # lines, and list "redundant_sql" in the authorize and
        # accounting sections.
        #
        #  The "virtual" module defined here can also be used with
        #  dynamic expansions, under a few conditions:
        #
        #  * The section is "redundant", or "load-balance", or
        #    "redundant-load-balance"
        #  * The section contains modules ONLY, and no sub-sections
        #  * all modules in the section are using the same rlm_
        #    driver, e.g. They are all sql, or all ldap, etc.
        #
        #  When those conditions are satisfied, the server will
        #  automatically register a dynamic expansion, using the
        #  name of the "virtual" module.  In the example below,
        #  it will be "redundant_sql".  You can then use this expansion
        #  just like any other:
        #
        #       update reply {
        #               Filter-Id := "%{redundant_sql: ... }"
        #       }
        #
        #  In this example, the expansion is done via module "sql1",
        #  and if that expansion fails, using module "sql2".
        #
        #  For best results, configure the "pool" subsection of the
        #  module so that "retry_delay" is non-zero.  That will allow
        #  the redundant block to quickly ignore all "down" SQL
        #  databases.  If instead we have "retry_delay = 0", then
        #  every time the redundant block is used, the server will try
        #  to open a connection to every "down" database, causing
        #  problems.
        #
        #redundant redundant_sql {
        #       sql1
        #       sql2
        #}
}
######################################################################
#
#  Policies are virtual modules, similar to those defined in the
#  "instantiate" section above.
#
#  Defining a policy in one of the policy.d files means that it can be
#  referenced in multiple places as a *name*, rather than as a series of
#  conditions to match, and actions to take.
#
#  Policies are something like subroutines in a normal language, but
#  they cannot be called recursively. They MUST be defined in order.
#  If policy A calls policy B, then B MUST be defined before A.
#
######################################################################
policy {
        $INCLUDE policy.d/
}
######################################################################
#
#       Load virtual servers.
#
#       This next $INCLUDE line loads files in the directory that
#       match the regular expression: /[a-zA-Z0-9_.]+/
#
#       It allows you to define new virtual servers simply by placing
#       a file into the raddb/sites-enabled/ directory.
#
$INCLUDE sites-enabled/
bash-5.1# cat radiusd.conf 
# -*- text -*-
##
## radiusd.conf -- FreeRADIUS server configuration file - 3.0.17
##
##      http://www.freeradius.org/
##      $Id: 59e59f3ac443e75663333a5b7732664b67c5567d $
##
######################################################################
#
#       Read "man radiusd" before editing this file.  See the section
#       titled DEBUGGING.  It outlines a method where you can quickly
#       obtain the configuration you want, without running into
#       trouble.
#
#       Run the server in debugging mode, and READ the output.
#
#               $ radiusd -X
#
#       We cannot emphasize this point strongly enough.  The vast
#       majority of problems can be solved by carefully reading the
#       debugging output, which includes warnings about common issues,
#       and suggestions for how they may be fixed.
#
#       There may be a lot of output, but look carefully for words like:
#       "warning", "error", "reject", or "failure".  The messages there
#       will usually be enough to guide you to a solution.
#
#       If you are going to ask a question on the mailing list, then
#       explain what you are trying to do, and include the output from
#       debugging mode (radiusd -X).  Failure to do so means that all
#       of the responses to your question will be people telling you
#       to "post the output of radiusd -X".
######################################################################
#
#       The location of other config files and logfiles are declared
#       in this file.
#
#       Also general configuration for modules can be done in this
#       file, it is exported through the API to modules that ask for
#       it.
#
#       See "man radiusd.conf" for documentation on the format of this
#       file.  Note that the individual configuration items are NOT
#       documented in that "man" page.  They are only documented here,
#       in the comments.
#
#       The "unlang" policy language can be used to create complex
#       if / else policies.  See "man unlang" for details.
#
prefix = /usr
exec_prefix = ${prefix}
sysconfdir = /etc
localstatedir = /var
sbindir = ${exec_prefix}/sbin
logdir = /var/log/radius
raddbdir = ${sysconfdir}/raddb
radacctdir = /var/log/radius/radacct
#
#  name of the running server.  See also the "-n" command-line option.
name = radiusd
#  Location of config and logfiles.
confdir = ${raddbdir}
modconfdir = ${confdir}/mods-config
certdir = ${confdir}/certs
cadir   = ${confdir}/certs
run_dir = ${localstatedir}/run/${name}
# Should likely be ${localstatedir}/lib/radiusd
db_dir = ${raddbdir}
#
# libdir: Where to find the rlm_* modules.
#
#   This should be automatically set at configuration time.
#
#   If the server builds and installs, but fails at execution time
#   with an 'undefined symbol' error, then you can use the libdir
#   directive to work around the problem.
#
#   The cause is usually that a library has been installed on your
#   system in a place where the dynamic linker CANNOT find it.  When
#   executing as root (or another user), your personal environment MAY
#   be set up to allow the dynamic linker to find the library.  When
#   executing as a daemon, FreeRADIUS MAY NOT have the same
#   personalized configuration.
#
#   To work around the problem, find out which library contains that symbol,
#   and add the directory containing that library to the end of 'libdir',
#   with a colon separating the directory names.  NO spaces are allowed.
#
#   e.g. libdir = /usr/local/lib:/opt/package/lib
#
#   You can also try setting the LD_LIBRARY_PATH environment variable
#   in a script which starts the server.
#
#   If that does not work, then you can re-configure and re-build the
#   server to NOT use shared libraries, via:
#
#       ./configure --disable-shared
#       make
#       make install
#
libdir = /usr/lib/freeradius
#  pidfile: Where to place the PID of the RADIUS server.
#
#  The server may be signalled while it's running by using this
#  file.
#
#  This file is written when ONLY running in daemon mode.
#
#  e.g.:  kill -HUP `cat /var/run/radiusd/radiusd.pid`
#
pidfile = ${run_dir}/${name}.pid
#
#  correct_escapes: use correct backslash escaping
#
#  Prior to version 3.0.5, the handling of backslashes was a little
#  awkward, i.e. "wrong".  In some cases, to get one backslash into
#  a regex, you had to put 4 in the config files.
#
#  Version 3.0.5 fixes that.  However, for backwards compatibility,
#  the new method of escaping is DISABLED BY DEFAULT.  This means
#  that upgrading to 3.0.5 won't break your configuration.
#
#  If you don't have double backslashes (i.e. \\) in your configuration,
#  this won't matter to you.  If you do have them, fix that to use only
#  one backslash, and then set "correct_escapes = true".
#
#  You can check for this by doing:
#
#       $ grep '\\\\' $(find raddb -type f -print)
#
correct_escapes = true
#  panic_action: Command to execute if the server dies unexpectedly.
#
#  FOR PRODUCTION SYSTEMS, ACTIONS SHOULD ALWAYS EXIT.
#  AN INTERACTIVE ACTION MEANS THE SERVER IS NOT RESPONDING TO REQUESTS.
#  AN INTERACTICE ACTION MEANS THE SERVER WILL NOT RESTART.
#
#  THE SERVER MUST NOT BE ALLOWED EXECUTE UNTRUSTED PANIC ACTION CODE
#  PATTACH CAN BE USED AS AN ATTACK VECTOR.
#
#  The panic action is a command which will be executed if the server
#  receives a fatal, non user generated signal, i.e. SIGSEGV, SIGBUS,
#  SIGABRT or SIGFPE.
#
#  This can be used to start an interactive debugging session so
#  that information regarding the current state of the server can
#  be acquired.
#
#  The following string substitutions are available:
#  - %e   The currently executing program e.g. /sbin/radiusd
#  - %p   The PID of the currently executing program e.g. 12345
#
#  Standard ${} substitutions are also allowed.
#
#  An example panic action for opening an interactive session in GDB would be:
#
#panic_action = "gdb %e %p"
#
#  Again, don't use that on a production system.
#
#  An example panic action for opening an automated session in GDB would be:
#
#panic_action = "gdb -silent -x ${raddbdir}/panic.gdb %e %p 2>&1 | tee ${logdir}/gdb-${name}-%p.log"
#
#  That command can be used on a production system.
#
#  max_request_time: The maximum time (in seconds) to handle a request.
#
#  Requests which take more time than this to process may be killed, and
#  a REJECT message is returned.
#
#  WARNING: If you notice that requests take a long time to be handled,
#  then this MAY INDICATE a bug in the server, in one of the modules
#  used to handle a request, OR in your local configuration.
#
#  This problem is most often seen when using an SQL database.  If it takes
#  more than a second or two to receive an answer from the SQL database,
#  then it probably means that you haven't indexed the database.  See your
#  SQL server documentation for more information.
#
#  Useful range of values: 5 to 120
#
max_request_time = 30
#  cleanup_delay: The time to wait (in seconds) before cleaning up
#  a reply which was sent to the NAS.
#
#  The RADIUS request is normally cached internally for a short period
#  of time, after the reply is sent to the NAS.  The reply packet may be
#  lost in the network, and the NAS will not see it.  The NAS will then
#  re-send the request, and the server will respond quickly with the
#  cached reply.
#
#  If this value is set too low, then duplicate requests from the NAS
#  MAY NOT be detected, and will instead be handled as separate requests.
#
#  If this value is set too high, then the server will cache too many
#  requests, and some new requests may get blocked.  (See 'max_requests'.)
#
#  Useful range of values: 2 to 10
#
cleanup_delay = 5
#  max_requests: The maximum number of requests which the server keeps
#  track of.  This should be 256 multiplied by the number of clients.
#  e.g. With 4 clients, this number should be 1024.
#
#  If this number is too low, then when the server becomes busy,
#  it will not respond to any new requests, until the 'cleanup_delay'
#  time has passed, and it has removed the old requests.
#
#  If this number is set too high, then the server will use a bit more
#  memory for no real benefit.
#
#  If you aren't sure what it should be set to, it's better to set it
#  too high than too low.  Setting it to 1000 per client is probably
#  the highest it should be.
#
#  Useful range of values: 256 to infinity
#
max_requests = 16384
#  hostname_lookups: Log the names of clients or just their IP addresses
#  e.g., www.freeradius.org (on) or 206.47.27.232 (off).
#
#  The default is 'off' because it would be overall better for the net
#  if people had to knowingly turn this feature on, since enabling it
#  means that each client request will result in AT LEAST one lookup
#  request to the nameserver.   Enabling hostname_lookups will also
#  mean that your server may stop randomly for 30 seconds from time
#  to time, if the DNS requests take too long.
#
#  Turning hostname lookups off also means that the server won't block
#  for 30 seconds, if it sees an IP address which has no name associated
#  with it.
#
#  allowed values: {no, yes}
#
hostname_lookups = no
#
#  Logging section.  The various "log_*" configuration items
#  will eventually be moved here.
#
log {
        #
        #  Destination for log messages.  This can be one of:
        #
        #       files - log to "file", as defined below.
        #       syslog - to syslog (see also the "syslog_facility", below.
        #       stdout - standard output
        #       stderr - standard error.
        #
        #  The command-line option "-X" over-rides this option, and forces
        #  logging to go to stdout.
        #
        #destination = files
        destination = stdout
        #
        #  Highlight important messages sent to stderr and stdout.
        #
        #  Option will be ignored (disabled) if output if TERM is not
        #  an xterm or output is not to a TTY.
        #
        colourise = yes
        #
        #  The logging messages for the server are appended to the
        #  tail of this file if destination == "files"
        #
        #  If the server is running in debugging mode, this file is
        #  NOT used.
        #
        file = ${logdir}/radius.log
        #
        #  Which syslog facility to use, if ${destination} == "syslog"
        #
        #  The exact values permitted here are OS-dependent.  You probably
        #  don't want to change this.
        #
        syslog_facility = daemon
        #  Log the full User-Name attribute, as it was found in the request.
        #
        # allowed values: {no, yes}
        #
        stripped_names = no
        #  Log authentication requests to the log file.
        #
        #  allowed values: {no, yes}
        #
        #auth = yes
        auth = $ENV{RAD_DEBUG}
        #  Log passwords with the authentication requests.
        #  auth_badpass  - logs password if it's rejected
        #  auth_goodpass - logs password if it's correct
        #
        #  allowed values: {no, yes}
        #
        #auth_badpass = yes
        auth_badpass = $ENV{RAD_DEBUG}
        #auth_goodpass = yes
        auth_goodpass = $ENV{RAD_DEBUG}
        #  Log additional text at the end of the "Login OK" messages.
        #  for these to work, the "auth" and "auth_goodpass" or "auth_badpass"
        #  configurations above have to be set to "yes".
        #
        #  The strings below are dynamically expanded, which means that
        #  you can put anything you want in them.  However, note that
        #  this expansion can be slow, and can negatively impact server
        #  performance.
        #
#       msg_goodpass = ""
#       msg_badpass = ""
        #  The message when the user exceeds the Simultaneous-Use limit.
        #
        msg_denied = "You are already logged in - access denied"
}
#  The program to execute to do concurrency checks.
checkrad = ${sbindir}/checkrad
# SECURITY CONFIGURATION
#
#  There may be multiple methods of attacking on the server.  This
#  section holds the configuration items which minimize the impact
#  of those attacks
#
security {
        #  chroot: directory where the server does "chroot".
        #
        #  The chroot is done very early in the process of starting
        #  the server.  After the chroot has been performed it
        #  switches to the "user" listed below (which MUST be
        #  specified).  If "group" is specified, it switches to that
        #  group, too.  Any other groups listed for the specified
        #  "user" in "/etc/group" are also added as part of this
        #  process.
        #
        #  The current working directory (chdir / cd) is left
        #  *outside* of the chroot until all of the modules have been
        #  initialized.  This allows the "raddb" directory to be left
        #  outside of the chroot.  Once the modules have been
        #  initialized, it does a "chdir" to ${logdir}.  This means
        #  that it should be impossible to break out of the chroot.
        #
        #  If you are worried about security issues related to this
        #  use of chdir, then simply ensure that the "raddb" directory
        #  is inside of the chroot, end be sure to do "cd raddb"
        #  BEFORE starting the server.
        #
        #  If the server is statically linked, then the only files
        #  that have to exist in the chroot are ${run_dir} and
        #  ${logdir}.  If you do the "cd raddb" as discussed above,
        #  then the "raddb" directory has to be inside of the chroot
        #  directory, too.
        #
#       chroot = /path/to/chroot/directory
        # user/group: The name (or #number) of the user/group to run radiusd as.
        #
        #   If these are commented out, the server will run as the
        #   user/group that started it.  In order to change to a
        #   different user/group, you MUST be root ( or have root
        #   privileges ) to start the server.
        #
        #   We STRONGLY recommend that you run the server with as few
        #   permissions as possible.  That is, if you're not using
        #   shadow passwords, the user and group items below should be
        #   set to radius'.
        #
        #  NOTE that some kernels refuse to setgid(group) when the
        #  value of (unsigned)group is above 60000; don't use group
        #  "nobody" on these systems!
        #
        #  On systems with shadow passwords, you might have to set
        #  'group = shadow' for the server to be able to read the
        #  shadow password file.  If you can authenticate users while
        #  in debug mode, but not in daemon mode, it may be that the
        #  debugging mode server is running as a user that can read
        #  the shadow info, and the user listed below can not.
        #
        #  The server will also try to use "initgroups" to read
        #  /etc/groups.  It will join all groups where "user" is a
        #  member.  This can allow for some finer-grained access
        #  controls.
        #
        user = radius
        group = radius
        #  Core dumps are a bad thing.  This should only be set to
        #  'yes' if you're debugging a problem with the server.
        #
        #  allowed values: {no, yes}
        #
        allow_core_dumps = no
        #
        #  max_attributes: The maximum number of attributes
        #  permitted in a RADIUS packet.  Packets which have MORE
        #  than this number of attributes in them will be dropped.
        #
        #  If this number is set too low, then no RADIUS packets
        #  will be accepted.
        #
        #  If this number is set too high, then an attacker may be
        #  able to send a small number of packets which will cause
        #  the server to use all available memory on the machine.
        #
        #  Setting this number to 0 means "allow any number of attributes"
        max_attributes = 200
        #
        #  reject_delay: When sending an Access-Reject, it can be
        #  delayed for a few seconds.  This may help slow down a DoS
        #  attack.  It also helps to slow down people trying to brute-force
        #  crack a users password.
        #
        #  Setting this number to 0 means "send rejects immediately"
        #
        #  If this number is set higher than 'cleanup_delay', then the
        #  rejects will be sent at 'cleanup_delay' time, when the request
        #  is deleted from the internal cache of requests.
        #
        #  As of Version 3.0.5, "reject_delay" has sub-second resolution.
        #  e.g. "reject_delay =  1.4" seconds is possible.
        #
        #  Useful ranges: 1 to 5
        reject_delay = 1
        #
        #  status_server: Whether or not the server will respond
        #  to Status-Server requests.
        #
        #  When sent a Status-Server message, the server responds with
        #  an Access-Accept or Accounting-Response packet.
        #
        #  This is mainly useful for administrators who want to "ping"
        #  the server, without adding test users, or creating fake
        #  accounting packets.
        #
        #  It's also useful when a NAS marks a RADIUS server "dead".
        #  The NAS can periodically "ping" the server with a Status-Server
        #  packet.  If the server responds, it must be alive, and the
        #  NAS can start using it for real requests.
        #
        #  See also raddb/sites-available/status
        #
        status_server = yes
        #
        #  allow_vulnerable_openssl: Allow the server to start with
        #  versions of OpenSSL known to have critical vulnerabilities.
        #
        #  This check is based on the version number reported by libssl
        #  and may not reflect patches applied to libssl by
        #  distribution maintainers.
        # Alpine 3.9 switched to openssl v1.1.1a-r1
        # CVE-2016-6309 was patch in openssl v1.1.0b
        allow_vulnerable_openssl = 'CVE-2016-6309'
}
# PROXY CONFIGURATION
#
#  proxy_requests: Turns proxying of RADIUS requests on or off.
#
#  The server has proxying turned on by default.  If your system is NOT
#  set up to proxy requests to another server, then you can turn proxying
#  off here.  This will save a small amount of resources on the server.
#
#  If you have proxying turned off, and your configuration files say
#  to proxy a request, then an error message will be logged.
#
#  To disable proxying, change the "yes" to "no", and comment the
#  $INCLUDE line.
#
#  allowed values: {no, yes}
#
#proxy_requests  = yes
proxy_requests  = no
#$INCLUDE proxy.conf
# CLIENTS CONFIGURATION
#
#  Client configuration is defined in "clients.conf".
#
#  The 'clients.conf' file contains all of the information from the old
#  'clients' and 'naslist' configuration files.  We recommend that you
#  do NOT use 'client's or 'naslist', although they are still
#  supported.
#
#  Anything listed in 'clients.conf' will take precedence over the
#  information from the old-style configuration files.
#
$INCLUDE clients.conf
# THREAD POOL CONFIGURATION
#
#  The thread pool is a long-lived group of threads which
#  take turns (round-robin) handling any incoming requests.
#
#  You probably want to have a few spare threads around,
#  so that high-load situations can be handled immediately.  If you
#  don't have any spare threads, then the request handling will
#  be delayed while a new thread is created, and added to the pool.
#
#  You probably don't want too many spare threads around,
#  otherwise they'll be sitting there taking up resources, and
#  not doing anything productive.
#
#  The numbers given below should be adequate for most situations.
#
thread pool {
        #  Number of servers to start initially --- should be a reasonable
        #  ballpark figure.
        start_servers = 5
        #  Limit on the total number of servers running.
        #
        #  If this limit is ever reached, clients will be LOCKED OUT, so it
        #  should NOT BE SET TOO LOW.  It is intended mainly as a brake to
        #  keep a runaway server from taking the system with it as it spirals
        #  down...
        #
        #  You may find that the server is regularly reaching the
        #  'max_servers' number of threads, and that increasing
        #  'max_servers' doesn't seem to make much difference.
        #
        #  If this is the case, then the problem is MOST LIKELY that
        #  your back-end databases are taking too long to respond, and
        #  are preventing the server from responding in a timely manner.
        #
        #  The solution is NOT do keep increasing the 'max_servers'
        #  value, but instead to fix the underlying cause of the
        #  problem: slow database, or 'hostname_lookups=yes'.
        #
        #  For more information, see 'max_request_time', above.
        #
        max_servers = 32
        #  Server-pool size regulation.  Rather than making you guess
        #  how many servers you need, FreeRADIUS dynamically adapts to
        #  the load it sees, that is, it tries to maintain enough
        #  servers to handle the current load, plus a few spare
        #  servers to handle transient load spikes.
        #
        #  It does this by periodically checking how many servers are
        #  waiting for a request.  If there are fewer than
        #  min_spare_servers, it creates a new spare.  If there are
        #  more than max_spare_servers, some of the spares die off.
        #  The default values are probably OK for most sites.
        #
        min_spare_servers = 3
        max_spare_servers = 10
        #  When the server receives a packet, it places it onto an
        #  internal queue, where the worker threads (configured above)
        #  pick it up for processing.  The maximum size of that queue
        #  is given here.
        #
        #  When the queue is full, any new packets will be silently
        #  discarded.
        #
        #  The most common cause of the queue being full is that the
        #  server is dependent on a slow database, and it has received
        #  a large "spike" of traffic.  When that happens, there is
        #  very little you can do other than make sure the server
        #  receives less traffic, or make sure that the database can
        #  handle the load.
        #
#       max_queue_size = 65536
        #  Clean up old threads periodically.  For no reason other than
        #  it might be useful.
        #
        #  '0' is a special value meaning 'infinity', or 'the servers never
        #  exit'
        max_requests_per_server = 0
        #  Automatically limit the number of accounting requests.
        #  This configuration item tracks how many requests per second
        #  the server can handle.  It does this by tracking the
        #  packets/s received by the server for processing, and
        #  comparing that to the packets/s handled by the child
        #  threads.
        #
        #  If the received PPS is larger than the processed PPS, *and*
        #  the queue is more than half full, then new accounting
        #  requests are probabilistically discarded.  This lowers the
        #  number of packets that the server needs to process.  Over
        #  time, the server will "catch up" with the traffic.
        #
        #  Throwing away accounting packets is usually safe and low
        #  impact.  The NAS will retransmit them in a few seconds, or
        #  even a few minutes.  Vendors should read RFC 5080 Section 2.2.1
        #  to see how accounting packets should be retransmitted.  Using
        #  any other method is likely to cause network meltdowns.
        #
        auto_limit_acct = no
}
######################################################################
#
#  SNMP notifications.  Uncomment the following line to enable
#  snmptraps.  Note that you MUST also configure the full path
#  to the "snmptrap" command in the "trigger.conf" file.
#
#$INCLUDE trigger.conf
# MODULE CONFIGURATION
#
#  The names and configuration of each module is located in this section.
#
#  After the modules are defined here, they may be referred to by name,
#  in other sections of this configuration file.
#
modules {
        #
        #  Each module has a configuration as follows:
        #
        #       name [ instance ] {
        #               config_item = value
        #               ...
        #       }
        #
        #  The 'name' is used to load the 'rlm_name' library
        #  which implements the functionality of the module.
        #
        #  The 'instance' is optional.  To have two different instances
        #  of a module, it first must be referred to by 'name'.
        #  The different copies of the module are then created by
        #  inventing two 'instance' names, e.g. 'instance1' and 'instance2'
        #
        #  The instance names can then be used in later configuration
        #  INSTEAD of the original 'name'.  See the 'radutmp' configuration
        #  for an example.
        #
        #
        #  As of 3.0, modules are in mods-enabled/.  Files matching
        #  the regex /[a-zA-Z0-9_.]+/ are loaded.  The modules are
        #  initialized ONLY if they are referenced in a processing
        #  section, such as authorize, authenticate, accounting,
        #  pre/post-proxy, etc.
        #
        $INCLUDE mods-enabled/
}
# Instantiation
#
#  This section orders the loading of the modules.  Modules
#  listed here will get loaded BEFORE the later sections like
#  authorize, authenticate, etc. get examined.
#
#  This section is not strictly needed.  When a section like
#  authorize refers to a module, it's automatically loaded and
#  initialized.  However, some modules may not be listed in any
#  of the following sections, so they can be listed here.
#
#  Also, listing modules here ensures that you have control over
#  the order in which they are initialized.  If one module needs
#  something defined by another module, you can list them in order
#  here, and ensure that the configuration will be OK.
#
#  After the modules listed here have been loaded, all of the modules
#  in the "mods-enabled" directory will be loaded.  Loading the
#  "mods-enabled" directory means that unlike Version 2, you usually
#  don't need to list modules here.
#
instantiate {
        #
        # We list the counter module here so that it registers
        # the check_name attribute before any module which sets
        # it
#       daily
        # subsections here can be thought of as "virtual" modules.
        #
        # e.g. If you have two redundant SQL servers, and you want to
        # use them in the authorize and accounting sections, you could
        # place a "redundant" block in each section, containing the
        # exact same text.  Or, you could uncomment the following
        # lines, and list "redundant_sql" in the authorize and
        # accounting sections.
        #
        #  The "virtual" module defined here can also be used with
        #  dynamic expansions, under a few conditions:
        #
        #  * The section is "redundant", or "load-balance", or
        #    "redundant-load-balance"
        #  * The section contains modules ONLY, and no sub-sections
        #  * all modules in the section are using the same rlm_
        #    driver, e.g. They are all sql, or all ldap, etc.
        #
        #  When those conditions are satisfied, the server will
        #  automatically register a dynamic expansion, using the
        #  name of the "virtual" module.  In the example below,
        #  it will be "redundant_sql".  You can then use this expansion
        #  just like any other:
        #
        #       update reply {
        #               Filter-Id := "%{redundant_sql: ... }"
        #       }
        #
        #  In this example, the expansion is done via module "sql1",
        #  and if that expansion fails, using module "sql2".
        #
        #  For best results, configure the "pool" subsection of the
        #  module so that "retry_delay" is non-zero.  That will allow
        #  the redundant block to quickly ignore all "down" SQL
        #  databases.  If instead we have "retry_delay = 0", then
        #  every time the redundant block is used, the server will try
        #  to open a connection to every "down" database, causing
        #  problems.
        #
        #redundant redundant_sql {
        #       sql1
        #       sql2
        #}
}
######################################################################
#
#  Policies are virtual modules, similar to those defined in the
#  "instantiate" section above.
#
#  Defining a policy in one of the policy.d files means that it can be
#  referenced in multiple places as a *name*, rather than as a series of
#  conditions to match, and actions to take.
#
#  Policies are something like subroutines in a normal language, but
#  they cannot be called recursively. They MUST be defined in order.
#  If policy A calls policy B, then B MUST be defined before A.
#
######################################################################
policy {
        $INCLUDE policy.d/
}
######################################################################
#
#       Load virtual servers.
#
#       This next $INCLUDE line loads files in the directory that
#       match the regular expression: /[a-zA-Z0-9_.]+/
#
#       It allows you to define new virtual servers simply by placing
#       a file into the raddb/sites-enabled/ directory.
#
$INCLUDE sites-enabled/
######################################################################
#
#       All of the other configuration sections like "authorize {}",
#       "authenticate {}", "accounting {}", have been moved to the
#       the file:
#
#               raddb/sites-available/default
#
#       This is the "default" virtual server that has the same
#       configuration as in version 1.0.x and 1.1.x.  The default
#       installation enables this virtual server.  You should
#       edit it to create policies for your local site.
#
#       For more documentation on virtual servers, see:
#
#               raddb/sites-available/README
#
######################################################################
================================================

File: sql.conf
================================================
#location /etc/raddb/mods-available/sql no extention
# -*- text -*-
##
## sql.conf -- SQL modules
##
##      $Id: 4a59483c35c77f573fb177919e19ba4434cc3da1 $
######################################################################
#
#  Configuration for the SQL module
#
#  The database schemas and queries are located in subdirectories:
#
#       sql/<DB>/main/schema.sql        Schema
#       sql/<DB>/main/queries.conf      Authorisation and Accounting queries
#
#  Where "DB" is mysql, mssql, oracle, or postgresql.
#
#
sql {
        # The sub-module to use to execute queries. This should match
        # the database you're attempting to connect to.
        #
        #    * rlm_sql_mysql
        #    * rlm_sql_mssql
        #    * rlm_sql_oracle
        #    * rlm_sql_postgresql
        #    * rlm_sql_sqlite
        #    * rlm_sql_null (log queries to disk)
        #
        driver = "rlm_sql_mysql"
        #
        #       Several drivers accept specific options, to set them, a
        #       config section with the the name as the driver should be added
        #       to the sql instance.
        #
        #       Driver specific options are:
        #
        #       sqlite {
        #               # Path to the sqlite database
        #               filename = "/tmp/freeradius.db"
        #
        #               # How long to wait for write locks on the database to be
        #               # released (in ms) before giving up.
        #               busy_timeout = 200
        #
        #               # If the file above does not exist and bootstrap is set
        #               # a new database file will be created, and the SQL statements
        #               # contained within the bootstrap file will be executed.
        #               bootstrap = "${modconfdir}/${..:name}/main/sqlite/schema.sql"
        #       }
        #
        #       mysql {
        #               # If any of the files below are set, TLS encryption is enabled
        #               tls {
        #                       ca_file = "/etc/ssl/certs/my_ca.crt"
        #                       ca_path = "/etc/ssl/certs/"
        #                       certificate_file = "/etc/ssl/certs/private/client.crt"
        #                       private_key_file = "/etc/ssl/certs/private/client.key"
        #                       cipher = "DHE-RSA-AES256-SHA:AES128-SHA"
        #               }
        #
        #               # If yes, (or auto and libmysqlclient reports warnings are
        #               # available), will retrieve and log additional warnings from
        #               # the server if an error has occured. Defaults to 'auto'
        #               warnings = auto
        #       }
        #
        #       postgresql {
        #
        #               # unlike MySQL, which has a tls{} connection configuration, postgresql
        #               # uses its connection parameters - see the radius_db option below in
        #               # this file
        #
        #               # Send application_name to the postgres server
        #               # Only supported in PG 9.0 and greater. Defaults to no.
        #               send_application_name = yes
        #       }
        #
        # The dialect of SQL you want to use, this should usually match
        # the driver you selected above.
        #
        # If you're using rlm_sql_null, then it should be the type of
        # database the logged queries are going to be executed against.
        dialect = "mysql"
        # Connection info:
        #
        server = $ENV{DB_HOST}
        port = $ENV{DB_PORT}
        login = $ENV{DB_USER}
        password = $ENV{DB_PASS}
        # Database table configuration for everything except Oracle
        radius_db = $ENV{DB_NAME}
        # If you are using Oracle then use this instead
#       radius_db = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=your_sid)))"
        # If you're using postgresql this can also be used instead of the connection info parameters
#       radius_db = "dbname=radius host=localhost user=radius password=raddpass"
        # Postgreql doesn't take tls{} options in its module config like mysql does - if you want to
        # use SSL connections then use this form of connection info parameter
#        radius_db = "host=localhost port=5432 dbname=radius user=radius password=raddpass sslmode=verify-full sslcert=/etc/ssl/client.crt sslkey=/etc/ssl/client.key sslrootcert=/etc/ssl/ca.crt" 
        # If you want both stop and start records logged to the
        # same SQL table, leave this as is.  If you want them in
        # different tables, put the start table in acct_table1
        # and stop table in acct_table2
        acct_table1 = "radacct"
        acct_table2 = "radacct"
        # Allow for storing data after authentication
        postauth_table = "radpostauth"
        # Tables containing 'check' items
        authcheck_table = "radcheck"
        groupcheck_table = "radgroupcheck"
        # Tables containing 'reply' items
        authreply_table = "radreply"
        groupreply_table = "radgroupreply"
        # Table to keep group info
        usergroup_table = "radusergroup"
        # If set to 'yes' (default) we read the group tables unless Fall-Through = no in the reply table.
        # If set to 'no' we do not read the group tables unless Fall-Through = yes in the reply table.
#       read_groups = yes
        # If set to 'yes' (default) we read profiles unless Fall-Through = no in the groupreply table.
        # If set to 'no' we do not read profiles unless Fall-Through = yes in the groupreply table.
#       read_profiles = yes
        # Remove stale session if checkrad does not see a double login
        delete_stale_sessions = yes
        # Write SQL queries to a logfile. This is potentially useful for tracing
        # issues with authorization queries.  See also "logfile" directives in
        # mods-config/sql/main/*/queries.conf.  You can enable per-section logging
        # by enabling "logfile" there, or global logging by enabling "logfile" here.
        #
        # Per-section logging can be disabled by setting "logfile = ''"
         logfile = ${logdir}/sqllog.sql
        #  Set the maximum query duration and connection timeout
        #  for rlm_sql_mysql.
#       query_timeout = 5
        #  As of version 3.0, the "pool" section has replaced the
        #  following configuration items:
        #
        #  num_sql_socks
        #  connect_failure_retry_delay
        #  lifetime
        #  max_queries
        #
        #  The connection pool is new for 3.0, and will be used in many
        #  modules, for all kinds of connection-related activity.
        #
        # When the server is not threaded, the connection pool
        # limits are ignored, and only one connection is used.
        #
        # If you want to have multiple SQL modules re-use the same
        # connection pool, use "pool = name" instead of a "pool"
        # section.  e.g.
        #
        #       sql1 {
        #           ...
        #           pool {
        #                ...
        #           }
        #       }
        #
        #       # sql2 will use the connection pool from sql1
        #       sql2 {
        #            ...
        #            pool = sql1
        #       }
        #
        pool {
                #  Connections to create during module instantiation.
                #  If the server cannot create specified number of
                #  connections during instantiation it will exit.
                #  Set to 0 to allow the server to start without the
                #  database being available.
                start = ${thread[pool].start_servers}
                #  Minimum number of connections to keep open
                min = ${thread[pool].min_spare_servers}
                #  Maximum number of connections
                #
                #  If these connections are all in use and a new one
                #  is requested, the request will NOT get a connection.
                #
                #  Setting 'max' to LESS than the number of threads means
                #  that some threads may starve, and you will see errors
                #  like 'No connections available and at max connection limit'
                #
                #  Setting 'max' to MORE than the number of threads means
                #  that there are more connections than necessary.
                max = ${thread[pool].max_servers}
                #  Spare connections to be left idle
                #
                #  NOTE: Idle connections WILL be closed if "idle_timeout"
                #  is set.  This should be less than or equal to "max" above.
                spare = ${thread[pool].max_spare_servers}
                #  Number of uses before the connection is closed
                #
                #  0 means "infinite"
                uses = 0
                #  The number of seconds to wait after the server tries
                #  to open a connection, and fails.  During this time,
                #  no new connections will be opened.
                retry_delay = 30
                # The lifetime (in seconds) of the connection
                lifetime = 0
                #  idle timeout (in seconds).  A connection which is
                #  unused for this length of time will be closed.
                idle_timeout = 60
                #  NOTE: All configuration settings are enforced.  If a
                #  connection is closed because of "idle_timeout",
                #  "uses", or "lifetime", then the total number of
                #  connections MAY fall below "min".  When that
                #  happens, it will open a new connection.  It will
                #  also log a WARNING message.
                #
                #  The solution is to either lower the "min" connections,
                #  or increase lifetime/idle_timeout.
        }
        # Set to 'yes' to read radius clients from the database ('nas' table)
        # Clients will ONLY be read on server startup.
        read_clients = yes
        # Table to keep radius client info
        client_table = "nas"
        #
        # The group attribute specific to this instance of rlm_sql
        #
        # This entry should be used for additional instances (sql foo {})
        # of the SQL module.
#       group_attribute = "${.:instance}-SQL-Group"
        # This entry should be used for the default instance (sql {})
        # of the SQL module.
        group_attribute = "SQL-Group"
        # Read database-specific queries
        $INCLUDE ${modconfdir}/${.:name}/main/${dialect}/queries.conf
}
================================================

File: docker-compose.yml
================================================
version: "3.2"
services:
  freeradius:
    image: "2stacks/freeradius"
    privileged: true
    container_name: my-radius
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - "./configs/radius/users:/etc/raddb/users"
    environment:
      - DB_NAME=radius
      - DB_HOST=mysql-radius
      - DB_USER=radius
      - DB_PASS=radpass
      - DB_PORT=3306
      - RADIUS_KEY=testing123
      - RAD_DEBUG=yes
      # - RAD_CLIENTS=172.28.5.0/24
      - RAD_CLIENTS=*
    ports:
      - "1812:1812/udp"
      - "1813:1813/udp"
    depends_on:
      - mysql
    restart: unless-stopped
    networks:
      my-network-2:
        ipv4_address: 172.29.1.2
  mysql:
    image: mysql:latest
    container_name: mysql-radius
    ports:
      - "3307:3306"
    volumes:
      - "./configs/mysql/master/data:/var/lib/mysql"
      - "./configs/mysql/radius.sql:/docker-entrypoint-initdb.d/radius.sql"
    environment:
      - MYSQL_ROOT_PASSWORD=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radpass
      - MYSQL_DATABASE=radius
    restart: unless-stopped
    networks:
      my-network-2:
        ipv4_address: 172.29.1.3
networks:
  my-network:
    external: true
  my-network-2:
    external: true
# docker run --name=mikrotik-3 -d -p 2222:22 -p 8728:8728 -p 8729:8729 -p 5900:5900 -ti evilfreelancer/docker-routeros
================================================

File: Dockerfile
================================================
FROM alpine:3.13.1
MAINTAINER 2stacks <2stacks@2stacks.net>
# Use docker build --pull -t 2stacks/freeradius .
# Image details
LABEL net.2stacks.name="2stacks" \
      net.2stacks.license="MIT" \
      net.2stacks.description="Dockerfile for autobuilds" \
      net.2stacks.url="http://www.2stacks.net" \
      net.2stacks.vcs-type="Git" \
      net.2stacks.version="1.5.1" \
      net.2stacks.radius.version="3.0.20-r1"
RUN apk --update add bash nano freeradius freeradius-mysql freeradius-eap openssl freeradius-utils freeradius-client 
EXPOSE 1812/udp 1813/udp
ENV DB_HOST=mysql
ENV DB_PORT=3306
ENV DB_USER=radius
ENV DB_PASS=radpass
ENV DB_NAME=radius
ENV RADIUS_KEY=testing123
#ENV RAD_CLIENTS=172.28.5.0/24
#For all IP
ENV RAD_CLIENTS=*
ENV RAD_DEBUG=yes
ADD --chown=root:radius ./etc/raddb/ /etc/raddb
RUN /etc/raddb/certs/bootstrap && \
    chown -R root:radius /etc/raddb/certs && \
    chmod 640 /etc/raddb/certs/*.pem
ADD ./scripts/start.sh /start.sh
ADD ./scripts/wait-for.sh /wait-for.sh
#copy file config
# Enable rlm_sqlcounter module
RUN ln -s /etc/raddb/mods-available/sqlcounter /etc/raddb/mods-enabled/sqlcounter
RUN chmod +x /start.sh wait-for.sh
CMD ["/start.sh"]
================================================

File: README.md
================================================
# FreeRADIUS Docker Container
This repository builds a FreeRADIUS Docker container using Alpine Linux.  It requires a MySQL database and can be configured with environment variables.
[![Build Status](https://travis-ci.org/2stacks/docker-freeradius.svg?branch=master)](https://travis-ci.org/2stacks/docker-freeradius)
[![Docker Stars](https://img.shields.io/docker/stars/2stacks/freeradius.svg?style=popout-square)](https://hub.docker.com/r/2stacks/freeradius)
[![Docker Pulls](https://img.shields.io/docker/pulls/2stacks/freeradius.svg?style=popout-square)](https://hub.docker.com/r/2stacks/freeradius)
[![Build Details](https://images.microbadger.com/badges/image/2stacks/freeradius.svg)](https://microbadger.com/images/2stacks/freeradius)
## Supported tags
| Tag | Alpine Version | FreeRADIUS Version | Release Date | Changes |
| --- | :---: | :---: | :---: | :---: |
| [1.5.1, latest](https://github.com/2stacks/docker-freeradius/blob/master/Dockerfile) | 3.11.0 | 3.0.20-r1 | 2019-12-23 | [Changelog](https://github.com/2stacks/docker-freeradius/compare/v1.5.0...master) |
| [1.5.0](https://github.com/2stacks/docker-freeradius/blob/v1.5.0/Dockerfile) | 3.10.3 | 3.0.19-r3 | 2019-11-14 | [Changelog](https://github.com/2stacks/docker-freeradius/compare/v1.4.3...v1.5.0) |
| [1.4.3](https://github.com/2stacks/docker-freeradius/blob/v1.4.3/Dockerfile) | 3.9.4 | 3.0.17-r5 | 2019-06-14 | [Changelog](https://github.com/2stacks/docker-freeradius/compare/v1.4.2...v1.4.3) |
| [1.4.2](https://github.com/2stacks/docker-freeradius/blob/v1.4.2/Dockerfile) | 3.9.3 | 3.0.17-r4 | 2019-04-12 | [Changelog](https://github.com/2stacks/docker-freeradius/compare/v1.4.1...v1.4.2) |
# Running the container
-   With MySQL
```bash
$ docker run -d -t --name freeradius -p 1812:1812/udp -p 1813:1813/udp -e DB_HOST=<mysql.server> 2stacks/freeradius
```
# Environment Variables
-   DB_HOST=localhost
-   DB_PORT=3306
-   DB_USER=radius
-   DB_PASS=radpass
-   DB_NAME=radius
-   RADIUS_KEY=testing123
-   RAD_CLIENTS=10.0.0.0/24
-   RAD_DEBUG=no
# Docker Compose Example
You can use the included docker-compose.yml file to test Freeradius and MySQL integration:
```yaml
version: '3.2'
services:
  freeradius:
    image: "2stacks/freeradius"
    ports:
      - "1812:1812/udp"
      - "1813:1813/udp"
    #volumes:
      #- "./configs/radius/users:/etc/raddb/users"
      #- "./configs/radius/clients.conf:/etc/raddb/clients.conf"
    environment:
      #- DB_NAME=radius
      - DB_HOST=mysql
      #- DB_USER=radius
      #- DB_PASS=radpass
      #- DB_PORT=3306
      #- RADIUS_KEY=testing123
      #- RAD_CLIENTS=10.0.0.0/24
      - RAD_DEBUG=yes
    depends_on:
      - mysql
    links:
      - mysql
    restart: always
    networks:
      - backend
  mysql:
    image: "mysql"
    command: --default-authentication-plugin=mysql_native_password
    ports:
      - "3306:3306"
    volumes:
      - "./configs/mysql/master/data:/var/lib/mysql"
      #- "./configs/mysql/master/conf.d:/etc/mysql/conf.d"
      - "./configs/mysql/radius.sql:/docker-entrypoint-initdb.d/radius.sql"
    environment:
      - MYSQL_ROOT_PASSWORD=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radpass
      - MYSQL_DATABASE=radius
    restart: always
    networks:
      - backend
networks:
  backend:
    ipam:
      config:
        - subnet: 10.0.0.0/24
```
This compose file can be used from within this code repository by executing;
```bash
$ docker-compose up -d
```
Note: The example above binds freeradius with a mysql database.  The mysql docker image, associated schema, volumes and configs are not a part of the 2stacks/freeradius image that can be pulled from docker hub.  See .dockerignore file for the parts of this repository that are excluded from the image.
# Testing Authentication
The freeradius container can be tested against the mysql backend created in the above compose file using a separate container running the radtest client.
```bash
$ docker run -it --rm --network docker-freeradius_backend 2stacks/radtest radtest testing password freeradius 0 testing123
Sent Access-Request Id 42 from 0.0.0.0:48898 to 10.0.0.3:1812 length 77
        User-Name = "testing"
        User-Password = "password"
        NAS-IP-Address = 10.0.0.4
        NAS-Port = 0
        Message-Authenticator = 0x00
        Cleartext-Password = "password"
Received Access-Accept Id 42 from 10.0.0.3:1812 to 0.0.0.0:0 length 20
```
Note: The username and password used in the radtest example above are pre-loaded in the mysql database by the radius.sql schema included in this repository.  The preconfigured mysql database is for validating freeradius functionality only and not intended for production use.
A default SQL schema for FreeRadius on MySQL can be found [here](https://github.com/FreeRADIUS/freeradius-server/blob/master/raddb/mods-config/sql/main/mysql/schema.sql).
# Build the container
If you would like to make modifications or customizations, clone this repository, make your changes and then run the following from the root of the repository.
```bash
$ docker build --pull -t <docker_hub_account>/freeradius .
```
Note: Some users have reported broken symlinks when building the container.  Check that you have the default servers enabled via symlinks in the repository's `./etc/raddb/sites-enabled` directory.  If there are no symlinks in this directory you can create them with;
```bash
cd docker-freeradius/etc/raddb/sites-enabled
ln -s ../sites-available/default default
ln -s ../sites-available/inner-tunnel inner-tunnel
``` 
See [this thread](https://github.com/2stacks/docker-freeradius/issues/3) for additional information.
# Certificates
The container has a set of test certificates that are generated each time the container is built using the included Dockerfile.  These certificates are configured with the default settings from the Freeradius package and are set to expire after sixty days.
These certificates are not meant to be used in production and should be recreated/replaced as needed.  Follow the steps below to generate new certificates.  It is important that you read and understand the instructions in '/etc/raddb/certs/README'
#### Generate new certs
From your docker host machine
  - Clone the git repository
```bash
$ git clone https://github.com/2stacks/docker-freeradius.git
```
  - Make changes to the .cnf files in /etc/raddb/certs as needed. (Optional)
  - Run the container
```bash
$ docker run -it --rm -v $PWD/etc/raddb:/etc/raddb 2stacks/freeradius:latest sh
```
From inside the container
```bash
/ # cd /etc/raddb/certs/
/ # rm -f *.pem *.der *.csr *.crt *.key *.p12 serial* index.txt*
/ # ./bootstrap
/ # chown -R root:radius /etc/raddb/certs
/ # chmod 640 /etc/raddb/certs/*.pem
/ # exit
```
You can bind mount these certificates back in to the container or rebuild the container as mentioned above.
You'll have to change the permissions to your local user before rebuilding the container.
```bash
$ sudo chown -R $USER:$USER etc/raddb/certs
```
================================================

File: _config.yml
================================================
remote_theme: mmistakes/minimal-mistakes
titles_from_headings:
  enabled:     true
  strip_title: true
plugins:
  - jekyll-include-cache
  - jekyll-titles-from-headings
================================================

File: README
================================================
  This directory contains scripts to create the server certificates.
To make a set of default (i.e. test) certificates, simply type:
$ ./bootstrap
  The "openssl" command will be run against the sample configuration
files included here, and will make a self-signed certificate authority
(i.e. root CA), and a server certificate.  This "root CA" should be
installed on any client machine needing to do EAP-TLS, PEAP, or
EAP-TTLS.
  The Microsoft "XP Extensions" will be automatically included in the
server certificate.  Without those extensions Windows clients will
refuse to authenticate to FreeRADIUS.
  The root CA and the "XP Extensions" file also contain a crlDistributionPoints
attribute. The latest release of Windows Phone needs this to be present
for the handset to validate the RADIUS server certificate. The RADIUS
server must have the URI defined but the CA need not have...however it
is best practice for a CA to have a revocation URI. Note that whilst
the Windows Mobile client cannot actually use the CRL when doing 802.1X
it is recommended that the URI be an actual working URL and contain a
revocation format file as there may be other OS behaviour at play and
future OSes that may do something with that URI.
  In general, you should use self-signed certificates for 802.1x (EAP)
authentication.  When you list root CAs from other organisations in
the "ca_file", you permit them to masquerade as you, to authenticate
your users, and to issue client certificates for EAP-TLS.
  If FreeRADIUS was configured to use OpenSSL, then simply starting
the server in root in debugging mode should also create test
certificates, i.e.:
$ radiusd -X
  That will cause the EAP-TLS module to run the "bootstrap" script in
this directory.  The script will be executed only once, the first time
the server has been installed on a particular machine.  This bootstrap
script SHOULD be run on installation of any pre-built binary package
for your OS.  In any case, the script will ensure that it is not run
twice, and that it does not over-write any existing certificates.
  If you already have CA and server certificates, rename (or delete)
this directory, and create a new "certs" directory containing your
certificates.  Note that the "make install" command will NOT
over-write your existing "raddb/certs" directory, which means that the
"bootstrap" command will not be run.
		NEW INSTALLATIONS OF FREERADIUS
  We suggest that new installations use the test certificates for
initial tests, and then create real certificates to use for normal
user authentication.  See the instructions below for how to create the
various certificates.  The old test certificates can be deleted by
running the following command:
$ rm -f *.pem *.der *.csr *.crt *.key *.p12 serial* index.txt*
  Then, follow the instructions below for creating real certificates.
  Once the final certificates have been created, you can delete the
"bootstrap" command from this directory, and delete the
"make_cert_command" configuration from the "tls" sub-section of
eap.conf.
  If you do not want to enable EAP-TLS, PEAP, or EAP-TTLS, then delete
the relevant sub-sections from the "eap.conf" file.
		MAKING A ROOT CERTIFICATE
$ vi ca.cnf
  Edit the "input_password" and "output_password" fields to be the
  password for the CA certificate.
  Edit the [certificate_authority] section to have the correct values
  for your country, state, etc.
$ make ca.pem
  This step creates the CA certificate.
$ make ca.der
  This step creates the DER format of the self-signed certificate,
  which is can be imported into Windows.
		MAKING A SERVER CERTIFICATE
$ vi server.cnf
  Edit the "input_password" and "output_password" fields to be the
  password for the server certificate.
  Edit the [server] section to have the correct values for your
  country, state, etc.  Be sure that the commonName field here is
  different from the commonName for the CA certificate.
$ make server.pem
  This step creates the server certificate.
  If you have an existing certificate authority, and wish to create a
  certificate signing request for the server certificate, edit
  server.cnf as above, and type the following command.
$ make server.csr
  You will have to ensure that the certificate contains the XP
  extensions needed by Microsoft clients.
		MAKING A CLIENT CERTIFICATE
  Client certificates are used by EAP-TLS, and optionally by EAP-TTLS
and PEAP.  The following steps outline how to create a client
certificate that is signed by the server certificate created above.
You will have to have the password for the server certificate in the
"input_password" and "output_password" fields of the server.cnf file.
$ vi client.cnf
  Edit the "input_password" and "output_password" fields to be the
  password for the client certificate.  You will have to give these
  passwords to the end user who will be using the certificates.
  Edit the [client] section to have the correct values for your
  country, state, etc.  Be sure that the commonName field here is
  the User-Name that will be used for logins!
$ make client.pem
  The users certificate will be in "emailAddress.pem",
  i.e. "user@example.com.pem".
  To create another client certificate, just repeat the steps for
  making a client certificate, being sure to enter a different login
  name for "commonName", and a different password.
		PERFORMANCE
  EAP performance for EAP-TLS, TTLS, and PEAP is dominated by SSL
  calculations.  That is, a normal system can handle PAP
  authentication at a rate of 10k packets/s.  However, SSL involves
  RSA calculations, which are very expensive.  To benchmark your system,
  do:
$ openssl speed rsa
  or
$ openssl speed rsa2048
  to test 2048 bit keys.
  A 1GHz system will likely do 30 calculations/s.  A 2GHz system may
  do 50 calculations/s, or more.  That number is also the number of
  authentications/s that can be done for EAP-TLS (or TTLS, or PEAP).
		COMPATIBILITY
The certificates created using this method are known to be compatible
with ALL operating systems.  Some common issues are:
  - Windows requires certain OIDs in the certificates.  If it doesn't
    see them, it will stop doing EAP.  The most visible effect is
    that the client starts EAP, gets a few Access-Challenge packets,
    and then a little while later re-starts EAP.  If this happens, see
    the FAQ, and the comments in raddb/eap.conf for how to fix it.
  - Windows requires the root certificates to be on the client PC.
    If it doesn't have them, you will see the same issue as above.
  - Windows XP post SP2 has a bug where it has problems with
    certificate chains.  i.e. if the server certificate is an
    intermediate one, and not a root one, then authentication will
    silently fail, as above.
  - Some versions of Windows CE cannot handle 4K RSA certificates.
    They will (again) silently fail, as above.
  - In none of these cases will Windows give the end user any
    reasonable error message describing what went wrong.  This leads
    people to blame the RADIUS server.  That blame is misplaced.
  - Certificate chains of more than 64K bytes are known to not work.
    This is a problem in FreeRADIUS.  However, most clients cannot
    handle 64K certificate chains.  Most Access Points will shut down
    the EAP session after about 50 round trips, while 64K certificate
    chains will take about 60 round trips.  So don't use large
    certificate chains.  They will only work after everyone upgrade
    everything in the network.
  - All other operating systems are known to work with EAP and
    FreeRADIUS.  This includes Linux, *BSD, Mac OS X, Solaris,
    Symbian, along with all known embedded systems, phones, WiFi
    devices, etc.
  - Someone needs to ask Microsoft to please stop making life hard for
    their customers.
		SECURITY CONSIDERATIONS
The default certificate configuration files uses MD5 for message
digests, to maintain compatibility with network equipment that
supports only this algorithm.
MD5 has known weaknesses and is discouraged in favour of SHA1 (see
http://www.kb.cert.org/vuls/id/836068 for details). If your network
equipment supports the SHA1 signature algorithm, we recommend that you
change the "ca.cnf", "server.cnf", and "client.cnf" files to specify
the use of SHA1 for the certificates. To do this, change the
'default_md' entry in those files from 'md5' to 'sha1'.
================================================

File: clients.conf
================================================
# -*- text -*-
##
## clients.conf -- client configuration directives
##
##	$Id: 76b300d3c55f1c5c052289b76bf28ac3a370bbb2 $
#######################################################################
#
#  Define RADIUS clients (usually a NAS, Access Point, etc.).
#
#  Defines a RADIUS client.
#
#  '127.0.0.1' is another name for 'localhost'.  It is enabled by default,
#  to allow testing of the server after an initial installation.  If you
#  are not going to be permitting RADIUS queries from localhost, we suggest
#  that you delete, or comment out, this entry.
#
#
#
#  Each client has a "short name" that is used to distinguish it from
#  other clients.
#
#  In version 1.x, the string after the word "client" was the IP
#  address of the client.  In 2.0, the IP address is configured via
#  the "ipaddr" or "ipv6addr" fields.  For compatibility, the 1.x
#  format is still accepted.
#
client localhost {
	#  Only *one* of ipaddr, ipv4addr, ipv6addr may be specified for
	#  a client.
	#
	#  ipaddr will accept IPv4 or IPv6 addresses with optional CIDR
	#  notation '/<mask>' to specify ranges.
	#
	#  ipaddr will accept domain names e.g. example.org resolving
	#  them via DNS.
	#
	#  If both A and AAAA records are found, A records will be
	#  used in preference to AAAA.
	ipaddr = 127.0.0.1
	#  Same as ipaddr but allows v4 addresses only. Requires A
	#  record for domain names.
#	ipv4addr = *	# any.  127.0.0.1 == localhost
	#  Same as ipaddr but allows v6 addresses only. Requires AAAA
	#  record for domain names.
#	ipv6addr = ::	# any.  ::1 == localhost
	#
	#  A note on DNS:  We STRONGLY recommend using IP addresses
	#  rather than host names.  Using host names means that the
	#  server will do DNS lookups when it starts, making it
	#  dependent on DNS.  i.e. If anything goes wrong with DNS,
	#  the server won't start!
	#
	#  The server also looks up the IP address from DNS once, and
	#  only once, when it starts.  If the DNS record is later
	#  updated, the server WILL NOT see that update.
	#
	#
	#  The transport protocol.
	#
	#  If unspecified, defaults to "udp", which is the traditional
	#  RADIUS transport.  It may also be "tcp", in which case the
	#  server will accept connections from this client ONLY over TCP.
	#
	proto = *
	#
	#  The shared secret use to "encrypt" and "sign" packets between
	#  the NAS and FreeRADIUS.  You MUST change this secret from the
	#  default, otherwise it's not a secret any more!
	#
	#  The secret can be any string, up to 8k characters in length.
	#
	#  Control codes can be entered vi octal encoding,
	#	e.g. "\101\102" == "AB"
	#  Quotation marks can be entered by escaping them,
	#	e.g. "foo\"bar"
	#
	#  A note on security:  The security of the RADIUS protocol
	#  depends COMPLETELY on this secret!  We recommend using a
	#  shared secret that is composed of:
	#
	#	upper case letters
	#	lower case letters
	#	numbers
	#
	#  And is at LEAST 8 characters long, preferably 16 characters in
	#  length.  The secret MUST be random, and should not be words,
	#  phrase, or anything else that is recognisable.
	#
	#  The default secret below is only for testing, and should
	#  not be used in any real environment.
	#
	secret = $ENV{RADIUS_KEY}
	#
	#  Old-style clients do not send a Message-Authenticator
	#  in an Access-Request.  RFC 5080 suggests that all clients
	#  SHOULD include it in an Access-Request.  The configuration
	#  item below allows the server to require it.  If a client
	#  is required to include a Message-Authenticator and it does
	#  not, then the packet will be silently discarded.
	#
	#  allowed values: yes, no
	require_message_authenticator = no
	#
	#  The short name is used as an alias for the fully qualified
	#  domain name, or the IP address.
	#
	#  It is accepted for compatibility with 1.x, but it is no
	#  longer necessary in >= 2.0
	#
#	shortname = localhost
	#
	# the following three fields are optional, but may be used by
	# checkrad.pl for simultaneous use checks
	#
	#
	# The nas_type tells 'checkrad.pl' which NAS-specific method to
	#  use to query the NAS for simultaneous use.
	#
	#  Permitted NAS types are:
	#
	#	cisco
	#	computone
	#	livingston
	#	juniper
	#	max40xx
	#	multitech
	#	netserver
	#	pathras
	#	patton
	#	portslave
	#	tc
	#	usrhiper
	#	other		# for all other types
	#
	nas_type	 = other	# localhost isn't usually a NAS...
	#
	#  The following two configurations are for future use.
	#  The 'naspasswd' file is currently used to store the NAS
	#  login name and password, which is used by checkrad.pl
	#  when querying the NAS for simultaneous use.
	#
#	login	   = !root
#	password	= someadminpas
	#
	#  As of 2.0, clients can also be tied to a virtual server.
	#  This is done by setting the "virtual_server" configuration
	#  item, as in the example below.
	#
#	virtual_server = home1
	#
	#  A pointer to the "home_server_pool" OR a "home_server"
	#  section that contains the CoA configuration for this
	#  client.  For an example of a coa home server or pool,
	#  see raddb/sites-available/originate-coa
#	coa_server = coa
	#
	#  Response window for proxied packets.  If non-zero,
	#  then the lower of (home, client) response_window
	#  will be used.
	#
	#  i.e. it can be used to lower the response_window
	#  packets from one client to a home server.  It cannot
	#  be used to raise the response_window.
	#
#	response_window = 10.0
	#
	#  Connection limiting for clients using "proto = tcp".
	#
	#  This section is ignored for clients sending UDP traffic
	#
	limit {
		#
		#  Limit the number of simultaneous TCP connections from a client
		#
		#  The default is 16.
		#  Setting this to 0 means "no limit"
		max_connections = 16
		#  The per-socket "max_requests" option does not exist.
		#
		#  The lifetime, in seconds, of a TCP connection.  After
		#  this lifetime, the connection will be closed.
		#
		#  Setting this to 0 means "forever".
		lifetime = 0
		#
		#  The idle timeout, in seconds, of a TCP connection.
		#  If no packets have been received over the connection for
		#  this time, the connection will be closed.
		#
		#  Setting this to 0 means "no timeout".
		#
		#  We STRONGLY RECOMMEND that you set an idle timeout.
		#
		idle_timeout = 30
	}
}
# IPv6 Client
client localhost_ipv6 {
	ipv6addr	= ::1
	secret		= $ENV{RADIUS_KEY}
}
# All IPv6 Site-local clients
#client sitelocal_ipv6 {
#	ipv6addr	= fe80::/16
#	secret		= testing123
#}
#client example.org {
#	ipaddr		= radius.example.org
#	secret		= testing123
#}
#
#  You can now specify one secret for a network of clients.
#  When a client request comes in, the BEST match is chosen.
#  i.e. The entry from the smallest possible network.
#
#client private-network-1 {
#	ipaddr		= 192.0.2.0/24
#	secret		= testing123-1
#}
#client private-network-2 {
#	ipaddr		= 198.51.100.0/24
#	secret		= testing123-2
#}
client  rad_clients {
	ipaddr          = $ENV{RAD_CLIENTS}
	secret          = $ENV{RADIUS_KEY}
	nas_type	    = other
}
#######################################################################
#
#  Per-socket client lists.  The configuration entries are exactly
#  the same as above, but they are nested inside of a section.
#
#  You can have as many per-socket client lists as you have "listen"
#  sections, or you can re-use a list among multiple "listen" sections.
#
#  Un-comment this section, and edit a "listen" section to add:
#  "clients = per_socket_clients".  That IP address/port combination
#  will then accept ONLY the clients listed in this section.
#
#clients per_socket_clients {
#	client socket_client {
#		ipaddr = 192.0.2.4
#		secret = testing123
#	}
#}
================================================

File: experimental.conf
================================================
#
#  This file contains the configuration for experimental modules.
#
#  By default, it is NOT included in the build.
#
#  $Id: 87d9744a4f0fa7b9b06b4908ddd6b7d2f1a7fd62 $
#
# Configuration for the Python module.
#
# Where radiusd is a Python module, radiusd.py, and the
# function 'authorize' is called.  Here is a dummy piece
# of code:
#
#	def authorize(params):
#		print params
#		return (5, ('Reply-Message', 'banned'))
#
# The RADIUS value-pairs are passed as a tuple of tuple
# pairs as the first argument, e.g. (('attribute1',
# 'value1'), ('attribute2', 'value2'))
#
# The function return is a tuple with the first element
# being the return value of the function.
# The 5 corresponds to RLM_MODULE_USERLOCK. I plan to
# write the return values as Python symbols to avoid
# confusion.
#
# The remaining tuple members are the string form of
# value-pairs which are passed on to pairmake().
#
python {
	mod_instantiate = radiusd_test
	func_instantiate = instantiate
	mod_authorize = radiusd_test
	func_authorize = authorize
	mod_accounting = radiusd_test
	func_accounting = accounting
	mod_pre_proxy = radiusd_test
	func_pre_proxy = pre_proxy
	mod_post_proxy = radiusd_test
	func_post_proxy = post_proxy
	mod_post_auth = radiusd_test
	func_post_auth = post_auth
	mod_recv_coa = radiusd_test
	func_recv_coa = recv_coa
	mod_send_coa = radiusd_test
	func_send_coa = send_coa
	mod_detach = radiusd_test
	func_detach = detach
}
# Configuration for the example module.  Uncommenting it will cause it
# to get loaded and initialised, but should have no real effect as long
# it is not referenced in one of the autz/auth/preacct/acct sections
example {
	#  Boolean variable.
	# allowed values: {no, yes}
	boolean = yes
	#  An integer, of any value.
	integer = 16
	#  A string.
	string = "This is an example configuration string"
	# An IP address, either in dotted quad (1.2.3.4) or hostname
	# (example.com)
	ipaddr = 127.0.0.1
	# A subsection
	mysubsection {
		anotherinteger = 1000
		# They nest
		deeply nested {
			string = "This is a different string"
		}
	}
}
#
#  To create a dbm users file, do:
#
#   cat test.users | rlm_dbm_parser -f /etc/raddb/users_db
#
#  Then add 'dbm' in 'authorize' section.
#
#  Note that even if the file has a ".db" or ".dbm" extension,
#  you may have to specify it here without that extension.  This
#  is because the DBM libraries "helpfully" add a ".db" to the
#  filename, but don't check if it's already there.
#
dbm {
	usersfile = ${confdir}/users_db
}
# Instantiate a couple instances of the idn module
idn {
}
# ...more commonly known as...
idn idna {
}
idn idna_lenient {
	UseSTD3ASCIIRules = no
}
================================================

File: README.rst
================================================
Modules in Version 3
====================
As of Version 3, all of the modules have been placed in the
"mods-available/" directory.  This practice follows that used by other
servers such as Nginx, Apache, etc.  The "modules" directory should
not be used.
Modules are enabled by creating a file in the mods-enabled/ directory.
You can also create a soft-link from one directory to another::
  $ cd raddb/mods-enabled
  $ ln -s ../mods-available/foo
This will enable module "foo".  Be sure that you have configured the
module correctly before enabling it, otherwise the server will not
start.  You can verify the server configuration by running
"radiusd -XC".
A large number of modules are enabled by default.  This allows the
server to work with the largest number of authentication protocols.
Please be careful when disabling modules.  You will likely need to
edit the "sites-enabled/" files to remove references to any disabled
modules.
Conditional Modules
-------------------
Version 3 allows modules to be conditionally loaded.  This is useful
when you want to have a virtual server which references a module, but
does not require it.  Instead of editing the virtual server file, you
can just conditionally enable the module.
Modules are conditionally enabled by adding a "-" before their name in
a virtual server.  For example, you can do::
  server {
    authorize {
      ...
      ldap
      -sql
      ...
    }
  }
This says "require the LDAP module, but use the SQL module only if it
is configured."
This feature is not very useful for production configurations.  It is,
however, very useful for the default examples that ship with the
server.
Ignoring module
---------------
If you see this message::
  Ignoring module (see raddb/mods-available/README.rst)
Then you are in the right place.  Most of the time this message can be
ignored.  The message can be fixed by finding the references to "-module"
in the virtual server, and deleting them.
Another way to fix it is to configure the module, as described above.
Simplification
--------------
Allowing conditional modules simplifies the default virtual servers
that are shipped with FreeRADIUS.  This means that if you want to
enable LDAP (for example), you no longer need to edit the files in
raddb/sites-available/ in order to enable it.
Instead, you should edit the raddb/mods-available/ldap file to point
to your local LDAP server.  Then, enable the module via the soft-link
method described above.
Once the module is enabled, it will automatically be used in the
default configuration.
================================================

File: README.rst
================================================
The mods-config Directory
=========================
This directory contains module-specific configuration files.  These
files are in a format different from the one used by the main
`radiusd.conf` files.  Earlier versions of the server had many
module-specific files in the main `raddb` directory.  The directory
contained many files, and it was not clear which files did what.
For Version 3 of FreeRADIUS, we have moved to a consistent naming
scheme.  Each module-specific configuration file is placed in this
directory, in a subdirectory named for the module.  Where necessary,
files in the subdirectory have been named for the processing section
where they are used.
For example, the `users` file is now located in
`mods-config/files/authorize`.  That filename tells us three things:
1. The file is used in the `authorize` section.
2. The file is used by the `files` module.
3. It is a "module configuration" file, which is a specific format.
================================================

File: dailycounter.conf
================================================
#
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
#
query = "\
	SELECT SUM(acctsessiontime - GREATEST((%%b - UNIX_TIMESTAMP(acctstarttime)), 0)) \
	FROM radacct \
	WHERE username = '%{${key}}' \
	AND UNIX_TIMESTAMP(acctstarttime) + acctsessiontime > '%%b'"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE username = '%{${key}}' \
#	AND acctstarttime > FROM_UNIXTIME('%%b')"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE username = '%{${key}}' \
#	AND acctstarttime BETWEEN FROM_UNIXTIME('%%b') AND FROM_UNIXTIME('%%e')"
================================================

File: expire_on_login.conf
================================================
query = "\
	SELECT IFNULL( MAX(TIME_TO_SEC(TIMEDIFF(NOW(), acctstarttime))),0) \
	FROM radacct \
	WHERE UserName='%{${key}}' \
	ORDER BY acctstarttime \
	LIMIT 1;"
================================================

File: monthlycounter.conf
================================================
#
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
#
query = "\
	SELECT SUM(acctsessiontime - GREATEST((%%b - UNIX_TIMESTAMP(acctstarttime)), 0)) \
	FROM radacct \
	WHERE username='%{${key}}' \
	AND UNIX_TIMESTAMP(acctstarttime) + acctsessiontime > '%%b'"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct\
#	WHERE username='%{${key}}' \
#	AND acctstarttime > FROM_UNIXTIME('%%b')"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE username='%{${key}}' \
#	AND acctstarttime BETWEEN FROM_UNIXTIME('%%b') \
#	AND FROM_UNIXTIME('%%e')"
================================================

File: noresetcounter.conf
================================================
query = "\
	SELECT IFNULL(SUM(AcctSessionTime),0) \
	FROM radacct \
	WHERE UserName='%{${key}}'"
================================================

File: dailycounter.conf
================================================
#
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
#
query = "\
	SELECT SUM(AcctSessionTime - GREATER((%%b - AcctStartTime::ABSTIME::INT4), 0)) \
	FROM radacct \
	WHERE UserName='%{${key}}' \
	AND AcctStartTime::ABSTIME::INT4 + AcctSessionTime > '%%b'"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(AcctSessionTime) \
#	FROM radacct \
#	WHERE UserName='%{${key}}' \
#	AND AcctStartTime::ABSTIME::INT4 > '%%b'"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(AcctSessionTime) \
#	FROM radacct \
#	WHERE UserName='%{${key}}' \
#	AND AcctStartTime::ABSTIME::INT4 BETWEEN '%%b' \
#	AND '%%e'"
================================================

File: expire_on_login.conf
================================================
query = "\
	SELECT EXTRACT(EPOCH FROM (NOW() - acctstarttime)) \
	FROM radacct \
	WHERE UserName='%{${key}}' \
	ORDER BY acctstarttime \
	LIMIT 1;"
================================================

File: monthlycounter.conf
================================================
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
query = "\
	SELECT SUM(AcctSessionTime - GREATER((%%b - AcctStartTime::ABSTIME::INT4), 0)) \
	FROM radacct \
	WHERE UserName='%{${key}}' \
	AND AcctStartTime::ABSTIME::INT4 + AcctSessionTime > '%%b'"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(AcctSessionTime) \
#	FROM radacct \
#	WHERE UserName='%{${key}}' \
#	AND AcctStartTime::ABSTIME::INT4 > '%%b'"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(AcctSessionTime) \
#	FROM radacct \
#	WHERE UserName='%{${key}}' \
#	AND AcctStartTime::ABSTIME::INT4 BETWEEN '%%b' AND '%%e'"
================================================

File: noresetcounter.conf
================================================
query = "\
	SELECT SUM(AcctSessionTime) \
	FROM radacct \
	WHERE UserName='%{${key}}'"
================================================

File: dailycounter.conf
================================================
#
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
#
query = "\
	SELECT SUM(acctsessiontime - GREATEST((%%b - strftime('%%s', acctstarttime)), 0)) \
	FROM radacct \
	WHERE username = '%{${key}}' \
	AND (strftime('%%s', acctstarttime) + acctsessiontime) > %%b"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE \username = '%{${key}}' \
#	AND acctstarttime > %%b"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(acctsessiontime) FROM radacct \
#	WHERE username = '%{${key}}' \
#	AND acctstarttime BETWEEN %%b \
#	AND %%e"
================================================

File: expire_on_login.conf
================================================
query = "\
	SELECT GREATEST(strftime('%%s', NOW()) - strftime('%%s', acctstarttime), 0) AS expires \
	FROM radacct \
	WHERE username = '%{${key}}' \
	ORDER BY acctstarttime \
	LIMIT 1;"
================================================

File: monthlycounter.conf
================================================
#
#  This query properly handles calls that span from the
#  previous reset period into the current period but
#  involves more work for the SQL server than those
#  below
#
query = "\
	SELECT SUM(acctsessiontime - GREATEST((%%b - strftime('%%s', acctstarttime)), 0)) \
	FROM radacct \
	WHERE username = '%{${key}}' AND \
	(strftime('%%s', acctstarttime) + acctsessiontime) > %%b"
#
#  This query ignores calls that started in a previous
#  reset period and continue into into this one. But it
#  is a little easier on the SQL server
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE username = '%{${key}}' \
#	AND acctstarttime > %%b"
#
#  This query is the same as above, but demonstrates an
#  additional counter parameter '%%e' which is the
#  timestamp for the end of the period
#
#query = "\
#	SELECT SUM(acctsessiontime) \
#	FROM radacct \
#	WHERE username = '%{${key}}' \
#	AND acctstarttime BETWEEN %%b \
#	AND %%e"
================================================

File: noresetcounter.conf
================================================
query = "\
	SELECT IFNULL(SUM(acctsessiontime),0) \
	FROM radacct \
	WHERE username = '%{${key}}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  cui/mysql/queries.conf -- Queries to update a MySQL CUI table.
#
#  $Id: f8f18cab562e7321756cd1f3411bbc9897ef3377 $
post-auth {
	query = "\
		INSERT IGNORE INTO ${..cui_table} \
			(clientipaddress, callingstationid, username, cui, lastaccounting) \
		VALUES \
			('%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}', '%{Calling-Station-Id}', \
			'%{User-Name}', '%{reply:Chargeable-User-Identity}', NULL) \
		ON DUPLICATE KEY UPDATE \
			lastaccounting='0000-00-00 00:00:00', \
			cui='%{reply:Chargeable-User-Identity}'"
}
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	type {
		start {
			query = "\
				UPDATE ${....cui_table} SET \
					lastaccounting = CURRENT_TIMESTAMP \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		interim-update {
			query ="\
				UPDATE ${....cui_table} SET \
					lastaccounting = CURRENT_TIMESTAMP \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		stop {
			query ="\
				DELETE FROM ${....cui_table} \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
	}
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  cui/postgresql/queries.conf -- Queries to update a PostgreSQL CUI table.
#
#  $Id: 6c2215f0abbe5cb30658ea541d525fd7a274c547 $
post-auth {
	query = "\
		INSERT INTO ${..cui_table} \
			(clientipaddress, callingstationid, username, cui) \
		VALUES \
			('%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}', '%{Calling-Station-Id}', \
			'%{User-Name}', '%{reply:Chargeable-User-Identity}')"
}
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	type {
		start {
			query = "\
				UPDATE ${....cui_table} SET \
					lastaccounting = now() \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		interim-update {
			query ="\
				UPDATE ${....cui_table} SET \
					lastaccounting = now() \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		stop {
			query ="\
				DELETE FROM ${....cui_table} \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
	}
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  cui/sqlite/queries.conf -- Queries to update a sqlite CUI table.
#
#  $Id: 41741eb70ae9c428ba5230aaf9d9b84f95c050a9 $
post-auth {
	query = "\
		INSERT OR REPLACE INTO ${..cui_table} \
			(clientipaddress, callingstationid, username, cui, lastaccounting) \
		VALUES \
			('%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}', '%{Calling-Station-Id}', \
			'%{User-Name}', '%{reply:Chargeable-User-Identity}', NULL)"
}
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	type {
		start {
			query = "\
				UPDATE ${....cui_table} SET \
					lastaccounting = CURRENT_TIMESTAMP \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		interim-update {
			query ="\
				UPDATE ${....cui_table} SET \
					lastaccounting = CURRENT_TIMESTAMP \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
		stop {
			query ="\
				DELETE FROM ${....cui_table} \
				WHERE clientipaddress = '%{%{Packet-Src-IPv6-Address}:-%{Packet-Src-IP-Address}}' \
				AND callingstationid = '%{Calling-Station-Id}' \
				AND username = '%{User-Name}' \
				AND cui = '%{Chargeable-User-Identity}'"
		}
	}
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool/mysql/queries.conf -- MySQL queries for rlm_sqlippool
#
#  $Id: bc51b1b2e2482b116f21010f93959ec3182206cf $
#
#  This series of queries allocates an IP address
#
#allocate_clear = "\
#	UPDATE ${ippool_table} \
#	SET \
#		nasipaddress = '', \
#		pool_key = 0, \
#		callingstationid = '', \
#		username = '', \
#		expiry_time = NULL \
#	WHERE pool_key = '${pool_key}'"
#
#  This series of queries allocates an IP address
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE expiry_time <= NOW() - INTERVAL 1 SECOND \
	AND nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'"
#
#  The ORDER BY clause of this query tries to allocate the same IP-address
#  which user had last session...
#
allocate_find = "\
	SELECT framedipaddress FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND (expiry_time < NOW() OR expiry_time IS NULL) \
	ORDER BY \
		(username <> '%{User-Name}'), \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	LIMIT 1 \
	FOR UPDATE"
#
#  If you prefer to allocate a random IP address every time, use this query instead.
#
#allocate_find = "\
#	SELECT framedipaddress FROM ${ippool_table} \
#	WHERE pool_name = '%{control:Pool-Name}' \
#	AND expiry_time IS NULL \
#	ORDER BY \
#		RAND() \
#	LIMIT 1 \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see if the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be
#  commented out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM ${ippool_table} \
	WHERE pool_name='%{control:Pool-Name}' \
	LIMIT 1"
#
#  This is the final IP Allocation query, which saves the allocated ip details.
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{User-Name}', expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE framedipaddress = '%I' \
	AND expiry_time IS NULL"
#
#  This series of queries frees an IP number when an accounting START record arrives.
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{${attribute_name}}'"
#
#  This series of queries frees an IP number when an accounting STOP record arrives.
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{${attribute_name}}'"
#
#  This series of queries frees an IP number when an accounting ALIVE record arrives.
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{${attribute_name}}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting ON record arrives
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting OFF record arrives
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool/oracle/queries.conf -- Oracle queries for rlm_sqlippool
#
#  $Id: 03b7f0ed281654d211a7e134c44e25679573a5fc $
allocate_begin = "commit"
start_begin = "commit"
alive_begin = "commit"
stop_begin = "commit"
on_begin = "commit"
off_begin = "commit"
#
#  This query allocates an IP address from the Pool
#  The ORDER BY clause of this query tries to allocate the same IP-address
#  to the user that they had last session...
#
allocate_find = "\
	SELECT framedipaddress \
	FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND expiry_time < current_timestamp \
	AND rownum <= 1 \
	ORDER BY \
		(username <> '%{SQL-User-Name}'), \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	FOR UPDATE"
#
#  This function is available if you want to use multiple pools
#
#allocate_find = "\
#	SELECT msqlippool('%{SQL-User-Name}','%{control:Pool-Name}') \
#	FROM dual"
#
#  If you prefer to allocate a random IP address every time, use this query instead
#
#allocate_find = "\
#	SELECT framedipaddress \
#	FROM ${ippool_table} \
#	WHERE pool_name = '%{control:Pool-Name}' \
#	AND expiry_time < current_timestamp \
#	AND rownum <= 1 \
#	ORDER BY RANDOM() \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see whether the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be commented
#  out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM (\
		SELECT id \
		FROM ${ippool_table} \
		WHERE pool_name='%{control:Pool-Name}'\
	) \
	WHERE ROWNUM = 1"
#
#  This query marks the IP address handed out by "allocate-find" as used
#  for the period of "lease_duration" after which time it may be reused.
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{SQL-User-Name}', \
		expiry_time = current_timestamp + INTERVAL '${lease_duration}' second(1) \
	WHERE framedipaddress = '%I'"
#
#  This query frees the IP address assigned to "pool_key" when a new request
#  comes in for the same "pool_key". This means that either you are losing
#  accounting Stop records or you use Calling-Station-Id instead of NAS-Port
#  as your "pool_key" and your users are able to reconnect before your NAS
#  has timed out their previous session. (Generally on wireless networks)
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = current_timestamp - INTERVAL '1' second(1) \
	WHERE pool_key = '${pool_key}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = current_timestamp + INTERVAL '${lease_duration}' second(1) \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}'"
#
#  This query frees an IP address when an accounting STOP record arrives
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = current_timestamp - INTERVAL '1' second(1) \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{SQL-User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = current_timestamp + INTERVAL '${lease_duration}' second(1) \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}' \
	AND pool_key = '${pool_key}' \
	AND framedipaddress = '%{${attribute_name}}' \
	AND username = '%{SQL-User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting ON record arrives from that NAS
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = current_timestamp - INTERVAL '1' second(1) \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting OFF record arrives from that NAS
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = current_timestamp - INTERVAL '1' second(1) \
	WHERE nasipaddress = '%{%{Nas-IP-Address}:-%{Nas-IPv6-Address}}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool/postgresql/queries.conf -- PostgreSQL queries for rlm_sqlippool
#
#  $Id: 38465e829f61efab50f565dc349ef64b29052f21 $
#
#  This query allocates an IP address from the Pool
#  The ORDER BY clause of this query tries to allocate the same IP-address
#  to the user that they had last session...
#
allocate_find = "\
	SELECT framedipaddress \
	FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND expiry_time < 'now'::timestamp(0) \
	ORDER BY \
		(username <> '%{SQL-User-Name}'), \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	LIMIT 1 \
	FOR UPDATE"
#
#  If you prefer to allocate a random IP address every time, use this query instead
#
allocate_find = "\
	SELECT framedipaddress FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' AND expiry_time < 'now'::timestamp(0) \
	ORDER BY RANDOM() \
	LIMIT 1 \
	FOR UPDATE"
#
#  If an IP could not be allocated, check to see whether the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be commented
#  out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM ${ippool_table} \
	WHERE pool_name='%{control:Pool-Name}' \
	LIMIT 1"
#
#  This query marks the IP address handed out by "allocate-find" as used
#  for the period of "lease_duration" after which time it may be reused.
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{SQL-User-Name}', \
		expiry_time = 'now'::timestamp(0) + '${lease_duration} second'::interval \
	WHERE framedipaddress = '%I'"
#
#  This query frees the IP address assigned to "pool_key" when a new request
#  comes in for the same "pool_key". This means that either you are losing
#  accounting Stop records or you use Calling-Station-Id instead of NAS-Port
#  as your "pool_key" and your users are able to reconnect before your NAS
#  has timed out their previous session. (Generally on wireless networks)
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{Nas-IP-Address}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = 'now'::timestamp(0) - '1 second'::interval \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = 'now'::timestamp(0) + '${lease_duration} second'::interval \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}'"
#
#  This query frees an IP address when an accounting
#  STOP record arrives
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = 'now'::timestamp(0) - '1 second'::interval \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{SQL-User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = 'now'::timestamp(0) + '${lease_duration} seconds'::interval \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND framedipaddress = '%{Framed-IP-Address}' \
	AND username = '%{SQL-User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting ON record arrives from that NAS
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = 'now'::timestamp(0) - '1 second'::interval \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting OFF record arrives from that NAS
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		expiry_time = 'now'::timestamp(0) - '1 second'::interval \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool/sqlite/queries.conf -- SQLite queries for rlm_sqlippool
#
#  $Id: e912bd32a7485f6a505dbb67ad6f54138845cdee $
#
#  This series of queries allocates an IP address
#
#allocate_clear = "\
#	UPDATE ${ippool_table} \
#	SET \
#		nasipaddress = '', pool_key = 0, \
#		callingstationid = '', username = '', \
#		expiry_time = NULL \
#	WHERE pool_key = '${pool_key}'"
#
#  This series of queries allocates an IP address
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{Nas-IP-Address}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE expiry_time <= datetime(strftime('%%s', 'now') - 1, 'unixepoch') \
	AND nasipaddress = '%{Nas-IP-Address}'"
#
#  The ORDER BY clause of this query tries to allocate the same IP-address
#  which user had last session...
#
allocate_find = "\
	SELECT framedipaddress \
	FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND (expiry_time < datetime('now') OR expiry_time IS NULL) \
	ORDER BY \
		(username <> '%{User-Name}'), \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	LIMIT 1 \
	FOR UPDATE"
#
#   If you prefer to allocate a random IP address every time, i
#   use this query instead
#
#allocate_find = "\
#	SELECT framedipaddress \
#	FROM ${ippool_table} \
# 	WHERE pool_name = '%{control:Pool-Name}' \
#	AND expiry_time IS NULL \
#	ORDER BY RAND() \
# 	LIMIT 1 \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see if the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be
#  commented out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM ${ippool_table} \
	WHERE pool_name='%{control:Pool-Name}' \
	LIMIT 1"
#
#  This is the final IP Allocation query, which saves the allocated ip details
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{User-Name}', \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE framedipaddress = '%I' \
	AND expiry_time IS NULL"
#
#  This series of queries frees an IP number when an accounting START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting STOP record arrives
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting
#  ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting ON record arrives
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting OFF record arrives
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool-dhcp/mysql/queries.conf -- MySQL queries for rlm_sqlippool
#
#  $Id: d4d390afc633cf220ba00f796bb5d6ac453e0c49 $
#
# This series of queries allocates an IP address
#
#allocate_clear = "\
#	UPDATE ${ippool_table} \
#	SET \
#		nasipaddress = '', \
#		pool_key = 0, \
#		callingstationid = '', \
#		username = '', \
#		expiry_time = NOW() \
#	WHERE pool_key = '${pool_key}'"
#
#  This series of queries allocates an IP address
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{Nas-IP-Address}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NOW() \
	WHERE expiry_time <= NOW() - INTERVAL 1 SECOND \
	AND nasipaddress = '%{Nas-IP-Address}'"
#
#  Search for the SAME Calling-Station-ID as last time, OR an entry
#  where there is no Calling-Station-Id.
#
#  If the lease was expired, the allocate_clear above will reset the
#  Calling-Station-Id to ''.
#
#  If the lease wasn't expired, we want to give the user the same IP
#  as last time.
#
#  Then, we order by expiry_time, so that when there is no existing
#  entry for the Calling-Station-Id, it picks the OLDEST expired IP.
#
allocate_find = "\
	SELECT framedipaddress \
	FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND (callingstationid = '%{Calling-Station-Id}' or callingstationid = '') \
	ORDER BY \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	LIMIT 1 \
	FOR UPDATE"
#
#  If you prefer to allocate a random IP address every time, use this query instead
#
#allocate_find = "\
#	SELECT framedipaddress \
#	FROM ${ippool_table} \
#	WHERE pool_name = '%{control:Pool-Name}' \
#	AND expiry_time < NOW() \
#	ORDER BY RAND() \
#	LIMIT 1 \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see if the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be
#  commented out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM ${ippool_table} \
	WHERE pool_name='%{control:Pool-Name}' \
	LIMIT 1"
#
#  This is the final IP Allocation query, which saves the allocated ip details
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{User-Name}', \
		expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE framedipaddress = '%I'"
#
#  This series of queries frees an IP number when an accounting
#  START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting
#  STOP record arrives
#
stop_clear = "UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NOW() \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting
#  ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = NOW() + INTERVAL ${lease_duration} SECOND \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting ON record arrives
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NOW() \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting OFF record arrives
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NOW() \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool-dhcp/oracle/queries.conf -- Oracle queries for dhcp-ippool
#
#  $id: 416d59802a1321c16b936bb5e63c288ca3634bcd $
#
#  "START TRANSACTION" not required with Oracle
#
allocate_begin = ""
start_begin = ""
alive_begin = ""
stop_begin = ""
on_begin = ""
off_begin = ""
#
#  This query allocates an IP address from the Pool
#  It query tries to allocate to the user
#  either the same IP-address that they had last session
#  or the IP which has been unused for the longest period of time
#
allocate_find = "\
	WITH POOLS AS (\
		SELECT * \
		FROM ${ippool_table} \
		WHERE pool_name = '%{control:Pool-Name}' \
		AND (\
			pool_key = '${pool_key}' \
			OR expiry_time = (\
				SELECT MIN(expiry_time) \
				FROM ${ippool_table} \
				WHERE pool_name = '%{control:Pool-Name}' \
				AND expiry_time < CURRENT_TIMESTAMP AND pool_key != '${pool_key}'\
			)\
		)\
	) \
	SELECT framedipaddress \
	FROM (\
		SELECT framedipaddress \
		FROM POOLS \
		WHERE pool_key = '${pool_key}' \
		OR (\
			NOT EXISTS (\
				SELECT 1 \
				FROM POOLS \
				WHERE pool_key = '${pool_key}'\
			)\
		)\
	) WHERE ROWNUM = 1 FOR UPDATE"
#
#  This function is available if you want to use multiple pools
#
#allocate_find = "\
	SELECT msqlippool('%{SQL-User-Name}','%{control:Pool-Name}') \
	FROM dual"
#
#  If you prefer to allocate a random IP address every time, use this query instead
#
#allocate_find = "\
#	SELECT framedipaddress \
#	FROM ${ippool_table}\
#	WHERE framedipaddress = (\
#		SELECT framedipaddress \
#		FROM (\
#			SELECT framedipaddress \
#			FROM ${ippool_table} \
#			WHERE pool_name = '%{control:Pool-Name}' \
#			AND expiry_time < CURRENT_TIMESTAMP \
#			ORDER BY DBMS_RANDOM.VALUE\
#		) \
#		WHERE ROWNUM = 1\
#	) \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see whether the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be commented
#  out to save running this query every time an ip is not allocated.
#
#pool_check = "\
#	SELECT id \
#	FROM (\
#		SELECT id \
#		FROM ${ippool_table} \
#		WHERE pool_name = '%{control:Pool-Name}'\
#	) WHERE ROWNUM = 1"
#
#  This query marks the IP address handed out by "allocate_find" as used
#  for the period of "lease_duration" after which time it may be reused.
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-id}', \
		username = '%{SQL-User-Name}', \
		expiry_time = CURRENT_TIMESTAMP + INTERVAL '${lease_duration}' SECOND(1) \
	WHERE framedipaddress = '%I'"
#
#  This query frees the IP address assigned to "pool_key" when a new request
#  comes in for the same "pool_key". This means that either you are losing
#  accounting Stop records or you use Calling-Station-id instead of NAS-Port
#  as your "pool_key" and your users are able to reconnect before your NAS
#  has timed out their previous session. (Generally on wireless networks)
#  (Note: If your pool_key is set to Calling-Station-id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{NAS-IP-Address}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP - INTERVAL '1' SECOND(1) \
	WHERE pool_key = '${pool_key}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP + INTERVAL '${lease_duration}' SECOND(1) \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_name = '%{control:Pool-Name}' \
	AND pool_key = '${pool_key}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This query frees an IP address when an accounting
#  STOP record arrives
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP - INTERVAL '1' SECOND(1) \
	WHERE pool_key = '${pool_key}'"
#
#  This query extends an IP address lease by "lease_duration" when an accounting
#  ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP + INTERVAL '${lease_duration}' SECOND(1) \
	WHERE pool_key = '${pool_key}' \
	AND pool_name = '%{control:Pool-Name}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting ON record arrives from that NAS
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP - INTERVAL '1' SECOND(1) \
	WHERE nasipaddress = '%{NAS-IP-Address}'"
#
#  This query frees all IP addresses allocated to a NAS when an
#  accounting OFF record arrives from that NAS
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = CURRENT_TIMESTAMP - INTERVAL '1' SECOND(1) \
	WHERE nasipaddress = '%{NAS-IP-Address}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  ippool-dhcp/sqlite/queries.conf -- SQLite queries for rlm_sqlippool
#
#  $Id: a42713506e55972346e02727cbd0a36a3f72644b $
#
#  This series of queries allocates an IP address
#
#allocate_clear = "\
#	UPDATE ${ippool_table} \
#	SET \
#		nasipaddress = '', \
#		pool_key = 0, \
#		callingstationid = '', \
#		username = '', \
#		expiry_time = NULL \
#	WHERE pool_key = '${pool_key}'"
#
#  This series of queries allocates an IP address
#  (Note: If your pool_key is set to Calling-Station-Id and not NAS-Port
#  then you may wish to delete the "AND nasipaddress = '%{Nas-IP-Address}'
#  from the WHERE clause)
#
allocate_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE expiry_time <= datetime(strftime('%%s', 'now') - 1, 'unixepoch') \
	AND nasipaddress = '%{Nas-IP-Address}'"
#
#  The ORDER BY clause of this query tries to allocate the same IP-address
#  which user had last session...
#
allocate_find = "\
	SELECT framedipaddress \
	FROM ${ippool_table} \
	WHERE pool_name = '%{control:Pool-Name}' \
	AND (\
		((expiry_time < datetime('now')) OR expiry_time IS NULL) \
		OR (callingstationid = '%{Calling-Station-Id}') \
		AND expiry_time > datetime('now')\
	) \
	ORDER BY \
		(callingstationid <> '%{Calling-Station-Id}'), \
		expiry_time \
	LIMIT 1"
#
# If you prefer to allocate a random IP address every time, use this query instead
#
#allocate_find = "\
#	SELECT framedipaddress FROM ${ippool_table} \
#	WHERE pool_name = '%{control:Pool-Name}' \
#	AND expiry_time IS NULL \
#	ORDER BY RAND() \
#	LIMIT 1 \
#	FOR UPDATE"
#
#  If an IP could not be allocated, check to see if the pool exists or not
#  This allows the module to differentiate between a full pool and no pool
#  Note: If you are not running redundant pool modules this query may be
#  commented out to save running this query every time an ip is not allocated.
#
pool_check = "\
	SELECT id \
	FROM ${ippool_table} \
	WHERE pool_name='%{control:Pool-Name}' \
	LIMIT 1"
#
#  This is the final IP Allocation query, which saves the allocated ip details
#
allocate_update = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '%{NAS-IP-Address}', \
		pool_key = '${pool_key}', \
		callingstationid = '%{Calling-Station-Id}', \
		username = '%{User-Name}', \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE framedipaddress = '%I' \
	AND expiry_time IS NULL"
#
#  The following queries are not used for DHCP IP assignment.
#
#
#  This series of queries frees an IP number when an accounting START record arrives
#
start_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE nasipaddress = '%{NAS-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting STOP record arrives
#
stop_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees an IP number when an accounting ALIVE record arrives
#
alive_update = "\
	UPDATE ${ippool_table} \
	SET \
		expiry_time = datetime(strftime('%%s', 'now') + ${lease_duration}, 'unixepoch') \
	WHERE nasipaddress = '%{Nas-IP-Address}' \
	AND pool_key = '${pool_key}' \
	AND username = '%{User-Name}' \
	AND callingstationid = '%{Calling-Station-Id}' \
	AND framedipaddress = '%{Framed-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting ON record arrives
#
on_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
#
#  This series of queries frees the IP numbers allocate to a
#  NAS when an accounting OFF record arrives
#
off_clear = "\
	UPDATE ${ippool_table} \
	SET \
		nasipaddress = '', \
		pool_key = 0, \
		callingstationid = '', \
		username = '', \
		expiry_time = NULL \
	WHERE nasipaddress = '%{Nas-IP-Address}'"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  main/mssql/queries.conf -- MSSQL configuration for default schema (schema.sql)
#
#  $Id: 56ece6e3db04d9254638253da49a7c2ef100eb5e $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'.  '%{SQL-User-Name}' should be used
# below everywhere a username substitution is needed so you you can
# be sure the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#    Use Stripped-User-Name, if it's there.
#    Else use User-Name, if it's there,
#    Else use hard-coded string "none" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-none}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
#  Authorization Queries
#######################################################################
#  These queries compare the check items for the user
#  in ${authcheck_table} and setup the reply items in
#  ${authreply_table}.  You can use any query/tables
#  you want, but the return data for each row MUST
#  be in the  following order:
#
#  0. Row ID (currently unused)
#  1. UserName/GroupName
#  2. Item Attr Name
#  3. Item Attr Value
#  4. Item Attr Operation
#######################################################################
# Query for case sensitive usernames was removed. Please contact with me,
# if you know analog of STRCMP functions for MS SQL.
authorize_check_query = "\
	SELECT id, UserName, Attribute, Value, op \
	FROM ${authcheck_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_reply_query = "\
	SELECT id, UserName, Attribute, Value, op \
	FROM ${authreply_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_group_check_query = "\
	SELECT \
		${groupcheck_table}.id,${groupcheck_table}.GroupName, \
		${groupcheck_table}.Attribute,${groupcheck_table}.Value, \
		${groupcheck_table}.op \
	FROM ${groupcheck_table},${usergroup_table} \
	WHERE ${usergroup_table}.Username = '%{SQL-User-Name}' \
	AND ${usergroup_table}.GroupName = ${groupcheck_table}.GroupName \
	ORDER BY ${groupcheck_table}.id"
authorize_group_reply_query = "\
	SELECT \
		${groupreply_table}.id, ${groupreply_table}.GroupName, \
		${groupreply_table}.Attribute,${groupreply_table}.Value, \
		${groupreply_table}.op \
	FROM ${groupreply_table},${usergroup_table} \
	WHERE ${usergroup_table}.Username = '%{SQL-User-Name}' \
	AND ${usergroup_table}.GroupName = ${groupreply_table}.GroupName \
	ORDER BY ${groupreply_table}.id"
group_membership_query = "\
	SELECT groupname \
	FROM ${usergroup_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY priority"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	type {
		accounting-on {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStopTime='%S', \
					AcctSessionTime=unix_timestamp('%S') - \
						unix_timestamp(AcctStartTime), \
					AcctTerminateCause='%{%{Acct-Terminate-Cause}:-NAS-Reboot}', \
					AcctStopDelay = %{%{Acct-Delay-Time}:-0} \
				WHERE AcctStopTime = 0 \
				AND NASIPAddress = '%{NAS-IP-Address}' \
				AND AcctStartTime <= '%S'"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			query = "\
				INSERT INTO ${....acct_table1} ( \
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPort, \
					NASPortType, \
					AcctStartTime, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					ConnectInfo_stop, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					AcctTerminateCause, \
					ServiceType, \
					FramedProtocol, \
					FramedIPAddress, \
					AcctStartDelay, \
					AcctStopDelay, \
					XAscendSessionSvrKey) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					'%S', \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'%{Acct-Delay-Time}', \
					'0', \
					'%{X-Ascend-Session-Svr-Key}')"
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStartTime = '%S', \
					AcctStartDelay = '%{%{Acct-Delay-Time}:-0}', \
					ConnectInfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime = 0"
		}
		interim-update {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					FramedIPAddress = '%{Framed-IP-Address}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime = 0"
			query = "\
				INSERT INTO ${....acct_table1} ( \
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPort, \
					NASPortType, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					ServiceType, \
					FramedProtocol, \
					FramedIPAddress, \
					AcctStartDelay, \
					XAscendSessionSvrKey) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					'%{Acct-Session-Time}', \
					'%{Acct-Authentic}', \
					'', \
					'%{Acct-Input-Octets}', \
					'%{Acct-Output-Octets}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'0', \
					'%{X-Ascend-Session-Svr-Key}')"
		}
		stop {
			query = "\
				UPDATE ${....acct_table2} \
				SET \
					AcctStopTime = '%S', \
					AcctSessionTime = '%{Acct-Session-Time}', \
					AcctInputOctets = convert(bigint, '%{%{Acct-Input-Gigawords}:-0}' * POWER(2.0, 32)) | '%{%{Acct-Input-Octets}:-0}', \
					AcctOutputOctets = convert(bigint, '%{%{Acct-Output-Gigawords}:-0}' * POWER(2.0, 32)) | '%{%{Acct-Output-Octets}:-0}', \
					AcctTerminateCause = '%{Acct-Terminate-Cause}', \
					AcctStopDelay = '%{%{Acct-Delay-Time}:-0}', \
					ConnectInfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime = 0"
			query = "\
				INSERT into ${....acct_table2} (\
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPort, \
					NASPortType, \
					AcctStopTime, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					ConnectInfo_stop, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					AcctTerminateCause, \
					ServiceType, \
					FramedProtocol,	\
					FramedIPAddress, \
					AcctStartDelay, \
					AcctStopDelay) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					'%S', \
					'%{Acct-Session-Time}', \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					NULL, \
					convert(bigint, '%{%{Acct-Input-Gigawords}:-0}' * POWER(2.0, 32)) | '%{%{Acct-Input-Octets}:-0}', \
					convert(bigint, '%{%{Acct-Output-Gigawords}:-0}' * POWER(2.0, 32)) | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'0', \
					'%{%{Acct-Delay-Time}:-0}')"
		}
	}
}
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
}
================================================

File: queries.conf
================================================
# -*- text -*-
##
## wimax.conf -- MySQL configuration for WiMAX keying
##
##	$Id: 26942305017c59d4589d0645cfc79405b98b4c6a $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'.  '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
#  Uncomment the next line, if you want the sql_user_name to mean:
#
#    Use Stripped-User-Name, if it's there.
#    Else use User-Name, if it's there,
#    Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
# Logging of WiMAX SPI -> key mappings
#######################################################################
# postauth_query		- Insert some info after authentication
#######################################################################
postauth_query = "INSERT INTO wimax \
		  (username, authdate, spi, mipkey, lifetime) \
		  VALUES ( \
		  '%{User-Name}', '%S' \
		  '%{%{reply:WiMAX-MN-hHA-MIP4-SPI}:-%{reply:WiMAX-MN-hHA-MIP6-SPI}}', \
		  '%{%{reply:WiMAX-MN-hHA-MIP4-Key}:-%{reply:WiMAX-MN-hHA-MIP6-Key}}', '%{%{reply:Session-Timeout}:-86400}' )"
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  main/mysql/queries.conf-- MySQL configuration for default schema (schema.sql)
#
#  $Id: 40508024d5fd6a319bbb85775c3fe1e8388be656 $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Connection config
#######################################################################
# The character set is not configurable. The default character set of
# the mysql client library is used. To control the character set,
# create/edit my.cnf (typically in /etc/mysql/my.cnf or /etc/my.cnf)
# and enter
# [client]
# default-character-set = utf8
#
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'. '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#	Use Stripped-User-Name, if it's there.
#	Else use User-Name, if it's there,
#	Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
# Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming packets,
# not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
#default_user_profile = "DEFAULT"
#######################################################################
# NAS Query
#######################################################################
# This query retrieves the radius clients
#
# 0. Row ID (currently unused)
# 1. Name (or IP address)
# 2. Shortname
# 3. Type
# 4. Secret
# 5. Server
#######################################################################
client_query = "\
	SELECT id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
# Authorization Queries
#######################################################################
# These queries compare the check items for the user
# in ${authcheck_table} and setup the reply items in
# ${authreply_table}. You can use any query/tables
# you want, but the return data for each row MUST
# be in the following order:
#
# 0. Row ID (currently unused)
# 1. UserName/GroupName
# 2. Item Attr Name
# 3. Item Attr Value
# 4. Item Attr Operation
#######################################################################
# Use these for case sensitive usernames.
#authorize_check_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authcheck_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#authorize_reply_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authreply_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#
#  The default queries are case insensitive. (for compatibility with
#  older versions of FreeRADIUS)
#
authorize_check_query = "\
	SELECT id, username, attribute, value, op \
	FROM ${authcheck_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_reply_query = "\
	SELECT id, username, attribute, value, op \
	FROM ${authreply_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY id"
#
#  Use these for case sensitive usernames.
#
#group_membership_query = "\
#	SELECT groupname \
#	FROM ${usergroup_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY priority"
group_membership_query = "\
	SELECT groupname \
	FROM ${usergroup_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY priority"
authorize_group_check_query = "\
	SELECT id, groupname, attribute, \
	Value, op \
	FROM ${groupcheck_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY id"
authorize_group_reply_query = "\
	SELECT id, groupname, attribute, \
	value, op \
	FROM ${groupreply_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query	- query for the number of current connections
#			- If this is not defined, no simultaneous use checking
#			- will be performed by this module instance
# simul_verify_query	- query to return details of current connections
#				for verification
#			- Leave blank or commented out to disable verification step
#			- Note that the returned field order should not be changed.
#######################################################################
simul_count_query = "\
	SELECT COUNT(*) \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
simul_verify_query = "\
	SELECT \
		radacctid, acctsessionid, username, nasipaddress, nasportid, framedipaddress, \
		callingstationid, framedprotocol \
	FROM ${acct_table1} \
	WHERE username = '%{SQL-User-Name}' \
	AND acctstoptime IS NULL"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	column_list = "\
		acctsessionid,		acctuniqueid,		username, \
		realm,			nasipaddress,		nasportid, \
		nasporttype,		acctstarttime,		acctupdatetime, \
		acctstoptime,		acctsessiontime, 	acctauthentic, \
		connectinfo_start,	connectinfo_stop, 	acctinputoctets, \
		acctoutputoctets,	calledstationid, 	callingstationid, \
		acctterminatecause,	servicetype,		framedprotocol, \
		framedipaddress"
	type {
		accounting-on {
			#
			#  Bulk terminate all sessions associated with a given NAS
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctstoptime = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= '%{integer:Event-Timestamp}' \
						- UNIX_TIMESTAMP(acctstarttime), \
					acctterminatecause = '%{%{Acct-Terminate-Cause}:-NAS-Reboot}' \
				WHERE acctstoptime IS NULL \
				AND nasipaddress   = '%{NAS-IP-Address}' \
				AND acctstarttime <= FROM_UNIXTIME(\
					%{integer:Event-Timestamp})"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			#
			#  Insert a new record into the sessions table
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
			#
			#  Key constraints prevented us from inserting a new session,
			#  use the alternate query to update an existing session.
			#
			query = "\
				UPDATE ${....acct_table1} SET \
					acctstarttime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					acctupdatetime	= FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					connectinfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		interim-update {
			#
			#  Update an existing session and calculate the interval
			#  between the last data we received for the session and this
			#  update. This can be used to find stale sessions.
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctupdatetime  = (@acctupdatetime_old:=acctupdatetime), \
					acctupdatetime  = FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctinterval    = %{integer:Event-Timestamp} - \
						UNIX_TIMESTAMP(@acctupdatetime_old), \
					framedipaddress = '%{Framed-IP-Address}', \
					acctsessiontime = %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets = '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					NULL, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
		stop {
			#
			#  Session has terminated, update the stop time and statistics.
			#
			query = "\
				UPDATE ${....acct_table2} SET \
					acctstoptime	= FROM_UNIXTIME(\
						%{integer:Event-Timestamp}), \
					acctsessiontime	= %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets	= '%{%{Acct-Input-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Input-Octets}:-0}', \
					acctoutputoctets = '%{%{Acct-Output-Gigawords}:-0}' \
						<< 32 | '%{%{Acct-Output-Octets}:-0}', \
					acctterminatecause = '%{Acct-Terminate-Cause}', \
					connectinfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table2} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					FROM_UNIXTIME(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					FROM_UNIXTIME(%{integer:Event-Timestamp}), \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					'%{%{Acct-Input-Gigawords}:-0}' << 32 | '%{%{Acct-Input-Octets}:-0}', \
					'%{%{Acct-Output-Gigawords}:-0}' << 32 | '%{%{Acct-Output-Octets}:-0}', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query	- Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query =	"\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES ( \
			'%{SQL-User-Name}', \
			'%{%{User-Password}:-%{Chap-Password}}', \
			'%{reply:Packet-Type}', \
			'%S')"
}
================================================

File: README
================================================
  The SQL schema and 'create admin user" scripts are here in order to
simplify the process of using MySQL cluster.
  The queries are NOT located here, because the database driver for
MySQL cluster is just "mysql", and not "ndb".
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  main/oracle/queries.conf -- Oracle configuration for default schema (schema.sql)
#
#  $Id: 387bcf97daa51b838b8d8bdddc9f279f538014b6 $
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'.  '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
#  Uncomment the next line, if you want the sql_user_name to mean:
#
#    Use Stripped-User-Name, if it's there.
#    Else use User-Name, if it's there,
#    Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
#  Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming packets,
# not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
#default_user_profile = "DEFAULT"
#
# Determines if we will query the default_user_profile or the User-Profile
# if the user is not found. If the profile is found then we consider the user
# found. By default this is set to 'no'.
#
#query_on_not_found = no
#######################################################################
#  NAS Query
#######################################################################
#  This query retrieves the radius clients
#
#  0. Row ID (currently unused)
#  1. Name (or IP address)
#  2. Shortname
#  3. Type
#  4. Secret
#  5. Virtual server
#######################################################################
client_query = "\
	SELECT id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
#  Authorization Queries
#######################################################################
#  These queries compare the check items for the user
#  in ${authcheck_table} and setup the reply items in
#  ${authreply_table}.  You can use any query/tables
#  you want, but the return data for each row MUST
#  be in the  following order:
#
#  0. Row ID (currently unused)
#  1. UserName/GroupName
#  2. Item Attr Name
#  3. Item Attr Value
#  4. Item Attr Operation
#######################################################################
#
# WARNING: Oracle is case sensitive
#
# The main difference between MySQL and Oracle queries is the date format.
# You must use the TO_DATE function to transform the radius date format to
# the Oracle date format, and put NULL otherwise '0' in a void date field.
#
#######################################################################
authorize_check_query = "\
	SELECT id, UserName, Attribute, Value, op \
	FROM ${authcheck_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_reply_query = "\
	SELECT id, UserName, Attribute, Value, op \
	FROM ${authreply_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_group_check_query = "\
	SELECT \
		${groupcheck_table}.id, ${groupcheck_table}.GroupName, ${groupcheck_table}.Attribute, \
		${groupcheck_table}.Value,${groupcheck_table}.op \
	FROM ${groupcheck_table}, ${usergroup_table} \
	WHERE ${usergroup_table}.Username = '%{SQL-User-Name}' \
	AND ${usergroup_table}.GroupName = ${groupcheck_table}.GroupName \
	ORDER BY ${groupcheck_table}.id"
authorize_group_reply_query = "\
	SELECT \
		${groupreply_table}.id, ${groupreply_table}.GroupName, ${groupreply_table}.Attribute, \
		${groupreply_table}.Value, ${groupreply_table}.op \
	FROM ${groupreply_table}, ${usergroup_table} \
	WHERE ${usergroup_table}.Username = '%{SQL-User-Name}' \
	AND ${usergroup_table}.GroupName = ${groupreply_table}.GroupName \
	ORDER BY ${groupreply_table}.id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query	- query for the number of current connections
#			- If this is not defined, no simultaneous use checking
#			- will be performed by this module instance
# simul_verify_query	- query to return details of current connections for verification
#			- Leave blank or commented out to disable verification step
#			- Note that the returned field order should not be changed.
#######################################################################
simul_count_query = "\
	SELECT COUNT(*) \
	FROM ${acct_table1} \
	WHERE UserName = '%{SQL-User-Name}' \
	AND AcctStopTime IS NULL"
simul_verify_query = "\
	SELECT \
		RadAcctId, AcctSessionId, UserName, NASIPAddress, NASPortId, \
		FramedIPAddress, CallingStationId, FramedProtocol \
	FROM ${acct_table1} \
	WHERE UserName='%{SQL-User-Name}' \
	AND AcctStopTime IS NULL"
#######################################################################
# Group Membership Queries
#######################################################################
# group_membership_query	- Check user group membership
#######################################################################
group_membership_query = "\
	SELECT GroupName \
	FROM ${usergroup_table} \
	WHERE UserName='%{SQL-User-Name}'"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#		logfile = ${logdir}/accounting.sql
	type {
		accounting-on {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStopTime = TO_DATE('%S','yyyy-mm-dd hh24:mi:ss'), \
					AcctSessionTime = round((TO_DATE('%S','yyyy-mm-dd hh24:mi:ss') - \
						TO_DATE(TO_CHAR(acctstarttime, 'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'))*86400), \
					AcctTerminateCause='%{%{Acct-Terminate-Cause}:-NAS-Reboot}', \
					AcctStopDelay = %{%{Acct-Delay-Time}:-0} \
				WHERE AcctStopTime IS NULL \
				AND NASIPAddress = '%{NAS-IP-Address}' \
				AND AcctStartTime <= TO_DATE('%S','yyyy-mm-dd hh24:mi:ss')"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			query = "\
				INSERT INTO ${....acct_table1} (\
					RadAcctId, \
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPortId, \
					NASPortType, \
					AcctStartTime, \
					AcctStopTime, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					ConnectInfo_stop, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					AcctTerminateCause, \
					ServiceType, \
					FramedProtocol, \
					FramedIPAddress, \
					AcctStartDelay,	\
					AcctStopDelay, \
					XAscendSessionSvrKey) \
				VALUES(\
					'', \
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					TO_DATE('%S','yyyy-mm-dd hh24:mi:ss'), \
					NULL, \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'%{Acct-Delay-Time}', \
					'0', \
					'%{X-Ascend-Session-Svr-Key}')"
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStartTime = TO_DATE('%S','yyyy-mm-dd hh24:mi:ss'), \
					AcctStartDelay = '%{%{Acct-Delay-Time}:-0}', \
					ConnectInfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime IS NULL"
		}
		interim-update {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					FramedIPAddress = NULLIF('%{Framed-IP-Address}', ''), \
					AcctSessionTime = '%{Acct-Session-Time}', \
					AcctInputOctets = '%{Acct-Input-Octets}' + \
						('%{%{Acct-Input-Gigawords}:-0}' * 4294967296), \
					AcctOutputOctets = '%{Acct-Output-Octets}' +  \
						('%{%{Acct-Output-Gigawords}:-0}' * 4294967296) \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime IS NULL"
			query = "\
				INSERT into ${....acct_table1} (\
					RadAcctId, \
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPortId, \
					NASPortType, \
					AcctStartTime, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					ServiceType, \
					FramedProtocol, \
					FramedIPAddress, \
					AcctStartDelay,	\
					XAscendSessionSvrKey) \
				VALUES(\
					'', \
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					NULL, \
					'%{Acct-Session-Time}', \
					'%{Acct-Authentic}', \
					'', \
					'%{Acct-Input-Octets}' + \
						('%{%{Acct-Input-Gigawords}:-0}' * 4294967296), \
					'%{Acct-Output-Octets}' +  \
						('%{%{Acct-Output-Gigawords}:-0}' * 4294967296), \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'0', \
					'%{X-Ascend-Session-Svr-Key}')"
		}
		stop {
			query = "\
				UPDATE ${....acct_table2} \
				SET \
					AcctStopTime = TO_DATE('%S','yyyy-mm-dd hh24:mi:ss'), \
					AcctSessionTime = '%{Acct-Session-Time}', \
					AcctInputOctets = '%{Acct-Input-Octets}' + \
						('%{%{Acct-Input-Gigawords}:-0}' * 4294967296), \
					AcctOutputOctets = '%{Acct-Output-Octets}' +  \
						('%{%{Acct-Output-Gigawords}:-0}' * 4294967296), \
					AcctTerminateCause = '%{Acct-Terminate-Cause}', \
					AcctStopDelay = '%{%{Acct-Delay-Time}:-0}', \
					ConnectInfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-ID}' \
				AND AcctStopTime IS NULL"
			query = "\
				INSERT into ${....acct_table2} (\
					RadAcctId, \
					AcctSessionId, \
					AcctUniqueId, \
					UserName, \
					Realm, \
					NASIPAddress, \
					NASPortId, \
					NASPortType, \
					AcctStartTime, \
					AcctStopTime, \
					AcctSessionTime, \
					AcctAuthentic, \
					ConnectInfo_start, \
					ConnectInfo_stop, \
					AcctInputOctets, \
					AcctOutputOctets, \
					CalledStationId, \
					CallingStationId, \
					AcctTerminateCause, \
					ServiceType, \
					FramedProtocol, \
					FramedIPAddress, \
					AcctStartDelay,	\
					AcctStopDelay) \
				VALUES(\
					'', \
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					NULL, \
					TO_DATE('%S','yyyy-mm-dd hh24:mi:ss'), \
					'%{Acct-Session-Time}', \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					NULL, \
					'%{Acct-Input-Octets}' + \
						('%{%{Acct-Input-Gigawords}:-0}' * 4294967296), \
					'%{Acct-Output-Octets}' + \
						('%{%{Acct-Output-Gigawords}:-0}' * 4294967296), \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}', \
					'0', \
					'%{%{Acct-Delay-Time}:-0}')"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query                - Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query = "\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES (\
			'%{User-Name}', \
			'%{%{User-Password}:-%{Chap-Password}}', \
			'%{reply:Packet-Type}', \
			TO_TIMESTAMP('%S','YYYY-MM-DDHH24:MI:SS'))"
}
================================================

File: voip-postpaid.conf
================================================
# -*- text -*-
##
## voip-postpaid.conf -- PostgreSQL configuration for H323 VoIP billingx
##			 (cisco_h323_db_schema.sql)
##
##	$Id: 9f1449cc37d80e37025bdfd08fbd4d028aa0c800 $
	#######################################################################
	#  Query config:  Username
	#######################################################################
	# This is the username that will get substituted, escaped, and added
	# as attribute 'SQL-User-Name'.  '%{SQL-User-Name}' should be used below
	# everywhere a username substitution is needed so you you can be sure
	# the username passed from the client is escaped properly.
	#
	#  Uncomment the next line, if you want the sql_user_name to mean:
	#
	#    Use Stripped-User-Name, if it's there.
	#    Else use User-Name, if it's there,
	#    Else use hard-coded string "none" as the user name.
	#
	#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-none}}"
	#
	sql_user_name = "%{User-Name}"
	accounting {
		reference = "%{tolower:type.%{Acct-Status-Type}.query}"
		# Write SQL queries to a logfile. This is potentially useful for bulk inserts
		# when used with the rlm_sql_null driver.
#		logfile = ${logdir}/accounting.sql
		type {
			start {
				query = "INSERT INTO ${....acct_table1}%{h323-call-type} \
						(RadiusServerName, UserName, NASIPAddress, AcctTime, CalledStationId, \
						 CallingStationId, AcctDelayTime, h323gwid, h323callorigin, \
						 h323setuptime, H323ConnectTime, callid) \
					VALUES(\
						'${radius_server_name}', '%{SQL-User-Name}', \
						'%{NAS-IP-Address}', now(), '%{Called-Station-Id}', \
						'%{Calling-Station-Id}', '%{%{Acct-Delay-Time}:-0}', '%{h323-gw-id}', \
						'%{h323-call-origin}', strip_dot('%{h323-setup-time}'), \
						strip_dot('%{h323-connect-time}'), pick_id('%{h323-conf-id}', \
						'%{call-id}'))"
			}
			stop {
				query = "INSERT INTO $....acct_table2}%{h323-call-type} \
						(RadiusServerName, UserName, NASIPAddress, AcctTime, \
						 AcctSessionTime, AcctInputOctets, AcctOutputOctets, CalledStationId, \
						 CallingStationId, AcctDelayTime, H323RemoteAddress, H323VoiceQuality, \
						 CiscoNASPort, h323callorigin, callid, h323connecttime, \
						 h323disconnectcause, h323disconnecttime, h323gwid, h323setuptime) \
					VALUES(\
						'${radius_server_name}', '%{SQL-User-Name}', '%{NAS-IP-Address}', \
						NOW(),  '%{%{Acct-Session-Time}:-0}', \
						'%{%{Acct-Input-Octets}:-0}', '%{%{Acct-Output-Octets}:-0}', \
						'%{Called-Station-Id}', '%{Calling-Station-Id}', \
						'%{%{Acct-Delay-Time}:-0}', NULLIF('%{h323-remote-address}', '')::inet, \
						NULLIF('%{h323-voice-quality}','')::integer, \
						NULLIF('%{Cisco-NAS-Port}', ''), \
						'%{h323-call-origin}', pick_id('%{h323-conf-id}', '%{call-id}'), \
						strip_dot('%{h323-connect-time}'), '%{h323-disconnect-cause}', \
						strip_dot('%{h323-disconnect-time}'), '%{h323-gw-id}', \
						strip_dot('%{h323-setup-time}'))"
			}
		}
	}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  main/postgresql/queries.conf -- PostgreSQL configuration for default schema (schema.sql)
#
#  $Id: 962f4f00b66f676cf6afed5ae15cb4dffe3b515d $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
# safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'.  '%{SQL-User-Name}' should be used
# below everywhere a username substitution is needed so you you can
# be sure the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#    Use Stripped-User-Name, if it's there.
#    Else use User-Name, if it's there,
#    Else use hard-coded string "none" as the user name.
#
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-none}}"
sql_user_name = "%{User-Name}"
#######################################################################
#  Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming
# packets, not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
# default_user_profile = "DEFAULT"
#######################################################################
#  Open Query
#######################################################################
# This query is run whenever a new connection is opened.
# It is commented out by default.
#
# If you have issues with connections hanging for too long, uncomment
# the next line, and set the timeout in milliseconds.  As a general
# rule, if the queries take longer than a second, something is wrong
# with the database.
#open_query = "set statement_timeout to 1000"
#######################################################################
#  NAS Query
#######################################################################
#  This query retrieves the radius clients
#
#  0. Row ID (currently unused)
#  1. Name (or IP address)
#  2. Shortname
#  3. Type
#  4. Secret
#  5. Server
#######################################################################
client_query = "\
	SELECT id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
#  Authorization Queries
#######################################################################
#  These queries compare the check items for the user
#  in ${authcheck_table} and setup the reply items in
#  ${authreply_table}.  You can use any query/tables
#  you want, but the return data for each row MUST
#  be in the  following order:
#
#  0. Row ID (currently unused)
#  1. UserName/GroupName
#  2. Item Attr Name
#  3. Item Attr Value
#  4. Item Attr Operation
#######################################################################
#
#  Use these for case insensitive usernames. WARNING: Slower queries!
#
#authorize_check_query = "\
#	SELECT id, UserName, Attribute, Value, Op \
#	FROM ${authcheck_table} \
#	WHERE LOWER(UserName) = LOWER('%{SQL-User-Name}') \
#	ORDER BY id"
#authorize_reply_query = "\
#	SELECT id, UserName, Attribute, Value, Op \
#	FROM ${authreply_table} \
#	WHERE LOWER(UserName) = LOWER('%{SQL-User-Name}') \
#	ORDER BY id"
authorize_check_query = "\
	SELECT id, UserName, Attribute, Value, Op \
	FROM ${authcheck_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_reply_query = "\
	SELECT id, UserName, Attribute, Value, Op \
	FROM ${authreply_table} \
	WHERE Username = '%{SQL-User-Name}' \
	ORDER BY id"
#
#  Use these for case insensitive usernames. WARNING: Slower queries!
#
#authorize_group_check_query = "\
#	SELECT \
#		${groupcheck_table}.id, ${groupcheck_table}.GroupName, ${groupcheck_table}.Attribute, \
#		${groupcheck_table}.Value, ${groupcheck_table}.Op \
#	FROM ${groupcheck_table}, ${usergroup_table} \
#	WHERE LOWER(${usergroup_table}.UserName) = LOWER('%{SQL-User-Name}') \
#	AND ${usergroup_table}.GroupName = ${groupcheck_table}.GroupName \
#	ORDER BY ${groupcheck_table}.id"
#authorize_group_reply_query = "\
#	SELECT \
#		${groupreply_table}.id, ${groupreply_table}.GroupName, \
#		${groupreply_table}.Attribute, ${groupreply_table}.Value, ${groupreply_table}.Op \
#	FROM ${groupreply_table}, ${usergroup_table} \
#	WHERE LOWER(${usergroup_table}.UserName) = LOWER('%{SQL-User-Name}') \
#	AND ${usergroup_table}.GroupName = ${groupreply_table}.GroupName \
#	ORDER BY ${groupreply_table}.id"
authorize_group_check_query = "\
	SELECT id, GroupName, Attribute, Value, op \
	FROM ${groupcheck_table} \
	WHERE GroupName = '%{${group_attribute}}' \
	ORDER BY id"
authorize_group_reply_query = "\
	SELECT id, GroupName, Attribute, Value, op \
	FROM ${groupreply_table} \
	WHERE GroupName = '%{${group_attribute}}' \
	ORDER BY id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query     - query for the number of current connections
#                       - If this is not defined, no simultaneous use checking
#                       - will be performed by this module instance
# simul_verify_query    - query to return details of current connections for verification
#                       - Leave blank or commented out to disable verification step
#                       - Note that the returned field order should not be changed.
#######################################################################
#
#  Uncomment simul_count_query to enable simultaneous use checking
#
#simul_count_query = "\
#	SELECT COUNT(*) \
#	FROM ${acct_table1} \
#	WHERE UserName='%{SQL-User-Name}' \
#	AND AcctStopTime IS NULL"
#simul_verify_query = "\
#	SELECT RadAcctId, AcctSessionId, UserName, NASIPAddress, NASPortId, FramedIPAddress, CallingStationId, \
#		FramedProtocol \
#	FROM ${acct_table1} \
#	WHERE UserName='%{SQL-User-Name}' \
#	AND AcctStopTime IS NULL"
#######################################################################
# Group Membership Queries
#######################################################################
# group_membership_query        - Check user group membership
#######################################################################
# Use these for case insensitive usernames. WARNING: Slower queries!
#group_membership_query = "\
#	SELECT GroupName \
#	FROM ${usergroup_table} \
#	WHERE LOWER(UserName) = LOWER('%{SQL-User-Name}') \
#	ORDER BY priority"
group_membership_query = "\
	SELECT GroupName \
	FROM ${usergroup_table} \
	WHERE UserName='%{SQL-User-Name}' \
	ORDER BY priority"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{%{Acct-Status-Type}:-none}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	column_list = "\
		AcctSessionId, \
		AcctUniqueId, \
		UserName, \
		Realm, \
		NASIPAddress, \
		NASPortId, \
		NASPortType, \
		AcctStartTime, \
		AcctUpdateTime, \
		AcctStopTime, \
		AcctSessionTime, \
		AcctAuthentic, \
		ConnectInfo_start, \
		ConnectInfo_Stop, \
		AcctInputOctets, \
		AcctOutputOctets, \
		CalledStationId, \
		CallingStationId, \
		AcctTerminateCause, \
		ServiceType, \
		FramedProtocol, \
		FramedIpAddress"
	type {
		accounting-on {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStopTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctSessionTime = (%{integer:Event-Timestamp} - EXTRACT(EPOCH FROM(AcctStartTime))), \
					AcctTerminateCause = '%{%{Acct-Terminate-Cause}:-NAS-Reboot}' \
				WHERE AcctStopTime IS NULL \
				AND NASIPAddress= '%{%{NAS-IPv6-Address}:-%{NAS-IP-Address}}' \
				AND AcctStartTime <= '%S'::timestamp"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					NULLIF('%{Realm}', ''), \
					'%{%{NAS-IPv6-Address}:-%{NAS-IP-Address}}', \
					NULLIF('%{%{NAS-Port-ID}:-%{NAS-Port}}', ''), \
					'%{NAS-Port-Type}', \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					NULL, \
					0, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					NULL, \
					0, \
					0, \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					NULL, \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					NULLIF('%{Framed-IP-Address}', '')::inet)"
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStartTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					ConnectInfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}' \
				AND AcctStopTime IS NULL"
			# and again where we don't have "AND AcctStopTime IS NULL"
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					AcctStartTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					ConnectInfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		interim-update {
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					FramedIPAddress = NULLIF('%{Framed-IP-Address}', '')::inet, \
					AcctSessionTime = %{%{Acct-Session-Time}:-NULL}, \
					AcctInterval = (%{integer:Event-Timestamp} - EXTRACT(EPOCH FROM (COALESCE(AcctUpdateTime, AcctStartTime)))), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctInputOctets = (('%{%{Acct-Input-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Input-Octets}:-0}'::bigint), \
					AcctOutputOctets = (('%{%{Acct-Output-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Output-Octets}:-0}'::bigint) \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}' \
				AND AcctStopTime IS NULL"
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					NULLIF('%{Realm}', ''), \
					'%{%{NAS-IPv6-Address}:-%{NAS-IP-Address}}', \
					NULLIF('%{%{NAS-Port-ID}:-%{NAS-Port}}', ''), \
					'%{NAS-Port-Type}', \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					NULL, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					NULL, \
					(('%{%{Acct-Input-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Input-Octets}:-0}'::bigint), \
					(('%{%{Acct-Output-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Output-Octets}:-0}'::bigint), \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					NULL, \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					NULLIF('%{Framed-IP-Address}', '')::inet)"
		}
		stop {
			query = "\
				UPDATE ${....acct_table2} \
				SET \
					AcctStopTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctSessionTime = COALESCE(%{%{Acct-Session-Time}:-NULL}, \
						(%{integer:Event-Timestamp} - EXTRACT(EPOCH FROM(AcctStartTime)))), \
					AcctInputOctets = (('%{%{Acct-Input-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Input-Octets}:-0}'::bigint), \
					AcctOutputOctets = (('%{%{Acct-Output-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Output-Octets}:-0}'::bigint), \
					AcctTerminateCause = '%{Acct-Terminate-Cause}', \
					FramedIPAddress = NULLIF('%{Framed-IP-Address}', '')::inet, \
					ConnectInfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}' \
				AND AcctStopTime IS NULL"
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES(\
					'%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					NULLIF('%{Realm}', ''), \
					'%{%{NAS-IPv6-Address}:-%{NAS-IP-Address}}', \
					NULLIF('%{%{NAS-Port-ID}:-%{NAS-Port}}', ''), \
					'%{NAS-Port-Type}', \
					TO_TIMESTAMP(%{integer:Event-Timestamp} - %{%{Acct-Session-Time}:-0}), \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					NULLIF('%{Acct-Session-Time}', '')::bigint, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					NULL, \
					(('%{%{Acct-Input-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Input-Octets}:-0}'::bigint), \
					(('%{%{Acct-Output-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Output-Octets}:-0}'::bigint), \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					NULLIF('%{Framed-IP-Address}', '')::inet)"
			# and again where we don't have "AND AcctStopTime IS NULL"
			query = "\
				UPDATE ${....acct_table2} \
				SET \
					AcctStopTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctUpdateTime = TO_TIMESTAMP(%{integer:Event-Timestamp}), \
					AcctSessionTime = COALESCE(%{%{Acct-Session-Time}:-NULL}, \
						(%{integer:Event-Timestamp} - EXTRACT(EPOCH FROM(AcctStartTime)))), \
					AcctInputOctets = (('%{%{Acct-Input-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Input-Octets}:-0}'::bigint), \
					AcctOutputOctets = (('%{%{Acct-Output-Gigawords}:-0}'::bigint << 32) + \
						'%{%{Acct-Output-Octets}:-0}'::bigint), \
					AcctTerminateCause = '%{Acct-Terminate-Cause}', \
					FramedIPAddress = NULLIF('%{Framed-IP-Address}', '')::inet, \
					ConnectInfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		#
		#  No Acct-Status-Type == ignore the packet
		#
		none {
		     query = "SELECT true"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query                - Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query = "\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES(\
			'%{User-Name}', \
			'%{%{User-Password}:-Chap-Password}', \
			'%{reply:Packet-Type}', \
			NOW())"
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  main/sqlite/queries.conf -- SQLite configuration for default schema (schema.sql)
#
#  Id: e1e83bf94814ed8be6239977b7bacfed21c0cd6a $
# Safe characters list for sql queries. Everything else is replaced
# with their mime-encoded equivalents.
# The default list should be ok
#safe_characters = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_: /"
#######################################################################
#  Query config:  Username
#######################################################################
# This is the username that will get substituted, escaped, and added
# as attribute 'SQL-User-Name'. '%{SQL-User-Name}' should be used below
# everywhere a username substitution is needed so you you can be sure
# the username passed from the client is escaped properly.
#
# Uncomment the next line, if you want the sql_user_name to mean:
#
#	Use Stripped-User-Name, if it's there.
#	Else use User-Name, if it's there,
#	Else use hard-coded string "DEFAULT" as the user name.
#sql_user_name = "%{%{Stripped-User-Name}:-%{%{User-Name}:-DEFAULT}}"
#
sql_user_name = "%{User-Name}"
#######################################################################
# Default profile
#######################################################################
# This is the default profile. It is found in SQL by group membership.
# That means that this profile must be a member of at least one group
# which will contain the corresponding check and reply items.
# This profile will be queried in the authorize section for every user.
# The point is to assign all users a default profile without having to
# manually add each one to a group that will contain the profile.
# The SQL module will also honor the User-Profile attribute. This
# attribute can be set anywhere in the authorize section (ie the users
# file). It is found exactly as the default profile is found.
# If it is set then it will *overwrite* the default profile setting.
# The idea is to select profiles based on checks on the incoming packets,
# not on user group membership. For example:
# -- users file --
# DEFAULT	Service-Type == Outbound-User, User-Profile := "outbound"
# DEFAULT	Service-Type == Framed-User, User-Profile := "framed"
#
# By default the default_user_profile is not set
#
#default_user_profile = "DEFAULT"
#######################################################################
# NAS Query
#######################################################################
# This query retrieves the radius clients
#
# 0. Row ID (currently unused)
# 1. Name (or IP address)
# 2. Shortname
# 3. Type
# 4. Secret
# 5. Server
#######################################################################
client_query = "\
	SELECT id, nasname, shortname, type, secret, server \
	FROM ${client_table}"
#######################################################################
# Authorization Queries
#######################################################################
# These queries compare the check items for the user
# in ${authcheck_table} and setup the reply items in
# ${authreply_table}. You can use any query/tables
# you want, but the return data for each row MUST
# be in the following order:
#
# 0. Row ID (currently unused)
# 1. UserName/GroupName
# 2. Item Attr Name
# 3. Item Attr Value
# 4. Item Attr Operation
#######################################################################
#
#  Use these for case sensitive usernames.
#
#authorize_check_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authcheck_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#authorize_reply_query = "\
#	SELECT id, username, attribute, value, op \
#	FROM ${authreply_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY id"
#
#  The default queries are case insensitive. (for compatibility with older versions of FreeRADIUS)
#
authorize_check_query = "\
	SELECT id, username, attribute, value, op \
	FROM ${authcheck_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY id"
authorize_reply_query = "\
	SELECT id, username, attribute, value, op \
	FROM ${authreply_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY id"
#
# Use these for case sensitive usernames.
#
#group_membership_query = "\
#	SELECT groupname \
#	FROM ${usergroup_table} \
#	WHERE username = BINARY '%{SQL-User-Name}' \
#	ORDER BY priority"
group_membership_query = "\
	SELECT groupname \
	FROM ${usergroup_table} \
	WHERE username = '%{SQL-User-Name}' \
	ORDER BY priority"
authorize_group_check_query = "\
	SELECT id, groupname, attribute, \
	Value, op \
	FROM ${groupcheck_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY id"
authorize_group_reply_query = "\
	SELECT id, groupname, attribute, \
	value, op \
	FROM ${groupreply_table} \
	WHERE groupname = '%{${group_attribute}}' \
	ORDER BY id"
#######################################################################
# Simultaneous Use Checking Queries
#######################################################################
# simul_count_query	- query for the number of current connections
#			- If this is not defined, no simultaneous use checking
#			- will be performed by this module instance
# simul_verify_query	- query to return details of current connections
#				for verification
#			- Leave blank or commented out to disable verification step
#			- Note that the returned field order should not be changed.
#######################################################################
#
#  Uncomment simul_count_query to enable simultaneous use checking
#
#simul_count_query = "\
#	SELECT COUNT(*) \
#	FROM ${acct_table1} \
#	WHERE username = '%{SQL-User-Name}' \
#	AND acctstoptime IS NULL"
simul_verify_query = "\
	SELECT radacctid, acctsessionid, username, nasipaddress, nasportid, framedipaddress, \
		callingstationid, framedprotocol \
	FROM ${acct_table1} \
	WHERE username = '%{${group_attribute}}' \
	AND acctstoptime IS NULL"
#######################################################################
# Accounting and Post-Auth Queries
#######################################################################
# These queries insert/update accounting and authentication records.
# The query to use is determined by the value of 'reference'.
# This value is used as a configuration path and should resolve to one
# or more 'query's. If reference points to multiple queries, and a query
# fails, the next query is executed.
#
# Behaviour is identical to the old 1.x/2.x module, except we can now
# fail between N queries, and query selection can be based on any
# combination of attributes, or custom 'Acct-Status-Type' values.
#######################################################################
accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/accounting.sql
	column_list = "\
		acctsessionid, \
		acctuniqueid, \
		username, \
		realm, \
		nasipaddress, \
		nasportid, \
		nasporttype, \
		acctstarttime, \
		acctupdatetime, \
		acctstoptime, \
		acctsessiontime, \
		acctauthentic, \
		connectinfo_start, \
		connectinfo_stop, \
		acctinputoctets, \
		acctoutputoctets, \
		calledstationid, \
		callingstationid, \
		acctterminatecause, \
		servicetype, \
		framedprotocol, \
		framedipaddress"
	type {
		accounting-on {
			#
			#  Bulk terminate all sessions associated with a given NAS
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctstoptime = %{%{integer:Event-Timestamp}:-date('now')}, \
					acctsessiontime	= \
						(%{%{integer:Event-Timestamp}:-strftime('%%s', 'now')} \
						- strftime('%%s', acctstarttime)), \
					acctterminatecause = '%{Acct-Terminate-Cause}' \
				WHERE acctstoptime IS NULL \
				AND nasipaddress   = '%{NAS-IP-Address}' \
				AND acctstarttime <= %{integer:Event-Timestamp}"
		}
		accounting-off {
			query = "${..accounting-on.query}"
		}
		start {
			#
			#  Insert a new record into the sessions table
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					%{%{integer:Event-Timestamp}:-date('now')}, \
					%{%{integer:Event-Timestamp}:-date('now')}, \
					NULL, \
					'0', \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					'0', \
					'0', \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
			#
			#  Key constraints prevented us from inserting a new session,
			#  use the alternate query to update an existing session.
			#
			query = "\
				UPDATE ${....acct_table1} SET \
					acctstarttime	= %{%{integer:Event-Timestamp}:-date('now')}, \
					acctupdatetime	= %{%{integer:Event-Timestamp}:-date('now'))}, \
					connectinfo_start = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
		}
		interim-update {
			#
			#  Update an existing session and calculate the interval
			#  between the last data we received for the session and this
			#  update. This can be used to find stale sessions.
			#
			query = "\
				UPDATE ${....acct_table1} \
				SET \
					acctupdatetime  = %{%{integer:Event-Timestamp}:-date('now')}, \
					acctinterval    = 0, \
					framedipaddress = '%{Framed-IP-Address}', \
					acctsessiontime = %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets = %{%{Acct-Input-Gigawords}:-0} \
						<< 32 | %{%{Acct-Input-Octets}:-0}, \
					acctoutputoctets = %{%{Acct-Output-Gigawords}:-0} \
						<< 32 | %{%{Acct-Output-Octets}:-0} \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table1} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					(%{%{integer:Event-Timestamp}:-strftime('%%s', 'now')} - %{%{Acct-Session-Time}:-0}), \
					%{%{integer:Event-Timestamp}:-date('now')}, \
					NULL, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'%{Connect-Info}', \
					'', \
					%{%{Acct-Input-Gigawords}:-0} << 32 | \
						%{%{Acct-Input-Octets}:-0}, \
					%{%{Acct-Output-Gigawords}:-0} << 32 | \
						%{%{Acct-Output-Octets}:-0}, \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
		stop {
			#
			#  Session has terminated, update the stop time and statistics.
			#
			query = "\
				UPDATE ${....acct_table2} SET \
					acctstoptime	= %{%{integer:Event-Timestamp}:-date('now')}, \
					acctsessiontime	= %{%{Acct-Session-Time}:-NULL}, \
					acctinputoctets	= %{%{Acct-Input-Gigawords}:-0} \
						<< 32 | %{%{Acct-Input-Octets}:-0}, \
					acctoutputoctets = %{%{Acct-Output-Gigawords}:-0} \
						<< 32 | %{%{Acct-Output-Octets}:-0}, \
					acctterminatecause = '%{Acct-Terminate-Cause}', \
					connectinfo_stop = '%{Connect-Info}' \
				WHERE AcctUniqueId = '%{Acct-Unique-Session-Id}'"
			#
			#  The update condition matched no existing sessions. Use
			#  the values provided in the update to create a new session.
			#
			query = "\
				INSERT INTO ${....acct_table2} \
					(${...column_list}) \
				VALUES \
					('%{Acct-Session-Id}', \
					'%{Acct-Unique-Session-Id}', \
					'%{SQL-User-Name}', \
					'%{Realm}', \
					'%{NAS-IP-Address}', \
					'%{%{NAS-Port-ID}:-%{NAS-Port}}', \
					'%{NAS-Port-Type}', \
					(%{%{integer:Event-Timestamp}:-strftime('%%s', 'now')} - %{%{Acct-Session-Time}:-0}), \
					%{%{integer:Event-Timestamp}:-date('now')}, \
					%{%{integer:Event-Timestamp}:-date('now')}, \
					%{%{Acct-Session-Time}:-NULL}, \
					'%{Acct-Authentic}', \
					'', \
					'%{Connect-Info}', \
					%{%{Acct-Input-Gigawords}:-0} << 32 | \
						%{%{Acct-Input-Octets}:-0}, \
					%{%{Acct-Output-Gigawords}:-0} << 32 | \
						%{%{Acct-Output-Octets}:-0}, \
					'%{Called-Station-Id}', \
					'%{Calling-Station-Id}', \
					'%{Acct-Terminate-Cause}', \
					'%{Service-Type}', \
					'%{Framed-Protocol}', \
					'%{Framed-IP-Address}')"
		}
	}
}
#######################################################################
# Authentication Logging Queries
#######################################################################
# postauth_query	- Insert some info after authentication
#######################################################################
post-auth {
	# Write SQL queries to a logfile. This is potentially useful for bulk inserts
	# when used with the rlm_sql_null driver.
#	logfile = ${logdir}/post-auth.sql
	query =	"\
		INSERT INTO ${..postauth_table} \
			(username, pass, reply, authdate) \
		VALUES ( \
			'%{SQL-User-Name}', \
			'%{%{User-Password}:-%{Chap-Password}}', \
			'%{reply:Packet-Type}', \
			'%S')"
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  moonshot-targeted-ids/mysql/queries.conf -- Queries to update a MySQL Moonshot-Targeted-Ids table.
#
#  $Id: 68306db5a6c67f70804dc019e19daba5e938b4a9 $
post-auth {
	#  Query to store the Moonshot-*-TargetedId
	query = "\
		INSERT IGNORE INTO ${..moonshot_tid_table} \
			(gss_acceptor, namespace, username, targeted_id) \
		VALUES \
			('%{control:Moonshot-MSTID-GSS-Acceptor}', '%{control:Moonshot-MSTID-Namespace}', \
			'%{tolower:%{User-Name}}', '%{control:Moonshot-MSTID-TargetedId}')"
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  moonshot-targeted-ids/postgresql/queries.conf -- Queries to update a PostgreSQL Moonshot-*-Targeted-Ids table.
#
#  $Id: f757a870a0b68c5dc3827c00bb501082fc7e03e9 $
post-auth {
	#  Query to store the Moonshot-*-TargetedId
	query = "\
		INSERT INTO ${..moonshot_tid_table} \
			(gss_acceptor, namespace, username, targeted_id) \
		VALUES \
			('%{control:Moonshot-MSTID-GSS-Acceptor}', '%{control:Moonshot-MSTID-Namespace}', \
			'%{tolower:%{User-Name}}', '%{control:Moonshot-MSTID-TargetedId}')"
}
================================================

File: queries.conf
================================================
# -*- text -*-
#
#  moonshot-targeted-ids/sqlite/queries.conf -- Queries to update a sqlite Moonshot-*-Targeted-Ids table.
#
#  $Id: 8cdb80382db6e94067a75c0428b375847eb04ad8 $
post-auth {
	#  Query to store the Moonshot-*-TargetedId
	query = "\
		INSERT INTO ${..moonshot_tid_table} \
			(gss_acceptor, namespace, username, targeted_id) \
		VALUES \
			('%{control:Moonshot-MSTID-GSS-Acceptor}', '%{control:Moonshot-MSTID-Namespace}', \
			'%{tolower:%{User-Name}}', '%{control:Moonshot-MSTID-TargetedId}')"
}
================================================

File: default.conf
================================================
server:
 num-threads: 2
================================================

File: proxy.conf
================================================
# -*- text -*-
##
## proxy.conf -- proxy radius and realm configuration directives
##
##	$Id: ba510994ae2a68af00642b5c3aa46091cc4b00f3 $
#######################################################################
#
#  Proxy server configuration
#
#  This entry controls the servers behaviour towards ALL other servers
#  to which it sends proxy requests.
#
proxy server {
	#
	#  Note that as of 2.0, the "synchronous", "retry_delay",
	#  "retry_count", and "dead_time" have all been deprecated.
	#  For backwards compatibility, they are are still accepted
	#  by the server, but they ONLY apply to the old-style realm
	#  configuration.  i.e. realms with "authhost" and/or "accthost"
	#  entries.
	#
	#  i.e. "retry_delay" and "retry_count" have been replaced
	#  with per-home-server configuration.  See the "home_server"
	#  example below for details.
	#
	#  i.e. "dead_time" has been replaced with a per-home-server
	#  "revive_interval".  We strongly recommend that this not
	#  be used, however.  The new method is much better.
	#
	#  In 2.0, the server is always "synchronous", and setting
	#  "synchronous = no" is impossible.  This simplifies the
	#  server and increases the stability of the network.
	#  However, it means that the server (i.e. proxy) NEVER
	#  originates packets.  It proxies packets ONLY when it receives
	#  a packet or a re-transmission from the NAS.  If the NAS never
	#  re-transmits, the proxy never re-transmits, either.  This can
	#  affect fail-over, where a packet does *not* fail over to a
	#  second home server.. because the NAS never retransmits the
	#  packet.
	#
	#  If you need to set "synchronous = no", please send a
	#  message to the list <freeradius-users@lists.freeradius.org>
	#  explaining why this feature is vital for your network.
	#
	#  If a realm exists, but there are no live home servers for
	#  it, we can fall back to using the "DEFAULT" realm.  This is
	#  most useful for accounting, where the server can proxy
	#  accounting requests to home servers, but if they're down,
	#  use a DEFAULT realm that is LOCAL (i.e. accthost = LOCAL),
	#  and then store the packets in the "detail" file.  That data
	#  can be later proxied to the home servers by radrelay, when
	#  those home servers come back up again.
	#  Setting this to "yes" may have issues for authentication.
	#  i.e. If you are proxying for two different ISP's, and then
	#  act as a general dial-up for Gric.  If one of the first two
	#  ISP's has their RADIUS server go down, you do NOT want to
	#  proxy those requests to GRIC.  Instead, you probably want
	#  to just drop the requests on the floor.  In that case, set
	#  this value to 'no'.
	#
	#  allowed values: {yes, no}
	#
	default_fallback = no
}
#######################################################################
#
#  Configuration for the proxy realms.
#
#  As of 2.0, the "realm" configuration has changed.  Instead of
#  specifying "authhost" and "accthost" in a realm section, the home
#  servers are specified separately in a "home_server" section.  For
#  backwards compatibility, you can still use the "authhost" and
#  "accthost" directives.  If you only have one home server for a
#  realm, it is easier to use the old-style configuration.
#
#  However, if you have multiple servers for a realm, we STRONGLY
#  suggest moving to the new-style configuration.
#
#
#  Load-balancing and failover between home servers is handled via
#  a "home_server_pool" section.
#
#  Finally, The "realm" section defines the realm, some options, and
#  indicates which server pool should be used for the realm.
#
#  This change means that simple configurations now require multiple
#  sections to define a realm.  However, complex configurations
#  are much simpler than before, as multiple realms can share the same
#  server pool.
#
#  That is, realms point to server pools, and server pools point to
#  home servers.  Multiple realms can point to one server pool.  One
#  server pool can point to multiple home servers.  Each home server
#  can appear in one or more pools.
#
#  See sites-available/tls for an example of configuring home servers,
#  pools, and realms with TLS.
#
######################################################################
#
#  This section defines a "Home Server" which is another RADIUS
#  server that gets sent proxied requests.  In earlier versions
#  of FreeRADIUS, home servers were defined in "realm" sections,
#  which was awkward.  In 2.0, they have been made independent
#  from realms, which is better for a number of reasons.
#
home_server localhost {
	#
	#  Home servers can be sent Access-Request packets
	#  or Accounting-Request packets.
	#
	#  Allowed values are:
	#	auth	  - Handles Access-Request packets
	#	acct	  - Handles Accounting-Request packets
	#	auth+acct - Handles Access-Request packets at "port",
	#		    and Accounting-Request packets at "port + 1"
	#	coa	  - Handles CoA-Request and Disconnect-Request packets.
	#		    See also raddb/sites-available/originate-coa
	type = auth
	#
	#  Configure ONE OF the following entries:
	#
	#	IPv4 address
	#
	ipaddr = 127.0.0.1
	#	OR IPv6 address
	# ipv6addr = ::1
	#	OR virtual server
	# virtual_server = foo
	#	Note that while both ipaddr and ipv6addr will accept
	#	both addresses and host names, we do NOT recommend
	#	using host names.  When you specify a host name, the
	#	server has to do a DNS lookup to find the IP address
	#	of the home server.  If the DNS server is slow or
	#	unresponsive, it means that FreeRADIUS will NOT be
	#	able to determine the address, and will therefore NOT
	#	start.
	#
	#	Also, the mapping of host name to address is done ONCE
	#	when the server starts.  If DNS is later updated to
	#	change the address, FreeRADIUS will NOT discover that
	#	until after a re-start, or a HUP.
	#
	#	If you specify a virtual_server here, then requests
	#	will be proxied internally to that virtual server.
	#	These requests CANNOT be proxied again, however.  The
	#	intent is to have the local server handle packets
	#	when all home servers are dead.
	#
	#	Requests proxied to a virtual server will be passed
	#	through the pre-proxy and post-proxy sections, just
	#	like any other request.  See also the sample "realm"
	#	configuration, below.
	#
	#	None of the rest of the home_server configuration is used
	#	for the "virtual_server" configuration.
	#
	#  The port to which packets are sent.
	#
	#  Usually 1812 for type "auth", and  1813 for type "acct".
	#  Older servers may use 1645 and 1646.
	#  Use 3799 for type "coa"
	#
	port = 1812
	#
	#  The transport protocol.
	#
	#  If unspecified, defaults to "udp", which is the traditional
	#  RADIUS transport.  It may also be "tcp", in which case TCP
	#  will be used to talk to this home server.
	#
	#  When home servers are put into pools, the pool can contain
	#  home servers with both UDP and TCP transports.
	#
	#proto = udp
	#
	#  The shared secret use to "encrypt" and "sign" packets between
	#  FreeRADIUS and the home server.
	#
	#  The secret can be any string, up to 8k characters in length.
	#
	#  Control codes can be entered vi octal encoding,
	#	e.g. "\101\102" == "AB"
	#  Quotation marks can be entered by escaping them,
	#	e.g. "foo\"bar"
	#  Spaces or other "special" characters can be entered
	#  by putting quotes around the string.
	#	e.g. "foo bar"
	#	     "foo;bar"
	#
	secret = $ENV{RADIUS_KEY}
	############################################################
	#
	#  The rest of the configuration items listed here are optional,
	#  and do not have to appear in every home server definition.
	#
	############################################################
	#
	#  You can optionally specify the source IP address used when
	#  proxying requests to this home server.  When the src_ipaddr
	#  it set, the server will automatically create a proxy
	#  listener for that IP address.
	#
	#  If you specify this field for one home server, you will
	#  likely need to specify it for ALL home servers.
	#
	#  If you don't care about the source IP address, leave this
	#  entry commented.
	#
#	src_ipaddr = 127.0.0.1
	#
	#  If the home server does not respond to a request within
	#  this time, the server marks the request as timed out.
	#  After "response_timeouts", the home server is marked
	#  as being "zombie", and "zombie_period" starts.
	#
	#  The response window can be a number between 0.001 and 60.000
	#  Values on the low end are discouraged, as they will likely
	#  not work due to limitations of operating system timers.
	#
	#  The default response window is large because responses may
	#  be slow, especially when proxying across the Internet.
	#
	#  Useful range of values: 5 to 60
	response_window = 20
	#
	#  Start "zombie_period" after this many responses have
	#  timed out.
	#
#	response_timeouts = 1
	#
	#  If you want the old behaviour of the server rejecting
	#  proxied requests after "response_window" timeout, set
	#  the following configuration item to "yes".
	#
	#  This configuration WILL be removed in a future release
	#  If you believe you need it, email the freeradius-users
	#  list, and explain why it should stay in the server.
	#
#	no_response_fail = no
	#
	#  If the home server does not respond to ANY packets during
	#  the "zombie period", it will be considered to be dead.
	#
	#  A home server that is marked "zombie" will be used for
	#  proxying as a low priority.  If there are live servers,
	#  they will always be preferred to a zombie.  Requests will
	#  be proxied to a zombie server ONLY when there are no
	#  live servers.
	#
	#  Any request that is proxied to a home server will continue
	#  to be sent to that home server until the home server is
	#  marked dead.  At that point, it will fail over to another
	#  server, if a live server is available.  If none is available,
	#  then the "post-proxy-type fail" handler will be called.
	#
	#  If "status_check" below is something other than "none", then
	#  the server will start sending status checks at the start of
	#  the zombie period.  It will continue sending status checks
	#  until the home server is marked "alive".
	#
	#  Useful range of values: 20 to 120
	zombie_period = 40
	############################################################
	#
	#  As of 2.0, FreeRADIUS supports RADIUS layer "status
	#  checks".  These are used by a proxy server to see if a home
	#  server is alive.
	#
	#  These status packets are sent ONLY if the proxying server
	#  believes that the home server is dead.  They are NOT sent
	#  if the proxying server believes that the home server is
	#  alive.  They are NOT sent if the proxying server is not
	#  proxying packets.
	#
	#  If the home server responds to the status check packet,
	#  then it is marked alive again, and is returned to use.
	#
	############################################################
	#
	#  Some home servers do not support status checks via the
	#  Status-Server packet.  Others may not have a "test" user
	#  configured that can be used to query the server, to see if
	#  it is alive.  For those servers, we have NO WAY of knowing
	#  when it becomes alive again.  Therefore, after the server
	#  has been marked dead, we wait a period of time, and mark
	#  it alive again, in the hope that it has come back to
	#  life.
	#
	#  If it has NOT come back to life, then FreeRADIUS will wait
	#  for "zombie_period" before marking it dead again.  During
	#  the "zombie_period", ALL AUTHENTICATIONS WILL FAIL, because
	#  the home server is still dead.  There is NOTHING that can
	#  be done about this, other than to enable the status checks,
	#  as documented below.
	#
	#  e.g. if "zombie_period" is 40 seconds, and "revive_interval"
	#  is 300 seconds, the for 40 seconds out of every 340, or about
	#  10% of the time, all authentications will fail.
	#
	#  If the "zombie_period" and "revive_interval" configurations
	#  are set smaller, than it is possible for up to 50% of
	#  authentications to fail.
	#
	#  As a result, we recommend enabling status checks, and
	#  we do NOT recommend using "revive_interval".
	#
	#  The "revive_interval" is used ONLY if the "status_check"
	#  entry below is "none".  Otherwise, it will not be used,
	#  and should be deleted.
	#
	#  Useful range of values: 60 to 3600
	revive_interval = 120
	#
	#  The proxying server (i.e. this one) can do periodic status
	#  checks to see if a dead home server has come back alive.
	#
	#  If set to "none", then the other configuration items listed
	#  below are not used, and the "revive_interval" time is used
	#  instead.
	#
	#  If set to "status-server", the Status-Server packets are
	#  sent.  Many RADIUS servers support Status-Server.  If a
	#  server does not support it, please contact the server
	#  vendor and request that they add it. With status-server if
	#  the home server is marked as a zombie and a status-server
	#  response is received, it will be immediately marked as live.
	#
	#  This prevents spurious failovers in federations such as 
	#  eduroam, where intermediary proxy servers may be functional
	#  but the servers of a home institution may not be,
	#
	#  If set to "request", then Access-Request, or Accounting-Request
	#  packets are sent, depending on the "type" entry above (auth/acct).
	#
	#  Allowed values: none, status-server, request
	status_check = status-server
	#
	#  If the home server does not support Status-Server packets,
	#  then the server can still send Access-Request or
	#  Accounting-Request packets, with a pre-defined user name.
	#
	#  This practice is NOT recommended, as it may potentially let
	#  users gain network access by using these "test" accounts!
	#
	#  If it is used, we recommend that the home server ALWAYS
	#  respond to these Access-Request status checks with
	#  Access-Reject.  The status check just needs an answer, it
	#  does not need an Access-Accept.
	#
	#  For Accounting-Request status checks, only the username
	#  needs to be set.  The rest of the accounting attribute are
	#  set to default values.  The home server that receives these
	#  accounting packets SHOULD NOT treat them like normal user
	#  accounting packets.  i.e It should probably NOT log them to
	#  a database.
	#
	# username = "test_user_please_reject_me"
	# password = "this is really secret"
	#
	#  Configure the interval between sending status check packets.
	#
	#  Setting it too low increases the probability of spurious
	#  fail-over and fallback attempts.
	#
	#  Useful range of values: 6 to 120
	check_interval = 30
	#
	#  Wait "check_timeout" seconds for a reply to a status check
	#  packet.
	#
	check_timeout = 4
	#
	#  Configure the number of status checks in a row that the
	#  home server needs to respond to before it is marked alive.
	#
	#  If you want to mark a home server as alive after a short
	#  time period of being responsive, it is best to use a small
	#  "check_interval", and a large value for
	#  "num_answers_to_alive".  Using a long "check_interval" and
	#  a small number for "num_answers_to_alive" increases the
	#  probability of spurious fail-over and fallback attempts.
	#
	#  Useful range of values: 3 to 10
	num_answers_to_alive = 3
	#
	#  Limit the total number of outstanding packets to the home
	#  server.
	#
	#  if ((#request sent) - (#requests received)) > max_outstanding
	#	then stop sending more packets to the home server
	#
	#  This lets us gracefully fall over when the home server
	#  is overloaded.
	max_outstanding = 65536
	#
	#  The configuration items in the next sub-section are used ONLY
	#  when "type = coa".  It is ignored for all other type of home
	#  servers.
	#
	#  See RFC 5080 for the definitions of the following terms.
	#  RAND is a function (internal to FreeRADIUS) returning
	#  random numbers between -0.1 and +0.1
	#
	#  First Re-transmit occurs after:
	#
	#	 RT = IRT + RAND*IRT
	#
	#  Subsequent Re-transmits occur after:
	#
	#	RT = 2 * RTprev + RAND * RTprev
	#
	#  Re-transmits are capped at:
	#
	#	if (MRT && (RT > MRT)) RT = MRT + RAND * MRT
	#
	#  For a maximum number of attempts: MRC
	#
	#  For a maximum (total) period of time: MRD.
	#
	coa {
		# Initial retransmit interval: 1..5
		irt = 2
		# Maximum Retransmit Timeout: 1..30 (0 == no maximum)
		mrt = 16
		# Maximum Retransmit Count: 1..20 (0 == retransmit forever)
		mrc = 5
		# Maximum Retransmit Duration: 5..60
		mrd = 30
	}
	#
	#  Connection limiting for home servers with "proto = tcp".
	#
	#  This section is ignored for other home servers.
	#
	limit {
	      #
	      #  Limit the number of TCP connections to the home server.
	      #
	      #  The default is 16.
	      #  Setting this to 0 means "no limit"
	      max_connections = 16
	      #
	      #  Limit the total number of requests sent over one
	      #  TCP connection.  After this number of requests, the
	      #  connection will be closed.  Any new packets that are
	      #  proxied to the home server will result in a new TCP
	      #  connection being made.
	      #
	      #  Setting this to 0 means "no limit"
	      max_requests = 0
	      #
	      #  The lifetime, in seconds, of a TCP connection.  After
	      #  this lifetime, the connection will be closed.
	      #
	      #  Setting this to 0 means "forever".
	      lifetime = 0
	      #
	      #  The idle timeout, in seconds, of a TCP connection.
	      #  If no packets have been sent over the connection for
	      #  this time, the connection will be closed.
	      #
	      #  Setting this to 0 means "no timeout".
	      idle_timeout = 0
	}
}
# Sample virtual home server.
#
#
#home_server virtual.example.com {
#	    virtual_server = virtual.example.com
#}
######################################################################
#
#  This section defines a pool of home servers that is used
#  for fail-over and load-balancing.  In earlier versions of
#  FreeRADIUS, fail-over and load-balancing were defined per-realm.
#  As a result, if a server had 5 home servers, each of which served
#  the same 10 realms, you would need 50 "realm" entries.
#
#  In version 2.0, you would need 5 "home_server" sections,
#  10 'realm" sections, and one "home_server_pool" section to tie the
#  two together.
#
home_server_pool my_auth_failover {
	#
	#  The type of this pool controls how home servers are chosen.
	#
	#  fail-over - the request is sent to the first live
	#  	home server in the list.  i.e. If the first home server
	#	is marked "dead", the second one is chosen, etc.
	#
	#  load-balance - the least busy home server is chosen,
	#	where "least busy" is counted by taking the number of
	#	requests sent to that home server, and subtracting the
	#	number of responses received from that home server.
	#
	#	If there are two or more servers with the same low
	#	load, then one of those servers is chosen at random.
	#	This configuration is most similar to the old
	#	"round-robin" method, though it is not exactly the same.
	#
	#	Note that load balancing does not work well with EAP,
	#	as EAP requires packets for an EAP conversation to be
	#	sent to the same home server.  The load balancing method
	#	does not keep state in between packets, meaning that
	#	EAP packets for the same conversation may be sent to
	#	different home servers.  This will prevent EAP from
	#	working.
	#
	#	For non-EAP authentication methods, and for accounting
	#	packets, we recommend using "load-balance".  It will
	#	ensure the highest availability for your network.
	#
	#  client-balance - the home server is chosen by hashing the
	#	source IP address of the packet.  If that home server
	#	is down, the next one in the list is used, just as
	#	with "fail-over".
	#
	#	There is no way of predicting which source IP will map
	#	to which home server.
	#
	#	This configuration is most useful to do simple load
	#	balancing for EAP sessions, as the EAP session will
	#	always be sent to the same home server.
	#
	#  client-port-balance - the home server is chosen by hashing
	#	the source IP address and source port of the packet.
	#	If that home server is down, the next one in the list
	#	is used, just as with "fail-over".
	#
	#	This method provides slightly better load balancing
	#	for EAP sessions than "client-balance".  However, it
	#	also means that authentication and accounting packets
	#	for the same session MAY go to different home servers.
	#
	#  keyed-balance - the home server is chosen by hashing (FNV)
	#	the contents of the Load-Balance-Key attribute from the
	#	control items.  The  request is then sent to home server
	#	chosen by taking:
	#
	#		server = (hash % num_servers_in_pool).
	#
	#	If there is no Load-Balance-Key in the control items,
	#	the load balancing method is identical to "load-balance".
	#
	#	For most non-EAP authentication methods, The User-Name
	#	attribute provides a good key.  An "unlang" policy can
	#	be used to copy the User-Name to the Load-Balance-Key
	#	attribute.  This method may not work for EAP sessions,
	#	as the User-Name outside of the TLS tunnel is often
	#	static, e.g. "anonymous@realm".
	#
	#
	#  The default type is fail-over.
	type = fail-over
	#
	#  A virtual_server may be specified here.  If so, the
	#  "pre-proxy" and "post-proxy" sections are called when
	#  the request is proxied, and when a response is received.
	#
	#  This lets you have one policy for all requests that are proxied
	#  to a home server.  This policy is completely independent of
	#  any policies used to receive, or process the request.
	#
	#virtual_server = pre_post_proxy_for_pool
	#
	#  Next, a list of one or more home servers.  The names
	#  of the home servers are NOT the hostnames, but the names
	#  of the sections.  (e.g. home_server foo {...} has name "foo".
	#
	#  Note that ALL home servers listed here have to be of the same
	#  type.  i.e. they all have to be "auth", or they all have to
	#  be "acct", or the all have to be "auth+acct".
	#
	home_server = localhost
	#  Additional home servers can be listed.
	#  There is NO LIMIT to the number of home servers that can
	#  be listed, though using more than 10 or so will become
	#  difficult to manage.
	#
	# home_server = foo.example.com
	# home_server = bar.example.com
	# home_server = baz.example.com
	# home_server = ...
	#
	#  If ALL home servers are dead, then this "fallback" home server
	#  is used.  If set, it takes precedence over any realm-based
	#  fallback, such as the DEFAULT realm.
	#
	#  For reasons of stability, this home server SHOULD be a virtual
	#  server.  Otherwise, the fallback may itself be dead!
	#
	#fallback = virtual.example.com
}
######################################################################
#
#
#  This section defines a new-style "realm".  Note the in version 2.0,
#  there are many fewer configuration items than in 1.x for a realm.
#
#  Automatic proxying is done via the "realms" module (see "man
#  rlm_realm").  To manually proxy the request put this entry in the
#  "users" file:
#
#
#DEFAULT	Proxy-To-Realm := "realm_name"
#
#
realm example.com {
	#
	#  Realms point to pools of home servers.
#
	#  For authentication, the "auth_pool" configuration item
	#  should point to a "home_server_pool" that was previously
	#  defined.  All of the home servers in the "auth_pool" must
	#  be of type "auth".
	#
	#  For accounting, the "acct_pool" configuration item
	#  should point to a "home_server_pool" that was previously
	#  defined.  All of the home servers in the "acct_pool" must
	#  be of type "acct".
	#
	#  If you have a "home_server_pool" where all of the home servers
	#  are of type "auth+acct", you can just use the "pool"
	#  configuration item, instead of specifying both "auth_pool"
	#  and "acct_pool".
	auth_pool = my_auth_failover
#	acct_pool = acct
	#  As of Version 3.0, the server can proxy CoA packets
	#  based on the Operator-Name attribute.  This requires
	#  that the "suffix" module be listed in the "recv-coa"
	#  section.
	#
	#  See raddb/sites-available/coa
	#
#	coa_pool = name_of_coa_pool
	#
	#  Normally, when an incoming User-Name is matched against the
	#  realm, the realm name is "stripped" off, and the "stripped"
	#  user name is used to perform matches.
	#
	#  e.g. User-Name = "bob@example.com" will result in two new
	#  attributes being created by the "realms" module:
	#
	#	Stripped-User-Name = "bob"
	#	Realm = "example.com"
	#
	#  The Stripped-User-Name is then used as a key in the "users"
	#  file, for example.
	#
	#  If you do not want this to happen, uncomment "nostrip" below.
	#
	# nostrip
	#  There are no more configuration entries for a realm.
}
#
#  This is a sample entry for iPass.
#  Note that you have to define "ipass_auth_pool" and
#  "ipass_acct_pool", along with home_servers for them, too.
#
#realm IPASS {
#	nostrip
#
#	auth_pool = ipass_auth_pool
#	acct_pool = ipass_acct_pool
#}
#
#  This realm is used mainly to cancel proxying.  You can have
#  the "realm suffix" module configured to proxy all requests for
#  a realm, and then later cancel the proxying, based on other
#  configuration.
#
#  For example, you want to terminate PEAP or EAP-TTLS locally,
#  you can add the following to the "users" file:
#
#  DEFAULT EAP-Type == PEAP, Proxy-To-Realm := LOCAL
#
realm LOCAL {
	#  If we do not specify a server pool, the realm is LOCAL, and
	#  requests are not proxied to it.
}
#
#  This realm is for requests which don't have an explicit realm
#  prefix or suffix.  User names like "bob" will match this one.
#
#realm NULL {
#	authhost	= radius.example.com:1600
#	accthost	= radius.example.com:1601
#	secret		= testing123
#}
#
#  This realm is for ALL OTHER requests.
#
#realm DEFAULT {
#	authhost	= radius.example.com:1600
#	accthost	= radius.example.com:1601
#	secret		= testing123
#}
#  This realm "proxies" requests internally to a virtual server.
#  The pre-proxy and post-proxy sections are run just as with any
#  other kind of home server.  The virtual server then receives
#  the request, and replies, just as with any other packet.
#
#  Once proxied internally like this, the request CANNOT be proxied
#  internally or externally.
#
#realm virtual.example.com {
#	virtual_server = virtual.example.com
#}
#
#
#  Regular expressions may also be used as realm names.  If these are used,
#  then the "find matching realm" process is as follows:
#
#    1) Look for a non-regex realm with an *exact* match for the name.
#       If found, it is used in preference to any regex matching realm.
#
#    2) Look for a regex realm, in the order that they are listed
#       in the configuration files.  Any regex match is performed in
#	a case-insensitive fashion.
#
#    3) If no realm is found, return the DEFAULT realm, if any.
#
#  The order of the realms matters in step (2).  For example, defining
#  two realms ".*\.example.net$" and ".*\.test\.example\.net$" will result in
#  the second realm NEVER matching.  This is because all of the realms
#  which match the second regex also match the first one.  Since the
#  first regex matches, it is returned.
#
#  The solution is to list the realms in the opposite order,. e.g.
#  ".*\.test\.example.net$", followed by ".*\.example\.net$".
#
#
#  Some helpful rules:
#
#   - always place a '~' character at the start of the realm name.
#     This signifies that it is a regex match, and not an exact match
#     for the realm.
#
#   - place the regex in double quotes.  This helps the configuration
#     file parser ignore any "special" characters in the regex.
#     Yes, this rule is different than the normal "unlang" rules for
#     regular expressions.  That may be fixed in a future release.
#
#   - for version 3.0.4 and following, with "correct_escapes = true",
#     use normal regex backslash rules.  Just one.  Not two.
#
#   - If you are matching domain names, put a '$' at the end of the regex
#     that matches the domain name.  This tells the regex matching code
#     that the realm ENDS with the domain name, so it does not match
#     realms with the domain name in the middle.  e.g. "~.*\.example\.net"
#     will match "test.example.netFOO", which is likely not what you want.
#     Using "~(.*\.)example\.net$" is better.
#
#  The more regex realms that are defined, the more time it takes to
#  process them.  You should define as few regex realms as possible
#  in order to maximize server performance.
#
#realm "~(.*\.)*example\.net$" {
#      auth_pool = my_auth_failover
#}
================================================

File: radiusd.conf
================================================
# -*- text -*-
##
## radiusd.conf	-- FreeRADIUS server configuration file - 3.0.17
##
##	http://www.freeradius.org/
##	$Id: 59e59f3ac443e75663333a5b7732664b67c5567d $
##
######################################################################
#
#	Read "man radiusd" before editing this file.  See the section
#	titled DEBUGGING.  It outlines a method where you can quickly
#	obtain the configuration you want, without running into
#	trouble.
#
#	Run the server in debugging mode, and READ the output.
#
#		$ radiusd -X
#
#	We cannot emphasize this point strongly enough.  The vast
#	majority of problems can be solved by carefully reading the
#	debugging output, which includes warnings about common issues,
#	and suggestions for how they may be fixed.
#
#	There may be a lot of output, but look carefully for words like:
#	"warning", "error", "reject", or "failure".  The messages there
#	will usually be enough to guide you to a solution.
#
#	If you are going to ask a question on the mailing list, then
#	explain what you are trying to do, and include the output from
#	debugging mode (radiusd -X).  Failure to do so means that all
#	of the responses to your question will be people telling you
#	to "post the output of radiusd -X".
######################################################################
#
#  	The location of other config files and logfiles are declared
#  	in this file.
#
#  	Also general configuration for modules can be done in this
#  	file, it is exported through the API to modules that ask for
#  	it.
#
#	See "man radiusd.conf" for documentation on the format of this
#	file.  Note that the individual configuration items are NOT
#	documented in that "man" page.  They are only documented here,
#	in the comments.
#
#	The "unlang" policy language can be used to create complex
#	if / else policies.  See "man unlang" for details.
#
prefix = /usr
exec_prefix = ${prefix}
sysconfdir = /etc
localstatedir = /var
sbindir = ${exec_prefix}/sbin
logdir = /var/log/radius
raddbdir = ${sysconfdir}/raddb
radacctdir = /var/log/radius/radacct
#
#  name of the running server.  See also the "-n" command-line option.
name = radiusd
#  Location of config and logfiles.
confdir = ${raddbdir}
modconfdir = ${confdir}/mods-config
certdir = ${confdir}/certs
cadir   = ${confdir}/certs
run_dir = ${localstatedir}/run/${name}
# Should likely be ${localstatedir}/lib/radiusd
db_dir = ${raddbdir}
#
# libdir: Where to find the rlm_* modules.
#
#   This should be automatically set at configuration time.
#
#   If the server builds and installs, but fails at execution time
#   with an 'undefined symbol' error, then you can use the libdir
#   directive to work around the problem.
#
#   The cause is usually that a library has been installed on your
#   system in a place where the dynamic linker CANNOT find it.  When
#   executing as root (or another user), your personal environment MAY
#   be set up to allow the dynamic linker to find the library.  When
#   executing as a daemon, FreeRADIUS MAY NOT have the same
#   personalized configuration.
#
#   To work around the problem, find out which library contains that symbol,
#   and add the directory containing that library to the end of 'libdir',
#   with a colon separating the directory names.  NO spaces are allowed.
#
#   e.g. libdir = /usr/local/lib:/opt/package/lib
#
#   You can also try setting the LD_LIBRARY_PATH environment variable
#   in a script which starts the server.
#
#   If that does not work, then you can re-configure and re-build the
#   server to NOT use shared libraries, via:
#
#	./configure --disable-shared
#	make
#	make install
#
libdir = /usr/lib/freeradius
#  pidfile: Where to place the PID of the RADIUS server.
#
#  The server may be signalled while it's running by using this
#  file.
#
#  This file is written when ONLY running in daemon mode.
#
#  e.g.:  kill -HUP `cat /var/run/radiusd/radiusd.pid`
#
pidfile = ${run_dir}/${name}.pid
#
#  correct_escapes: use correct backslash escaping
#
#  Prior to version 3.0.5, the handling of backslashes was a little
#  awkward, i.e. "wrong".  In some cases, to get one backslash into
#  a regex, you had to put 4 in the config files.
#
#  Version 3.0.5 fixes that.  However, for backwards compatibility,
#  the new method of escaping is DISABLED BY DEFAULT.  This means
#  that upgrading to 3.0.5 won't break your configuration.
#
#  If you don't have double backslashes (i.e. \\) in your configuration,
#  this won't matter to you.  If you do have them, fix that to use only
#  one backslash, and then set "correct_escapes = true".
#
#  You can check for this by doing:
#
#	$ grep '\\\\' $(find raddb -type f -print)
#
correct_escapes = true
#  panic_action: Command to execute if the server dies unexpectedly.
#
#  FOR PRODUCTION SYSTEMS, ACTIONS SHOULD ALWAYS EXIT.
#  AN INTERACTIVE ACTION MEANS THE SERVER IS NOT RESPONDING TO REQUESTS.
#  AN INTERACTICE ACTION MEANS THE SERVER WILL NOT RESTART.
#
#  THE SERVER MUST NOT BE ALLOWED EXECUTE UNTRUSTED PANIC ACTION CODE
#  PATTACH CAN BE USED AS AN ATTACK VECTOR.
#
#  The panic action is a command which will be executed if the server
#  receives a fatal, non user generated signal, i.e. SIGSEGV, SIGBUS,
#  SIGABRT or SIGFPE.
#
#  This can be used to start an interactive debugging session so
#  that information regarding the current state of the server can
#  be acquired.
#
#  The following string substitutions are available:
#  - %e   The currently executing program e.g. /sbin/radiusd
#  - %p   The PID of the currently executing program e.g. 12345
#
#  Standard ${} substitutions are also allowed.
#
#  An example panic action for opening an interactive session in GDB would be:
#
#panic_action = "gdb %e %p"
#
#  Again, don't use that on a production system.
#
#  An example panic action for opening an automated session in GDB would be:
#
#panic_action = "gdb -silent -x ${raddbdir}/panic.gdb %e %p 2>&1 | tee ${logdir}/gdb-${name}-%p.log"
#
#  That command can be used on a production system.
#
#  max_request_time: The maximum time (in seconds) to handle a request.
#
#  Requests which take more time than this to process may be killed, and
#  a REJECT message is returned.
#
#  WARNING: If you notice that requests take a long time to be handled,
#  then this MAY INDICATE a bug in the server, in one of the modules
#  used to handle a request, OR in your local configuration.
#
#  This problem is most often seen when using an SQL database.  If it takes
#  more than a second or two to receive an answer from the SQL database,
#  then it probably means that you haven't indexed the database.  See your
#  SQL server documentation for more information.
#
#  Useful range of values: 5 to 120
#
max_request_time = 30
#  cleanup_delay: The time to wait (in seconds) before cleaning up
#  a reply which was sent to the NAS.
#
#  The RADIUS request is normally cached internally for a short period
#  of time, after the reply is sent to the NAS.  The reply packet may be
#  lost in the network, and the NAS will not see it.  The NAS will then
#  re-send the request, and the server will respond quickly with the
#  cached reply.
#
#  If this value is set too low, then duplicate requests from the NAS
#  MAY NOT be detected, and will instead be handled as separate requests.
#
#  If this value is set too high, then the server will cache too many
#  requests, and some new requests may get blocked.  (See 'max_requests'.)
#
#  Useful range of values: 2 to 10
#
cleanup_delay = 5
#  max_requests: The maximum number of requests which the server keeps
#  track of.  This should be 256 multiplied by the number of clients.
#  e.g. With 4 clients, this number should be 1024.
#
#  If this number is too low, then when the server becomes busy,
#  it will not respond to any new requests, until the 'cleanup_delay'
#  time has passed, and it has removed the old requests.
#
#  If this number is set too high, then the server will use a bit more
#  memory for no real benefit.
#
#  If you aren't sure what it should be set to, it's better to set it
#  too high than too low.  Setting it to 1000 per client is probably
#  the highest it should be.
#
#  Useful range of values: 256 to infinity
#
max_requests = 16384
#  hostname_lookups: Log the names of clients or just their IP addresses
#  e.g., www.freeradius.org (on) or 206.47.27.232 (off).
#
#  The default is 'off' because it would be overall better for the net
#  if people had to knowingly turn this feature on, since enabling it
#  means that each client request will result in AT LEAST one lookup
#  request to the nameserver.   Enabling hostname_lookups will also
#  mean that your server may stop randomly for 30 seconds from time
#  to time, if the DNS requests take too long.
#
#  Turning hostname lookups off also means that the server won't block
#  for 30 seconds, if it sees an IP address which has no name associated
#  with it.
#
#  allowed values: {no, yes}
#
hostname_lookups = no
#
#  Logging section.  The various "log_*" configuration items
#  will eventually be moved here.
#
log {
	#
	#  Destination for log messages.  This can be one of:
	#
	#	files - log to "file", as defined below.
	#	syslog - to syslog (see also the "syslog_facility", below.
	#	stdout - standard output
	#	stderr - standard error.
	#
	#  The command-line option "-X" over-rides this option, and forces
	#  logging to go to stdout.
	#
	#destination = files
	destination = stdout
	#
	#  Highlight important messages sent to stderr and stdout.
	#
	#  Option will be ignored (disabled) if output if TERM is not
	#  an xterm or output is not to a TTY.
	#
	colourise = yes
	#
	#  The logging messages for the server are appended to the
	#  tail of this file if destination == "files"
	#
	#  If the server is running in debugging mode, this file is
	#  NOT used.
	#
	file = ${logdir}/radius.log
	#
	#  Which syslog facility to use, if ${destination} == "syslog"
	#
	#  The exact values permitted here are OS-dependent.  You probably
	#  don't want to change this.
	#
	syslog_facility = daemon
	#  Log the full User-Name attribute, as it was found in the request.
	#
	# allowed values: {no, yes}
	#
	stripped_names = no
	#  Log authentication requests to the log file.
	#
	#  allowed values: {no, yes}
	#
	#auth = yes
        auth = $ENV{RAD_DEBUG}
	#  Log passwords with the authentication requests.
	#  auth_badpass  - logs password if it's rejected
	#  auth_goodpass - logs password if it's correct
	#
	#  allowed values: {no, yes}
	#
	#auth_badpass = yes
	auth_badpass = $ENV{RAD_DEBUG}
	#auth_goodpass = yes
	auth_goodpass = $ENV{RAD_DEBUG}
	#  Log additional text at the end of the "Login OK" messages.
	#  for these to work, the "auth" and "auth_goodpass" or "auth_badpass"
	#  configurations above have to be set to "yes".
	#
	#  The strings below are dynamically expanded, which means that
	#  you can put anything you want in them.  However, note that
	#  this expansion can be slow, and can negatively impact server
	#  performance.
	#
#	msg_goodpass = ""
#	msg_badpass = ""
	#  The message when the user exceeds the Simultaneous-Use limit.
	#
	msg_denied = "You are already logged in - access denied"
}
#  The program to execute to do concurrency checks.
checkrad = ${sbindir}/checkrad
# SECURITY CONFIGURATION
#
#  There may be multiple methods of attacking on the server.  This
#  section holds the configuration items which minimize the impact
#  of those attacks
#
security {
	#  chroot: directory where the server does "chroot".
	#
	#  The chroot is done very early in the process of starting
	#  the server.  After the chroot has been performed it
	#  switches to the "user" listed below (which MUST be
	#  specified).  If "group" is specified, it switches to that
	#  group, too.  Any other groups listed for the specified
	#  "user" in "/etc/group" are also added as part of this
	#  process.
	#
	#  The current working directory (chdir / cd) is left
	#  *outside* of the chroot until all of the modules have been
	#  initialized.  This allows the "raddb" directory to be left
	#  outside of the chroot.  Once the modules have been
	#  initialized, it does a "chdir" to ${logdir}.  This means
	#  that it should be impossible to break out of the chroot.
	#
	#  If you are worried about security issues related to this
	#  use of chdir, then simply ensure that the "raddb" directory
	#  is inside of the chroot, end be sure to do "cd raddb"
	#  BEFORE starting the server.
	#
	#  If the server is statically linked, then the only files
	#  that have to exist in the chroot are ${run_dir} and
	#  ${logdir}.  If you do the "cd raddb" as discussed above,
	#  then the "raddb" directory has to be inside of the chroot
	#  directory, too.
	#
#	chroot = /path/to/chroot/directory
	# user/group: The name (or #number) of the user/group to run radiusd as.
	#
	#   If these are commented out, the server will run as the
	#   user/group that started it.  In order to change to a
	#   different user/group, you MUST be root ( or have root
	#   privileges ) to start the server.
	#
	#   We STRONGLY recommend that you run the server with as few
	#   permissions as possible.  That is, if you're not using
	#   shadow passwords, the user and group items below should be
	#   set to radius'.
	#
	#  NOTE that some kernels refuse to setgid(group) when the
	#  value of (unsigned)group is above 60000; don't use group
	#  "nobody" on these systems!
	#
	#  On systems with shadow passwords, you might have to set
	#  'group = shadow' for the server to be able to read the
	#  shadow password file.  If you can authenticate users while
	#  in debug mode, but not in daemon mode, it may be that the
	#  debugging mode server is running as a user that can read
	#  the shadow info, and the user listed below can not.
	#
	#  The server will also try to use "initgroups" to read
	#  /etc/groups.  It will join all groups where "user" is a
	#  member.  This can allow for some finer-grained access
	#  controls.
	#
	user = radius
	group = radius
	#  Core dumps are a bad thing.  This should only be set to
	#  'yes' if you're debugging a problem with the server.
	#
	#  allowed values: {no, yes}
	#
	allow_core_dumps = no
	#
	#  max_attributes: The maximum number of attributes
	#  permitted in a RADIUS packet.  Packets which have MORE
	#  than this number of attributes in them will be dropped.
	#
	#  If this number is set too low, then no RADIUS packets
	#  will be accepted.
	#
	#  If this number is set too high, then an attacker may be
	#  able to send a small number of packets which will cause
	#  the server to use all available memory on the machine.
	#
	#  Setting this number to 0 means "allow any number of attributes"
	max_attributes = 200
	#
	#  reject_delay: When sending an Access-Reject, it can be
	#  delayed for a few seconds.  This may help slow down a DoS
	#  attack.  It also helps to slow down people trying to brute-force
	#  crack a users password.
	#
	#  Setting this number to 0 means "send rejects immediately"
	#
	#  If this number is set higher than 'cleanup_delay', then the
	#  rejects will be sent at 'cleanup_delay' time, when the request
	#  is deleted from the internal cache of requests.
	#
	#  As of Version 3.0.5, "reject_delay" has sub-second resolution.
	#  e.g. "reject_delay =  1.4" seconds is possible.
	#
	#  Useful ranges: 1 to 5
	reject_delay = 1
	#
	#  status_server: Whether or not the server will respond
	#  to Status-Server requests.
	#
	#  When sent a Status-Server message, the server responds with
	#  an Access-Accept or Accounting-Response packet.
	#
	#  This is mainly useful for administrators who want to "ping"
	#  the server, without adding test users, or creating fake
	#  accounting packets.
	#
	#  It's also useful when a NAS marks a RADIUS server "dead".
	#  The NAS can periodically "ping" the server with a Status-Server
	#  packet.  If the server responds, it must be alive, and the
	#  NAS can start using it for real requests.
	#
	#  See also raddb/sites-available/status
	#
	status_server = yes
	#
	#  allow_vulnerable_openssl: Allow the server to start with
	#  versions of OpenSSL known to have critical vulnerabilities.
	#
	#  This check is based on the version number reported by libssl
	#  and may not reflect patches applied to libssl by
	#  distribution maintainers.
	# Alpine 3.9 switched to openssl v1.1.1a-r1
	# CVE-2016-6309 was patch in openssl v1.1.0b
	allow_vulnerable_openssl = 'CVE-2016-6309'
}
# PROXY CONFIGURATION
#
#  proxy_requests: Turns proxying of RADIUS requests on or off.
#
#  The server has proxying turned on by default.  If your system is NOT
#  set up to proxy requests to another server, then you can turn proxying
#  off here.  This will save a small amount of resources on the server.
#
#  If you have proxying turned off, and your configuration files say
#  to proxy a request, then an error message will be logged.
#
#  To disable proxying, change the "yes" to "no", and comment the
#  $INCLUDE line.
#
#  allowed values: {no, yes}
#
#proxy_requests  = yes
proxy_requests  = no
#$INCLUDE proxy.conf
# CLIENTS CONFIGURATION
#
#  Client configuration is defined in "clients.conf".
#
#  The 'clients.conf' file contains all of the information from the old
#  'clients' and 'naslist' configuration files.  We recommend that you
#  do NOT use 'client's or 'naslist', although they are still
#  supported.
#
#  Anything listed in 'clients.conf' will take precedence over the
#  information from the old-style configuration files.
#
$INCLUDE clients.conf
# THREAD POOL CONFIGURATION
#
#  The thread pool is a long-lived group of threads which
#  take turns (round-robin) handling any incoming requests.
#
#  You probably want to have a few spare threads around,
#  so that high-load situations can be handled immediately.  If you
#  don't have any spare threads, then the request handling will
#  be delayed while a new thread is created, and added to the pool.
#
#  You probably don't want too many spare threads around,
#  otherwise they'll be sitting there taking up resources, and
#  not doing anything productive.
#
#  The numbers given below should be adequate for most situations.
#
thread pool {
	#  Number of servers to start initially --- should be a reasonable
	#  ballpark figure.
	start_servers = 5
	#  Limit on the total number of servers running.
	#
	#  If this limit is ever reached, clients will be LOCKED OUT, so it
	#  should NOT BE SET TOO LOW.  It is intended mainly as a brake to
	#  keep a runaway server from taking the system with it as it spirals
	#  down...
	#
	#  You may find that the server is regularly reaching the
	#  'max_servers' number of threads, and that increasing
	#  'max_servers' doesn't seem to make much difference.
	#
	#  If this is the case, then the problem is MOST LIKELY that
	#  your back-end databases are taking too long to respond, and
	#  are preventing the server from responding in a timely manner.
	#
	#  The solution is NOT do keep increasing the 'max_servers'
	#  value, but instead to fix the underlying cause of the
	#  problem: slow database, or 'hostname_lookups=yes'.
	#
	#  For more information, see 'max_request_time', above.
	#
	max_servers = 32
	#  Server-pool size regulation.  Rather than making you guess
	#  how many servers you need, FreeRADIUS dynamically adapts to
	#  the load it sees, that is, it tries to maintain enough
	#  servers to handle the current load, plus a few spare
	#  servers to handle transient load spikes.
	#
	#  It does this by periodically checking how many servers are
	#  waiting for a request.  If there are fewer than
	#  min_spare_servers, it creates a new spare.  If there are
	#  more than max_spare_servers, some of the spares die off.
	#  The default values are probably OK for most sites.
	#
	min_spare_servers = 3
	max_spare_servers = 10
	#  When the server receives a packet, it places it onto an
	#  internal queue, where the worker threads (configured above)
	#  pick it up for processing.  The maximum size of that queue
	#  is given here.
	#
	#  When the queue is full, any new packets will be silently
	#  discarded.
	#
	#  The most common cause of the queue being full is that the
	#  server is dependent on a slow database, and it has received
	#  a large "spike" of traffic.  When that happens, there is
	#  very little you can do other than make sure the server
	#  receives less traffic, or make sure that the database can
	#  handle the load.
	#
#	max_queue_size = 65536
	#  Clean up old threads periodically.  For no reason other than
	#  it might be useful.
	#
	#  '0' is a special value meaning 'infinity', or 'the servers never
	#  exit'
	max_requests_per_server = 0
	#  Automatically limit the number of accounting requests.
	#  This configuration item tracks how many requests per second
	#  the server can handle.  It does this by tracking the
	#  packets/s received by the server for processing, and
	#  comparing that to the packets/s handled by the child
	#  threads.
	#
	#  If the received PPS is larger than the processed PPS, *and*
	#  the queue is more than half full, then new accounting
	#  requests are probabilistically discarded.  This lowers the
	#  number of packets that the server needs to process.  Over
	#  time, the server will "catch up" with the traffic.
	#
	#  Throwing away accounting packets is usually safe and low
	#  impact.  The NAS will retransmit them in a few seconds, or
	#  even a few minutes.  Vendors should read RFC 5080 Section 2.2.1
	#  to see how accounting packets should be retransmitted.  Using
	#  any other method is likely to cause network meltdowns.
	#
	auto_limit_acct = no
}
######################################################################
#
#  SNMP notifications.  Uncomment the following line to enable
#  snmptraps.  Note that you MUST also configure the full path
#  to the "snmptrap" command in the "trigger.conf" file.
#
#$INCLUDE trigger.conf
# MODULE CONFIGURATION
#
#  The names and configuration of each module is located in this section.
#
#  After the modules are defined here, they may be referred to by name,
#  in other sections of this configuration file.
#
modules {
	#
	#  Each module has a configuration as follows:
	#
	#	name [ instance ] {
	#		config_item = value
	#		...
	#	}
	#
	#  The 'name' is used to load the 'rlm_name' library
	#  which implements the functionality of the module.
	#
	#  The 'instance' is optional.  To have two different instances
	#  of a module, it first must be referred to by 'name'.
	#  The different copies of the module are then created by
	#  inventing two 'instance' names, e.g. 'instance1' and 'instance2'
	#
	#  The instance names can then be used in later configuration
	#  INSTEAD of the original 'name'.  See the 'radutmp' configuration
	#  for an example.
	#
	#
	#  As of 3.0, modules are in mods-enabled/.  Files matching
	#  the regex /[a-zA-Z0-9_.]+/ are loaded.  The modules are
	#  initialized ONLY if they are referenced in a processing
	#  section, such as authorize, authenticate, accounting,
	#  pre/post-proxy, etc.
	#
	$INCLUDE mods-enabled/
}
# Instantiation
#
#  This section orders the loading of the modules.  Modules
#  listed here will get loaded BEFORE the later sections like
#  authorize, authenticate, etc. get examined.
#
#  This section is not strictly needed.  When a section like
#  authorize refers to a module, it's automatically loaded and
#  initialized.  However, some modules may not be listed in any
#  of the following sections, so they can be listed here.
#
#  Also, listing modules here ensures that you have control over
#  the order in which they are initialized.  If one module needs
#  something defined by another module, you can list them in order
#  here, and ensure that the configuration will be OK.
#
#  After the modules listed here have been loaded, all of the modules
#  in the "mods-enabled" directory will be loaded.  Loading the
#  "mods-enabled" directory means that unlike Version 2, you usually
#  don't need to list modules here.
#
instantiate {
	#
	# We list the counter module here so that it registers
	# the check_name attribute before any module which sets
	# it
#	daily
	# subsections here can be thought of as "virtual" modules.
	#
	# e.g. If you have two redundant SQL servers, and you want to
	# use them in the authorize and accounting sections, you could
	# place a "redundant" block in each section, containing the
	# exact same text.  Or, you could uncomment the following
	# lines, and list "redundant_sql" in the authorize and
	# accounting sections.
	#
	#  The "virtual" module defined here can also be used with
	#  dynamic expansions, under a few conditions:
	#
	#  * The section is "redundant", or "load-balance", or
	#    "redundant-load-balance"
	#  * The section contains modules ONLY, and no sub-sections
	#  * all modules in the section are using the same rlm_
	#    driver, e.g. They are all sql, or all ldap, etc.
	#
	#  When those conditions are satisfied, the server will
	#  automatically register a dynamic expansion, using the
	#  name of the "virtual" module.  In the example below,
	#  it will be "redundant_sql".  You can then use this expansion
	#  just like any other:
	#
	#	update reply {
	#		Filter-Id := "%{redundant_sql: ... }"
	#	}
	#
	#  In this example, the expansion is done via module "sql1",
	#  and if that expansion fails, using module "sql2".
	#
	#  For best results, configure the "pool" subsection of the
	#  module so that "retry_delay" is non-zero.  That will allow
	#  the redundant block to quickly ignore all "down" SQL
	#  databases.  If instead we have "retry_delay = 0", then
	#  every time the redundant block is used, the server will try
	#  to open a connection to every "down" database, causing
	#  problems.
	#
	#redundant redundant_sql {
	#	sql1
	#	sql2
	#}
}
######################################################################
#
#  Policies are virtual modules, similar to those defined in the
#  "instantiate" section above.
#
#  Defining a policy in one of the policy.d files means that it can be
#  referenced in multiple places as a *name*, rather than as a series of
#  conditions to match, and actions to take.
#
#  Policies are something like subroutines in a normal language, but
#  they cannot be called recursively. They MUST be defined in order.
#  If policy A calls policy B, then B MUST be defined before A.
#
######################################################################
policy {
	$INCLUDE policy.d/
}
######################################################################
#
#	Load virtual servers.
#
#	This next $INCLUDE line loads files in the directory that
#	match the regular expression: /[a-zA-Z0-9_.]+/
#
#	It allows you to define new virtual servers simply by placing
#	a file into the raddb/sites-enabled/ directory.
#
$INCLUDE sites-enabled/
######################################################################
#
#	All of the other configuration sections like "authorize {}",
#	"authenticate {}", "accounting {}", have been moved to the
#	the file:
#
#		raddb/sites-available/default
#
#	This is the "default" virtual server that has the same
#	configuration as in version 1.0.x and 1.1.x.  The default
#	installation enables this virtual server.  You should
#	edit it to create policies for your local site.
#
#	For more documentation on virtual servers, see:
#
#		raddb/sites-available/README
#
######################################################################
================================================

File: README.rst
================================================
Upgrading to Version 3.0
========================
.. contents:: Sections
   :depth: 2
.. important:: 
   The configuration for 3.0 is *largely* compatible with the 2.x.x
   configuration.  However, it is NOT possible to simply use the 2.x.x
   configuration as-is.  Instead, you should re-create it.
Security
--------
A number of configuration items have moved into the "security"
subsection of radiusd.conf.  If you use these, you should move them.
Otherwise, they can be ignored.
The list of moved options is::
  chroot
  user
  group
  allow_core_dumps
  reject_delay
  status_server
These entries should be moved from "radiusd.conf" to the "security"
subsection of that file.
Naming
------
Many names used by configuration items were inconsistent in earlier
versions of the server.  These names have been unified in version 3.0.
If a file is being referenced or created the config item ``filename``
is used.
If a file is being created, the initial permissions are set by the
``permissions`` config item.
If a directory hierarchy needs to be created, the permissions are set
by ``dir_permissions``.
If an external host is referenced in the context of a module the
``server`` config item is used.
Unless the config item is a well recognised portmanteau
(as ``filename`` is for example), it must be written as multiple
distinct words separated by underscores ``_``.
The configuration items ``file``, ``script_file``, ``module``,
``detail``, ``detailfile``, ``attrsfile``, ``perm``, ``dirperm``,
``detailperm``, and ``hostname`` are deprecated. As well as any false
portmanteaus, and configuration items that used hyphens as word
delimiters.  e.g. ``foo-bar`` has been changed to ``foo_bar``.  Please
update your module configuration to use the new syntax.
In most cases the server will tell you the replacement config item to
use.  As always, run the server in debugging mode to see these
messages.
Modules Directory
-----------------
As of version 3.0, the ``modules/`` directory no longer exists.
Instead, all "example" modules have been put into the
``mods-available/`` directory.  Modules which can be loaded by the
server are placed in the ``mods-enabled/`` directory.  All of the
modules in that directory will be loaded.  This means that the
``instantiate`` section of radiusd.conf is less important.  The only
reason to list a module in the ``instantiate`` section is to force
ordering when the modules are loaded.
Modules can be enabled by creating a soft link.  For module ``foo``, do::
  $ cd raddb/mods-enabled
  $ ln -s ../mods-available/foo
To create "local" versions of the modules, we suggest copying the file
instead.  This leaves the original file (with documentation) in the
``mods-available/`` directory.  Local changes should go into the
``mods-enabled/`` directory.
Module-specific configuration files are now in the ``mods-config/``
directory.  This change allows for better organization, and means that
there are fewer files in the main ``raddb`` directory.  See
``mods-config/README.rst`` for more details.
Changed Modules
---------------
The following modules have been changed.
rlm_sql
~~~~~~~
The SQL configuration has been moved from ``sql.conf`` to
``mods-available/sql``.  The ``sqlippool.conf`` file has also been
moved to ``mods-available/sqlippool``.
The SQL module configuration has been changed.  The old connection
pool options are no longer accepted::
  num_sql_socks
  connect_failure_retry_delay
  lifetime
  max_queries
Instead, a connection pool configuration is used.  This configuration
contains all of the functionality of the previous configuration, but
in a more generic form.  It also is used in multiple modules, meaning
that there are fewer different configuration items.  The mapping
between the configuration items is::
  num_sql_socks			-> pool { max }
  connect_failure_retry_delay	-> pool { retry_delay }
  lifetime			-> pool { lifetime }
  max_queries			-> pool { uses }
The pool configuration adds a number of new configuration options,
which allow the administrator to better control how FreeRADIUS uses
SQL connection pools.
The following parameters have been changed::
  trace				-> removed
  tracefile			-> logfile
The logfile is intended to log SQL queries performed.  If you need to
debug the server, use debugging mode.  If ``logfile`` is set, then
*all* SQL queries will go to ``logfile``.
You can now use a NULL SQL database::
  driver = rlm_sql_null
This is an empty driver which will always return "success".  It is
intended to be used to replace the ``sql_log`` module, and to work in
conjunction with the ``radsqlrelay`` program.  Simply take your normal
configuration for raddb/mods-enabled/sql, and set::
  driver = rlm_sql_null
  ...
  logfile = ${radacctdir}/sql.log
All of the SQL queries will be logged to that file.  The connection
pool does not need to be configured for the ``null`` SQL driver.  It
can be left as-is, or deleted from the SQL configuration file.
rlm_sql_sybase
~~~~~~~~~~~~~~
The ``rlm_sql_sybase`` module has been renamed to ``rlm_sql_freetds``
and the old ``rlm_sql_freetds`` module has been removed.
``rlm_sql_sybase`` used the newer ct-lib API, and ``rlm_sql_freetds``
used an older API and was incomplete.
The new ``rlm_sql_freetds`` module now also supports database
selection on connection startup so ``use`` statements no longer
have to be included in queries.
sql/dialup.conf
~~~~~~~~~~~~~~~
Queries for post-auth and accounting calls have been re-arranged.  The
SQL module will now expand the 'reference' configuration item in the
appropriate sub-section, and resolve this to a configuration
item. This behaviour is similar to rlm_linelog.  This dynamic
expansion allows for a dynamic mapping between accounting types and
SQL queries.  Previously, the mapping was fixed.  Any "new" accounting
type was ignored by the module.  Now, support for any accounting type
can be added by just adding a new target, as below.
Queries from v2.x.x may be manually copied to the new v3.0
``dialup.conf`` file (``raddb/sql/main/<dialect>/queries.conf``).
When doing this you may also need to update references to the
accounting tables, as their definitions will now be outside of
the subsection containing the query.
The mapping from old "fixed" query to new "dynamic" query is as follows::
  accounting_onoff_query		-> accounting.type.accounting-on.query
  accounting_update_query		-> accounting.type.interim-update.query
  accounting_update_query_alt		+> accounting.type.interim-update.query
  accounting_start_query		-> accounting.type.start.query
  accounting_start_query_alt		+> accounting.type.start.query
  accounting_stop_query			-> accounting.type.stop.query
  accounting_stop_query_alt		+> accounting.type.stop.query
  postauth_query			-> post-auth.query
Alternatively a 2.x.x config may be patched to work with the
3.0 module by adding the following::
  accounting {
	reference = "%{tolower:type.%{Acct-Status-Type}.query}"
	type {
		accounting-on {
			query = "${....accounting_onoff_query}"
		}
		accounting-off {
			query = "${....accounting_onoff_query}"
		}
		start {
			query = "${....accounting_start_query}"
			query = "${....accounting_start_query_alt}"
		}
		interim-update {
			query = "${....accounting_update_query}"
			query = "${....accounting_update_query_alt}"
		}
		stop {
			query = "${....accounting_stop_query}"
			query = "${....accounting_stop_query_alt}"
		}
	}
  }
  post-auth {
	query = "${..postauth_query}"
  }
In general, it is safer to migrate the configuration rather than
trying to "patch" it, to make it look like a v2 configuration.
Note that the sub-sections holding the queries are labelled
``accounting-on``, and not ``accounting_on``.  The reason is that the
names of these sections are taken directly from the
``Accounting-Request`` packet, and the ``Acct-Status-Type`` field.
The ``sql`` module looks at the value of that field, and then looks
for a section of that name, in order to find the query to use.
That process means that the server can be extended to support any new
value of ``Acct-Status-Type``, simply by adding a named sub-section,
and a query.  This behavior is preferable to that of v2, which had
hard-coded queries for certain ``Acct-Status-Type`` values, and was
ignored all other values.
rlm_ldap
~~~~~~~~
The LDAP module configuration has been substantially changed.  Please
read ``raddb/mods-available/ldap``.  It now uses a connection pool,
just like the SQL module.
Many of the configuration items remain the same, but they have been
moved into subsections.  This change is largely cosmetic, but it makes
the configuration clearer.  Instead of having a large set of random
configuration items, they are now organized into logical groups.
You will need to read your old LDAP configuration, and migrate it
manually to the new configuration.  Simply copying the old
configuration WILL NOT WORK.
Users upgrading from 2.x.x who used to call the ldap module in
``post-auth`` should now set ``edir_autz = yes``, and remove the ``ldap``
module from the ``post-auth`` section.
rlm_ldap and LDAP-Group
~~~~~~~~~~~~~~~~~~~~~~~
In 2.x.x the registration of the ``LDAP-Group`` pair comparison was done
by the last instance of rlm_ldap to be instantiated. In 3.0 this has
changed so that only the default ``ldap {}`` instance registers
``LDAP-Group``.
If ``<instance>-LDAP-Group`` is already used throughout your configuration
no changes will be needed.
rlm_ldap authentication
~~~~~~~~~~~~~~~~~~~~~~~
In 2.x.x the LDAP module had a ``set_auth_type`` configuration item,
which forced ``Auth-Type := ldap``. This was removed in 3.x.x as it
often did not work, and was not consistent with the rest of the
server.  We generally recommend that LDAP should be used as a
database, and that FreeRADIUS should do authentication.
The only reason to use ``Auth-Type := ldap`` is when the LDAP server
will not supply the "known good" password to FreeRADIUS, *and* where
the Access-Request contains User-Password.  This situation happens
only for Active Directory.  If you think you need to force ``Auth-Type
:= ldap`` in other situations, you are very likely to be wrong.
The following is an example of what should be inserted into the
``authorize {}`` and ``authenticate {}`` sections of the relevant
virtual-servers, to get functionality equivalent to v2.x::
  authorize {
    ...
    ldap
    if ((ok || updated) && User-Password) {
      update control {
	Auth-Type := ldap
      }
    }
    ...
  }
  authenticate {
    ...
    Auth-Type ldap {
      ldap   
    }
    ...
  }
rlm_eap
~~~~~~~
The EAP configuration has been moved from ``eap.conf`` to
``mods-available/eap``.  A new ``pwd`` subsection has been added for
EAP-PWD.
rlm_expiration & rlm_logintime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The rlm_expiration and rlm_logintime modules no longer add a ``Reply-Message``,
the same behaviour can be achieved checking the return code of the module and
adding the ``Reply-Message`` with unlang::
  expiration
  if (userlock) {
    update reply {
      Reply-Message := "Your account has expired"
    }
  }
rlm_unix
~~~~~~~~
The ``unix`` module does not have an ``authenticate`` section.  So you
cannot set ``Auth-Type := System``.  The ``unix`` module has also been
deleted from the examples in ``sites-available/``.  Listing it there
has been deprecated for many years.
The PAP module can do crypt authentication.  It should be used instead
of Unix authentication.
The Unix module still can pull the passwords from ``/etc/passwd``, or
``/etc/shadow``.  This is done by listing it in the ``authorize``
section, as is done in the examples in ``sites-available/``.  However,
some systems using NIS or NSS will not supply passwords to the
``unix`` module.  For those systems, we recommend putting users and
passwords into a database, instead of relying on ``/etc/passwd``.
rlm_preprocess
~~~~~~~~~~~~~~
In 2.x.x ``huntroups`` and ``users`` files were loaded from default locations
without being configured explicitly. Since 3.x.x you need to set
``huntgroups`` and ``users`` configuration item(s) in module section in order
to get them being processed.
New Modules
-----------
rlm_date
~~~~~~~~
Instances of rlm_date register an xlat method which can translate
integer and date values to an arbitrarily formatted date time
string, or an arbitrarily formated time string to an integer, 
depending on the attribute type passed.
rlm_rest
~~~~~~~~
The ``rest`` module is used to translate RADIUS requests into 
RESTfull HTTP requests. Currently supported body types are JSON
and POST.
rlm_unpack
~~~~~~~~~~
The ``unpack`` module is used to turn data buried inside of binary
attributes.  e.g. if we have ``Class = 0x00000001020304`` then::
  Tmp-Integer-0 := "%{unpack:&Class 4 short}"
will unpack octets 4 and 5 as a "short", which has value 0x0304.
All integers are assumed to be in network byte order.
rlm_yubikey
~~~~~~~~~~~
The ``yubikey`` module can be used to forward yubikey OTP token
values to a Yubico validation server, or decrypt the token 
using a PSK.
Deleted Modules
---------------
The following modules have been deleted, and are no longer supported
in Version 3.  If you are using one of these modules, your
configuration can probably be changed to not need it.  Otherwise email
the freeradius-devel list, and ask about the module.
rlm_acct_unique
~~~~~~~~~~~~~~~
This module has been replaced by the "acct_unique" policy.  See
raddb/policy.d/accounting.
The method for calculating the value of acct_unique has changed.
However, as this method was configurable, this change should not
matter.  The only issue is in having a v2 and v3 server writing to the
same database at the same time.  They will calculate different values
for Acct-Unique-Id.
rlm_acctlog
~~~~~~~~~~~
You should use rlm_linelog instead.  That module has a superset of the
acctlog functionality.
rlm_attr_rewrite
~~~~~~~~~~~~~~~~
The attr_rewrite module looked for an attribute, and then re-wrote it,
or created a new attribute.  All of that can be done in "unlang".
A sample configuration in "unlang" is::
  if (request:Calling-Station-Id) {
    update request {
      Calling-Station-Id := "...."
    }
  }
We suggest updating all uses of attr_rewrite to use unlang instead.
rlm_checkval
~~~~~~~~~~~~
The checkval module compared two attributes.  All of that can be done in "unlang"::
  if (&request:Calling-Station-Id == &control:Calling-Station-Id) {
    ok
  }
We suggest updating all uses of checkval to use unlang instead.
rlm_dbm
~~~~~~~
No one seems to use it.  There is no sample configuration for it.
There is no speed advantage to using it over the "files" module.
Modern systems are fast enough that 10K entries can be read from the
"users" file in about 10ms.  If you need more users than that, use a
real database such as SQL.
rlm_fastusers
~~~~~~~~~~~~~
No one seems to use it.  It has been deprecated since Version 2.0.0.
The "files" module was rewritten so that the "fastusers" module was no
longer necessary.
rlm_policy
~~~~~~~~~~
No one seems to use it.  Almost all of its functionality is available
via "unlang".
rlm_sim_files
~~~~~~~~~~~~~
The rlm_sim_files module has been deleted.  It was never marked "stable",
and was never used in a production environment.  There are better ways
to test EAP.
If you want similar functionality, see rlm_passwd.  It can read CSV
files, and create attributes from them.
rlm_sql_log
~~~~~~~~~~~
This has been replaced with the "null" sql driver.  See
raddb/mods-available/sql for an example configuration.
The main SQL module has more functionality than rlm_sql_log, and
results in less code in the server.
Other Functionality
-------------------
The following is a list of new / changed functionality.
RadSec
~~~~~~
RadSec (or RADIUS over TLS) is now supported.  RADIUS over bare TCP
is also supported, but is recommended only for secure networks.
See ``sites-available/tls`` for complete details on using TLS.  The server
can both receive incoming TLS connections, and also originate outgoing
TLS connections.
The TLS configuration is taken from the old EAP-TLS configuration.  It
is largely identical to the old EAP-TLS configuration, so it should be
simple to use and configure.  It re-uses much of the EAP-TLS code,
so it is well-tested and reliable.
Once RadSec is enabled, normal debugging mode will not work.  This is
because the TLS code requires threading to work properly.  Instead of doing::
  $ radiusd -X
you will need to do::
  $ radiusd -fxx -l stdout
That's the price to pay for using RadSec.  This limitation may be
lifted in a future version of the server.
PAP and User-Password
~~~~~~~~~~~~~~~~~~~~~
From version 3.0 onwards the server no longer supports authenticating
against a cleartext password in the 'User-Password' attribute. Any
occurences of this (for instance, in the users file) should now be changed
to 'Cleartext-Password' instead.
e.g. change entries like this::
  bob User-Password == "hello"
to ones like this::
  bob Cleartext-Password := "hello"
If this is not done, authentication will likely fail.  The server will
also print a helpful message in debugging mode.
If it really is impossible to do this, the following unlang inserted above
the call to the pap module may be used to copy User-Password to the correct
attribute::
  if (!control:Cleartext-Password && control:User-Password) {
    update control {
      Cleartext-Password := "%{control:User-Password}"
    }
  }
However, this should only be seen as a temporary, not permanent, fix.
It is better to fix your databases to use the correct configuration.
Unlang
~~~~~~
The unlang policy language is compatible with v2, but has a number of
new features.  See ``man unlang`` for complete documentation.
ERRORS
Many more errors are caught when the server is starting up.  Syntax
errors in ``unlang`` are caught, and a helpful error message is
printed.  The error message points to the exact place where the error
occurred::
  ./raddb/sites-enabled/default[230]: Parse error in condition
  ERROR:  if (User-Name ! "bob") {
  ERROR:                ^ Invalid operator
``update`` sections are more generic.  Instead of doing ``update
reply``, you can do the following::
  update {
	  reply:Class := 0x0000
	  control:Cleartext-Password := "hello"
  }
This change means that you need fewer ``update`` sections.
COMPARISONS
Attribute comparisons can be done via the ``&`` operator.  When you
needed to compare two attributes, the old comparison style was::
  if (User-Name == "%{control:Tmp-String-0}") {
This syntax is inefficient, as the ``Tmp-String-0`` attribute would be
printed to an intermediate string, causing unnecessary work.  You can
now instead compare the two attributes directly::
  if (&User-Name == &control:Tmp-String-0) {
See ``man unlang`` for more details.
CASTS
Casts are now permitted.  This allows you to force type-specific
comparisons::
  if (<ipaddr>"%{sql: SELECT...}" == 127.0.0.1) {
This forces the string returned by the SELECT to be treated as an IP
address, and compare to ``127.0.0.1``.  Previously, the comparison
would have been done as a simple string comparison.
NETWORKS
IP networks are now supported::
  if (127.0.0.1/32 == 127.0.0.1) {
Will be ``true``.  The various comparison operators can be used to
check IP network membership::
  if (127/8 > 127.0.0.1) {
Returns ``true``, because ``127.0.0.1`` is within the ``127/8``
network.  However, the following comparison will return ``false``::
  if (127/8 > 192.168.0.1) {
because ``192.168.0.1`` is outside of the ``127/8`` network.
OPTIMIZATION
As ``unlang`` is now pre-compiled, many compile-time optimizations are
done.  This means that the debug output may not be exactly the same as
what is in the configuration files::
  if (0 && (User-Name == "bob')) {
The result will always be ``false``, as the ``if 0`` prevents the
following ``&& ...`` from being evaluated.
Not only that, but the entire contents of that section will be ignored
entirely::
  if (0) {
      this_module_does_not_exist
      and_this_one_does_not_exist_either
  }
In v2, that configuration would result in a parse error, as there is
no module called ``this_module_does_not_exist``.  In v3, that text is
ignored.  This ability allows you to have dynamic configurations where
certain parts are used (or not) depending on compile-time configuration.
Similarly, conditions which always evaluate to ``true`` will be
optimized away::
  if (1) {
      files
  }
That configuration will never show the ``if (1)`` output in debugging mode.
Dialup_admin
------------
The dialup_admin directory has been removed.  No one stepped forward
to maintain it, and the code had not been changed in many years.
================================================

File: README
================================================
1.  Virtual Servers.
  FreeRADIUS 2.0 supports virtual servers.  This is probably the
single largest change that is NOT backwards compatible with 1.x.
  The virtual servers do NOT have to be set up with the
"sites-available" and "sites-enabled" directories.  You can still have
one "radiusd.conf" file, and put the server configuration there:
	...
	server {
		authorize {
			...
		}
		authenticate {
			...
		}
		...
	}
	...
  The power of virtual servers lies in their ability to separate
policies.  A policy can be placed into a virtual server, where it is
guaranteed to affect only the requests that are passed through that
virtual server.  In 1.x, the policies were global, and it sometimes
took much effort to write a policy so that it only applied in certain
limited situations.
2.  What do we mean by "virtual server"?
  A virtual server is a (nearly complete) RADIUS server, just like a
configuration for FreeRADIUS 1.x.  However, FreeRADIUS can now run
multiple virtual servers at the same time.  The virtual servers can
even proxy requests to each other!
  The simplest way to create a virtual server is to take the all of
the request processing sections from radius.conf, ("authorize" ,
"authenticate", etc.) and wrap them in a "server {}" block, as above.
  You can create another virtual server by:
    1) defining a new "server foo {...}" section in radiusd.conf
    2) Putting the normal "authorize", etc. sections inside of it
    3) Adding a "listen" section *inside* of the "server" section.
  e.g.
	...
	server foo {
		listen {
			ipaddr = 127.0.0.1
			port = 2000
			type = auth
		}
		authorize {
			update control {
				Cleartext-Password := "bob"
			}
			pap
		}
		authenticate {
			pap
		}
	}
	...
  With that text added to "radiusd.conf", run the server in debugging
mode (radiusd -X), and in another terminal window, type:
$ radtest bob bob localhost:2000 0 testing123
  You should see the server return an Access-Accept.
3. Capabilities and limitations
  The only sub-sections that can appear in a virtual server section
are:
	listen
	client
	authorize
	authenticate
	post-auth
	pre-proxy
	post-proxy
	preacct
	accounting
	session
  All other configuration parameters (modules, etc.) are global.
  Inside of a virtual server, the authorize, etc. sections have their
normal meaning, and can contain anything that an authorize section
could contain in 1.x.
  When a "listen" section is inside of a virtual server definition, it
means that all requests sent to that IP/port will be processed through
the virtual server.  There cannot be two "listen" sections with the
same IP address and port number.
  When a "client" section is inside of a virtual server definition, it
means that that client is known only to the "listen" sections that are
also inside of that virtual server.  Not only is this client
definition available only to this virtual server, but the details of
the client configuration is also available only to this virtual
server.
  i.e. Two virtual servers can listen on different IP address and
ports, but both can have a client with IP address 127.0.0.1.  The
shared secret for that client can be different for each virtual
server.
4. More complex "listen" capabilities
  The "listen" sections have a few additional configuration items that
were not in 1.x, and were not mentioned above.  These configuration
items enable almost any mapping of IP / port to clients to virtual
servers.
  The configuration items are:
	virtual_server = <name>
		If set, all requests sent to this IP / port are processed
		through the named virtual server.
		This directive can be used only for "listen" sections
		that are global.  i.e. It CANNOT be used if the
		"listen" section is inside of a virtual server.
	clients = <name>
		If set, the "listen" section looks for a "clients" section:
			clients <name> {
				...
			}
		It looks inside of that named "clients" section for
		"client" subsections, at least one of which must
		exist.  Each client in that section is added to the
		list of known clients for this IP / port.  No other
		clients are known.
		If it is set, it over-rides the list of clients (if
		any) in the same virtual server.  Note that the
		clients are NOT additive!
		If it is not set, then the clients from the current
		virtual server (if any) are used.  If there are no
		clients in this virtual server, then the global
		clients are used.
		i.e. The most specific directive is used:
			* configuration in this "listen" section
			* clients in the same virtual server
			* global clients
		The directives are also *exclusive*, not *additive*.
		If you have one client in a virtual server, and
		another client referenced from a "listen" section,
		then that "listen" section will ONLY use the second
		client.  It will NOT use both clients.
5. More complex "client" capabilities
  The "client" sections have a few additional configuration items that
were not in 1.x, and were not mentioned above.  These configuration
items enable almost any mapping of IP / port to clients to virtual
servers.
  The configuration items are:
	virtual_server = <name>
		If set, all requests from this client are processed
		through the named virtual server.
		This directive can be used only for "client" sections
		that are global.  i.e. It CANNOT be used if the
		"client" section is inside of a virtual server.
  If the "listen" section has a "server" entry, and a matching
client is found ALSO with a "server" entry, then the clients server is
used for that request.
6. Worked examples
  Listening on one socket, and mapping requests from two clients to
two different servers.
	listen {
		...
	}
	client one {
		...
		virtual_server = server_one
	}
	client two {
		...
		virtual_server = server_two
	}
	server server_one {
		authorize {
			...
		}
		...
	}
	server server_two {
		authorize {
			...
		}
		...
	}
  This could also be done as:
	listen {
		...
		virtual_server = server_one
	}
	client one {
		...
	}
	client two {
		...
		virtual_server = server_two
	}
	server server_one {
		authorize {
			...
		}
		...
	}
	server server_two {
		authorize {
			...
		}
		...
	}
  In this case, the default server for the socket is "server_one", so
there is no need to set that in the client "one" configuration.  The
"server_two" configuration for client "two" over-rides the default
setting for the socket.
  Note that the following configuration will NOT work:
	listen {
		...
		virtual_server = server_one
	}
	client one {
		...
	}
	server server_one {
		authorize {
			...
		}
		...
	}
	server server_two {
		client two {
			...
		}
		authorize {
			...
		}
		...
	}
  In this example, client "two" is hidden inside of the virtual
server, where the "listen" section cannot find it.
7. Outlined examples
  This section outlines a number of examples, with alternatives.
  One server, multiple sockets
	- multiple "listen" sections in a "server" section
  one server per client
	- define multiple servers
	- have a global "listen" section
	- have multiple global "clients", each with "virtual_server = X"
  two servers, each with their own sockets
	- define multiple servers
	- put "client" sections into each "server"
	- put a "listen" section into each "server"
	Each server can list the same client IP, and the secret
	can be different
  two sockets, sharing a list of clients, but pointing to different servers
	- define global "listen" sections
	- in each, set "virtual_server = X"
	- in each, set "clients = Y"
	- define "clients Y" section, containing multiple clients.
	This also means that you can have a third socket, which
	doesn't share any of these clients.
8.  How to decide what to do
  If you want *completely* separate policies for a socket or a client,
then create a separate virtual server.  Then, map the request to that
server by setting configuration entries in a "listen" section or in a
"client" section.
  Start off with the common cases first.  If most of the clients
and/or sockets get a particular policy, make that policy the default.
Configure it without paying attention to the sockets or clients you
want to add later, and without adding a second virtual server.  Once
it works, then add the second virtual server.
  If you want to re-use the previously defined sockets with the second
virtual server, then you will need one or more global "client"
sections.  Those clients will contain a "virtual_server = ..." entry
that will direct requests from those clients to the appropriate
virtual server.
================================================

File: templates.conf
================================================
# -*- text -*-
##
## templates.conf -- configurations to be used in multiple places
##
##	$Id: 7b8b44e051c974c1a0a6e27a0cff50e621835df2 $
######################################################################
#
#  Version 2.0 has a useful new feature called "templates".
#
#  Use templates by adding a line in radiusd.conf:
#
#	$INCLUDE templates.conf
#
#  The goal of the templates is to have common configuration located
#  in this file, and to list only the *differences* in the individual
#  sections.  This feature is most useful for sections like "clients"
#  or "home_servers", where many may be defined, and each one has
#  similar repeated configuration.
#
#  Something similar to templates can be done by putting common
#  configuration into separate files, and using "$INCLUDE file...",
#  but this is more flexible, and simpler to understand.  It's also
#  cheaper for the server, because "$INCLUDE" makes a copy of the
#  configuration for inclusion, and templates are simply referenced.
#
#  The templates are defined in the "templates" section, so that they
#  do not affect the rest of the server configuration.
#
#  A section can reference a template by using "$template name"
#
templates {
	#
	#  The contents of the templates section are other
	#  configuration sections that would normally go into
	#  the configuration files.
	#
	#
	#  This is a default template for the "home_server" section.
	#  Note that there is no name for the section.
	#
	#  Any configuration item that is valid for a "home_server"
	#  section is also valid here.  When a "home_server" section
	#  is defined in proxy.conf, this section is referenced as
	#  the template.
	#
	#  Configuration items that are explicitly listed in a
	#  "home_server" section of proxy.conf are used in
	#  preference to the configuration items listed here.
	#
	#  However, if a configuration item is NOT listed in a
	#  "home_server" section of proxy.conf, then the value here
	#  is used.
	#
	#  This functionality lets you put common configuration into
	#  a template, and to put only the unique configuration
	#  items in "proxy.conf".  Each section in proxy.conf can
	#  then contain a line "$template home_server", which will
	#  cause it to reference this template.
	#
	home_server {
		response_window = 20
		zombie_period = 40
		revive_interval = 120
		#
		#  Etc.
	}
	#
	#  You can also have named templates.  For example, if you
	#  are proxying to 3 different home servers all at the same
	#  site, with identical configurations (other than IP
	#  addresses), you can use this named template.
	#
	#  Then, each "home_server" section in "proxy.conf" would
	#  only list the IP address of that home server, and a
	#  line saying
	#
	#		$template example_com
	#
	#  That would tell FreeRADIUS to look in the section below
	#  for the rest of the configuration items.
	#
	#  For various reasons, you shouldn't have a "." in the template
	#  name.  Doing so means that the server will be unable to find
	#  the template.
	#
	example_com {
		type = auth
		port = 1812
		secret = testing123
		response_window = 20
		#
		# Etc...
	}
	#
	#  You can have templates for other sections, too, but they
	#  seem to be most useful for home_servers.
	#
	#  For now, you can use templates only for sections in
	#  radiusd.conf, not sub-sections.  So you still have to use
	#  the "$INCLUDE file.." method for things like defining
	#  multiple "sql" modules, each with similar configuration.
	#
}
================================================

File: trigger.conf
================================================
# -*- text -*-
##
## trigger.conf -- Events in the server can trigger a hook to be executed.
##
##	$Id: 413a182eec6a193ef8ffd284295e181962265395 $
#
#  The triggers are named as "type.subtype.value".  These names refer
#  to subsections and then configuration items in the "trigger"
#  section below.  When an event occurs, the trigger is executed.  The
#  trigger is simply a program that is run, with optional arguments.
#
#  The server does not wait when a trigger is executed.  It is simply
#  a "one-shot" event that is sent.
#
#  The trigger names should be self-explanatory.
#
#
#  SNMP configuration.
#
#  For now, this is only for SNMP traps.
#
#  They are enabled by uncommenting (or adding) "$INCLUDE trigger.conf"
#  in the main "radiusd.conf" file.
#
#  The traps *REQUIRE* that the files in the "mibs" directory be copied
#  to the global mibs directory, usually /usr/share/snmp/mibs/.
#  If this is not done, the "snmptrap" program has no idea what information
#  to send, and will not work.  The MIB installation is *NOT* done as
#  part of the default installation, so that step *MUST* be done manually.
#
#  The global MIB directory can be found by running the following command:
#
#	snmptranslate -Dinit_mib .1.3 2>&1 | grep MIBDIR | sed "s/' .*//;s/.* '//;s/.*://"
#
#  Or maybe just:
#
#	snmptranslate -Dinit_mib .1.3 2>&1 | grep MIBDIR
#
#  If you have copied the MIBs to that directory, you can test the
#  FreeRADIUS MIBs by running the following command:
#
#	snmptranslate -m +FREERADIUS-NOTIFICATION-MIB -IR -On  serverStart
#
#  It should print out:
#
#	.1.3.6.1.4.1.11344.4.1.1
#
#  As always, run the server in debugging mode after enabling the
#  traps.  You will see the "snmptrap" command being run, and it will
#  print out any errors or issues that it encounters.  Those need to
#  be fixed before running the server in daemon mode.
#
#  We also suggest running in debugging mode as the "radiusd" user, if
#  you have "user/group" set in radiusd.conf.  The "snmptrap" program
#  may behave differently when run as "root" or as the "radiusd" user.
#
snmp {
	#
	#  Configuration for SNMP traps / notifications
	#
	#  To disable traps, edit "radiusd.conf", and delete the line
	#  which says "$INCUDE trigger.conf"
	#
	trap {
		#
		#  Absolute path for the "snmptrap" command, and
		#  default command-line arguments.
		#
		#  You can disable traps by changing the command to
		#  "/bin/echo".
		#
		cmd = "/usr/bin/snmptrap -v2c"
		#
		#  Community string
		#
		community = "public"
		#
		#  Agent configuration.
		#
		agent = "localhost ''"
	}
}
#
#  The "snmptrap" configuration defines the full command used to run the traps.
#
#  This entry should not be edited.  Instead, edit the "trap" section above.
#
snmptrap = "${snmp.trap.cmd} -c ${snmp.trap.community} ${snmp.trap.agent} FREERADIUS-NOTIFICATION-MIB"
#
#  The individual triggers are defined here.  You can disable one by
#  deleting it, or by commenting it out.  You can disable an entire
#  section of traps by deleting the section.
#
#  The entries below should not be edited.  For example, the double colons
#  *must* immediately follow the ${snmptrap} reference.  Adding a space
#  before the double colons  will break all SNMP traps.
#
#  However... the traps are just programs which are run when
#  particular events occur.  If you want to replace a trap with
#  another program, you can.  Just edit the definitions below, so that
#  they run a program of your choice.
#
#  For example, you can leverage the "start/stop" triggers to run a
#  program when the server starts, or when it stops.  But that will
#  prevent the start/stop SNMP traps from working, of course.
#
trigger {
	#
	# Events in the server core
	#
	server {
		# the server has just started
		start = "${snmptrap}::serverStart"
		# the server is about to stop
		stop = "${snmptrap}::serverStop"
		# The "max_requests" condition has been reached.
		# This will trigger only once per 60 seconds.
		max_requests = "${snmptrap}::serverMaxRequests"
		# For events related to clients
		client {
			#  Added a new dynamic client
			add = "/path/to/file %{Packet-Src-IP-Address}"
			#  There is no event for when dynamic clients expire
		}
		# Events related to signals received.
		signal {
			# a HUP signal
			hup = "${snmptrap}::signalHup"
			# a TERM signal
			term = "${snmptrap}::signalTerm"
		}
		# Events related to the thread pool
		thread {
		       # A new thread has been started
		       start = "${snmptrap}::threadStart"
		       # an existing thread has been stopped
		       stop = "${snmptrap}::threadStop"
		       # an existing thread is unresponsive
		       unresponsive = "${snmptrap}::threadUnresponsive"
		       # the "max_threads" limit has been reached
		       max_threads = "${snmptrap}::threadMaxThreads"
		}
	}
	# When a home server changes state.
	# These traps are edge triggered.
	home_server {
		# common arguments: IP, port, identifier
		args = "radiusAuthServerAddress a %{proxy-request:Packet-Dst-IP-Address} radiusAuthClientServerPortNumber i %{proxy-request:Packet-Dst-Port} radiusAuthServIdent s '%{home_server:instance}'"
		# The home server has been marked "alive"
		alive = "${snmptrap}::homeServerAlive ${args}"
		# The home server has been marked "zombie"
		zombie = "${snmptrap}::homeServerZombie ${args}"
		# The home server has been marked "dead"
		dead = "${snmptrap}::homeServerDead ${args}"
	}
	# When a pool of home servers changes state.
	home_server_pool {
		# common arguments
		args = "radiusdConfigName s %{home_server:instance}"
		# It has reverted to "normal" mode, where at least one
		# home server is alive.
		normal = "${snmptrap}::homeServerPoolNormal ${args}"
		# It is in "fallback" mode, with all home servers "dead"
		fallback = "${snmptrap}::homeServerPoolFallback ${args}"
	}
	#  Triggers for specific modules.  These are NOT in the module
	#  configuration because they are global to all instances of the
	#  module.  You can have module-specific triggers, by placing a
	#  "trigger" subsection in the module configuration.
	modules {
		# Common arguments
		args = "radiusdModuleInstance s ''"
		# The files module
		files {
			# Common arguments
			args = "radiusdModuleName s files ${..args}"
			# The module has been HUP'd via radmin
			hup = "${snmptrap}::serverModuleHup ${args}"
			# Note that "hup" can be used for every module
			# which can be HUP'd via radmin
		}
		# The LDAP module
		# If the server does "bind as user", it will open and close
		# an LDAP connection ofr every "bind as user".  Be aware that
		# this will likely produce a lot of triggers.
		ldap {
			# Common arguments
			args = "radiusdModuleName s ldap ${..args}"
			# A new connection to the DB has been opened
			open = "${snmptrap}::serverModuleConnectionUp ${args}"
			# A connection to the DB has been closed
			close = "${snmptrap}::serverModuleConnectionDown ${args}"
			# The module has been HUP'd via radmin
			hup = "${snmptrap}::serverModuleHup ${args}"
		}
		# The SQL module
		sql {
			# Common arguments
			args = "radiusdModuleName s sql ${..args}"
			# A new connection to the DB has been opened
			open = "${snmptrap}::serverModuleConnectionUp ${args}"
			# A connection to the DB has been closed
			close = "${snmptrap}::serverModuleConnectionDown ${args}"
			# Failed to open a new connection to the DB
			fail = "${snmptrap}::serverModuleConnectionFail ${args}"
			# The module has been HUP'd via radmin
			hup = "${snmptrap}::serverModuleHup ${args}"
		}
		# You can also use connection pool's start/stop/open/close triggers
		# for any module which uses the "pool" section, here and under
		# pool.trigger in module configuration.
	}
}
#
#  The complete list of triggers as generated from the source code is below.
#
#  These are the ONLY traps which are generated.  You CANNOT add new traps
#  by defining them in one of the sections above.  New traps can be created
#  only by edited both the source code to the server, *and* the MIBs.
#  If you are not an expert in C and SNMP, then adding new traps will be
#  difficult to create.
#
# home_server.alive
# home_server.dead
# home_server.zombie
# home_server_pool.fallback
# home_server_pool.normal
# modules.*.hup
# modules.ldap.timeout
# modules.sql.close
# modules.sql.fail
# modules.sql.open
# server.client.add
# server.max_requests
# server.signal.hup
# server.signal.term
# server.start
# server.stop
# server.thread.max_threads
# server.thread.start
# server.thread.stop
# server.thread.unresponsive
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2017 2stacks
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: docker-compose.yml
================================================
version: "3"
services:
  chr:
    image: dharma007/mikrotik-cloud:latest
    container_name: mikrotik-2
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun
    ports:
      - "2244:22"
      - "16106:80"
      - "1144:1194"
      - "12423:23"
      - "1213:8291"
      - "18291:8729"
      - "18491:8728"
      - "18221:1812/udp"
      - "18321:1813/udp"
    networks:
      my-network-2:
        ipv4_address: 172.29.1.2
  #command : /bin/bash
#add new eth1 interface
#    - "ip link add eth1 type dummy"
#    - "ip addr add
#    - "ip link set eth1 up"
networks:
  my-network-2:
    external: true
================================================

File: entrypoint.sh
================================================
#!/usr/bin/env bash
# A bridge of this name will be created to host the TAP interface created for
# the VM
QEMU_BRIDGE='qemubr0'
# DHCPD must have an IP address to run, but that address doesn't have to
# be valid. This is the dummy address dhcpd is configured to use.
#DUMMY_DHCPD_IP='10.0.0.254'
DUMMY_DHCPD_IP='172.29.1.254'
# These scripts configure/deconfigure the VM interface on the bridge.
QEMU_IFUP='/routeros/bin/qemu-ifup'
QEMU_IFDOWN='/routeros/bin/qemu-ifdown'
# The name of the dhcpd config file we make
DHCPD_CONF_FILE='/routeros/dhcpd.conf'
function default_intf() {
    ip -json route show | jq -r '.[] | select(.dst == "default") | .dev'
}
# First step, we run the things that need to happen before we start mucking
# with the interfaces. We start by generating the DHCPD config file based
# on our current address/routes. We "steal" the container's IP, and lease
# it to the VM once it starts up.
/routeros/bin/generate-dhcpd-conf.py $QEMU_BRIDGE > $DHCPD_CONF_FILE
default_dev=`default_intf`
# Now we start modifying the networking configuration. First we clear out
# the IP address of the default device (will also have the side-effect of
# removing the default route)
ip addr flush dev $default_dev
# Next, we create our bridge, and add our container interface to it.
ip link add $QEMU_BRIDGE type bridge
ip link set dev $default_dev master $QEMU_BRIDGE
# Then, we toggle the interface and the bridge to make sure everything is up
# and running.
ip link set dev $default_dev up
ip link set dev $QEMU_BRIDGE up
touch /var/lib/udhcpd/udhcpd.leases
# Finally, start our DHCPD server
udhcpd -I $DUMMY_DHCPD_IP -f $DHCPD_CONF_FILE &
# And run the VM! A brief explanation of the options here:
# -enable-kvm: Use KVM for this VM (much faster for our case).
# -nographic: disable SDL graphics.
# -serial mon:stdio: use "monitored stdio" as our serial output.
# -nic: Use a TAP interface with our custom up/down scripts.
# -drive: The VM image we're booting.
exec qemu-system-x86_64 \
    -nographic -serial mon:stdio \
    -vnc 0.0.0.0:0 \
    -m 256 \
    "$@" \
    -hda $ROUTEROS_IMAGE \
    -device e1000,netdev=net0 \
    -netdev user,id=net0 \
    -device e1000,netdev=net1 \
    -netdev user,id=net1 \
    -device e1000,netdev=net2 \
    -netdev user,id=net2 \
    -device e1000,netdev=net3 \
    -netdev user,id=net3 \
    -device e1000,netdev=net4 \
    -netdev user,id=net4 \
    -device e1000,netdev=net5 \
    -netdev user,id=net5 \
    -device e1000,netdev=net6 \
    -netdev user,id=net6 \
    -device e1000,netdev=net7 \
    -netdev user,id=net7 \
    -device e1000,netdev=net8 \
    -netdev user,id=net8 \
    -device e1000,netdev=net9 \
    -netdev user,id=net9 \
    -device e1000,netdev=net10 \
    -netdev user,id=net10,net=172.29.0.0/16,hostfwd=tcp::21-:21,hostfwd=tcp::22-:22,hostfwd=tcp::23-:23,hostfwd=tcp::80-:80,hostfwd=tcp::443-:443,hostfwd=tcp::8291-:8291,hostfwd=tcp::8728-:8728,hostfwd=tcp::8729-:8729 \
    -nic tap,id=qemu0,script=$QEMU_IFUP,downscript=$QEMU_IFDOWN
================================================

File: entrypoint_with_four_interfaces.sh
================================================
#!/bin/sh
qemu-system-x86_64 \
    -vnc 0.0.0.0:0 \
    -m 256 \
    -hda $ROUTEROS_IMAGE \
    -device e1000,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::21-:21,hostfwd=tcp::22-:22,hostfwd=tcp::23-:23,hostfwd=tcp::80-:80,hostfwd=tcp::443-:443,hostfwd=tcp::8291-:8291,hostfwd=tcp::8728-:8728,hostfwd=tcp::8729-:8729 \
    -device e1000,netdev=net1 \
    -netdev user,id=net1 \
    -device e1000,netdev=net2 \
    -netdev user,id=net2 \
    -device e1000,netdev=net3 \
    -netdev user,id=net3
================================================

File: generate-dhcpd-conf.py
================================================
#!/usr/bin/env python3
import argparse
import ipaddress
import json
import re
import socket
import subprocess
from typing import List, Iterable
DEFAULT_ROUTE = 'default'
DEFAULT_DNS_IPS = ('8.8.8.8', '8.8.4.4')
DHCP_CONF_TEMPLATE = """
start {host_addr}
end   {dhcp_host_addr}
#end   172.29.1.20
# avoid dhcpd complaining that we have
# too many addresses
maxleases 21
interface {dhcp_intf}
option dns      {dns}
option router   {gateway}
option subnet   {subnet}
option hostname {hostname}
"""
def default_route(routes):
    """Returns the host's default route"""
    for route in routes:
        if route['dst'] == DEFAULT_ROUTE:
            return route
    raise ValueError('no default route')
def addr_of(addrs, dev : str) -> ipaddress.IPv4Interface:
    """Finds and returns the IP address of `dev`"""
    for addr in addrs:
        if addr['ifname'] != dev:
            continue
        info = addr['addr_info'][0]
        return ipaddress.IPv4Interface((info['local'], info['prefixlen']))
    raise ValueError('dev {0} not found'.format(dev))
def generate_conf(intf_name : str, dns : Iterable[str]) -> str:
    """Generates a dhcpd config. `intf_name` is the interface to listen on."""
    with subprocess.Popen(['ip', '-json', 'route'], stdout=subprocess.PIPE) as proc:
        routes = json.load(proc.stdout)
    with subprocess.Popen(['ip', '-json', 'addr'], stdout=subprocess.PIPE) as proc:
        addrs = json.load(proc.stdout)
    droute = default_route(routes)
    host_addr = addr_of(addrs, droute['dev'])
    #generate max IP DHCP config for a host on the same subnet as the default route
    return DHCP_CONF_TEMPLATE.format(
        dhcp_intf = intf_name,
        dns = ' '.join(dns),
        gateway = droute['gateway'],
        host_addr = host_addr.ip,
        #make end address for dhcpd 20 addresses away from host address
        dhcp_host_addr = ipaddress.IPv4Address(int(host_addr.ip)) + 20,
        hostname = socket.gethostname(),
        subnet = host_addr.network.netmask,
    )
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('intf_name')
    parser.add_argument('dns_ips', nargs='*')
    args = parser.parse_args()
    dns_ips = args.dns_ips
    if not dns_ips:
        dns_ips = DEFAULT_DNS_IPS
    print(generate_conf(args.intf_name, dns_ips))
================================================

File: docker-compose.yaml
================================================
version: "3"
services:
    routeros:
        image: kilip/routeros:6.47.1
        privileged: true
        container_name: "mikrotik-4"
        build:
            context: .
            dockerfile: Dockerfile
        restart: unless-stopped
        ports: 
            - "8243:8291"
            - "8791:8729"
            - "8782:8728"
            - "2652:22"
            - "3799:3799"
            - "18221:1812/udp"
            - "18321:1813/udp"
        cap_add: 
            - NET_ADMIN
        devices: 
            - /dev/net/tun
        networks:
            my-network-2:
                ipv4_address: 172.29.1.4
networks:
  my-network-2:
    external: true
================================================

File: Dockerfile
================================================
FROM alpine:latest
RUN set -xe \
    && apk add --no-cache --update \
        netcat-openbsd \
        qemu-x86_64 \
        qemu-system-x86_64 \
        busybox-extras \
        iproute2 \
        iputils \
        bridge-utils \
        iptables \
        jq \
        bash \
        python3 \
        curl nano
# Environments which may be change
ENV ROUTEROS_VERSION="6.47.2"
ENV ROUTEROS_IMAGE="chr-${ROUTEROS_VERSION}.vdi"
ENV ROUTEROS_URL="https://download.mikrotik.com/routeros/${ROUTEROS_VERSION}/$ROUTEROS_IMAGE"
WORKDIR /routeros
RUN mkdir /routeros/bin
COPY ./bin/* /routeros/bin/
RUN ls -l /routeros/bin
RUN ip link show
RUN wget ${ROUTEROS_URL} -O /routeros/${ROUTEROS_IMAGE}
# Download VDI image from remote site
EXPOSE 21 22 23 80 443 8291 8728 8729 1812 1813
ENTRYPOINT [ "/routeros/bin/entrypoint.sh" ]
================================================

File: network
================================================
 docker network create \
  --driver=bridge \
  --subnet=172.28.0.0/16 \
  --ip-range=172.28.5.0/24 \
  --gateway=172.28.5.1 \
  my-network
# Create a container
 docker network create \
  --driver=bridge \
  --subnet=172.29.0.0/16 \
  --ip-range=172.29.1.0/24 \
  --gateway=172.29.1.1 \
  my-network-2
================================================

File: README.md
================================================
docs/README.md
================================================

File: run-tests.sh
================================================
#!/bin/bash
set -ev
docker-compose up -d
docker pull 2stacks/radtest
# Wait for MySQL to bootstrap
sleep 15
docker-compose ps
#radtest username password radius_server_secret nas_ip_address nas_port_number
#radtest john secret 127.0.0.1:1812 0 testing123
docker run -it --rm --network docker-freeradius_backend 2stacks/radtest radtest testing password my-radius 1812 testing123
#docker run -it --rm --network docker-freeradius_backend 2stacks/radtest radtest testing password my-radius 172.21.0.2 8728 testing123 
#docker exec -it docker-radius-mysql_radius_1 radtest fredf wilma localhost testing123
# docker exec -it stingy_exchange radtest testing password localhost testing123
# radtest user1 password1 172.28.0.3 0 testing123 nasipaddress=192.168.1.100
# radtest hotspotuser password1123 172.28.5.3:1812 8728 testing123  0 172.28.0.11
# radtest user-nas-1 password123 172.28.0.3:1812 8728 testing123  0 172.28.0.4
================================================

File: start.sh
================================================
#!/bin/sh
if [ "${RAD_DEBUG}" = "yes" ]
  then
    /wait-for.sh ${DB_HOST}:${DB_PORT} -t 15 -- /usr/sbin/radiusd -X -f -d /etc/raddb
  else
    /wait-for.sh ${DB_HOST}:${DB_PORT} -t 15 -- /usr/sbin/radiusd -f -d /etc/raddb
fi
================================================

File: startup.sh
================================================
#!/bin/sh
# Start OpenVPN
openvpn --config /etc/openvpn/server.conf &
# Wait until OpenVPN is ready
while ! nc -z localhost 1194; do
  sleep 1
done
# Start FreeRADIUS
freeradius -f
================================================

File: wait-for.sh
================================================
#!/bin/sh
TIMEOUT=15
QUIET=0
echoerr() {
  if [ "$QUIET" -ne 1 ]; then printf "%s\n" "$*" 1>&2; fi
}
usage() {
  exitcode="$1"
  cat << USAGE >&2
Usage:
  $cmdname host:port [-t timeout] [-- command args]
  -q | --quiet                        Do not output any status messages
  -t TIMEOUT | --timeout=timeout      Timeout in seconds, zero for no timeout
  -- COMMAND ARGS                     Execute command with args after the test finishes
USAGE
  exit "$exitcode"
}
wait_for() {
  command="$*"
  for i in `seq $TIMEOUT` ; do
    nc -z "$HOST" "$PORT" > /dev/null 2>&1
    result=$?
    if [ $result -eq 0 ] ; then
      if [ -n "$command" ] ; then
        exec $command
      fi
      exit 0
    fi
    sleep 1
  done
  echo "Operation timed out" >&2
  exit 1
}
while [ $# -gt 0 ]
do
  case "$1" in
    *:* )
    HOST=$(printf "%s\n" "$1"| cut -d : -f 1)
    PORT=$(printf "%s\n" "$1"| cut -d : -f 2)
    shift 1
    ;;
    -q | --quiet)
    QUIET=1
    shift 1
    ;;
    -t)
    TIMEOUT="$2"
    if [ "$TIMEOUT" = "" ]; then break; fi
    shift 2
    ;;
    --timeout=*)
    TIMEOUT="${1#*=}"
    shift 1
    ;;
    --)
    shift
    break
    ;;
    --help)
    usage 0
    ;;
    *)
    echoerr "Unknown argument: $1"
    usage 1
    ;;
  esac
done
if [ "$HOST" = "" -o "$PORT" = "" ]; then
  echoerr "Error: you need to provide a host and port to test."
  usage 2
fi
wait_for "$@"
================================================

File: dependabot.yml
================================================
version: 2
updates:
- package-ecosystem: docker
  directory: "/"
  schedule:
    interval: daily
  open-pull-requests-limit: 10
  ignore:
  - dependency-name: ubuntu
    versions:
    - ">= 16.10.a, < 16.11"
  - dependency-name: ubuntu
    versions:
    - "< 18, >= 17.a"
  - dependency-name: ubuntu
    versions:
    - "< 19, >= 18.a"
================================================

File: .travis.yml
================================================
# travis.yml
sudo: required
services:
  - docker
install:
  - docker build --pull -t 2stacks/docker-ovpn .
# Assist with ci test debugging:
#  - DEBUG=1
before_script:
  - image="2stacks/docker-ovpn"
  - docker inspect "$image"
script:
  - docker run -it --rm -v /$PWD/configs/ovpn:/etc/openvpn 2stacks/docker-ovpn gen-keys
  - docker run -itd -h openvpn --restart=always --name openvpn --cap-add=NET_ADMIN -e "RADIUS_HOST=freeradius" -e "RADIUS_KEY=testing123" -e "DNS_HOST1=1.1.1.1" -e "DNS_HOST2=1.0.0.1" -p 1194:1194/udp -p 443:443 -v /$PWD/configs/ovpn:/etc/openvpn 2stacks/docker-ovpn
  - docker container ls | grep openvpn
notifications:
  email:
    - 2stacks@2stacks.net
================================================

File: README.md
================================================
## Key Files Required in this Directory
-   ca.crt
-   site.crt
-   site.dh
-   site.Key
-   ta.Key
See [OpenVPN PKI HowTo](https://openvpn.net/index.php/open-source/documentation/howto.html#pki)
================================================

File: docker-compose.yml
================================================
version: "3.2"
services:
  ovpn:
    image: "2stacks/docker-ovpn:latest"
    container_name: my-vpn
    networks:
      my-network:
        ipv4_address: 172.28.5.15
    ports:
      - "4433:443"
      - "1194:1194/udp"
    volumes:
      - "./configs/ovpn:/etc/openvpn"
    environment:
      - RADIUS_HOST=my-radius
      - RADIUS_KEY=testing123
      - DNS_HOST1=1.1.1.1
      - DNS_HOST2=1.0.0.1
      - OVPN_DEBUG=yes
    cap_add:
      - NET_ADMIN
    restart: unless-stopped
networks:
  my-network:
    external: true
================================================

File: Dockerfile
================================================
# Credit: https://github.com/jpetazzo/dockvpn
# Credit: https://github.com/kylemanna/docker-openvpn
FROM ubuntu:16.04
MAINTAINER "2stacks@2stacks.net"
# Image details
LABEL net.2stacks.name="2stacks" \
      net.2stacks.license="MIT" \
      net.2stacks.description="Dockerfile for autobuilds" \
      net.2stacks.url="http://www.2stacks.net" \
      net.2stacks.vcs-type="Git" \
      net.2stacks.version="1.5" \
      net.2stacks.ovpn.version="2.4.7"
# Install OpenVPN
RUN apt-get -y update && apt-get install -y \
                                              apt-transport-https \
                                              ca-certificates \
                                              curl \
	                                          iptables \
                                              software-properties-common && \
    curl -fsSL https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] http://build.openvpn.net/debian/openvpn/release/2.4 xenial main" && \
    apt-get -y update && apt-get install -y \
                                              easy-rsa \
                                              openvpn \
	                                          openvpn-auth-radius \
                                              freeradius-utils \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*
# Add Scripts to Configure and Run OpenVPN
ADD ./bin /usr/local/sbin
RUN chmod 755 /usr/local/sbin/*
# Create Mount Point for OpenVPN Config Files
VOLUME /etc/openvpn
# Expose Container Ports to Host
EXPOSE 443/tcp 1194/udp
# Allow run time config of options
ENV RADIUS_KEY=testing123
ENV RADIUS_HOST=my-radius
ENV DNS_HOST1=1.1.1.1
ENV DNS_HOST2=1.0.0.1
# Execute 'run' Script
CMD run
================================================

File: README.md
================================================
## OpenVPN Server in Docker Container
Builds an OpenVPN server that uses Freeradius/MySQL for backend authentication.
Server listens for connections on both UDP 1194 and TCP 443.  The server will look
for key material in '$PWD/config/ovpn'
[![Build Status](https://travis-ci.org/2stacks/docker-ovpn.svg?branch=master)](https://travis-ci.org/2stacks/docker-ovpn)
[![Docker Stars](https://img.shields.io/docker/stars/2stacks/docker-ovpn.svg?style=popout-square)](https://hub.docker.com/r/2stacks/docker-ovpn)
[![Docker Pulls](https://img.shields.io/docker/pulls/2stacks/docker-ovpn.svg?style=popout-square)](https://hub.docker.com/r/2stacks/docker-ovpn)
[![Build Details](https://images.microbadger.com/badges/image/2stacks/docker-ovpn.svg)](https://microbadger.com/images/2stacks/docker-ovpn)
## Supported tags
-   `1.5`, `latest`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/master/Dockerfile)
-   `1.4`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/v1.4/Dockerfile)
-   `1.3`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/v1.3/Dockerfile)
-   `1.2`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/1.2/Dockerfile)
## The following key materials are required to launch the server.
-   ca.crt  
-   site.crt  
-   site.dh  
-   site.key  
-   ta.key
A very basic shell script has been included to generate a set of key material using
EasyRSA.  This key material uses the EasyRSA package default configuration and is not
suitable for use in production.  To generate the keys as well as an example of how
to use the keys in a client configuration run the following;
```
docker run -it --rm -v /$PWD/configs/ovpn:/etc/openvpn 2stacks/docker-ovpn gen-keys
```
All files will be copied to the the local volume mapped to /etc/openvpn.
## Environment Variables
-   RADIUS_HOST=freeradius
-   RADIUS_KEY=testing123
-   DNS_HOST1=1.1.1.1
-   DNS_HOST2=1.0.0.1
-   OVPN_DEBUG=yes
Note: Setting OVPN_DEBUG ENV to anything will enable server logging to /tmp
## Build the OpenVPN Container
```bash
docker build --pull -t 2stacks/docker-ovpn .
```
## Run the OpenVPN Container
```bash
docker run -itd \
  -h openvpn \
  --restart=always \
  --name openvpn \
  --cap-add=NET_ADMIN \
  -e "RADIUS_HOST=freeradius" \
  -e "RADIUS_KEY=testing123" \
  -e "DNS_HOST1=1.1.1.1" \
  -e "DNS_HOST2=1.0.0.1" \
  -p 1194:1194/udp \
  -p 443:443 \
  -v /$PWD/configs/ovpn:/etc/openvpn \
  2stacks/docker-ovpn
```
## Run using Docker Compose (can be used to launch freeradius and mysql)
```bash
docker-compose -f docker-compose.yml up -d
```
## Testing
If you launch the stack using the included docker-compose file you should be able to test that everything is working with;
```bash
docker run -it --rm -v $PWD/configs/ovpn/client.conf:/etc/openvpn/client.conf --device /dev/net/tun:/dev/net/tun --net=docker-ovpn_backend --cap-add=NET_ADMIN 2stacks/ovpn-client client.conf
```
  - Enter Auth Username: testing
  - Enter Auth Password: password
Example 'docker-compose.yml' File
```bash
version: '3.2'
services:
  ovpn:
    image: "2stacks/docker-ovpn:latest"
    ports:
      - "443:443"
      - "1194:1194/udp"
    volumes:
      - "./configs/ovpn:/etc/openvpn"
    environment:
      #- RADIUS_HOST=freeradius
      #- RADIUS_KEY=testing123
      #- DNS_HOST1=1.1.1.1
      #- DNS_HOST2=1.0.0.1
      - OVPN_DEBUG=yes
    cap_add:
      - NET_ADMIN
    restart: always
    networks:
      - backend
  freeradius:
    image: "2stacks/freeradius"
    #ports:
      #- "1812:1812/udp"
      #- "1813:1813/udp"
    #volumes:
      #- "./configs/radius/users:/etc/raddb/users"
    environment:
      #- DB_NAME=radius
      - DB_HOST=mysql
      #- DB_USER=radius
      #- DB_PASS=radpass
      #- DB_PORT=3306
      #- RADIUS_KEY=testing123
      #- RAD_CLIENTS=10.0.0.0/24
      - RAD_DEBUG=yes
    depends_on:
      - mysql
    links:
      - mysql
    restart: always
    networks:
      - backend
  mysql:
    image: "mysql:5.7"
    command: mysqld
    #ports:
      #- "3306:3306"
    volumes:
      - "./configs/mysql/master/data:/var/lib/mysql"
      - "./configs/mysql/master/conf.d:/etc/mysql/conf.d"
      - "./configs/mysql/radius.sql:/docker-entrypoint-initdb.d/radius.sql"
    environment:
      - MYSQL_ROOT_PASSWORD=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radpass
      - MYSQL_DATABASE=radius
    restart: always
    networks:
      - backend
networks:
  backend:
    ipam:
      config:
        - subnet: 10.0.0.0/24
```
================================================

File: _config.yml
================================================
remote_theme: mmistakes/minimal-mistakes
titles_from_headings:
  enabled:     true
  strip_title: true
plugins:
  - jekyll-include-cache
  - jekyll-titles-from-headings
================================================

File: LICENSE.md
================================================
MIT License
Copyright (c) 2017 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
## OpenVPN Server in Docker Container
Builds an OpenVPN server that uses Freeradius/MySQL for backend authentication.
Server listens for connections on both UDP 1194 and TCP 443.  The server will look
for key material in '$PWD/config/ovpn'
[![Build Status](https://travis-ci.org/2stacks/docker-ovpn.svg?branch=master)](https://travis-ci.org/2stacks/docker-ovpn)
[![Docker Stars](https://img.shields.io/docker/stars/2stacks/docker-ovpn.svg?style=popout-square)](https://hub.docker.com/r/2stacks/docker-ovpn)
[![Docker Pulls](https://img.shields.io/docker/pulls/2stacks/docker-ovpn.svg?style=popout-square)](https://hub.docker.com/r/2stacks/docker-ovpn)
[![Build Details](https://images.microbadger.com/badges/image/2stacks/docker-ovpn.svg)](https://microbadger.com/images/2stacks/docker-ovpn)
## Supported tags
-   `1.5`, `latest`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/master/Dockerfile)
-   `1.4`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/v1.4/Dockerfile)
-   `1.3`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/v1.3/Dockerfile)
-   `1.2`  [*(Dockerfile)*](https://github.com/2stacks/docker-ovpn/blob/1.2/Dockerfile)
## The following key materials are required to launch the server.
-   ca.crt  
-   site.crt  
-   site.dh  
-   site.key  
-   ta.key
A very basic shell script has been included to generate a set of key material using
EasyRSA.  This key material uses the EasyRSA package default configuration and is not
suitable for use in production.  To generate the keys as well as an example of how
to use the keys in a client configuration run the following;
```
docker run -it --rm -v /$PWD/configs/ovpn:/etc/openvpn 2stacks/docker-ovpn gen-keys
```
All files will be copied to the the local volume mapped to /etc/openvpn.
## Environment Variables
-   RADIUS_HOST=freeradius
-   RADIUS_KEY=testing123
-   DNS_HOST1=1.1.1.1
-   DNS_HOST2=1.0.0.1
-   OVPN_DEBUG=yes
Note: Setting OVPN_DEBUG ENV to anything will enable server logging to /tmp
## Build the OpenVPN Container
```bash
docker build --pull -t 2stacks/docker-ovpn .
```
## Run the OpenVPN Container
```bash
docker run -itd \
  -h openvpn \
  --restart=always \
  --name openvpn \
  --cap-add=NET_ADMIN \
  -e "RADIUS_HOST=freeradius" \
  -e "RADIUS_KEY=testing123" \
  -e "DNS_HOST1=1.1.1.1" \
  -e "DNS_HOST2=1.0.0.1" \
  -p 1194:1194/udp \
  -p 443:443 \
  -v /$PWD/configs/ovpn:/etc/openvpn \
  2stacks/docker-ovpn
```
## Run using Docker Compose (can be used to launch freeradius and mysql)
```bash
docker-compose -f docker-compose.yml up -d
```
## Testing
If you launch the stack using the included docker-compose file you should be able to test that everything is working with;
```bash
docker run -it --rm -v $PWD/configs/ovpn/client.conf:/etc/openvpn/client.conf --device /dev/net/tun:/dev/net/tun --net=docker-ovpn_backend --cap-add=NET_ADMIN 2stacks/ovpn-client client.conf
```
  - Enter Auth Username: testing
  - Enter Auth Password: password
Example 'docker-compose.yml' File
```bash
version: '3.2'
services:
  ovpn:
    image: "2stacks/docker-ovpn:latest"
    ports:
      - "443:443"
      - "1194:1194/udp"
    volumes:
      - "./configs/ovpn:/etc/openvpn"
    environment:
      #- RADIUS_HOST=freeradius
      #- RADIUS_KEY=testing123
      #- DNS_HOST1=1.1.1.1
      #- DNS_HOST2=1.0.0.1
      - OVPN_DEBUG=yes
    cap_add:
      - NET_ADMIN
    restart: always
    networks:
      - backend
  freeradius:
    image: "2stacks/freeradius"
    #ports:
      #- "1812:1812/udp"
      #- "1813:1813/udp"
    #volumes:
      #- "./configs/radius/users:/etc/raddb/users"
    environment:
      #- DB_NAME=radius
      - DB_HOST=mysql
      #- DB_USER=radius
      #- DB_PASS=radpass
      #- DB_PORT=3306
      #- RADIUS_KEY=testing123
      #- RAD_CLIENTS=10.0.0.0/24
      - RAD_DEBUG=yes
    depends_on:
      - mysql
    links:
      - mysql
    restart: always
    networks:
      - backend
  mysql:
    image: "mysql:5.7"
    command: mysqld
    #ports:
      #- "3306:3306"
    volumes:
      - "./configs/mysql/master/data:/var/lib/mysql"
      - "./configs/mysql/master/conf.d:/etc/mysql/conf.d"
      - "./configs/mysql/radius.sql:/docker-entrypoint-initdb.d/radius.sql"
    environment:
      - MYSQL_ROOT_PASSWORD=radius
      - MYSQL_USER=radius
      - MYSQL_PASSWORD=radpass
      - MYSQL_DATABASE=radius
    restart: always
    networks:
      - backend
networks:
  backend:
    ipam:
      config:
        - subnet: 10.0.0.0/24
```