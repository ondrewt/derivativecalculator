def roundit(integer):
    if integer > 0:
        positive = integer + 1/2
        pfinal = int(positive)
        return pfinal
    elif integer < 0:
        negative = integer - 1/2
        nfinal = int(negative)
        return nfinal
    elif integer == 0:
        return 0
