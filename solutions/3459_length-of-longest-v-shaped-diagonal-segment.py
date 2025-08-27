"""
Title   : Length of Longest V-Shaped Diagonal Segment
Number  : 3459
Link    : https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
"""

from typing import List
import time
import functools

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Dynamic Programming
        # Let dp(x, y, t, d) be the longest segment starting with (x, y) where the segment has been turned or not (indicated by the binary flag t) and the current direction is d.
        # When grid(x, y) == 1:
        # dp(x, y, t, *) = max(dp(x', y', true, d) if grid(x', y') == 2, 1)
        # Otherwise:
        # dp(x, y, t, d) = max(dp(x', y', t, d) if grid(x',y') == 2 - grid(x, y) else 1, dp(x'', y'', false, d') if d is true and grid(x'',y'') == 2 - grid(x, y))
        # The overall complexity is O(m * n * 4 * 2) ~ O(2 * 10^6).
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)
        m = len(grid[0])
        nv = [2, 2, 0] # Next expected value

        @functools.cache
        def helper(x, y, turned, dir):
            # First, we do not change the direction
            res = 1
            dx, dy = dirs[dir]
            if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                res = helper(x + dirs[dir][0], y + dirs[dir][1], turned, dir) + 1
            if not turned:
                dx, dy = dirs[(dir + 1) % 4]
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                    res = max(res, helper(x + dx, y + dy, True, (dir + 1) % 4) + 1)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Optimization: we can compute the theorically longest path. If the current answer is already better than this, we do not need to make the DFS.
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > ans:
                            ans = max(ans, helper(i, j, False, d))
        return ans


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[2,1,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,0,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,0,2],[2,2,2,2,2,2,2],[2,2,2,0,2,2,2]], ), "expected": 7},
        {"input": ([[0],[1],[2],[0],[1],[2],[0],[1],[0],[2]], ), "expected": 1},
        {"input": ([[2,2,2,2,2,2,2,2,2,2],[2,1,2,2,2,2,2,2,2,2],[2,2,2,0,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,0,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,0,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,2,2,0,2,2,2,2,2,2]], ), "expected": 2},
        {"input": ([[2,2,2,2,2,2,2,2,1,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,0,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,0,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,0,2,0,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,1,2,2,2,2,2,2,2,2,2,2]], ), "expected": 6},
        {"input": ([[2,2,2,2,2,2,2,2,1,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,0,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,0,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,0,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,0,2,0,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2],[2,1,2,2,2,2,2,2,2,2,2,2]], ), "expected": 6},
        {"input": ([[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[1,2,0,2,0,2,0,2]], ), "expected": 3},
        {"input": ([[1,2,0,2,0,2,0,2,0,2,0,2,0,2,0],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]], ), "expected": 2},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.lenOfVDiagonal(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.032 ms
Test 2: PASSED in 0.027 ms
Test 3: PASSED in 0.034 ms
Test 4: PASSED in 0.058 ms
Test 5: PASSED in 0.057 ms
Test 6: PASSED in 0.028 ms
Test 7: PASSED in 0.041 ms
"""