vowel = 'аяуюоеёэиы'

class Test:
    def __init__(self):
        pass

    def first(self, item):
        if isinstance(item, str):
            vowelQuan = 0
            vowels = ''
            consonants = ''
            for i in item:
                if i in vowel:
                    vowelQuan += 1
                    vowels += i
                else:
                    consonants += i
            if vowelQuan * (self.second(item) - vowelQuan) <= self.second(item):
                print(vowels)
            else:
                print(consonants)
        elif isinstance(item, int):
            sum = 0
            for i in str(item):
                if int(i) % 2 == 0:
                    sum += int(i)
            print(sum * self.second(str(item)))
    def second(self, item):
        return len(item)

if __name__ == '__main__':
    obj1 = Test()
    obj1.first(34567)
    obj2 = Test()
    obj2.first('Привет!')
