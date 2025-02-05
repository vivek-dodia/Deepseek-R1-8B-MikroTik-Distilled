# Repository Information
Name: be-cekmac

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
	url = https://gitlab.com/tugasakhirweb2015/be-cekmac.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mac_cek.js
================================================
const axios = require('axios')
const firebase = require('firebase')
const MAC_ADDRESS = require('is-mac-address')
// Your web app's Firebase configuration
// var firebaseConfig = {
//     apiKey: "AIzaSyBcHgXr-7-UoMI5V0Ihe7ycD6DiZH4U9Ps",
//     authDomain: "cekmac-71ae9.firebaseapp.com",
//     projectId: "cekmac-71ae9",
//     storageBucket: "cekmac-71ae9.appspot.com",
//     messagingSenderId: "403103852578",
//     appId: "1:403103852578:web:effeaba3863c02d94f427b"
// };
// Initialize Firebase
// const fire = firebase.initializeApp(firebaseConfig);
// const { MongoClient } = require('mongodb');
const mongoose = require('mongoose');
const urlMongo = "mongodb+srv://tugasakhirwebku:tugasakhirwebku@cluster0.mlged.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
// const uri = "mongodb+srv://tugasakhirwebku:tugasakhirweb2015@cluster0.mlged.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
var isConnectedBefore = false;
var connect = async function () {
    mongoose.connect(urlMongo, { useNewUrlParser: true, useUnifiedTopology: true });
};
connect();
let colMacMongo = mongoose.connection.collection("col_mac")
mongoose.connection.on('error', function () {
    console.log('Could not connect to MongoDB');
});
mongoose.connection.on('disconnected', function () {
    console.log('Lost MongoDB connection...');
    if (!isConnectedBefore)
        connect();
});
mongoose.connection.on('connected', function () {
    isConnectedBefore = true;
    colMacMongo = mongoose.connection.collection("col_mac")
    colMacMongo.createIndex({
        mac: 1,
    }).then().catch()
    console.log('Connection established to MongoDB');
});
mongoose.connection.on('reconnected', function () {
    console.log('Reconnected to MongoDB');
});
// Close the Mongoose connection, when receiving SIGINT
process.on('SIGINT', function () {
    mongoose.connection.close(function () {
        console.log('Force to close the MongoDB conection');
        process.exit(0);
    });
});
// var dbFS = fire.firestore()
// dbFS.settings({
//     timestampsInSnapshots: true
// })
// const collection = dbFS.collection('mackita')
const express = require('express')
const cors = require('cors')
const e = require('express')
const app = express()
const port = 4567
const whitelistMac = []
app.use(cors())
app.get('/', (req, res) => {
    res.send('<H1>NGAPAIN LO GOBLOK</H1>')
})
// app.get('/apaya/:macnya', async (req, res) => {
//     try {
//         const macnya = req.params.macnya
//         console.log(macnya)
//         if (MAC_ADDRESS.isMACAddress(macnya) === false) {
//             return res.send('<H1>NGAPAIN LO GOBLOK :)</H1>')
//         }
//         if (whitelistMac.indexOf(macnya) >= 0) {
//             try {
//                 return res.send({
//                     status: "ok",
//                     msg: 'white list ' + macnya.replace(/:/g, '_')
//                 })
//             } catch (error) {
//                 return res.send({
//                     status: "#ok",
//                     msg: error.message
//                 })
//             }
//         }
//         const hasilMacDB = await collection.doc(macnya).get();
//         if (hasilMacDB.exists) {
//             // console.log(hasilMacDB.data());
//             if (hasilMacDB.data().organization_name !== 'mac-acak') {
//                 return res.send({
//                     status: "ok",
//                     msg: hasilMacDB.data().organization_name
//                 })
//             } else {
//                 return res.send({
//                     status: "###ok",
//                     msg: "mac-acak"
//                 })
//             }
//         }
//         // console.log(req.params.macnya)
//         try {
//             const respMac = await axios.get('https://api.macvendors.com/v1/lookup/' + macnya, {
//                 headers: {
//                     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImp0aSI6ImIxYWQxNTA4LWFiYmEtNDRmMy05YzE1LThhZTMxNDUzNzMwYyJ9.eyJpc3MiOiJtYWN2ZW5kb3JzIiwiYXVkIjoibWFjdmVuZG9ycyIsImp0aSI6ImIxYWQxNTA4LWFiYmEtNDRmMy05YzE1LThhZTMxNDUzNzMwYyIsImlhdCI6MTYxNzk2NTY5NCwiZXhwIjoxOTMyNDYxNjk0LCJzdWIiOiI4NTA3IiwidHlwIjoiYWNjZXNzIn0.hUXRWDmlxxxV2Hsau0t-Grv0Om7qjJzWVnZT8QpBB0hwZBS3Mvgnx9HoMlYnCfLPrxCAmdD-k2askPvEumi8ng"
//                 }
//             })
//             respMac.data.data["lokasi"] = "tng_ratna"
//             await collection.doc(macnya).set(respMac.data.data)
//             // console.log(respMac.data)
//             return res.send({
//                 status: "ok",
//                 msg: respMac.data.data.organization_name
//             })
//         } catch (error) {
//             console.log(error.response.data.errors.detail)
//             if (error.response.data.errors.detail) {
//                 await collection.doc(macnya).set(
//                     {
//                         assignment: '',
//                         organization_address: '',
//                         organization_name: 'mac-acak',
//                         registry: '-',
//                         "lokasi": "tng_ratna"
//                     })
//                 return res.send({
//                     status: "###ok#99",
//                     msg: 'mac-acak'
//                 })
//             } else {
//                 throw error.message
//             }
//         }
//     } catch (error) {
//         const macnya = req.params.macnya
//         let MY_MESSAGE_TEXT = macnya.replace(/:/g, '_') + '___'
//         if (error.response) {
//             /*
//              * The request was made and the server responded with a
//              * status code that falls out of the range of 2xx
//              */
//             // console.log(error.response.data);
//             // console.log(error.response.status);
//             // console.log(error.response.headers);
//             if (typeof error.response.data === 'object') {
//                 MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '_' + JSON.stringify(error.response.data)
//             } else {
//                 MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '_' + error.response.data
//             }
//         } else if (error.request) {
//             /*
//              * The request was made but no response was received, `error.request`
//              * is an instance of XMLHttpRequest in the browser and an instance
//              * of http.ClientRequest in Node.js
//              */
//             // console.log(error.request);
//         } else {
//             // Something happened in setting up the request and triggered an Error
//             // console.log('Error', error.message);
//             MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '__' + error.message
//         }
//         const BOT_API_KEY = '673250853:AAGNzH6WbZ5g3DzEMN0gMIeuO8-69Q5jo5w'
//         const MY_CHANNEL_NAME = '-347088847'
//         const urlnya = `https://api.telegram.org/bot` + BOT_API_KEY + `/sendMessage?chat_id=` + MY_CHANNEL_NAME + `&text=` + MY_MESSAGE_TEXT
//         axios.get(urlnya).then((resp) => {
//             // console.log(resp)
//         }).catch((error) => {
//             // console.log(error.message)
//         })
//         console.log(MY_MESSAGE_TEXT)
//         return res.send({
//             status: "###ok",
//             msg: MY_MESSAGE_TEXT
//         })
//     }
// })
app.get('/apayav2/:macnya', async (req, res) => {
    try {
        const macnya = req.params.macnya
        // console.log(macnya)
        if (MAC_ADDRESS.isMACAddress(macnya) === false) {
            return res.send('<H1>NGAPAIN LO GOBLOK :)</H1>')
        }
        if (whitelistMac.indexOf(macnya) >= 0) {
            try {
                return res.send({
                    status: "ok",
                    msg: 'white list ' + macnya.replace(/:/g, '_')
                })
            } catch (error) {
                return res.send({
                    status: "#ok",
                    msg: error.message
                })
            }
        }
        if (isConnectedBefore === false) {
            await connect()
        }
        const hasilMacDB = await colMacMongo.find({
            mac: macnya,
            // organization_name
        }).toArray()
        // console.log(hasilMacDB)
        // process.exit(0)
        // const hasilMacDB = await collection.doc(macnya).get();
        if (hasilMacDB.length > 0) {
            // console.log(hasilMacDB.data());
            if (hasilMacDB[0].organization_name !== 'mac-acak') {
                return res.send({
                    status: "ok",
                    msg: hasilMacDB[0].organization_name
                })
            } else {
                return res.send({
                    status: "###ok",
                    msg: "mac-acak"
                })
            }
        }
        try {
            let respMac = await axios.get('https://api.macvendors.com/v1/lookup/' + macnya, {
                headers: {
                    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImp0aSI6ImIxYWQxNTA4LWFiYmEtNDRmMy05YzE1LThhZTMxNDUzNzMwYyJ9.eyJpc3MiOiJtYWN2ZW5kb3JzIiwiYXVkIjoibWFjdmVuZG9ycyIsImp0aSI6ImIxYWQxNTA4LWFiYmEtNDRmMy05YzE1LThhZTMxNDUzNzMwYyIsImlhdCI6MTYxNzk2NTY5NCwiZXhwIjoxOTMyNDYxNjk0LCJzdWIiOiI4NTA3IiwidHlwIjoiYWNjZXNzIn0.hUXRWDmlxxxV2Hsau0t-Grv0Om7qjJzWVnZT8QpBB0hwZBS3Mvgnx9HoMlYnCfLPrxCAmdD-k2askPvEumi8ng"
                }
            })
            respMac.data.data["lokasi"] = "tng_ratna"
            respMac.data.data["mac"] = macnya
            console.log(respMac.data.data)
            const isInsert = await colMacMongo.insertOne(respMac.data.data)
            console.log("done insert" + isInsert.insertedId.inspect())
            // console.log(respMac.data)
            return res.send({
                status: "ok",
                msg: respMac.data.data.organization_name
            })
        } catch (error) {
            console.log(error.response.data.errors.detail)
            if (error.response.data.errors.detail) {
                await colMacMongo.insertOne(
                    {
                        mac: macnya,
                        assignment: '',
                        organization_address: '',
                        organization_name: 'mac-acak',
                        registry: '-',
                        "lokasi": "tng_ratna"
                    })
                return res.send({
                    status: "###ok#99",
                    msg: 'mac-acak'
                })
            } else {
                throw error.message
            }
        }
    } catch (error) {
        const macnya = req.params.macnya
        let MY_MESSAGE_TEXT = macnya.replace(/:/g, '_') + '___'
        if (error.response) {
            /*
             * The request was made and the server responded with a
             * status code that falls out of the range of 2xx
             */
            // console.log(error.response.data);
            // console.log(error.response.status);
            // console.log(error.response.headers);
            if (typeof error.response.data === 'object') {
                MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '_' + JSON.stringify(error.response.data)
            } else {
                MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '_' + error.response.data
            }
        } else if (error.request) {
            /*
             * The request was made but no response was received, `error.request`
             * is an instance of XMLHttpRequest in the browser and an instance
             * of http.ClientRequest in Node.js
             */
            // console.log(error.request);
        } else {
            // Something happened in setting up the request and triggered an Error
            // console.log('Error', error.message);
            MY_MESSAGE_TEXT = MY_MESSAGE_TEXT + '__' + error.message
        }
        const BOT_API_KEY = '673250853:AAGNzH6WbZ5g3DzEMN0gMIeuO8-69Q5jo5w'
        const MY_CHANNEL_NAME = '-347088847'
        const urlnya = `https://api.telegram.org/bot` + BOT_API_KEY + `/sendMessage?chat_id=` + MY_CHANNEL_NAME + `&text=` + MY_MESSAGE_TEXT
        axios.get(urlnya).then((resp) => {
            // console.log(resp)
        }).catch((error) => {
            // console.log(error.message)
        })
        console.log(MY_MESSAGE_TEXT)
        return res.send({
            status: "###ok",
            msg: MY_MESSAGE_TEXT + " err catch"
        })
    }
})
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
================================================

