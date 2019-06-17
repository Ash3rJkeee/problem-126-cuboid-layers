"""Гораздо лучшее решение. Работает очень быстро. Дело в грамотно заданных интервалах размеров.
А так же не теряются значения прошлых итераций."""

import datetime


def x(a, b, c, n):
    """Возвращает количество кубиков, необходимое, для покрытия фигуры размеров a,b,c слоем n"""
    return 2*(a*b+a*c+b*c) + 4*(a+b+c)*(n-1) + 4*(n-1)*(n-2)


# область поиска используемого количества кубиков
nmax = 20000


# массив ответов C
s = (nmax + 1) * [0]

start = datetime.datetime.now()

for a in range(1, nmax + 1):
    for b in range(a, nmax // a + 1):
        for c in range(b, nmax // b + 1):
            for n in range(1, nmax):
                y = x(a, b, c, n)
                if y > nmax:
                    break
                s[y] += 1

finish = datetime.datetime.now()
time = finish - start

print("Вычисления закончены и заняли", time.microseconds, "микросекунд.")

print(s.index(1000))
