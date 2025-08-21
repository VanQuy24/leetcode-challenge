"""
Title   : Count Submatrices With All Ones
Number  : 1504
Link    : https://leetcode.com/problems/count-submatrices-with-all-ones/
"""

from typing import List
import time


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [0] * n
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            
            # Count submatrices ending at this row
            for j in range(n):
                min_height = height[j]
                for k in range(j, -1, -1):
                    if height[k] == 0:
                        break
                    min_height = min(min_height, height[k])
                    ans += min_height
                    
        return ans


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[1,0,1],[1,1,0],[1,1,0]],), "expected": 13},
        {"input": ([[0,1,1,0],[0,1,1,1],[1,1,1,0]],), "expected": 24},

    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.numSubmat(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")
