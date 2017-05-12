"""
    Merge Sort
"""
import unittest


def merge_sort(array, verbose=False):
    if len(array) <= 1:
        return array
    mid_index = len(array) // 2
    left_array = merge_sort(array[:mid_index])
    right_array = merge_sort(array[mid_index:])
    if verbose: print('Divided', left_array, right_array)

    return merge(left_array, right_array, verbose)

def merge(left_array, right_array, verbose=False):
    array = []
    i = 0
    j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array.append(left_array[i])
            i+=1
        else:
            array.append(right_array[j])
            j+=1
    array += left_array[i:]
    array += right_array[j:]
    if verbose: print('Merged', array)
    return array


class TestMergeSort(unittest.TestCase):

    def test_empty(self):
        array = []
        self._test_merge_sort(array)

    def test_one(self):
        array = [1]
        self._test_merge_sort(array)

    def test_two(self):
        array = [0, -1]
        self._test_merge_sort(array)

    def test_even(self):
        array = [1,2,5,6,4,304,6,54,33,1,1,3,8,9,0,0]
        self._test_merge_sort(array)

    def test_odd(self):
        array = [1,2,5,6,4,304,6,54,33,1,1,3,1111,8,9,0,0]
        self._test_merge_sort(array)

    def _test_merge_sort(self, array):
        sorted_array_using_merge_sort = merge_sort(array)
        using_py_sort = sorted(array)
        assert sorted_array_using_merge_sort == using_py_sort


if __name__ == '__main__':
    unittest.main()
