import datetime


def f(a, b, c, n):
    """
    Возвращает количество кубов, необходимое для покрытия фигуры слоя n
    a, b, c - грани исходного параллелепипеда
    n - количество наложенных слоев на базовую фигуру
    """

    # количество кубов, необходимое для покрытия базовой площади
    sum_base = (a*b + b*c + c*a)*2

    # количество кубов, добавляемых к ребрам
    sum_edge = ((a+b+c)+(n-1))*4*n

    return sum_base + sum_edge


# максимальное количество слоев, которе надо рассматривать
max_layers = 10

# область поиска кубиков
k_min = 156
k_max = 156

# число параллелепипедов, содержащих k кубов в одном из своих слоев
res = 10

massive = []
massive_list = []

start = datetime.datetime.now()

answer = 0

# количесвто подходящих комбинаций для данного k
max_count = 0

# значение k, при котором достигнуто max_count
max_count_k = 0

print()
for k in range(k_min, k_max + 1, 2):
    count = 0

    # перебор комбинаций паралеллепипедов для каждого k
    for a in range(1, k + 1):
        for b in range(a, k + 1):
            for c in range(b, k + 1):
                for n in range(0, max_layers):

                    # прогрессбар
                    progress = round((k - k_min) / (k_max + 1 - k_min) * 100, 1)
                    print("\rПрогресс: " + str(progress) + "%",
                          "("+str(a)+", "+str(b)+", "+str(c)+", "+str(n)+")  " + "k = " + str(k),
                          end="")

                    if f(a, b, c, n) == k:
                        abc_set = {a, b, c, n}
                        if abc_set not in massive:
                            massive.append(abc_set)
                            massive_list.append((a, b, c, n))
                            count = count + 1

                            if count > max_count:
                                max_count = count
                                max_count_k = k

                            if count == res:
                                answer = k
                                break

                            continue


finish = datetime.datetime.now()
ellapsed_time = finish - start

print()
print("\nВычисления закончены и заняли ", ellapsed_time.seconds, "секунд.")

if answer != 0:
    print("C(" + str(answer) + ") = " + str(res))
else:
    print("Максимальное количество комбинаций =" + str(max_count) + " при k = " + str(max_count_k))

for i in massive_list:
    print(massive_list.index(i), i)

# count = 0
# for item in massive_list:
#     count = count + 1
#     print("\n", count, item)


# Вычисления закончены и заняли  175 секунд.
# C(154) = 10
# 0 (1, 1, 18, 1)
# 1 (1, 1, 38, 0)
# 2 (1, 2, 5, 3)
# 3 (1, 2, 25, 0)
# 4 (1, 3, 11, 1)
# 5 (1, 4, 9, 1)
# 6 (1, 5, 12, 0)
# 7 (2, 7, 7, 0)
# 8 (3, 3, 4, 2)
# 9 (3, 3, 7, 1)

# Вычисления закончены и заняли  186 секунд.
# Максимальное количество комбинаций =3 при k = 156
# 0 (1, 2, 14, 1)
# 1 (2, 2, 11, 1)
# 2 (2, 5, 6, 1)