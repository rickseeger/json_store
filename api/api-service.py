import sys, os
from flask import Flask
app = Flask(__name__)

datastore = '/srv'


@app.route('/<hashkey>')
def get_value(hashkey):

    path = datastore + '/' + hashkey
    app.logger.debug('data path [%s]' % path)

    payload = None
    if (os.path.isfile(path)):
        app.logger.debug('data found [%s]' % path)
        with open(path, 'r') as f:
            payload = f.read()
            app.logger.debug('payload [%s]' % payload.strip())
            return payload
    else:
        app.logger.debug('data not found [%s]' % path)
        return None
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

