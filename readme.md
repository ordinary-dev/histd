# How I spent this day

A simple but useful personal diary application.

The sole purpose of this application is to quickly create a file
and open it in a text editor so that I can take a note before I lose my desire.
Notes can be found in the `~/.local/share/histd` directory.

```sh
tree ~/.local/share/histd
# /home/user/.local/share/histd
# └── 2022
#     └── 08
#         ├── 18.txt
#         └── 19.txt
```

## Usage
```sh
python3 histd.py
```

## Installation
To copy the script to `/usr/local/bin`, run this command as root:
```sh
make install
```
