class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        start_at = -1
        for i in range(len(nums) - 1):
        # search other element in the array
            for j in range(i + 1, len(nums)):
            # if these two elemets sum to target, print the index
                if nums[i] + nums[j] == target:
                    
                        result1 = nums.index(nums[i], start_at+1)
                        result.append(result1)
                        start_at=result1
                        
                        result2 = nums.index(nums[j], start_at+1)
                        result.append(result2)
                        start_at = result2
                        
                    
                        return result