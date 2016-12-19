# -*- coding:utf-8 -*-


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)

# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))


'''
通过type 函数创建类
创建class的定义是在运行时动态创建的，而创建class的方法就是使用type()函数
'''


def fn(self, name='world'):
    print('hello, %s.' % name)

MyHello = type('MyHello', (object,), dict(hello=fn))

'''
要创建一个class对象，type()函数需要传递3个参数：
1. class的名称
2. 继承的父类集合，python支持多重继承，如果只有一个父类，注意tuple的单元素写法
3. class的方法名称与函数绑定，这里把fn绑定到方法名hello上。
'''
h = MyHello()
h.hello()
print(type(MyHello))
print(type(h))

