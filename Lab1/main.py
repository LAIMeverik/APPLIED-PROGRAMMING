a = int(input())
b = int(input())


def absolute(param):
    if param < 0:
        param = -param
    return param


def maximum(param1, param2):
    if param1 < param2:
        return param2
    else:
        return param1


def minimum(param1, param2):
    if param1 < param2:
        return param1
    else:
        return param2


print(a + b)
print(a - b)
print(a * b)
print((a + b) / 2)
print(maximum(absolute(a), absolute(b)) - minimum(absolute(a), absolute(b)))