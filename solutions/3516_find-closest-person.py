"""
Title   : Find Closest Person
Number  : 3516
Link    : https://leetcode.com/problems/find-closest-person/
"""

from typing import List
import time


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        res = abs(x-z) - abs(y-z)
        if res == 0: return 0
        return 1 if res < 0 else 2


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": (1, 2, 3, ), "expected": 2},
        {"input": (1, 3, 2, ), "expected": 0},
        {"input": (2, 1, 3, ), "expected": 1},
        {"input": (3, 1, 2, ), "expected": 0},
        {"input": (2, 3, 1, ), "expected": 1},
        {"input": (3, 2, 1, ), "expected": 2},
        {"input": (1, 50, 20, ), "expected": 1},
        {"input": (5,  1, 20, ), "expected": 1},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.findClosest(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.002 ms
Test 2: PASSED in 0.003 ms
Test 3: PASSED in 0.002 ms
Test 4: PASSED in 0.001 ms
Test 5: PASSED in 0.001 ms
Test 6: PASSED in 0.001 ms
Test 7: PASSED in 0.002 ms
Test 8: PASSED in 0.001 ms
"""