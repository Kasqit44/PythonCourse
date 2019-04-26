a2 = input('Введите положительное число и я посчитаю сумму и произведение его цифр ')
a2 = list(a2)


def sum_a2():
    ss = 0
    for i in range(len(a2)):
        ss += int(a2[i])
    print ('сумма чисел вашего числа =', ss)
    
def mult_a2():
    mm = 1
    for i in range(len(a2)):
        mm *= int(a2[i])
    print ('произведение чисел вашего числа =', mm)

sum_a2()
mult_a2()
