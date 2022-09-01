from functools import cmp_to_key
import re

def custom(b, a):
    a = re.split('([0-9]+)', a)
    b = re.split('([0-9]+)', b)
    aHead, bHead = a[0].lower(), b[0].lower()
    aNumber, bNumber = int(a[1]), int(b[1])
    if aHead == bHead: 
        return bNumber - aNumber
    elif aHead < bHead:
        return 1
    else: 
        return -1
    

def solution(files):
    return sorted(files, key=cmp_to_key(custom))