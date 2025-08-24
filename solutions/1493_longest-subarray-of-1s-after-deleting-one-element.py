"""
Title   : Longest Subarray of 1s After Deleting One Element
Number  : 1493
Link    : https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""

from typing import List
import time


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        output = 0
        have_zero = False
        pre = 0
        curr = 0

        for i in nums:
            if i == 1:
                curr += 1
            else:
                have_zero = True
                if pre + curr > output:
                    output = pre + curr
                pre = curr
                curr = 0
        
        if pre + curr > output:
            output = pre + curr
        
        return output if have_zero else output - 1



if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": ([1,1,0,1], ), "expected": 3},
        {"input": ([0,1,1,1,0,1,1,0,1], ), "expected": 5},
        {"input": ([1,1,1], ), "expected": 2},
        
        
        
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.longestSubarray(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")


"""
Test 1: PASSED in 0.003 ms
Test 2: PASSED in 0.003 ms
Test 3: PASSED in 0.002 ms
"""