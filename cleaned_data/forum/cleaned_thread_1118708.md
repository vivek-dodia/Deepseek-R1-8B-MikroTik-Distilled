# Thread Information
Title: Thread-1118708
Section: RouterOS
Thread ID: 1118708

# Discussion

## Initial Question
Hi folks, is there any MikroTik device which supports PoE-out with Mode A?I know the wiki (https://help.mikrotik.com/docs/spaces/R ... 69/PoE-Out) says "no" but I'm hardly searching a solution for powering DoorBird systems without an additional power supply.MikroTik devices utilize an RJ45 mode B pinout for power deliveryAny ideas? ---

## Response 1
Doorbird is a strange Beast.It declares 802.3af Mode A, which Is against the specs, as 802.3af PD's should be compatibile with BOTH mode A and mode B.Anyway, the question is which specific devices we are talking of, both the Mikrotik and the Doorbird.If the interfaces are 10/100 It Is relatively easy, if they are 1000 It becomes more difficult and costly:https://www.planet.com.tw/en/product/poe-e201-v2This Is a PoE extender, but It accepts both Mode A and Mode B in (as a compliant PD) and outputs Mode A (on the out side It Is a PSE and can decide which mode).Or two of these:https://shopify.poe-world.com/products/ ... 4-pair-poeand a short ethernet cable between them.But It has to be seen of the Doorbird powers on with these ("passive 802.3af/at" Is another abomination). ---

## Response 2
Exactly, jaclaz! You got the point.I'm especially talking about CRS328-24P-4S+RM and the DoorBird D1101V.Best solution would be Digitus DN-95130 (https://www.assmann.com/product-pdf/apl ... 5890?PL=en) which isn't available since years.All other options require an additional power sourceDoorBird A1093https://www.doorbird.com/shop/?ean=4260423913868TP-Link TL-PoE150Shttps://www.amazon.de/-/en/TL-POE150S-I ... S9E5I?th=1Ubiquiti PoE-50-60Whttps://www.omg.de/ubiquiti-networks/po ... il/a-13285 ---

## Response 3
Naah, the Planet one Is generally available, but It Is not cheap, example:https://www.digitx.it/codice/c-poe_e201 ... od-115326/70 €!Of course if you arewastinginvesting the awful amount of money a Doorbird costs, It could be fine. ---

## Response 4
Oh, this device really looks promising!Will try it!Thank you very much! ---