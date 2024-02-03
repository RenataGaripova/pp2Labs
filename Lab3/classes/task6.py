def isPrime(num): #function that defines if the number is prime or not
    d = 2
    if num == 0 or num == 1:
        return 0

    while d * d <= num:
        if num % d == 0:
            return 0
        d += 1

    return 1

lst = [34, 1, 2, 67, 8, 9, 44, 51, 13, 7]

new_lst = filter(lambda x: isPrime(x) == 1, lst) #adding all the prime numbers to a new list

print(*new_lst)