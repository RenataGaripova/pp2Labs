import time, math

msec = int(input())
sec = msec / 1000

num = int(input())

time.sleep(sec)

print(f"Square root of {num} after {msec} miliseconds is {math.sqrt(num)}")
