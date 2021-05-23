# AriesZhan, coding starts at 2020-11-25
import numpy as np
import pandas as pd
import os
import time
import sys
import re

__name__ = "algorithms"


class algorithms:
    def __init__(self, **kw_args):
        # if need to init any privated variables, add them here.
        print("Init algorithms obj.")

    def bubbleSorting(self, ls):
        if len(ls) <= 0:
            print("Input List is NULL!")
            return False
        print(ls)
        running = True
        sortnum = len(ls)-1
        # for sortnum in range(len(ls)-1, 0 , -1):
        while sortnum > 0 and running:
            running = False
            for i in range(sortnum):
                print("sorting.")
                j = i + 1
                if ls[i] > ls[j]:
                    running = True
                    ls[i], ls[j] = ls[j], ls[i]
                    print("exchanged.")
            sortnum = sortnum - 1
            print(ls)

    def selectSorting(self, ls):
        if len(ls) <= 0:
            print("Input List is NULL!")
            return False
        elif len(ls) == 1:
            print("Only 1 element, no need for sorting.")
            print(ls)
            return ls
        for sortnum in range(len(ls)-1, 0, -1):
            maxIndex = sortnum
            for i in range(sortnum):
                print("sorting.")
                if ls[i] > ls[maxIndex]:
                    maxIndex = i
            if sortnum != maxIndex:
                ls[sortnum], ls[maxIndex] = ls[maxIndex], ls[sortnum]
                print("exchanged.")
            print(ls)

    def selectSortingExt(self, ls):
        if len(ls) <= 0:
            print("Input List is NULL!")
            return False
        elif len(ls) == 1:
            print("Only 1 element, no need for sorting.")
            return ls
            print(ls)
        for sortnum in range(len(ls)-1, 0, -1):
            for i in range(sortnum):
                print("sorting.")
                if ls[i] > ls[sortnum]:
                    ls[sortnum], ls[i] = ls[i], ls[sortnum]
                    print("exchanged.")
            print(ls)

    def rapidSorting(self, ls, first, last):
        if len(ls) <= 0 or first > last:
            print("Arguments Error!")
            return False
        elif len(ls) == 1 or first == last:
            print("Only 1 element, no need for sorting.")
        elif first + 1 == last:
            if ls[first] > ls[last]:
                ls[first], ls[last] = ls[last], ls[first]
        else:
            # separate ls to 2 partition, one's elements less than the base value, another's element greater than the base value.
            splitpoint = self.rapidSortingPartition(ls, first, last)
            # recursively invoke rapidSorting function to handle those 2 new ls partitions.
            self.rapidSorting(ls, first, splitpoint)
            self.rapidSorting(ls, splitpoint+1, last)

    def rapidSortingPartition(self, ls, first, last):
        leftmark = first
        rightmark = last
        basevalue = int((ls[first] + ls[last]+ls[int((first+last)/2)])/3)
        print([leftmark, rightmark, basevalue])
        while leftmark < rightmark:
            while ls[leftmark] < basevalue:
                leftmark = leftmark + 1
                print("move leftmark to index:"+str(leftmark))
            while ls[rightmark] > basevalue:
                rightmark = rightmark - 1
                print("move rightmark to index:"+str(rightmark))
            if leftmark < rightmark:
                print("exchange value of leftmark and rightmark.")
                ls[leftmark], ls[rightmark] = ls[rightmark], ls[leftmark]
                print(ls)
            else:
                return rightmark

    def decToBinary(self, data):
        if re.search('int', str(type(data))):
            stack = self.Stack()
            while data > 0:
                stack.push(data % 2)
                data = data // 2
            binaryStr = ''
            while not stack.isEmpty():
                binaryStr += str(stack.pop())
            return binaryStr
        else:
            print("Input data is not integer!")
            return False

    class BinaryTree:
        def __init__(self, rootValue=None):
            # if need to init any privated variables, add them here.
            print("Init Binary Tree obj.")
            self.key = rootValue
            self.leftChild = None
            self.rightChild = None

        def setRootValue(self, rootValue):
            self.key = rootValue

        def getRootValue(self):
            return self.key

        def getLeftChild(self):
            return self.leftChild

        def getRightChild(self):
            return self.rightChild

        def insertLeft(self, node):
            if self.leftChild == None:
                self.leftChild = BinaryTree(node)
            else:
                newnode = BinaryTree(node)
                newnode.leftChild, self.leftChild = self.leftChid, newnode

        def insertRight(self, node):
            if self.rightChild == None:
                self.rightChild = BinaryTree(node)
            else:
                newnode = BinaryTree(node)
                newnode.rightChild, self.rightChild = self.rightChid, newnode

    class Stack:
        def __init__(self):
            # if need to init any privated variables, add them here.
            print("Init Stack obj.")
            self.stack = []

        def push(self, value):
            if re.search('list', str(type(value))):
                self.stack += value
            else:
                self.stack.append(value)

        def pop(self):
            if not self.isEmpty():
                return self.stack.pop()

        def isEmpty(self):
            return self.stack == []

        def peek(self):
            if not self.isEmpty():
                return self.stack[len(self.stack) - 1]

        def size(self):
            return len(self.stack)

        def reverse(self):
            tempList = []
            while len(self.stack) > 0:
                tempList.append(self.stack.pop())
            self.stack = tempList

        def content(self):
            return self.stack

    class Formula:
        def __init__(self, formulaStr):
            print("Init Formula obj.")
            if len(formulaStr.replace(' ', '')) > 3:
                self.formulaStr = formulaStr
            else:
                print("Input formula string is not valid!")
                exit(0)
            self.signList = []

        def formulaStrToList(self, formulaStr: str = ''):
            if len(self.signList) > 0 and formulaStr == '':
                print("Formula string already convert to list.")
            else:
                if formulaStr == '':
                    formulaStr = self.formulaStr
                decimalStr = ''
                signList = []
                if re.search('[+\-*/()\s\d]{3,}', formulaStr):
                    for c in formulaStr:
                        if c in '+-*/()':
                            if len(decimalStr) > 0:
                                signList.append(decimalStr)
                                decimalStr = ''
                            signList.append(c)
                        elif c in '0123456789.':
                            decimalStr += c
                    if len(decimalStr) > 0:
                        signList.append(decimalStr)
                        decimalStr = ''
                    if formulaStr == self.formulaStr:
                        self.signList = signList
                    return signList
                else:
                    print("The formula format is not valid!")
                    return False

        def preOrder(self):
            # get fully Infix Order formula list.
            fullyInfixStack = self.fullyInfixOrder()
            # create a stack to store the results.
            preOrderStack = algorithms.Stack()
            operatorStack = algorithms.Stack()
            while not fullyInfixStack.isEmpty():
                sign = fullyInfixStack.pop()
                if sign == ')':
                    next
                elif re.search('\d+', sign):
                    preOrderStack.push(sign)
                elif sign in '+-*/':
                    operatorStack.push(sign)
                elif sign == '(':
                    preOrderStack.push(operatorStack.pop())
            preOrderStack.reverse()
            return preOrderStack

        def preOrderCalc(self):
            preOrderStack = self.preOrder()
            calcStack = algorithms.Stack()
            while not preOrderStack.isEmpty():
                sign = preOrderStack.pop()
                if re.search('\d+', sign):
                    calcStack.push(sign)
                elif sign in '+-*/':
                    value1 = calcStack.pop()
                    value2 = calcStack.pop()
                    calcStack.push(eval(str(value1)+sign+str(value2)))
            return calcStack.pop()

