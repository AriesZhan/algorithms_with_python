def Sqrt(x: int):
    r = 0
    mid = x//2
    if x == 0:
        return 0
    while r != mid:
        r = x // mid
        mid = (r+mid)//2
        print([r, mid])
        if r > mid:
            r = mid
    return r

# print(Sqrt(1000))
