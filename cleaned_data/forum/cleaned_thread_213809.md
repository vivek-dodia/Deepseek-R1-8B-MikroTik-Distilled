# Thread Information
Title: Thread-213809
Section: RouterOS
Thread ID: 213809

# Discussion

## Initial Question
I'd like a firewall rule to block any inbound https request where the URI string contains "cart.pl" but the cookie named "VISA" is missing. ---

## Response 1
Hard task ... almost impossible with ROS.simple forum search gives thatviewtopic.php?p=1112124&hilit=http+leve ... r#p1112124 ---

## Response 2
Since this seems to be part of a Webshop, it might be better to setup a reverse proxy (eg. with nginx) in front of your server(s) to filter those requests. Also you might consider using this Proxy to have your TLS (HTTPS) connection handling, which might add to the overall performance. ---