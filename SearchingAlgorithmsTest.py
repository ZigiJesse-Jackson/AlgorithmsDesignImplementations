import unittest
import numpy as np
from SequentialSearch import sequentialsearch
from utility import list_generator

class SearchingTests(unittest.TestCase):

    def test_search(self):
        testlist = list_generator(250)
        randIndex = np.random.randint(low=0, high=250)

        key = testlist[randIndex]
        keyIndex = sequentialsearch(testlist, key)

        self.assertEqual(keyIndex, randIndex)

def searching_algorithm_tests():
    suite = unittest.TestSuite()
    suite.addTest(SearchingTests('test_search'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(searching_algorithm_tests())