
# simple key/value store. the value is saved in the local filesystem
# using its sha256 hash as the key.

import sys, os, hashlib

data_path = '/srv'


# retrieve data by its hash value, returns None if hash not found
def get_value(hashkey):

    value = None
    path = data_path + '/' + hashkey

    if (os.path.isfile(path)):

        try:
            with open(path, 'r') as data_file:
                value = data_file.read()

        except IOError as e:
            errinfo, traceback = sys.exc_info()
            sys.stderr.write('error opening %s: %s' % (errinfo.filename, errinfo.strerror))

    return value
        

# write data using its hash as a key, returns the hash or None on failure
def set_value(value):

    hashkey = hashlib.sha256(value).hexdigest()
    path = data_path + '/' + hashkey

    try:
        with open(path, 'w') as data_file:
            data_file.write(value)

    except IOError as e:
        errinfo, traceback = sys.exc_info()
        sys.stderr.write('error opening %s: %s' % (errinfo.filename, errinfo.strerror))
        hashkey = None
    
    return hashkey


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

