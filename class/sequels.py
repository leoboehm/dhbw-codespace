def fibonacci(n):
    a = 0
    b = 1

    if n < 1:
        print("undefined")
    if n == 1:
        print(a)
    if n == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(n):
            total = a + b
            a = b
            b = total

            print(total, end=" ")
    print()

fibonacci(10)

def rows():
    counter = input("Geben Sie eine Zahl zwischen 1 und 9 ein: ")
    if int(counter) > 9:
        rows()
    
    print(int(counter) * counter)

rows()

def primeChecker():
    number = int(input("Geben Sie eine beliebige ganze Zahl ein: "))
    partialsList = []
    
    for i in range(2, number):
        if number % i == 0:
            partialsList.append(i)

    if number < 2 or len(partialsList) != 0:
        print("Die eingegebene Zahl ist KEINE Primzahl!")
    else:
        print("Die eingegebene Zahl ist eine Primzahl!")

primeChecker()