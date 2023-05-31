N = abs(int(input("Введите количество элементов в списке А: ")))
A = input("Введите через пробел элементы списка: ").split()
A1 = list(map(int, A))
if len(A1) != N or N == 0:
    print("Некорректное количество элементов")
else:
    X = int(input("Введите число X, для сравнения со списком: "))
    max = abs(X - A1[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A1[i])
        if count < max:
            max = count
            index = i
    print(f"Число {A1[index]} в списке A наиболее близко по величине к числу {X}")