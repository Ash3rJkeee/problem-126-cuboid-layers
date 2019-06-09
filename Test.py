# def f(a, b, c, k):
#     """
#     Возвращает количество кубов, необходимое для покрытия фигуры слоя n
#     a, b, c - грани исходного параллелепипеда
#     k - количество наложенных слоев на базовую фигуру
#     """
#
#     # количество кубов, необходимое для покрытия базовой площади
#     sum_base = (a*b + b*c + c*a)*2
#
#     # количество кубов, добавляемых к ребрам
#     sum_edge = ((a+b+c) + (k - 1)) * 4 * k
#
#     return sum_base + sum_edge
#
#
# a, b, c, k = 4, 4, 6, 29
#
# print(f(a, b, c, k))


def my_round(n):
    """округление до ближайшего четного"""
    answer = round(n)
    if answer % 2 != 0:
        if abs(answer - n + 1) < abs(answer - n - 1):
            return answer + 1
        else:
            return answer - 1
    else:
        return answer


n = 6.47

print(my_round(n))
print(round(n))
