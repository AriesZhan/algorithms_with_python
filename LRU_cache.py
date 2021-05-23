import collections


class Solution:
    def __init__(self):
        self.cache = collections.OrderedDict()
        self.rslt = []
        self.volume = 0

    def set(self, key, value):
        if self.volume == 0:
            self.cache.popitem(last=False)
        elif self.volume > 0:
            self.volume -= 1
        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def LRU(self, operators, k):
        self.volume = k
        for item in operators:
            if item[0] == 1:
                self.set(item[1], item[2])
            elif item[0] == 2:
                self.rslt.append(self.get(item[1]))
        return self.rslt


obj = Solution()
print(obj.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3))
