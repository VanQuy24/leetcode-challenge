"""
Title   : Sort Matrix by Diagonals
Number  : 3446
Link    : https://leetcode.com/problems/sort-matrix-by-diagonals/
"""

from typing import List
import time


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        i, j = 0, n-1
        while j > 1:
            j -= 1
            tmp = sorted([grid[i+x][j+x] for x in range(0,n-j)])
            for x in range(0,n-j):
                grid[i+x][j+x] = tmp[x]
        
        i, j = 0, 0
        while i < n-1:
            tmp = sorted([grid[i+x][j+x] for x in range(0,n-i)], reverse=True)
            for x in range(0,n-i):
                grid[i+x][j+x] = tmp[x]

            i += 1

        return grid


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[2,4,1],[7,5,9],[3,8,6]], ), "expected": [[6,4,1],[8,5,9],[3,7,2]]},
        {"input": ([[10,3,6,1],[4,7,2,5],[9,8,12,11],[13,14,0,15]], ), "expected": [[15,2,5,1],[8,12,3,6],[14,4,10,11],[13,9,0,7]]},
        {"input": ([[5,1,8],[6,7,2],[3,9,4]], ), "expected": [[7,1,8],[9,5,2],[3,6,4]]},
        {"input": ([[11,2,9,5],[6,12,1,3],[4,8,7,10],[0,13,14,15]], ), "expected": [[15,1,3,5],[14,12,2,9],[13,8,11,10],[0,4,6,7]]},
        {"input": ([[3,7,2],[8,4,6],[1,9,5]], ), "expected": [[5,6,2],[9,4,7],[1,8,3]]},
        {"input": ([[9,1,4,7],[2,5,3,6],[8,0,10,11],[12,13,14,15]], ), "expected": [[15,1,4,7],[14,10,3,6],[13,2,9,11],[12,8,0,5]]},
        {"input": ([[6,2,9],[5,7,1],[4,3,8]], ), "expected": [[8,1,9],[5,7,2],[4,3,6]]},
        {"input": ([[10,5,3,8],[2,7,6,1],[4,9,0,11],[12,13,14,15]], ), "expected": [[15,5,1,8],[14,10,6,3],[13,9,7,11],[12,4,2,0]]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.sortMatrix(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.014 ms
Test 2: PASSED in 0.013 ms
Test 3: PASSED in 0.007 ms
Test 4: PASSED in 0.007 ms
Test 5: PASSED in 0.005 ms
Test 6: PASSED in 0.007 ms
Test 7: PASSED in 0.005 ms
Test 8: PASSED in 0.007 ms
"""