lst = [5, 10, 20, 40, 80]
sq_lst = []


def sqr(lst):
    for i in lst:
        sq_lst.append(i ** 2)
    return sq_lst


def sqr2(itm):
    return itm ** 2


dirSqr = lambda x: x ** 2

print(sqr(lst))

sq_fn_list = []

print(list(map(sqr2, lst)))
print(list(map(dirSqr, lst)))
