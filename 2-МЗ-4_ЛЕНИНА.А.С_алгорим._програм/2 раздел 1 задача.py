month = int(input("Введите номер месяца (от 1 до 12): "))

if month < 1 or month > 12:
    print("Ошибка! Номер месяца должен быть от 1 до 12.")
else:
    if month in (12, 1, 2):
        season = "зима"
    elif 3 <= month <= 5:  
        season = "весна"
    elif 6 <= month <= 8:
        season = "лето"
    else:  
        season = "осень"
    
    print(f"Месяц номер {month} — это {season}.")
