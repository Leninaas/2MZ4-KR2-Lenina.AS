# 4.3
h = int(input("Введите высоту елки: "))
s = input("Введите символ для елки: ")

print(" " * (h - 1) + "||")

for i in range(1, h):
    a = " " * (h - i - 1)
    b = s * i
    print(a + b + "||" + b)
 
print(" " * (h - 1) + "||")
