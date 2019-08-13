import hashlib
import string
letters = string.punctuation + string.ascii_letters + string.digits


class Hashlib:

    def __init__(self):
        self.c = hashlib.sha512()

    def start_pass(self, pwd):
        pwd = bytes(pwd, 'utf-8')
        self.c.update(pwd)
        return self.c.hexdigest()



def set_ascii_num(num):
    text = ''
    if num > 93:
        while num > 93:
            #text = '!'
            num, rest = divmod(num, 94)
            text += letters[rest]
            print(text, rest, num)
    text += letters[num]
    print(text, '####')
    # if num <= 93:
    #     return letters[num]
    # else:
    #     x, y = divmod(num, 94)
    #     z = ''
    #     i = 0
    #     while i < int(x):
    #         z += letters[93]
    #         i += 1
    #     z += letters[y]
    #     return z


def get_ascii_num(num):
    z = 1
    if num.__len__() == 1:
        z = 0
    for ni in range(0, num.__len__()):
        i = 0
        for li in letters:
            if num[ni] == li:
                z += i
            i += 1
    return z


h = Hashlib()
print(hashlib.algorithms_available)
# 1 = " ... 93 = 9 94 = "!
print(letters)
print(set_ascii_num(96), get_ascii_num('!'))
# A >bytes> 1 >my alfabet> ?? >bytes> 1 >int> 1 >bin> 1 xor key
# 1 xor key >int> 1 >bytes> ?? >my alfabet> 1 >bytes> A
