from math import *
import random
import time

# Перебирает все ключи в заданом диапазоне [0, key_range) пока не не будет найдено значение равное key
# Возвращает время в мс
def broodforce(key_range: int, key: int):
    start_time = time.time()
    for k in range(key_range):
        if k == key:
            print(f"Найден ключ: {k}")
            return round((time.time() - start_time) * 1000)

if __name__ == "__main__":
    size = [2 ** x for x in range(int(log2(8)), int(log2(4096)) + 1)]
    for s in size:
        print(f"Количество вариантов {s}-битных ключей: {2 ** s}")

    for s in size:
        key_range = 2 ** s
        key = random.randint(0, key_range - 1)
        print(f"Случайный {s}-битный ключ: {key}")
        print(f"Время перебора: {broodforce(key_range, key)} мс.")