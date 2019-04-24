This repo holds a collection of useful things, from aliases and config files
from various applications to utility scripts.

# Installation
| script           | description |
| ---------------- | ---------- |
| install_utils.sh | installs the bashrc, adds bin folder to path |
| install_i3.sh | installs i3 configuration |
| install_i3_scripts.sh | creates python virtualenv for i3 scripts, adds keyboard binding to i3 config for scripts |
| python_envs.sh | creates general python virtualenvs for python2 and python3 and creates appropriate aliases |


# Aliases
## Python Virtualenv aliases
`alias virton="source pyenv/bin/activate`

`alias genv3="source $HOME/.general_py3/bin/activate`

`alias genv2="source $HOME/.general_py2/bin/activate`

## Terminal alias
This alias simply hides the `user@machinename:/current/path$ ` by the simpler `>`.
