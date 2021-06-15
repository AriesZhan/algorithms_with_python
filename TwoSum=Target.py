def TwoSumChk(ls, target):
    fp = 0
    bp = len(ls)-1
    while(fp != bp):
        if (ls[bp] > target) or (ls[fp] + ls[bp]) > target:
            bp -= 1
        elif (ls[fp] + ls[bp]) < target:
            fp += 1
        else:
            print([fp, bp])
            return [fp, bp]
    return False
