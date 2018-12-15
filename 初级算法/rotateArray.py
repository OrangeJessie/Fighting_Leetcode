class Solution:
    # 原地算法, 时间复杂度O(n**2)
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        k = divmod(k, length)[1]
        if k < length/2:
            while i < k:
                a = nums[length-1]
                for j in range(length-1, 0, -1):
                    nums[j] = nums[j-1]
                nums[0] = a
                i += 1
        else:
            k = length - k
            while i < k:
                a = nums[0]
                for j in range(0, length-1, 1):
                    nums[j] = nums[j+1]
                nums[length-1] = a
                i += 1
    # 原地算法
    def rotate3(self, nums, k):
        l = len(nums)
        k %= l
        k1 = l - k
        if k != 0:
            for i in range((k1 - 1) // 2 + 1):
                t1 = nums[i]
                nums[i] = nums[k1 - 1 - i]
                nums[k1 - 1 - i] = t1
            for j in range(k1, (k1 + l - 1) // 2 + 1):
                t2 = nums[j]
                nums[j] = nums[l - 1 + k1 - j]
                nums[l - 1 + k1 - j] = t2
            r_l = int(l/2)
            for i in range(r_l):
                a = nums[i]
                num[i] = nums[l-i-1]
                num[l-i-1] = a

    # 非原地算法，时间复杂度O(n)
    def rotate4(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = divmod(k, length)[1]
        p = nums[0: length-k]
        nums[0: k-1] = nums[length-k:]
        nums[k:] = p


s = Solution()
num = [1, 2, 3, 4, 5, 6, 7]
r_k = 4
s.rotate3(num, r_k)
print(num)

