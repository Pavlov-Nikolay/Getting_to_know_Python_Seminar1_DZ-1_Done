# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input("Введите количество журавликов: "))

if number % 2 != 0:
    print('Петя и Сережа могут сделать только целое число журавликов. Повторите ввод')
else:
    c = int(number / 2)
    if (c % 2) == 0:
        a = int(number / 2)
        b = int((number / 2) // 2)
        print(f'Катя сделала {a} журавликов')
        print(f'Петя и Сережа сделали по {b} журавликов')
    else:
        a = int(number / 2) + 1
        b = int(a / 2)
        print(f'Катя сделала {a} журавликов')
        print(f'Петя и Сережа сделали по {b} журавликов')
