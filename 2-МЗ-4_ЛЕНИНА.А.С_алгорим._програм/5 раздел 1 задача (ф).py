def find_max_digit(num):
    """
    Функция для поиска наибольшей цифры в числе.
    :param num: натуральное число
    :return: наибольшая цифра в числе
    """
    max_digit = 0
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    return max_digit

def main():
    number = int(input("Введите натуральное число: "))
    
    result = find_max_digit(number)
    
    print(f"Наибольшая цифра в числе {number} — это {result}")

if __name__ == "__main__":
    main()
