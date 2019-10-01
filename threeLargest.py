# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
# O(n) time | O(1) space

import unittest

# Add, edit, or remove tests in this file.
# Treat it as your playground!
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]

class TestProgram(unittest.TestCase):



    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers(
            [55, 7, 8]), [7, 8, 55])

    def test_case_2(self):
        self.assertEqual(findThreeLargestNumbers(
            [55, 43, 11, 3, -3, 10]), [11, 43, 55])

    def test_case_3(self):
        self.assertEqual(findThreeLargestNumbers(
            [7, 8, 3, 11, 43, 55]), [11, 43, 55])

    def test_case_4(self):
        self.assertEqual(findThreeLargestNumbers(
            [55, 7, 8, 3, 43, 11]), [11, 43, 55])

    def test_case_5(self):
        self.assertEqual(findThreeLargestNumbers(
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]), [7, 7, 7])

    def test_case_6(self):
        self.assertEqual(findThreeLargestNumbers(
            [7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]), [7, 7, 8])

    def test_case_7(self):
        self.assertEqual(findThreeLargestNumbers(
            [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_case_8(self):
        self.assertEqual(findThreeLargestNumbers(
            [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]), [-2, -1, 7])




if __name__ == "__main__":
    unittest.main()
