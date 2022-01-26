#!/bin/bash

# have bashrc add this repo's bin folder to the PATH
ROOT_PATH=$(dirname `readlink -f "$0"`)

cd $ROOT_PATH  # cd to folder where script lives
cd ..

cp config/i3.config $HOME/.config/i3/config
