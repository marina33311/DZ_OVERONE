class W1:
    def __init__(self):
        self.n = 3

    def total(self, a):
        return self.n + int(a)


class W2:
    def __init__(self):
        self.string = 'Hello'

    def total(self, a):
        return len(self.string + str(a))


w1 = W1()
w2 = W2()

print(w1.total(15))  #Вывод: 18
print(w2.total(15))  #Вывод 7