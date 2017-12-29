<!-- TITLE: i -->

#  **`i`** Get info about opened file from r_bin

Usage: i Get info from opened file (see rabin2's manpage)

- Output mode:
  - **`'*'`** Output in radare commands
  - **`'j'`** Output in json
  - **`'q'`** Simple quiet output
- Actions:

  - **`i|ij`** Show info of current file (in JSON)
  - **`iA`** List archs
  - **`ia`** Show all info (imports, exports, sections..)
  - **`ib`** Reload the current buffer for setting of the bin (use once only)
  - **`ic`** List classes, methods and fields
  - **`icc`** List classes, methods and fields in Header Format
  - **`iC`** Show signature info (entitlements, ...)

  - [ `id[?]` Debug information (source lines)](/options/i/id)

  - **`idp`** Load pdb file information
  - **`iD lang sym`** demangle symbolname for given language
  - **`ie`** Entrypoint
  - **`iee`** shows entrypoint and endpoint. Shows init and fini 
  - **`iE`** Exports (global symbols)
  - **`ih`** Headers (alias for iH)
  - **`iHH`** Verbose Headers in raw text
  - **`ii`** Imports
  - **`iI`** Binary info
  - **`ik [query]`** Key-value database from RBinObject
  - **`il`** Libraries _information libraries_
	  > 🚀 `il` can be used to show linked libraries [asciinema](https://asciinema.org/a/NYgYqTer5PAyoTLbOWp5UUqtP)
  - **`il.`** nothing documented 👎
  - **`iL [plugin]`** List all RBin plugins loaded or plugin details
  - **`im`** Show info about predefined memory allocation
  - **`iM`** Show main address
  - **`io [file]`** Load info from file (or last opened) use bin.baddr
  - **`ir`** Relocs
  - **`iR`** Resources
  - **`is`** Symbols
  - **`iS [entropy,sha1]`** Sections (choose which hash algorithm to use)
  - **`iV`** Display file version info
  - **`iz|izj`** Strings in data sections (in JSON/Base64)
  - **`izz`** Search for Strings in the whole binary
  - **`iZ`** Guess size of binary program

<p hidden>ij iA ia ib ic icc iC idp iD ie iE ih iHH ii iI ik il iL im iM io ir iR is iS iV iz izj izz iZ iee</p>