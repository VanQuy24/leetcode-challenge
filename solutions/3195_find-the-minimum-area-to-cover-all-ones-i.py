"""
Title   : Find the Minimum Area to Cover All Ones I
Number  : 3195
Link    : https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
"""

from typing import List
import time


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        xs, xe = 0, len(grid[0])-1
        ys, ye = 0, len(grid)-1

        while ys < ye:
            if sum(grid[ys]) == 0:
                ys += 1
            else:
                break
        
        while ys < ye:
            if sum(grid[ye]) == 0:
                ye -= 1
            else:
                break

        while xs < xe:
            if sum([grid[i][xs] for i in range(ys, ye+1)]) == 0:
                xs += 1
            else:
                break

        while xs < xe:
            if sum([grid[i][xe] for i in range(ys, ye+1)]) == 0:
                xe -= 1
            else:
                break

        return (xe - xs + 1) * (ye - ys + 1)


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[0,1,0],[1,0,1]], ), "expected": 6},
        {"input": ([[1,0],[0,0]], ), "expected": 1},
        {"input": ([[0,1,0,0],[1,0,1,0],[0,0,0,0],[1,0,0,1]], ), "expected": 16},
        {"input": ([[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]], ), "expected": 16},
        {"input": ([[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]], ), "expected": 9},
        {"input": ([[1,0,0],[0,0,0],[0,0,1]], ), "expected": 9},
        {"input": ([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]], ), "expected": 1},
        {"input": ([[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]], ), "expected": 25},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.minimumArea(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.007 ms
Test 2: PASSED in 0.005 ms
Test 3: PASSED in 0.003 ms
Test 4: PASSED in 0.002 ms
Test 5: PASSED in 0.003 ms
Test 6: PASSED in 0.001 ms
Test 7: PASSED in 0.003 ms
Test 8: PASSED in 0.002 ms
"""