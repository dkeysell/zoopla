import time


def square_of_digits(_i):
    total = 0
    for c in map(int, str(_i)):
        total = total + int(c) * int(c)
    if total == 1:
        #print('ended at 1')
        return 0
    if total == 89:
        #print('ended at 89')
        return 1
    return square_of_digits(total)


count = 0
negative_cases = []
start = time.time()
for i in range(1, 10000000, 1):
    #print('starting: ' + str(i))
    count = count + square_of_digits(i)

print('time taken: ' + str(time.time() - start))
print(count)

