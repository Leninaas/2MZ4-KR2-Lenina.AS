
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

print(f"Числа от {A} до {B}: ", end="")

if A < B:
    
    for number in range(A, B + 1):
        print(number, end=" ")
elif A > B:
  
    for number in range(A, B - 1, -1):
        print(number, end=" ")
else:
    print(A, end="")

print() 
