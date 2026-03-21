class LargestConainer:
    def most_water(self, nums):
        #2 pointers - area would be min on heights * width of container
        l, r = 0, len(nums) - 1 #start with max width of container
        max_water = 0
        while l < r:
            water = min(nums[r], nums[l]) * (r - l)
            max_water = max(max_water, water)
            #left "hindering" the most water level
            if nums[l] < nums[r]:
                l += 1
            #if right is "hindering"
            elif nums[l] > nums[r]:
                r -= 1
            #same heights at left and right pointer
            else:
                l += 1
                r -= 1
        return max_water

largest = LargestConainer()
heights = [2, 7, 8, 3, 7, 6]
print(largest.most_water(heights))