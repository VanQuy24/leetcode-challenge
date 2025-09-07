"""
Title   : Find N Unique Integers Sum up to Zero
Number  : 1304
Link    : https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""

from typing import List
import time


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0]*n
        i = 0
        for x in range(1, n//2+1):
            result[i] = x
            i += 1
            result[-i] = -x

        return result


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": (1, ), "expected": [0]},
        {"input": (2, ), "expected": [1, -1]},
        {"input": (3, ), "expected": [1,  0, -1]},
        {"input": (4, ), "expected": [1, 2, -2, -1]},
        {"input": (5, ), "expected": [1, 2, 0, -2, -1]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.sumZero(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")
