# -*- coding:utf-8 -*-


"""
__str__  __repr__
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__      # __repr__返回的是程序员看到的字符串

# print(Student('chenchen'))

"""
__iter__   __next__
"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self         # 实例本身就是可迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a       # 返回下一个值

    def __getitem__(self, item):    # 类似于list , 以下标形式取得元素
        if isinstance(item, int):   # item是下标
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):     # item是切片
            start = item.start
            stop = item.stop            # step参数没有处理
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

# for n in Fib():
#     print(n)

# f = Fib()
# print(f[3])
# print(f[0:5:2])

# __getattr__ 例子


class Student(object):

    def __init__(self):
        self.name = 'chenchen'

    def __getattr__(self, item):
        if item == 'score':
            return 100                  # score属性, 返回100
        if item == 'age':
            return lambda: 25           # age属性,返回一个lambda匿名函数
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
        # 让class只响应几个属性，其他的抛出属性异常

s = Student()
print(s.name)
print(s.score)        # 属性不存在，报错
print(s.age)
print(s.age())
print(s.abc)          # 属性异常，不存在
