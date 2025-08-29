"""
Title   : Alice and Bob Playing Flower Game
Number  : 3021
Link    : https://leetcode.com/problems/alice-and-bob-playing-flower-game/
"""

from typing import List
import time


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_x = (n + 1) // 2
        even_x = n // 2
        odd_y = (m + 1) // 2
        even_y = m // 2
        return odd_x * even_y + even_x * odd_y


if __name__ == "__main__":
    s = Solution()

    # Add your test cases here
    # Each test case is {"input": (...args...), "expected": ...}
    tests = [
        {"input": (1, 4), "expected": 2},
        {"input": (4, 3), "expected": 6},
        {"input": (12312, 3), "expected": 18468},
        {"input": (42, 24444), "expected": 513324},
        {"input": (93116, 25827), "expected": 1202453466},
        {"input": (34376, 92317), "expected": 1586744596},
        {"input": (75582, 9773), "expected": 369331443},
        {"input": (69561, 64626), "expected": 2247724593},
    ]

    for idx, t in enumerate(tests, 1):
        start = time.perf_counter()
        result = s.flowerGame(*t["input"])
        end = time.perf_counter()
        runtime = (end - start) * 1000  # ms

        if result == t["expected"]:
            print(f"Test {idx}: PASSED in {runtime:.3f} ms")
        else:
            print(f"Test {idx}: FAILED in {runtime:.3f} ms "
                  f"(expected {t['expected']}, got {result})")

"""
Test 1: PASSED in 0.002 ms
Test 2: PASSED in 0.003 ms
Test 3: PASSED in 0.003 ms
Test 4: PASSED in 0.002 ms
Test 5: PASSED in 0.002 ms
Test 6: PASSED in 0.001 ms
Test 7: PASSED in 0.001 ms
Test 8: PASSED in 0.001 ms
"""