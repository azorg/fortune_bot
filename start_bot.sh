#!/bin/sh

WDIR=`dirname $0`
OLDPWD=`pwd`

whoami

cd "$WDIR"

. "./venv/bin/activate"

pwd

python3 fortune_bot.py

cd "$OLDDIR"

