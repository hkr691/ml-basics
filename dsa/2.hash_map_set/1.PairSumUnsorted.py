class PairSumUnsorted:
    def get_pair(self, nums, target):
        hash_map = {}
        #constraint is nums in arr are unique so use num as key and it's index as value
        for idx, num in enumerate(nums):
            if (target - num) in hash_map:
                return [hash_map[target - num], idx]
            hash_map[num] = idx
        return [-1, -1]

array = [-1, 3, 4, 2]
target = 3
pair_sum = PairSumUnsorted()
print(pair_sum.get_pair(array, target))