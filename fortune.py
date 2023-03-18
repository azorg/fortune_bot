#!/usr/bin/env python3
# -*- coding: utf8 -*-

import subprocess as sp

#from secret_bot import API_TOKEN
#print(API_TOKEN)

FORTUNE = "/usr/games/fortune"

CPUINFO = ["sh",  "-c",
           "cat /proc/cpuinfo | grep 'model name' | head -n1 | " + \
           "cut -d: -f2 | sed -r 's/  */ /g' | sed -r 's/^ *| *$//'"]

DISK = ["sh", "-c",
        "LC_ALL=C df -Phl -x tmpfs | grep -v '/dev$'"]

output = sp.run(FORTUNE.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

output = sp.run(CPUINFO, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

output = sp.run(DISK, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

