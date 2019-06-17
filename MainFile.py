import datetime
from math import ceil
import math

"""Плохой и крайне медленный способ. Способ из файла BetterWay гораздо быстрее.
Хитрость была в области поиска габаритов.
Этот метод пытался перебирать количество кубиков и под него однозначно рассчитывать количество свлоев и 3-й 
размер параллелепипеда. При этом теряются все промежуточные результаты.

Бессмысленно при такой скорости прямого подхода при нормально заданных граничных размерах."""

# todo 1) Написать проверку на повторяющиеся комбинации ГОТОВО


def c(n):
    """Принимает количество кубиков. Возвращает количество комбинаций для введенного количества кубиков"""

    def f(a, b, c, k):
        """
        Возвращает количество кубов, необходимое для покрытия фигуры слоя n
        a, b, c - грани исходного параллелепипеда
        k - количество ПОВТОРНО наложенных слоев на базовую фигуру
        (первое оборачивание k = 0)
        """

        # количество кубов, необходимое для покрытия базовой площади
        sum_base = (a * b + b * c + c * a) * 2

        # количество кубов, добавляемых к ребрам
        # sum_edge = (a+b+c) * 4 * k + (k - 1)*8
        sum_edge = ((a + b + c) + (k - 1)) * 4 * k

        return sum_base + sum_edge

    def square_solution(a, b, c):
        """Решает квадратное уравнение. Возвращает МНОЖЕСТВО (set() ) положительных решений."""
        discr_square = b ** 2 - 4 * a * c
        if discr_square >= 0:
            discr = math.sqrt(discr_square)
            x1 = round((-b + discr) / (2 * a))
            x2 = round((-b - discr) / (2 * a))
            answer = set()
            if x1 >= 0:
                answer.add(x1)
            if x2 >= 0:
                answer.add(x2)
            return answer
        else:
            return {}

    count = 0

    # перебор комбинаций паралеллепипедов для каждого k

    # a_max, b_max, c_max оцениваем из условия, что при фиксированном n a максимально при (a_max, 1, 1)
    # тогда n = a_max*f + 2. Выражаем а_max с округлением вверх до целых.
    a_max = ceil((n - 2) / 4)
    b_max = a_max

    for a in range(1, a_max + 1):
        for b in range(a, b_max + 1):

            # при заданных a и b можем однозначно определить максимум для с из условия, что максимальные размеры для
            # минимального количества слоев n = sum_base (k=0)
            c_max = ceil((n - 2 * a * b) / (2 * (a + b)))
            for c in range(b, c_max + 1):

                # коэффициенты квадратного уравнения, относительно k
                a_ = 4
                b_ = 4 * (a + b + c - 1)
                c_ = 2 * (a * b + b * c + c * a) - n

                # находим все k, однозначно определямые по формуле, при заданных a, b, c и перебираем их
                for k in square_solution(a_, b_, c_):

                    # если комбинация удовлетворяет условию, то проверяем параллелепипед на повторяемость и записываем
                    # комбинацию в массив
                    if f(a, b, c, k) == n:
                        count = count + 1
    return count


def my_round(n):
    """округление до ближайшего четного. Пригодится, т.к. количество кубиков всегда должно быть четным"""
    answer = round(n)
    if answer % 2 != 0:
        if abs(answer - n + 1) < abs(answer - n - 1):
            return answer + 1
        else:
            return answer - 1
    else:
        return answer


# область поиска кубиков
n_start = 18000
delta = 2

# число параллелепипедов, содержащих k кубов в одном из своих слоев
res = 1000

start = datetime.datetime.now()

# количесвто подходящих комбинаций для данного k
max_count = 0

# значение k, при котором достигнуто max_count
max_count_n = 0

answer = 0

print()

# n - потенциальное количество кубиков
# for n in range(n_min, n_max + 1, 2):

n = n_start
while True:
    cn = c(n)
    print("("+str(n)+";"+str(cn)+")")
    n = n + delta
    if cn == res:
        break

finish = datetime.datetime.now()
ellapsed_time = finish - start

print()
print("\nВычисления закончены и заняли ", ellapsed_time.seconds, "секунд.")

if answer != 0:
    print("C(" + str(answer) + ") = " + str(res))
else:
    print("Максимальное количество комбинаций = " + str(max_count) + " при n = " + str(max_count_n))


