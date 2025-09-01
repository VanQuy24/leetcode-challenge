"""
Title   : Maximum Average Pass Ratio
Number  : 1792
Link    : https://leetcode.com/problems/maximum-average-pass-ratio/
"""

from typing import List
from heapq import heappush, heappop
import time


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        mem = []
        for p, t in classes:
            r = p/t
            rn = (p+1)/(t+1)
            heappush(mem, (r-rn, t, r))
        
        for _ in range(extraStudents):
            c, t, r = heappop(mem)
            rn = r - c
            heappush(mem, (rn-(r*t+2)/(t+2), t+1, rn))
        
        return sum([x[2] for x in mem]) / len(mem)


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[1,2],[3,5],[2,2]], 2), "expected": 0.78333},
        {"input": ([[2,4],[3,9],[4,5],[2,10]], 4), "expected": 0.53485},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.maxAverageRatio(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if round(result, 5) == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.011 ms
Test 2: PASSED in 0.012 ms
"""