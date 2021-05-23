import os
import sys


class Solution2:
    def merge(A, m, B, n):
        if m == 0 or n == 0 or not A or not B:
            return A+B
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                i += 1
            else:
                A.insert(i, B[j])
                j += 1
        if i >= m:
            return A + B[j:n]
        elif j >= n:
            return A
