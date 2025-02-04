# Thread Information
Title: Thread-1120993
Section: RouterOS
Thread ID: 1120993

# Discussion

## Initial Question
Hi mikrotikers!I have 3 Mikrotik routers using Wireguard peers and no one is showing Client Config and Client QR in WebFig or Winbox.All have latest firmware, but this have been happening since many firmware updates before.Any clues why this could happen?Captura de pantalla 2025-01-22 a las 17.46.44.png ---

## Response 1
You need to populate the "Client XXX" parameters with values. Their content (plus the value of Private Key in the upper section, plus the Port and Public Key from the Wireguard interface configuration) is used to generate the QR-Code and the Client Config output. ---