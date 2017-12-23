# Radare2 Wiki
The goal of this wiki is to make a searchable collection of documents which can be used to find various use cases and help regarding using r2. This is a live wiki and the 
 goal is to updated frequently. If you have a tip, use case or plugin you would like to suggest, either create an issue, or tweet to me at [@securisec](https://twitter.com/securisec)

This wiki can be used either from the online version or locally.

#### Credits:
Tons of great youtube videos, the radare2 irc channel, twitter, too many to list.
Wiki is powered by [wiki.js](https://wiki.js.org/)

## Online
The wiki is available online at [https://radare2.securisec.com](https://radare2.securisec.com)

## Local Installation
- Install wiki.js by following [these instructions](https://docs.requarks.io/wiki/install)
- Copy all the files in this repo to the `repo` directory, or run 
```git clone https://github.com/securisec/radare2_wiki.git repo/``` from inside your wiki directory.
- Allow some time for the search to finish indexing.

#### Update local installation
- To update to the latest **(this wiki will be updated frequently :stuck_out_tongue_winking_eye:)**, simply run  
`git pull origin master` from inside the repo directory.

#### Tips
To style your local wiki in a manner similar to the online version, add the following to the `/wiki_installation_dir/server/views/layout.pug` under the section marked as `//- JS / CSS`  
```css
    style(type='text/css').
      .mkcontent {
        font-family: Arial;
      }

    style(type='text/css').
      .mkcontent {
        font-size: 16px;
      }
```
