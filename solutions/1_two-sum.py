"""
Title   : Two Sum
Number  : 1
Link    : https://leetcode.com/problems/two-sum/
"""

from typing import List
import time
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = defaultdict(list)
        n = len(nums)

        for i in range(n):
            mem[nums[i]].append(i)
        
        for i in mem.keys():
            if target - i not in mem:
                continue
            if target == i*2:
                if len(mem[target-i]) > 1:
                    return mem[target-i][:2]
            elif len(mem[target-i]) > 0:
                return [mem[i][0], mem[target-i][0]]


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
        {"input": ([3, 2, 4], 6), "expected": [1, 2]},
        {"input": ([3, 3], 6), "expected": [0, 1]},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.twoSum(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")
