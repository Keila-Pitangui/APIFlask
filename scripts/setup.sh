#!/bin/bash

pytho3 -m pip install --upgrade pip

pip install flask_sqlachemy

#instala as dependências no arquivo requirements
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt