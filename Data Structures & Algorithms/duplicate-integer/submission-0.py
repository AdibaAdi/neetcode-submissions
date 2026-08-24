class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a seen hashset
        seen={}
        #add the nums to the hashset
        for i in range(len(nums)):
            if nums[i] in seen:
                #if in seen hashset return true
                return True
            else:
                #add to the hashset with index as key-val
                seen[nums[i]]=i
        return False