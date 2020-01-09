
# coding: utf-8

# In[ ]:


class Solution(object):
    def sortArray(self, nums):
        if len(nums) < 1:
            return nums
        for i in range(1,len(nums)):
            j = i
            while j > 0:
                if nums[j] < nums[j-1]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
                    j -= 1
                else:
                    break
        return nums

