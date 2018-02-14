<!-- TITLE: dx -->

#  `dx[?]` Inject and run code on target process (See gs)


```
Usage: dx # Code injection commands
```


- `dx <opcode>...` Inject opcodes
- `dxa nop` Assemble code and inject
- `dxe egg-expr` Compile egg expression and inject it
- `dxr <opcode>...` Inject opcodes and restore state
- `dxs write 1, 0x8048, 12` Syscall injection (see gs)

    
```
Examples: 
		| dx 9090 Inject two x86 nop
		| "dxa mov eax,6;mov ebx,0;int 0x80" Inject and restore state
```

<p hidden>dx dxa dxe dxr dxs</p>