"""
Title   : Minimum Operations to Make the Integer Zero
Number  : 2749
Link    : https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
"""

from typing import List
import time


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
        return -1


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": (3, -2), "expected": 3},
        {"input": (5, 7), "expected": -1},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.makeTheIntegerZero(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.005 ms
Test 2: PASSED in 0.003 ms
"""