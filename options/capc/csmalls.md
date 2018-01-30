<!-- TITLE: Cs -->

#  **`Cs[?] [-] [size] [@addr]`** add string


```text
Usage: Cs[ga-*.] [size] [@addr]
```


- **`NOTE: size`** 1 unit in bytes == width in bytes of smallest possible char in encoding, so ascii/latin1/utf8 = 1, utf16le = 2
- **`Cs`** list all strings in human friendly form
	> As an example: `Cs` will give strings from bytes
- **`Cs*`** list all strings in r2 commands
- **`Cs [size] @addr`** add string (guess latin1/utf16le)
- **`Csg [size] [@addr]`** as above but addr not needed
- **`Cz [size] [@addr]`** ditto
- **`Csa [size] [@addr]`** add ascii/latin1 string
- **`Cs8 [size] [@addr]`** add utf8 string
- **`Cs- [@addr]`** remove string
- **`Cs.`** show string at current address
- **`Cs..`** show string + info about it at current address

<p hidden>Cs Cs* Csg Cz Csa Cs8 Cs- Cs.. Cs.</p>