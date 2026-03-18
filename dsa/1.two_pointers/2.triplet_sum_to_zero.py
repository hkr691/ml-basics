from typing import List

class TripletSum:
    def get_all_triplets(self, nums):
        triplets = []
        #sort nums since we can port over logic from pair_sum_sorted
        nums.sort()

        for i in range(len(nums)):
            #since target for get_all_pairs is positive, and numbers are sorted, exit loop on encountering first positive element
            if nums[i] > 0:
                break
            #avoid returning duplicate triplets
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            pairs = self.get_all_pairs(nums, i + 1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]] + pair)
        return triplets
    

    def get_all_pairs(self, nums, start, target):
        l, r = start, len(nums) - 1
        pairs = []
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == target:
                pairs.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l - 1] == nums[l]:
                    l += 1
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        return pairs

arr = [0,0,1,-1,1,-1]
triplet_sum = TripletSum()
print(triplet_sum.get_all_triplets(arr))