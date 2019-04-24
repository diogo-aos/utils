#!/bin/bash

# have bashrc add this repo's bin folder to the PATH
ROOT_PATH=$(dirname `readlink -f "$0"`)

cd $ROOT_PATH  # cd to folder where script lives
cd ..

echo "installing virtualenv"
sudo apt-get install virtualenv

echo "creating virtualenv for i3 scripts"
virtualenv  $HOME/.i3_pyenv -p python3
$HOME/.i3_pyenv/bin/pip install i3-py

echo "adding i3 keyboard bind to i3 config"
cd i3

echo "" >> $HOME/.config/i3/config
echo "# move workspace to another monitor" >> $HOME/.config/i3/config
echo "# works only horizontally" >> $HOME/.config/i3/config
echo "# bindsym \$mod+Tab move workspace to output right" >> $HOME/.config/i3/config
echo "# works horizontally and vertically" >> $HOME/.config/i3/config
echo "bindsym \$mod+Tab exec $HOME/.i3_pyenv/bin/python $(pwd)/cycle-workspace.py" >> $HOME/.config/i3/config
