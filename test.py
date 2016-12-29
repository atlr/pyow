#!/usr/bin/env python

import unittest
import main

class Test_gen_url(unittest.TestCase):

    FORMAT_PSN_URL ='https://playoverwatch.com/en-us/career/psn/{0}'
    FORMAT_XBL_URL ='https://playoverwatch.com/en-us/career/xbl/{0}'
    ARB_NAME ='cham'
    ARB_NUM ='223'
    HYPHENATED_NAME ='-'.join([ARB_NAME, ARB_NUM])

    def test_console_name_hyphen_num(self):
        URL =Test_gen_url.FORMAT_PSN_URL.format(Test_gen_url.ARB_NAME)
        name_arg =Test_gen_url.HYPHENATED_NAME
        self.assertEqual(main.gen_url(name_arg, main.PSN), URL)

    def test_console_name_sharp_num(self):
        NAME ='#'.join([Test_gen_url.ARB_NAME, Test_gen_url.ARB_NUM])
        URL =Test_gen_url.FORMAT_XBL_URL.format(Test_gen_url.ARB_NAME)
        self.assertEqual(main.gen_url(NAME, main.XBL), URL)

    def test_nonplatform(self):
        self.assertRaises(ValueError, main.gen_url, Test_gen_url.ARB_NAME, 'NEPTUNE')

    def test_nonregion(self):
        name_arg =Test_gen_url.HYPHENATED_NAME
        platform_arg =(main.PC, 'ELSEPLACE')
        self.assertRaises(ValueError, main.gen_url, name_arg, platform_arg)

    def test_greater_than_2_tuple(self):
        name_arg =Test_gen_url.HYPHENATED_NAME
        THREE_TUPLE =(main.PC, 'PLANEPTUNE', 'NEPTUNA')
        self.assertRaises(ValueError, main.gen_url, name_arg, THREE_TUPLE)

    def test_pc_no_region(self):
        self.assertRaises(ValueError, main.gen_url, Test_gen_url.HYPHENATED_NAME, main.PC)
    
if __name__=='__main__':
    unittest.main()

