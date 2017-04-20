#/usr/bin/python3
# Author: CrazyWhiteMonkey
# Date: April 20, 2017
# What is this? = An insecure password locker program.
# Script Name =- pw.py
#Usage - python3 pw.py account

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) > 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account naned ' + account)