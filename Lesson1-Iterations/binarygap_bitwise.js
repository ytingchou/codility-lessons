function solution(N) {
    // Save previous position of LSB
    var pre = -1;
    var max_gap = 0;

    while (N > 0) {
        // Find current LSB
        k = N & -N;

        // Get position of current LSB
        curr = Math.log2(k);

        // Remove current LSB
        N = N & (N - 1);

        if ((pre != -1) && ((curr - pre) > max_gap)) {
            max_gap = curr - pre - 1;
        }

        pre = curr;
    }

    return max_gap;
}

const assert = require('assert');

assert.equal(solution(9), 2, "max binary gap of 9 is 2");
assert.equal(solution(15), 0, "max binary gap of 15 is 0");
assert.equal(solution(20), 1, "max binary gap of 20 is 1");
assert.equal(solution(529), 4, "max binary gap of 529 is 4");
assert.equal(solution(1041), 5, "max binary gap of 1041 is 5");
