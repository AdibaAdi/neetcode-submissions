class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #hashset to store the index and num
       seen={}
       #enumerate the num list with index and num
       for i,n in enumerate(nums):
       #compare the target and num with their compliment
            compliment=target-n
            #check if the compliment num exist in the hashset
            #if it does return the index of that and num as res array
            if compliment in seen:
                return [seen[compliment], i]
            #if num not in hashset add to hashset
            seen[n]=i