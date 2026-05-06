#!/bin/bash
# make sure to make this file executable with `chmod +x setup.sh` 
python3 -m venv .venv;  # create a virutal enviroment
./.venv/bin/pip install pip --upgrade # update pip 
./.venv/bin/pip install -r requirements.txt # install requirements files 

