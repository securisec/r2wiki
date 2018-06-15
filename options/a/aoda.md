<!-- TITLE: aoda -->

# aoda show all mnemonic descriptions
`aaa` ascii adjust after addition
`aad` ascii adjust ax before division
`aam` ascii adjust ax after multiply
`aas` ascii adjust al after subtraction
`adc` add with carry
`adcx` unsigned integer addition of two operands with carry flag
`add` adds src and dst, stores result on dst
`addpd` add packed double-fp values
`addps` add packed single-fp values
`addsd` add scalar double-fp values
`addss` add scalar single-fp values
`addsubpd` packed double-fp add/subtract
`addsubps` packed single-fp add/subtract
`adox` unsigned integer addition of two operands with overflow flag
`aesdec` perform one round of an AES decryption flow
`aesdeclast` perform the last round of an AES decryption flow
`aesenc` perform one round of an AES encryption flow
`aesenclast` perform the last round of an AES encryption flow
`aesimc` assist in aes Inverse Mix Columns
`aeskeygenassist` assist in AES round key generation
`and` binary and operation between src and dst, stores result on dst
`andn` logical and not
`andnpd` bitwise logical and not of packed double-fp values
`andnps` bitwise logical and not of packed single-fp values
`andpd` bitwise logical and of packed double-fp values
`andps` bitwise logical and of packed single-fp values
`arpl` adjust rpl field of segment selector
`bextr` bit field extract
`blendpd` blend packed double-fp values
`blendps` blend packed single-fp values
`blendvpd` variable blend packed double-fp values
`blendvps` variable blend packed single-fp values
`blsi` extract lowest set isolated bit
`blsmsk` get mask up to lowest set bit
`blsr` reset lowest set bit
`bndcl` check lower bound
`bndcn` check upper bound
`bndcu` check upper bound
`bndldx` load extended bounds using address translation
`bndmk` make bounds
`bndmov` move bounds
`bndstx` store extended bounds using address translation
`bound` check array index against bounds
`bsf` bit scan forward
`bsr` bit scan reverse
`bswap` byte swap
`bt` bit test
`btc` bit test and complement
`btr` bit test and reset
`bts` bit test and set
`bzhi` zero high bits starting with specified bit position
`call` calls a subroutine, push eip into the stack (esp)
`cbw` convert byte to word
`cdq` sign extends eax into edx (convert doubleword to quadword)
`cdqe` sign extend eax into rax
`clac` clear ac flag in eflags register
`clc` clear carry flag
`cld` clear direction flag
`clflush` flush cache line
`clflushopt` flush cache line optimized
`cli` clear interrupt flag
`clts` clear task-switched flag in cr0
`cmc` complement carry flag
`cmova` conditional move - above/not below nor equal (cf=0 and zf=0)
`cmovae` conditional move - above or equal/not below/not carry (cf=0)
`cmovb` conditional move - below/not above nor equal/carry (cf=1)
`cmovbe` conditional move - below or equal/not above (cf=1 or zf=1)
`cmovc` conditional move - carry/below/not above or equal (cf=1)
`cmove` conditional move - equal/zero (zf=1)
`cmovg` conditional move - greater/not less nor equal (zf=0 and sf=of)
`cmovge` conditional move - greater or equal/not less (sf=of)
`cmovl` conditional move - less/not greater nor equal (sf!=of)
`cmovle` conditional move - less or equal/not greater (zf=1 or sf!=of)
`cmovna` conditional move - not above/below or equal (cf=1 or zf=1)
`cmovnae` conditional move - not above nor equal/below/carry (cf=1)
`cmovnb` conditional move - not below/above or equal/not carry (cf=0)
`cmp` compare two operands
`cmppd` compare packed double-fp values
`cmpps` compare packed single-fp values
`cmps` compare string operands
`cmpsb` cmp DS:[esi], (byte)ES:[edi] (esi++, edi++)
`cmpsd` cmp DS:[esi], (dword)ES:[edi] (esi+=4, edi+=4)/compare scalar double-fp values
`cmpsq` cmp DS:[rsi], (qword)ES:[rdi] (rsi+=8, rdi+=8)
`cmpss` compare scalar single-fp values
`cmpsw` cmp DS:[esi], (word)ES:[edi] (esi+=2, edi+=2)
`cmpxchg` compare and exchange
`cmpxchg16b` compare and exchange bytes
`cmpxchg8b` compare and exchange bytes
`comisd` compare scalar ordered double-fp values and set eflags
`comiss` compare scalar ordered single-fp values and set eflags
`cpuid` cpu identification
`cqo` sign extends rax into rdx (convert quadword to double-quadword)
`crc32` accumulate crc32 value
`cvtdq2pd` convert packed dw integers to double-fp values
`cvtdq2ps` convert packed dw integers to single-fp values
`cvtpd2dq` convert packed double-fp values to dw integers
`cvtpd2pi` convert packed double-fp values to dw integers
`cvtpd2ps` convert packed double-fp values to single-fp values
`cvtpi2pd` convert packed dw integers to double-fp values
`cvtpi2ps` convert packed dw integers to single-fp values
`cvtps2dq` convert packed single-fp values to dw integers
`cvtps2pd` convert packed single-fp values to double-fp values
`cvtps2pi` convert packed single-fp values to dw integers
`cvtsd2si` convert scalar double-fp value to dw integer
`cvtsd2ss` convert scalar double-fp value to scalar single-fp value
`cvtsi2sd` convert dw integer to scalar double-fp value
`cvtsi2ss` convert dw integer to scalar single-fp value
`cvtss2sd` convert scalar single-fp value to scalar double-fp value
`cvtss2si` convert scalar single-fp value to dw integer
`cvttpd2dq` convert with trunc. packed double-fp values to dw integers
`cvttpd2pi` convert with trunc. packed double-fp values to dw integers
`cvttps2dq` convert with trunc. packed single-fp values to dw integers
`cvttps2pi` convert with trunc. packed single-fp values to dw integers
`cvttsd2si` conv. with trunc. scalar double-fp value to signed dw int
`cvttss2si` convert with trunc. scalar single-fp value to dw integer
`cwd` convert word to doubleword
`cwde` convert word to doubleword
`daa` decimal adjust al after addition
`das` decimal adjust al after subtraction
`dec` decrement by 1
`div` unsigned divide
`divpd` divide packed double-fp values
`divps` divide packed single-fp values
`divsd` divide scalar double-fp values
`divss` divide scalar single-fp values
`dppd` dot product of packed double-fp values
`dpps` dot product of packed single-fp values
`emms` empty mmx technology state
`enter` alias for push ebp; mov ebp, esp
`extractps` extract packed single-fp value
`f2xm1` compute pow(2,x) - 1
`fabs` absolute value
`fadd` floating point add
`faddp` floating point add and pop
`fbld` load binary coded decimal
`fbstp` store binary coded decimal integer and pop
`fchs` change sign
`fclex` clear exceptions
`fcmovb` fp conditional move - below (cf=1)
`fcmovbe` fp conditional move - below or equal (cf=1 or zf=1)
`fcmove` fp conditional move - equal (zf=1)
`fcmovnb` fp conditional move - not below (cf=0)
`fcmovnbe` fp conditional move - not below or equal (cf=0 and zf=0)
`fcmovne` fp conditional move - not equal (zf=0)
`fcmovu` fp conditional move - unordered (pf=1)
`fcom` floating point compare
`fcomi` compare floating point values and set eflags
`fcomip` compare floating point values and set eflags and pop
`fcomp` floating point compare and pop
`fcompp` floating point compare and pop twice
`fcos` floating point cosine
`fdecstp` decrement floating point stack pointer
`fdiv` floating point divide
`fdivp` floting point divide and pop
`fdivr` floating point divide reversed
`fdivrp` floating point reverse divide and pop
`ffree` free floating-point register
`fiadd` integer add
`ficom` integer compare
`ficomp` integer compare and pop
`fidiv` integer divide
`fidivr` integer divide reserved
`fild` load integer
`fimul` integer multiply
`fincstp` increment floating-point stack pointer
`finit` initialize fpu (floating-point unit)
`fist` store integer
`fistp` store integer and pop
`fisttp` store integer with truncation and pop
`fisub` integer substract
`fisubr` integer susbtract reversed
`fld` load floating point value
`fld1` load constant onto stack +1.0f
`fldcw` load x87 fpu control word
`fldenv` load x87 fpu environment
`fldl2e` load constant onto stack: logarithm base 2 (e)
`fldl2t` load constant onto stack: logarithm base 2 (10)
`fldlg2` load constant onto stack: logarithm base 10 (2)
`fldln2` load constant onto stack: natural logarithm (2)
`fldpi` load constant onto stack: pi (3.141592...)
`fldz` load constant onto stack 0.0f
`fmul` floating point multiply
`fmulp` floating point multiply and pop
`fnclex` clear exceptions
`fninit` initialize fpu (floating-point unit)
`fnop` no operation
`fnsave` store x87 fpu state
`fnstcw` store x87 fpu control word
`fnstenv` store x87 fpu environment
`fnstsw` store x87 fpu status word
`fpatan` partial arctangent and pop
`fprem` partial remainder (for compatibility with i8087 and i287)
`fprem1` ieee partial remainder
`fptan` partial tangent
`frndint` round to integer
`frstor` restore x87 fpu state
`fsave` store x87 fpu state
`fscale` scale
`fsin` sine
`fsincos` sine and cosine
`fsqrt` square root
`fst` store floating point value
`fstcw` store x87 fpu control word
`fstenv` store x87 fpu environment
`fstp` store floating point value and pop
`fstsw` store x87 fpu status word
`fsub` floating point subtract
`fsubp` subtract and pop
`fsubr` reverse subtract
`fsubrp` reverse subtract and pop
`ftst` test
`fucom` unordered compare floating point values
`fucomi` unordered compare floating point values and set eflags
`fucomip` unordered compare floating point values and set eflags and pop
`fucomp` unordered compare floating point values and pop
`fucompp` unordered compare floating point values and pop twice
`fwait` check pending unmasked floating-point exceptions
`fxam` examine
`fxch` exchange register contents
`fxrstor` restore x87 fpu, mmx, xmm, and mxcsr state
`fxsave` save x87 fpu, mmx, xmm, and mxcsr state
`fxtract` extract exponent and significand
`fyl2x` compute y times log2(x) and pop
`fyl2xp1` compute y times log2(x+1) and pop
`haddpd` packed double-fp horizontal add
`haddps` packed single-fp horizontal add
`hlt` stop process until external interrupt received
`hsubpd` packed double-fp horizontal subtract
`hsubps` packed single-fp horizontal subtract
`idiv` signed divide
`imul` signed multiply
`in` input from port
`inc` increment by 1
`ins` input from port to string
`insb` input from port to string
`insd` input from port to string
`insertps` insert scalar single-precision floating-point value
`insw` input from port to string
`int` call to interrupt procedure
`int` 3=call to interrupt procedure
`into` call to interrupt if overflow
`invd` invalidate internal caches
`invlpg` invalidate tlb entry
`invpcid` invalidate process-context identifier
`iret` return from interrupt
`iretd` interrupt return
`ja` jump short if above (cf=0 and zf=0)
`jae` jump short if above or equal (cf=0)
`jb` jump short if below/not above nor equal/carry (cf=1)
`jbe` jump short if below or equal/not above (cf=1 or zf=1)
`jc` jump short if carry (cf=1)
`jcxz` jump short if ecx register is 0
`je` jump short if equal (zf=1)
`jecxz` jump short if ecx is 0
`jg` jump short if greater (zf=0 and sf=of)
`jge` jump short if greater or equal (sf=of)
`jl` jump short if less/not greater (sf!=of)
`jle` jump short if less or equal/not greater (zf=1 or sf!=of)
`jmp` jump
`jna` jump short if not above/equal (cf=1 or zf=1)
`jnae` jump short if not above nor equal/below (cf=1)
`jnb` jump short if not below/above or equal/not carry (cf=0)
`jnbe` jump short if not below or equal/above (cf=0 and zf=0)
`jnc` jump short if not carry (cf=0)
`jne` jump short if not equal/not zero (zf=0)
`jng` jump short if not greater/less or equal (zf=1 or sf!=of)
`jnge` jump short if not greater/less (sf!=of)
`jnl` jump short if not less/greater or equal (sf=of)
`jnle` jump short if not less nor equal/greater (zf=0 and sf=of)
`jno` jump short if not overflow (of=0)
`jnp` jump short if not parity/parity odd (pf=0)
`jns` jump short if not sign (sf=0)
`jnz` jump short if not zero/not equal (zf=0)
`jo` jump short if overflow (of=1)
`jp` jump short if parity/parity even (pf=1)
`jpe` jump short if parity even/parity (pf=1)
`jpo` jump short if parity odd/not parity (pf=0)
`jrcxz` jump short if rcx register is 0
`js` jump short if sign (sf=1)
`jz` jump short if zero/equal (zf=1)
`kaddb` add two masks
`kaddd` add two masks
`kaddq` add two masks
`kaddw` add two masks
`kandb` bitwise logical and masks
`kandd` bitwise logical and masks
`kandnb` bitwise logical and not masks
`kandnd` bitwise logical and not masks
`kandnq` bitwise logical and not masks
`kandnw` bitwise logical and not masks
`kandq` bitwise logical and masks
`kandw` bitwise logical and masks
`kmovb` move from and to mask registers
`kmovd` move from and to mask registers
`kmovq` move from and to mask registers
`kmovw` move from and to mask registers
`knotb` not mask register
`knotd` not mask register
`knotq` not mask register
`knotw` not mask register
`korb` bitwise logical or masks
`kord` bitwise logical or masks
`korq` bitwise logical or masks
`kortestb` or masks and set flags
`kortestd` or masks and set flags
`kortestq` or masks and set flags
`kortestw` or masks and set flags
`korw` bitwise logical or masks
`kshiftlb` shift left mask registers
`kshiftld` shift left mask registers
`kshiftlq` shift left mask registers
`kshiftlw` shift left mask registers
`kshiftrb` shift right mask registers
`kshiftrd` shift right mask registers
`kshiftrq` shift right mask registers
`kshiftrw` shift right mask registers
`ktestb` packed bit test masks and set flags
`ktestd` packed bit test masks and set flags
`ktestq` packed bit test masks and set flags
`ktestw` packed bit test masks and set flags
`kunpckbw` unpack for mask registers
`kunpckdq` unpack for mask registers
`kunpckwd` unpack for mask registers
`kxnorb` bitwise logical xnor masks
`kxnord` bitwise logical xnor masks
`kxnorq` bitwise logical xnor masks
`kxnorw` bitwise logical xnor masks
`kxorb` bitwise logical xor masks
`kxord` bitwise logical xor masks
`kxorq` bitwise logical xor masks
`kxorw` bitwise logical xor masks
`lahf` load status flags into ah register
`lar` load acces right byte
`lddqu` load unaligned integer 128 bits
`ldmxcsr` load mxcsr register
`lds` load far pointer
`lea` load effective address
`leave` one byte alias for mov esp, ebp ; pop ebp
`les` load far pointer
`lfence` load fence
`lfs` load far pointer
`lgdt` load global descriptor table register
`lgs` load far pointer
`lidt` load interrupt descriptor table register
`lldt` load local descriptor table register
`lmsw` load machine status word
`lock` instruction prefix to setup the LOCK pin
`lods` load string
`lodsb` Load string byte
`lodsd` Load string doubleword
`lodsq` Load string quadword
`lodsw` Load string word
`loop` decrement count; jump short if ecx!=0
`loope` decrement count; jump short if ecx!=0 and zf=1
`loopne` decrement count; jump short if ecx!=0 and zf=0
`loopnz` decrement count; jump short if ecx!=0 and zf=0
`loopz` decrement count; jump short if ecx!=0 and zf=1
`lsl` load segment limit
`lss` load far pointer
`ltr` load task register
`lzcnt` count the number of leading zero bits
`maskmovdqu` store selected bytes of double quadword
`maskmovq` store selected bytes of quadword
`maxpd` return maximum packed double-fp values
`maxps` return maximum packed single-fp values
`maxsd` return maximum scalar double-fp value
`maxss` return maximum scalar single-fp value
`mfence` memory fence
`minpd` return minimum packed double-fp values
`minps` return minimum packed single-fp values
`minsd` return minimum scalar double-fp value
`minss` return minimum scalar single-fp value
`monitor` set up monitor address
`mov` moves data from src to dst
`movapd` move aligned packed double-fp values
`movaps` move aligned packed single-fp values
`movbe` move data after swapping bytes
`movd` move doubleword
`movddup` move one double-fp and duplicate
`movdq2q` move quadword from xmm to mmx technology register
`movdqa` move aligned double quadword
`movdqu` move unaligned double quadword
`movhlps` move packed single-fp values high to low
`movhpd` move high packed double-fp value
`movhps` move high packed single-fp values
`movlhps` move packed single-fp values low to high
`movlpd` move low packed double-fp value
`movlps` move low packed single-fp values
`movmskpd` extract packed double-fp sign mask
`movmskps` extract packed single-fp sign mask
`movntdq` store double quadword using non-temporal hint
`movntdqa` load double quadword non-temporal aligned hint
`movnti` store doubleword using non-temporal hint
`movntpd` store packed double-fp values using non-temporal hint
`movntps` store packed single-fp values using non-temporal hint
`movntq` store of quadword using non-temporal hint
`movq` move quadword
`movq2dq` move quadword from mmx technology to xmm register
`movs` move data from string to string
`movsb` ES:[edi] = (byte)DS:[esi] (esi++, edi++)
`movsd` ES:[edi] = (dword)DS:[esi] (esi+=4, edi+=4)/move scalar double-fp value
`movshdup` move packed single-fp high and duplicate
`movsldup` move packed single-fp low and duplicate
`movsq` ES:[rdi] = (qword)DS:[rsi] (rsi+=8, rdi+=8)
`movss` move scalar single-fp values
`movsw` ES:[edi] = (word)DS:[esi] (esi+=2, edi+=2)
`movsx` move with sign-extension
`movsxd` move with sign-extension
`movupd` move unaligned packed double-fp values
`movups` move unaligned packed single-fp values
`movzx` move dst register size padding with zeroes
`mpsadbw` compute multiple packed sums of absolute difference
`mul` unsigned multiply
`mulpd` multiply packed double-fp values
`mulps` multiply packed single-fp values
`mulsd` multiply scalar double-fp values
`mulss` multiply scalar single-fp value
`mulx` unsigned multiply without affecting flags
`mwait` monitor wait
`neg` two's complement negation
`nop` no operation
`not` one's complement negation
`or` logical inclusive or
`orpd` bitwise logical or of double-fp values
`orps` bitwise logical or of single-fp values
`out` output to port
`outs` output string to port
`outsb` Output string byte to port
`outsd` Output string doubleword to port
`outsw` Output string word to port
`pabsb` packed absolute value
`pabsd` packed absolute value
`pabsq` packed absolute value
`pabsw` packed absolute value
`packssdw` pack with signed saturation
`packsswb` pack with signed saturation
`packusdw` pack with unsigned saturation
`packuswb` pack with unsigned saturation
`paddb` add packed integers
`paddd` add packed integers
`paddq` add packed quadword integers
`paddsb` add packed signed integers with signed saturation
`paddsw` add packed signed integers with signed saturation
`paddusb` add packed unsigned integers with unsigned saturation
`paddusw` add packed unsigned integers with unsigned saturation
`paddw` add packed integers
`palignr` packed align right
`pand` logical and
`pandn` logical and not
`pause` spin loop hint
`pavgb` average packed integers
`pavgw` average packed integers
`pblendvb` variable blend packed bytes
`pblendw` blend packed words
`pclmulqdq` performs a carry-less multiplication of two 64-bit polynomials over the finite field GF(2).
`pcmpeqb` compare packed data for equal
`pcmpeqd` compare packed data for equal
`pcmpeqq` compare packed qword data for equal
`pcmpeqw` compare packed data for equal
`pcmpestri` packed compare explicit length strings, return index
`pcmpestrm` packed compare explicit length strings, return mask
`pcmpgtb` compare packed signed integers for greater than
`pcmpgtd` compare packed signed integers for greater than
`pcmpgtq` compare packed data for greater than
`pcmpgtw` compare packed signed integers for greater than
`pcmpistri` packed compare implicit length strings, return index
`pcmpistrm` packed compare implicit length strings, return mask
`pdep` parallel bits deposit
`pext` parallel bits extract
`pextrb` extract a byte from an XMM register and insert the value into a general-purpose register or memory
`pextrd` extract a dword from an XMM register and insert the value into a general-purpose register or memory
`pextrq` extract a qword from an XMM register and insert the value into a general-purpose register or memory
`pextrw` extract a word from an XMM register and insert the value into a general-purpose register or memory
`phaddd` packed horizontal add
`phaddsw` packed horizontal add and saturate
`phaddw` packed horizontal add
`phminposuw` packed horizontal word minimum
`phsubd` packed horizontal subtract
`phsubsw` packed horizontal subtract and saturate
`phsubw` packed horizontal subtract
`pinsrb` insert a byte value from a register or memory into an XMM register
`pinsrd` insert a dword value from a register or memory into an XMM register
`pinsrq` insert a qword value from a register or memory into an XMM register
`pinsrw` insert a word value from a register or memory into an XMM register
`pmaddubsw` multiply and add packed signed and unsigned bytes
`pmaddwd` multiply and add packed integers
`pmaxsb` maximum of packed signed byte integers
`pmaxsd` maximum of packed signed dword integers
`pmaxsq` maximum of packed signed integers
`pmaxsw` maximum of packed signed word integers
`pmaxub` maximum of packed unsigned byte integers
`pmaxud` maximum of packed unsigned dword integers
`pmaxuq` maximum of packed unsigned integers
`pmaxuw` maximum of packed unsigned word integers
`pminsb` minimum of packed signed byte integers
`pminsd` minimum of packed signed dword integers
`pminsq` minimum of packed signed integers
`pminsw` minimum of packed signed word integers
`pminub` minimum of packed unsigned byte integers
`pminud` minimum of packed unsigned dword integers
`pminuq` minimum of packed unsigned integers
`pminuw` minimum of packed unsigned word integers
`pmovmskb` move byte mask
`pmovsxbd` sign extend the lower 8-bit integer of each packed dword element into packed signed dword integers
`pmovsxbq` sign extend the lower 8-bit integer of each packed qword element into packed signed qword integers
`pmovsxbw` sign extend the lower 8-bit integer of each packed word element into packed signed word integers
`pmovsxdq` sign extend the lower 32-bit integer of each packed qword element into packed signed qword integers
`pmovsxwd` sign extend the lower 16-bit integer of each packed dword element into packed signed dword integers
`pmovsxwq` sign extend the lower 16-bit integer of each packed qword element into packed signed qword integers
`pmovzxbd` zero extend the lower 8-bit integer of each packed dword element into packed signed dword integers
`pmovzxbq` zero extend the lower 8-bit integer of each packed qword element into packed signed qword integers
`pmovzxbw` zero extend the lower 8-bit integer of each packed word element into packed signed word integers
`pmovzxdq` zero extend the lower 32-bit integer of each packed qword element into packed signed qword integers
`pmovzxwd` zero extend the lower 16-bit integer of each packed dword element into packed signed dword integers
`pmovzxwq` zero extend the lower 16-bit integer of each packed qword element into packed signed qword integers
`pmuldq` multiply packed doubleword integers
`pmulhrsw` packed multiply high with round and scale
`pmulhuw` multiply packed unsigned integers and store high result
`pmulhw` multiply packed signed integers and store high result
`pmulld` multiply packed signed dword integers and store low result
`pmullq` multiply packed integers and store low result
`pmullw` multiply packed signed integers and store low result
`pmuludq` multiply packed unsigned dw integers
`pop` pops last element of stack and stores the result in argument
`popa` pop all general-purpose registers
`popad` pop all general-purpose registers
`popcnt` bit population count
`popf` pop stack into flags register
`popfd` pop stack into eflags register
`popfq` pop stack into rflags register
`por` bitwise logical or
`prefetchnta` prefetch data into caches
`prefetcht0` prefetch data into caches
`prefetcht1` prefetch data into caches
`prefetcht2` prefetch data into caches
`prefetchw` prefetch data into caches
`prefetchwt1` prefetch vector data into caches with intent to write and t1 hint
`prold` bit rotate left
`prolq` bit rotate left
`prolvd` bit rotate left
`prolvq` bit rotate left
`prord` bit rotate right
`prorq` bit rotate right
`prorvd` bit rotate right
`prorvq` bit rotate right
`psadbw` compute sum of absolute differences
`pshufb` packed shuffle bytes
`pshufd` shuffle packed doublewords
`pshufhw` shuffle packed high words
`pshuflw` shuffle packed low words
`pshufw` shuffle packed words
`psignb` packed sign
`psignd` packed sign
`psignw` packed sign
`pslld` shift packed data left logical
`pslldq` shift double quadword left logical
`psllq` shift packed data left logical
`psllw` shift packed data left logical
`psrad` shift packed data right arithmetic
`psraq` shift packed data right arithmetic
`psraw` shift packed data right arithmetic
`psrld` shift packed data right logical
`psrldq` shift double quadword right logical
`psrlq` shift packed data right logical
`psrlw` shift packed data right logical
`psubb` subtract packed integers
`psubd` subtract packed integers
`psubq` subtract packed quadword integers
`psubsb` subtract packed signed integers with signed saturation
`psubsw` subtract packed signed integers with signed saturation
`psubusb` subtract packed unsigned integers with unsigned saturation
`psubusw` subtract packed unsigned integers with unsigned saturation
`psubw` subtract packed integers
`ptest` logical compare
`ptwrite` ptwrite - write data to a processor trace packet
`punpckhbw` unpack high data
`punpckhdq` unpack high data
`punpckhqdq` unpack high data
`punpckhwd` unpack high data
`punpcklbw` unpack low data
`punpckldq` unpack low data
`punpcklqdq` unpack low data
`punpcklwd` unpack low data
`push` push word, doubleword or quadword onto the stack
`pusha` push all general-purpose registers
`pushad` push all general-purpose registers
`pushf` push flags register onto the stack
`pushfd` push eflags register onto the stack
`pxor` logical exclusive or
`rcl` rotate bits left (with CF)
`rcpps` compute reciprocals of packed single-fp values
`rcpss` compute reciprocal of scalar single-fp values
`rcr` rotate bits right (with CF)
`rdfsbase` read fs/gs segment base
`rdgsbase` read fs/gs segment base
`rdmsr` read from model specific register
`rdpid` read processor id
`rdpkru` read protection key rights for user pages
`rdpmc` read performance-monitoring counters
`rdrand` read random number
`rdseed` read random seed
`rdtsc` read time-stamp counter
`rdtscp` read time-stamp counter and processor id
`rep` ins=repeat string operation prefix
`rep` lods=repeat string operation prefix
`rep` movs=repeat string operation prefix
`rep` outs=repeat string operation prefix
`rep` stos=repeat string operation prefix
`repe` cmps=repeat string operation prefix
`repe` scas=repeat string operation prefix
`repne` cmps=repeat string operation prefix
`repne` scas=repeat string operation prefix
`ret` return from subroutine. pop 4 bytes from esp and jump there.
`rol` rotate bits left
`ror` rotate bits right
`rorx` rotate right logical without affecting flags
`roundpd` round packed double-fp values
`roundps` round packed single-fp values
`roundsd` round scalar double-fp values
`roundss` round scalar single-fp values
`rsm` resume from system management mode
`rsqrtps` compute recipr. of square roots of packed single-fp values
`rsqrtss` compute recipr. of square root of scalar single-fp value
`sahf` store ah into flags
`sal` arithmetic left shift
`sar` arithmetic right shift
`sarx` shift without affecting flags
`sbb` integer subtraction with borrow
`scas` scan string
`scasb` cmp al, ES:[edi++]
`scasd` cmp eax, ES:[edi+=4]
`scasw` cmp ax, ES:[edi+=2]
`seta` set byte on condition - above/not below nor equal (cf=0 and zf=0)
`setae` set byte on condition - above or equal/not below/not carry (cf=0)
`setb` set byte on condition - below/not above nor equal/carry (cf=1)
`setbe` set byte on condition - below or equal/not above (cf=1 or zf=1)
`setc` set byte on condition - carry/below/not above nor equal (cf=1)
`sete` set byte on condition - equal/zero (zf=1)
`setg` set byte on condition - greater/not less nor equal (zf=0 and sf=of)
`setge` set byte on condition - greater or equal/not less (sf=of)
`setl` set byte on condition - less/not greater nor equal (sf!=of)
`setle` set byte on condition - less or equal/not greater (zf=1 or sf!=of)
`setna` set byte on condition - not above/below or equal (cf=1 or zf=1)
`setnae` set byte on condition - not above nor equal/below/carry (cf=1)
`setnb` set byte on condition - not below/above or equal/not carry (cf=0)
`setnbe` set byte on condition - not below nor equal/above (cf=0 and zf=0)
`setnc` set byte on condition - not carry/above or equal/not below (cf=0)
`setne` set byte on condition - not equal/not zero (zf=0)
`setng` set byte on condition - not greater/less or equal (zf=1 or sf!=of)
`setnge` set byte on condition - not greater nor equal/less (sf!=of)
`setnl` set byte on condition - not less/greater or equal (sf=of)
`setno` set byte on condition - not overflow (of=0)
`setnp` set byte on condition - not parity/parity odd (pf=0)
`setns` set byte on condition - not sign (sf=0)
`setnz` set byte on condition - not zero/not equal (zf=0)
`seto` set byte on condition - overflow (of=1)
`setp` set byte on condition - parity/parity even (pf=1)
`setpe` set byte on condition - parity even/parity (pf=1)
`setpo` set byte on condition - parity odd/not parity (pf=0)
`sets` set byte on condition - sign (sf=1)
`setz` set byte on condition - zero/equal (zf=1)
`sfence` store fence
`sgdt` store global descriptor table register
`sha1msg1` perform an intermediate calculation for the next four sha1 message dwords
`sha1msg2` perform a final calculation for the next four sha1 message dwords
`sha1nexte` calculate sha1 state variable e after four rounds
`sha1rnds4` perform four rounds of sha1 operation
`sha256msg1` perform an intermediate calculation for the next four sha256 message dwords
`sha256msg2` perform a final calculation for the next four sha256 message dwords
`sha256rnds2` perform two rounds of sha256 operation
`shl` logic left shift (0 padding)
`shld` double precision shift left
`shlx` shift without affecting flags
`shr` logic right shift (0 padding)
`shrd` double precision shift right
`shrx` shift without affecting flags
`shufpd` shuffle packed double-fp values
`shufps` shuffle packed single-fp values
`sidt` store interrupt descriptor table register
`sldt` store local descriptor table register.
`smsw` store machine status word
`sqrtpd` compute square roots of packed double-fp values
`sqrtps` compute square roots of packed single-fp values
`sqrtsd` compute square root of scalar double-fp value
`sqrtss` compute square root of scalar single-fp value
`stac` set ac flag in eflags register
`stc` set carry flag
`std` set direction flag
`sti` set interrupt flag
`stmxcsr` store mxcsr register state
`stos` store string
`stosb` store string byte
`stosd` store string dword
`stosq` store string quadword
`stosw` store string word
`str` store task register
`sub` substract src and dst, stores result on dst
`subpd` subtract packed double-fp values
`subps` subtract packed single-fp values
`subsd` subtract scalar double-fp values
`subss` subtract scalar single-fp values
`swapgs` swap gs base register
`syscall` fast system call
`sysenter` fast system call
`sysexit` fast return from fast system call
`sysret` return from fast system call
`test` set eflags after comparing two registers (AF, CF, OF, PF, SF, ZF)
`tzcnt` count the number of trailing zero bits
`ucomisd` unordered compare scalar double-fp values and set eflags
`ucomiss` unordered compare scalar single-fp values and set eflags
`ud2` undefined instruction
`unpckhpd` unpack and interleave high packed double-fp values
`unpckhps` unpack and interleave high packed single-fp values
`unpcklpd` unpack and interleave low packed double-fp values
`unpcklps` unpack and interleave low packed single-fp values
`vaddpd` add packed double-precision floating-point values
`vaddps` add packed single-precision floating-point values
`vaddsd` add scalar double-precision floating-point values
`vaddss` add scalar single-precision floating-point values
`vaddsubpd` packed double-fp add/subtract
`vaddsubps` packed single-fp add/subtract
`vaesdec` perform one round of an aes decryption flow
`vaesdeclast` perform last round of an aes decryption flow
`vaesenc` perform one round of an aes encryption flow
`vaesenclast` perform last round of an aes encryption flow
`vaesimc` perform the aes invmixcolumn transformation
`vaeskeygenassist` aes round key generation assist
`valignd` align doubleword/quadword vectors
`valignq` align doubleword/quadword vectors
`vandnpd` bitwise logical and not of packed double precision floating-point values
`vandnps` bitwise logical and not of packed single precision floating-point values
`vandpd` bitwise logical and of packed double precision floating-point values
`vandps` bitwise logical and of packed single precision floating-point values
`vblendmpd` blend float64/float32 vectors using an opmask control
`vblendmps` blend float64/float32 vectors using an opmask control
`vblendpd` blend packed double precision floating-point values
`vblendps` blend packed single precision floating-point values
`vblendvpd` variable blend packed double precision floating-point values
`vblendvps` variable blend packed single precision floating-point values
`vbroadcastf128` load with broadcast floating-point data
`vbroadcastf32x2` load with broadcast floating-point data
`vbroadcastf32x4` load with broadcast floating-point data
`vbroadcastf32x8` load with broadcast floating-point data
`vbroadcastf64x2` load with broadcast floating-point data
`vbroadcastf64x4` load with broadcast floating-point data
`vbroadcasti32x8` load integer and broadcast
`vbroadcasti32x2` load integer and broadcast
`vbroadcasti64x4` load integer and broadcast
`vbroadcastsd` load with broadcast floating-point data
`vbroadcastss` load with broadcast floating-point data
`vcmppd` compare packed double-precision floating-point values
`vcmpps` compare packed single-precision floating-point values
`vcmpsd` compare scalar double-precision floating-point value
`vcmpss` compare scalar single-precision floating-point value
`vcomisd` compare scalar ordered double-precision floating-point values and set eflags
`vcomiss` compare scalar ordered single-precision floating-point values and set eflags
`vcompresspd` store sparse packed double-precision floating-point values into dense memory
`vcompressps` store sparse packed single-precision floating-point values into dense memory
`vcvtdq2pd` convert packed doubleword integers to packed double-precision floating-point values
`vcvtdq2ps` convert packed doubleword integers to packed single-precision floating-point values
`vcvtpd2dq` convert packed double-precision floating-point values to packed doubleword integers
`vcvtpd2ps` convert packed double-precision floating-point values to packed single-precision floating-point values
`vcvtpd2qq` convert packed double-precision floating-point values to packed quadword integers
`vcvtpd2udq` convert packed double-precision floating-point values to packed unsigned doubleword integers
`vcvtpd2uqq` convert packed double-precision floating-point values to packed unsigned quadword integers
`vcvtph2ps` convert 16-bit fp values to single-precision fp values
`vcvtps2dq` convert packed single-precision floating-point values to packed signed doubleword integer values
`vcvtps2pd` convert packed single-precision floating-point values to packed double-precision floating-point values
`vcvtps2ph` convert single-precision fp value to 16-bit fp value
`vcvtps2qq` convert packed single precision floating-point values to packed singed quadword integer values
`vcvtps2udq` convert packed single-precision floating-point values to packed unsigned doubleword integer values
`vcvtps2uqq` convert packed single precision floating-point values to packed unsigned quadword integer values
`vcvtqq2pd` convert packed quadword integers to packed double-precision floating-point values
`vcvtqq2ps` convert packed quadword integers to packed single-precision floating-point values
`vcvtsd2si` convert scalar double-precision floating-point value to doubleword integer
`vcvtsd2ss` convert scalar double-precision floating-point value to scalar single-precision floating-point value
`vcvtsd2usi` convert scalar double-precision floating-point value to unsigned doubleword integer
`vcvtsi2sd` convert doubleword integer to scalar double-precision floating-point value
`vcvtsi2ss` convert doubleword integer to scalar single-precision floating-point value
`vcvtss2sd` convert scalar single-precision floating-point value to scalar double-precision floating-point value
`vcvtss2si` convert scalar single-precision floating-point value to doubleword integer
`vcvtss2usi` convert scalar single-precision floating-point value to unsigned doubleword integer
`vcvttpd2dq` convert with truncation packed double-precision floating-point values to packed doubleword integers
`vcvttpd2qq` convert with truncation packed double-precision floating-point values to packed quadword integers
`vcvttpd2udq` convert with truncation packed double-precision floating-point values to packed unsigned doubleword integers
`vcvttpd2uqq` convert with truncation packed double-precision floating-point values to packed unsigned quadword integers
`vcvttps2dq` convert with truncation packed single-precision floating-point values to packed signed doubleword integer values
`vcvttps2qq` convert with truncation packed single precision floating-point values to packed singed quadword integer values
`vcvttps2udq` convert with truncation packed single-precision floating-point values to packed unsigned doubleword integer values
`vcvttps2uqq` convert with truncation packed single precision floating-point values to packed unsigned quadword integer values
`vcvttsd2si` convert with truncation scalar double-precision floating-point value to signed integer
`vcvttsd2usi` convert with truncation scalar double-precision floating-point value to unsigned integer
`vcvttss2si` convert with truncation scalar single-precision floating-point value to integer
`vcvttss2usi` convert with truncation scalar single-precision floating-point value to unsigned integer
`vcvtudq2pd` convert packed unsigned doubleword integers to packed double-precision floating-point values
`vcvtudq2ps` convert packed unsigned doubleword integers to packed single-precision floating-point values
`vcvtuqq2pd` convert packed unsigned quadword integers to packed double-precision floating-point values
`vcvtuqq2ps` convert packed unsigned quadword integers to packed single-precision floating-point values
`vcvtusi2sd` convert unsigned integer to scalar double-precision floating-point value
`vcvtusi2ss` convert unsigned integer to scalar single-precision floating-point value
`vdbpsadbw` double block packed sum-absolute-differences (sad) on unsigned bytes
`vdivpd` divide packed double-precision floating-point values
`vdivps` divide packed single-precision floating-point values
`vdivsd` divide scalar double-precision floating-point value
`vdivss` divide scalar single-precision floating-point values
`vdppd` dot product of packed double precision floating-point values
`vdpps` dot product of packed single precision floating-point values
`verr` verify a segment for reading
`verw` verify a segment for writing
`vexp2pd` approximation to the exponential 2^x of packed double-precision floating-point values with less than 2^-23 relative error
`vexp2ps` approximation to the exponential 2^x of packed single-precision floating-point values with less than 2^-23 relative error
`vexpandpd` load sparse packed double-precision floating-point values from dense memory
`vexpandps` load sparse packed single-precision floating-point values from dense memory
`vextractf128` extra ct packed floating-point values
`vextractf32x4` extra ct packed floating-point values
`vextractf32x8` extra ct packed floating-point values
`vextractf64x2` extra ct packed floating-point values
`vextractf64x4` extra ct packed floating-point values
`vextracti128` extract packed integer values
`vextracti32x4` extract packed integer values
`vextracti32x8` extract packed integer values
`vextracti64x2` extract packed integer values
`vextracti64x4` extract packed integer values
`vextractps` extract packed floating-point values
`vfixupimmpd` fix up special packed float64 values
`vfixupimmps` fix up special packed float32 values
`vfixupimmsd` fix up special scalar float64 value
`vfixupimmss` fix up special scalar float32 value
`vfmadd132pd` fused multiply-add of packed double-precision floating-point values
`vfmadd132ps` fused multiply-add of packed single-precision floating-point values
`vfmadd132sd` fused multiply-add of scalar double-precision floating-point values
`vfmadd132ss` fused multiply-add of scalar single-precision floating-point values
`vfmadd213pd` fused multiply-add of packed double-precision floating-point values
`vfmadd213ps` fused multiply-add of packed single-precision floating-point values
`vfmadd213sd` fused multiply-add of scalar double-precision floating-point values
`vfmadd213ss` fused multiply-add of scalar single-precision floating-point values
`vfmadd231pd` fused multiply-add of packed double-precision floating-point values
`vfmadd231ps` fused multiply-add of packed single-precision floating-point values
`vfmadd231sd` fused multiply-add of scalar double-precision floating-point values
`vfmadd231ss` fused multiply-add of scalar single-precision floating-point values
`vfmaddsub132pd` fused multiply-alternating add/subtract of packed double-precision floating-point values
`vfmaddsub132ps` fused multiply-alternating add/subtract of packed single-precision floating-point values
`vfmaddsub213pd` fused multiply-alternating add/subtract of packed double-precision floating-point values
`vfmaddsub213ps` fused multiply-alternating add/subtract of packed single-precision floating-point values
`vfmaddsub231pd` fused multiply-alternating add/subtract of packed double-precision floating-point values
`vfmaddsub231ps` fused multiply-alternating add/subtract of packed single-precision floating-point values
`vfmsub132pd` fused multiply-subtract of packed double-precision floating-point values
`vfmsub132ps` fused multiply-subtract of packed single-precision floating-point values
`vfmsub132sd` fused multiply-subtract of scalar double-precision floating-point values
`vfmsub132ss` fused multiply-subtract of scalar single-precision floating-point values
`vfmsub213pd` fused multiply-subtract of packed double-precision floating-point values
`vfmsub213ps` fused multiply-subtract of packed single-precision floating-point values
`vfmsub213sd` fused multiply-subtract of scalar double-precision floating-point values
`vfmsub213ss` fused multiply-subtract of scalar single-precision floating-point values
`vfmsub231pd` fused multiply-subtract of packed double-precision floating-point values
`vfmsub231ps` fused multiply-subtract of packed single-precision floating-point values
`vfmsub231sd` fused multiply-subtract of scalar double-precision floating-point values
`vfmsub231ss` fused multiply-subtract of scalar single-precision floating-point values
`vfmsubadd132pd` fused multiply-alternating subtract/add of packed double-precision floating-point values
`vfmsubadd132ps` fused multiply-alternating subtract/add of packed single-precision floating-point values
`vfmsubadd213pd` fused multiply-alternating subtract/add of packed double-precision floating-point values
`vfmsubadd213ps` fused multiply-alternating subtract/add of packed single-precision floating-point values
`vfmsubadd231pd` fused multiply-alternating subtract/add of packed double-precision floating-point values
`vfmsubadd231ps` fused multiply-alternating subtract/add of packed single-precision floating-point values
`vfnmadd132pd` fused negative multiply-add of packed double-precision floating-point values
`vfnmadd132ps` fused negative multiply-add of packed single-precision floating-point values
`vfnmadd132sd` fused negative multiply-add of scalar double-precision floating-point values
`vfnmadd132ss` fused negative multiply-add of scalar single-precision floating-point values
`vfnmadd213pd` fused negative multiply-add of packed double-precision floating-point values
`vfnmadd213ps` fused negative multiply-add of packed single-precision floating-point values
`vfnmadd213sd` fused negative multiply-add of scalar double-precision floating-point values
`vfnmadd213ss` fused negative multiply-add of scalar single-precision floating-point values
`vfnmadd231pd` fused negative multiply-add of packed double-precision floating-point values
`vfnmadd231ps` fused negative multiply-add of packed single-precision floating-point values
`vfnmadd231sd` fused negative multiply-add of scalar double-precision floating-point values
`vfnmadd231ss` fused negative multiply-add of scalar single-precision floating-point values
`vfnmsub132pd` fused negative multiply-subtract of packed double-precision floating-point values
`vfnmsub132ps` fused negative multiply-subtract of packed single-precision floating-point values
`vfnmsub132sd` fused negative multiply-subtract of scalar double-precision floating-point values
`vfnmsub132ss` fused negative multiply-subtract of scalar single-precision floating-point values
`vfnmsub213pd` fused negative multiply-subtract of packed double-precision floating-point values
`vfnmsub213ps` fused negative multiply-subtract of packed single-precision floating-point values
`vfnmsub213sd` fused negative multiply-subtract of scalar double-precision floating-point values
`vfnmsub213ss` fused negative multiply-subtract of scalar single-precision floating-point values
`vfnmsub231pd` fused negative multiply-subtract of packed double-precision floating-point values
`vfnmsub231ps` fused negative multiply-subtract of packed single-precision floating-point values
`vfnmsub231sd` fused negative multiply-subtract of scalar double-precision floating-point values
`vfnmsub231ss` fused negative multiply-subtract of scalar single-precision floating-point values
`vfpclasspd` tests types of a packed float64 values
`vfpclassps` tests types of a packed float32 values
`vfpclasssd` tests types of a scalar float64 values
`vfpclassss` tests types of a scalar float32 values
`vgatherdpd` gather packed single, packed double with signed dword
`vgatherdps` gather packed sp fp values using signed dword/qword indices
`vgatherpf0dpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint
`vgatherpf0dps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint
`vgatherpf0qpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint
`vgatherpf0qps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint
`vgatherpf1dpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint
`vgatherpf1dps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint
`vgatherpf1qpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint
`vgatherpf1qps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint
`vgatherqpd` gather packed single, packed double with signed qword indices
`vgatherqps` gather packed single, packed double with signed qword indices
`vgetexppd` convert exponents of packed dp fp values to dp fp values
`vgetexpps` convert exponents of packed sp fp values to sp fp values
`vgetexpsd` convert exponents of scalar dp fp values to dp fp value
`vgetexpss` convert exponents of scalar sp fp values to sp fp value
`vgetmantpd` extract float64 vector of normalized mantissas from float64 vector
`vgetmantps` extract float32 vector of normalized mantissas from float32 vector
`vgetmantsd` extract float64 of normalized mantissas from float64 scalar
`vgetmantss` extract float32 vector of normalized mantissa from float32 vector
`vhaddpd` packed double-fp horizontal add
`vhaddps` packed single-fp horizontal add
`vhsubpd` packed double-fp horizontal subtract
`vhsubps` packed single-fp horizontal subtract
`vinsertf128` insert packed floating-point values
`vinsertf32x4` insert packed floating-point values
`vinsertf32x8` insert packed floating-point values
`vinsertf64x2` insert packed floating-point values
`vinsertf64x4` insert packed floating-point values
`vinserti128` insert packed integer values
`vinserti32x4` insert packed integer values
`vinserti32x8` insert packed integer values
`vinserti64x2` insert packed integer values
`vinserti64x4` insert packed integer values
`vinsertps` insert scalar single-precision floating-point value
`vlddqu` load unaligned integer 128 bits
`vldmxcsr` load mxcsr register
`vmaskmovdqu` store selected bytes of double quadword
`vmaskmovpd` conditional simd packed loads and stores
`vmaskmovps` conditional simd packed loads and stores
`vmaxpd` maximum of packed double-precision floating-point values
`vmaxps` maximum of packed single-precision floating-point values
`vmaxsd` return maximum scalar double-precision floating-point value
`vmaxss` return maximum scalar single-precision floating-point value
`vminpd` minimum of packed double-precision floating-point values
`vminps` minimum of packed single-precision floating-point values
`vminsd` return minimum scalar double-precision floating-point value
`vminss` return minimum scalar single-precision floating-point value
`vmovapd` move aligned packed double-precision floating-point values
`vmovaps` move aligned packed single-precision floating-point values
`vmovd` move doubleword/move quadword
`vmovddup` replicate double fp values
`vmovdqa` move aligned packed integer values
`vmovdqa32` move aligned packed integer values
`vmovdqa64` move aligned packed integer values
`vmovdqu` move unaligned packed integer values
`vmovdqu16` move unaligned packed integer values
`vmovdqu32` move unaligned packed integer values
`vmovdqu64` move unaligned packed integer values
`vmovdqu8` move unaligned packed integer values
`vmovhlps` move packed single-precision floating-point values high to low
`vmovhpd` move high packed double-precision floating-point value
`vmovhps` move high packed single-precision floating-point values
`vmovlhps` move packed single-precision floating-point values low to high
`vmovlpd` move low packed double-precision floating-point value
`vmovlps` move low packed single-precision floating-point values
`vmovmskpd` extract packed double-precision floating-point sign mask
`vmovmskps` extract packed single-precision floating-point sign mask
`vmovntdq` store packed integers using non-temporal hint
`vmovntdqa` load double quadword non-temporal aligned hint
`vmovntpd` store packed double-precision floating-point values using non-temporal hint
`vmovntps` store packed single-precision floating-point values using non-temporal hint
`vmovq` move quadword
`vmovsd` move or merge scalar double-precision floating-point value
`vmovshdup` replicate single fp values
`vmovsldup` replicate single fp values
`vmovss` move or merge scalar single-precision floating-point value
`vmovupd` move unaligned packed double-precision floating-point values
`vmovups` move unaligned packed single-precision floating-point values
`vmpsadbw` compute multiple packed sums of absolute difference
`vmulpd` multiply packed double-precision floating-point values
`vmulps` multiply packed single-precision floating-point values
`vmulsd` multiply scalar double-precision floating-point value
`vmulss` multiply scalar single-precision floating-point values
`vorpd` bitwise logical or of packed double precision floating-point values
`vorps` bitwise logical or of packed single precision floating-point values
`vpabsb` packed absolute value
`vpabsd` packed absolute value
`vpabsq` packed absolute value
`vpabsw` packed absolute value
`vpackssdw` pack with signed saturation
`vpacksswb` pack with signed saturation
`vpackusdw` pack with unsigned saturation
`vpackuswb` pack with unsigned saturation
`vpaddb` add packed integers
`vpaddd` add packed integers
`vpaddq` add packed integers
`vpaddsb` add packed signed integers with signed saturation
`vpaddsw` add packed signed integers with signed saturation
`vpaddusb` add packed unsigned integers with unsigned saturation
`vpaddusw` add packed unsigned integers with unsigned saturation
`vpaddw` add packed integers
`vpalignr` packed align right
`vpand` logical and
`vpandd` logical and
`vpandn` logical and not
`vpandnd` logical and not
`vpandnq` logical and not
`vpandq` logical and
`vpavgb` average packed integers
`vpavgw` average packed integers
`vpblendd` blend packed dwords
`vpblendmb` blend byte/word vectors using an opmask control
`vpblendmd` blend int32/int64 vectors using an opmask control
`vpblendmq` blend int32/int64 vectors using an opmask control
`vpblendmw` blend byte/word vectors using an opmask control
`vpblendvb` variable blend packed bytes
`vpblendw` blend packed words
`vpbroadcastb` load with broadcast integer data from general purpose register
`vpbroadcastd` load with broadcast integer data from general purpose register
`vpbroadcastmb2q` broadcast mask to vector register
`vpbroadcastmw2d` broadcast mask to vector register
`vpbroadcastq` load with broadcast integer data from general purpose register
`vpbroadcastw` load with broadcast integer data from general purpose register
`vpclmulqdq` pclmulqdq - carry-less multiplication quadword
`vpcmpb` compare packed byte values into mask
`vpcmpd` compare packed integer values into mask
`vpcmpeqb` compare packed data for equal
`vpcmpeqd` compare packed data for equal
`vpcmpeqq` compare packed qword data for equal
`vpcmpeqw` compare packed data for equal
`vpcmpestri` packed compare explicit length strings, return index
`vpcmpestrm` packed compare explicit length strings, return mask
`vpcmpgtb` compare packed signed integers for greater than
`vpcmpgtd` compare packed signed integers for greater than
`vpcmpgtq` compare packed data for greater than
`vpcmpgtw` compare packed signed integers for greater than
`vpcmpistri` packed compare implicit length strings, return index
`vpcmpistrm` packed compare implicit length strings, return mask
`vpcmpq` compare packed integer values into mask
`vpcmpub` compare packed byte values into mask
`vpcmpud` compare packed integer values into mask
`vpcmpuq` compare packed integer values into mask
`vpcmpuw` compare packed word values into mask
`vpcmpw` compare packed word values into mask
`vpcompressd` store sparse packed doubleword integer values into dense memory/register
`vpcompressq` store sparse packed quadword integer values into dense memory/register
`vpconflictd` detect conflicts within a vector of packed dword/qword values into dense memory/ register
`vpconflictq` detect conflicts within a vector of packed dword/qword values into dense memory/ register
`vperm2f128` permute floating-point values
`vperm2i128` permute integer values
`vpermd` permute packed doublewords/words elements
`vpermi2d` full permute from two tables overwriting the index
`vpermi2pd` full permute from two tables overwriting the index
`vpermi2ps` full permute from two tables overwriting the index
`vpermi2q` full permute from two tables overwriting the index
`vpermi2w` full permute from two tables overwriting the index
`vpermilpd` permute in-lane of pairs of double-precision floating-point values
`vpermilps` permute in-lane of quadruples of single-precision floating-point values
`vpermpd` permute double-precision floating-point elements
`vpermps` permute single-precision floating-point elements
`vpermq` qwords element permutation
`vpermw` permute packed doublewords/words elements
`vpexpandd` load sparse packed doubleword integer values from dense memory / register
`vpexpandq` load sparse packed quadword integer values from dense memory / register
`vpextrb` extract byte/dword/qword
`vpextrd` extract byte/dword/qword
`vpextrq` extract byte/dword/qword
`vpextrw` extract word
`vpgatherdd` gather packed dword values using signed dword/qword indices
`vpgatherdq` gather packed qword values using signed dword/qword indices
`vpgatherqd` gather packed dword, packed qword with signed qword indices
`vpgatherqq` gather packed dword, packed qword with signed qword indices
`vphaddd` packed horizontal add
`vphaddsw` packed horizontal add and saturate
`vphaddw` packed horizontal add
`vphminposuw` packed horizontal word minimum
`vphsubd` packed horizontal subtract
`vphsubsw` packed horizontal subtract and saturate
`vphsubw` packed horizontal subtract
`vpinsrb` insert byte/dword/qword
`vpinsrd` insert byte/dword/qword
`vpinsrq` insert byte/dword/qword
`vpinsrw` insert word
`vplzcntd` count the number of leading zero bits for packed dword, packed qword values
`vplzcntq` count the number of leading zero bits for packed dword, packed qword values
`vpmaddubsw` multiply and add packed signed and unsigned bytes
`vpmaddwd` multiply and add packed integers
`vpmaskmovd` conditional simd integer packed loads and stores
`vpmaskmovq` conditional simd integer packed loads and stores
`vpmaxsb` maximum of packed signed integers
`vpmaxsd` maximum of packed signed integers
`vpmaxsq` maximum of packed signed integers
`vpmaxsw` maximum of packed signed integers
`vpmaxub` maximum of packed unsigned integers
`vpmaxud` maximum of packed unsigned integers
`vpmaxuq` maximum of packed unsigned integers
`vpmaxuw` maximum of packed unsigned integers
`vpminsb` minimum of packed signed integers
`vpminsd` minimum of packed signed integers
`vpminsq` minimum of packed signed integers
`vpminsw` minimum of packed signed integers
`vpminub` minimum of packed unsigned integers
`vpminud` minimum of packed unsigned integers
`vpminuq` minimum of packed unsigned integers
`vpminuw` minimum of packed unsigned integers
`vpmovb2m` convert a vector register to a mask
`vpmovd2m` convert a vector register to a mask
`vpmovdb` down convert dword to byte
`vpmovdw` down convert dword to word
`vpmovm2b` convert a mask register to a vector register
`vpmovm2d` convert a mask register to a vector register
`vpmovm2q` convert a mask register to a vector register
`vpmovm2w` convert a mask register to a vector register
`vpmovmskb` move byte mask
`vpmovq2m` convert a vector register to a mask
`vpmovqb` down convert qword to byte
`vpmovqd` down convert qword to dword
`vpmovqw` down convert qword to word
`vpmovsdb` down convert dword to byte
`vpmovsdw` down convert dword to word
`vpmovsqb` down convert qword to byte
`vpmovsqd` down convert qword to dword
`vpmovsqw` down convert qword to word
`vpmovswb` down convert word to byte
`vpmovsxbd` packed move with sign extend
`vpmovsxbq` packed move with sign extend
`vpmovsxbw` packed move with sign extend
`vpmovsxdq` packed move with sign extend
`vpmovsxwd` packed move with sign extend
`vpmovsxwq` packed move with sign extend
`vpmovusdb` down convert dword to byte
`vpmovusdw` down convert dword to word
`vpmovusqb` down convert qword to byte
`vpmovusqd` down convert qword to dword
`vpmovusqw` down convert qword to word
`vpmovuswb` down convert word to byte
`vpmovw2m` convert a vector register to a mask
`vpmovwb` down convert word to byte
`vpmovzxbd` packed move with zero extend
`vpmovzxbq` packed move with zero extend
`vpmovzxbw` packed move with zero extend
`vpmovzxdq` packed move with zero extend
`vpmovzxwd` packed move with zero extend
`vpmovzxwq` packed move with zero extend
`vpmuldq` multiply packed doubleword integers
`vpmulhrsw` packed multiply high with round and scale
`vpmulhuw` multiply packed unsigned integers and store high result
`vpmulhw` multiply packed signed integers and store high result
`vpmulld` multiply packed integers and store low result
`vpmullq` multiply packed integers and store low result
`vpmullw` multiply packed signed integers and store low result
`vpmuludq` multiply packed unsigned doubleword integers
`vpor` bitwise logical or
`vpord` bitwise logical or
`vporq` bitwise logical or
`vprold` bit rotate left
`vprolq` bit rotate left
`vprolvd` bit rotate left
`vprolvq` bit rotate left
`vprord` bit rotate right
`vprorq` bit rotate right
`vprorvd` bit rotate right
`vprorvq` bit rotate right
`vpsadbw` compute sum of absolute differences
`vpscatterdd` scatter packed dword, packed qword with signed dword, signed qword indices
`vpscatterdq` scatter packed dword, packed qword with signed dword, signed qword indices
`vpscatterqd` scatter packed dword, packed qword with signed dword, signed qword indices
`vpscatterqq` scatter packed dword, packed qword with signed dword, signed qword indices
`vpshufb` packed shuffle bytes
`vpshufd` shuffle packed doublewords
`vpshufhw` shuffle packed high words
`vpshuflw` shuffle packed low words
`vpsignb` packed sign
`vpsignd` packed sign
`vpsignw` packed sign
`vpslld` shift packed data left logical
`vpslldq` shift double quadword left logical
`vpsllq` shift packed data left logical
`vpsllvd` variable bit shift left logical
`vpsllvq` variable bit shift left logical
`vpsllvw` variable bit shift left logical
`vpsllw` shift packed data left logical
`vpsrad` shift packed data right arithmetic
`vpsraq` shift packed data right arithmetic
`vpsravd` variable bit shift right arithmetic
`vpsravq` variable bit shift right arithmetic
`vpsravw` variable bit shift right arithmetic
`vpsraw` shift packed data right arithmetic
`vpsrld` shift packed data right logical
`vpsrldq` shift double quadword right logical
`vpsrlq` shift packed data right logical
`vpsrlvd` variable bit shift right logical
`vpsrlvq` variable bit shift right logical
`vpsrlvw` variable bit shift right logical
`vpsrlw` shift packed data right logical
`vpsubb` subtract packed integers
`vpsubd` subtract packed integers
`vpsubq` subtract packed quadword integers
`vpsubsb` subtract packed signed integers with signed saturation
`vpsubsw` subtract packed signed integers with signed saturation
`vpsubusb` subtract packed unsigned integers with unsigned saturation
`vpsubusw` subtract packed unsigned integers with unsigned saturation
`vpsubw` subtract packed integers
`vpternlogd` bitwise ternary logic
`vpternlogq` bitwise ternary logic
`vptest` ptest- logical compare
`vptestmb` logical and and set mask
`vptestmd` logical and and set mask
`vptestmq` logical and and set mask
`vptestmw` logical and and set mask
`vptestnmb` logical nand and set
`vptestnmd` logical nand and set
`vptestnmq` logical nand and set
`vptestnmw` logical nand and set
`vpunpckhbw` unpack high data
`vpunpckhdq` unpack high data
`vpunpckhqdq` unpack high data
`vpunpckhwd` unpack high data
`vpunpcklbw` unpack low data
`vpunpckldq` unpack low data
`vpunpcklqdq` unpack low data
`vpunpcklwd` unpack low data
`vpxor` logical exclusive or
`vpxord` logical exclusive or
`vpxorq` logical exclusive or
`vrangepd` range restriction calculation for packed pairs of float64 values
`vrangeps` range restriction calculation for packed pairs of float32 values
`vrangesd` range restriction calculation from a pair of scalar float64 values
`vrangess` range restriction calculation from a pair of scalar float32 values
`vrcp14pd` compute approximate reciprocals of packed float64 values
`vrcp14ps` compute approximate reciprocals of packed float32 values
`vrcp14sd` compute approximate reciprocal of scalar float64 value
`vrcp14ss` compute approximate reciprocal of scalar float32 value
`vrcp28pd` approximation to the reciprocal of packed double-precision floating-point values with less than 2^-28 relative error
`vrcp28ps` approximation to the reciprocal of packed single-precision floating-point values with less than 2^-28 relative error
`vrcp28sd` approximation to the reciprocal of scalar double-precision floating-point value with less than 2^-28 relative error
`vrcp28ss` approximation to the reciprocal of scalar single-precision floating-point value with less than 2^-28 relative error
`vrcpps` compute reciprocals of packed single-precision floating-point values
`vrcpss` compute reciprocal of scalar single-precision floating-point values
`vreducepd` perform reduction transformation on packed float64 values
`vreduceps` perform reduction transformation on packed float32 values
`vreducesd` perform a reduction transformation on a scalar float64 value
`vreducess` perform a reduction transformation on a scalar float32 value
`vrndscalepd` round packed float64 values to include a given number of fraction bits
`vrndscaleps` round packed float32 values to include a given number of fraction bits
`vrndscalesd` round scalar float64 value to include a given number of fraction bits
`vrndscaless` round scalar float32 value to include a given number of fraction bits
`vroundpd` round packed double precision floating-point values
`vroundps` round packed single precision floating-point values
`vroundsd` round scalar double precision floating-point values
`vroundss` round scalar single precision floating-point values
`vrsqrt14pd` compute approximate reciprocals of square roots of packed float64 values
`vrsqrt14ps` compute approximate reciprocals of square roots of packed float32 values
`vrsqrt14sd` compute approximate reciprocal of square root of scalar float64 value
`vrsqrt14ss` compute approximate reciprocal of square root of scalar float32 value
`vrsqrt28pd` approximation to the reciprocal square root of packed double-precision floating-point values with less than 2^-28 relative error
`vrsqrt28ps` approximation to the reciprocal square root of packed single-precision floating-point values with less than 2^-28 relative error
`vrsqrt28sd` approximation to the reciprocal square root of scalar double-precision floating-point value with less than 2^-28 relative error
`vrsqrt28ss` approximation to the reciprocal square root of scalar single-precision floating-point value with less than 2^-28 relative error
`vrsqrtps` compute reciprocals of square roots of packed single-precision floating-point values
`vrsqrtss` compute reciprocal of square root of scalar single-precision floating-point value
`vscalefpd` scale packed float64 values with float64 values
`vscalefps` scale packed float32 values with float32 values
`vscalefsd` scale scalar float64 values with float64 values
`vscalefss` scale scalar float32 value with float32 value
`vscatterdpd` scatter packed single, packed double with signed dword and qword indices
`vscatterdps` scatter packed single, packed double with signed dword and qword indices
`vscatterpf0dpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint with intent to write
`vscatterpf0dps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint with intent to write
`vscatterpf0qpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint with intent to write
`vscatterpf0qps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t0 hint with intent to write
`vscatterpf1dpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint with intent to write
`vscatterpf1dps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint with intent to write
`vscatterpf1qpd` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint with intent to write
`vscatterpf1qps` sparse prefetch packed sp/dp data values with signed dword, signed qword indices using t1 hint with intent to write
`vscatterqpd` scatter packed single, packed double with signed dword and qword indices
`vscatterqps` scatter packed single, packed double with signed dword and qword indices
`vshuff32x4` shuffle packed values at 128-bit granularity
`vshuff64x2` shuffle packed values at 128-bit granularity
`vshufi32x4` shuffle packed values at 128-bit granularity
`vshufi64x2` shuffle packed values at 128-bit granularity
`vshufpd` packed interleave shuffle of pairs of double-precision floating-point values
`vshufps` packed interleave shuffle of quadruplets of single-precision floating-point values
`vsqrtpd` square root of double-precision floating-point values
`vsqrtps` square root of single-precision floating-point values
`vsqrtsd` compute square root of scalar double-precision floating-point value
`vsqrtss` compute square root of scalar single-precision value
`vstmxcsr` store mxcsr register state
`vsubpd` subtract packed double-precision floating-point values
`vsubps` subtract packed single-precision floating-point values
`vsubsd` subtract scalar double-precision floating-point value
`vsubss` subtract scalar single-precision floating-point value
`vtestpd` packed bit test
`vtestps` packed bit test
`vucomisd` unordered compare scalar double-precision floating-point values and set eflags
`vucomiss` unordered compare scalar single-precision floating-point values and set eflags
`vunpckhpd` unpack and interleave high packed double-precision floating-point values
`vunpckhps` unpack and interleave high packed single-precision floating-point values
`vunpcklpd` unpack and interleave low packed double-precision floating-point values
`vunpcklps` unpack and interleave low packed single-precision floating-point values
`vxorpd` bitwise logical xor of packed double precision floating-point values
`vxorps` bitwise logical xor of packed single precision floating-point values
`vzeroall` zero all ymm registers
`vzeroupper` zero upper bits of ymm registers
`wait` stop process execution until TEST pin activated
`wbinvd` write back and invalidate cache
`wrfsbase` write fs/gs segment base
`wrgsbase` write fs/gs segment base
`wrmsr` write to model specific register
`wrpkru` write data to user page key register
`xabort` transactional abort
`xacquire` hardware lock elision prefix hints
`xadd` exchange and add
`xbegin` transactional begin
`xchg` exchange register/memory with register
`xend` transactional end
`xgetbv` get value of extended control register
`xlat` table look-up translation
`xlatb` table look-up translation
`xor` logical exclusive or
`xorpd` bitwise logical xor for double-fp values
`xorps` bitwise logical xor for single-fp values
`xrelease` hardware lock elision prefix hints
`xrstor` restore processor extended states
`xrstors` restore processor extended states supervisor
`xsave` save processor extended states
`xsavec` save processor extended states with compaction
`xsaveopt` save processor extended states optimized
`xsaves` save processor extended states supervisor
`xsetbv` set extended control register
`xtest` test if in transactional execution
`callf` call procedure
`cmovnbe` conditional move - not below nor equal/above (cf=0 and zf=0)
`cmovnc` conditional move - not carry/above or equal/not below (cf=0)
`cmovne` conditional move - not equal/not zero (zf=0)
`cmovng` conditional move - not greater/less or equal (zf=1 or sf!=of)
`cmovnge` conditional move - not greater nor equal/less (sf!=of)
`cmovnl` conditional move - not less/greater or equal (sf=of)
`cmovnle` conditional move - not less nor equal/greater (zf=0 and sf=of)
`cmovno` conditional move - not overflow (of=0)
`cmovnp` conditional move - not parity/parity odd (pf=0)
`cmovns` conditional move - not sign (sf=0)
`cmovnz` conditional move - not zero/not equal (zf=0)
`cmovo` conditional move - overflow (of=1)
`cmovp` conditional move - parity/parity even (pf=1)
`cmovpe` conditional move - parity even/parity (pf=1)
`cmovpo` conditional move - parity odd/not parity (pf=0)
`cmovs` conditional move - sign (sf=1)
`cmovz` conditional move - zero/equal (zf=1)
`cs` cs segment override prefix
`ds` ds segment override prefix
`es` es segment override prefix
`fcmovnu` fp conditional move - not unordered (pf=0)
`fdisi` disable npx (numeric coprocessor extension) interrupt
`feni` enable npx (numeric coprocessor extension) interrupt
`ffreep` free floating-point register and pop (undocumented)
`fndisi` disable npx (numeric coprocessor extension) interrupts (8087 only, otherwise, FNOP)
`fneni` enable npx (numeric coprocessor extension) interrupts (8087 only, otherwise, FNOP)
`fnsetpm` set protected mode (8087 only, otherwise FNOP)
`fsetpm` set protected mode
`fs` fs segment override prefix
`fstpnce` store floating point value and pop (undocumented)
`getsec` getsec leaf functions
`gs` gs segment override prefix
`hint_nop` hintable nop
`icebp` Single byte single-step exception / Invoke ICE
`int1` call to interrupt procedure
`int3` int 3, software breakpoint
`invept` invalidate translations derived from ept
`invvpid` invalidate translations based on vpid
`iretq` interrupt return (64 bit)
`jmpe` jump to ia-64 instruction set
`jmpf` jump
`loadalld` loads All Registers from memory address es:edi
`loadall` load all of the cpu registers
`movabs` absolute data moves
`popal` pop all general-purpose registers
`pushal` push all general-purpose registers
`pushfq` push rflags register onto the stack
`repe` repeat string
`repne` repeat string operation prefix
`repnz` repeat string operation prefix
`rep` repeats next instruction ECX times
`repz` repeat string operation prefix
`retf` return from procedure
`retn` return from procedure
`rex` access to new 8-bit registers
`rex.b` extension of r/m field, base field, or opcode reg field
`rex.rb` rex.r and rex.b combination
`rex.r` extension of modr/m reg field
`rex.rxb` rex.r, rex.x and rex.b combination
`rex.rx` rex.r and rex.x combination
`rex.w` 64 bit operand size
`rex.wb` rex.w and rex.b combination
`rex.wrb` rex.w, rex.r and rex.b combination
`rex.wr` rex.w and rex.r combination
`rex.wrxb` rex.w, rex.r, rex.x and rex.b combination
`rex.wrx` rex.w, rex.r and rex.x combination
`rex.wxb` rex.w, rex.x and rex.b combination
`rex.wx` rex.w and rex.x combination
`rex.xb` rex.x and rex.b combination
`rex.x` extension of sib index field
`rtdsc` read time-stamp counter into edx:eax
`salc` set al if carry
`scasq` cmp rax, ES:[rdi+=8]
`setnle` set byte on condition - not less nor equal/greater (zf=0 and sf=of)
`ss` ss segment override prefix
`ud1` undefined instruction
`vmcall` call to vm monitor
`vmclear` clear virtual-machine control structure
`vmlaunch` launch virtual machine
`vmptrld` load pointer to virtual-machine control structure
`vmptrst` store pointer to virtual-machine control structure
`vmread` read field from virtual-machine control structure
`vmresume` resume virtual machine
`vmwrite` write field to virtual-machine control structure
`vmxoff` leave vmx operation
`vmxon` enter vmx operation




