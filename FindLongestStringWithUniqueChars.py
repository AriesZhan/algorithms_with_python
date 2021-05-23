import os
import sys


def fsp_find_longest(s):
    sp = 0
    sub_str = ""
    for index in range(1, len(s)):
        fp = index
        if s[fp] in s[sp:fp]:
            if fp-sp > len(sub_str):
                sub_str = s[sp:fp]
            sp += 1
    print(fp-sp)
    print(sub_str)
