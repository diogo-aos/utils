#!/usr/bin/python3

import datetime
import os.path
import subprocess as sp
import time
import sys

ext = '.md'
date = datetime.datetime.now()
filename_ori = date.strftime('%d-%m-%Y')
num_ext = ''
num = 1
while os.path.exists(filename_ori + num_ext + ext):
    num += 1
    num_ext = '_{}'.format(num)

fn = filename_ori + num_ext + ext

if len(sys.argv) == 1:
    print('no tags received')

tags = sys.argv[1:]

tag = ', '.join(tags)

with open(fn, 'w') as f:
    f.write('---\n')
    f.write('date: ')
    f.write(date.strftime("%d-%m-%Y %H:%M" + '\n'))
    f.write('tag: ')
    f.write(tag + '\n')
    f.write('---\n')

print(fn)
#args = ['atom', os.path.abspath(fn)]
#p = sp.Popen(args, shell=True)
#p.wait()

