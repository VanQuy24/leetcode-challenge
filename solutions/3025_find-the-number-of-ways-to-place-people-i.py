"""
Title   : Find the Number of Ways to Place People I
Number  : 3025
Link    : https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
"""

from typing import List
import time


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        output = 0
        n = len(points)
        sorted_points = sorted(points, key=lambda x: (x[0], -x[1]))
        for i in range(n-1):
            for j in range(i+1, n):
                xa, ya = sorted_points[i]
                xb, yb = sorted_points[j]
                if ya < yb: continue
                for k in range(i+1, j):
                    xk, yk = sorted_points[k]
                    if ya >= yk >= yb:
                        break
                else:
                    output += 1

        return output


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[1,10],[2,9],[3,8],[4,7],[5,6],[6,5],[7,4],[8,3],[9,2],[10,1]], ), "expected": 9},
        {"input": ([[1,6],[1,2],[1,3],[1,4],[1,5],[2,5],[3,5],[4,5],[5,5]], ), "expected": 8},
        {"input": ([[25,25],[30,30],[35,35],[40,40],[45,45],[20,30],[15,35],[10,40],[5,45]], ), "expected": 8},
        {"input": ([[5,5],[10,10],[15,15],[20,20],[25,25],[6,24],[7,23],[8,22],[9,21]], ), "expected": 6},
        {"input": ([[50,50],[45,45],[40,40],[35,35],[30,30],[25,25],[20,20],[15,15],[10,10],[5,5]], ), "expected": 0},
        {"input": ([[1,25],[2,20],[3,15],[4,10],[5,5],[6,4],[7,3],[8,2],[9,1],[10,0]], ), "expected": 9},
        {"input": ([[10,40],[20,35],[30,30],[40,25],[15,20],[25,15],[35,10],[45,5]], ), "expected": 10},
        {"input": ([[1,1],[50,50],[25,25],[40,40],[10,10],[30,20],[20,30],[45,10],[10,45],[50,5]], ), "expected": 10},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.numberOfPairs(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.018 ms
Test 2: PASSED in 0.020 ms
Test 3: PASSED in 0.014 ms
Test 4: PASSED in 0.011 ms
Test 5: PASSED in 0.008 ms
Test 6: PASSED in 0.016 ms
Test 7: PASSED in 0.012 ms
Test 8: PASSED in 0.014 ms
"""