#!/usr/bin/env python3
# -*- coding: utf8 -*-

import subprocess as sp

#from secret_bot import API_TOKEN
#print(API_TOKEN)

cmd = "fortune"
output = sp.run(cmd.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
print(output.stdout)

