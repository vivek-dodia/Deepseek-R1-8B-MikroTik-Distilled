# Repository Information
Name: mikronode

# Files

File: .eslintrc.json
================================================
{
    "env": {
        "browser": true,
        "commonjs": true,
        "es6": true,
        "node": true
    },
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": true
        },
        "sourceType": "module"
    },
    "rules": {
        "no-const-assign": "warn",
        "no-this-before-super": "warn",
        "no-undef": "warn",
        "no-unreachable": "warn",
        "no-unused-vars": "warn",
        "constructor-super": "warn",
        "valid-typeof": "warn"
    }
}
================================================

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
	url = https://gitlab.com/audy018/mikronode.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "release"]
	remote = origin
	merge = refs/heads/release
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: constants.js
================================================
export default {};
================================================

File: getInterfacesAndRoutes.js
================================================
var api=require('../dist/mikronode.js');
var device=new api(/* Host */'10.10.10.10' /*, Port */ /*, Timeout */);
// device.setDebug(api.DEBUG);
// connect: user, password.
device.connect().then(([login])=>login('username','password')).then(function(conn) {
    var c1=conn.openChannel();
    var c2=conn.openChannel();
    c1.closeOnDone(true);
    c2.closeOnDone(true);
    console.log('Getting Interfaces');
    c1.write('/interface/ethernet/print');
    console.log('Getting routes');
    c2.write('/ip/route/print');
    c1.data // get only data here
      .subscribe(function(data) { // feeds in one result line at a time.
          console.log('Interfaces:');
          console.log(JSON.stringify(data.data,true,2));
       })
    // In this one, we wait for the data to be done before running handler.
    c2.done // return here only when all data is received.
      .subscribe(function(data){ // feeds in all results at once.
        console.log('Routes:');
        // data.forEach(function(i){console.log(JSON.stringify(i,4,true))});
        console.log(JSON.stringify(data.data,true,2));
      });
},function(err) {
  console.log("Error connecting:",err);
});
================================================

File: ipCountOnly.js
================================================
var MikroNode = require('../dist/mikronode.js');
// Create API instance to a host.
var device = new MikroNode('10.10.10.10');
// device.setDebug(MikroNode.DEBUG);
// Connect to MikroTik device
device.connect(/* socketOpts */).then(([login])=>login('username','password')).then(
	function(conn) { 
		// When all channels are marked done, close the connection.
		conn.closeOnDone(true);
		var channel1=conn.openChannel();
		var channel2=conn.openChannel();
		// get only a count of the addresses.
		channel1.write(['/ip/address/print','=count-only=']);
		// Get all of the addresses
		channel2.write('/ip/address/print');
		// Print data from channel 1
		channel1.data.subscribe(e=>console.log("Data 1: ",e.data));
		// Pring data from channel 2
		channel2.data.subscribe(e=>console.log("Data 2: ",e.data));
	}
);
================================================

File: promise.js
================================================
require('babel-register');var MikroNode = require('../src');
var device = new MikroNode('10.10.10.10');
// device.setDebug(MikroNode.DEBUG);
device.connect().then(([login])=>login('admin','password')).then(function(conn) {
    console.log("Logged in.");
    conn.closeOnDone(true); // All channels need to complete before the connection will close.
    var listenChannel=conn.openChannel("listen");
    // Each sentence that comes from the device goes through the data stream.
    listenChannel.data.subscribe(function(data) {
        // var packet=MikroNode.resultsToObj(data);
        console.log('Interface change: ',JSON.stringify(data));
    },error=>{
        console.log("Error during listenChannel subscription",error) // This shouldn't be called.
    },()=>{
        console.log("Listen channel done.");
    });
    // Tell our listen channel to notify us of changes to interfaces.
    listenChannel.write('/interface/listen').then(result=>{
        console.log("Listen channel done promise.",result);
    })
    // Catch shuold be called when we call /cancel (or listenChannel.close())
    .catch(error=>console.log("Listen channel rejection:",error));
    // All our actions go through this.
    var actionChannel=conn.openChannel("action",false); // don't close on done... because we are running these using promises, the commands complete before each then is complete.
    // Do things async. This is to prove that promises work as expected along side streams.
    actionChannel.sync(false);
    actionChannel.closeOnDone(false); // Turn off closeOnDone because the timeouts set to allow the mikrotik to reflect the changes takes too long. The channel would close.
    // These will run synchronsously (even though sync is not set to true)
    console.log("Disabling interface");
    actionChannel.write('/interface/set',{'disabled':'yes','.id':'ether1'}).then(results=>{
        console.log("Disable complete.");
        // when the first item comes in from the listen channel, it should send the next command.
        const {promise,resolve,reject}=MikroNode.getUnwrappedPromise();
        listenChannel.data
            .take(1)
            // This is just to prove that it grabbed the first one.
            .do(d=>console.log("Data:",MikroNode.resultsToObj(d.data)))
            .subscribe(d=>actionChannel.write('/interface/set',{'disabled':'no','.id':'ether1'}).then(resolve,reject));
        return promise;
    })
    .then(results=>{
        console.log("Enabled complete.");
        // return new Promise((r,x)=>setTimeout(r,1000)).then(()=>actionChannel.write('/interface/getall'));
        const {promise,resolve,reject}=MikroNode.getUnwrappedPromise();
        // when the second item comes in from the listen channel, it should send the next command.
        listenChannel.data
            .take(1)
            // This is just to prove that it grabbed the second one.
            .do(d=>console.log("Data:",MikroNode.resultsToObj(d.data)))
            .subscribe(d=>actionChannel.write('/interface/getall').then(resolve,reject));
        return promise;
    })
    .then(results=>{
        var formatted=MikroNode.resultsToObj(results.data);
        var columns=[".id","name","mac-address","comment"];
        var filtered=formatted.map(line=>columns.reduce((p,c)=>{p[c]=line[c];return p},{}));
        console.log('Interface [ID,Name,MAC-Address]: ',JSON.stringify(filtered,true,4));
    })
    .catch(error=>{
        console.log("An error occurred during one of the above commands: ",error);
    })
    // This runs after all commands above, or if an error occurs.
    .then(nodata=>{
        console.log("Closing everything.");
        listenChannel.close(true); // This should call the /cancel command to stop the listen.
        actionChannel.close();
    });
}).catch(e=>console.log("Error connecting: ",e));
================================================

File: showLog.js
================================================
var MikroNode = require('../dist/mikronode.js');
// Create API link to host. No connection yet..
var device = new MikroNode('10.10.10.10');
// Debug level is "DEBUG"
// device.setDebug(MikroNode.DEBUG);
var removeId=[];
// Connect to the MikroTik device.
device.connect()
      .then(([login])=>login('username','password'))
      .then(function(conn) {
        console.log("Connected")
    // var channel=conn.openChannel('all_addresses');
    // channel.closeOnDone(true); // only use this channel for one command.
    var listener=conn.openChannel('address_changes');
    listener.closeOnDone(true); // only use this channel for one command.
    // channel.write('/ip/address/print');
    listener.write('/log/listen');
    // channel.write('/ip/firewall/filter/print');
    listener.data.filter(d=>d.data[d.data.length-1].field!=='.dead').subscribe(d=>{
        const data = MikroNode.resultsToObj(d.data.filter(col=>["time","topics","message"].indexOf(col.field)!=-1));
        console.log("Log:",JSON.stringify(data));
    });
    // in 5 seconds, stop listening for address changes.
    setTimeout(function() {
        console.log("Closing out listener");
        listener.write('/cancel'); /* cancel listen */
    },500000);
}).catch(function(err) {
    console.log("Failed to connect. ",err);
});
================================================

File: simpleWrite.js
================================================
var MikroNode = require('../dist/mikronode.js');
// Create API instance to a host.
var device = new MikroNode('10.10.10.10');
device.setDebug(MikroNode.DEBUG);
// Connect to MikroTik device
device.connect().then(([login])=>login('admin','password')).then(conn=>{
		// When all channels are marked done, close the connection.
	    console.log('connected');
		conn.closeOnDone(true);
		var channel1=conn.openChannel();
		channel1.closeOnDone(true);
		console.log('going write 1');
		// get only a count of the addresses.
		channel1.write('/interface/set',{
			'name':'ether1',
			'disabled': 'yes'
		}).then(data=>{
			console.log("Done");
		}).catch(error=>{
			console.log("Error result ",error);
		});
		console.log('Wrote');
	}
).catch(error=>{
	console.log("Error logging in ",error);
});
================================================

File: testCount.js
================================================
var MikroNode = require('../dist/mikronode.js');
// Create API instance to a host.
var device = new MikroNode('10.10.10.10');
// device.setDebug(MikroNode.DEBUG);
// Connect to MikroTik device
device.connect().then(([login])=>login('admin','password')).then(conn=>{
		// When all channels are marked done, close the connection.
	    console.log('connected');
		conn.closeOnDone(true);
		var channel1=conn.openChannel();
		channel1.closeOnDone(true);
		console.log('going write 1');
		// get only a count of the addresses.
		channel1.write('/ip/address/print',{
			'=count-only=':''
		}).then(data=>{
			console.log("Done",JSON.stringify(data));
		}).catch(error=>{
			console.log("Error result ",error);
		});
		console.log('Wrote');
	}
).catch(error=>{
	console.log("Error logging in ",error);
});
================================================

