<!-- TITLE: r2wiki.py -->

# r2wiki python
## Help

```text
usage: r2wiki.py [-h] [-a] [-l] what_to_search_for

positional arguments:
  what_to_search_for  What to search for. Supports regex . Triple escape
                      escapes. \\

optional arguments:
  -h, --help          show this help message and exit
  -a                  Will match any of the words.
  -l                  Show the corresponding r2wiki link
  -u                  Update r2wiki with latest content

To update, use -u ''
```

## Installation
### Dependencies
- `python pygments`
- `pip install -U pygments`
> NOTE: make sure your pygments is upto date for {.is-danger}
### From r2pm
- r2pm -i r2wiki
### Manual installation
<a href="https://asciinema.org/a/e9jU79M8c8cdMsgsyREfDH5qm" target="_blank"><img src="https://asciinema.org/a/e9jU79M8c8cdMsgsyREfDH5qm.png" width="50%" align="middle"/></a>
Access the radare2 wiki from inside the r2 shell
> In order for this to work, you need a local copy of the wiki. You can get it from [github](https://github.com/securisec/radare2_wiki)
> The argument supports regex and the output is in less format

> Because the output is using less, you can highlight/search using `/` or show only matching lines by using `&`

> /path/to/repo/r2wiki.py needs to be absolute path {.is-warning}

- This can be accessed multiple ways. 
	- Method 1: Set an alias in your `~/.radare2rc` file		
    ```sh
    echo '$'wiki="#"'!'"pipe python /path/to/repo/r2wiki.py" >> ~/.radare2rc
    ```
	 > Invoke as `$wiki arg`
	- Method 2: Set an alias from inside r2 shell:
	```text
	$wiki=#!pipe python /path/to/r2wiki.py
	```
	 > invoke as `$wiki arg`
	- Method 3: 
    ```text
    #!pipe python /path/to/repo/r2wiki.py
    ```
		


<p hidden>python wiki</p>
		