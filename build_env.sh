#!/bin/sh

WDIR=`dirname $0`
OLDPWD=`pwd`

cd "$WDIR"

rm -rf venv

sudo apt -y install fortunes fortunes-ru

sudo apt -y install python3 python3-virtualenv

virtualenv venv -p python3

. "./venv/bin/activate"

pip install aiogram

cd "$OLDPWD"