<p hidden>aaa aad aam aas adc adcx add addpd addps addsd addss addsubpd addsubps adox aesdec aesdeclast aesenc aesenclast aesimc aeskeygenassist and andn andnpd andnps andpd andps arpl bextr blendpd blendps blendvpd blendvps blsi blsmsk blsr bndcl bndcn bndcu bndldx bndmk bndmov bndstx bound bsf bsr bswap bt btc btr bts bzhi call cbw cdq cdqe clac clc cld clflush clflushopt cli clts cmc cmova cmovae cmovb cmovbe cmovc cmove cmovg cmovge cmovl cmovle cmovna cmovnae cmovnb cmp cmppd cmpps cmps cmpsb cmpsd cmpsq cmpss cmpsw cmpxchg cmpxchg16b cmpxchg8b comisd comiss cpuid cqo crc32 cvtdq2pd cvtdq2ps cvtpd2dq cvtpd2pi cvtpd2ps cvtpi2pd cvtpi2ps cvtps2dq cvtps2pd cvtps2pi cvtsd2si cvtsd2ss cvtsi2sd cvtsi2ss cvtss2sd cvtss2si cvttpd2dq cvttpd2pi cvttps2dq cvttps2pi cvttsd2si cvttss2si cwd cwde daa das dec div divpd divps divsd divss dppd dpps emms enter extractps f2xm1 fabs fadd faddp fbld fbstp fchs fclex fcmovb fcmovbe fcmove fcmovnb fcmovnbe fcmovne fcmovu fcom fcomi fcomip fcomp fcompp fcos fdecstp fdiv fdivp fdivr fdivrp ffree fiadd ficom ficomp fidiv fidivr fild fimul fincstp finit fist fistp fisttp fisub fisubr fld fld1 fldcw fldenv fldl2e fldl2t fldlg2 fldln2 fldpi fldz fmul fmulp fnclex fninit fnop fnsave fnstcw fnstenv fnstsw fpatan fprem fprem1 fptan frndint frstor fsave fscale fsin fsincos fsqrt fst fstcw fstenv fstp fstsw fsub fsubp fsubr fsubrp ftst fucom fucomi fucomip fucomp fucompp fwait fxam fxch fxrstor fxsave fxtract fyl2x fyl2xp1 haddpd haddps hlt hsubpd hsubps idiv imul in inc ins insb insd insertps insw int int into invd invlpg invpcid iret iretd ja jae jb jbe jc jcxz je jecxz jg jge jl jle jmp jna jnae jnb jnbe jnc jne jng jnge jnl jnle jno jnp jns jnz jo jp jpe jpo jrcxz js jz kaddb kaddd kaddq kaddw kandb kandd kandnb kandnd kandnq kandnw kandq kandw kmovb kmovd kmovq kmovw knotb knotd knotq knotw korb kord korq kortestb kortestd kortestq kortestw korw kshiftlb kshiftld kshiftlq kshiftlw kshiftrb kshiftrd kshiftrq kshiftrw ktestb ktestd ktestq ktestw kunpckbw kunpckdq kunpckwd kxnorb kxnord kxnorq kxnorw kxorb kxord kxorq kxorw lahf lar lddqu ldmxcsr lds lea leave les lfence lfs lgdt lgs lidt lldt lmsw lock lods lodsb lodsd lodsq lodsw loop loope loopne loopnz loopz lsl lss ltr lzcnt maskmovdqu maskmovq maxpd maxps maxsd maxss mfence minpd minps minsd minss monitor mov movapd movaps movbe movd movddup movdq2q movdqa movdqu movhlps movhpd movhps movlhps movlpd movlps movmskpd movmskps movntdq movntdqa movnti movntpd movntps movntq movq movq2dq movs movsb movsd movshdup movsldup movsq movss movsw movsx movsxd movupd movups movzx mpsadbw mul mulpd mulps mulsd mulss mulx mwait neg nop not or orpd orps out outs outsb outsd outsw pabsb pabsd pabsq pabsw packssdw packsswb packusdw packuswb paddb paddd paddq paddsb paddsw paddusb paddusw paddw palignr pand pandn pause pavgb pavgw pblendvb pblendw pclmulqdq pcmpeqb pcmpeqd pcmpeqq pcmpeqw pcmpestri pcmpestrm pcmpgtb pcmpgtd pcmpgtq pcmpgtw pcmpistri pcmpistrm pdep pext pextrb pextrd pextrq pextrw phaddd phaddsw phaddw phminposuw phsubd phsubsw phsubw pinsrb pinsrd pinsrq pinsrw pmaddubsw pmaddwd pmaxsb pmaxsd pmaxsq pmaxsw pmaxub pmaxud pmaxuq pmaxuw pminsb pminsd pminsq pminsw pminub pminud pminuq pminuw pmovmskb pmovsxbd pmovsxbq pmovsxbw pmovsxdq pmovsxwd pmovsxwq pmovzxbd pmovzxbq pmovzxbw pmovzxdq pmovzxwd pmovzxwq pmuldq pmulhrsw pmulhuw pmulhw pmulld pmullq pmullw pmuludq pop popa popad popcnt popf popfd popfq por prefetchnta prefetcht0 prefetcht1 prefetcht2 prefetchw prefetchwt1 prold prolq prolvd prolvq prord prorq prorvd prorvq psadbw pshufb pshufd pshufhw pshuflw pshufw psignb psignd psignw pslld pslldq psllq psllw psrad psraq psraw psrld psrldq psrlq psrlw psubb psubd psubq psubsb psubsw psubusb psubusw psubw ptest ptwrite punpckhbw punpckhdq punpckhqdq punpckhwd punpcklbw punpckldq punpcklqdq punpcklwd push pusha pushad pushf pushfd pxor rcl rcpps rcpss rcr rdfsbase rdgsbase rdmsr rdpid rdpkru rdpmc rdrand rdseed rdtsc rdtscp rep rep rep rep rep repe repe repne repne ret rol ror rorx roundpd roundps roundsd roundss rsm rsqrtps rsqrtss sahf sal sar sarx sbb scas scasb scasd scasw seta setae setb setbe setc sete setg setge setl setle setna setnae setnb setnbe setnc setne setng setnge setnl setno setnp setns setnz seto setp setpe setpo sets setz sfence sgdt sha1msg1 sha1msg2 sha1nexte sha1rnds4 sha256msg1 sha256msg2 sha256rnds2 shl shld shlx shr shrd shrx shufpd shufps sidt sldt smsw sqrtpd sqrtps sqrtsd sqrtss stac stc std sti stmxcsr stos stosb stosd stosq stosw str sub subpd subps subsd subss swapgs syscall sysenter sysexit sysret test tzcnt ucomisd ucomiss ud2 unpckhpd unpckhps unpcklpd unpcklps vaddpd vaddps vaddsd vaddss vaddsubpd vaddsubps vaesdec vaesdeclast vaesenc vaesenclast vaesimc vaeskeygenassist valignd valignq vandnpd vandnps vandpd vandps vblendmpd vblendmps vblendpd vblendps vblendvpd vblendvps vbroadcastf128 vbroadcastf32x2 vbroadcastf32x4 vbroadcastf32x8 vbroadcastf64x2 vbroadcastf64x4 vbroadcasti32x8 vbroadcasti32x2 vbroadcasti64x4 vbroadcastsd vbroadcastss vcmppd vcmpps vcmpsd vcmpss vcomisd vcomiss vcompresspd vcompressps vcvtdq2pd vcvtdq2ps vcvtpd2dq vcvtpd2ps vcvtpd2qq vcvtpd2udq vcvtpd2uqq vcvtph2ps vcvtps2dq vcvtps2pd vcvtps2ph vcvtps2qq vcvtps2udq vcvtps2uqq vcvtqq2pd vcvtqq2ps vcvtsd2si vcvtsd2ss vcvtsd2usi vcvtsi2sd vcvtsi2ss vcvtss2sd vcvtss2si vcvtss2usi vcvttpd2dq vcvttpd2qq vcvttpd2udq vcvttpd2uqq vcvttps2dq vcvttps2qq vcvttps2udq vcvttps2uqq vcvttsd2si vcvttsd2usi vcvttss2si vcvttss2usi vcvtudq2pd vcvtudq2ps vcvtuqq2pd vcvtuqq2ps vcvtusi2sd vcvtusi2ss vdbpsadbw vdivpd vdivps vdivsd vdivss vdppd vdpps verr verw vexp2pd vexp2ps vexpandpd vexpandps vextractf128 vextractf32x4 vextractf32x8 vextractf64x2 vextractf64x4 vextracti128 vextracti32x4 vextracti32x8 vextracti64x2 vextracti64x4 vextractps vfixupimmpd vfixupimmps vfixupimmsd vfixupimmss vfmadd132pd vfmadd132ps vfmadd132sd vfmadd132ss vfmadd213pd vfmadd213ps vfmadd213sd vfmadd213ss vfmadd231pd vfmadd231ps vfmadd231sd vfmadd231ss vfmaddsub132pd vfmaddsub132ps vfmaddsub213pd vfmaddsub213ps vfmaddsub231pd vfmaddsub231ps vfmsub132pd vfmsub132ps vfmsub132sd vfmsub132ss vfmsub213pd vfmsub213ps vfmsub213sd vfmsub213ss vfmsub231pd vfmsub231ps vfmsub231sd vfmsub231ss vfmsubadd132pd vfmsubadd132ps vfmsubadd213pd vfmsubadd213ps vfmsubadd231pd vfmsubadd231ps vfnmadd132pd vfnmadd132ps vfnmadd132sd vfnmadd132ss vfnmadd213pd vfnmadd213ps vfnmadd213sd vfnmadd213ss vfnmadd231pd vfnmadd231ps vfnmadd231sd vfnmadd231ss vfnmsub132pd vfnmsub132ps vfnmsub132sd vfnmsub132ss vfnmsub213pd vfnmsub213ps vfnmsub213sd vfnmsub213ss vfnmsub231pd vfnmsub231ps vfnmsub231sd vfnmsub231ss vfpclasspd vfpclassps vfpclasssd vfpclassss vgatherdpd vgatherdps vgatherpf0dpd vgatherpf0dps vgatherpf0qpd vgatherpf0qps vgatherpf1dpd vgatherpf1dps vgatherpf1qpd vgatherpf1qps vgatherqpd vgatherqps vgetexppd vgetexpps vgetexpsd vgetexpss vgetmantpd vgetmantps vgetmantsd vgetmantss vhaddpd vhaddps vhsubpd vhsubps vinsertf128 vinsertf32x4 vinsertf32x8 vinsertf64x2 vinsertf64x4 vinserti128 vinserti32x4 vinserti32x8 vinserti64x2 vinserti64x4 vinsertps vlddqu vldmxcsr vmaskmovdqu vmaskmovpd vmaskmovps vmaxpd vmaxps vmaxsd vmaxss vminpd vminps vminsd vminss vmovapd vmovaps vmovd vmovddup vmovdqa vmovdqa32 vmovdqa64 vmovdqu vmovdqu16 vmovdqu32 vmovdqu64 vmovdqu8 vmovhlps vmovhpd vmovhps vmovlhps vmovlpd vmovlps vmovmskpd vmovmskps vmovntdq vmovntdqa vmovntpd vmovntps vmovq vmovsd vmovshdup vmovsldup vmovss vmovupd vmovups vmpsadbw vmulpd vmulps vmulsd vmulss vorpd vorps vpabsb vpabsd vpabsq vpabsw vpackssdw vpacksswb vpackusdw vpackuswb vpaddb vpaddd vpaddq vpaddsb vpaddsw vpaddusb vpaddusw vpaddw vpalignr vpand vpandd vpandn vpandnd vpandnq vpandq vpavgb vpavgw vpblendd vpblendmb vpblendmd vpblendmq vpblendmw vpblendvb vpblendw vpbroadcastb vpbroadcastd vpbroadcastmb2q vpbroadcastmw2d vpbroadcastq vpbroadcastw vpclmulqdq vpcmpb vpcmpd vpcmpeqb vpcmpeqd vpcmpeqq vpcmpeqw vpcmpestri vpcmpestrm vpcmpgtb vpcmpgtd vpcmpgtq vpcmpgtw vpcmpistri vpcmpistrm vpcmpq vpcmpub vpcmpud vpcmpuq vpcmpuw vpcmpw vpcompressd vpcompressq vpconflictd vpconflictq vperm2f128 vperm2i128 vpermd vpermi2d vpermi2pd vpermi2ps vpermi2q vpermi2w vpermilpd vpermilps vpermpd vpermps vpermq vpermw vpexpandd vpexpandq vpextrb vpextrd vpextrq vpextrw vpgatherdd vpgatherdq vpgatherqd vpgatherqq vphaddd vphaddsw vphaddw vphminposuw vphsubd vphsubsw vphsubw vpinsrb vpinsrd vpinsrq vpinsrw vplzcntd vplzcntq vpmaddubsw vpmaddwd vpmaskmovd vpmaskmovq vpmaxsb vpmaxsd vpmaxsq vpmaxsw vpmaxub vpmaxud vpmaxuq vpmaxuw vpminsb vpminsd vpminsq vpminsw vpminub vpminud vpminuq vpminuw vpmovb2m vpmovd2m vpmovdb vpmovdw vpmovm2b vpmovm2d vpmovm2q vpmovm2w vpmovmskb vpmovq2m vpmovqb vpmovqd vpmovqw vpmovsdb vpmovsdw vpmovsqb vpmovsqd vpmovsqw vpmovswb vpmovsxbd vpmovsxbq vpmovsxbw vpmovsxdq vpmovsxwd vpmovsxwq vpmovusdb vpmovusdw vpmovusqb vpmovusqd vpmovusqw vpmovuswb vpmovw2m vpmovwb vpmovzxbd vpmovzxbq vpmovzxbw vpmovzxdq vpmovzxwd vpmovzxwq vpmuldq vpmulhrsw vpmulhuw vpmulhw vpmulld vpmullq vpmullw vpmuludq vpor vpord vporq vprold vprolq vprolvd vprolvq vprord vprorq vprorvd vprorvq vpsadbw vpscatterdd vpscatterdq vpscatterqd vpscatterqq vpshufb vpshufd vpshufhw vpshuflw vpsignb vpsignd vpsignw vpslld vpslldq vpsllq vpsllvd vpsllvq vpsllvw vpsllw vpsrad vpsraq vpsravd vpsravq vpsravw vpsraw vpsrld vpsrldq vpsrlq vpsrlvd vpsrlvq vpsrlvw vpsrlw vpsubb vpsubd vpsubq vpsubsb vpsubsw vpsubusb vpsubusw vpsubw vpternlogd vpternlogq vptest vptestmb vptestmd vptestmq vptestmw vptestnmb vptestnmd vptestnmq vptestnmw vpunpckhbw vpunpckhdq vpunpckhqdq vpunpckhwd vpunpcklbw vpunpckldq vpunpcklqdq vpunpcklwd vpxor vpxord vpxorq vrangepd vrangeps vrangesd vrangess vrcp14pd vrcp14ps vrcp14sd vrcp14ss vrcp28pd vrcp28ps vrcp28sd vrcp28ss vrcpps vrcpss vreducepd vreduceps vreducesd vreducess vrndscalepd vrndscaleps vrndscalesd vrndscaless vroundpd vroundps vroundsd vroundss vrsqrt14pd vrsqrt14ps vrsqrt14sd vrsqrt14ss vrsqrt28pd vrsqrt28ps vrsqrt28sd vrsqrt28ss vrsqrtps vrsqrtss vscalefpd vscalefps vscalefsd vscalefss vscatterdpd vscatterdps vscatterpf0dpd vscatterpf0dps vscatterpf0qpd vscatterpf0qps vscatterpf1dpd vscatterpf1dps vscatterpf1qpd vscatterpf1qps vscatterqpd vscatterqps vshuff32x4 vshuff64x2 vshufi32x4 vshufi64x2 vshufpd vshufps vsqrtpd vsqrtps vsqrtsd vsqrtss vstmxcsr vsubpd vsubps vsubsd vsubss vtestpd vtestps vucomisd vucomiss vunpckhpd vunpckhps vunpcklpd vunpcklps vxorpd vxorps vzeroall vzeroupper wait wbinvd wrfsbase wrgsbase wrmsr wrpkru xabort xacquire xadd xbegin xchg xend xgetbv xlat xlatb xor xorpd xorps xrelease xrstor xrstors xsave xsavec xsaveopt xsaves xsetbv xtest callf cmovnbe cmovnc cmovne cmovng cmovnge cmovnl cmovnle cmovno cmovnp cmovns cmovnz cmovo cmovp cmovpe cmovpo cmovs cmovz cs ds es fcmovnu fdisi feni ffreep fndisi fneni fnsetpm fsetpm fs fstpnce getsec gs hint_nop icebp int1 int3 invept invvpid iretq jmpe jmpf loadalld loadall movabs popal pushal pushfq repe repne repnz rep repz retf retn rex rex.b rex.rb rex.r rex.rxb rex.rx rex.w rex.wb rex.wrb rex.wr rex.wrxb rex.wrx rex.wxb rex.wx rex.xb rex.x rtdsc salc scasq setnle ss ud1 vmcall vmclear vmlaunch vmptrld vmptrst vmread vmresume vmwrite vmxoff vmxon