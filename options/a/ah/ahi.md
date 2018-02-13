<!-- TITLE: ahi -->

#  `ahi[?] 10` define numeric base for immediates (1, 8, 10, 16, s)

- `ahi [base]` set numeric base (1, 2, 8, 10, 16)
	> `ahi` can be used to change how a value looks or is represented
- `ahi b` set base to binary (2)
- `ahi d` set base to decimal (10)
- `ahi h` set base to hexadecimal (16)
- `ahi o` set base to octal (8)
- `ahi p` set base to htons(port) (3)
- `ahi i` set base to IP address (32)
- `ahi S` set base to syscall (80)
- `ahi s` set base to string (1)
  - Example: Convert to string

     `ahi s @@=0x080485a3 0x080485ad 0x080485b7` ( `@@=` helps specify multiple offsets).

    ![](/uploads/a-afvd/ahi.png) 

    > `ahi` _Forcefully convert value to string_

<p hidden>ahi</p>
