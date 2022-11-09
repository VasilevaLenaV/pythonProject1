# Урок 4.
# Задача 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
def get_prime_factors(n):
    i = 2
    factors = []
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
            i = 2
        else:
            i += 1
    return factors


N = int(input('Задача 2. Введите число: '))

if N < 1:
    print(f"Значение {N} не является натуральным числом")
else:
    print(get_prime_factors(N))


# Задача 3.Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def get_uniq_value(values):
    uniq = []
    for i in range(len(values)):
        start = -1
        count = 0
        while True:
            start = values.find(values[i], start + 1)
            if start == -1:
                break
            count += 1
        if count == 1:
            uniq.append(values[i])
    return uniq


numbers = input("Задача 3. Задайте последовательность цифр: ")
print(get_uniq_value(numbers))

# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint
import itertools


def get_coefficients(k):
    coefficients = []
    for i in range(k + 1):
        coeff = randint(-100, 100)

        if coeff == 0:
            continue

        coefficients.append(coeff)
    return coefficients


def get_polynomial(k, ratios):
    var = ['*x**'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


k = int(input("Задача 4. Задайте натуральную степень k: "))

coeffs = get_coefficients(k)
polynom = get_polynomial(k, coeffs)

print(polynom)

with open('Polynomial.txt', 'w') as data:
    data.write(polynom)
