This repo holds a collection of useful things, from aliases and config files 
from various applications to utility scripts.

# Installation
The `install.sh` script simply adds `/bin` to the `$PATH` inside the system's
`bashrc`. It also has the system's `bashrc` source `/config/bashrc`.

# Aliases
## Python Virtualenv aliases
`alias virton="source pyenv/bin/activate`
`alias genv3="source $HOME/.general_py3/bin/activate`
`alias genv2="source $HOME/.general_py2/bin/activate`

## Terminal alias
This alias simply hides the `user@machinename:/current/path$ ` by the simpler `>`.

# Firefox profile creator
```
usage: ff_new_prof.py [-h] [--ppath PPATH] name

Create new Firefox profile.

positional arguments:
  name           profile name

optional arguments:
  -h, --help     show this help message and exit
  --ppath PPATH  path to store profile folder
```
