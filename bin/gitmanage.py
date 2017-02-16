#!/home/diogoaos/workspace/general_pyenv3/bin/python

from git import Repo
import subprocess as sp
from os import chdir, curdir
from os.path import expanduser, abspath
from collections import OrderedDict

#How to add a file with GitPython:
#repo.git.add('app/static/ui_prot.html', A=True)

startpath = abspath(curdir)

projects = {
    'centralserver': '~/workspace/centralserver',
    'piccolosdk': '~/workspace/piccolosdk',
    'sharpeye15': '~/workspace/sharpeye15'
}
projects_c = {
    'operation_ready': '~/workspace/operation_ready',
    'pypiccolo': '~/workspace/pypiccolo',
    'pmu_software': '~/workspace/pmu_software',
    'db_utils': '~/workspace/db_utils',
    'data_viz': '~/workspace/data_viz'
}

selected_projs = projects_c

class StringPrep:
    HEADER = '\033[95m'
    c_project = '\033[94m'
    c_green = '\033[92m'
    c_branch = '\033[93m'
    c_red = '\033[91m'
    c_ENDC = '\033[0m'

def print_project(proj):
    print(StringPrep.c_project + '{}project: {} {}'.format('', proj, '* ' * 0) + StringPrep.c_ENDC)

def print_branch(branch):
    print(StringPrep.c_branch + 'branch: {} {}'.format(branch, '# ' * 0) + StringPrep.c_ENDC)

def print_staged(changetype, path):
    print( StringPrep.c_green + '{} \t{}'.format(changetype, path) + StringPrep.c_ENDC )

def print_unstaged(changetype, path):
    print( StringPrep.c_red + '{} \t{}'.format(changetype, path) + StringPrep.c_ENDC )

def print_untracked(path):
    print( StringPrep.c_red + path + StringPrep.c_ENDC )

def status(repo, branch):
    modified_files = repo.index.diff(None)
    staged_files = repo.index.diff(branch)
    untracked_files = repo.untracked_files

    if staged_files:
        staged_type = {'D': 'new file', 'M': 'modified', 'A': 'deleted'}
        print('')
        print(' '*4, end='')
        print('Staged:')
        for f in staged_files:
            print(' '*4, end='')
            print_staged(staged_type.get(f.change_type, 'unknown'), f.a_path)

    if modified_files:
        unstaged_type = {'D': 'deleted', 'M': 'modified'}
        print('')
        print(' '*4, end='')
        print('Not staged:')
        for f in modified_files:
            print(' '*4, end='')
            print_staged(unstaged_type.get(f.change_type, 'unknown'), f.a_path)

    if untracked_files:
        print('')
        print(' '*4, end='')
        print('Untracked:')
        for fi in untracked_files:
            print(' '*4, end='')
            print_untracked(fi)
        print('')


def process_repo(proj, path):
    print_project(proj)
    repo = Repo(path)
    branches = [b.name for b in repo.branches]
    for b in branches:
        print(' '*2, end='')
        print_branch(b)
        status(repo, b)

    ret = input('')
    if not ret:
        return

    # for i, b in enumerate(branches):
    #     print('{} - {}'.format(i, b))
    # branch = input('choose branch: ')
    print('interpreter mode (press q to exit)')
    cmd_str = ''
    while True:
        cmd_str = input('> ')
        if cmd_str == '':
            continue
        if cmd_str == 'q':
            break
        cmds = cmd_str.split(' ')
        chdir(expanduser(path))
        p = sp.Popen(cmds, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        output, err = p.communicate()
        if output:
            print(output.decode('ASCII'))
        if err:
            print(err.decode('ASCII'))
    process_repo(proj, path)

ordprojs = OrderedDict(sorted(selected_projs.items()))
for proj, ppath in ordprojs.items():
    process_repo(proj, ppath)

chdir(startpath)
