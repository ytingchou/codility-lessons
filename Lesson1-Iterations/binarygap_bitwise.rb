# This solution is inspired by java solution 2 in
# http://www.programcreek.com/2013/02/twitter-codility-problem-max-binary-gap/

def solution(n)
    # Save previous position of LSB
    pre = -1
    max_gap = 0

    while n > 0 do
        # Find current LSB
        k = n & -n

        # Get current position of LSB
        curr = Math.log2(k)

        # Remove current LSB
        n = n & (n - 1)

        if pre != -1 and (curr - pre) > max_gap
            max_gap = curr - pre - 1
        end

        pre = curr
    end

    return max_gap
end

require 'minitest/autorun'

class Tests < Minitest::Test
    def test_n_9
        assert_equal 2, solution(9)
    end

    def test_n_15
        assert_equal 0, solution(15)
    end

    def test_n_20
        assert_equal 1, solution(20)
    end

    def test_n_529
        assert_equal 4, solution(529)
    end

    def test_n_1041
        assert_equal 5, solution(1041)
    end
end
