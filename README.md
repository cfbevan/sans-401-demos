# SANS 401 Crypto Demos

A small set of scripts to demo different crypto techniques.

# xor
Demo xor as a crypto technique.

```
usage: xor.py [-h] word

Demo xor.

positional arguments:
  word        Word to encrypt

optional arguments:
  -h, --help  show this help message and exit
```

# rot
Demo rotation as a crypto technique.
```
usage: rot.py [-h] [--rotate ROTATE] word [word ...]

Rotate a string by a number.

positional arguments:
  word             Words to encrypt

optional arguments:
  -h, --help       show this help message and exit
  --rotate ROTATE  rotate by a number (default 13)
  ```

# sub
Demo substituteion as a crypto technique.

```
usage: sub.py [-h] [--decrypt] [--stats] word [word ...]

Substitute characters in string using key.

positional arguments:
  word        Words to encrypt/decrypt

optional arguments:
  -h, --help  show this help message and exit
  --decrypt   decrypt string
  --stats     print stats of string
```