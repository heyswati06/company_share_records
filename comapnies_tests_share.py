import csv
import random
import sys
import unittest
from datetime import datetime

from companies_share import CompanyHighestSharePrice

class TestHighestSharePrice(unittest.TestCase):
    """
    Unittests for the HighestSharePrice Class
    """

    EXPECTED = {'Company_0': {'month': 'Mar', 'price': 50, 'year': '1993'},
                'Company_1': {'month': 'Aug', 'price': 100, 'year': '1991'},
                'Company_2': {'month': 'Sep', 'price': 150, 'year': '1995'},
                'Company_3': {'month': 'Sep', 'price': 200, 'year': '1996'},
                'Company_4': {'month': 'Sep', 'price': 250, 'year': '1992'}}

    
    def setUp(self):
        self.no_companies = 5


    def test_success(self):
        """
        Test the Working of Module
        """      
        x = CompanyHighestSharePrice()
        hightest_price = x.get_highest_share_price()
        self.assert_company0(hightest_price)
        self.assert_company1(hightest_price)
        self.assert_company2(hightest_price)
        self.assert_company3(hightest_price)
        self.assert_company4(hightest_price)

    def assert_company0(self, hightest_price):
        """
        Test the company0
        """
        self.assertEqual(hightest_price['Company_0']['year'], self.EXPECTED['Company_0']['year'])
        self.assertEqual(hightest_price['Company_0']['month'], self.EXPECTED['Company_0']['month'])
        self.assertEqual(hightest_price['Company_0']['price'], self.EXPECTED['Company_0']['price'])

    def assert_company1(self, hightest_price):
        """
        Test the company1
        """
        self.assertEqual(hightest_price['Company_1']['year'], self.EXPECTED['Company_1']['year'])
        self.assertEqual(hightest_price['Company_1']['month'], self.EXPECTED['Company_1']['month'])
        self.assertEqual(hightest_price['Company_1']['price'], self.EXPECTED['Company_1']['price'])

    def assert_company2(self, hightest_price):
        """
        Test the company2
        """
        self.assertEqual(hightest_price['Company_2']['year'], self.EXPECTED['Company_2']['year'])
        self.assertEqual(hightest_price['Company_2']['month'], self.EXPECTED['Company_2']['month'])
        self.assertEqual(hightest_price['Company_2']['price'], self.EXPECTED['Company_2']['price'])

    def assert_company3(self, hightest_price):
        """
        Test the company3
        """
        self.assertEqual(hightest_price['Company_3']['year'], self.EXPECTED['Company_3']['year'])
        self.assertEqual(hightest_price['Company_3']['month'], self.EXPECTED['Company_3']['month'])
        self.assertEqual(hightest_price['Company_3']['price'], self.EXPECTED['Company_3']['price'])

    def assert_company4(self, hightest_price):
        """
        Test the company4
        """
        self.assertEqual(hightest_price['Company_4']['year'], self.EXPECTED['Company_4']['year'])
        self.assertEqual(hightest_price['Company_4']['month'], self.EXPECTED['Company_4']['month'])
        self.assertEqual(hightest_price['Company_4']['price'], self.EXPECTED['Company_4']['price'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHighestSharePrice)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit()
