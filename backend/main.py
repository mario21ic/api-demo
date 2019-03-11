#!/usr/bin/env python

import re, json

from bottle import route, run, template
from bottle import request, response, hook
from bottle import post, get, put, delete

import mysql.connector

cnx = mysql.connector.connect(host='db', database='api_db', user='root', password='myclave')
cursor = cnx.cursor()

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers


@route('/personaje', method=['POST', 'OPTIONS'])
def save_handler():
    if request.method == "OPTIONS":
      return json.dumps({'status': True})

    status = False
    data = request.json
    if data['first_name'] is not None and \
      data["last_name"] is not None and \
      data["twitter"] is not None:
      sql_insert_query = "insert into `personaje` values(NULL, '%s', '%s', '%s')" % (data['first_name'], data["last_name"], data["twitter"])
      result  = cursor.execute(sql_insert_query)
      cnx.commit()
      status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status})

@get('/personaje')
def listing_handler():
    query = ("SELECT * FROM personaje")
    cursor.execute(query)
    records = cursor.fetchall()
    personajes = []
    for row in records:
        personajes.append({
        "id": row[0],
        "first_name": row[1],
        "last_name": row[2],
        "twitter": row[3],
        })
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(personajes)

@get('/')
def index():
    return json.dumps({"message": "Hello World"})


_names = set()                    # the set of names

namepattern = re.compile(r'^[a-zA-Z\d]{1,64}$')



@put('/names/<oldname>')
def update_handler(name):
    '''Handles name updates'''
    try:
        # parse input data
        try:
            data = json.load(utf8reader(request.body))
        except:
            raise ValueError

        # extract and validate new name
        try:
            if namepattern.match(data['name']) is None:
                raise ValueError
            newname = data['name']
        except (TypeError, KeyError):
            raise ValueError

        # check if updated name exists
        if oldname not in _names:
            raise KeyError(404)

        # check if new name exists
        if name in _names:
            raise KeyError(409)

    except ValueError:
        response.status = 400
        return
    except KeyError as e:
        response.status = e.args[0]
        return

    # add new name and remove old name
    _names.remove(oldname)
    _names.add(newname)

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': newname})


@delete('/names/<name>')
def delete_handler(name):
    '''Handles name updates'''

    try:
        # Check if name exists
        if name not in _names:
            raise KeyError
    except KeyError:
        response.status = 404
        return

    # Remove name
    _names.remove(name)
    return

run(host='0.0.0.0', reloader=True, port=8080)

