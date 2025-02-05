# Repository Information
Name: mikrotik-usage-logging

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
	url = https://gitlab.com/iqrok/mikrotik-usage-logging.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: db.class.js
================================================
// from here -> https://codeburst.io/node-js-mysql-and-promises-4c3be599909b
'use strict';
const mysql = require( 'mysql' );
const md5 = require( 'md5' );
class Database {
    constructor( config ) {
			//~ console.log(global);
			if(global.__sqlConfigs === undefined){
				global.__sqlConfigs = [];
			}
			if(global.__sqlConnection === undefined){
				global.__sqlConnection = {};
			}
			this.config = config;
			this.config.dateStrings = true;
			if(this.config.gracefulExit === undefined)
				this.config.gracefulExit= true;
			this.config_hash = md5(JSON.stringify(config));
			if(!__sqlConfigs.includes(this.config_hash)){
				__sqlConfigs.push(this.config_hash);
				__sqlConnection[this.config_hash] = mysql.createPool( this.config );
			}
    }
    query( sql, args) {
			let ini = this;
			return new Promise(async ( resolve, reject ) => {
				//just in case. Limit query executed only for data manipulation only
				if(sql.match(/(CREATE|TRUNCATE|GRANT|DROP|ALTER|SHUTDOWN)/)){
					return reject(["SQL Query contains forbidden words : CREATE,TRUNCATE,GRANT,DROP,ALTER,SHUTDOWN"]);
				}
				let __error=false;
				let __rows;
				if(!__sqlConfigs.includes(this.config_hash)){
					__sqlConnection[this.config_hash] = mysql.createPool( this.config );
				}
				//~ console.dir(__sqlConnection);
				this.connection = __sqlConnection[this.config_hash];
				this.connection.getConnection(function(err,conn){
					if(err){
						return reject(err);
					}
					conn.query(sql,args,async(err,rows)=>{
						conn.release();
						if(err){
							return reject(err);
						}
						if(rows.length!== null && rows.length == 0)
							return reject(["Empty Result"]);
						resolve( rows );
					});
				});
			});
		}
    open() {
			let ini = this;
			//~ this.connection = mysql.createConnection( this.config );
			this.connection = mysql.createPool( this.config );
			this.connection.on('error', async function(err) {
				console.error('iki error',err.code); // 'ER_BAD_DB_ERROR'
				//~ if(err.code === 'ER_CON_COUNT_ERROR'){
					await this.connection.end();
				//~ }
				console.log('connection restarted');
				await ini.open();
			});
    }
    close() {
        return new Promise( ( resolve, reject ) => {
            this.connection.end( err => {
                if ( err )
                    return reject( err );
                resolve();
            } );
        } );
    }
    execute(sql, param=[], inArray = false){
      //return query not as promise, but as a dircet value
      return this.query(sql,param)
      .then(results=>{
				//~ console.log(results);
				//~ try{
					if(!Array.isArray(results) && results instanceof Object)
						return results;
				//~ }
				//~ catch{
					else
						return (results.length>1 || inArray)?(results):(results[0]);
				//~ }
			})
			.catch(error=>{
				return {__ERROR__:error};
			});
    }
    escape(string){
      return this.connection.escape(string);
    }
}
module.exports = Database;
================================================

File: db_config.sample.json
================================================
{
    "host"     : "localhost",
    "user"     : "root",
    "password" : "",
    "database" : "mikrotik_db"
}
================================================

File: mikrotik_config.sample.json
================================================
{
	"host"		: "192.168.88.1",
	"user"		: "yyyyyy",
	"password": "xxxxx",
	"port"		: "8678"
}
================================================

File: dhcp-server.js
================================================
const mtikConfig = require('./config/mikrotik_config.json');
const RouterOSClient = require('routeros-client').RouterOSClient;
const getListDHCP = async function(){
	const api = new RouterOSClient(mtikConfig);
	const mtikResult = await api.connect()
		.then(async (client) => {
				let status = false
				return client.menu("/ip dhcp-server lease")
				.exec('print')
				.then(results => {
					//~ console.log('DHCP',results);
					return results;
				})
				.catch(error=>{
					console.error(error);
				});
		})
		.catch((err) => {
				// Connection error
				console.error('Timed Out Error:',err);
				return null;
		});
	await api.close().then(() =>{
		console.log('DHCP DONE..!');
	}).catch((err) =>{
		// Error trying to disconnect
		console.log('DHCP Err:',err);
	});
	return mtikResult;
}
module.exports = {
	getListDHCP:getListDHCP,
};
================================================

