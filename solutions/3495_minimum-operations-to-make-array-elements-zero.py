"""
Title   : Minimum Operations to Make Array Elements Zero
Number  : 3495
Link    : https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
"""

from typing import List
import time


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        expSum4=[1]+[0]*17
        def expSum(x):
            if x==0: return 0
            log4=(x.bit_length()-1)>>1
            r=x-(1<<(log4<<1))
            return expSum4[log4]+r*(log4+1)
        for i in range(1,18):
            expSum4[i]=expSum4[i-1]+3*i*(1<<(2*(i-1)))+1
        op=0
        for l1, r in queries:
            op+=(expSum(r)-expSum(l1-1)+1)>>1

        return op


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([[1,2],[2,4]],), "expected": 3},
        {"input": ([[2,6]],), "expected": 4},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.minOperations(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.014 ms
Test 2: PASSED in 0.012 ms
"""