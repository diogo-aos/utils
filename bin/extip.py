import sys
import urllib.request
import subprocess as sp
import os
import time

dir = '/home/chiro/workspace/extip/'
fn = 'extip.txt'
current_ip = ''

print('changing dir...')
os.chdir(dir)

first = True

while True:
    if not first:
        print('sleeping...')
        time.sleep(60)
    else:
        first = False
    print('requesting ip...')
    resp = urllib.request.urlopen('https://myexternalip.com')
    print('got response...')
    data = resp.readlines()

    print('parsed lines...')
    line = None
    for l in data:
        if b'<title>My External IP address -' in l:
            line = l

    if line is None:
        continue

    ip = ''
    for c in line:
        if  c == ord('.') or (c >= ord('0') and c <= ord('9')):
            ip += chr(c)

    if ip == current_ip:
        continue

    print('new ip: {}'.format(ip))
    current_ip = ip

    print('writing ip to file...')
    with open (fn, 'w') as f:
        f.write(ip)

    print('pushing git...')
    sp.Popen(['git', 'add', '-A'])
    sp.Popen(['git', 'commit', '-m', 'new ip'])
    sp.Popen(['git', 'push', 'origin', 'master'])
