import unittest
from SelectionSort import selectionsort
from ListGenerator import ListGenerator
from BubbleSort import bubblesort

class SortingTests(unittest.TestCase):


    def test_selection_sort(self):
        testList = ListGenerator(200)
        sortedTestList = selectionsort(testList)
        for i in range(0, 199):
            if not self.assertLessEqual(sortedTestList[i], sortedTestList[i + 1]):
                return False
        return True


    def test_selection_sort_Error(self):
        testList = []
        with self.assertRaises(Warning, msg='Function cannot be performed on an empty list'):
            selectionsort(testList)


    def test_bubble_sort(self):
        testList = ListGenerator(200)
        sortedTestList = bubblesort(testList)
        for i in range(0, 199):
            if not self.assertLessEqual(sortedTestList[i], sortedTestList[i + 1]):
                return False
        return True

    def test_bubble_sort_Error(self):
        testList = []
        with self.assertRaises(Warning, msg='Function cannot be performed on an empty list'):
            bubblesort(testList)

def sorting_algorithms_test():
    suite = unittest.TestSuite()
    suite.addTest(SortingTests('test_selection_sort'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(sorting_algorithms_test())
