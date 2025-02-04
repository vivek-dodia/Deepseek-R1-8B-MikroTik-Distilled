# Thread Information
Title: Thread-1114661
Section: RouterOS
Thread ID: 1114661

# Discussion

## Initial Question
Hi, I'm pretty fine reading any kind of registers with the KNOT device via the transceive command, like/iot modbus transceive address=1 function=1 data=00000006 (read 6 coil registers from 0 - 5, it will return a decimal number what can be processed to become digitals)/iot modbus transceive address=1 function=2 data=00000009 (read 9 discrete registers from 0 - 8, it will return a decimal number what can be processed to become digitals)/iot modbus transceive address=1 function=3 data=000000AA (read 170 holding registers from 0 - 169, it will return 170 decimal numbers in an array)/iot modbus transceive address=1 function=4 data=000000AA (read 170 input registers from 0 - 169, it will return 170 decimal numbers in an array)I would like to write the coil registers with function 5 or 15 and write holding registers with function 6 or 16, but based on the description, I'm not able to find how to do that.Any example code is appreciated.Thank you. ---

## Response 1
I think that the issue is that the data does not represent the same things with different functions.Or if you prefer each function has different arguments.Check this:https://www.fernhillsoftware.com/help/d ... tocol.htmlwith this:function=3 data=000000AAyou are actually sending03 (read) 0000=First input address (from) 00AA=Register count (amount)Function 5 has arguments:05 (write) First coil address (offset) Coil value (can only be two values 0000 or FF00 or 0/1, off/on) <- here it has to be understood if FF should be 00FF or FF00 in Mikrotik syntax, likely FF00, but needs to be verifiedCheck also this online parser:https://rapidscada.net/modbus/try using this value (last two bytes are checksum, that i presume ROS calculates automatically, to play with the parser, add - say - ABCD, the parser will throw an error but provide the correct checksum that you can use to replace the ABCD placeholder):10050000FF008F7B
```
PartofDataPackageDescriptionValue10Slaveaddress0x10(16)05Functioncode0x05(5)-WriteSingleCoil0000OutputaddressPhysical:0x0000(0)Logical:0x0001(1)FF00OutputvalueOn8F7BCRC0x8F7B(36731)value:1003000000AAC6F4
```

```
PartofDataPackageDescriptionValue10Slaveaddress0x10(16)03Functioncode0x03(3)-ReadHoldingRegisters0000StartingaddressPhysical:0x0000(0)Logical:0x0001(1)00AAQuantity0x00AA(170)C6 F4 	CRC0xC6F4(50932)

---
```

## Response 2
write single holding register as integer:/iot modbus transceive address=1 function=6 values=a2, a1, v2, v1a2 - high byte of register addressa1 - low byte of register addressv2 - high byte of valuev1 - low byte of valueas hexadecimal:/iot modbus transceive address=1 function=6 data=A2A1V2V1set value 10 to register at address 1
```
/iot modbus transceive address=1function=6values=0,1,0,10/iot modbus transceive address=1function=6data=0001000Awrite multiple holding registers as integer:/iot modbus transceive address=1 function=16 values=a2,a1,c2,c1,b,v12,v11,v22,v21...a2 - high byte of first register addressa1 - low byte of  first register addressc2 - high byte of registers countc1 - low byte of registers countb - count of bytes next (count of bytes in message)v12,v11 - high and low bytes of first valuev22,v21 - high and low bytes of second valueas hexadecimal:/iot modbus transceive address=1 function=16 data=A2A1C2C1BBV2V1V2V1set value 10 to register at address 1 and value 20 to register at address 2
```

```
/iot modbus transceive address=1function=16values=0,1,0,2,4,0,10,0,20/iot modbus transceive address=1function=16data=0001000204000A0014REST API
```

```
POST http://router/rest/iot/modbus/transceive{"address":1,"function":16,"values":"0,1,0,2,4,0,10,0,20"}And let remind once again, this applies not only to KNOT, you can connect USB/RS485 adapter to any MikroTik with USB and install IoT package.

---
```