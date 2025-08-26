"""
Title   : Maximum Area of Longest Diagonal Rectangle
Number  : 3000
Link    : https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
"""

import time
from math import sqrt
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mem = [0, 0]
        for w, h in dimensions:
            diagonal = sqrt(w*w + h*h)
            if diagonal > mem[0] or (diagonal == mem[0] and  w * h > mem[1]):
                mem = [diagonal, w * h]

        return mem[1]


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[9,3],[8,6]], ), "expected": 48},
        {"input": ([[3,4],[4,3]], ), "expected": 12},
        {"input": ([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]], ), "expected": 20},
        {"input": ([[4,7],[8,9],[5,3],[6,10],[2,9],[3,10],[2,2],[5,8],[5,10],[5,6],[8,9],[10,7],[8,9],[3,7],[2,6],[5,1],[7,4],[1,10],[1,7],[6,9],[3,3],[4,6],[8,2],[10,6],[7,9],[9,2],[1,2],[3,8],[10,2],[4,1],[9,7],[10,3],[6,9],[9,8],[7,7],[5,7],[5,4],[6,5],[1,8],[2,3],[7,10],[3,9],[5,7],[2,4],[5,6],[9,5],[8,8],[8,10],[6,8],[5,1],[10,8],[7,4],[2,1],[2,7],[10,3],[2,5],[7,6],[10,5],[10,9],[5,7],[10,6],[4,3],[10,4],[1,5],[8,9],[3,1],[2,5],[9,10],[6,6],[5,10],[10,2],[6,10],[1,1],[8,6],[1,7],[6,3],[9,3],[1,4],[1,1],[10,4],[7,9],[4,5],[2,8],[7,9],[7,3],[4,9],[2,8],[4,6],[9,1],[8,4],[2,4],[7,8],[3,5],[7,6],[8,6],[4,7],[25,60],[39,52],[16,63],[33,56]], ), "expected": 2028},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.areaOfMaxDiagonal(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.006 ms
Test 2: PASSED in 0.003 ms
Test 3: PASSED in 0.002 ms
Test 4: PASSED in 0.015 ms
"""