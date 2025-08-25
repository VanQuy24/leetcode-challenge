"""
Title   : Diagonal Traverse
Number  : 498
Link    : https://leetcode.com/problems/diagonal-traverse/
"""

from typing import List
import time


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        d = -1
        output = [None] * (m*n)
        idx = 0
        for i in range(m+n-1):
            if d+1:
                e = min(i+1, m)
                s = max(0, i-n+1)
            else:
                s = min(i, m-1)
                e = max(-1, i-n)

            for x in range(s, e, d):
                output[idx] = mat[x][i-x]
                idx += 1
            d *= -1
        
        return output


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[5, -3, 17, 99, -42]], ), "expected": [5, -3, 17, 99, -42]},
        {"input": ([[-7], [14], [0], [88], [-65]], ), "expected": [-7,14,0,88,-65]},
        {"input": ([[1, 2], [3, 4]], ), "expected": [1,2,3,4]},
        {"input": ([[10, -20, 30], [-40, 50, -60]], ), "expected": [10,-20,-40,50,30,-60]},
        {"input": ([[1, -2, 3, -4], [5, -6, 7, -8], [9, -10, 11, -12], [13, -14, 15, -16]], ), "expected": [1,-2,5,9,-6,3,-4,7,-10,13,-14,11,-8,-12,15,-16]},
        {"input": ([[7, 8, -9], [10, -11, 12], [-13, 14, -15], [16, 17, -18], [19, -20, 21]], ), "expected": [7,8,10,-13,-11,-9,12,14,16,19,17,-15,-18,-20,21]},
        {"input": ([[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]], ), "expected": [1,-1,2,3,-2,-3,4,5,-4,-5,6,7,-6,-7,8,-8]},
        {"input": ([[12, -45, 33, 87, -29, 54, -76, 0, 91, -8], [77, 25, -11, 64, -30, 18, -55, 84, -99, 100], [-4, 38, 59, -97, 12, -66, 71, -3, 45, -12], [90, -81, 23, -5, 62, -44, 36, 79, -72, 27], [56, 31, -64, 17, -90, 11, 8, -15, 99, -100], [3, -7, 41, -92, 53, -25, 66, 74, -34, 82], [61, -13, 15, -41, 87, -69, 19, 32, -53, 9], [-99, 100, -88, 77, -55, 42, -36, 25, -20, 11], [44, -11, 33, -22, 66, -77, 55, -99, 88, -66], [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]], ), "expected": [12,-45,77,-4,25,33,87,-11,38,90,56,-81,59,64,-29,54,-30,-97,23,31,3,61,-7,-64,-5,12,18,-76,0,-55,-66,62,17,41,-13,-99,44,100,15,-92,-90,-44,71,84,91,-8,-99,-3,36,11,53,-41,-88,-11,1,2,33,77,87,-25,8,79,45,100,-12,-72,-15,66,-69,-55,-22,-3,4,66,42,19,74,99,27,-100,-34,32,-36,-77,-5,6,55,25,-53,82,9,-20,-99,-7,8,88,11,-66,-9,10]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.findDiagonalOrder(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.011 ms
Test 2: PASSED in 0.012 ms
Test 3: PASSED in 0.006 ms
Test 4: PASSED in 0.006 ms
Test 5: PASSED in 0.010 ms
Test 6: PASSED in 0.010 ms
Test 7: PASSED in 0.012 ms
Test 8: PASSED in 0.030 ms
"""