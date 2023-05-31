N = abs(int(input("Введите количество элементов в списке А: ")))
A = input("Введите через пробел элементы списка: ").split()
A1 = list(map(int, A))
if len(A1) != N:
    print("Некорректное количество элементов")
else:
    X = int(input("Введите число X, которое необходимо найти в списке A: "))
    count = 0
    for i in range(N):
        if A1[i] == X:
            count = count + 1
    print(f"Число {X} встречается в списке A {count} раз")