def HalfSearch(n, ls):
    if len(ls) == 1 and ls[0] != n:
        return False
    if ls[len(ls)//2] == n:
        return True
    elif ls[len(ls)//2] > n:
        tmpList = ls[0:len(ls)//2]
        return HalfSearch(n, tmpList)
    else:
        tmpList = ls[len(ls)//2:len(ls)]
        return HalfSearch(n, tmpList)


def HalfSearchV2(n, ls):
    tmp_ls = ls
    while len(tmp_ls) > 1:
        if tmp_ls[len(tmp_ls)//2] == n:
            return True
        elif tmp_ls[len(tmp_ls)//2] > n:
            tmp_ls = tmp_ls[0:len(tmp_ls)//2]
        else:
            tmp_ls = tmp_ls[len(tmp_ls)//2:len(tmp_ls)]
    if tmp_ls[0] == n:
        return True
    else:
        return False

# print(HalfSearchV2(6, [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 15]))
# print(HalfSearchV2(5, [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 15]))
