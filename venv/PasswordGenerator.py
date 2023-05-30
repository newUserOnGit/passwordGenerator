import random
import string
import numpy
from itertools import chain
from random import Random


class PasswordGenerator():
    ready_password = ''
    list_password = []
    while True:
        try:
            pwd_length = int(input(
                'Укаэите длину необходимого пароля: '))
            pwd_digith = True if input(
                'В пароле должны присутствовать цифры? (Y - да, N - нет)') == 'y' else False
            pwd_uppercase = True if input(
                'В пароле должны присутствовать заглавные буквы? (Y - да, N - нет)') == 'y' else False
            pwd_lowercase = True if input(
                'В пароле должны присутствовать маленькие буквы? (Y - да, N - нет)') == 'y' else False
            pwd_punctuation = True if input(
                'В пароле должны присутствовать символы? (Y - да, N - нет)') == 'y26' else False
        except ValueError:
            continue
        break



    def generation_symbosl(self):
        if self.pwd_digith:
            self.list_password.append([random.randrange(0, 10, 1) for i in range(self.pwd_length)])
        if self.pwd_lowercase:
           self.list_password.append([chr(random.randint(ord('a'), ord('z'))) for i in range(self.pwd_length)])
        if self.pwd_uppercase:
            self.list_password.append([chr(random.randint(ord('A'), ord('Z'))) for i in range(self.pwd_length)])
        if self.pwd_punctuation:
            self.list_password.append([random.choice(string.punctuation) for i in range(self.pwd_length)])

        self.list_password = list(chain.from_iterable(self.list_password))


    def create_password(self):
        list_password = numpy.array(self.list_password)
        self.ready_password = ''.join(random.choice(list_password) for i in range(0, self.pwd_length))

    def main(self):
        self.generation_symbosl()
        self.create_password()
        print(self.ready_password)

if __name__ == '__main__':
    start = PasswordGenerator()
    start.main()