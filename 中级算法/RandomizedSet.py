class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataset = set()
        self.datalist = []
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataset:
            return False
        self.dataset.add(val)
        self.size += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataset:
            self.dataset.remove(val)
            self.size -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        rand_index = random.randint(0, self.size)
        return list(self.dataset)[rand_index]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())
