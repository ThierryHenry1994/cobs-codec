# Consistent Overhead Byte Stuffing (COBS) Codec

Python algorithm demo for COBS

## What Is COBS?

COBS is a method of encoding a packet of bytes into a form that contains no bytes with value zero (0x00). The input packet of bytes can contain bytes in the full range of 0x00 to 0xFF. The COBS encoded packet is guaranteed to generate packets with bytes only in the range 0x01 to 0xFF. Thus, in a communication protocol, packet boundaries can be reliably delimited with 0x00 bytes.

The COBS encoding does have to increase the packet size to achieve this encoding. However, compared to other byte-stuffing methods, the packet size increase is reasonable and predictable. COBS always adds 1 byte to the message length. Additionally, for longer packets of length *n*, it *may* add n/254 (rounded down) additional bytes to the encoded packet size.

For example, compare to the PPP protocol, which uses 0x7E bytes to delimit PPP packets. The PPP protocol uses an "escape" style of byte stuffing, replacing all occurences of 0x7E bytes in the packet with 0x7D 0x5E. But that byte-stuffing method can potentially double the size of the packet in the worst case. COBS uses a different method for byte-stuffing, which has a much more reasonable worst-case overhead.

Details in https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing .



## Test Result

| Example | Unencoded data (hex)  |                   Encoded with COBS (hex)                    | Encode Result                           | Decode Result                           |
| :-----: | :-------------------: | :----------------------------------------------------------: | --------------------------------------- | --------------------------------------- |
|    1    |          00           | <span style="color: red;">01</span> <span style="color: green;">01</span> <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    2    |         00 00         | <span style="color: red;">01</span> <span style="color: green;">01</span> <span style="color: green;">01</span> <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    3    |       00 11 00        | <span style="color: red;">01</span> <span style="color: green;">02</span> **11** <span style="color: green;">01</span> <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    4    |      11 22 00 33      | <span style="color: red;">03</span> **11 22** <span style="color: green;">02</span> **33** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    5    |      11 22 33 44      | <span style="color: red;">05</span> **11 22 33 44** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    6    |      11 00 00 00      | <span style="color: red;">02</span> **11** <span style="color: green;">01</span> <span style="color: green;">01</span> <span style="color: red;">01</span> <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    7    |  01 02 03 ... FD FE   | <span style="color: red;">FF</span> **01 02 03 ... FD FE** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    8    | 00 01 02 ... FC FD FE | <span style="color: red;">01</span> <span style="color: green;">FF</span> **01 02 ... FC FD FE** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|    9    | 01 02 03 ... FD FE FF | <span style="color: red;">FF</span> **01 02 03 ... FD FE** <span style="color: red;">02</span> **FF** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|   10    | 02 03 04 ... FE FF 00 | <span style="color: red;">FF</span> **02 03 04 ... FE FF** <span style="color: red;">01</span> <span style="color: green;">01</span> <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |
|   11    | 03 04 05 ... FF 00 01 | <span style="color: red;">FE</span> **03 04 05 ... FF** <span style="color: green;">02</span> **01** <span style="color: blue;">00</span> | <span style="color: green;">Pass</span> | <span style="color: green;">Pass</span> |

## License

The code is released under the MIT license. See LICENSE for details.



If you find this project useful or helpful to you, please give stars. Thanks