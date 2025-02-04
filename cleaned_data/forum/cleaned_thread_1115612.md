# Thread Information
Title: Thread-1115612
Section: RouterOS
Thread ID: 1115612

# Discussion

## Initial Question
Dear Ladies and Gents!Since years we do have the RB912R-2nD with several hundret units in the field.We mainly use them for LTE backup for DSL connected sites.What else we have:own APNown Radius ServerProvider: T-Mobile AustriaThe HUGE problem:Since the launch of the NEW EC200A Modems it is not possibe to have routed networks behind a interface assigned IP.e.g.: Framed IP on interface: lte1 172.16.1.1Framed route on lo0: 172.16.5.1/interface lteset [ find default-name=lte1 ] allow-roaming=yes band="" network-mode=lte/interface lte apnset [ find default=yes ] apn=myapn authentication=chap ip-type=ipv4 password=password use-network-apn=no user=myuser/interface lte settingsset sim-slot=down/ip addressadd address=172.16.5.1/32 interface=lo0 network=172.16.5.1Before the EC200 i saw packets arriving, when pulling a pcap, fpr 172.16.5.1, since the EC200 they do NOT show up at all.I've tried it as well with the actual 7.16.2, as with 7.17rc3Firmware @R11E: MikroTik_CP_2.160.000_v021FW @Quectel EC200A: EC200AEUHAR01A19M16Behavior is reproduceable.Does any face the same situation or habe a solution for us?Greetings from Vienna, roland ---

## Response 1
Already checked with support ? ---

## Response 2
Yes, and unfortunately this is a known issue.Will be solved in the release of the EC200A firmware, but without a date.So beware of currently using the RB912 version 2004 with routed networks.luckily I have some old ones, but lets look, how long they last.The "hAP ax lite LTE6" are within the same price category, and they work. But I don't wanna have to widen my portfolio...greetings from rainy Vienna, roland ---