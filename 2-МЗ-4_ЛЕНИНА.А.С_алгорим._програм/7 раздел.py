
import sys

def readFile():
    print("Содержимое файла: ")
    with open('2-МЗ-4.txt', 'r',encoding="utf8") as file: 
        for line in file: 
            line= line.replace("\n","") 
            print(line) 

print("Для конца напишите \"exit\"...")
while True:
    n = str(input("Введите имя студента: "))
    if n == "exit":
        readFile()
        sys.exit(0)
    m = str(input("Введите почту студента: "))
    if m == "exit":
        readFile()
        sys.exit(0)
    with open("2-МЗ-4.txt", 'a',encoding="utf8") as file: 
        file.write(f"{n} - {m}\n")

