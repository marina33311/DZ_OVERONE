import string

class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = list(letters)

    def __repr__(self):
        return repr(self.letters)

    def letters_num():
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__(lang='En', letters=string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return type(self).__letters_num

    @staticmethod
    def example():
        print('English Example:\nSaying and doing are two things.')


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    print(eng_alphabet)
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()