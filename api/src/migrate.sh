#!/bin/bash

#echo "### clean ###"
#rm -rf app.db
#rm -rf migrations/

export FLASK_APP="manage.py" 

echo "### migrate ###"
flask db init

echo "### migrate ###"
flask db migrate

echo "### upgrade ###"
flask db upgrade
