<!-- TITLE: fd -->

#  `fd addr` return flag+delta


```text
Usage: fd[d] [offset|flag|expression]
```

- `fd $$`         # describe flag + delta for given offset
- `fd.`           # check flags in current address (no delta)
- `fdd $$`        # describe flag without space restrictions
- `fdw [string]`  # filter closest flag by string for current offset

<p hidden>fd fdd fdw fd.</p>