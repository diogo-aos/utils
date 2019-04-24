#!/bin/bash

# have bashrc add this repo's bin folder to the PATH
ROOT_PATH=$(dirname `readlink -f "$0"`)

cd $ROOT_PATH  # cd to folder where script lives
cd ..  # cd to utils repo folder

virtualenv $HOME/.general_py3 -p python3
virtualenv $HOME/.general_py2 -p python2

cat setup/python_genvs_bashrc.txt >> $HOME/.bashrc
