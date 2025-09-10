"""
Title   : Minimum Number of People to Teach
Number  : 1733
Link    : https://leetcode.com/problems/minimum-number-of-people-to-teach/
"""

from typing import List
import time


class Solution:
    def solve(self, *args, **kwargs):
        # TODO: implement solution
        pass


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        # Example:
        # {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.solve(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")