File: index.js
================================================
const config = require('./config/db_config.json');
const mtikConfig = require('./config/mikrotik_config.json');
const __mysql = require('./class/db.class.js');
const mysql = new __mysql(config);
const RouterOSClient = require('routeros-client').RouterOSClient;
const CronJob = require('cron').CronJob;
const __INTERVAL = 10000;
const localIP_LIKES = '192.168.';
const cronUpdate = require('./updateData.js');
const dhcp = require('./dhcp-server.js');
const getDataMikrotik = async function(){
	const api = new RouterOSClient(mtikConfig);
	const mtikResult = await api.connect()
		.then(async (client) => {
				let status = false
				await client.menu("/ip accounting snapshot")
				.exec('take')
				.then(result => {
					status = true;
					return result;
				})
				.catch(error=>{
					console.error(error);
				});
				if(status){
					const tmpMtik = await client.menu("/ip accounting snapshot")
					.exec('print')
					.then((result) => {
						return result;
					}).catch((err) => {
						console.log(err); // Some error trying to get the identity
						return null;
					});
					return tmpMtik;
				}
		})
		.catch((err) => {
				// Connection error
				console.error('Timed Out Error:',err);
				return null;
		});
	await api.close().then(() =>{
		console.log('Fetching DONE..!');
	}).catch((err) =>{
			// Error trying to disconnect
			console.log('Fetching Err:',err);
	});
	return mtikResult;
}
const insertIntoDB = async function(){
	const timer = new Date();
	const mtikResult = await getDataMikrotik();
	if(mtikResult){
		let sql = 'INSERT INTO mtik_accounting(`accSrcAddr`,`accDstAddr`,`accPackets`,`accBytes`,`accTypeId`) VALUES ?';
		let params = [];
		for(let key in mtikResult){
			const data = mtikResult[key];
			/* NETWORK TYPE:
			 *	1 : LOCAL
			 * 	2	:	DOWNSTREAM
			 * 	3	:	UPSTREAM
			 * */
			let networkType = null;
			if(data.srcAddress.includes(localIP_LIKES) && data.dstAddress.includes(localIP_LIKES))
				networkType = 1;
			else if(!data.srcAddress.includes(localIP_LIKES) && data.dstAddress.includes(localIP_LIKES))
				networkType = 2;
			else if(data.srcAddress.includes(localIP_LIKES) && !data.dstAddress.includes(localIP_LIKES))
				networkType = 3;
			else
				networkType = 4;
			params.push([data.srcAddress,data.dstAddress,data.packets,data.bytes,networkType]);
		}
		return mysql.query(sql,[params])
			.then(result => {
				console.log(new Date()-timer,'SUCCESS ',params.length,new Date());
				return true;
			})
			.catch(async error=>{
				if(error.code == 'ER_LOCK_DEADLOCK'){
					console.log('DEADELOCK HAPPENS. Trying to Re-query again');
					await mysql.query(sql,[params])
						.catch(error => {
							console.error('Still Error after deadlock',error);
						})
				}
				else{
					console.error(error);
				}
				return false;
			});
	}
	console.log('Failed while attempting fetch');
	return false
}
const updateDHCP = new CronJob('* 2,32 * * * *', async function() {
	const sql = "INSERT INTO mtik_local_ip(`ipAddress`,`ipHostname`,`ipMACAddress`) VALUES(?,?,?) ON DUPLICATE KEY UPDATE  ipMACAddress=VALUES(ipMACAddress)";
	const DHCPList = await dhcp.getListDHCP();
	//~ console.log(DHCPList);
	for(let tmp of DHCPList){
		await mysql.query(sql,[tmp.address ,tmp.hostName ,tmp.macAddress])
			.then(result => {
				console.log('DHCP LIST UPDATE SUCCEEDED',new Date());
				return true;
			})
			.catch(error => {
				console.error('DHCP LIST  UPDATE FAILED! ',error);
				return false;
			});
	}
}, null, true, 'Asia/Jakarta');
cronUpdate.start();
setInterval(async function(){
	await insertIntoDB();
}, __INTERVAL);
================================================

File: package.json
================================================
{
  "name": "mikrotik-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cron": "^1.7.2",
    "json5": "^2.1.1",
    "md5": "^2.2.1",
    "mysql": "^2.17.1",
    "routeros-client": "^0.11.0"
  }
}
================================================

File: README.md
================================================
# Mikrotik Usage Logging
> You need to create configs file first, just copy files inside config folder, and remove '.sample' from file's name
================================================

