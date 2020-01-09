
# coding: utf-8

# In[ ]:


class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                rep = nums[i]
                break
        total = 0
        for i in range(1,len(nums)+1):
            total = total+i
        miss = total - (sum(nums) - rep)
        return (rep,miss)

