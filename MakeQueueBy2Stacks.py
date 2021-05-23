# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.reverseStack = []
    def push(self, node):
        self.stack.append(node)# write code here
    def pop(self):
        self.reverseStack = self.stack
        self.reverseStack.reverse()
        val = self.reverseStack.pop()
        self.stack = self.reverseStack
        self.stack.reverse()
        return val