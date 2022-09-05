a = input('Введите операцию: ')
x = int(input("Введите первое число: "))
y = int(input('Введите второе число: '))

def sum(x,y):
    print(x+y)
def razn(x,y):
    print(x-y)
def proiz(x,y):
    print(x*y)
def chast(x,y):
    if y == 0:
        print('Деление на ноль!')
    else:
        print(x/y)
if a == '+':
    print(sum(x,y))
elif a == '-':
    print(razn(x,y))
elif a == '*':
    print(proiz(x,y))
else:
    print(chast(x,y))


