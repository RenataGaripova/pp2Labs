def has_33(mylist):

    for i in range(0, len(mylist) - 1):
        if mylist[i] == 3 and mylist[i + 1] == 3:
            return False

    return True
