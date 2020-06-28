# Factorial Recursion
def recursion(num):
    if num == 0:
        return 1
    else:
        return num * recursion(num - 1)


print(recursion(5))
