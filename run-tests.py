#!/usr/bin/python

import unittest, datastore, hashlib, random, sys


class test_datastore(unittest.TestCase):
 
    def setUp(self):
        pass
 

    def test_write_read(self):

        # create new record
        value = str(random.random())
        key = datastore.set_value(value)
        sys.stderr.write('wrote kv-pair: {} => {}\n'.format(key, value))

        # fetch record back
        value2 = datastore.get_value(key)
        sys.stderr.write('retrieved value: {}\n'.format(value2))
        self.assertEqual(value, value2)


    def test_cache_miss_returns_none(self):
        rand_value = str(random.random())
        rand_key = hashlib.sha256(rand_value).hexdigest()
        value = datastore.get_value(rand_key)
        sys.stderr.write('get_value returned {} on cache-miss\n'.format(value))
        self.assertIsNone(value)

    
if __name__ == '__main__':
    unittest.main()

