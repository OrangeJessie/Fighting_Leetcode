import random
import copy


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.initial_num = nums
        self.length = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.initial_num

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new = []
        copy_num = copy.copy(self.initial_num)
        for i in range(self.length, 0, -1):
            j = random.randint(0, i-1)
            new.append(copy_num[j])
            del copy_num[j]
        return new
