import random
q1= ('чётное','четное','чётное?','четное?')
q2= ('нечётное','нечетное', 'нечетное?', 'нечётное?' )
q3= ('2', 'два', 'двум','2?', 'два?', 'двум?')
q4= ('3', 'три', 'трём','3?', 'три?', 'трём?', 'трем', 'трем?')
q5= ('4', 'четыре', 'четырём','четырем', '4?', 'четыре?', 'четырем?', 'четырём?')
q6= ('5', 'пять', 'пяти','5?', 'пять?', 'пяти?')
q7= ('7', 'семь', 'семи','7?', 'семь?', 'семи?')
q8= ('9', 'девять', 'девяти','9?', 'девять?', 'девяти?')
q9= ('10', 'десяти', 'десять','10?', 'десять?', 'десяти?')
q10= ('11', 'одиннадцать', 'одиннадцати','11?', 'одиннадцать?', 'одиннадцати?')
q11 = ('простое','простым','простому','простое?','простым?','простому?')
a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
r = random.randint(1,200)
n = 0
A = ['Твоё число меньше моего',
     'Твой лік меньш за мой',
     'Your number is less than mine',
     'Twoja liczba jest mniejsza od mojej',
     'Deine Nummer ist weniger als meine',
     'Tu numero es menor que el mio',
     'Ton nimbre est inférieur au mien',
     'Tua numerus est minor quam mea',
     '你的号码比我的少',
     'رقمك أقل من لي',
     'Боюсь, что ты проиграл... Давай начнём сначала!']
B = ['Твоё число больше моего',
     'Твой лік большы за мой',
     'Your number is greater than mine',
     'Twoja liczba jest większa od mojej',
     'Deine Nummer ist größer als meine',
     'Tu numero es mayor que el mio',
     'Ton nombre est supérieur au mien',
     'Tua numerus est major quam mea',
     '你的人数比我多',
     'رقمك أكبر من لي',
     'Боюсь, что ты проиграл... Давай начнём сначала!']

print ('Давай сыграем в игру!\nЯ загадаю число от 1 до 200. Ты можешь задать о нём три вопроса, на которые\nя смогу ответить ДА или НЕТ. \n(Не задавай вопросы типа "больше/меньше ли число чего-то" Эти подсказки я тебе и сам дам!) \nДальше попробуй его угадать.\nНо будь осторожен! Мои подсказки с каждой новой попыткой будут усложняться.')
quest1 = input()

def check1():
    que1 = quest1.split()
    for i1 in q1:
        for j1 in que1:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
                    
           
    for i1 in q2:
        for j1 in que1:
            if i1==j1:
                if r%2 == 0:
                    print ('НЕТ')
                    check2()
                    return
                else:
                    print ('ДА')
                    check2()
                    return
    for i1 in q3:
        for j1 in que1:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q4:
        for j1 in que1:
            if i1==j1:
                if r%3 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q5:
        for j1 in que1:
            if i1==j1:
                if r%4 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q6:
        for j1 in que1:
            if i1==j1:
                if r%5 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q7:
        for j1 in que1:
            if i1==j1:
                if r%7 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q8:
        for j1 in que1:
            if i1==j1:
                if r%9 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q9:
        for j1 in que1:
            if i1==j1:
                if r%10 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    for i1 in q10:
        for j1 in que1:
            if i1==j1:
                if r%11 == 0:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
    
    for i1 in q11:
            if quest1.count(i1) == 1:
                    
                if a.count(r)== 1:
                    print ('ДА')
                    check2()
                    return
                else:
                    print ('НЕТ')
                    check2()
                    return
            else:
                print ('Я не могу ответить на этот вопрос') # т.к. это последний из возможных для робота вопросов, если и в этом случае он не находит ничего похожего
                check2()                                    # на какой-то из его 11 вариантов, он отчаивается и говорит, что не может ответить на ваш вопрос:)
                return
    
#если он по всему циклу не находит совпадений, он идёт на следующий цикл(=вопрос) и т.д. на последнем вопросе зададим исход "не могу ответить" (поскольку прогнал всё и совпадений не нашёл)
#переход на вводимый вопрос 2 будем осуществлять внутри цикла (перейдет тот цикл, который ответит)
def check2():
    quest2 = input()
    que2 = quest2.split()
    for i1 in q1:
        for j1 in que2:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
                    
           
    for i1 in q2:
        for j1 in que2:
            if i1==j1:
                if r%2 == 0:
                    print ('НЕТ')
                    check3()
                    return
                else:
                    print ('ДА')
                    check3()
                    return
    for i1 in q3:
        for j1 in que2:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q4:
        for j1 in que2:
            if i1==j1:
                if r%3 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q5:
        for j1 in que2:
            if i1==j1:
                if r%4 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q6:
        for j1 in que2:
            if i1==j1:
                if r%5 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q7:
        for j1 in que2:
            if i1==j1:
                if r%7 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q8:
        for j1 in que2:
            if i1==j1:
                if r%9 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q9:
        for j1 in que2:
            if i1==j1:
                if r%10 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    for i1 in q10:
        for j1 in que2:
            if i1==j1:
                if r%11 == 0:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
    
    for i1 in q11:
            if quest2.count(i1) == 1:
                    
                if a.count(r)== 1:
                    print ('ДА')
                    check3()
                    return
                else:
                    print ('НЕТ')
                    check3()
                    return
            else:
                print ('Я не могу ответить на этот вопрос') 
                check3()                                    
                return

def check3():
    quest3 = input()
    que3 = quest3.split()
    for i1 in q1:
        for j1 in que3:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
                    
           
    for i1 in q2:
        for j1 in que3:
            if i1==j1:
                if r%2 == 0:
                    print ('НЕТ')
                    return
                else:
                    print ('ДА')
                    return
    for i1 in q3:
        for j1 in que3:
            if i1==j1:
                if r%2 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q4:
        for j1 in que3:
            if i1==j1:
                if r%3 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q5:
        for j1 in que3:
            if i1==j1:
                if r%4 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q6:
        for j1 in que3:
            if i1==j1:
                if r%5 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q7:
        for j1 in que3:
            if i1==j1:
                if r%7 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q8:
        for j1 in que3:
            if i1==j1:
                if r%9 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q9:
        for j1 in que3:
            if i1==j1:
                if r%10 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    for i1 in q10:
        for j1 in que3:
            if i1==j1:
                if r%11 == 0:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
    
    for i1 in q11:
            if quest3.count(i1) == 1:
                    
                if a.count(r)== 1:
                    print ('ДА')
                    return
                else:
                    print ('НЕТ')
                    return
            else:
                print ('Я не могу ответить на этот вопрос') 
                return
check1()

def randon():
    for z in range(11):
        n = int(input())
        if n<r:
            print (A[z])
        elif n>r:
            print (B[z])
        else:
            print ('Ты угадал! Поздравляю!!!:)')
            break
randon()        

