#!/bin/sh

WDIR=`dirname $0`
OLDPWD=`pwd`

cd "$WDIR"

. "./venv/bin/activate"

python3 "fortune_bot.py"

cd "$OLDPWD"

