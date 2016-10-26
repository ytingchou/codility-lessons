# This solution is inspired by java solution 2 in
# http://www.programcreek.com/2013/02/twitter-codility-problem-max-binary-gap/

import math

def solution(N):
    # Save previous position of LSB
    pre = -1
    max_gap = 0

    while N > 0:
        # Find current LSB
        k = N & -N

        # Get current position of LSB
        curr = int(math.log(k, 2))

        # Remove current LSB
        N = N & (N - 1)

        if pre != -1 and (curr - pre) > max_gap:
            max_gap = curr - pre - 1

        pre = curr

    return max_gap

import unittest

class Tests(unittest.TestCase):
    def test_N_9(self):
        self.assertEqual(solution(9), 2)

    def test_N_15(self):
        self.assertEqual(solution(15), 0)

    def test_N_20(self):
        self.assertEqual(solution(20), 1)

    def test_N_529(self):
        self.assertEqual(solution(529), 4)

    def test_N_1041(self):
        self.assertEqual(solution(1041), 5)


if __name__ == '__main__':
    unittest.main()
