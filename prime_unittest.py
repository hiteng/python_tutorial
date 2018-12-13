

import unittest
import prime_test

class PrimeTestCase(unittest.TestCase):

    def test_prime_check(self):
        result = prime_test.prime_check(13)
        self.assertTrue(result, True)


if __name__ == '__main__':

    unittest.main()

