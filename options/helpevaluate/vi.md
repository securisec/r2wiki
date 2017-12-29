<!-- TITLE: ?vi -->
# ?vi
```
Usage: ?v[id][ num]  # Show value
```
- `?vi1 200`    -> 1 byte size value (char)
- `?vi2 0xffff` -> 2 byte size value (short)
- `?vi4 0xffff` -> 4 byte size value (int)
- `?vi8 0xffff` -> 8 byte size value (st64)
-  No argument shows $? value
- `?vi` will show in decimal instead of hex