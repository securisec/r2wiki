<!-- TITLE: wop -->

# `wop[DO][arg]` De Bruijn Patterns

```text
Usage: wop[DO] len @ addr | value
```

- `wopD len [@ addr]`   Write a De Bruijn Pattern of length 'len' at address 'addr'
- `wopD* len [@ addr]`  Show wx command that creates a debruijn pattern of a specific length
- `wopO value`          Finds the given value into a De Bruijn Pattern at current offset

<p hidden>wopD wopD* wopO</p>