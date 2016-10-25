def solution(N):
    # Minimal number which has a binary gap is 5(101)
    if N < 5:
        return 0

    # Skip the tailing zero(s)
    while N > 0 and N % 2 == 0:
        N >>= 1

    max_binary_gap = 0
    gap_count = 0

    while N > 0:
        remainder = N % 2

        if remainder > 0:
            if gap_count > 0:
                max_binary_gap = max(gap_count, max_binary_gap)
                gap_count = 0
        else:
            gap_count += 1

        N >>= 1

    return max_binary_gap

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
