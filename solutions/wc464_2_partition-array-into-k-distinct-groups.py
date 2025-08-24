"""
Weekly Contest 464
Title   : Q2. Partition Array Into K-Distinct Groups
Link    : https://leetcode.com/contest/weekly-contest-464/problems/partition-array-into-k-distinct-groups/
"""

from typing import List
from collections import defaultdict
import time


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        min = len(nums)//k
            
        mem = defaultdict(int)
        for num in nums:
            mem[num] += 1
            if mem[num] > min:
                return False
        return True



if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([1,2,3,4], 2), "expected": True},
        {"input": ([3,5,2,2], 2), "expected": True},
        {"input": ([1,5,2,3], 3), "expected": False},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.partitionArray(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")


"""
Test 1: PASSED in 0.007 ms
Test 2: PASSED in 0.007 ms
Test 3: PASSED in 0.002 ms
"""