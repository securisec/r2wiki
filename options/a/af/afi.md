<!-- TITLE: afi -->
#  `afi [addr|fcn.name]`   show function(s) information (verbose afl)

- `afi`   show information of the function
	> Use `afi~offset[1]` to get the functions entrypoint or offset

  > 🚀 Use `afi` to show call references for a function. [asciinema](https://asciinema.org/a/1aLHLqw0dmR6ZH78fWvDlpYFG)
- `afi.`   show function name in current offset
- `afi*`   function, variables and arguments
- `afij`   function info in json format
- `afil`   verbose function info

<p hidden>afi afi. afi* afij afil</p>