File: mikrotik_db.sql
================================================
-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 07, 2019 at 07:20 PM
-- Server version: 10.3.17-MariaDB-0+deb10u1
-- PHP Version: 7.3.9-1~deb10u1
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
--
-- Database: `mikrotik_db`
--
-- --------------------------------------------------------
--
-- Table structure for table `mtik_accounting`
--
CREATE TABLE `mtik_accounting` (
  `accId` bigint(20) NOT NULL,
  `accSrcAddr` varchar(15) DEFAULT NULL,
  `accDstAddr` varchar(15) DEFAULT NULL,
  `accPackets` int(11) DEFAULT NULL,
  `accBytes` int(11) DEFAULT NULL,
  `accTypeId` tinyint(4) UNSIGNED DEFAULT NULL,
  `accTimestamp` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------
--
-- Table structure for table `mtik_local_ip`
--
CREATE TABLE `mtik_local_ip` (
  `ipAddress` varchar(16) NOT NULL,
  `ipHostname` varchar(64) DEFAULT NULL,
  `ipMACAddress` varchar(24) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------
--
-- Table structure for table `mtik_total_downstream_local`
--
CREATE TABLE `mtik_total_downstream_local` (
  `downstreamIP` varchar(15) NOT NULL,
  `downstreamDate` date NOT NULL,
  `downstreamTotalMB` int(11) DEFAULT NULL,
  `downstreamTimestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------
--
-- Table structure for table `mtik_total_upstream_local`
--
CREATE TABLE `mtik_total_upstream_local` (
  `upstreamIP` varchar(15) NOT NULL,
  `upstreamDate` date NOT NULL,
  `upstreamTotalMB` int(11) DEFAULT NULL,
  `upstreamTimestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------
--
-- Table structure for table `mtik_types`
--
CREATE TABLE `mtik_types` (
  `typeId` tinyint(4) UNSIGNED NOT NULL,
  `typeName` varchar(10) DEFAULT NULL,
  `typeNetwork` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Indexes for dumped tables
--
--
-- Indexes for table `mtik_accounting`
--
ALTER TABLE `mtik_accounting`
  ADD PRIMARY KEY (`accId`),
  ADD KEY `accType` (`accTypeId`),
  ADD KEY `accSrcAddr` (`accSrcAddr`),
  ADD KEY `accDstAddr` (`accDstAddr`);
--
-- Indexes for table `mtik_local_ip`
--
ALTER TABLE `mtik_local_ip`
  ADD PRIMARY KEY (`ipAddress`);
--
-- Indexes for table `mtik_total_downstream_local`
--
ALTER TABLE `mtik_total_downstream_local`
  ADD PRIMARY KEY (`downstreamIP`,`downstreamDate`);
--
-- Indexes for table `mtik_total_upstream_local`
--
ALTER TABLE `mtik_total_upstream_local`
  ADD PRIMARY KEY (`upstreamIP`,`upstreamDate`);
--
-- Indexes for table `mtik_types`
--
ALTER TABLE `mtik_types`
  ADD PRIMARY KEY (`typeId`);
--
-- AUTO_INCREMENT for dumped tables
--
--
-- AUTO_INCREMENT for table `mtik_accounting`
--
ALTER TABLE `mtik_accounting`
  MODIFY `accId` bigint(20) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mtik_types`
--
ALTER TABLE `mtik_types`
  MODIFY `typeId` tinyint(4) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
================================================

File: updateData.js
================================================
const config = require('./config/db_config.json');
const mtikConfig = require('./config/mikrotik_config.json');
const __mysql = require('./class/db.class.js');
const mysql = new __mysql(config);
const CronJob = require('cron').CronJob;
const updateData = new CronJob('55 29,59,14,44 * * * *', async function() {
	const upstream = mysql.query('CALL  p_insert_edit_total_upstream();',[])
		.then(result => {
			console.log('UPSTREAM UPDATE SUCCEEDED',new Date());
			return true;
		})
		.catch(error => {
			console.error('UPSTREAM UPDATE FAILED! ',error);
			return false;
		});
	const downstream = mysql.query('CALL  p_insert_edit_total_downstream();',[])
		.then(result => {
			console.log('DOWNSTREM UPDATE SUCCEEDED',new Date());
			return true;
		})
		.catch(error => {
			console.error('DOWNSTREM UPDATE FAILED! ',error);
			return false;
		});
	await(downstream);
	await(upstream);
}, null, true, 'Asia/Jakarta');
module.exports = updateData;