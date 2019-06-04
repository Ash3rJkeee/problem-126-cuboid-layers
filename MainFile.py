import datetime
from math import ceil
import itertools
import math


# todo 1) Написать проверку на повторяющиеся комбинации ГОТОВО


def f(a, b, c, k):
    """
    Возвращает количество кубов, необходимое для покрытия фигуры слоя n
    a, b, c - грани исходного параллелепипеда
    k - количество ПОВТОРНО наложенных слоев на базовую фигуру
    (первое оборачивание k = 0)
    """

    # количество кубов, необходимое для покрытия базовой площади
    sum_base = (a*b + b*c + c*a)*2

    # количество кубов, добавляемых к ребрам
    # sum_edge = (a+b+c) * 4 * k + (k - 1)*8
    sum_edge = ((a+b+c) + (k - 1)) * 4 * k

    return sum_base + sum_edge


def entry_check(a, b, c):
    """Получает на вход размеры фигуры и проверет, не была ли она уже проверена в другой ориентации.
    Возвращает:
    True - если проверяется впервые
    False - если фигура раньше встречалась"""

    my_list = itertools.permutations((a, b, c))
    for i in my_list:
        if i in inner_set_for_check:
            return False
    return True


def square_solution(a, b, c):
    """Решает квадратное уравнение. Возвращает МНОЖЕСТВО (set() ) положительных решений."""
    discr_square = b**2 - 4*a*c
    if discr_square >= 0:
        discr = math.sqrt(discr_square)
        x1 = round((-b + discr)/(2*a))
        x2 = round((-b - discr)/(2*a))
        answer = set()
        if x1 >= 0:
            answer.add(x1)
        if x2 >= 0:
            answer.add(x2)
        return answer
    else:
        return {}


# максимальное количество слоев, которе надо рассматривать
max_layers = 12

# область поиска кубиков
n_min = 10000
n_max = 10000

# число параллелепипедов, содержащих k кубов в одном из своих слоев
res = 1000

# массив комбинаций (a, b, c, n)
massive_list = []

start = datetime.datetime.now()

# количесвто подходящих комбинаций для данного k
max_count = 0

# значение k, при котором достигнуто max_count
max_count_n = 0

answer = 0

print()

# n - потенциальное количество кубиков
for n in range(n_min, n_max + 1, 2):
    inner_set_for_check = set()  # множество комбинаций {(a, b, c)} для каждого n, как можеств для пропуска дубликатов
    inner_massive_as_list = []    # внутренний массив комбтнаций (a, b, c, n) в виде листа
    count = 0

    # перебор комбинаций паралеллепипедов для каждого k

    # a_max, b_max, c_max оцениваем из условия, что при фиксированном n a максимально при (a_max, 1, 1)
    # тогда n = a_max*f + 2. Выражаем а_max с округлением вверх до целых.
    a_max = ceil((n - 2) / 4)
    b_max = a_max
    c_max = a_max

    for a in range(1, a_max + 1):
        for b in range(a, b_max + 1):
            for c in range(b, c_max + 1):

                # коэффициенты квадратного уравнения, относительно k
                a_ = 4
                b_ = 4*(a+b+c-1)
                c_ = 2*(a*b+b*c+c*a)-n

                # находим все k, однозначно определямые по формуле, при заданных a, b, c и перебираем их
                for k in square_solution(a_, b_, c_):

                    # прогрессбар
                    progress = round((n - n_min) / (n_max + 1 - n_min) * 100, 1)
                    print("\rПрогресс: " + str(progress) + "%",
                          "(" + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(k) + ")  " + "n = " + str(n),
                          end="")

                    # если комбинация удовлетворяет условию, то проверяем параллелепипед на повторяемость и записываем
                    # комбинацию в массив
                    if f(a, b, c, k) == n:
                        if entry_check(a, b, c):
                            inner_set_for_check.add((a, b, c))
                            inner_massive_as_list.append((a, b, c, k))
                            count = count + 1

    # если получили массив больший, чем при прощлом количестве кубиков, то перезаписываем массив, как максиальный
    if count > max_count:
        max_count = count
        max_count_n = n
        massive_list = inner_massive_as_list[:]

    # если досчитали до количества комбинаций, как в условии задачи, то остановить перебор
    if count == res:
        answer = n
        break


finish = datetime.datetime.now()
ellapsed_time = finish - start

print()
print("\nВычисления закончены и заняли ", ellapsed_time.seconds, "секунд.")

if answer != 0:
    print("C(" + str(answer) + ") = " + str(res))
else:
    print("Максимальное количество комбинаций = " + str(max_count) + " при n = " + str(max_count_n))

for i in massive_list:
    print(massive_list.index(i) + 1, i)