File: watchIpList.js
================================================
var MikroNode = require('../dist/mikronode.js');
// Create API link to host. No connection yet..
var device = new MikroNode('10.10.10.10');
// Debug level is "DEBUG"
// device.setDebug(MikroNode.DEBUG);
var removeId=[];
// Connect to the MikroTik device.
device.connect().then(([login])=>login('username','password')).then(function(conn) {
    var channel=conn.openChannel('all_addresses');
    channel.closeOnDone(true); // only use this channel for one command.
    var listener=conn.openChannel('address_changes');
    channel.write('/ip/address/print');
    listener.write('/ip/address/listen');
    channel.done //merge done with data from firewall connections. why? no reason.
        .merge(listener.data)
        .scan(function(last,stream,idx) {
            // console.log('Concat stream data to last',JSON.stringify(stream,true,2));
            if (stream.type==='done') {
                console.log('Concat stream data to last',stream.type);
                return last.concat(stream.data.map(MikroNode.resultsToObj));
            }
            else {
                const data = MikroNode.resultsToObj(stream.data);
                if (data['.dead']) {
                    return last.filter(function(n) {
                        return n.field=='.id' !== data['.id'];
                    });
                } else {
                    console.log("New IP detected",data);
                    removeId.push(data['.id']);
                    return last.concat(data);
                }
            }
        },[]).subscribe(function(changes) {
            ipList=changes;
        });
    const addressInjector=conn.openChannel('address_inject');
    setTimeout(function() {
        const id=removeId.pop();
        console.log("Delete one...",id);
        addressInjector.write('/ip/address/remove',{
            '.id':id
        });
    },3000);
    listener.trap.subscribe(t=>{
        console.log("Ip list on trap:",ipList);
        // Don't care about why.. just remove the new ones.
        var id;
        while(id=removeId.pop()) {
            console.log("Removing id ",id);
            addressInjector.write('/ip/address/remove',{
                '.id':id
            });
        }
    })
    setTimeout(function() {
        addressInjector.write('/ip/address/add',{
            'address'   :'10.1.1.1',
            'interface' :'ether1',
            'netmask'   :'255.255.255.252',
            'disabled'  :'yes'
        });
    },1000);
    setTimeout(function() {
        addressInjector.write('/ip/address/add',{
            'address'   :'10.1.1.2',
            'interface' :'ether1',
            'netmask'   :'255.255.255.252',
            'disabled'  :'yes'
        });
    },1000);
    addressInjector.write('/ip/address/print');
    addressInjector.data.subscribe(d=>console.log('Address Inject Data: ',d));
    var ipList=[];
    // in 5 seconds, stop listening for address changes.
    setTimeout(function() {
        console.log("Closing out listener");
        listener.write('/cancel'); /* cancel listen */
    },5000);
},function(err) {
    console.log("Failed to connect. ",err);
});
================================================

File: package.json
================================================
{
  "name": "mikronode",
  "description": "Mikrotik API implemented in Node",
  "version": "2.3.7",
  "author": "Brandon Myers <trakkasure@gmail.com>",
  "scripts": {
    "prebuild": "pegjs src/parser.g",
    "build": "webpack --color --progress",
    "dev": "webpack --watch --color -d --progress",
    "compile:debug": "f(){ webpack --entry=\"$1\" --output-path=./.compiled --output-filename=debug.js; };f",
    "precompile:debug": "rm -rf .compiled",
    "clean": "rm -rf dist .compiled",
    "prepublish": "npm run build"
  },
  "contributors": [
    {
      "name": "Brandon Myers",
      "email": "trakkasure@gmail.com"
    }
  ],
  "keywords": [
    "mikrotik",
    "socket",
    "api"
  ],
  "repository": "git://github.com/trakkasure/mikronode",
  "bugs": "https://github.com/Trakkasure/mikronode/issues",
  "devDependencies": {
    "babel": "^6.5.2",
    "babel-eslint": "^6.1.2",
    "babel-loader": "^6.2.4",
    "babel-plugin-add-module-exports": "^0.2.1",
    "babel-plugin-transform-decorators-legacy": "^1.3.4",
    "babel-plugin-transform-dev-warning": "^0.1.0",
    "babel-plugin-transform-private-properties": "^1.0.2",
    "babel-plugin-transform-replace-object-assign": "^0.2.1",
    "babel-plugin-transform-runtime": "^6.12.0",
    "babel-polyfill": "^6.9.1",
    "babel-preset-es2015": "^6.14.0",
    "babel-preset-stage-1": "^6.5.0",
    "babel-register": "^6.24.1",
    "chai": "^3.5.0",
    "mocha": ">=1.7.4",
    "simple-assign": "^0.1.0",
    "uglify-js": ">=1.2.5",
    "webpack": "^1.13.1",
    "webpack-dev-server": "^1.15.0"
  },
  "dependencies": {
    "core-decorators": "^0.12.3",
    "rxjs": "^5.3.0"
  },
  "main": "dist/mikronode.js",
  "engines": {
    "node": ">= 6"
  }
}
================================================

