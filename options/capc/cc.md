<!-- TITLE: CC -->

#  **`CC[?] [-] [comment-text] [@addr]`** add/remove comment


```text
Usage: CC[-+!*au] [base64:..|str] @ addr
```


- **`CC`** list all comments in human friendly form
- **`CC*`** list all comments in r2 commands
- **`CC.`** show comment at current offset
- **`CC, [file]`** show or set comment file
- **`CC [text]`** append comment at current address
- **`CCf`** list comments in function
- **`CC+ [text]`** append comment at current address
- **`CC!`** edit comment using cfg.editor (vim, ..)
- **`CC- @ cmt_addr`** remove comment at given address
- **`CCu good boy @ addr`** add good boy comment at given address
- **`CCu base64:AA== @ addr`** add comment in base64