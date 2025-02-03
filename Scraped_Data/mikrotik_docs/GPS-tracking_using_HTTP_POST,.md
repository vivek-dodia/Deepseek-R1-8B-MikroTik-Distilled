---
title: GPS-tracking using HTTP POST
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/84901903/GPS-tracking+using+HTTP+POST,
crawled_date: 2025-02-02T21:11:22.327112
section: mikrotik_docs
type: documentation
---

The following article explains how to create a simple vehicle tracking system using the RouterOS GPS function and scripting.
# Method
This approach uses HTTP POST capability of RouterOS Fetch tool. It allows you to POST any kind of data to a webserver, right from the RouterOS command line. Of course, you can use scripting, to fill the POST data with variables. The posted data will be written to an SQLITE3 database (file is created, if it doesn't exist) and then, read from the database and fed into a Leaflet.js PolyLine array. This is a proof of concept example, there is no authentication, security, or error handling.
# Requirements
* Web server of your choice
* PHP
* SQLite3 module for PHP
* RouterOS device with a working GPS module
* RouterOS
* Set GPS format in RouterOS todd
# RouterOS script
You can run this script in the Scheduler tool, with an interval of 1s, to have your coordinates sent every 1 second.
```
{
:global lat
:global lon
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
}
tool fetch mode=http url="http://YOURSERVER.com/index.php" port=80 http-method=post http-data=("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}") http-header-field="Content-Type: application/json" 
:put ("{\"lat\":\"" . $lat . "\",\"lon\":\"" . $lon . "\"}")
}
```
# index.php file
Create an empty directory calledsqlite_dbnext to the index.php file. Make sure that directory and files are writable by the group withchmod -R a+w sqlite_db/
```
<?php
$loc = dirname(__FILE__).'/sqlite_db/coord.db';
$db = new SQLite3($loc,SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE);
$raw = file_get_contents('php://input');
$raw = preg_replace('/\\x00/','',$raw);
$data = json_decode($raw);
if (!empty($data) && is_object($data) && property_exists($data,'lat') && property_exists($data,'lon')){
    if(file_exists($loc)) echo 'exists!'.chr(0xa);
    $src = 'SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'coordinates\'';
    $res = $db->querySingle($src);
    if (count($res)==0){
            $db->exec('CREATE TABLE coordinates (latitude TEXT, longitude TEXT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, added TIMESTAMP DEFAULT CURRENT_TIMESTAMP ) ');
    }
$regex = '/^(|\-)([0-9]{2,3}\.[0-9]{0,8})$/';
if (preg_match($regex,$data->lat) && preg_match($regex,$data->lon) )
	{
		$lat = $data->lat;
		$lon = $data->lon;
	}
	$ins = 'INSERT INTO coordinates (latitude,longitude) VALUES (\''.SQLite3::escapeString($lat).'\',\''.SQLite3::escapeString($lon).'\')';
	$db->exec($ins);
	die();
}
?>
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
</head>
<body>
<div id="map" style="width: 800px; height: 600px;"></div>
<script>
var map = L.map('map').setView([0,0], 4);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: '<a href="http://osm.org/copyright">OSM</a>'}).addTo(map);
<?php
    if($result = $db->query('SELECT latitude,longitude FROM coordinates')){
    echo ' var latlngs = [ ';
    while($obj = $result->fetchArray()){
    	if (!is_array($obj) || !isset($obj['latitude']) || !isset($obj['longitude']) || empty($obj['latitude']) || empty($obj['longitude'])) continue;
    	echo '["'. $obj['latitude'].'","'.$obj['longitude'].'"],';
    }
    echo ']; ';
    } else
     echo('//'.$db->lastErrorMsg().chr(0xa));  
	 echo($data);
?>
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
map.fitBounds(polyline.getBounds());
</script>
</body>
</html>
```
# Result