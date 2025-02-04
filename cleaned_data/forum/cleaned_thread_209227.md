# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209227

# Discussion

## Initial Question
Author: [SOLVED]Fri Jul 12, 2024 11:47 pm
``` :put[:convertfrom=raw to=base64"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"] ``` ``` :put[:convertfrom=base64 to=raw"QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkrLw=="] ``` ``` :put[:convertfrom=base64 to=byte-array"QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkrLw=="] ``` You should check out the new ":convert" operator in V7. For example, to get base64 string from the alphabet:
```
QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODkrLw==And reverse works too:
```

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/There is even a "byte-array" pseudo-type, so if you want an array on the ASCII int values from a base64-encoded string, that too is possible:
```

```
65;66;67;68;69;70;71;72;73;74;75;76;77;78;79;80;81;82;83;84;85;86;87;88;89;90;97;98;99;100;101;102;103;104;105;106;107;108;109;110;111;112;113;114;115;116;117;118;119;120;121;122;48;49;50;51;52;53;54;55;56;57;43;47which is the same ABCD...xyz...789+/, as num type in array of those ascii codes.The "raw" in to=raw or from=raw just mean "RouterOS string" for purposes here.
```