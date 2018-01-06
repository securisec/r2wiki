<!-- TITLE: radare2 plugins -->
# Radare Plugins

**_This a list of plugins that I find interesting._** 

## Tips
> Sometimes, a plugin installation using r2pm will fail with a Directory nonexistant error. To prevent this, simply run `mkdir -p $HOME/.config/radare2/prefix/bin/` (on Ubuntu)

## angr and r2 (symbolic exectution)
[angr and r2](/radare-plugins/angr)

## diaphora (binary diffing)
   > _Binary diffing powered by diaphora (originally for IDA Pro)_ {.is-info}

  [radare/diaphora](https://github.com/radare/diaphora)

## r2frida
[r2frida](/radare-plugins/frida)

 ## r2dec

  [wargio/r2dec-js](https://github.com/wargio/r2dec-js)  
> 🚀 [r2dec installation help and demo](https://asciinema.org/a/0Ncb0iVwwNaXFP6qkpO1hvFVI)


## r2pm package manager

  [radare/radare2-pm](https://github.com/radare/radare2-pm/tree/master/db)
	
## r2scylla scylla for radare2

  [zlowram/r2scylla](https://github.com/zlowram/r2scylla)

## rarop

  [rarop install help](/plugins/rarop-install-help)

  [jpenalbae/rarop](https://github.com/jpenalbae/rarop)
	
## ripr for radare2
[ripr for radare2](/radare-plugins/ripr)

## snowman for r2
  [radare/radare2-extras](https://github.com/radare/radare2-extras/tree/master/r2snowman)


# Plugins Errors/Installation Help

  - Error: `checking pkg-config flags for r_core... no`
    - `sudo apt install pkg-config` (tested on Ubuntu 16.04)
  - Installing the latest NodeJS

    [Installing Node.js via package manager | Node.js](https://nodejs.org/en/download/package-manager/)
		
# External plugins
## jupyter-radare2
[jupyter-radare2](https://github.com/guedou/jupyter-radare2)