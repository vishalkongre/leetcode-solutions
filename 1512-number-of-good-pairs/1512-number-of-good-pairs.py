class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs = []
        current_num = 0 
        for i_index, i_num in enumerate(nums):
            current_num = i_num 
            for j_index in range(i_index+1, len(nums)):
                if i_index != j_index:
                    if i_num == nums[j_index]:
                        good_pairs.append((i_index, j_index))
        print(good_pairs)
        return len(good_pairs)



        