
n = int(input("Число n: "))
a = 0
f = 1

for i in range(1, n + 1):
    f *= i
    a += f

print(f"Сумма факториалов от 1 до {n}: {a}")
