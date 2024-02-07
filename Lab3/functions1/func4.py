def filter_prime(numbers):
    lst1 = list(map(int, numbers.split())) #separating spaces from numbers
    length = len(lst1)
    lst2 = [True] * length #the list will contain boolean variables (true if number on position is prime, false if it's not)

    d = 2

    for i in range(length):
        if lst1[i] == 1 or lst1[i] == 0: #0 and 1 are not prime
            lst2[i] = False

        while d * d <= lst1[i]: #if the number has a divisor which is not equal to 1 or the number itself it's not prime
            if (lst1[i] % d == 0):
                lst2[i] = False
                break
            d += 1

        d = 2

    result = [lst1[i] for i in range(length) if lst2[i] == True]

    return result
