# Input order arrays A/B with element number m/n, but length of A extend to m+n.
# Merge array B into A.

def MergeSortedArray(A, m, B, n):
    i = m-1
    j = n-1
    k = m+n-1
    while k >= 0:
        if i < 0:
            A[k] = B[j]
            k -= 1
            j -= 1
            next
        elif j < 0:
            return A
        if A[i] <= B[j]:
            A[k] = B[j]
            j -= 1
        else:
            A[k] = A[i]
            i -= 1
        k -= 1
    return A
