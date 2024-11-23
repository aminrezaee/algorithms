"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        skip_count = 0
        last_number = nums[0]
        counter = 0
        for i in range(len(nums)):
            if nums[i] == last_number:
                counter += 1
            else:
                counter = 1
                last_number = nums[i]
            if counter > 2:
                skip_count += 1
            if skip_count > 0:
                nums[int(i-skip_count)] = nums[i]
        return int(i - skip_count + 1)




        