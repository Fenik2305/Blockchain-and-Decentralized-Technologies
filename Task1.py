from random import *
import time

def exhaustive_search(byte):
    random_key = randint(0, 2 ** byte)
    begin = time.time()
    for i in range(2 ** byte):
        if i == random_key:
            end = time.time()
            print("successfully found the key", i)
            print(round((end - begin) * 1000))

size = [2 ** x for x in range(3, 13)]
print(size)
for x in size:
    print(f"{x}-byte: {2 ** x}")
print()

for byte in size:
    print('y')
    exhaustive_search(byte)
