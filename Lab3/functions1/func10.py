def only_unique(mylist):

    result = [elem for elem in mylist if mylist.count(elem) == 1]

    return result
