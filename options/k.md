<!-- TITLE: k -->

#  **`k`** Run sdb-query. see k? for help, 'k *', 'k **' ...


```text
Usage: k[s] [key[=value]]Sdb Query
```


- **`k foo=bar`** set value
- **`k foo`** show value
- **`k`** list keys
- **`ko [file.sdb] [ns]`** open file into namespace
- **`kd [file.sdb] [ns]`** dump namespace to disk
- **`ks [ns]`** enter the sdb query shell
- **`k anal/meta/*`** ist kv from anal > meta namespaces
- **`k anal/**`** list namespaces under anal
- **`k anal/meta/meta.0x80404`** get value for meta.0x80404 key

<p hidden>ko kd ks</p>