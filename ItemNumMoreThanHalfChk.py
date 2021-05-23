# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.dic = dict()

    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 1:
            return numbers[0]
        for num in numbers:
            if str(num) in self.dic:
                self.dic[str(num)] += 1
                if self.dic[str(num)] > (len(numbers)/2):
                    return num
            else:
                self.dic[str(num)] = 1
        return 0
