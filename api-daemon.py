#!/usr/bin/python

import datastore
from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/datastore/<hashkey>')
def get_data(hashkey):
    return datastore.get_value(hashkey)


@app.route('/datastore/set', methods=['POST'])
def insert_data():
    data = request.form['v']
    hashkey = datastore.set_value(data)
    if hashkey is None:
        return 'Failed to insert record'
    else:
        return redirect('/datastore/'+str(hashkey), code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

