# AKA
Python Script to create aliases for long-named command line executables

## Installation
```
git clone https://www.github.com/soubikbhuiwk007/aka
cd aka
./aka.py -n <alias-name> <exec-path>
```
To access the `aliases` globally from command line, add the path `~/.aka.bin/` or `C:\Users\<user>\.aka.bin\` to the `Path` environment variable.

## Why did I made this ?

When I was using `VBoxManage.exe` to use the `virtualbox` from `command-line`, the name of the executable seemed pretty long to me. So I thought of creating `alias` for those long-named executables. That's why I wrote a simple `python` script that could do this.
