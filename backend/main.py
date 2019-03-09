#!/usr/bin/env python

import re, json

from bottle import route, run, template
from bottle import request, response, hook
from bottle import post, get, put, delete

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

_personajes = [
      {
        "first_name": "Jill",
        "last_name": "Valentine",
        "twitter": "eviljill",
        "juegos":[1,3,5]
      },
      {
        "first_name": "Leon",
        "last_name": "Kennedy",
        "twitter": "evilleon",
        "juegos":[2,4,6]
      }
  ]


@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''
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
      first_name = data['first_name']
      last_name = data["last_name"]
      twitter = data["twitter"]
      _personajes.append({
        "first_name": first_name,
        "last_name": last_name,
        "twitter": twitter,
      })
      status = True

    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'status': status})

@get('/personaje')
def listing_handler():
    '''Handles name listing'''
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(_personajes)


@get('/')
def index(name):
    return template('Hello World!')


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

