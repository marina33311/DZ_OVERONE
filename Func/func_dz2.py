p = [1,2,3,4, 'a', 'b']
print(type(p))
def tup(p):
    for item in p:
       if type(item) == str:
           print(len(item))
def lis(p):
    print('букв', len(list(filter(lambda x: type(x) == str, p))), 'чисел',
          len(list(filter(lambda x: type(x) in (int, float), p))))

def st(p):
    print('букв', len(p) - p.count(" "))

if type(p) == tuple:
    tup(p)
elif type(p) == list:
    lis(p)
elif type(p) == str:
    st(p)
else:
    print('Неизвестный тип')






