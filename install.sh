#!/bin/bash

BIN_PATH=$(dirname `readlink -f "$0"`)/bin

chmod +x $BIN_PATH/*

echo "export PATH=\$PATH:$BIN_PATH" >> $HOME/.bashrc
