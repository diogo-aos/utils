#!/bin/bash

# have bashrc add this repo's bin folder to the PATH
ROOT_PATH=$(dirname `readlink -f "$0"`)

cd $ROOT_PATH  # cd to folder where script lives
cd ..
cd bin
chmod +x *
echo "export PATH=\$PATH:$(pwd)" >> $HOME/.bashrc

# have bashrc execute commands in this repo's bashrc
#BASHRC_PATH=$ROOT_PATH/config/bashrc
cd ../config
echo "source $(pwd)/bashrc" >> $HOME/.bashrc
