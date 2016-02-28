
# simple key-value store. the value is saved in the local filesystem
# using its sha256 hash as the filename.

import traceback, sys, os, hashlib, json

data_path = '/srv'


# retrieve data by its hash value, returns None if hash not found
def get_value(hashkey):

    value = ''  # return on cache-miss
    path = data_path + '/' + hashkey

    if (os.path.isfile(path)):
        try:
            with open(path, 'r') as data_file:
                value = data_file.read()

        except IOError as e:
            errinfo, traceback = sys.exc_info()
            sys.stderr.write('error opening %s: %s' % (errinfo.filename, errinfo.strerror))

    return value
        

# write data using its hash as a key, returns the hash or None on error
def set_value(value):

    # check JSON syntax
    try:
        tmp = json.loads(value)

    except:
        sys.stderr.write('error: invalid JSON string: {}'.format(str(value)))
        return None


    # save value using hash for fileaname
    hashkey = hashlib.sha256(value).hexdigest()
    path = data_path + '/' + hashkey

    try:
        with open(path, 'w') as data_file:
            data_file.write(value + '\n')

    except IOError as e:
        errinfo, traceback = sys.exc_info()
        sys.stderr.write('error: opening %s: %s' % (errinfo.filename, errinfo.strerror))
        return None
    
    return hashkey



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

