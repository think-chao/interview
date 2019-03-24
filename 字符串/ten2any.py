# coding:utf-8

from string import digits, ascii_lowercase, ascii_uppercase

Alphabet = digits + ascii_uppercase + ascii_lowercase


def ten2any(n, base=62):
    assert base <= 62
    n, index = divmod(n, base)
    if n > 0:
        return ten2any(n, base) + Alphabet[index]
    else:
        return Alphabet[index]


def any2ten(s, base=10):
    """
    :param s: 'ac2'
    :param base:
    :return:
    """
    n = 0
    for i, c in enumerate(reversed(s)):
        index = Alphabet.index(c)
        n += index * pow(base, i)
    return n


if __name__ == '__main__':
    print(ten2any(15, 7))
    print(any2ten('z'))
