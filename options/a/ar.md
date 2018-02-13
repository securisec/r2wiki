<!-- TITLE: ar -->

#  `ar[?]`   like 'dr' but for the esil vm. (registers)

- `ar` Show 'gpr' registers
- `ar0` Reset register arenas to 0

- [ `ara[?]` Manage register arenas](/options/a/ar/ara)

- `ar 16` Show 16 bit registers
- `ar 32` Show 32 bit registers
- `ar all` Show all bit registers
- `ar <type>` Show all registers of given type
- `arC` Display register profile comments
- `arr` Show register references (telescoping)
- `ar=` Show register values in columns
- `ar? <reg>` Show register value
- `arb <type>` Display hexdump of the given arena
- `arc <name>` Conditional flag registers
- `ard <name>` Show only different registers
- `arn <regalias>` Get regname for pc,sp,bp,a0-3,zf,cf,of,sg
- `aro` Show old (previous) register values
- `arp[?] <file>` Load register profile from file
- `ars` Stack register state
- `art` List all register types
- `arw <hexnum>` Set contents of the register arena
- `.ar*` Import register values as flags
- `.ar-` Unflag all registers