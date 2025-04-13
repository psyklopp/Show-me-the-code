'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,num in enumerate(nums):
            if target - num in nums_dict:
                return [i, nums_dict[target - num]]
            nums_dict[num] = i        