File: Readme.md
================================================
# Mikronode
  Full-Featured asynchronous Mikrotik API interface for [NodeJS](http://nodejs.org).
 ```javscript 
     var MikroNode = require('mikronode');
     var device = new MikroNode('192.168.0.1');
     device.connect()
       .then(([login])=>{
         return login('username','password');
       })
       .then(function(conn) {
         var chan=conn.openChannel("addresses"); // open a named channel
         var chan2=conn.openChannel("firewall_connections",true); // open a named channel, turn on "closeOnDone"
         chan.write('/ip/address/print');
         chan.on('done',function(data) {
              // data is all of the sentences in an array.
              data.forEach(function(item) {
                 console.log('Interface/IP: '+item.data.interface+"/"+item.data.address);
              });
              chan.close(); // close the channel. It is not autoclosed by default.
              conn.close(); // when closing connection, the socket is closed and program ends.
         });
         chan.write('/ip/firewall/print');
         chan.done.subscribe(function(data){
              // data is all of the sentences in an array.
              data.forEach(function(item) {
                 var data = MikroNode.resultsToObj(item.data); // convert array of field items to object.
                 console.log('Interface/IP: '+data.interface+"/"+data.address);
              });
         });
     });
```
## Installation
  Clone this repository into your node_modules directory.
  - or -
     $ npm install mikronode
## Features
  * Channel based communication
  * Multiple channels can be used at once.
  * Synchronous execution of commands issued on the same channel.
  * Asynchrounous execution of commands issued on different channels.
  * Focus on high performance
## TODO
  * Write tests con make sure everything keeps working whenever making changes.
## API
        // There are 2 ways to get resulting data from channels:
        // Using events, like earlier versions:
        //   data takes each sentence one at a time.
        //   done takes an entire result from last command.
        // Using Streams channel and connection provides access to several layers of them.
        //   Channels filter only data for that channel
        //      data: sentences that are data.
        //      trap: stream of traps. Useful for reading data streams using takeUntil(trapStream). Or for piping to notification on UI.
        //      bufferedSteam: when data response is "done" the buffered stream emits packets. Don't use this with a "listen" command.
        //      read: every sentence passes through this one.
        //   Connections also have streams, where they do not filter per channel:
        //      raw: The raw socket data. This emits buffers.
        //      sentence:each raw sentence is emitted from this stream
        //      read: the parsed sentences this is similar to the Channel read stream except does not filter by channel id.
        //      trap: all traps
### Connection
  Calling new MikroNode(host[,port,socketTimeout]) returns an object representing the device.
```javascript
    var MikroNode = require('mikronode');
    var Device =new MikroNode(host,port);
    Device.connect().then(([login])=>login('admin','password')).then(function(conn) { 
        var chan=conn.openChannel();
    });
```
With the above code, the following is API description. conn is Connection object, chan is Channel object.
  * MikroNode.resultsToObj(dataObj) <Object|Array>
      Convert the sentence format of the mikrotik into a more easily readable
  * Device.connect([cb]) <Promise>
      Connect to the target device. The optional callback function is called after successful connect with the function to call to login as the 2nd parameter, and any connection errors as the first.
      the connect method returns a Promise that is resolved when connecting.
  * Device.socketOpts (write-only property)
      Optionally allows the setting of parameters that the socket connecting to the mikrotik will use.
  * Device.TLS(tlsOpts)
      Enable TLS and set it's options. Take note that you will need to be sure the port the API is trying to connect is an SSL/TLS port. For unauthenticated SSL connections (no signed certs) only ADH cipher is supported. This is a limitation of the RouterOS software
  * Device.setDebug(level)
      Set the default debug logging level for the device, and all subsequent created connections.
  * conn.openChannel(id|name)  <Channel>
      Open and return a new channel object. Each channel is a unique command line to the mikrotik, allowing simultaneous execution of commands. The ID parameter is optional. If not specified, the current timestamp is used. If too many channels are opened at one time without specifying a name, there could be duplicate names.  * conn.connected()
      Returns true is currently connected to a mikrotik device.
  * conn.closeChannel(id)  
      Closes an open channel. This will call the close method of the channel object.
  * conn closeOnDone(b)  
      If b == true, when a done event occurs, close the connection after all channels have been closed.
  * conn.close(force)  
      Close the connection. If force is true, force close of any open channels then close this connection.
  * conn.getHost()
  * conn.getUser()
### Channel
  The following property/methods are available for channels:
  * channel.done <Observable>
      "done" is the stream that contains events when the done sentence comes from the device.
      When subscribing, the stream's data contans an object with each line received in an array.
  * channel.data <Observable>
      For each sentence received, this has an observable event. Only sentences designated for this channel will pass through this sentence.
      This is handy when following trailing output from a listen command, where the data could be endless.
  * channel.trap <Observable>
      Any traps that occur on a channel can be captured in this observable stream.
  * chanenl.sync(b)
      If b == true, each command is run synchronously. Otherwise commands are executed as they are passed.
  * channel.closeOnDone(b)
      If b == true, when a done event occurs, close the channel after all commands queued have been executed.
  * channel.getId()
  * channel.write(lines[,optionsObject]) <Promise>
      Returns a promise that is resolved when the command sent is complete and is "done"
      The promise is rejected if a trap or fatal error occurs.
      Lines can be a string, or an array of strings. If it is a string, then it is split on the EOL character and each resulting line is sent as a separate word (in API speak)
      If lines is an array, then each element is sent unaltered.
      If lines is a string and optionsObject is provided, the optionsObject is converted to standard sentence output: =propertyName=propertyValue
  * channel.close(force)
      Close the channel. If there are any commands still waiting to be executed, they will be completed before closing the channel.  
      If force is TRUE, then the channel is immediately closed. If the channel is running, the cancel command is sent to stop any running listen commands, or potentially long running output.
## Examples
### Connect to a Mikrotik, and add an address to ether1
```javascript
     var api = require('mikronode');
     var device = new api('192.168.0.1');
     device.connect().then(([login])=>login('admin','password')).then(function(conn) {
        var chan=conn.openChannel();
        chan.write('/ip/address/add',{'interface':'ether1','address':'192.168.1.1'});
        chan.on('trap',function(data) {
            console.log('Error setting IP: '+data);
        });
        chan.on('done',function(data) {
            console.log('IP Set.');
        });
        chan.close();
        conn.close();
     });
```
### Writing the program for the example API conversation on the [Mikrotik Wiki](http://wiki.mikrotik.com/wiki/API#.2Fcancel.2C_simultaneous_commands)
```javascript
     var MikroNode = require('mikronode');
     var device = new MikroNode('192.168.0.1');
     device.connect().then(([login])=>login('admin','password')).then(function(conn) {
        conn.closeOnDone(true); // when all channels are "done" the connection should close.
        var chan1=conn.openChannel("interface_listener");
        chan1.write('/interface/listen');
        chan1.data.subscribe(function(item) {
            var packet=MikroNode.resultsToObj(item.data);
            console.log('Interface change: '+JSON.stringify(packet));
        });
        // This should be called when the cancel is called below. (trap occurs first, then done)
        chan1.done.subscribe(function(packet) {
            // This should output everything that the above outputted.
            packet.data.forEach(function(data) {
                var packets=MikroNode.resultsToObj(data);
                console.log('Interface: '+JSON.stringify(packet));
            });
        });
        var chan2=conn.openChannel('config_interface');
        // added closeOnDone option to this call
        var chan3=conn.openChannel('enable_interface'); // We'll use this later.
        var chan4=conn.openChannel('getall_interfaces'); 
        chan2.write('/interface/set',{'disabled':'yes','.id':'ether1'});
        chan2.done.subscribe(function(items) {
            // We do this here, 'cause we want channel 4 to write after channel 3 is done.
            // No need to listen for channel3 to complete if we don't care.
            chan3.write('/interface/set',{'disabled':'no','.id':'ether1'});
            chan4.write('/interface/getall');
            // Alternative (legacy) way of caturing when chan4 is done.
            chan4.on('done',function(packet) {
                packet.data.forEach(function(data) {
                    var packets=MikroNode.resultsToObj(data);
                    console.log('Interface: '+JSON.stringify(packet));
                });
                chan1.close(); // This should call the /cancel command to stop the listen.
            });
        });
    });
```
### Simplifying the above by reducing the number of channels.
  Notice how the callback embedding is not needed using the syncronous capability.
```javascript
    var MikroNode = require('mikronode');
    var device = new MikroNode('192.168.0.1');
     device.connect().then(([login])=>login('admin','password')).then(function(conn) {
        conn.closeOnDone(true); // All channels need to complete before the connection will close.
        var listenChannel=conn.openChannel();
        listenChannel.write('/interface/listen');
        // Each sentence that comes from the device goes through this.
        listenChannel.read.subscribe(function(data) {
            var packet=MikroNode.resultsToObj(data);
            console.log('Interface change: '+JSON.stringify(packet));
        });
        var actionChannel=conn.openChannel();
        actionChannel.sync(true);
        // These will run synchronsously
        actionChannel.write('/interface/set',{'disabled':'yes','.id':'ether1'});
        actionChannel.write('/interface/set',{'disabled':'no','.id':'ether1'});
        actionChannel.write('/interface/getall');
        actionChannel.on('done',function(packet) {
            packet.data.forEach(function(data) {
                var packets=MikroNode.resultsToObj(data);
                console.log('Interface: '+JSON.stringify(packet));
            });
            listenChannel.close(); // This should call the /cancel command to stop the listen.
        });
        actionChannel.close(); // The above commands will complete before this is closed.
    });
```
### Promises add simplicity:
```javascript
    var MikroNode = require('mikronode');
    var device = new MikroNode('192.168.0.1');
    device.connect().then(([login])=>login('admin','password')).then(function(conn) {
        console.log("Logged in.");
        conn.closeOnDone(true); // All channels need to complete before the connection will close.
        var listenChannel=conn.openChannel("listen");
        // Each sentence that comes from the device goes through the data stream.
        listenChannel.data.subscribe(function(data) {
            // var packet=MikroNode.resultsToObj(data);
            console.log('Interface change: ',JSON.stringify(data));
        },error=>{
            console.log("Error during listenChannel subscription",error) // This shouldn't be called.
        },()=>{
            console.log("Listen channel done.");
        });
        // Tell our listen channel to notify us of changes to interfaces.
        listenChannel.write('/interface/listen').then(result=>{
            console.log("Listen channel done promise.",result);
        })
        // Catch shuold be called when we call /cancel (or listenChannel.close())
        .catch(error=>console.log("Listen channel rejection:",error));
        // All our actions go through this.
        var actionChannel=conn.openChannel("action",false); // don't close on done... because we are running these using promises, the commands complete before each then is complete.
        // Do things async. This is to prove that promises work as expected along side streams.
        actionChannel.sync(false);
        actionChannel.closeOnDone(false); // Turn off closeOnDone because the timeouts set to allow the mikrotik to reflect the changes takes too long. The channel would close.
        // These will run synchronsously (even though sync is not set to true)
        console.log("Disabling interface");
        actionChannel.write('/interface/set',{'disabled':'yes','.id':'ether1'}).then(results=>{
            console.log("Disable complete.");
            // when the first item comes in from the listen channel, it should send the next command.
            const {promise,resolve,reject}=MikroNode.getUnwrappedPromise();
            listenChannel.data
                .take(1)
                // This is just to prove that it grabbed the first one.
                .do(d=>console.log("Data:",MikroNode.resultsToObj(d.data)))
                .subscribe(d=>actionChannel.write('/interface/set',{'disabled':'no','.id':'ether1'}).then(resolve,reject));
            return promise;
        })
        .then(results=>{
            console.log("Enabled complete.");
            // return new Promise((r,x)=>setTimeout(r,1000)).then(()=>actionChannel.write('/interface/getall'));
            const {promise,resolve,reject}=MikroNode.getUnwrappedPromise();
            // when the second item comes in from the listen channel, it should send the next command.
            listenChannel.data
                .take(1)
                // This is just to prove that it grabbed the second one.
                .do(d=>console.log("Data:",MikroNode.resultsToObj(d.data)))
                .subscribe(d=>actionChannel.write('/interface/getall').then(resolve,reject));
            return promise;
        })
        .then(results=>{
            var formatted=MikroNode.resultsToObj(results.data);
            var columns=[".id","name","mac-address","comment"];
            var filtered=formatted.map(line=>columns.reduce((p,c)=>{p[c]=line[c];return p},{}));
            console.log('Interface [ID,Name,MAC-Address]: ',JSON.stringify(filtered,true,4));
        })
        .catch(error=>{
            console.log("An error occurred during one of the above commands: ",error);
        })
        // This runs after all commands above, or if an error occurs.
        .then(nodata=>{
            console.log("Closing everything.");
            listenChannel.close(true); // This should call the /cancel command to stop the listen.
            actionChannel.close();
        });
    });
```
### The methods *decodeLength* and *encodeString* were written based on code [here on the Mikrotik Wiki](http://wiki.mikrotik.com/wiki/API_PHP_class#Class).
## License
(The MIT License)
Copyright (c) 2011,2012,2013,2014,2015,2016,2017 Brandon Myers <trakkasure@gmail.com>
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
================================================

File: Channel.js
================================================
import util from 'util';
import events from 'events';
import {Observable, Subject, Scheduler} from 'rxjs';
import {DEBUG, CONNECTION, CHANNEL, EVENT} from './constants.js';
import {resultsToObj,getUnwrappedPromise} from './Util.js';
// console.log2=console.log;
// console.log=function(...args) {
//     const stack=new Error().stack.split('\n');
//     const file = (stack[2].match(/\(([^:]+:\d+)/)||['',''])[1].split("/").pop()+": "+typeof args[0]==="string"?args.shift():'';
//     console.log2(file,...args);
// }
export default class Channel extends events.EventEmitter {
    /** ID of the channel. 
     * @private
     * @instance
     * @member {boolean} id
     * @memberof Channel
    **/
    @Private
    id;
    /** Current channel status. See Constants for list of channel status (CHANNEL)
     * @private
     * @instance
     * @member {boolean} id
     * @memberof Channel
    **/
    @Private
    status=CHANNEL.OPEN;
    /** ID of the channel. 
     * @private
     * @instance
     * @member {boolean} id
     * @memberof Channel
    **/
    @Private
    closed=false;
    /** In/Out stream object for this channel.
     * @private
     * @instance
     * @member {Object} stream
     * @memberof Channel
    **/
    @Private
    stream;
    /** Current Debug level for this channel.
     * @private
     * @instance
     * @member {int} debug
     * @memberof Channel
    **/
    @Private
    debug=DEBUG.NONE;
    /** If whether to call close on this channel when done event occurs, and there are no commands in the queue to run.
     * @private
     * @instance
     * @member {boolean} closeOnDone
     * @memberof Channel
    **/
    @Private
    closeOnDone=true;
    /** If wether to call close on this channel when trap event occurs.
     * @private
     * @instance
     * @member {boolean} closeOnTrap
     * @memberof Channel
    **/
    @Private
    closeOnTrap=false;
    /** The buffered stream. Used to hold all results until done or trap events occur.
     * @private
     * @instance
     * @member {Observable} bufferedStream
     * @memberof Channel
    **/
    @Private
    bufferedStream;
    /** "data stream" for this channel. no other sentences execpt data sentences get to this point.
     * @private
     * @instance
     * @member {Observable} data
     * @memberof Channel
    **/
    @Private
    data;
    /** contains all sentences for this stream
     * @private
     * @instance
     * @member {Observable} read
     * @memberof Channel
    **/
    @Private
    read;
    /** Trap stream
     * @private
     * @instance
     * @member {Observable} trap
     * @memberof Channel
    **/
    @Private
    trap;
    /** write stream
     * @private
     * @instance
     * @member {Subject} write
     * @memberof Channel
    **/
    @Private
    write=new Subject();
    /** If commands should be synchronous.
     * @private
     * @instance
     * @member {boolean} sync
     * @memberof Channel
    **/
    @Private
    sync=true;
    /** Data buffer per command execution
     * @private
     * @instance
     * @member {Object} buffer
     * @memberof Channel
    **/
    @Private
    dataBuffer = {};
    /** Command buffer. All output commands go through this buffer.
     * @private
     * @instance
     * @member {Array} buffer
     * @memberof Channel
     */
    @Private
    buffer = [];
    @Private
    cmdCount = 0;
    /**
      * Command ID tracking.
      * @private
      * @instance
      * @member {Object}
      * @memberof Channel
      */
    @Private
    cmd = {};
    @Private
    done;
    /** 
      * Create new channel on a connection. This should not be called manually. Use Connection.openChannel
      * @constructor
      * @param {string|number} id ID of the channel
      * @param {object} stream stream object representing link to connection.
      * @param {number} debug The debug level.
      * @param {boolean} closeOnDone If the channel should close itself when the next done event occurs, and there are no more commands to run.
      */
    constructor(id,stream,debug,closeOnDone) {
        super();
        this.debug=debug;
        this.debug&DEBUG.SILLY&&console.log('Channel::New',[].slice.call(arguments));
        this.closeOnDone=(typeof closeOnDone===typeof true)?closeOnDone:this.closeOnDone;
        this.id=id; // hold a copy.
        if(this.status&(CHANNEL.CLOSING|CHANNEL.CLOSED)) return; // catch bad status
        this.stream = stream; // Hold a copy
        // Stream for reading everything.
        this.read = stream.read.takeWhile(data=>!(this.status&CHANNEL.CLOSED))
            .do(e=>this.debug>=DEBUG.SILLY&&console.log('Channel (%s)::%s Sentence on channel ',e.tag))
            .flatMap(data=>{
                const cmd=this.getCommandId(data);
                const d={...data,tag:data.tag.substring(0,data.tag.lastIndexOf('-')),cmd:(this.getCommand(cmd)||{cmd:null}).cmd};
                if (d.type==EVENT.DONE_RET||d.type===EVENT.DONE_RET_TAG) {
                    d.data=d.data;
                    const d2={...d,type:EVENT.DATA};
                    return Observable.of(d2).concat(Observable.of(d));
                }
                return Observable.of(d);
            }).share();
        // Stream for sentences with data.
        this.data = this.createStream(this.read,[EVENT.DATA,EVENT.DATA_RET,EVENT.DATA_RET_TAG]).share();
        // Stream for signaling when done.
        this.done = this.createStream(this.read,[EVENT.DONE,EVENT.DONE_RET,EVENT.DONE_TAG]).share();
        // Stream for all traps from device.
        this.trap=this.read
            .filter(e=>e.type==EVENT.TRAP||e.type===EVENT.TRAP_TAG)
            .do(e=>this.debug>=DEBUG.DEBUG&&console.log('Channel (%s)::TRAP ',id))
            .share();
        this.read.filter(e=>e.type==EVENT.FATAL)
            .subscribe(e=>{
                this.debug>=DEBUG.DEBUG&&console.log('Channel (%s)::FATAL ',id);
                this.status=CHANNEL.CLOSING;
                this.close();
            });
        this.bufferedStream=new Subject();
    }
    /**
     * 
     * @param {string} command The command to write to the device on this channel.
     * @param {*} args Arguments to pass as part of the command.
     */
    write(command,args=[]) {
        if (this.status&(CHANNEL.CLOSED|CHANNEL.CLOSING)) {
            this.debug>=DEBUG.WARN&&console.error("Cannot write on closed or closing channel");
            const p = new Promise((resolve,reject)=>reject({tag:this.id,data:{message:"Cannot write on closed or closing channel"},cmd:{command,args}}));
            // p.catch(e=>{console.error(e.data.message)});
            return p;
        }
        if (command==='/cancel') {
            Object.keys(this.cmd).forEach(id=>{
                this.stream.write(command,args,id);
            });
            return Promise.resolve({tag:this.id,data:{message:"/cancel sent."}});
        }
        const {promise,resolve,reject}=getUnwrappedPromise();
        promise.resolve=resolve;
        promise.reject=reject;
        // Add the command to the registry.
        const cmd=this.registerCommand(command,args,promise);
        const commandId=cmd.id;
        promise.cmd=cmd;
        if ((Object.keys(this.cmd).length-1)==0 && !(this.sync&&this.status&CHANNEL.RUNNING)) {
                // console.log("There are no commands in the buffer, but channel is in running state while sync enabled.");
            this.status=CHANNEL.RUNNING;
            this.debug>=DEBUG.INFO&&console.log("Writing on channel %s",this.id,command,args);
            this.stream.write(command,args,commandId);
        } else {
            const last=this.lastCommand(commandId);
            // If we are in sync mode, wait until the command is complete
            if (this.sync) last.promise.then(()=>{
                this.status=CHANNEL.RUNNING;
                this.stream.write(command,args,commandId);
            }).catch(()=>{
                this.stream.write(command,args,commandId);
            });
            // Otherwise since the last command was sent, we can send this one now.
            else {
                this.status=CHANNEL.RUNNING;
                this.stream.write(command,args,commandId);
            }
        }
        return promise;
    }
    /**
     * Clear the command from cache
     * @param {number} commandId 
     */
    @Private
    clearCommand(commandId) {
        if (typeof commandId === typeof {}) {
            if (commandId.cmd)
                return this.clearCommand(commandId.cmd.id);
            if (commandId.id)
                return this.clearCommand(commandId.id);
            return null;
        }
        this.debug>=DEBUG.DEBUG&&console.log("Clearing command cache for #",commandId);
        const cmd = this.cmd[commandId];
        if (!cmd) return;
        delete cmd.promise.cmd;
        delete cmd.promise.resolve;
        delete cmd.promise.reject;
        delete cmd.promise;
        delete this.cmd[commandId];
        if (!Object.keys(this.cmd).length) {
            if (this.closeOnDone) this.close();
        }
    }
    /**
     * Get the last command relative to the commandId
     * @param {number} commandId 
     */
    @Private
    lastCommand(commandId) {
        return this.cmd[commandId-1];
    }
    @Private
    getCommand(commandId) {
        if (!commandId) return null;
        if (typeof commandId===typeof {}) {
            if (commandId.cmd) return commandId.cmd;
            else return null;
        }
        return this.cmd[commandId];
    }
    /**
     * 
     * @param {string} command Command to send to device
     * @param {array} args Arguments for command
     * @param {object} promise object containing resolve and reject functions.
     */
    @Private
    registerCommand(command,args,promise) {
        this.cmdCount=this.cmdCount+1;
        const commandId=this.cmdCount;
        this.cmd[commandId]={id:commandId,cmd:{id:commandId,command,args},promise};
        (function(id,p){
            const race = Observable.race(
                this.done
                    .filter(
                        data=>data.cmd&&data.cmd.id===id
                    )
                    // .do(
                    //     d=>console.log("*** Done in %s:%s",d.cmd.id,id)
                    // )
                    .take(1)
              , this.trap
                    .filter(
                        data=>data.cmd&&data.cmd.id===id
                    )
                    // .do(
                    //     d=>console.log("*** Trap in %s:%s",d.cmd.id,id)
                    // )
                    .take(1)
            ).take(1);
            race.partition(data=>data.type==EVENT.TRAP||data.type===EVENT.TRAP_TAG)
                .reduce((r,o,i)=>{
                    if (i==0) {
                        o.subscribe(error=>{
                            this.debug>=DEBUG.DEBUG&&console.error("*** Register Command: trap",id,error);
                            this.status=CHANNEL.DONE;
                            if (this.closeOnTrap) {
                                this.status=CHANNEL.CLOSING;
                                this.debug>=DEBUG.DEBUG&&console.log('Channel (%s):: read-done catch CLOSING',this.id);
                                this.close(true);
                            }
                            p.reject(error);
                            this.emit('trap',error);
                        },null);
                    } else return o;
                },{})
            const isListen=command.split('/').indexOf('listen')>0;
            this.data
                .filter(data=>data.cmd.id===id)
                .takeUntil(race)
                .do(d=>this.debug>=DEBUG.SILLY&&console.log("*** Data in %s:%s",d.cmd.id,id))
                .reduce((acc,d)=>{
                    if (d.data&&!isListen) acc.data=acc.data.concat([d.data]);
                    return acc;
                },{cmd:this.cmd[id].cmd,tag:this.id,data:[]})
                .do(d=>this.debug>=DEBUG.SILLY&&console.log("*** Reduced Data in ",d))
                .takeUntil(race.filter(data=>data.type==EVENT.TRAP||data.type===EVENT.TRAP_TAG))
                .subscribe(data=>{
                    this.debug>=DEBUG.SILLY&&console.log("*** Register Command: subscribe",id,data);
                    this.status=CHANNEL.DONE;
                    this.bufferedStream.next(data);
                    p.resolve(data);
                    this.emit('done',data);
                },
                error=>{
                    this.debug>=DEBUG.SILLY&&console.error("*** Register Command: error",id,error);
                },
                // this should happen for every command
                ()=>{
                    this.debug>=DEBUG.SILLY&&console.log("*** Register Command: complete",commandId);
                    setTimeout(()=>this.clearCommand(id),50); // make sure all promises complete before running this.
                });
        }.bind(this))(commandId,promise);
        return this.cmd[commandId].cmd;
    }
    /**
     * Create a stream filtered by list of event types.
     * @param {Observable} stream The stream representing the incoming data
     * @param {Array} events list of events to filter by
     * @return {Observable} The incoming stream filtered to only the packets having data.
     */
    createStream(stream,events) {
        return this.read
                   .filter(e=>events.indexOf(e.type)!=-1)
                   .do(e=>this.debug>=DEBUG.DEBUG&&console.log('Channel (%s)::%s flatMap',e.tag,e.type))
                   .flatMap(d=>{
                       return Observable.of(d);
                       // this.dataBuffer[d.cmd.id].push(d.data);
                   });
    }
    /**
     * 
     * @param {Object} data Sentence object from read stream
     * @return {String} Command ID of sentence.
     */
    getCommandId(data) {
        if (!data) return null;
        if (typeof data === typeof {})
            return this.getCommandId(data.tag);
        return data.substring(data.lastIndexOf('-')+1);
    }
    // status() { return this.status }
    close(force) { 
        if (this.status&CHANNEL.RUNNING) {
            if (force)
                Object.keys(this.cmd).forEach(id=>{
                    this.stream.write('/cancel',[],id);
                });
            this.closeOnDone=true;
            this.sync=true;
            this.status=CHANNEL.CLOSING;
            return;
        }
        if (this.status&CHANNEL.CLOSED) return;
        this.status=CHANNEL.CLOSED;
        this.debug>=DEBUG.INFO&&console.log('Channel (%s)::CLOSED',this.id);
        this.bufferedStream.complete();
        this.stream.close();
        this.removeAllListeners(EVENT.DONE);
        this.removeAllListeners(EVENT.DATA);
        this.removeAllListeners(EVENT.TRAP);
    }
    /** Data stream returns each sentence from the device as it is received. **/
    get data() {
        return this.data;
    }
    /** Done stream buffers every sentence and returns all sentences at once.
        Don't use this stream when "listen"ing to data. Done never comes on a watch/listen command.
        A trap signals the end of the data of a listen command.
     **/
    get done() {
        return this.bufferedStream;
    }
    /** When a trap occurs, the trap sentence flows through this stream **/
    get trap() {
        // TRAP_TAG is the only one that *should* make it here.
        return this.trap;
    }
    /** This is the raw stream. Everything for this channel comes through here. **/
    get stream() {
        return this.read;
    }
    /**
     * Get the current status of this channel.
     * @return The status code
     */
    get status() {
        return this.status;
    }
    /**
     * Commands are sent to the device in a synchronous manor. This is enabled by default.
     * @param {sync} sync If passed, this sets the value of sync.
     * @return If sync parameter is not passed, the value of sync is returned. Otherwise this channel object is returned.
     */
    sync(...args) {
        if (args.length) {
            this.sync=!!args[0];
            return this;
        }
        return this.sync;
    }
    /**
     * 
     * @param {Observable} stream Take incoming commands to write to this channel from the provided stream. The channel will stop taking commands if a fatal error occurs, or if the channel is closing or closed.
     * 
     */
    pipeFrom(stream) {
        if (this.status&(CHANNEL.DONE|CHANNEL.OPEN)) {
            this.status=CHANNEL.RUNNING;
            stream.takeWhile(o=>!(this.status&(CHANNEL.FATAL|CHANNEL.CLOSING|CHANNEL.CLOSED))).subscribe(
                d=>this.write(d),
                ()=>{
                    this.status=CHANNEL.DONE;
                    this.stream.close();
                },
                ()=>{
                    this.status=CHANNEL.DONE;
                    this.stream.close();
                }
            );
        }
    }
    getId(){return this.id}
    on(event,func) {
        const ret=super.on(event,func);
        this.setupEventSubscription(event,this.getStreamByEventType(event));
        return ret;
    }
    addEventListener(event,func) {
        const ret=super.addEventListener(event,func);
        this.setupEventSubscription(event,this.getStreamByEventType(event));
        return ret;
    }
    once(event,func) {
        const ret=super.once(event,func);
        this.setupEventSubscription(event,this.getStreamByEventType(event));
        return ret;
    }
    /**
     * @param {String} event The event name to map to an observable stream.
     * @return Observable stream.
     */
    @Private
    getStreamByEventType(event) {
        switch(event) {
            case EVENT.DONE:
                return this.bufferedStream;
            case EVENT.TRAP:
                return this.trap;
            case EVENT.FATAL:
                return this.fatal;
            default:
                return this.read;
        }
    }
    /**
     * @param {String} event The name of the event to setup for emitting.
     * @param {Observable} stream The stream to listen for events.
     * @return {Observable} Stream that will send out a copy of its input as long as there are event callbacks for the event requested.
     */
    @Private
    setupEventSubscription(event,stream) {
        if (this.listeners(event)) return;
        // take from the stream until there are no more event listeners for that event.
        const listenerStream = stream.takeWhile(o=>!this.listeners(event));
        listenerStream.subscribe(e=>{
            this.emit(event,e);
        });
        return listenerStream;
    }
    /** When the done sentence arrives, close the channel. This only works in synchronous mode. **/
    closeOnDone(...args) { 
        if (args.length)
            this.closeOnDone=!!args[0];
        else this.closeOnDone;
        return this;
    }
    /** If trap occurs, consider it closed. **/
    closeOnTrap(...args)  {
        if (args.length)
            this.closeOnTrap=!!args[0];
        else return this.closeOnTrap;
        return this;
    }
}
================================================

File: Connection.js
================================================
import util from 'util';
import events from 'events';
import {Subject, Observable} from 'rxjs';
import {autobind} from 'core-decorators';
import {STRING_TYPE, DEBUG, CONNECTION, CHANNEL, EVENT} from './constants.js';
import Channel from './Channel';
export default class Connection extends events.EventEmitter {
    @Private
    status=CONNECTION.NONE;
    @Private
    channels=[];
    @Private
    stream;
    @Private
    debug=DEBUG.NONE;
    @Private
    closeOnDone=false;
    constructor(stream,loginHandler,p) {
        super();
        const login=stream.read
            // .do(d=>console.log("Sentence: ",d))
            .takeWhile(o=>this.status!==CONNECTION.CONNECTED).share();
        this.stream=stream;
        const rejectAndClose = d=>{
            p.reject(d);
            this.close();
        };
        login.filter(d=>d.type===EVENT.TRAP)
             .do(t=> {
                this.emit('trap',t.data)
                this.debug&&console.log('Trap during login: ',t.data);
              }).map(t=>t.data)
             .subscribe(rejectAndClose,rejectAndClose);
        login.filter(d=>d.type===EVENT.DONE_RET)
             .subscribe(data=>{
                this.status=CONNECTION.CONNECTING;
                this.debug>=DEBUG.DEBUG&&console.log("Got done_ret, building response to ",data);
                var a=data.data.split('');
                var challenge=[];
                while(a.length) challenge.push(parseInt("0x"+a.shift()+a.shift()));
                this.debug>=DEBUG.DEBUG&&console.log('Challenge length:'+challenge.length);
                if (challenge.length!=16) {
                    this.status=CONNECTION.ERROR;
                    this.debug>=DEBUG.WARN&&console.log(this.status);
                    stream.sentence.error('Bad Connection Response: '+data);
                } else {
                    loginHandler(challenge);
                }
             });
        login.filter(d=>d.type===EVENT.DONE)
             .subscribe(d=>{
                this.status=CONNECTION.CONNECTED;
                this.debug>=DEBUG.INFO&&console.log('Login complete: Connected');
                p.resolve(this);
              },
              rejectAndClose,
              ()=>{
                this.debug>=DEBUG.DEBUG&&console.log("Login stream complete");
              }
             );
        stream.read
        .subscribe(null,null,e=>{
          this.channels.forEach(c=>c.close(true));
          setTimeout(()=>{
            this.emit('close',this);
          },50)
        });
    }
    close() {
      this.debug>=DEBUG.SILLY&&console.log("Closing connection through stream");
      this.emit('close',this);
      this.stream.close();
    }
    /*
     * @deprecated use debug(level)
     */
    setDebug(d) {
      this.debug=d;
      return this;
    }
    debug(...args) {
      if (args.length) 
        this.debug=args[0];
      else return this.debug;
      return this;
    }
    /** If all channels are closed, close this connection */
    closeOnDone(...args) {
      if (args.length) 
        this.closeOnDone=!!args[0];
      else return this.closeOnDone;
      return this;
    }
    getChannel(id) {
      return this.channels.filter(c=>c.getId()==id)[0];
    }
    get connected() {
      return !!(this.status&(CONNECTION.CONNECTED|CONNECTION.WAITING|CONNECTION.CLOSING));
    }
    @autobind
    openChannel(id,closeOnDone) {
        this.debug>=DEBUG.SILLY&&console.log("Connection::OpenChannel");
        if (!id) {
            id=+(new Date());
        } else {
            if (this.channels.some(c=>c.getId()===id)) throw('Channel already exists for ID '+id);
        }
        this.debug>=DEBUG.SILLY&&console.log("Creating proxy stream");
        const matchId=RegExp("^"+id+"-");
        let s = {
          "read": this.stream.read
                      .filter(e=>matchId.test(e.tag)),
          "write": (d,args,cmdTrack=0) => {
              if (typeof(d)===STRING_TYPE)
                d=d.split("\n");
              if (Array.isArray(d)&&d.length) {
                d.push(`.tag=${id}-${cmdTrack}`);
                return this.stream.write(d,args);
              }
              else return;
          },
          "close": ()=>{
              var channel=this.getChannel(id);
              if (channel) {
                this.debug>=DEBUG.DEBUG&&console.log("Closing channel ",id);
                setTimeout(channel.emit.bind(channel,'close',channel),50);
                this.channels.splice(this.channels.indexOf(channel),1);
                if (this.channels.filter(c=>c.status&(CHANNEL.OPEN|CHANNEL.RUNNING)).length===0 && this.closeOnDone) this.close(); 
              } else
                this.debug>=DEBUG.WARN&&console.log("Could not find channel %s when trying to close",id);
          },
          "done": ()=>{
              // If Connection closeOnDone, then check if all channels are done.
              if (this.closeOnDone) {
                  const cl=this.channels.filter(c=>c.status&(CHANNEL.OPEN|CHANNEL.RUNNING));
                  if (cl.length) return false;
                  this.debug>=DEBUG.DEBUG&&console.log("Channel done (%s)",id);
                  this.channels.filter(c=>c.status&(CHANNEL.DONE)).forEach(c=>console.log("Closing...",c));
                  return true;
              }
              return false;
          }
        };
        var c;
        this.debug>=DEBUG.INFO&&console.log("Creating channel ",id);
        this.channels.push((c=new Channel(id,s,this.debug,closeOnDone)));
        this.debug>=DEBUG.INFO&&console.log("Channel %s Created",id);
        return  c;
    }
}
================================================

File: constants.js
================================================
const STRING_TYPE=typeof "";
const DEBUG = {
    NONE:0
  , ERROR:1
  , WARN:2
  , INFO:4
  , DEBUG:8
  , SILLY:16
};
const connectionLabels = {
    DISCONNECTED:"Disconnected" // Disconnected from device
  , ERROR:"Error" // ERROR defined above means a connect or transport error.
  , CONNECTING:"Connecting"   // Connecting to device
  , CONNECTED:"Connected"    // Connected and idle
  , WAITING:"Waiting"      // Waiting for response(s)
  , CLOSING:"Closing" 
  , CLOSED:"Closed" 
};
const CONNECTION = {
    DISCONNECTED:0
  , CONNECTING:1
  , CONNECTED:2
  , WAITING:4
  , CLOSING:8
  , CLOSED:16
  , ERROR: 32
};
const CHANNEL = {
    NONE:0
  , OPEN : 1
  , CLOSED : 2
  , CLOSING : 4
  , RUNNING : 8
  , DONE:16
};
const EVENT = {
    TRAP: 'trap'
  , TRAP_TAG: 'trap_tag'
  , DONE: 'done'
  , DONE_RET: 'done_ret'
  , FATAL: 'fatal'
  , FATAL_TAG: 'fatal_tag'
  , TAG: 'tag'
  , DONE_RET_TAG: 'done_ret_tag'
  , DONE_TAG: 'done_tag'
  , RE: 're'
  , DATA: 'data'  // This is an artifical event, not one from the API
};
export {STRING_TYPE, DEBUG, CONNECTION, CHANNEL, EVENT, connectionLabels};
================================================

File: index.js
================================================
import util from 'util';
import net from 'net';
import TLS from 'tls';
import Promise from 'promise';
import {Subject, Observable} from 'rxjs';
import {autobind} from 'core-decorators';
import crypto from 'crypto';
import dns from 'dns';
import {hexDump, decodePacket, encodeString, objToAPIParams, resultsToObj, getUnwrappedPromise} from './Util.js';
import {STRING_TYPE, DEBUG, CONNECTION,CHANNEL,EVENT} from './constants.js';
import parser from './parser.js';
import Connection from './Connection';
const Socket=net.Socket;
const nullString=String.fromCharCode(0);
class MikroNode {
    /** Host to connect */
    @Private
    host;
    /** Port to connect */
    @Private
    port;
    /** Debug Level */
    @Private
    debug=DEBUG.NONE;
    /** Timeout for connecting. */
    @Private
    timeout;
    /** Socket connected to mikrotik device */
    @Private
    sock;
    @Private
    status=CONNECTION.DISCONNECTED;
    @Private
    tls=null;
    @Private
    socketOpts={};
    @Private
    socketProto='tcp4';
/**
 * Creates a MikroNode API object.
 * @exports mikronode
 * @function
 * @static
 * @param {string} host - The host name or ip address
 * @param {number} [port=8728] - Sets the port if not the standard 8728 (8729 for
 *           TLS).
 * @param {number} [timeout=0] - Sets the socket inactivity timeout. A timeout
 *           does not necessarily mean that an error has occurred, especially if you're
 *           only listening for events.
 * @param {(object|boolean)} [options.tls] - Set to true to use TLS for this connection.
 *           Set to an object to use TLS and pass the object to tls.connect as the tls
 *           options. If your device uses self-signed certificates, you'll either have to
 *           set 'rejectUnauthorized : false' or supply the proper CA certificate. See the
 *           options for
 *           {@link https://nodejs.org/api/tls.html#tls_tls_connect_port_host_options_callback|tls.connect()}
 *           for more info.
 * @throws <strong>WARNING: If you do not listen for 'error' or 'timeout' events and one
 *            occurrs during the initial connection (host unreachable, connection refused,
 *            etc.), an "Unhandled 'error' event" exception will be thrown.</strong>
 * 
 * @example
 * 
 * <pre>
 * var MikroNode = require('mikronode');
 * 
 * var device1 = new MikroNode('192.168.88.1')
 * var device2 = new MikroNode('192.168.88.2')
 * var promise1 = Observable.fromPromise(device1.connect('admin', 'mypassword'));
 * var promise2 = Observable.fromPromise(device2.connect('admin', 'mypassword'));
 *
 *  // When connected to both servers.
 *  Observable.zip(promise1,promise2).subscribe(function(connections) {
 *      connections[0].closeOnDone(true); // Set close on done for the connection. All channels must be done before this will issue done.
 *      connections[1].closeOnDone(true);
 *      var channel1=connections[0].openChannel(null,true); // choose chanel number for me, close chanel on done.
 *      var channel2=connections[1].openChannel(null,true); // choose chanel number for me, close chanel on done.
 *      // Everything is an observable stream now. Much more powerful
 *      channel1.data.merge(channel2.data).map(function(sentence){ return sentence; // do something cool mapping streams from both devices })
                .filter(function(sentence){ return sentence.type!='trap'}) // filter out traps. We could split off the stream and handle it somewhere else.
 *              .subscribe(function(sentence){ console.log(sentence)}
 *  }
 * , null
 * , function(err)
 *     console.error('Error when connecting: ', err);
 *   });
 * 
 * </pre>
 */
    constructor(host,port=8728,timeout=5) {
        // const {debug,port,timeout}=opts;
        this.host=host;
        this.port=port;
        this.timeout=timeout;
    }
    /** Change debug level **/
    setDebug(debug) {
        this.debug=debug;
        if (this.sock) this.sock.setDebug(debug);
        if (this.connection) this.connection.setDebug(debug);
    }
    /** Change the port */
    setPort(port) {
        this.port=port;
    }
    /** get/set tls options for this connection */
    TLS(opts={}) {
        if (opts) {
            this.tls=opts;
            if (opts.host) this.host=opts.host;
            if (opts.port) this.port=opts.port;
            return this;
        }
        return this.tls;
    }
    set socketOpts(opts) {
        this.socketOpts=opts;
        if (opts.host) this.host=opts.host;
        if (opts.port) this.port=opts.port;
    }
    /** Set timeout for socket connecion */
    setTimeout(timeout) {
        this.timeout=timeout;
        this.sock.setTimeout(timeout);
    }
    /** Connect to remote server using ID and password */
    connect(arg1,arg2) {
        this.debug>=DEBUG.INFO&&console.log('Connecting to '+this.host);
        let cb;
        this.debug>=DEBUG.SILLY&&console.log('Creating socket');
        this.sock = new SocketStream(this.timeout,this.debug,this.tls?typeof this.tls===typeof {}?this.tls:{}:false);
        const stream=this.sock.getStream();
        if (typeof arg1===typeof {}) {
            this.socketOpts={...this.socketOpts,arg1};
            if (typeof arg1===typeof function(){})
                cb=arg2;
        } else if (typeof arg1===typeof function(){}) cb=arg1;
        const close=()=>this.sock.getStream().sentence.complete();
        const login=(user,password,cb)=>{
            this.debug>=DEBUG.DEBUG&&console.log('Logging in');
            stream.write('/login');
            const {promise,resolve,reject}=getUnwrappedPromise();
            // Create a connection handler
            this.connection=new Connection(
                {...stream,close},
                challenge=>{
                    const md5=crypto.createHash('md5');
                    md5.update(Buffer.concat([Buffer.from(nullString+password),Buffer.from(challenge)]));
                    stream.write([
                        "/login",
                        "=name="+user,
                        "=response=00"+md5.digest("hex")
                    ]);
                },{resolve,reject}
            );
            this.connection.setDebug(this.debug);
            promise.then(()=>{
                if (cb) cb(null,this.connection);
            },err=>{
                if (cb) cb(err,null);
            });
            return promise;
        };
        this.debug>=DEBUG.SILLY&&console.log('Creating promise for socket connect');
        const promise = new Promise((resolve,reject) => {
            this.debug>=DEBUG.SILLY&&console.log('Connecting to remote host. Detected %s',net.isIPv6(this.host)?'ipv6':net.isIPv4(this.host)?'ipv4':'DNS lookup');
            const fn=((net.isIPv4(this.host)||net.isIPv6(this.host))?((this.socketOpts.family=net.isIPv6(this.host)?6:4),(a,b)=>b(null,[a])):((this.socketOpts.family==6)?dns.resolve4:dns.resolve6));
            fn(this.host,(err,data)=>{
                if (err) {
                    return reject("Host resolve error: ",err);
                }
                // this.debug>=DEBUG.DEBUG&&console.log('Socket connect: ',{...this.socketOpts,...this.tls,host:this.host,port:this.port});
                this.sock.connect({
                    ...this.socketOpts,
                    ...this.tls,
                    host:data[0],
                    port:this.port
                }).then(([socketOpts,...args])=>{
                    this.debug>=DEBUG.DEBUG&&console.log('Connected. Waiting for login.');
                    // initiate the login process
                    resolve([login,socketOpts,...args]);
                    if (cb) cb(null,login,socketOpts,...args);
                    /* Initiate Login */
                    this.sock.getStream().sentence.take(1).subscribe(null,reject,null);
                }).catch(err=>{
                    if (cb) cb(err,null);
                    reject("Caught error in socket connect",err);
                });
                // reject connect promise if the socket throws an error.
            });
        });
        // Connect to the server.
        return promise;
    }
}
// Object.keys(DEBUG).forEach(k=>MikroNode[k]=DEBUG[k]);
const api=Object.assign(MikroNode,DEBUG);
export default Object.assign(api,{CONNECTION, CHANNEL, EVENT, resultsToObj, getUnwrappedPromise});
/** Handles the socket connection and parsing of infcoming data. */
/* This entire class is private (not exported) */
class SocketStream {
    @Private
    rawSocket;
    @Private
    socket;
    @Private
    status=CONNECTION.NONE;
    @Private
    debug=DEBUG.NONE;
    @Private
    sentence$
    @Private
    parsed$;
    @Private
    data$;
    constructor(timeout,debug,tls) {
        debug>=DEBUG.DEBUG&&console.log('SocketStream::new',[timeout,debug]);
        this.debug=debug;
        this.rawSocket = new Socket();
        this.socket=tls?new TLS.TLSSocket(this.rawSocket,tls):this.rawSocket;
        this.sentence$=new Subject();
        // Each raw sentence from the stream passes through this parser.
        let holdBuffer=[];
        this.parsed$=this.sentence$
            .do(d=>this.debug>=DEBUG.SILLY&&console.log("Data to parse:",JSON.stringify(d)))
            .map(o=>o.map(x=>x.split("\r").join("\\r").split("\n").join("\\n")).join('\n')) // Make array string.
            .map(d=>{
                    if (holdBuffer.length) {
                        console.log("Hold buffer:",holdBuffer);
                        holdBuffer=[];
                    }
                    var s=parser.parse(d);
                    s.host=this.host;
                    return s;
            })
            .catch(e=>{
                holdBuffer=[];
                console.error("***************************************************************************");
                console.error("***************************************************************************");
                console.error("Error processing sentence:",e);
                console.error("Skipping and continuing");
                console.error("***************************************************************************");
                console.error("***************************************************************************");
                return this.parsed$;
            })
            .filter(e=>!!e)
            .flatMap(d=>{
                Object.keys(d).forEach(k=>{if(typeof d[k]==="string")d[k]=d[k].split("\\r").join("\r").split("\\n").join("\n")});
                return Observable.from(d);
            }) // break off observable from parse stream.
            .share(); // parse the string.
        // When we receive data, it is pushed into the stream defined below.
        this.data$=Observable.fromEvent(this.socket,'data');
        // this is the stream reader/parser.
        // My poor stream parser
        this.data$.scan((/* @type Buffer */ last,/* @type Buffer */stream,i)=>{
            let buff=Buffer.concat([last,stream]),end=0,idx=0,packet;
            this.debug>=DEBUG.DEBUG&&console.log("Packet received: ",stream.toString().split('\u0000'));
            this.debug>=DEBUG.DEBUG&&last.length>0&&console.log("Starting parse loop w/existing packet ",last.toString());
            while(idx<buff.length&&(end = buff.indexOf("\u0000",idx,"utf8")) !== -1 ) {
                this.debug>=DEBUG.SILLY&&console.log("Decoding: ",idx,end,buff.length,buff.slice(idx,end));
                packet=decodePacket(buff.slice(idx,end));
                idx=end+1;
                this.debug>=DEBUG.SILLY&&console.log('Detected end of sentence, posting existing sentence',packet);
                this.sentence$.next(packet);
            }
            return idx>=buff.length?Buffer.alloc(0):buff.slice(idx,buff.length);
        },Buffer.from([]))
        .subscribe(e=>this.debug>=DEBUG.DEBUG&&e.length&&console.log('Buffer leftover: ',e),closeSocket,closeSocket);
        this.socket.on('end',a => {
            this.debug>=DEBUG.INFO&&console.log('Connection end '+a);
            if (this.status==CONNECTION.CONNECTED)
                // Completing the sentence closes all downstream observables and completes any subscriptions.
                this.sentence$.complete();
                // this.handler.close(true);
        });
        this.socket.on('error',a => {
            this.debug>=DEBUG.ERROR&&console.log('Connection error: '+a);
            // Erroring the sentence closes all downstream observables and issues error any subscriptions.
            this.sentence$.error(a);
        });
        this.setTimeout(timeout);
        // This is the function handler for error or complete for the parsing functions.
        const closeSocket=(e)=>{
            this.debug>=DEBUG.DEBUG&&console.log("Closing Socket ",e);
            e?this.rawSocket.destroy(e):this.rawSocket.destroy();
        }
        /** Listen for complete on stream to dictate if socket will close */
        this.sentence$
            // .do(d=>console.log("Sentence: ",d))
            .subscribe(null,closeSocket,closeSocket);
        // This will be called if there is no activity to the server.
        // If this occurs before the login is successful, it could be
        // that it is a connection timeout.
        this.socket.setKeepAlive(true); 
        this.b=[];
        this.len=0;
        this.line='';
    }
    setDebug(d) {
        this.debug>=DEBUG.DEBUG&&console.log('SocketStream::setDebug',[d]);
        this.debug=d;
    }
    setTimeout(timeout) {
        this.debug>=DEBUG.DEBUG&&console.log('SocketStream::setTimeout',[timeout]);
        this.socket.setTimeout(timeout*1000,e=>{ // the socket timed out. According to the NodeJS api docs, right after this, it will be._closed.
            if (this.status!==CONNECTION.CONNECTED) {
                this.debug&&console.log('Socket Timeout');
                this.sentence$.error("Timeout: ",JSON.stringify(e));
                // self.emit('error','Timeout Connecting to host',self);
            }
        });
    }
    /** Connect the socket */
    connect(socketOpts) {
        this.debug>=DEBUG.DEBUG&&console.log('SocketStream::Connect %s',this.tls?"(TLS)":"",socketOpts);
        this.status=CONNECTION.CONNECTING;
        this.host = socketOpts.host||'localhost';
        return new Promise((res,rej)=>{
            // Connect to the socket. This works for both TLS and non TLS sockets.
            try {
                this.rawSocket.connect(socketOpts,(...args)=>{
                    this.debug>=DEBUG.INFO&&console.log('SocketStream::Connected ',args,socketOpts);
                    this.status=CONNECTION.CONNECTED;
                    socketOpts={
                        ...socketOpts,
                        localAddress:this.socket.localAddress,
                        localPort:this.socket.localPort
                    };
                    if (this.socket.encrypted)
                        res([{
                            ...socketOpts,
                            authorized:this.socket.authorized,
                            authorizationError:this.socket.authorizationError,
                            protocol: this.socket.getProtocol(),
                            alpnProtocol:this.socket.alpnProtocol,
                            npnProtocol:this.socket.npnProtocol,
                            cipher: this.socket.getCipher(),
                            cert: this.socket.getPeerCertificate(),
                        },...args]);
                    else res([socketOpts,...args]);
                });
            } catch (e) {
                rej("Caught exception while opening socket: ",e)
            }
        });
    }
    /** Provides access to all of the different stages of input streams and the write stream. */
    getStream() {
        return {sentence:this.sentence$,write:this.write,read:this.parsed$,raw:this.data$};
    }
    @autobind
    write(data,args) {
        if (args && typeof(args)===typeof({}))  {
            this.debug>=DEBUG.SILLY&&console.log("Converting obj to args",args);
            data=data.concat(Array.isArray(args)?args:objToAPIParams(args,data[0].split('/').pop()));
        }
        this.debug>=DEBUG.DEBUG&&console.log('SocketStream::write:',[data]);
        if (!this.socket||!(this.status&(CONNECTION.CONNECTED|CONNECTION.CONNECTING))) {
            this.debug>DEBUG.WARN&&console.log('write: not connected ');
            return;
        }
        if (typeof(data)===STRING_TYPE) data=[data];
        else if (!Array.isArray(data)) return;
        data.forEach(i => {
            try {
                this.debug>=DEBUG.DEBUG&&console.log('SocketStream::write: sending '+i);
                this.socket.write(encodeString(i,this.debug&DEBUG.SILLY));
            } catch(error) {
                this.sentence$.error(error);
            }
        });
        this.socket.write(nullString);
    }
}
================================================

File: Util.js
================================================
function encodeString(s,d) {
    var data = null;
    var len = Buffer.byteLength(s);
    var offset=0;
    if (len < 0x80) {
            data=new Buffer(len+1);
            data[offset++]=len;
    } else 
    if (len < 0x4000) {
            data=new Buffer(len+2);
            len |= 0x8000;
            data[offset++]=(len >> 8) & 0xff;
            data[offset++]=len & 0xff;
    } else
    if (len < 0x200000) {
            data=new Buffer(len+3);
            len |= 0xC00000;
            data[offset++]=(len >> 16) & 0xff;
            data[offset++]=(len >> 8) & 0xff;
            data[offset++]=len & 0xff;
    } else
    if (len < 0x10000000) {
            data=new Buffer(len+4);
            len |= 0xE0000000;
            data[offset++]=(len >> 24) & 0xff;
            data[offset++]=(len >> 16) & 0xff;
            data[offset++]=(len >> 8) & 0xff;
            data[offset++]=len & 0xff;
    } else {
        data=new Buffer(len+5);
        data[offset++]=0xF0;
        data[offset++]=(len >> 24) & 0xff;
        data[offset++]=(len >> 16) & 0xff;
        data[offset++]=(len >> 8) & 0xff;
        data[offset++]=len & 0xff;
    }
    data.utf8Write(s,offset);
    d&&console.log("Writing ",data);
    return data;
}
function decodePacket(data){
    if (!data.length) return [];
    const buf=[];
    let idx=0;
    while (idx<data.length) {
        let len;
        let b=data[idx++];
        if (b&128) { // Ported from the PHP API on the Wiki. Thanks
            if ((b&192)==128) {
                len=((b&63)<<8)+data[idx++];
            } else {
                if ((b & 224) == 192) {
                    len = ((b & 31) << 8 ) + data[idx++];
                    len = (len << 8 ) + data[idx++];
                } else {
                    if ((b & 240) == 224) {
                        len = ((b & 15) << 8 ) + data[idx++];
                        len = (len << 8 ) + data[idx++];
                        len = (len << 8 ) + data[idx++];
                    } else {
                        len = data[idx++];
                        len = (len << 8 ) + data[idx++];
                        len = (len << 8 ) + data[idx++];
                        len = (len << 8 ) + data[idx++];
                    }
                }
            }
        } else {
            len=b;
        } 
        // console.log("Pushing ",idx,len,data.slice(idx,idx+len));
        buf.push(data.slice(idx,idx+len).toString('utf8'));
        idx+=len;
    }
    return buf;
}
//hexDump=require('./hexdump');
function hexDump(data) {
    var hex=[]
    var cref=[];
    var i=0,j=0;
    for (j=0;j<data.length;j++) {
        i=j%8;
        //m=ctrl.indexOf(data[j]);
        if (data[j]<20||data[j]>126) cref[i]='.';
        else cref[i]=String.fromCharCode(data[j])
        hex[i]=Number(data[j]).toString(16);
        while (hex[i].length < 2) hex[i] = "0" + hex[i];
        if (hex.length==8) {
            console.log("%d: %s    %s",j-7,hex.join(' '),cref.join('') );
            hex=[];
            cref=[];
        }
    }
    if (i!=8) {
        console.log(hex.join(' ')+'    '+ cref.join('') )
        hex=[];
        cref=[];
    }
}
// This is probably over done...
// Uncomment if you want to detail trace your promises.
function nullfunc(){}
const rejectionWatcher=new WeakMap();
// function clearRejectionTrack(catcher,reason) {
//     const x=rejectionWatcher.get(this);
//     x.splice(x.findIndex(catcher),1);
//     return catcher.call(this,reason);
// }
// function proxyThenCatch(promise) {
//     const catchEx = promise.catch;
//     const thenEx = promise.then;
//     console.log("Adding promise to watcher map");
//     // rejectionWatcher.set(promise,[]);
//     promise.then=function(handler,catcher) {
//         if (catcher) {
//             // rejectionWatcher.get(promise).push(catcher);
//             console.log("tracking catcher");
//         }
//         return proxyThenCatch(thenEx.call(promise,handler,clearRejectionTrack.bind(promise,catcher)));
//     }.bind(promise);
//     promise.catch=function(catcher) {
//         if (!catcher) return;
//         // rejectionWatcher.get(promise).push(catcher);
//         return proxyThenCatch(catchEx.call(promise,catcher));
//     }.bind(promise);
//     return promise;
// }
process.on('unhandledRejection',function(event,promise){
    if (event.cmd) return;
    //     console.log("caught unhandled rejection. Command still running...");
    //     rejectionWatcher.set(promise,event);
    // } else
        console.error("Unhandled rejection: ",JSON.stringify(event,true,4),'\n',promise);
});
// process.on('rejectionHandled',function(p){
//     console.log('Rejection handled.');
//     rejectionWatcher.delete(p);
// });
function getUnwrappedPromise() {
    let resolve,reject;
    const e = new Error();
    const promise = new Promise((res,rej)=>{
        resolve=res;
        reject=rej;
    });
    promise.createdAt=e.stack.split('\n').slice(2,3).join('\n');
    return {
        get promise() {
            return promise;
        }
      , resolve:function(...args) {
          if (resolve===nullfunc) return;
        //   const e = new Error();
        //   console.log("Resolving promise",promise);
        //   console.log(e.stack.split('\n').slice(2).join('\n'))
          reject=nullfunc;
          const r=resolve(...args);
          resolve=nullfunc;return r;
        }
      , reject:function(...args) {
          if (reject===nullfunc) return;
        //   const e = new Error();
        //   console.log("Rejecting promise",promise);
        //   console.log(e.stack.split('\n').slice(2).join('\n'))
          resolve=nullfunc;
          const r=reject(...args);
          reject=nullfunc;
          return r;
        }
    };
}
function objToAPIParams(obj,type) {
    const prefix=type==='print'?'':'=';
    return Object.keys(obj)
        .map(k=>obj[k]?`${prefix}${k}=${obj[k]}`:`${prefix}${k}`);
}
function resultsToObj(r) {
    if (r.type) {
        if(Array.isArray(r.data)) return resultsToObj(r.data);
        return [];
    }
    if (r.length&&Array.isArray(r[0])) return r.map(resultsToObj);
    if (!Array.isArray(r)) return {};
    return r.reduce((p,f)=>{p[f.field]=f.value;return p},{});
}
export {hexDump, decodePacket, encodeString, objToAPIParams, resultsToObj,getUnwrappedPromise};
================================================

File: close.js
================================================
// this tests that the connection is properly closed.
// This only verifies that all channels have been eliminated.
// A more full-featured test is in the works. 
var api=require('../dist/mikronode.js')
var device=new api('10.10.10.10');
// device.setDebug(api.DEBUG);
device.connect(
    function(err,login) {
        login('admin','password',runProgram);
    }
);
function runProgram(err,c) {
    console.log('Connection established');
    const channel1 = c.openChannel(1);
    const channel2 = c.openChannel(2);
    const channel3 = c.openChannel(3);
    c.on('close',function(c2) {
        var id=channel1.getId();
        console.log("Channel closing...")
        try {
            c2.getChannel(id);
            console.log('Channel %s is still available. Error.',id);
        } catch (e) {
            console.log('Channel %s is gone!',id);
        }
        id=channel2.getId();
        try {
            c2.getChannel(id);
            console.log('Channel %s is still available. Error.',id);
        } catch (e) {
            console.log('Channel %s is gone!',id);
        }
        id=channel3.getId();
        try {
            c2.getChannel(id);
            console.log('Channel %s is still available. Error.',id);
        } catch (e) {
            console.log('Channel %s is gone!',id);
        }
    });
    channel1.write('/quit').catch(e=>{console.log("Error writing quit",e)})
}
================================================

File: config.js
================================================
// Currently these tests suck. But they help make things work. I'll be using a testing framework later to make it succeed.
// Put the IP, username, and password below for the tests to import.
module.exports=['10.10.10.10','test','user'];
================================================

File: ssl.js
================================================
var MikroNode = require('../dist/mikronode.js');
var device = new MikroNode('10.10.10.10',8729); // We specify the SSL/TLS port of our Mikrotik here.
0
// device.setDebug(MikroNode.DEBUG);
// By setting TLS options, TLS connection is enabled.
device.TLS({
	rejectUnauthorized : false,
	// If your mikrotik does not have a valid certificate, this cipher is the only one that will work.
	ciphers:'ADH'
});
device.connect(/* socketOpts */).then(function([login,socketInfo]){
	// The ability to login or not depending on resolting socket info.
	console.log("Connected.\nLogging in.");
	return login('admin','password'); // must return result of login();
}).then(function(conn) { 
	try {
		console.log("Login complete. Ready for command.");
		conn.closeOnDone(true);
		var channel=conn.openChannel("address_export");
		channel.closeOnDone(true);
		console.log("Writing command to listen for DHCP lease changes.");
		const p=channel.write('/ip/dhcp-server/lease/listen').catch(e=>{
            console.log("Cancel processed");
        });
		// Cancel the listen in 60 seconds. Should cause stuff to complete.
		setTimeout(()=>{channel.write('/cancel').then(()=>{console.log("Sent cancel.")})},10*1000);
		// p.then(data=>console.log("Data received in promise: ",data));
		channel.data.subscribe(e=>console.log("Data Sub: ",MikroNode.resultsToObj(e.data)));
		// channel.done.subscribe(data=>console.log("Done Sub %s:",data.cmd.command,MikroNode.resultsToObj(data.data)));
	} catch (e) {
		console.log("Error while running ",e);
	}
}).catch(err=>{
  	console.log("Error occured while connecting/logging in ",err);
});
================================================

File: sync.js
================================================
var MikroNode = require('../dist/mikronode.js');
var device = new MikroNode('10.10.10.10');
// device.setDebug(MikroNode.DEBUG);
device.connect().then(([login])=>login('admin', 'password').then(function (conn) {
    console.log("Connected");
    // When all channels are complete close the connection.
    conn.closeOnDone(true); 
    // Open new channel named "1" with auto close on.
    let chan = conn.openChannel('1',true)
    // Force sync command mode.
    chan.sync(true);
    // Write first command. P is a promise returned. We show how we can handle it at a later time.
    const p=chan.write('/ip/address/add',{
        'interface':'LAN',
        'network':'255.255.255.0',
        'address':'10.0.0.1'
    });
    // Writing the same IP again will cause a trap.
    chan.write('/ip/address/add',{
        'interface':'LAN',
        'network':'255.255.255.0',
        'address':'10.0.0.1'
    }).then(data=>{
        // Do nothing, since this shouldn't get here.
    }).catch(error=>{
        console.log("Yes. a Trap occurred as expected");
    });
    p.then(data=>{
        // remove the address when the original was complete done.
        const x=chan.write('/ip/address/remove',{
            '.id':data.data
        });
        console.log("ID of write:",x.commandId);
    }).catch(e=>{
        console.log("Add command trap: ",e);
    });
    // Print the list of addresses.. we should see 10.0.0.1 since we are queueing this command before the first promise is resolved.
    const j=chan.write('/ip/address/print').then(data=>{
        // Show ALL data.
        console.log("Done promise all data:", data);
    }).catch(e=>{
        // We shouldn't get to this line.
        console.log("Print command trap: ",e.error);
    });
    // Capture any trap on channel "1"
    chan.trap.subscribe(error=>{
        console.log("Trap recieved on channel.");
    });
    // Listen to individual sentences.
    chan.data.subscribe(data=>{
        // Print each line as it arrives.
        console.log("Chan data:",data);
    },error=>{
        // This should never happen.
        console.log("Error data: ",error);
    },()=>{
        // When we are all done (channel is closed).
        console.log("Closed data: ");
    });
    chan.done.subscribe(data=>{
        console.log("Got chan done:",data);
    },error=>{
        // This should never happen
        console.log("Error done: ",error);
    },()=>{
        // When we are all closed.
        console.log("Closed done: ");
    });
});
================================================

File: test1.js
================================================
var MikroNode = require('../dist/mikronode.js');
var device = new MikroNode('10.10.10.10');
// device.setDebug(MikroNode.DEBUG);
// By setting TLS options, TLS connection is enabled.
device.connect(/* socketOpts */).then(function([login,socketInfo,...args]){
	// The ability to login or not depending on resolting socket info.
	console.log("Connected: ",socketInfo);
	return login('admin','password'); // must return result of login();
}).then(conn=>{ 
	try {
		console.log("Connected");
		conn.closeOnDone(true);
		var channel=conn.openChannel("address_export");
		channel.closeOnDone(true);
		console.log("Writing command...");
		const p=channel.write('/ip/dhcp-server/lease/listen');
		// Cancel the listen in 60 seconds. Should cause stuff to complete.
		setTimeout(()=>{channel.write('/cancel')},60*1000);
		// p.then(data=>console.log("Data received in promise: ",data));
		channel.data.subscribe(e=>console.log("Data Sub: ",e.data));
		// channel.done.subscribe(data=>console.log("Done Sub %s:",data.cmd.command,MikroNode.resultsToObj(data.data)));
	} catch (e) {
		console.log("Error while running ",e);
	}
},err=>{
  	console.log("Error occured while connecting/logging in ",err);
});
================================================

File: testAPI.js
================================================
var api=require('../dist/mikronode.js');
var device=new api(/* Host */'127.0.0.1' /*, Port */ /*, Timeout */);
// device.setDebug(api.DEBUG);
// connect:
device.connect().then(([login])=>login('usrename','password')).then(function(conn) {
    var c1=conn.openChannel();
    console.log('Getting Packages');
    c1.write('/system/package/getall');
    c1.data // get only data here
      .subscribe(function(data) { // feeds in one result line at a time.
          console.log('Data Packet:');
          console.log(JSON.stringify(data.data,true,2));
       })
},function(err) {
  console.log("Error connecting:",err);
});
================================================

File: webpack.config.babel.js
================================================
var webpack = require("webpack");
module.exports = {
    entry: {
      mikronode:['./src/index.js']
    },
    target: 'node',
    module: {
      loaders: [
        {
            test: /\.[ej]s6?$/
          , exclude: /node_modules/
          , loader: 'babel-loader'
          , query: {
                "presets": ['es2015','stage-1']
              , "plugins": [
                    ["transform-replace-object-assign", "simple-assign"]
                  , "transform-dev-warning"
                  , "add-module-exports"
                  , "transform-decorators-legacy"
                  , "transform-private-properties"
                ]
            }
        }
      ]
    },
    output: {
      libraryTarget: 'umd',
      library: 'MikroNode',
      path: 'dist',
      filename: '[name].js'
    },
    resolve: {
      extensions: ['', '.js','.es6']
    },
    plugins: [
      // new webpack.optimize.OccurenceOrderPlugin(),
      new webpack.NoErrorsPlugin(),
      new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify('production')
      })
    ]
}