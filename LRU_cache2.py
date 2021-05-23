#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#

class Solution:
    def __init__(self):
        self.cache = dict()
        self.order = list()
        self.rslt = list()
        self.volume = 0

    def set(self, key, value):
        if self.volume == 0:
            self.cache.pop(self.order.pop(0))
        elif self.volume > 0:
            self.volume -= 1
        self.order.append(key)
        self.cache[key] = value
        
    def get(self,key):
        if key not in self.cache:
            return -1
        indx = self.order.index(key)
        k = self.order.pop(indx)
        self.order.append(k)
        return self.cache[key]
    
    def LRU(self , operators , k):
        self.volume = k
        for item in operators:
            if item[0] == 1:
                self.set(item[1], item[2])
            elif item[0] == 2:
                self.rslt.append(self.get(item[1]))
        return self.rslt