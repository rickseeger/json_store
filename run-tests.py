#!/usr/bin/python

import unittest, datastore, hashlib, random


class test_datastore(unittest.TestCase):
 
    def setUp(self):
        pass
 

    def test_write_read(self):

        value = str(random.random())
        key = datastore.set_value(value)
        value2 = datastore.get_value(key)
        self.assertEqual(value, value2)


    def test_cache_miss_returns_empty_string(self):

        rand_value = str(random.random())
        rand_key = hashlib.sha256(rand_value).hexdigest()
        value = datastore.get_value(rand_key)
        self.assertEqual(value, '')

    
    def test_write_hash_returned(self):

        value = '{ "company" : "ItBit" }'
        hashkey = datastore.set_value(value)
        self.assertEqual(hashkey, '84aee9fb0137a38d6ef082bb210ea787f9e8d649ab699ad94acaa61d980e13e6')

    
if __name__ == '__main__':
    unittest.main()

