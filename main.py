N = int(input("Введите количество чисел: "))
a = []
print("Введите ", N, " чисел:")
for i in range(N):
    print(i+1, ": ")
    a.append(int(input()))

print("Выбери направление сортировки: 1 - возрастание, 2 - убывание")
way = int(input())

if way == 1:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
if way == 2:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
else:
    print("Некорректный ввод")
print(a)