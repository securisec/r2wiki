<!-- TITLE: r2wiki.py -->

# r2wiki python
Access the radare2 wiki from inside the r2 shell
> In order for this to work, you need a local copy of the wiki. You can get it from [github](https://github.com/securisec/radare2_wiki)
> The argument supports regex and the output is in less format

> /path/to/repo/r2wiki.py needs to be absolute path {.is-warning}
{.is-info}
- This can be accessed multiple ways. 
	- Method 1: Set an alias in your `~/.radare2rc` file		
    ```sh
    echo '$'wiki="#"'!'"pipe python /path/to/repo/r2wiki.py" >> ~/.radare2rc
    ```
	 > Invoke as `$wiki arg`
	- Method 2: Set an alias from inside r2 shell:
	```text
	$wiki='#!pipe python /path/to/r2wiki.py'
	```
	 > invoke as `$wiki arg`
	- Method 3: 
    ```text
    #!pipe python /path/to/repo/r2wiki.py
    ```


<p hidden>python wiki</p>
		