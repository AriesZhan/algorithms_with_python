def MinWindowSubstring(strA, strB):
    lp = rp = 0
    flag = {}
    min_str = ""
    for i in strB:
        flag[i] = 0
    cnt = 0
    while rp < len(strA):
        if strA[rp] in flag:
            flag[strA[rp]] += 1
            if flag[strA[rp]] == 1:
                cnt += 1
            while cnt == len(strB):
                if strA[lp] in flag:
                    if flag[strA[lp]] > 1:
                        flag[strA[lp]] -= 1
                        lp += 1
                    else:
                        if not min_str or len(min_str) > rp-lp+1:
                            min_str = strA[lp:rp+1]
                        break
                else:
                    lp += 1
        rp += 1
    return min_str


# print(MinWindowSubstring("ADOBECODEBANC", "ABC"))
