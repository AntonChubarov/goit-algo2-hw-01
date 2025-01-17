import unittest

from min_max import find_min_max, find_kth_min


class TestMinMaxAlgorithms(unittest.TestCase):

    def test_find_min_max(self):
        test_cases = [
            ([3, 1, 4, 1, 5, 9], (1, 9)),
            ([10, 20, 30], (10, 30)),
            ([5], (5, 5)),
            ([100, -1, 0, 50], (-1, 100)),
            ([-5, -10, -1], (-10, -1)),
            ([], ValueError)
        ]
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                if isinstance(expected, tuple):
                    self.assertEqual(find_min_max(arr), expected)
                else:
                    with self.assertRaises(expected):
                        find_min_max(arr)

    def test_find_kth_min(self):
        test_cases = [
            ([3, 1, 4, 1, 5, 9], 1, 1),
            ([], 1, ValueError),
            ([3, 1, 4, 1, 5, 9], 3, 3),
            ([10, 20, 30], 2, 20),
            ([5], 1, 5),
            ([5], 2, IndexError),
            ([100, -1, 0, 50], 4, 100),
            ([100, -1, 0, 50], 5, IndexError),
            ([-5, -10, -1], 2, -5)
        ]
        for arr, k, expected in test_cases:
            with self.subTest(arr=arr, k=k):
                if isinstance(expected, int):
                    self.assertEqual(find_kth_min(arr, k), expected)
                else:
                    with self.assertRaises(expected):
                        find_kth_min(arr, k)


if __name__ == "__main__":
    unittest.main()
