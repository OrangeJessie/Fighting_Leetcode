class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num = []
        self.minimum = []           # 添加minimum记录最小的

    # 等于也要记录，因为pop掉一个最小的后，如果不记录等于的，相当于把所以等于最小的都pop了
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.num.append(x)
        if self.minimum ==[] or self.minimum[-1] >= x:
            self.minimum.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self.num[-1]
        del self.num[-1]
        if value == self.minimum[-1]:
            del self.minimum[-1]
        return value

    def top(self):
        """
        :rtype: int
        """
        return self.num[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # l = len(self.num)
        # minimum = self.num[0]
        # for i in range(1, l):
        #     if self.num[i] < minimum:
        #         minimum = self.num[i]
        # return minimum
        return self.minimum[-1]
