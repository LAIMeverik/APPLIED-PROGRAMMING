a = int(input())
b = int(input())


def Abs(a):
    if a < 0:
        a = -a
    return a


def Max(a, b):
    if a < b:
        return b
    else:
        return a


def Min(a, b):
    if a < b:
        return a
    else:
        return b


print(a + b)
print(a - b)
print(a * b)
print((a + b) / 2)
print(Max(Abs(a), Abs(b)) - Min(Abs(a), Abs(b)))