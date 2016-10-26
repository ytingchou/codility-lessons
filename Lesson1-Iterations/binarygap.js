function solution(N) {
    // Minimal number which has a binary gap is 5(101
    if (N < 5) {
        return 0;
    }

    // Skip the trailing zero(s)
    while ((N > 0) && ((N % 2) == 0)) {
        N >>= 1;
    }

    max_binary_gap = 0;
    gap_count = 0;

    while (N > 0) {
        remainder = N % 2;

        if (remainder > 0) {
            if (gap_count > 0) {
                max_binary_gap = Math.max(gap_count, max_binary_gap);
                gap_count = 0;
            }
        } else {
            gap_count += 1;
        }

        N >>= 1;
    }

    return max_binary_gap;
}

const assert = require('assert');

assert.equal(solution(9), 2, "max binary gap of 9 is 2");
assert.equal(solution(15), 0, "max binary gap of 15 is 0");
assert.equal(solution(20), 1, "max binary gap of 20 is 1");
assert.equal(solution(529), 4, "max binary gap of 529 is 4");
assert.equal(solution(1041), 5, "max binary gap of 1041 is 5");
