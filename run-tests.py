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
        self.assertEqual('')

    
    def test_write_hash_returned(self):

        value = "ItBit"
        hashkey = datastore.set_value(value)
        self.assertEqual(hashkey, '0fedc5c0162c9dbe53ccb6aeb22ac953c9ced58644eed7ee5f9301bd5af492dd')

    
if __name__ == '__main__':
    unittest.main()

