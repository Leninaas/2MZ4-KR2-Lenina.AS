
import random

a = random.randint(1, 10)
b = 7

for i in range(b):
    c = b - i
    print(f"Осталось попыток: {c}")
    
    d = int(input("Твое число: "))
    
    if d == a:
        print("Победа!")
        break
    elif d < a:
        print("Загаданное число больше...")
    else:
        print("Загаданное число меньше...")
    
    if i == b - 1:
        print(f"Поражение! Загаданное число: {a}")
