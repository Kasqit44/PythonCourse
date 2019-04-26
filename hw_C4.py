a = float(input('Введите старший коэффициент (а) '))
b= float(input('Введите средний коэффициент (b) '))
c = float(input('Введите свободный член(с) '))
def quadratic_equation(a, b, c):
    discr = (b**2)-4*a*c
    
    if discr<0:
        print ('Корней нет')
    elif discr==0:
        x = -b/(2*a)
        print ('единственный корень уравнения равен', x)
    else:
        x1 = (-b+(discr**0.5))/(2*a)
        x2 = (-b-(discr**0.5))/(2*a)
        print (f'x1=:{x1}, x2=:{x2}')
    
quadratic_equation(a, b, c)