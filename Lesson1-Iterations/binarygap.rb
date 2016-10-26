def solution(n)
    # Minimal number which has a binary gap is 5(101
    if n < 5
        return 0
    end

    # Skip the trailing zero(s)
    until n == 0 || n % 2 == 1 do
        n >>= 1
    end

    max_binary_gap = 0
    gap_count = 0

    until n == 0 do
        remainder = n % 2

        if remainder > 0
            if gap_count > 0
                max_binary_gap = [gap_count, max_binary_gap].max
                gap_count = 0
            end
        else
            gap_count += 1
        end

        n >>= 1
    end

    return max_binary_gap
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
