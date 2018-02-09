def mul(a,b):
    count = 1
    c = a
    while count < b:
        a = a + c
        count = count + 1
    return a