# still need to enhance to add parenthesis for sign "+" and "-".
        def fullyInfixOrder(self):
            # convert formula string to list.
            if len(self.signList) == 0:
                self.formulaStrToList()
            # create a stack to store the results.
            fullyInfixStack = algorithms.Stack()
            # init a string to store signs work with operators '*' and '/' which need to add parenthesis .
            formulaConvertStr = ''
            fullyInfixStack.push('(')

            for c in self.signList:
                if c in '*/':
                    priorSign = fullyInfixStack.pop()
                    if priorSign == ')':
                        count = 1
                        while count:
                            popChar = fullyInfixStack.pop()
                            if popChar == ')':
                                count += 1
                            elif popChar == '(':
                                count -= 1
                            priorSign = popChar + priorSign
                    formulaConvertStr = priorSign + c
                    print(formulaConvertStr)
                else:
                    if len(formulaConvertStr) > 0:
                        if c in ')+-':
                            if c == ')' and fullyInfixStack.peek() != '(' or c in '+-':
                                formulaConvertStr = '(' + \
                                    formulaConvertStr + ')'
                            for char in self.formulaStrToList(formulaConvertStr):
                                fullyInfixStack.push(char)
                            formulaConvertStr = ''
                            fullyInfixStack.push(c)
                        else:
                            formulaConvertStr += c
                    else:
                        if c in '+-':
                            tmplist = []
                            # need to enhance here.
                            for i in range(3):
                                tmplist.append(fullyInfixStack.pop())
                            fullyInfixStack.push('(')
                            for i in range(3):
                                fullyInfixStack.push(tmplist.pop())
                            fullyInfixStack.push(')')
                        fullyInfixStack.push(c)
            if len(formulaConvertStr) > 0:
                formulaConvertStr = '(' + formulaConvertStr + ')'
                for char in self.formulaStrToList(formulaConvertStr):
                    fullyInfixStack.push(char)
                formulaConvertStr = ''

            fullyInfixStack.push(')')
            return fullyInfixStack

        def postOrder(self):
            # get fully Infix Order formula list.
            fullyInfixList = self.fullyInfixOrder().stack
            # create a stack to store the results.
            postOrderStack = algorithms.Stack()
            operatorStack = algorithms.Stack()
            for sign in fullyInfixList:
                if sign == '(':
                    next
                elif re.search('\d+', sign):
                    postOrderStack.push(sign)
                elif sign in '+-*/':
                    operatorStack.push(sign)
                elif sign == ')':
                    postOrderStack.push(operatorStack.pop())
            return postOrderStack

        def postOrderCalc(self):
            postOrderStack = self.postOrder().stack
            calcStack = algorithms.Stack()
            for sign in postOrderStack:
                if re.search('\d+', sign):
                    calcStack.push(sign)
                elif sign in '+-*/':
                    value2 = calcStack.pop()
                    value1 = calcStack.pop()
                    calcStack.push(eval(str(value1)+sign+str(value2)))
            return calcStack.pop()

        def formulaToBinaryTree(self):
            # Not completed.
            if len(self.signList) > 3:
                treeStack = algorithms.Stack()
                fullyInfixList = self.fullyInfixOrder().stack
                for c in fullyInfixList:
                    if c == '(':
                        if not treeStack.isEmpty():
                            currentNode = treeStack.peek()
                            if currentNode.getLeftChild() != None:
                                currentNode.insertRight()
                                treeStack.push(currentNode.getRightChild())
                            else:
                                currentNode.insertLeft()
                                treeStack.push(currentNode.getLeftChild())
                        else:
                            treeStack.push(algorithms.BinaryTree())
                    elif re.search('\d+', c):
                        upperNode = treeStack.peek()
                        if upperNode.getLeftChild() != None:
                            upperNode.insertRight(c)
                            treeStack.push(upperNode.getRightChild())
                        else:
                            upperNode.insertLeft(c)
                    elif c in '+-*/':
                        currentNode = treeStack.peek()
                        currentNode.setRootValue(c)
                    elif c == ')':
                        if len(fullyInfixList) > 0:
                            treeStack.pop()
                        else:
                            return treeStack.pop()
            else:
                print(
                    "Sign List error, please invoke formulaStrToList() and  to generate sign list!")
                return False
