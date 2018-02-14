<!-- TITLE: dcu -->

#  `dcu[?] [..end|addr] ([end])` Continue until address (or range)


```
Usage: dcu Continue until address
```


- `dcu.` Alias for dcu $$ (continue until current address
  > _This will continue execution to wherever the current seek is_

  > _`dcu offset` is a better option than`db offset; dc`_
- `dcu address` Continue until address
- `dcu [..tail]` Continue until the range
- `dcu [from] [to]` Continue until the range

<p hidden>dcu</p>