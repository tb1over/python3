# -*- coding:utf-8 -*-


# 可变参数求和函数
def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax


# 不需要立即求和，返回求和函数
def lazy_sum(*args):
    def my_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return my_sum

# f = lazy_sum(1, 2, 3, 4)
# print(f)        # 输出lazy_sum函数的地址

# print(f())      # 输出f函数调用的结果

'''
闭包(Closure):返回的函数在其内部引用了外部的局部变量args,
所以，当一个函数返回了一个函数之后，其内部的局部变量还被新函数引用，
'''


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

'''
匿名函数:lambda 表示匿名函数
'''
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
# print(L)


# 返回函数
def return_func1(x, y):
    def g():
        return x**2 + y**2
    return g


# 返回lambda匿名函数
def return_func2(x, y):
    return lambda: x ** 2 + y ** 2

f1 = return_func1(1, 2)
f2 = return_func2(2, 4)

print(f1())
print(f2())


