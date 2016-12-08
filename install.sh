#!/bin/bash

# have bashrc add this repo's bin folder to the PATH
ROOT_PATH=$(dirname `readlink -f "$0"`)
BIN_PATH=$ROOT_PATH/bin
chmod +x $BIN_PATH/*
echo "export PATH=\$PATH:$BIN_PATH" >> $HOME/.bashrc

# have bashrc execute commands in this repo's bashrc
BASHRC_PATH=$ROOT_PATH/config/bashrc
cat "source $BASHRC_PATH" >> $HOME/.bashrc
