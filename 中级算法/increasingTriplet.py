# 递增的三元子序列
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。


# 可以用归并的方法，但时间复杂度为O(nlogn)
class Solution(object):
    # 只需要把每个位置都更新为当前可以的最小值，只要出现大于first和second的就返回True
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    def increasingTriplet2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ln = len(nums)
        if ln < 3:
            return False
        minr = nums[0]
        mintemp = nums[0]
        max1 = -2147483648
        max2 = -2147483648
        for i in nums:
            if (i == max1) or (i == mintemp):
                continue
            elif i < mintemp:
                mintemp = i
            elif (i > mintemp) and (i < minr):
                minr = mintemp
                max1 = i
            else:
                minr = mintemp
                if max1 == -2147483648:
                    max1 = i
                elif i > max1:
                    max2 = i
                elif i < max1:
                    max1 = i
            if max2 != -2147483648:
                return True
        return False
