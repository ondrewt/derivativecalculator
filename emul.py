import math
def emul(a,b):
    c = abs(a)
    d = abs(b)
    sum1 = 0
    while d > 0:
        if d % 2 == 1:
            sum1 += c
        c = c * 2
        d = d // 2
    if a > 0 and b > 0:
        return sum1
    elif a < 0 and b < 0:
        return sum1
    elif a > 0 and b < 0:
        return sum1 * -1
    elif a < 0 and b > 0:
        return sum1 * -1
