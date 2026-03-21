from typing import List

class Pair_sum_sorted:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # since nums is sorted array, take advantage and use 2 pointers, initialized at beginning and end of array
        l, r = 0, len(nums) - 1
        while l < r:
            # if nums at indices l and r equal target, return l, r indices
            if nums[l] + nums[r] == target:
                return [l, r]
            # if sum of nums at l and r > tgt, look for a smaller value of num at r
            elif nums[l] + nums[r] > target:
                r -= 1
            #only other condition is tgt < sum of nums at l & r, so advance left pointer to get get higher sum
            else:
                l += 1
        return [-1, -1]

"""
time: one pass -> O(n)
space: no additional space for o/p - O(1)
"""

pair_sum = Pair_sum_sorted()
arr, tgt = [1,2,3,4,5], 5

print(pair_sum.two_sum(arr, tgt))

