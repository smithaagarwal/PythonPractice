"""""
Leet Code
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""""
from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, x in enumerate(nums):
            for index2, y in enumerate(nums):
                if index1 != index2:
                    if y == (target - x):
                        result.append(index1)
                        result.append(index2)
                        return result


nums = [2, 7, 11, 15]
target = 26
s = Solution()
result = s.twoSum(nums, target)
print(result)