File: package-lock.json
================================================
{
  "name": "macvendor",
  "version": "1.0.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "@firebase/analytics": {
      "version": "0.6.8",
      "resolved": "https://registry.npmjs.org/@firebase/analytics/-/analytics-0.6.8.tgz",
      "integrity": "sha512-cPbQIQo3uqpImtiGIB42F9s9fw8cPseCj1ZMR3VshL6u/6kzC9ptOpgg8PMCLOgZvBwC993LbT1UOTuufTd49Q==",
      "requires": {
        "@firebase/analytics-types": "0.4.0",
        "@firebase/component": "0.4.0",
        "@firebase/installations": "0.4.24",
        "@firebase/logger": "0.2.6",
        "@firebase/util": "0.4.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/analytics-types": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/analytics-types/-/analytics-types-0.4.0.tgz",
      "integrity": "sha512-Jj2xW+8+8XPfWGkv9HPv/uR+Qrmq37NPYT352wf7MvE9LrstpLVmFg3LqG6MCRr5miLAom5sen2gZ+iOhVDeRA=="
    },
    "@firebase/app": {
      "version": "0.6.19",
      "resolved": "https://registry.npmjs.org/@firebase/app/-/app-0.6.19.tgz",
      "integrity": "sha512-qDimGNoukCuWvGYcsosGV2tOKbJ98RuRHLoK2j4t73TupY6rH+4QeR3tf5E3q1gZ5mtaFZloXc6aZWWOgtfwoQ==",
      "requires": {
        "@firebase/app-types": "0.6.2",
        "@firebase/component": "0.4.0",
        "@firebase/logger": "0.2.6",
        "@firebase/util": "0.4.1",
        "dom-storage": "2.1.0",
        "tslib": "^2.1.0",
        "xmlhttprequest": "1.8.0"
      }
    },
    "@firebase/app-types": {
      "version": "0.6.2",
      "resolved": "https://registry.npmjs.org/@firebase/app-types/-/app-types-0.6.2.tgz",
      "integrity": "sha512-2VXvq/K+n8XMdM4L2xy5bYp2ZXMawJXluUIDzUBvMthVR+lhxK4pfFiqr1mmDbv9ydXvEAuFsD+6DpcZuJcSSw=="
    },
    "@firebase/auth": {
      "version": "0.16.4",
      "resolved": "https://registry.npmjs.org/@firebase/auth/-/auth-0.16.4.tgz",
      "integrity": "sha512-zgHPK6/uL6+nAyG9zqammHTF1MQpAN7z/jVRLYkDZS4l81H08b2SzApLbRfW/fmy665xqb5MK7sVH0V1wsiCNw==",
      "requires": {
        "@firebase/auth-types": "0.10.2"
      }
    },
    "@firebase/auth-interop-types": {
      "version": "0.1.5",
      "resolved": "https://registry.npmjs.org/@firebase/auth-interop-types/-/auth-interop-types-0.1.5.tgz",
      "integrity": "sha512-88h74TMQ6wXChPA6h9Q3E1Jg6TkTHep2+k63OWg3s0ozyGVMeY+TTOti7PFPzq5RhszQPQOoCi59es4MaRvgCw=="
    },
    "@firebase/auth-types": {
      "version": "0.10.2",
      "resolved": "https://registry.npmjs.org/@firebase/auth-types/-/auth-types-0.10.2.tgz",
      "integrity": "sha512-0GMWVWh5TBCYIQfVerxzDsuvhoFpK0++O9LtP3FWkwYo7EAxp6w0cftAg/8ntU1E5Wg56Ry0b6ti/YGP6g0jlg=="
    },
    "@firebase/component": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/component/-/component-0.4.0.tgz",
      "integrity": "sha512-L7kLKpW1v5qxPfIhx/VqHuVi+vr5IcnDS4zCJFb+/eYe23i6czSOWR1urAoJ4r42Dk0XB5kDt6Idojdd9BGMEA==",
      "requires": {
        "@firebase/util": "0.4.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/database": {
      "version": "0.9.8",
      "resolved": "https://registry.npmjs.org/@firebase/database/-/database-0.9.8.tgz",
      "integrity": "sha512-bqZUDR6jIQSQcY7oZVGmI/Bg7SfmUUW/toaZBCfaddWAnniBthaa8o0Hyv1ypPxjEZCu1CfPQwtpMhlSTjG0tA==",
      "requires": {
        "@firebase/auth-interop-types": "0.1.5",
        "@firebase/component": "0.4.0",
        "@firebase/database-types": "0.7.1",
        "@firebase/logger": "0.2.6",
        "@firebase/util": "0.4.1",
        "faye-websocket": "0.11.3",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/database-types": {
      "version": "0.7.1",
      "resolved": "https://registry.npmjs.org/@firebase/database-types/-/database-types-0.7.1.tgz",
      "integrity": "sha512-465ceJXSMqFFMnL2lxYx+YhYajcyk+VpGiXf9T6KNME0lKne5hYuqYr7XmS8/sTeyV0huhmTb8K1nxlA7hiPOg==",
      "requires": {
        "@firebase/app-types": "0.6.2"
      }
    },
    "@firebase/firestore": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/@firebase/firestore/-/firestore-2.2.3.tgz",
      "integrity": "sha512-efJxJahP9936QlIHeATvatCO4c3UEk6nz7pc812xxkgTVezkg8K66IDUe0fncV70zbDrIyxUIl8yRcxhXytiGw==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/firestore-types": "2.2.0",
        "@firebase/logger": "0.2.6",
        "@firebase/util": "0.4.1",
        "@firebase/webchannel-wrapper": "0.4.1",
        "@grpc/grpc-js": "^1.0.0",
        "@grpc/proto-loader": "^0.5.0",
        "node-fetch": "2.6.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/firestore-types": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/@firebase/firestore-types/-/firestore-types-2.2.0.tgz",
      "integrity": "sha512-5kZZtQ32FIRJP1029dw+ZVNRCclKOErHv1+Xn0pw/5Fq3dxroA/ZyFHqDu+uV52AyWHhNLjCqX43ibm4YqOzRw=="
    },
    "@firebase/functions": {
      "version": "0.6.6",
      "resolved": "https://registry.npmjs.org/@firebase/functions/-/functions-0.6.6.tgz",
      "integrity": "sha512-cvZiqcL3X7+6ObkwcRUV54iFHaVxVgio2t610p2qwjzMxyYfiHWDA+GwKPioObDWqyXmNtkU8cw2WLoGf46cnA==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/functions-types": "0.4.0",
        "@firebase/messaging-types": "0.5.0",
        "node-fetch": "2.6.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/functions-types": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/@firebase/functions-types/-/functions-types-0.4.0.tgz",
      "integrity": "sha512-3KElyO3887HNxtxNF1ytGFrNmqD+hheqjwmT3sI09FaDCuaxGbOnsXAXH2eQ049XRXw9YQpHMgYws/aUNgXVyQ=="
    },
    "@firebase/installations": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/@firebase/installations/-/installations-0.4.24.tgz",
      "integrity": "sha512-cMWI3IfnmdJ4SzPav56yaHwEhpPPl5b03AVtv7AeKnmDZ61eBqPzEnYSL8Iso73/FeKpr8BYcZelAx0EyxcJ3Q==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/installations-types": "0.3.4",
        "@firebase/util": "0.4.1",
        "idb": "3.0.2",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/installations-types": {
      "version": "0.3.4",
      "resolved": "https://registry.npmjs.org/@firebase/installations-types/-/installations-types-0.3.4.tgz",
      "integrity": "sha512-RfePJFovmdIXb6rYwtngyxuEcWnOrzdZd9m7xAW0gRxDIjBT20n3BOhjpmgRWXo/DAxRmS7bRjWAyTHY9cqN7Q=="
    },
    "@firebase/logger": {
      "version": "0.2.6",
      "resolved": "https://registry.npmjs.org/@firebase/logger/-/logger-0.2.6.tgz",
      "integrity": "sha512-KIxcUvW/cRGWlzK9Vd2KB864HlUnCfdTH0taHE0sXW5Xl7+W68suaeau1oKNEqmc3l45azkd4NzXTCWZRZdXrw=="
    },
    "@firebase/messaging": {
      "version": "0.7.8",
      "resolved": "https://registry.npmjs.org/@firebase/messaging/-/messaging-0.7.8.tgz",
      "integrity": "sha512-rXYvVQPZd+rCMV7+/FgpvsHad0HuEhoyH5OQgYxeBgSsgFn6mOyvAtYcoCFjPTvTV5eyGH1I4hQtNOyY8zVzzg==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/installations": "0.4.24",
        "@firebase/messaging-types": "0.5.0",
        "@firebase/util": "0.4.1",
        "idb": "3.0.2",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/messaging-types": {
      "version": "0.5.0",
      "resolved": "https://registry.npmjs.org/@firebase/messaging-types/-/messaging-types-0.5.0.tgz",
      "integrity": "sha512-QaaBswrU6umJYb/ZYvjR5JDSslCGOH6D9P136PhabFAHLTR4TWjsaACvbBXuvwrfCXu10DtcjMxqfhdNIB1Xfg=="
    },
    "@firebase/performance": {
      "version": "0.4.10",
      "resolved": "https://registry.npmjs.org/@firebase/performance/-/performance-0.4.10.tgz",
      "integrity": "sha512-gyAOd9Z/GVlLE5V8U5pVQDZpjr4Msdx5yJr7oQE/xkh6dNZGuYp5qJh1pAmJs2ZI8eMTs+j2bXJEMYk6w7ehRg==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/installations": "0.4.24",
        "@firebase/logger": "0.2.6",
        "@firebase/performance-types": "0.0.13",
        "@firebase/util": "0.4.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/performance-types": {
      "version": "0.0.13",
      "resolved": "https://registry.npmjs.org/@firebase/performance-types/-/performance-types-0.0.13.tgz",
      "integrity": "sha512-6fZfIGjQpwo9S5OzMpPyqgYAUZcFzZxHFqOyNtorDIgNXq33nlldTL/vtaUZA8iT9TT5cJlCrF/jthKU7X21EA=="
    },
    "@firebase/polyfill": {
      "version": "0.3.36",
      "resolved": "https://registry.npmjs.org/@firebase/polyfill/-/polyfill-0.3.36.tgz",
      "integrity": "sha512-zMM9oSJgY6cT2jx3Ce9LYqb0eIpDE52meIzd/oe/y70F+v9u1LDqk5kUF5mf16zovGBWMNFmgzlsh6Wj0OsFtg==",
      "requires": {
        "core-js": "3.6.5",
        "promise-polyfill": "8.1.3",
        "whatwg-fetch": "2.0.4"
      }
    },
    "@firebase/remote-config": {
      "version": "0.1.35",
      "resolved": "https://registry.npmjs.org/@firebase/remote-config/-/remote-config-0.1.35.tgz",
      "integrity": "sha512-szhu48LTyb46S33hUR3sC4kiykEoc+B5M7HWWHhjp7Ne+524G8pH/9+/r9ZA8eVj48c5cihXyQKQ/6yCQotnUA==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/installations": "0.4.24",
        "@firebase/logger": "0.2.6",
        "@firebase/remote-config-types": "0.1.9",
        "@firebase/util": "0.4.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/remote-config-types": {
      "version": "0.1.9",
      "resolved": "https://registry.npmjs.org/@firebase/remote-config-types/-/remote-config-types-0.1.9.tgz",
      "integrity": "sha512-G96qnF3RYGbZsTRut7NBX0sxyczxt1uyCgXQuH/eAfUCngxjEGcZQnBdy6mvSdqdJh5mC31rWPO4v9/s7HwtzA=="
    },
    "@firebase/storage": {
      "version": "0.4.7",
      "resolved": "https://registry.npmjs.org/@firebase/storage/-/storage-0.4.7.tgz",
      "integrity": "sha512-5DFb+VncNBomPzpzYqJzzJjfiZhOWg0FHTBkw90K9OdE2wUfKqzhhbIAjyaXcu+2YLB2hjft8BKbjQfV5BDFnw==",
      "requires": {
        "@firebase/component": "0.4.0",
        "@firebase/storage-types": "0.3.13",
        "@firebase/util": "0.4.1",
        "tslib": "^2.1.0"
      }
    },
    "@firebase/storage-types": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@firebase/storage-types/-/storage-types-0.3.13.tgz",
      "integrity": "sha512-pL7b8d5kMNCCL0w9hF7pr16POyKkb3imOW7w0qYrhBnbyJTdVxMWZhb0HxCFyQWC0w3EiIFFmxoz8NTFZDEFog=="
    },
    "@firebase/util": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/@firebase/util/-/util-0.4.1.tgz",
      "integrity": "sha512-XhYCOwq4AH+YeQBEnDQvigz50WiiBU4LnJh2+//VMt4J2Ybsk0eTgUHNngUzXsmp80EJrwal3ItODg55q1ajWg==",
      "requires": {
        "tslib": "^2.1.0"
      }
    },
    "@firebase/webchannel-wrapper": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/@firebase/webchannel-wrapper/-/webchannel-wrapper-0.4.1.tgz",
      "integrity": "sha512-0yPjzuzGMkW1GkrC8yWsiN7vt1OzkMIi9HgxRmKREZl2wnNPOKo/yScTjXf/O57HM8dltqxPF6jlNLFVtc2qdw=="
    },
    "@grpc/grpc-js": {
      "version": "1.2.12",
      "resolved": "https://registry.npmjs.org/@grpc/grpc-js/-/grpc-js-1.2.12.tgz",
      "integrity": "sha512-+gPCklP1eqIgrNPyzddYQdt9+GvZqPlLpIjIo+TveE+gbtp74VV1A2ju8ExeO8ma8f7MbpaGZx/KJPYVWL9eDw==",
      "requires": {
        "@types/node": ">=12.12.47",
        "google-auth-library": "^6.1.1",
        "semver": "^6.2.0"
      }
    },
    "@grpc/proto-loader": {
      "version": "0.5.6",
      "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.5.6.tgz",
      "integrity": "sha512-DT14xgw3PSzPxwS13auTEwxhMMOoz33DPUKNtmYK/QYbBSpLXJy78FGGs5yVoxVobEqPm4iW9MOIoz0A3bLTRQ==",
      "requires": {
        "lodash.camelcase": "^4.3.0",
        "protobufjs": "^6.8.6"
      }
    },
    "@protobufjs/aspromise": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/aspromise/-/aspromise-1.1.2.tgz",
      "integrity": "sha1-m4sMxmPWaafY9vXQiToU00jzD78="
    },
    "@protobufjs/base64": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/base64/-/base64-1.1.2.tgz",
      "integrity": "sha512-AZkcAA5vnN/v4PDqKyMR5lx7hZttPDgClv83E//FMNhR2TMcLUhfRUBHCmSl0oi9zMgDDqRUJkSxO3wm85+XLg=="
    },
    "@protobufjs/codegen": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/@protobufjs/codegen/-/codegen-2.0.4.tgz",
      "integrity": "sha512-YyFaikqM5sH0ziFZCN3xDC7zeGaB/d0IUb9CATugHWbd1FRFwWwt4ld4OYMPWu5a3Xe01mGAULCdqhMlPl29Jg=="
    },
    "@protobufjs/eventemitter": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/eventemitter/-/eventemitter-1.1.0.tgz",
      "integrity": "sha1-NVy8mLr61ZePntCV85diHx0Ga3A="
    },
    "@protobufjs/fetch": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/fetch/-/fetch-1.1.0.tgz",
      "integrity": "sha1-upn7WYYUr2VwDBYZ/wbUVLDYTEU=",
      "requires": {
        "@protobufjs/aspromise": "^1.1.1",
        "@protobufjs/inquire": "^1.1.0"
      }
    },
    "@protobufjs/float": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/float/-/float-1.0.2.tgz",
      "integrity": "sha1-Xp4avctz/Ap8uLKR33jIy9l7h9E="
    },
    "@protobufjs/inquire": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/inquire/-/inquire-1.1.0.tgz",
      "integrity": "sha1-/yAOPnzyQp4tyvwRQIKOjMY48Ik="
    },
    "@protobufjs/path": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@protobufjs/path/-/path-1.1.2.tgz",
      "integrity": "sha1-bMKyDFya1q0NzP0hynZz2Nf79o0="
    },
    "@protobufjs/pool": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/pool/-/pool-1.1.0.tgz",
      "integrity": "sha1-Cf0V8tbTq/qbZbw2ZQbWrXhG/1Q="
    },
    "@protobufjs/utf8": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@protobufjs/utf8/-/utf8-1.1.0.tgz",
      "integrity": "sha1-p3c2C1s5oaLlEG+OhY8v0tBgxXA="
    },
    "@types/long": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/@types/long/-/long-4.0.1.tgz",
      "integrity": "sha512-5tXH6Bx/kNGd3MgffdmP4dy2Z+G4eaXw0SE81Tq3BNadtnMR5/ySMzX4SLEzHJzSmPNn4HIdpQsBvXMUykr58w=="
    },
    "@types/node": {
      "version": "14.14.37",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-14.14.37.tgz",
      "integrity": "sha512-XYmBiy+ohOR4Lh5jE379fV2IU+6Jn4g5qASinhitfyO71b/sCo6MKsMLF5tc7Zf2CE8hViVQyYSobJNke8OvUw=="
    },
    "@types/webidl-conversions": {
      "version": "6.1.1",
      "resolved": "https://registry.npmjs.org/@types/webidl-conversions/-/webidl-conversions-6.1.1.tgz",
      "integrity": "sha512-XAahCdThVuCFDQLT7R7Pk/vqeObFNL3YqRyFZg+AqAP/W1/w3xHaIxuW7WszQqTbIBOPRcItYJIou3i/mppu3Q=="
    },
    "@types/whatwg-url": {
      "version": "8.2.1",
      "resolved": "https://registry.npmjs.org/@types/whatwg-url/-/whatwg-url-8.2.1.tgz",
      "integrity": "sha512-2YubE1sjj5ifxievI5Ge1sckb9k/Er66HyR2c+3+I6VDUUg1TLPdYYTEbQ+DjRkS4nTxMJhgWfSfMRD2sl2EYQ==",
      "requires": {
        "@types/node": "*",
        "@types/webidl-conversions": "*"
      }
    },
    "abort-controller": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/abort-controller/-/abort-controller-3.0.0.tgz",
      "integrity": "sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg==",
      "requires": {
        "event-target-shim": "^5.0.0"
      }
    },
    "accepts": {
      "version": "1.3.7",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.7.tgz",
      "integrity": "sha512-Il80Qs2WjYlJIBNzNkK6KYqlVMTbZLXgHx2oT0pU/fjRHyEp+PEfEPY0R3WCwAGVOtauxh1hOxNgIf5bv7dQpA==",
      "requires": {
        "mime-types": "~2.1.24",
        "negotiator": "0.6.2"
      }
    },
    "agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "requires": {
        "debug": "4"
      },
      "dependencies": {
        "debug": {
          "version": "4.3.1",
          "resolved": "https://registry.npmjs.org/debug/-/debug-4.3.1.tgz",
          "integrity": "sha512-doEwdvm4PCeK4K3RQN2ZC2BYUBaxwLARCqZmMjtF8a51J2Rb0xpVloFRnCODwqjpwnAoao4pelN8l3RJdv3gRQ==",
          "requires": {
            "ms": "2.1.2"
          }
        },
        "ms": {
          "version": "2.1.2",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
          "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
        }
      }
    },
    "array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha1-ml9pkFGx5wczKPKgCJaLZOopVdI="
    },
    "arrify": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-2.0.1.tgz",
      "integrity": "sha512-3duEwti880xqi4eAMN8AyR4a0ByT90zoYdLlevfrvU43vb0YZwZVfxOgxWrLXXXpyugL0hNZc9G6BiB5B3nUug=="
    },
    "async-disk-cache": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/async-disk-cache/-/async-disk-cache-2.1.0.tgz",
      "integrity": "sha512-iH+boep2xivfD9wMaZWkywYIURSmsL96d6MoqrC94BnGSvXE4Quf8hnJiHGFYhw/nLeIa1XyRaf4vvcvkwAefg==",
      "requires": {
        "debug": "^4.1.1",
        "heimdalljs": "^0.2.3",
        "istextorbinary": "^2.5.1",
        "mkdirp": "^0.5.0",
        "rimraf": "^3.0.0",
        "rsvp": "^4.8.5",
        "username-sync": "^1.0.2"
      },
      "dependencies": {
        "debug": {
          "version": "4.3.1",
          "resolved": "https://registry.npmjs.org/debug/-/debug-4.3.1.tgz",
          "integrity": "sha512-doEwdvm4PCeK4K3RQN2ZC2BYUBaxwLARCqZmMjtF8a51J2Rb0xpVloFRnCODwqjpwnAoao4pelN8l3RJdv3gRQ==",
          "requires": {
            "ms": "2.1.2"
          }
        },
        "ms": {
          "version": "2.1.2",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
          "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
        }
      }
    },
    "axios": {
      "version": "0.21.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.21.1.tgz",
      "integrity": "sha512-dKQiRHxGD9PPRIUNIWvZhPTPpl1rf/OxTYKsqKUDjBwYylTvV7SjSHJb9ratfyzM6wCdLCOYLzs73qpg5c4iGA==",
      "requires": {
        "follow-redirects": "^1.10.0"
      }
    },
    "balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw=="
    },
    "base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA=="
    },
    "bignumber.js": {
      "version": "9.0.1",
      "resolved": "https://registry.npmjs.org/bignumber.js/-/bignumber.js-9.0.1.tgz",
      "integrity": "sha512-IdZR9mh6ahOBv/hYGiXyVuyCetmGJhtYkqLBpTStdhEGjegpPlUawydyaF3pbIOFynJTpllEs+NP+CS9jKFLjA=="
    },
    "binaryextensions": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/binaryextensions/-/binaryextensions-2.3.0.tgz",
      "integrity": "sha512-nAihlQsYGyc5Bwq6+EsubvANYGExeJKHDO3RjnvwU042fawQTQfM3Kxn7IHUXQOz4bzfwsGYYHGSvXyW4zOGLg=="
    },
    "body-parser": {
      "version": "1.19.0",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.19.0.tgz",
      "integrity": "sha512-dhEPs72UPbDnAQJ9ZKMNTP6ptJaionhP5cBb541nXPlW60Jepo9RV/a4fX4XWW9CuFNK22krhrj1+rgzifNCsw==",
      "requires": {
        "bytes": "3.1.0",
        "content-type": "~1.0.4",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "http-errors": "1.7.2",
        "iconv-lite": "0.4.24",
        "on-finished": "~2.3.0",
        "qs": "6.7.0",
        "raw-body": "2.4.0",
        "type-is": "~1.6.17"
      }
    },
    "brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "requires": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "bson": {
      "version": "4.5.1",
      "resolved": "https://registry.npmjs.org/bson/-/bson-4.5.1.tgz",
      "integrity": "sha512-XqFP74pbTVLyLy5KFxVfTUyRrC1mgOlmu/iXHfXqfCKT59jyP9lwbotGfbN59cHBRbJSamZNkrSopjv+N0SqAA==",
      "requires": {
        "buffer": "^5.6.0"
      }
    },
    "buffer": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
      "integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
      "requires": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.1.13"
      }
    },
    "buffer-equal-constant-time": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/buffer-equal-constant-time/-/buffer-equal-constant-time-1.0.1.tgz",
      "integrity": "sha1-+OcRMvf/5uAaXJaXpMbz5I1cyBk="
    },
    "bytes": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.0.tgz",
      "integrity": "sha512-zauLjrfCG+xvoyaqLoV8bLVXXNGC4JqlxFCutSDWA6fJrTo2ZuvLYTqZ7aHBLZSMOopbzwv8f+wZcVzfVTI2Dg=="
    },
    "concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha1-2Klr13/Wjfd5OnMDajug1UBdR3s="
    },
    "content-disposition": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.3.tgz",
      "integrity": "sha512-ExO0774ikEObIAEV9kDo50o+79VCUdEB6n6lzKgGwupcVeRlhrj3qGAfwq8G6uBJjkqLrhT0qEYFcWng8z1z0g==",
      "requires": {
        "safe-buffer": "5.1.2"
      }
    },
    "content-type": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.4.tgz",
      "integrity": "sha512-hIP3EEPs8tB9AT1L+NUqtwOAps4mk2Zob89MWXMHjHWg9milF/j4osnnQLXBCBFBk/tvIG/tUc9mOUJiPBhPXA=="
    },
    "cookie": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.4.0.tgz",
      "integrity": "sha512-+Hp8fLp57wnUSt0tY0tHEXh4voZRDnoIrZPqlo3DPiI4y9lwg/jqx+1Om94/W6ZaPDOUbnjOt/99w66zk+l1Xg=="
    },
    "cookie-signature": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
      "integrity": "sha1-4wOogrNCzD7oylE6eZmXNNqzriw="
    },
    "core-js": {
      "version": "3.6.5",
      "resolved": "https://registry.npmjs.org/core-js/-/core-js-3.6.5.tgz",
      "integrity": "sha512-vZVEEwZoIsI+vPEuoF9Iqf5H7/M3eeQqWlQnYa8FSKKePuYTf5MWnxb5SDAzCa60b3JBRS5g9b+Dq7b1y/RCrA=="
    },
    "cors": {
      "version": "2.8.5",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.5.tgz",
      "integrity": "sha512-KIHbLJqu73RGr/hnbrO9uBeixNGuvSQjul/jdFvS/KFSIH1hWVd1ng7zOHx+YrEfInLG7q4n6GHQ9cDtxv/P6g==",
      "requires": {
        "object-assign": "^4",
        "vary": "^1"
      }
    },
    "debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "requires": {
        "ms": "2.0.0"
      }
    },
    "denque": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/denque/-/denque-1.5.1.tgz",
      "integrity": "sha512-XwE+iZ4D6ZUB7mfYRMb5wByE8L74HCn30FBN7sWnXksWc1LO1bPDl67pBR9o/kC4z/xSNAwkMYcGgqDV3BE3Hw=="
    },
    "depd": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
      "integrity": "sha1-m81S4UwJd2PnSbJ0xDRu0uVgtak="
    },
    "destroy": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz",
      "integrity": "sha1-l4hXRCxEdJ5CBmE+N5RiBYJqvYA="
    },
    "dom-storage": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/dom-storage/-/dom-storage-2.1.0.tgz",
      "integrity": "sha512-g6RpyWXzl0RR6OTElHKBl7nwnK87GUyZMYC7JWsB/IA73vpqK2K6LT39x4VepLxlSsWBFrPVLnsSR5Jyty0+2Q=="
    },
    "ecdsa-sig-formatter": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/ecdsa-sig-formatter/-/ecdsa-sig-formatter-1.0.11.tgz",
      "integrity": "sha512-nagl3RYrbNv6kQkeJIpt6NJZy8twLB/2vtz6yN9Z4vRKHN4/QZJIEbqohALSgwKdnksuY3k5Addp5lg8sVoVcQ==",
      "requires": {
        "safe-buffer": "^5.0.1"
      }
    },
    "editions": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/editions/-/editions-2.3.1.tgz",
      "integrity": "sha512-ptGvkwTvGdGfC0hfhKg0MT+TRLRKGtUiWGBInxOm5pz7ssADezahjCUaYuZ8Dr+C05FW0AECIIPt4WBxVINEhA==",
      "requires": {
        "errlop": "^2.0.0",
        "semver": "^6.3.0"
      }
    },
    "ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha1-WQxhFWsK4vTwJVcyoViyZrxWsh0="
    },
    "encodeurl": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
      "integrity": "sha1-rT/0yG7C0CkyL1oCw6mmBslbP1k="
    },
    "errlop": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/errlop/-/errlop-2.2.0.tgz",
      "integrity": "sha512-e64Qj9+4aZzjzzFpZC7p5kmm/ccCrbLhAJplhsDXQFs87XTsXwOpH4s1Io2s90Tau/8r2j9f4l/thhDevRjzxw=="
    },
    "escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha1-Aljq5NPQwJdN4cFpGI7wBR0dGYg="
    },
    "etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha1-Qa4u62XvpiJorr/qg6x9eSmbCIc="
    },
    "event-target-shim": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/event-target-shim/-/event-target-shim-5.0.1.tgz",
      "integrity": "sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ=="
    },
    "express": {
      "version": "4.17.1",
      "resolved": "https://registry.npmjs.org/express/-/express-4.17.1.tgz",
      "integrity": "sha512-mHJ9O79RqluphRrcw2X/GTh3k9tVv8YcoyY4Kkh4WDMUYKRZUq0h1o0w2rrrxBqM7VoeUVqgb27xlEMXTnYt4g==",
      "requires": {
        "accepts": "~1.3.7",
        "array-flatten": "1.1.1",
        "body-parser": "1.19.0",
        "content-disposition": "0.5.3",
        "content-type": "~1.0.4",
        "cookie": "0.4.0",
        "cookie-signature": "1.0.6",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.1.2",
        "fresh": "0.5.2",
        "merge-descriptors": "1.0.1",
        "methods": "~1.1.2",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.3",
        "path-to-regexp": "0.1.7",
        "proxy-addr": "~2.0.5",
        "qs": "6.7.0",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.1.2",
        "send": "0.17.1",
        "serve-static": "1.14.1",
        "setprototypeof": "1.1.1",
        "statuses": "~1.5.0",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      }
    },
    "extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g=="
    },
    "fast-text-encoding": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/fast-text-encoding/-/fast-text-encoding-1.0.3.tgz",
      "integrity": "sha512-dtm4QZH9nZtcDt8qJiOH9fcQd1NAgi+K1O2DbE6GG1PPCK/BWfOH3idCTRQ4ImXRUOyopDEgDEnVEE7Y/2Wrig=="
    },
    "faye-websocket": {
      "version": "0.11.3",
      "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.11.3.tgz",
      "integrity": "sha512-D2y4bovYpzziGgbHYtGCMjlJM36vAl/y+xUyn1C+FVx8szd1E+86KwVw6XvYSzOP8iMpm1X0I4xJD+QtUb36OA==",
      "requires": {
        "websocket-driver": ">=0.5.1"
      }
    },
    "finalhandler": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.1.2.tgz",
      "integrity": "sha512-aAWcW57uxVNrQZqFXjITpW3sIUQmHGG3qSb9mUah9MgMC4NeWhNOlNjXEYq3HjRAvL6arUviZGGJsBg6z0zsWA==",
      "requires": {
        "debug": "2.6.9",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.3",
        "statuses": "~1.5.0",
        "unpipe": "~1.0.0"
      }
    },
    "firebase": {
      "version": "8.3.3",
      "resolved": "https://registry.npmjs.org/firebase/-/firebase-8.3.3.tgz",
      "integrity": "sha512-eRkW7bD25aevlGwtCEsP53xBo5/Fi4wkxvfvmDW6R2/oSHjy+hVLkQILP4kQFFXgFL0LBjxIPOchXoQ5MUbTCA==",
      "requires": {
        "@firebase/analytics": "0.6.8",
        "@firebase/app": "0.6.19",
        "@firebase/app-types": "0.6.2",
        "@firebase/auth": "0.16.4",
        "@firebase/database": "0.9.8",
        "@firebase/firestore": "2.2.3",
        "@firebase/functions": "0.6.6",
        "@firebase/installations": "0.4.24",
        "@firebase/messaging": "0.7.8",
        "@firebase/performance": "0.4.10",
        "@firebase/polyfill": "0.3.36",
        "@firebase/remote-config": "0.1.35",
        "@firebase/storage": "0.4.7",
        "@firebase/util": "0.4.1"
      }
    },
    "follow-redirects": {
      "version": "1.13.3",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.13.3.tgz",
      "integrity": "sha512-DUgl6+HDzB0iEptNQEXLx/KhTmDb8tZUHSeLqpnjpknR70H0nC2t9N73BK6fN4hOvJ84pKlIQVQ4k5FFlBedKA=="
    },
    "forwarded": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.1.2.tgz",
      "integrity": "sha1-mMI9qxF1ZXuMBXPozszZGw/xjIQ="
    },
    "fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha1-PYyt2Q2XZWn6g1qx+OSyOhBWBac="
    },
    "fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha1-FQStJSMVjKpA20onh8sBQRmU6k8="
    },
    "gaxios": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/gaxios/-/gaxios-4.2.0.tgz",
      "integrity": "sha512-Ms7fNifGv0XVU+6eIyL9LB7RVESeML9+cMvkwGS70xyD6w2Z80wl6RiqiJ9k1KFlJCUTQqFFc8tXmPQfSKUe8g==",
      "requires": {
        "abort-controller": "^3.0.0",
        "extend": "^3.0.2",
        "https-proxy-agent": "^5.0.0",
        "is-stream": "^2.0.0",
        "node-fetch": "^2.3.0"
      }
    },
    "gcp-metadata": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/gcp-metadata/-/gcp-metadata-4.2.1.tgz",
      "integrity": "sha512-tSk+REe5iq/N+K+SK1XjZJUrFPuDqGZVzCy2vocIHIGmPlTGsa8owXMJwGkrXr73NO0AzhPW4MF2DEHz7P2AVw==",
      "requires": {
        "gaxios": "^4.0.0",
        "json-bigint": "^1.0.0"
      }
    },
    "glob": {
      "version": "7.1.6",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.6.tgz",
      "integrity": "sha512-LwaxwyZ72Lk7vZINtNNrywX0ZuLyStrdDtabefZKAY5ZGJhVtgdznluResxNmPitE0SAO+O26sWTHeKSI2wMBA==",
      "requires": {
        "fs.realpath": "^1.0.0",
        "inflight": "^1.0.4",
        "inherits": "2",
        "minimatch": "^3.0.4",
        "once": "^1.3.0",
        "path-is-absolute": "^1.0.0"
      }
    },
    "google-auth-library": {
      "version": "6.1.6",
      "resolved": "https://registry.npmjs.org/google-auth-library/-/google-auth-library-6.1.6.tgz",
      "integrity": "sha512-Q+ZjUEvLQj/lrVHF/IQwRo6p3s8Nc44Zk/DALsN+ac3T4HY/g/3rrufkgtl+nZ1TW7DNAw5cTChdVp4apUXVgQ==",
      "requires": {
        "arrify": "^2.0.0",
        "base64-js": "^1.3.0",
        "ecdsa-sig-formatter": "^1.0.11",
        "fast-text-encoding": "^1.0.0",
        "gaxios": "^4.0.0",
        "gcp-metadata": "^4.2.0",
        "gtoken": "^5.0.4",
        "jws": "^4.0.0",
        "lru-cache": "^6.0.0"
      }
    },
    "google-p12-pem": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/google-p12-pem/-/google-p12-pem-3.0.3.tgz",
      "integrity": "sha512-wS0ek4ZtFx/ACKYF3JhyGe5kzH7pgiQ7J5otlumqR9psmWMYc+U9cErKlCYVYHoUaidXHdZ2xbo34kB+S+24hA==",
      "requires": {
        "node-forge": "^0.10.0"
      }
    },
    "gtoken": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/gtoken/-/gtoken-5.2.1.tgz",
      "integrity": "sha512-OY0BfPKe3QnMsY9MzTHTSKn+Vl2l1CcLe6BwDEQj00mbbkl5nyQ/7EUREstg4fQNZ8iYE7br4JJ7TdKeDOPWmw==",
      "requires": {
        "gaxios": "^4.0.0",
        "google-p12-pem": "^3.0.3",
        "jws": "^4.0.0"
      }
    },
    "heimdalljs": {
      "version": "0.2.6",
      "resolved": "https://registry.npmjs.org/heimdalljs/-/heimdalljs-0.2.6.tgz",
      "integrity": "sha512-o9bd30+5vLBvBtzCPwwGqpry2+n0Hi6H1+qwt6y+0kwRHGGF8TFIhJPmnuM0xO97zaKrDZMwO/V56fAnn8m/tA==",
      "requires": {
        "rsvp": "~3.2.1"
      },
      "dependencies": {
        "rsvp": {
          "version": "3.2.1",
          "resolved": "https://registry.npmjs.org/rsvp/-/rsvp-3.2.1.tgz",
          "integrity": "sha1-B8tKXfJa3Z6Cbrxn3Mn9idsn2Eo="
        }
      }
    },
    "http-errors": {
      "version": "1.7.2",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.7.2.tgz",
      "integrity": "sha512-uUQBt3H/cSIVfch6i1EuPNy/YsRSOUBXTVfZ+yR7Zjez3qjBz6i9+i4zjNaoqcoFVI4lQJ5plg63TvGfRSDCRg==",
      "requires": {
        "depd": "~1.1.2",
        "inherits": "2.0.3",
        "setprototypeof": "1.1.1",
        "statuses": ">= 1.5.0 < 2",
        "toidentifier": "1.0.0"
      }
    },
    "http-parser-js": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/http-parser-js/-/http-parser-js-0.5.3.tgz",
      "integrity": "sha512-t7hjvef/5HEK7RWTdUzVUhl8zkEu+LlaE0IYzdMuvbSDipxBRpOn4Uhw8ZyECEa808iVT8XCjzo6xmYt4CiLZg=="
    },
    "https-proxy-agent": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.0.tgz",
      "integrity": "sha512-EkYm5BcKUGiduxzSt3Eppko+PiNWNEpa4ySk9vTC6wDsQJW9rHSa+UhGNJoRYp7bz6Ht1eaRIa6QaJqO5rCFbA==",
      "requires": {
        "agent-base": "6",
        "debug": "4"
      },
      "dependencies": {
        "debug": {
          "version": "4.3.1",
          "resolved": "https://registry.npmjs.org/debug/-/debug-4.3.1.tgz",
          "integrity": "sha512-doEwdvm4PCeK4K3RQN2ZC2BYUBaxwLARCqZmMjtF8a51J2Rb0xpVloFRnCODwqjpwnAoao4pelN8l3RJdv3gRQ==",
          "requires": {
            "ms": "2.1.2"
          }
        },
        "ms": {
          "version": "2.1.2",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
          "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
        }
      }
    },
    "iconv-lite": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
      "integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
      "requires": {
        "safer-buffer": ">= 2.1.2 < 3"
      }
    },
    "idb": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/idb/-/idb-3.0.2.tgz",
      "integrity": "sha512-+FLa/0sTXqyux0o6C+i2lOR0VoS60LU/jzUo5xjfY6+7sEEgy4Gz1O7yFBXvjd7N0NyIGWIRg8DcQSLEG+VSPw=="
    },
    "ieee754": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
      "integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA=="
    },
    "inflight": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
      "integrity": "sha1-Sb1jMdfQLQwJvJEKEHW6gWW1bfk=",
      "requires": {
        "once": "^1.3.0",
        "wrappy": "1"
      }
    },
    "inherits": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
      "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4="
    },
    "ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g=="
    },
    "is-mac-address": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-mac-address/-/is-mac-address-1.0.4.tgz",
      "integrity": "sha1-9r/TN9dg0WiFZx0y2gJwMHgXbIU=",
      "requires": {
        "node-ratify": "~1.1.0"
      }
    },
    "is-stream": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-2.0.0.tgz",
      "integrity": "sha512-XCoy+WlUr7d1+Z8GgSuXmpuUFC9fOhRXglJMx+dwLKTkL44Cjd4W1Z5P+BQZpr+cR93aGP4S/s7Ftw6Nd/kiEw=="
    },
    "istextorbinary": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/istextorbinary/-/istextorbinary-2.6.0.tgz",
      "integrity": "sha512-+XRlFseT8B3L9KyjxxLjfXSLMuErKDsd8DBNrsaxoViABMEZlOSCstwmw0qpoFX3+U6yWU1yhLudAe6/lETGGA==",
      "requires": {
        "binaryextensions": "^2.1.2",
        "editions": "^2.2.0",
        "textextensions": "^2.5.0"
      }
    },
    "json-bigint": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/json-bigint/-/json-bigint-1.0.0.tgz",
      "integrity": "sha512-SiPv/8VpZuWbvLSMtTDU8hEfrZWg/mH/nV/b4o0CYbSxu1UIQPLdwKOCIyLQX+VIPO5vrLX3i8qtqFyhdPSUSQ==",
      "requires": {
        "bignumber.js": "^9.0.0"
      }
    },
    "jwa": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/jwa/-/jwa-2.0.0.tgz",
      "integrity": "sha512-jrZ2Qx916EA+fq9cEAeCROWPTfCwi1IVHqT2tapuqLEVVDKFDENFw1oL+MwrTvH6msKxsd1YTDVw6uKEcsrLEA==",
      "requires": {
        "buffer-equal-constant-time": "1.0.1",
        "ecdsa-sig-formatter": "1.0.11",
        "safe-buffer": "^5.0.1"
      }
    },
    "jws": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/jws/-/jws-4.0.0.tgz",
      "integrity": "sha512-KDncfTmOZoOMTFG4mBlG0qUIOlc03fmzH+ru6RgYVZhPkyiy/92Owlt/8UEN+a4TXR1FQetfIpJE8ApdvdVxTg==",
      "requires": {
        "jwa": "^2.0.0",
        "safe-buffer": "^5.0.1"
      }
    },
    "kareem": {
      "version": "2.3.2",
      "resolved": "https://registry.npmjs.org/kareem/-/kareem-2.3.2.tgz",
      "integrity": "sha512-STHz9P7X2L4Kwn72fA4rGyqyXdmrMSdxqHx9IXon/FXluXieaFA6KJ2upcHAHxQPQ0LeM/OjLrhFxifHewOALQ=="
    },
    "lodash.camelcase": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
      "integrity": "sha1-soqmKIorn8ZRA1x3EfZathkDMaY="
    },
    "long": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/long/-/long-4.0.0.tgz",
      "integrity": "sha512-XsP+KhQif4bjX1kbuSiySJFNAehNxgLb6hPRGJ9QsUr8ajHkuXGdrHmFUTUUXhDwVX2R5bY4JNZEwbUiMhV+MA=="
    },
    "lru-cache": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz",
      "integrity": "sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==",
      "requires": {
        "yallist": "^4.0.0"
      }
    },
    "media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha1-hxDXrwqmJvj/+hzgAWhUUmMlV0g="
    },
    "memory-pager": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/memory-pager/-/memory-pager-1.5.0.tgz",
      "integrity": "sha512-ZS4Bp4r/Zoeq6+NLJpP+0Zzm0pR8whtGPf1XExKLJBAczGMnSi3It14OiNCStjQjM6NU1okjQGSxgEZN8eBYKg==",
      "optional": true
    },
    "merge-descriptors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz",
      "integrity": "sha1-sAqqVW3YtEVoFQ7J0blT8/kMu2E="
    },
    "methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha1-VSmk1nZUE07cxSZmVoNbD4Ua/O4="
    },
    "mime": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
      "integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg=="
    },
    "mime-db": {
      "version": "1.47.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.47.0.tgz",
      "integrity": "sha512-QBmA/G2y+IfeS4oktet3qRZ+P5kPhCKRXxXnQEudYqUaEioAU1/Lq2us3D/t1Jfo4hE9REQPrbB7K5sOczJVIw=="
    },
    "mime-types": {
      "version": "2.1.30",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.30.tgz",
      "integrity": "sha512-crmjA4bLtR8m9qLpHvgxSChT+XoSlZi8J4n/aIdn3z92e/U47Z0V/yl+Wh9W046GgFVAmoNR/fmdbZYcSSIUeg==",
      "requires": {
        "mime-db": "1.47.0"
      }
    },
    "minimatch": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz",
      "integrity": "sha512-yJHVQEhyqPLUTgt9B83PXu6W3rx4MvvHvSUvToogpwoGDOUQ+yDrR0HRot+yOCdCO7u4hX3pWft6kWBBcqh0UA==",
      "requires": {
        "brace-expansion": "^1.1.7"
      }
    },
    "minimist": {
      "version": "1.2.5",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz",
      "integrity": "sha512-FM9nNUYrRBAELZQT3xeZQ7fmMOBg6nWNmJKTcgsJeaLstP/UODVpGsr5OhXhhXg6f+qtJ8uiZ+PUxkDWcgIXLw=="
    },
    "mkdirp": {
      "version": "0.5.5",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.5.tgz",
      "integrity": "sha512-NKmAlESf6jMGym1++R0Ra7wvhV+wFW63FaSOFPwRahvea0gMUcGUhVeAg/0BC0wiv9ih5NYPB1Wn1UEI1/L+xQ==",
      "requires": {
        "minimist": "^1.2.5"
      }
    },
    "mongodb": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/mongodb/-/mongodb-4.1.1.tgz",
      "integrity": "sha512-fbACrWEyvr6yl0sSiCGV0sqEiBwTtDJ8iSojmkDjAfw9JnOZSAkUyv9seFSPYhPPKwxp1PDtyjvBNfMDz0WBLQ==",
      "requires": {
        "bson": "^4.5.1",
        "denque": "^1.5.0",
        "mongodb-connection-string-url": "^2.0.0",
        "saslprep": "^1.0.0"
      }
    },
    "mongodb-connection-string-url": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/mongodb-connection-string-url/-/mongodb-connection-string-url-2.0.0.tgz",
      "integrity": "sha512-M0I1vyLoq5+HQTuPSJWbt+hIXsMCfE8sS1fS5mvP9R2DOMoi2ZD32yWqgBIITyu0dFu4qtS50erxKjvUeBiyog==",
      "requires": {
        "@types/whatwg-url": "^8.2.1",
        "whatwg-url": "^9.1.0"
      }
    },
    "mongoose": {
      "version": "6.0.5",
      "resolved": "https://registry.npmjs.org/mongoose/-/mongoose-6.0.5.tgz",
      "integrity": "sha512-1MoG52oosjEK8z45DHQVbakP6DJG1sbQI/ZASBW8sZRV+rCaG/pC3L3wWjrsiped/2+uhvanWM9C89F2n6bQ3w==",
      "requires": {
        "bson": "^4.2.2",
        "kareem": "2.3.2",
        "mongodb": "4.1.1",
        "mpath": "0.8.4",
        "mquery": "4.0.0",
        "ms": "2.1.2",
        "regexp-clone": "1.0.0",
        "sift": "13.5.2",
        "sliced": "1.0.1"
      },
      "dependencies": {
        "ms": {
          "version": "2.1.2",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
          "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
        }
      }
    },
    "mpath": {
      "version": "0.8.4",
      "resolved": "https://registry.npmjs.org/mpath/-/mpath-0.8.4.tgz",
      "integrity": "sha512-DTxNZomBcTWlrMW76jy1wvV37X/cNNxPW1y2Jzd4DZkAaC5ZGsm8bfGfNOthcDuRJujXLqiuS6o3Tpy0JEoh7g=="
    },
    "mquery": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/mquery/-/mquery-4.0.0.tgz",
      "integrity": "sha512-nGjm89lHja+T/b8cybAby6H0YgA4qYC/lx6UlwvHGqvTq8bDaNeCwl1sY8uRELrNbVWJzIihxVd+vphGGn1vBw==",
      "requires": {
        "debug": "4.x",
        "regexp-clone": "^1.0.0",
        "sliced": "1.0.1"
      },
      "dependencies": {
        "debug": {
          "version": "4.3.2",
          "resolved": "https://registry.npmjs.org/debug/-/debug-4.3.2.tgz",
          "integrity": "sha512-mOp8wKcvj7XxC78zLgw/ZA+6TSgkoE2C/ienthhRD298T7UNwAg9diBpLRxC0mOezLl4B0xV7M0cCO6P/O0Xhw==",
          "requires": {
            "ms": "2.1.2"
          }
        },
        "ms": {
          "version": "2.1.2",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
          "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
        }
      }
    },
    "ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
    },
    "negotiator": {
      "version": "0.6.2",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.2.tgz",
      "integrity": "sha512-hZXc7K2e+PgeI1eDBe/10Ard4ekbfrrqG8Ep+8Jmf4JID2bNg7NvCPOZN+kfF574pFQI7mum2AUqDidoKqcTOw=="
    },
    "node-fetch": {
      "version": "2.6.1",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.6.1.tgz",
      "integrity": "sha512-V4aYg89jEoVRxRb2fJdAg8FHvI7cEyYdVAh94HH0UIK8oJxUfkjlDQN9RbMx+bEjP7+ggMiFRprSti032Oipxw=="
    },
    "node-forge": {
      "version": "0.10.0",
      "resolved": "https://registry.npmjs.org/node-forge/-/node-forge-0.10.0.tgz",
      "integrity": "sha512-PPmu8eEeG9saEUvI97fm4OYxXVB6bFvyNTyiUOBichBpFG8A1Ljw3bY62+5oOjDEMHRnd0Y7HQ+x7uzxOzC6JA=="
    },
    "node-ratify": {
      "version": "1.1.32",
      "resolved": "https://registry.npmjs.org/node-ratify/-/node-ratify-1.1.32.tgz",
      "integrity": "sha1-OVeDfyyu2Du2G5mS21N9BSHbLfU="
    },
    "object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha1-IQmtx5ZYh8/AXLvUQsrIv7s2CGM="
    },
    "on-finished": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz",
      "integrity": "sha1-IPEzZIGwg811M3mSoWlxqi2QaUc=",
      "requires": {
        "ee-first": "1.1.1"
      }
    },
    "once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha1-WDsap3WWHUsROsF9nFC6753Xa9E=",
      "requires": {
        "wrappy": "1"
      }
    },
    "parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ=="
    },
    "path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha1-F0uSaHNVNP+8es5r9TpanhtcX18="
    },
    "path-to-regexp": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz",
      "integrity": "sha1-32BBeABfUi8V60SQ5yR6G/qmf4w="
    },
    "promise-polyfill": {
      "version": "8.1.3",
      "resolved": "https://registry.npmjs.org/promise-polyfill/-/promise-polyfill-8.1.3.tgz",
      "integrity": "sha512-MG5r82wBzh7pSKDRa9y+vllNHz3e3d4CNj1PQE4BQYxLme0gKYYBm9YENq+UkEikyZ0XbiGWxYlVw3Rl9O/U8g=="
    },
    "protobufjs": {
      "version": "6.10.2",
      "resolved": "https://registry.npmjs.org/protobufjs/-/protobufjs-6.10.2.tgz",
      "integrity": "sha512-27yj+04uF6ya9l+qfpH187aqEzfCF4+Uit0I9ZBQVqK09hk/SQzKa2MUqUpXaVa7LOFRg1TSSr3lVxGOk6c0SQ==",
      "requires": {
        "@protobufjs/aspromise": "^1.1.2",
        "@protobufjs/base64": "^1.1.2",
        "@protobufjs/codegen": "^2.0.4",
        "@protobufjs/eventemitter": "^1.1.0",
        "@protobufjs/fetch": "^1.1.0",
        "@protobufjs/float": "^1.0.2",
        "@protobufjs/inquire": "^1.1.0",
        "@protobufjs/path": "^1.1.2",
        "@protobufjs/pool": "^1.1.0",
        "@protobufjs/utf8": "^1.1.0",
        "@types/long": "^4.0.1",
        "@types/node": "^13.7.0",
        "long": "^4.0.0"
      },
      "dependencies": {
        "@types/node": {
          "version": "13.13.48",
          "resolved": "https://registry.npmjs.org/@types/node/-/node-13.13.48.tgz",
          "integrity": "sha512-z8wvSsgWQzkr4sVuMEEOvwMdOQjiRY2Y/ZW4fDfjfe3+TfQrZqFKOthBgk2RnVEmtOKrkwdZ7uTvsxTBLjKGDQ=="
        }
      }
    },
    "proxy-addr": {
      "version": "2.0.6",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.6.tgz",
      "integrity": "sha512-dh/frvCBVmSsDYzw6n926jv974gddhkFPfiN8hPOi30Wax25QZyZEGveluCgliBnqmuM+UJmBErbAUFIoDbjOw==",
      "requires": {
        "forwarded": "~0.1.2",
        "ipaddr.js": "1.9.1"
      }
    },
    "punycode": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz",
      "integrity": "sha512-XRsRjdf+j5ml+y/6GKHPZbrF/8p2Yga0JPtdqTIY2Xe5ohJPD9saDJJLPvp9+NSBprVvevdXZybnj2cv8OEd0A=="
    },
    "qs": {
      "version": "6.7.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.7.0.tgz",
      "integrity": "sha512-VCdBRNFTX1fyE7Nb6FYoURo/SPe62QCaAyzJvUjwRaIsc+NePBEniHlvxFmmX56+HZphIGtV0XeCirBtpDrTyQ=="
    },
    "range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg=="
    },
    "raw-body": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.4.0.tgz",
      "integrity": "sha512-4Oz8DUIwdvoa5qMJelxipzi/iJIi40O5cGV1wNYp5hvZP8ZN0T+jiNkL0QepXs+EsQ9XJ8ipEDoiH70ySUJP3Q==",
      "requires": {
        "bytes": "3.1.0",
        "http-errors": "1.7.2",
        "iconv-lite": "0.4.24",
        "unpipe": "1.0.0"
      }
    },
    "regexp-clone": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/regexp-clone/-/regexp-clone-1.0.0.tgz",
      "integrity": "sha512-TuAasHQNamyyJ2hb97IuBEif4qBHGjPHBS64sZwytpLEqtBQ1gPJTnOaQ6qmpET16cK14kkjbazl6+p0RRv0yw=="
    },
    "rimraf": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz",
      "integrity": "sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==",
      "requires": {
        "glob": "^7.1.3"
      }
    },
    "rsvp": {
      "version": "4.8.5",
      "resolved": "https://registry.npmjs.org/rsvp/-/rsvp-4.8.5.tgz",
      "integrity": "sha512-nfMOlASu9OnRJo1mbEk2cz0D56a1MBNrJ7orjRZQG10XDyuvwksKbuXNp6qa+kbn839HwjwhBzhFmdsaEAfauA=="
    },
    "safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="
    },
    "safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg=="
    },
    "saslprep": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/saslprep/-/saslprep-1.0.3.tgz",
      "integrity": "sha512-/MY/PEMbk2SuY5sScONwhUDsV2p77Znkb/q3nSVstq/yQzYJOH/Azh29p9oJLsl3LnQwSvZDKagDGBsBwSooag==",
      "optional": true,
      "requires": {
        "sparse-bitfield": "^3.0.3"
      }
    },
    "semver": {
      "version": "6.3.0",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.0.tgz",
      "integrity": "sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw=="
    },
    "send": {
      "version": "0.17.1",
      "resolved": "https://registry.npmjs.org/send/-/send-0.17.1.tgz",
      "integrity": "sha512-BsVKsiGcQMFwT8UxypobUKyv7irCNRHk1T0G680vk88yf6LBByGcZJOTJCrTP2xVN6yI+XjPJcNuE3V4fT9sAg==",
      "requires": {
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "destroy": "~1.0.4",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "0.5.2",
        "http-errors": "~1.7.2",
        "mime": "1.6.0",
        "ms": "2.1.1",
        "on-finished": "~2.3.0",
        "range-parser": "~1.2.1",
        "statuses": "~1.5.0"
      },
      "dependencies": {
        "ms": {
          "version": "2.1.1",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.1.tgz",
          "integrity": "sha512-tgp+dl5cGk28utYktBsrFqA7HKgrhgPsg6Z/EfhWI4gl1Hwq8B/GmY/0oXZ6nF8hDVesS/FpnYaD/kOWhYQvyg=="
        }
      }
    },
    "serve-static": {
      "version": "1.14.1",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.14.1.tgz",
      "integrity": "sha512-JMrvUwE54emCYWlTI+hGrGv5I8dEwmco/00EvkzIIsR7MqrHonbD9pO2MOfFnpFntl7ecpZs+3mW+XbQZu9QCg==",
      "requires": {
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.3",
        "send": "0.17.1"
      }
    },
    "setprototypeof": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.1.tgz",
      "integrity": "sha512-JvdAWfbXeIGaZ9cILp38HntZSFSo3mWg6xGcJJsd+d4aRMOqauag1C63dJfDw7OaMYwEbHMOxEZ1lqVRYP2OAw=="
    },
    "sift": {
      "version": "13.5.2",
      "resolved": "https://registry.npmjs.org/sift/-/sift-13.5.2.tgz",
      "integrity": "sha512-+gxdEOMA2J+AI+fVsCqeNn7Tgx3M9ZN9jdi95939l1IJ8cZsqS8sqpJyOkic2SJk+1+98Uwryt/gL6XDaV+UZA=="
    },
    "sliced": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/sliced/-/sliced-1.0.1.tgz",
      "integrity": "sha1-CzpmK10Ewxd7GSa+qCsD+Dei70E="
    },
    "sparse-bitfield": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/sparse-bitfield/-/sparse-bitfield-3.0.3.tgz",
      "integrity": "sha1-/0rm5oZWBWuks+eSqzM004JzyhE=",
      "optional": true,
      "requires": {
        "memory-pager": "^1.0.2"
      }
    },
    "statuses": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz",
      "integrity": "sha1-Fhx9rBd2Wf2YEfQ3cfqZOBR4Yow="
    },
    "textextensions": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/textextensions/-/textextensions-2.6.0.tgz",
      "integrity": "sha512-49WtAWS+tcsy93dRt6P0P3AMD2m5PvXRhuEA0kaXos5ZLlujtYmpmFsB+QvWUSxE1ZsstmYXfQ7L40+EcQgpAQ=="
    },
    "toidentifier": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.0.tgz",
      "integrity": "sha512-yaOH/Pk/VEhBWWTlhI+qXxDFXlejDGcQipMlyxda9nthulaxLZUNcUqFxokp0vcYnvteJln5FNQDRrxj3YcbVw=="
    },
    "tr46": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/tr46/-/tr46-2.1.0.tgz",
      "integrity": "sha512-15Ih7phfcdP5YxqiB+iDtLoaTz4Nd35+IiAv0kQ5FNKHzXgdWqPoTIqEDDJmXceQt4JZk6lVPT8lnDlPpGDppw==",
      "requires": {
        "punycode": "^2.1.1"
      }
    },
    "tslib": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.2.0.tgz",
      "integrity": "sha512-gS9GVHRU+RGn5KQM2rllAlR3dU6m7AcpJKdtH8gFvQiC4Otgk98XnmMU+nZenHt/+VhnBPWwgrJsyrdcw6i23w=="
    },
    "type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "requires": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      }
    },
    "unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha1-sr9O6FFKrmFltIF4KdIbLvSZBOw="
    },
    "username-sync": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/username-sync/-/username-sync-1.0.2.tgz",
      "integrity": "sha512-ayNkOJdoNSGNDBE46Nkc+l6IXmeugbzahZLSMkwvgRWv5y5ZqNY2IrzcgmkR4z32sj1W3tM3TuTUMqkqBzO+RA=="
    },
    "utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha1-n5VxD1CiZ5R7LMwSR0HBAoQn5xM="
    },
    "vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha1-IpnwLG3tMNSllhsLn3RSShj2NPw="
    },
    "webidl-conversions": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-6.1.0.tgz",
      "integrity": "sha512-qBIvFLGiBpLjfwmYAaHPXsn+ho5xZnGvyGvsarywGNc8VyQJUMHJ8OBKGGrPER0okBeMDaan4mNBlgBROxuI8w=="
    },
    "websocket-driver": {
      "version": "0.7.4",
      "resolved": "https://registry.npmjs.org/websocket-driver/-/websocket-driver-0.7.4.tgz",
      "integrity": "sha512-b17KeDIQVjvb0ssuSDF2cYXSg2iztliJ4B9WdsuB6J952qCPKmnVq4DyW5motImXHDC1cBT/1UezrJVsKw5zjg==",
      "requires": {
        "http-parser-js": ">=0.5.1",
        "safe-buffer": ">=5.1.0",
        "websocket-extensions": ">=0.1.1"
      }
    },
    "websocket-extensions": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/websocket-extensions/-/websocket-extensions-0.1.4.tgz",
      "integrity": "sha512-OqedPIGOfsDlo31UNwYbCFMSaO9m9G/0faIHj5/dZFDMFqPTcx6UwqyOy3COEaEOg/9VsGIpdqn62W5KhoKSpg=="
    },
    "whatwg-fetch": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.4.tgz",
      "integrity": "sha512-dcQ1GWpOD/eEQ97k66aiEVpNnapVj90/+R+SXTPYGHpYBBypfKJEQjLrvMZ7YXbKm21gXd4NcuxUTjiv1YtLng=="
    },
    "whatwg-url": {
      "version": "9.1.0",
      "resolved": "https://registry.npmjs.org/whatwg-url/-/whatwg-url-9.1.0.tgz",
      "integrity": "sha512-CQ0UcrPHyomtlOCot1TL77WyMIm/bCwrJ2D6AOKGwEczU9EpyoqAokfqrf/MioU9kHcMsmJZcg1egXix2KYEsA==",
      "requires": {
        "tr46": "^2.1.0",
        "webidl-conversions": "^6.1.0"
      }
    },
    "wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha1-tSQ9jz7BqjXxNkYFvA0QNuMKtp8="
    },
    "xmlhttprequest": {
      "version": "1.8.0",
      "resolved": "https://registry.npmjs.org/xmlhttprequest/-/xmlhttprequest-1.8.0.tgz",
      "integrity": "sha1-Z/4HXFwk/vOfnWX197f+dRcZaPw="
    },
    "yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A=="
    }
  }
}
================================================

File: package.json
================================================
{
  "name": "macvendor",
  "version": "1.0.0",
  "description": "",
  "main": "node mac_cek.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "async-disk-cache": "^2.1.0",
    "axios": "^0.21.1",
    "body-parser": "^1.19.0",
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "firebase": "^8.3.3",
    "is-mac-address": "^1.0.4",
    "mongoose": "^6.0.5"
  }
}