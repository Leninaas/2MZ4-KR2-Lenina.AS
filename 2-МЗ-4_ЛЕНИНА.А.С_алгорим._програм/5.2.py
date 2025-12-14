
def calc(n):
    if n == 0:
        return 0
    a = ""
    while n > 0:
        a = str(n % 2) + a
        n = n // 2
    return a

b = int(input("Введите десятичное число: "))
a = calc(b)

print(f"Десятичное число: {b}")
print(f"Двоичное представление: {a}")
