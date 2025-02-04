# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208636

# Discussion

## Initial Question
Author: [SOLVED]Wed Jun 26, 2024 12:52 pm
``` curl -s -u x:y -X DELETE http://abc.com/rest/ppp/active/xyz ``` ``` for id in $(curl -s -u x:y http://abc.com/rest/ppp/active?name=xyz | jq -r '.[] | .".id"') do curl -s -u x:y -X DELETE http://abc.com/rest/ppp/active/$id done ``` ``` curl -s -u x:y http://abc.com/rest/log \ | jq -r '.[] | select (.topics | contains("ppp")) | select (.message | (contains("xyz logged in") or contains("xyz logged out"))) | .message' \ | tail -n 50 ``` I am trying to remove a user from ppp where it is like xyzWhen you are certain that only one entry exists for the user (ppp profile only-one=yes), you can DELETE by name:
```
When multiple entries exist for the user (or could exist, e.g. only-one=no), you will have to query and run DELETE for every result:
```

```
also to get last 50 entries filtered by a specific ppp user from the log from memory - is that possible with curl?From the documentation -https://help.mikrotik.com/docs/display/ROS/REST+APIAnd further:https://help.mikrotik.com/docs/display/ ... PI-QueriesRegular expressions are not supported in API, so do not try to send a query with the ~ symbolSo filtering has to be done client side, to fetch the last 50 lines from log:
```