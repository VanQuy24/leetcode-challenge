"""
Weekly Contest 464
Title   : Q1. GCD of Odd and Even Sums
Link    : https://leetcode.com/contest/weekly-contest-464/problems/gcd-of-odd-and-even-sums/description/
"""

from typing import List
import time


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n



if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": (4, ), "expected": 4},
        {"input": (5, ), "expected": 5},
        
        
        
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.gcdOfOddEvenSums(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")


"""
Test 1: PASSED in 0.001 ms
Test 2: PASSED in 0.002 ms
"""