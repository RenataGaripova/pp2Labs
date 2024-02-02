def spy_game(nums):
    checker = 0
    for i in nums:
        if i == 0 and checker == 0:
            checker += 1

        if i == 0 and checker == 1:
            checker += 1

        if i == 7 and checker >= 2:
            return True

    return False

