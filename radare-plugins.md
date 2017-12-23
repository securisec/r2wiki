# Radare Plugins

**_This a list of plugins that I find interesting._** 

## `r2frida`

  - **Tips**
    - Trace symbols
      - Use the following syntax to trace. Example: `\dtf write iZi` (this was tested against node. Write is the symbol being hooked)

  [Frida Commands](plugins/Frida-Commands)

  [nowsecure/r2frida](https://github.com/nowsecure/r2frida)

  [r2con2017 - r2frida /by @mrmacete](https://www.youtube.com/watch?list=PLjIhlLNy_Y9Oe-nfcPEpaki0_En5dhQ5S&time_continue=15&v=URyd4bcV-Ik){.youtube}

## `r2pm` package manager

  [radare/radare2-pm](https://github.com/radare/radare2-pm/tree/master/db)

## `rarop`

  [rarop install help](./plugins/rarop-install-help)

  [jpenalbae/rarop](https://github.com/jpenalbae/rarop)

## `snowman` for r2

  [radare/radare2-extras](https://github.com/radare/radare2-extras/tree/master/r2snowman)

## `r4ge` (symbolic exectution)

  [gast04/r4ge](https://github.com/gast04/r4ge)

## `diaphora` (binary diffing)
   > _Binary diffing powered by diaphora (originally for IDA Pro)_ {.is-info}

  [radare/diaphora](https://github.com/radare/diaphora)

## `r2dec`

  [wargio/r2dec-js](https://github.com/wargio/r2dec-js)

## `ripr` for radare2

  ripr is a tool that helps you rip out functionality from binary code and use it from python. It accomplishes this by pairing the Unicorn-Engine with Binary Ninja

  - Dependencies:
    - Binary Ninja
    - To install the binary ninja api, use:

      [Install the Binary Ninja Python API](https://gist.github.com/withzombies/c9ab65b878d05fa20878d6c2bfa935d9)

    - Clone ripr from:

      [pbiernat/ripr](https://github.com/pbiernat/ripr)

  - Seek to function - `s offset/function`
  - Run `#!pipe python ./r2pipe_run.py `s``
  - Follow prompts
  - Example from original [pull request](https://github.com/pbiernat/ripr/pull/9)

        ripr $ r2 /tmp/example3 
 -- Remember that word: C H A I R
[0x004007f0]> s sym.algo
[0x00400908]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze len bytes of instructions for references (aar)
[x] Analyze function calls (aac)
[x] Emulate code to find computed references (aae)
[x] Analyze consecutive function (aat)
[x] Type matching analysis for all functions (afta))unc.* functions (aan)
[x] Type matching analysis for all functions (afta)
[0x00400908]> #!pipe python ./r2pipe_run.py `s`
[!!] Not running in Binary Ninja
[!] Not running in IDA
[+] Not running in BinaryNinja
[ripr] Packaging function 0x400908
(4196616,)
Enter Class Name? asdf
Resolving Dependencies for 400908
[ripr] Inside branchScan
[ripr] JUMP TARGET: 4196668
[ripr] Found LLIL CALL instruction
[ripr] IL_INST Dest:
[ripr] JUMP TARGET: 4196641
[ripr] Inside dataScan
Target code may depend on outside code, attempt to map automatically? (Y/N)Y
[ripr] Performing analysis on code dependencies...
Found CodeRef: 4196582::call
Resolving Dependencies for 4008e6
[ripr] Inside branchScan
[ripr] Found imported Call target...
[ripr] Inside dataScan
Found Potential Pointer: 4196977
[ripr] Selection includes calls to imported Functions!
Code contains calls to imported functions. How should this be handled? (nop, hook, cancel)?hook
[ripr] Found these potential Data References
Data Referenced: 0x400a71
Use Section-Marking Mode for data dependencies (default; yes) (Y/N)yes
Mapping Sections
[(4196960, 4196981, u'.rodata')]
[{4196616: <codegen.codeSlice object at 0x7fbcc90c3550>}, {4196582: <codegen.codeSlice object at 0x7fbcc90c3850>}]
from unicorn import *
from unicorn.x86_const import *

import struct
class asdf(object):
    def __init__(self):
        self.mu = Uc(UC_ARCH_X86, UC_MODE_64)
        self.code_0 = '554889e54883ec10897dfcbf710a4000e885feffff8b45fc0faf45fc0faf45fcc9c3'.decode('hex') 
        self.code_1 = '554889e54883ec20897decc745fc00000000c745f8000000008b45f83b45ec7d138b45f889c7e8b3ffffff0145fc8345f801ebe58b45fcc9c3'.decode('hex') 

        self.data_0 = '010002000000000000000000000000000068692100'.decode('hex') 

        self.mu.mem_map(0x400000,0x200000)
        self.mu.mem_map(0x7ffff000,0x200000)

        self.mu.mem_write(0x400a60, self.data_0)
        self.mu.mem_write(0x4008e6, self.code_0)
        self.mu.mem_write(0x400908, self.code_1)

        self.hookdict = {4196603: 'hook_puts'}
    def hook_puts(self):
        pass
    def _start_unicorn(self, startaddr):
        try:
            self.mu.emu_start(startaddr, 0)
        except Exception as e:
            if self.mu.reg_read(UC_X86_REG_RIP) == 1:
                return
            retAddr = struct.unpack("<q", self.mu.mem_read(self.mu.reg_read(UC_X86_REG_RSP), 8))[0]
            if retAddr in self.hookdict.keys():
                getattr(self, self.hookdict[retAddr])()
                self.mu.reg_write(UC_X86_REG_RSP, self.mu.reg_read(UC_X86_REG_RSP) + 8)
                self._start_unicorn(retAddr)
            else:
                raise e
    def run(self):
        self.mu.reg_write(UC_X86_REG_RSP, 0x7fffffff)
        self.mu.mem_write(0x7fffffff, '\x01\x00\x00\x00')
        self._start_unicorn(0x400908)
        return self.mu.reg_read(UC_X86_REG_RAX)

## `r2scylla` scylla for radare2

  [zlowram/r2scylla](https://github.com/zlowram/r2scylla)

## Plugins Errors/Installation Help

  - Error: `checking pkg-config flags for r_core... no`
    - `sudo apt install pkg-config` (tested on Ubuntu 16.04)
  - Installing the latest NodeJS

    [Installing Node.js via package manager | Node.js](https://nodejs.org/en/download/package-manager/)