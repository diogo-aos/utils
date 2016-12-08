#!/usr/bin/python3

import argparse
import os
import sys
from uuid import uuid4

parser = argparse.ArgumentParser(description='Create new Firefox profile.')
parser.add_argument('name', type=str, help='profile name')
parser.add_argument('--ppath', help='path to store profile folder')

args = parser.parse_args()

ff_path = '$HOME/.mozilla/firefox/'
ff_path = os.path.expandvars(ff_path)
ff_path = os.path.expanduser(ff_path)
base_profile_path = ''  # if used, path for base profile

prof_name = args.name
prof_path = args.ppath

# TODO: sanitize profile name

if prof_path:
    prof_path = os.path.expandvars(prof_path)
    prof_path = os.path.expanduser(prof_path)
    if not os.path.exists(args.ppath):
        print('profile path does not exist')
        sys.exit(1)
else:
    prof_path = ff_path

prof_folder = '{}.{}'.format(uuid4().hex[:8], prof_name)
prof_folder_path = os.path.join(prof_path, prof_folder)
os.mkdir(prof_folder_path)

# determine number of new profile
f = open(ff_path + 'profiles.ini','r')
data = f.read()
number = 1
if data.find('[Profile') != -1:
    number = int(data.split('[Profile')[-1].split(']')[0])

f.close()

# create new profile

f = open(ff_path + 'profiles.ini', 'a')
to_write = ['\n',
    '[Profile{}]\n'.format(number),
    'Name={}\n'.format(prof_name),
    'IsRelative=0\n',
    'Path={}'.format(prof_folder_path)]
f.writelines(to_write)
