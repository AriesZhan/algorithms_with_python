# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.cnt_list = {}
    def jumpFloor(self, number):
        if number <= 1:
            return 1
        if number not in self.cnt_list:
            self.cnt_list[number] = self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
        return self.cnt_list[number]

