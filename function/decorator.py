# -*- coding:utf-8 -*-
import functools

# def now():
#    print('2016-12-14')

# f = now
# f()     # 调用变量f指向的函数

# 函数对象有一个__name__属性，可以得到函数的名字
# print(now.__name__)
# print(f.__name__)

'''
装饰器(decorator)：假设想增强以上now函数的功能，但是又不想修改now函数的定义
这种在运行期间动态增加功能的方式，称之为装饰器
'''


def log(func):
    def wrapper(*args, **kw):
        print('call %s() ' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log        # @log相当于执行了now = log(now)
def date():
    print('2016-12-14')

# print('name:', date.__name__, date)
# date()
'''
date()将会执行log返回的新的函数,即wrapper函数,首先打印日志，然后再调用原始函数
'''


def year():
    print('2016')

# print('name:', year.__name__, year)     # 注意与上一条输出的区别

'''
如果decorator本身需要传递参数，那就需要编写一个返回decorator的高阶函数
比如，自定义log的文本
'''


def ex_log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('###START### %s %s() :' % (text, func.__name__))
            ret = func(*args, **kw)
            print("###END###")
            return ret
        return wrapper
    return decorator


@ex_log('DEBUG')
def month():
    print('12')


month()
# print(month.__name__)
'''
以上等价于 month = ex_log('excute')(now)
1.执行ex_log('excute'),返回decotator函数
2.再调用返回的decorator函数，参数是now函数，返回值最终是wrapper函数
3.问题是，经过decorator装饰后的函数，它们的__name__已经从原来的date/month变成了wrapper
  因为最终返回的是wrapper函数,所以，需要把原始函数的__name__等属性复制到wrapper函数中
  利用Python内置的functools.wraps , 只需在定义wrapper的前面加上functools.wraps(func)
'''



