number = int(input("Введите натуральное число: "))

max_digit = 0

temp = number
while temp > 0:
    digit = temp % 10   
    if digit > max_digit:
        max_digit = digit  
    temp //= 10         

print(f"Наибольшая цифра в числе {number} — это {max_digit}")
