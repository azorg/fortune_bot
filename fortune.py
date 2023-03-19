#!/usr/bin/env python3
# -*- coding: utf8 -*-

import subprocess as sp

try:
    from secret_bot import API_TOKEN
except:
    API_TOKEN = "0123456789:AAAOOOlefqewoOUyOIOiybOUybUYvpwrXRX"

print(API_TOKEN)

FORTUNE = "/usr/games/fortune"

CPUINFO = ["sh",  "-c",
           "cat /proc/cpuinfo | grep 'model name' | head -n 1 | " + \
           "cut -d: -f2 | sed -r 's/  */ /g' | sed -r 's/^ *| *$//'"]

CPUFREQ = ["sh",  "-c",
           "cat /proc/cpuinfo | grep 'cpu MHz' | head -n 1 | " + \
           "cut -d: -f2 | sed 's/^ */F=/' | sed 's/ *$/MHz/'"]

MEMINFO = ["sh", "-c",
           "free -m | tail -n +2 | " + \
           "awk '{printf(\"%s\ttotal=%sMB\tused=%sMB\tfree=%sMB\\n\",$1,$2,$3,$4)}'"]

DISK = ["sh", "-c",
        "LC_ALL=C df -Phl -x tmpfs | grep -v '/dev$'"]

output = sp.run(FORTUNE.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

cpuinfo = sp.run(CPUINFO, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
cpufreq = sp.run(CPUFREQ, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(cpuinfo.stdout + cpufreq.stdout)

output = sp.run(MEMINFO, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

output = sp.run(DISK, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

