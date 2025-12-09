# list1=[1,2,3,4]
# print(list1[-1::-1])
# print(list1[::-1])
# print(list1[-1:0:-1])
# print(list1[-1:1:-1])
# dict([('a',1),('b',2),('c',3)])
# print(dict([('a',1),('b',2),('c',3)]))
# # print(dict([('a',1),('b',2),('c',3)]))
# x = bytes("hello", encoding="utf-8")
# print(x) #b'hello'
# y = x[1:3]
# print(y) #b'el'
# z= x + b'world'
# print(z) #b'helloworld'
# x = b'hello'
# if x[0] == ord('h'):
#     print("True") #Truew
# firstName = 'senhuang'
# lastName = "wang"
# print(type(firstName))#<class 'str'>
# print(type(lastName))#<class 'str'>
# print(f"uppername:{firstName.upper()} {lastName.upper()}")#uppername:SENHUANG WANG
#控制小数位数
# pi = 3.141592653589793
# print(f"{pi:.2f}")#3.14w
# 对齐文本
# name = "senhuang"
# print(f"name:{name:>10}")#右对齐，宽度为10 name:  senhuang
# print(f"name:{name:<10}")#左对齐，宽度为10 name:senhuang
# print(f"name:{name:^10}")#居中对齐，宽度为10 name: senhuang
# #调用函数或方法
# def greet(name):
#     return f"Hello, {name}!"
# print(f"{greet('Alice')}")#Hello, Alice!
# #如不使用f-string，原型为
# def greet2(name):
#     return "Hello, " + name +"!"
# print(greet2('Alice'))#Hello,Alice
# a = 20
# b = 20
# if a is b:
#     print("a和b有相同的标识")
# else:
#     print("a和b没有相同的标识")#a和b有相同的标识
# a = 30
# if a is b:
#     print("a和b有相同的标识")
# else:
#     print("a和b没有相同的标识")#a和b没有相同的标识

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum += counter
#     counter += 1
# print(f"1到{n}之和为{sum}")

# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:
#     print(f"当前水果:{fruit}")
# sequence = [x**2 for x in range(10)]
# print(sequence)#0,1,4,9,16,25,36,49,64,81

# sequence = [x**2 for x in range(10) if x % 2 == 0]
# print(sequence)#0,4,16,36,64

# multiplication_table = [i * j for j in range(1, 6) for i in range(1, 6)]
# print(multiplication_table)

# multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
# print(multiplication_table)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# print("Last fruit:", fruit)  # 输出: Last fruit: cherry
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(f"第{i + 1}个网站是{a[i]}")
#     print(i + 1,a[i])

# i = 231*123
# j = 123*231
# # print("i的值为：",i,j)#逗号分隔输出

# # print("i的值为：%d" % i)#%格式化输出
# # print("i的值为：%d,j的值为：%d" %(i,j))#%格式化输出

# # print("i的值为：{}".format(i))#str.format()格式化输出
# # print("i的值为：{},j的值为：{}".format(i,j))#str.format()格式化输出

# print(f"i的值为：{i}")#f-string格式 化输出
# print(f"i的值为：{i},j的值为：{j}")#f-string格式化输出
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
# new_names = [name.upper() for name in names if len(name) > 3]
# print(new_names)
# listdemo = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
# newdict = {name:len(name) for name in listdemo}
# print(newdict)
# #{'Alice': 5, 'Bob': 3, 'Charlie': 7, 'David': 5, 'Eve': 3, 'Frank': 5, 'Grace': 5, 'Heidi': 5, 'Ivan': 4, 'Judy': 4}
# newset = {x**2 for x in range(10)}
# # print(newset)
# # # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# a = (x for x in range(10))
# print(a)#<generator object <genexpr> at 0x000001F3D3D3A7C8>
# tuple1 = tuple(a)#将生成器转换为元组
# tuple2 = tuple(a)#生成器已经被消耗，无法再次转换为元组
# print(tuple1)#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(tuple2)#()

# import sys

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# #直接调用next()函数
# print(next(it))#1
# print(next(it))#2
# print(next(it))#3
# print(next(it))#4
# #print(next(it))#StopIteration
# #使用for循环
# it1 = iter(list)
# for x in it1:
#     print (x, end=" ")#无
# #使用while循环
# #无输出，因为迭代器已经被消耗
# while True:
#     try:
#         print (next(it))
#     except StopIteration:
#         sys.exit()
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))#1
# print(next(myiter))#2
# print(next(myiter))#3
# print(next(myiter))#4
# print(next(myiter))#5
# print(next(myiter))#StopIteration
# print(iter(myiter))#<__main__.MyNumbers object at 0x000001F3D3D3A7C8>
# def countdown(n):
#     print("Counting down from", n)
#     while n > 0:
#         yield n
#         n -= 1
#     return

# generator = countdown(5)
# print(generator)#<generator object countdown at 0x0000020D3B2E9AC8>
# print(next(generator))#Counting down from 5 5
# print(next(generator))#4
# print(next(generator))#3

# for i in generator:
#     print(i)#2 1
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         print(f"生成器内部:counter={counter}")  # 调试输出
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1

# f = fibonacci(10)

# try:
#     while True:
#         print(next(f), end=" ")
# except StopIteration:
#     print("\n生成器已结束")
# #生成器内部：counter=0
# #0 生成器内部：counter=1
# #1 生成器内部：counter=2
# #1 生成器内部：counter=3
# #。。。。
# #生成器内部：counter=11
# #生成器已结束
# def printinfo(name,age=35):
#     print(f"name:{name},age:{age}")
#     return

# printinfo("mike")#name:mike,age:35

# a = [1,2,3,4,5]
# print(a)#1,2,3,4,5
# a = "hello"
# # print(a)#hello
# def change(a):#形参
#     print(id(a))#形参id
#     a = 10#修改形参
#     print(id(a))#修改后的形参id

# a = 1
# print(id(a))#140732674004352#实参id
# change(a)#140732674004352 140732674004672
# print(id(a))#140732674004352#实参id
# # #在调用函数前后，形参和实参实际指向的是同一个对象，在函数内部修改形参后，形参指向了不同的id
# def change(a):
#     print(id(a))#形参id
#     a[0] = 10#修改形参
#     print(id(a))#修改后的形参id

# a = [1,2,3,4,5]
# print(id(a))#140732674004352
# change(a)#140732674004352 140732674004352
# print(id(a))#140732674004352
# #在函数内部修改形参后，形参指向的id没有发生变化

# def printme(str):
#     print(str)

# printme()
# # #TypeError: printme() missing 1 required positional argument: 'str'

# def printme(arg1, *vartuple):
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# printme(10)
# #输出:  10
# printme(10,20,30)
# #输出:  10
# #20
#30

# def printme(arg1, **vardict):
#     print("输出: ")
#     print(arg1)
#     for key in vardict:
#         print(f"{key}:{vardict[key]}")
#     return
# printme(1,a=2,b=3)
# #输出:
# #1
# # #{'a': 2, 'b': 3}

# def printme(arg1,arg2,*,arg3):
#     print("输出: ")
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     return
# printme(1,2,arg3=3)#输出: 1 2 3
# printme(1,2,3)#TypeError: printme() takes 2 positional arguments but 3 were given

#lambda函数语法
# # lambda [arg1 [,arg2,.....argn]]:expression
# lambada = lambda x,y:x+y
# print(lambada(1,2))#3

# def creatlamda(n):
#     return lambda x:x*n

# f = creatlamda(2)
# g = creatlamda(3)
# print(f(2))#4
# print(g(2))#6

# def sum(arg1,arg2):
#     total = arg1 + arg2
#     print(f"函数内: {total}")
#     return total

# total = sum(10,20)
# print(f"函数外: {total}")
# #函数内: 30
# #函数外: 30
# def f(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)
# print("hello world")
# # f(10,20,30,d=40,e=50,f=60)#10 20 30 40 50 60
# # #f(10,20,c=30,d=40,e=50,f=60)#TypeError: f() got some positional-only arguments passed as keyword arguments: 'c'
# # f(10,20,30,40,e=50,f=60)#10 20 30 40 50 60
# # f(10,20,30,40,50,60)#TypeError: f() takes 4 positional arguments but 6 were given

# f = lambda :print("hello world")
# #lambda函数没有参数，返回一个函数对象
# print(f())#hello world None

# #以上代码等价于
# def f():
#     return print("hello world")
# #返回值为None
# #hello world None
# #修复方法lambda
# f  = lambda : "hello world"
# print(f())#hello world

#lambda函数通常与内置函数如map（）、filter（）和reduce（）一起使用，以便在集合上操作
#使用map函数计算一个序列的平方
# # map()函数
# # map()函数接受两个参数，一个是函数，一个是序列，map()函数将序列中的每个元素传递给函数，返回一个包含结果的列表
# numbers = [1,2,3,4,5]
# squared = list(map(lambda x:x**2,numbers))
# print(squared)#1,4,9,16,25
# #使用 lambda 函数与 filter() 一起，筛选偶数

#filter()函数原理：对序列中的每个元素应用函数，返回包含使函数返回True的元素的序列
# #filter()函数作用:过滤序列，返回由符合条件的元素组成的新序列
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x:x%2==0,numbers))
# print(even)#2,4,6,8,10

# #使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积
# #reduce()函数原理：对序列中的每个元素应用函数，返回一个值
# #reduce()函数作用：对序列中的元素进行累积计算
# # from functools import reduce#需从functools模块导入reduce函数
# # numbers = [1,2,3,4,5]
# # product = reduce(lambda x,y:x*y,numbers)#1*2*3*4*5
# # print(product)#120
# #使用普通函数计算一个序列的累积乘积
# from functools import reduce
# def multiply(x,y):
#     return x*y
# numbers = [1,2,3,4,5]
# product = reduce(multiply,numbers)#1*2*3*4*5
# print(product)#120

# def before_call_code():
#     print("===== 函数调用开始 =====")

# def after_call_code():
#     print("===== 函数调用结束 =====")

# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):
#         # 调用原始函数前的逻辑
#         before_call_code()  
        
#         # 执行原始函数并获取结果
#         result = original_function(*args, **kwargs)  
        
#         # 调用原始函数后的逻辑
#         after_call_code()  
        
#         return result
#     return wrapper  # 返回包装后的函数

# @decorator_function
# def target_function(a, b):
#     print(f"执行加法：{a} + {b}")
#     return a + b
# #target_function = decorator_function(target_function)
# #等同于语法糖@decorator_function

# # 调用装饰后的函数
# result = target_function(3, 5)#实际调用的是wrapper函数
# print("结果：", result)
# # ===== 函数调用开始 =====
# # 执行加法：3 + 5
# # ===== 函数调用结束 =====
# # 结果： 8

# def repeat(n):#工厂函数，定义外层装饰器函数，返回装饰器函数
#     def decorator(func):#定义装饰器函数，返回wrapper函数
#         def wrapper(*args, **kwargs):#定义wrapper函数，实现装饰逻辑
#             for _ in range(n):#循环n次#_表示一个临时变量，不会被使用
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(3)#等同于repeat(3)(target_function)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")#Hello, Alice!Hello, Alice!Hello, Alice!

# #闭包，实现计数器
# def counter_factory(initial = 0):#外层函数
#     count = initial #外层函数变量
#     def increment(): #内层函数
#         nonlocal count #声明count为非局部变量
#         count += 1
#         return count
#     return increment #返回内层函数 

# counter1 = counter_factory(0)#调用外层函数，返回内层函数
# print(counter1())#1
# print(counter1())#2

# counter2 = counter_factory(0)#调用外层函数，返回内层函数
# print(counter2())#1
# print(counter2())#2

# #函数工厂

# def create_multiplier(n):
#     def multiplier(x):
#         return x ** n
#     return multiplier

# square = create_multiplier(2)
# cube = create_multiplier(3)

# print(square(2))#4
# print(cube(2))#8

# text = "   Hello, World!   "
# clean_text = text.strip().lower().replace("world", "Python")
# #执行顺序strip()-->lower()-->replace()
# print(clean_text)  # 输出 "hello, Python!"

# class Calculate:
#     def __init__(self,value):
#         self.value = value

#     def add(self, value):
#         self.value += value
#         return self#返回实例对象以支持链式调用
    
#     def multiply(self, value):
#         self.value *= value
#         return self

# #链式调用
# result = Calculate(5).add(3).multiply(2).value
# # print(result)#16

# #柯里化前案例
# def add(x,y,z):
#     return x + y + z
# print(add(1,2,3))#6

# #柯里化后案例
# def add(x):
#     def add_y(y):
#         def add_z(z):
#             return x + y + z
#         return add_z
#     return add_y
# print(add(1)(2)(3))#6

# #分步处理用户请求
# def process_request(base_url):
#     def set_endpoint(endpoint):
#         def send_request(params):
#             url = f"{base_url}/{endpoint}"
#             print(f"请求 {url}，参数：{params}")
#             # 实际发送请求...
#         return send_request
#     return set_endpoint

# # 配置基础 URL
# api = process_request("https://api.example.com")

# # 配置端点
# user_api = api("users")

# # 发送请求
# user_api({"id": 123})  # 请求 https://api.example.com/users，参数：{'id': 123}

# #复用函数逻辑
# def curried_round(ndigits):
#     def round_number(x):
#         return round(x, ndigits)
#     return round_number

# # 生成保留两位小数的函数
# round_to_two = curried_round(2)
# print(round_to_two(3.14159))  # 输出 3.14

# # 生成保留整数部分的函数
# round_to_int = curried_round(0)
# print(round_to_int(3.14159))  # 输出 3

# def muplitplier(n):
#     return lambda x : x * n

# double = muplitplier(2)
# triple = muplitplier(3)

# print(double(2))#4
# print(triple(2))#6

# from functools import partial

# def add(a, b, c):
#     return a + b + c

# add_5 = partial(add, 2, 3)  # 固定 a=2, b=3
# print(add_5(4))  # 输出 9 (2+3+4)

# def curry(func):
#     def curried(*args):
#         if len(args) >= func.__code__.co_argcount:#判断参数个数是否满足
#             return func(*args)#满足则调用原函数
#         return lambda *more_args: curried(*(args + more_args))#不满足则返回新函数
#     return curried

# @curry
# def add(a, b, c):
#     return a + b + c

# print(add(1)(2)(3))        # 输出 6
# print(add(1, 2)(3))        # 输出 6
# print(add(1)(2, 3))        # 输出 6
# def func(*arg):
#     print(arg)
# func(1,2,3)#(1,2,3)#元组
# def func(**arg):
#     print(arg)
# # func(a=1,b=2,c=3)#{'a':1,'b':2,'c':3}#字典

# args = (1,2,3)
# print(*args)#1,2,3
# args = {'a':1,'b':2,'c':3}
# #print(**args)#报错
# print(args)#输出{'a': 1, 'b': 2, 'c': 3}

# def greet(name, age, greeting="Hello"):
#     print(f"{greeting}, {name}! You are {age} years old.")

# # 创建一个字典，包含函数所需的关键字参数
# kwargs = {"name": "Alice", "age": 30}

# # 使用 ** 解包字典并传递给函数
# greet(**kwargs)  # 等价于 greet(name="Alice", age=30)

# #类装饰器
# class Decorator:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print("调用前")
#         result = self.func(*args, **kwargs)
#         print("调用后")
#         return result
# @Decorator#等同于target_function = Decorator(target_function)
# def target_function():
#     print("执行目标函数")
    
# target_function()

# #创建一个空栈
# stack = []

# #压入操作
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)#[1,2,3]

# #弹出操作
# topElement = stack.pop()
# print(topElement)#3
# print(stack)#[1,2]

# #查看栈顶元素
# topElement = stack[-1]
# print(topElement)#2

# #检查是否为空
# is_Empty = len(stack) == 0
# print(is_Empty)#False

# #获取栈的大小
# size = len(stack)
# print(size)#2

# from collections import deque

# #创建一个空队列
# queue = deque()
# #向队尾添加元素
# queue.append(1)
# queue.append(2)
# queue.append(3)

# print(queue)#deque([1,2,3])

# #从队首弹出元素
# topElement = queue.popleft()
# print(topElement)#1
# print(queue)#deque([2,3])

# #查看队首元素(不移除)
# from_element = queue[0]
# print(from_element)#2

# #检查队列是否为空
# is_Empty = len(queue) == 0
# print(is_Empty)#False

# #获取队列的大小
# size = len(queue)
# print(size)#2

# var = [2,3,4]
# varlist = [x*2 for x in var]
# print(varlist)#[4,6,8]

# varlist2 = [[x,x*2] for x in var]
# print(varlist2)#[[2,4],[3,6],[4,8]]

# fruits = ['  apple ', '  banana', '            cherry']
# varlist3 = [weapon.strip() for weapon in fruits]
# print(varlist3)#['apple','banana','cherry']

# var2 = [3,4,5]
# varlist4 = [x * y for x in var for y in var2]
# print(varlist4)#[6,8,10,8,12,16,10,15,20]
# varlist5 = [x + y for x in var for y in var2]
# print(varlist5)#[5,6,7,6,7,8,7,8,9]
# varlist6 = [var[i] * var2[i] for i in range(len(var))]
# print(varlist6)#[6,12,20]
# #行列转换方式1
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix2 = [[row[i] for row in matrix] for i in range(4)]
# print(matrix2)#[[1,5,9],[2,6,10],[3,7,11],[4,8,12]]
# #行列转换方式2
# matrix3 = []
# for i in range(4):
#     matrix3.append([row[i] for row in matrix])
# print(matrix3)
# #行转列方式3
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# import sys

# print('命令行参数如下')
# for i in sys.argv:
#     print(i)

# print(f"路径为:{sys.path}")

# def func1():
#     import support
#     support.print_func("world")#Hello,world
# func1()#正常输出，模块处于函数作用域
# print(support.print_func("world"))#显示support未定义

# def func():
#     print("local func")
# #     return


# #Filename:support.py
# def print_func(par):
#     print(f"Hello,{par}")
#     return

# #方式2：from ... import ...导入
# def print_func(par):
#     print(f"ok,{par}")
#     return

# import support
# from support import *

# print_func("world")#输出hello,world
# support.print_func("world")#输出hello world
a = [1, 2, 3, 4, 5]

# import support
# func = support.func
# print(dir()) # 得到一个当前模块中定义的属性列表
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
# a = 5 # 建立一个新的变量 'a'
# print(dir())
# ['__builtins__', '__doc__', '__name__', 'a', 'sys']
# del a # 删除变量名a
# print(dir())
# ['__builtins__', '__doc__', '__name__', 'sys']

# f = open(r"C:\Users\8381599\Desktop\7100BI.txt","r",encoding = 'utf-8')
# fi = open(r"C:\Users\8381599\Desktop\7100BI.txt","r",errors = 'ignore')
# data = f.read()
# date2 = fi.read()
# print(data)
# print(fi)
# f.close()
# import chardet

# with open(r"C:\Users\8381599\Desktop\7100BI.txt", "rb") as f:
#     raw_data = f.read()
#     result = chardet.detect(raw_data)
#     encoding = result["encoding"]
#     print(f"检测到编码: {encoding}")

#     text = raw_data.decode(encoding)
#     print(text)
# with open(r"C:\Users\8381599\Desktop\7100BI.txt", "r",encoding='utf-8') as f:
#     data = f.read()
#     print(data)
# # 文件会在 with 块结束后自动关闭
#!/usr/bin/python3
 
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num) 
#     num = 123
#     print(num)
# fun1()
# print(num)
# #1
# #123
# #123
#!/usr/bin/python3
 
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()
# # #100
# # #100
# a = 10
# def printinfo(a):
#     a+=1
#     print(a)
#     return a
# printinfo(a)#局部变量a=11
# # print(a)#全局变量a=10
# num1 = float(input("输入第一个数字:"))
# num_sqrt = num1 ** 0.5
# # print('%0.3f 的平方根为%0.3f'%(num1,num_sqrt))
# import cmath

# def get_float_input(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except:
#             print("请输入有效数字")

# def solve_quadratic(a,b,c):
#     discriminant = b**2 - 4*a*c
#     root1 = (-b + cmath.sqrt(discriminant)) / 2 * a
#     root2 = (-b - cmath.sqrt(discriminant)) / 2 * a
#     return root1,root2

# def main():
#     print("求解2次方程 ax^2 + bx + c ")
#     a = get_float_input("请输入二次项系数a(a≠0):")
#     while a == 0:
#         print("二次方程的二次项系数a不能为0！请重新输入")
#         a = get_float_input("请重新输入二次项系数a：")
#     b = get_float_input("请输入一次项系数b：")
#     c = get_float_input("请输入常数项系数c：")

#     root1,root2 = solve_quadratic(a,b,c)
#     print(f"方程的解为：{root1}和{root2}")

# if __name__ == '__main__':
#     main()
# def get_float_input():
#     while True:
#         try:
#             a = float(input("输入三角形第一边长a："))
#             b = float(input("输入三角形第二边长b："))
#             c = float(input("输入三角形第三边长c："))
#             if a < 0 or b < 0 or c < 0:
#                 print("三角形边长不能小于0，请重新输入！")
#             elif a+b <= c or a+c <= b or c+b <= a:
#                 print("三角形两边之和必须大于第三边，请重新输入！")
#             else:
#                 s = (a + b + c) / 2
#                 area = (s*(s-a)*(s-b)*(s-c))**0.5
#                 return area
#         except:
#             print("请输入正确数字格式！")

# if __name__ == '__main__':
#     area = get_float_input()
#     print("三角形面积为:%0.2f"%area)

# def get_postive_float(prompt):
#     #验证单边输入得到正浮点数
#     while True:
#         try:
#             value = float(input(prompt))
#             if value > 0:
#                 return value
#             else:
#                 print("三角形边长需大于0，请输入正数！")
#                 continue
#         except:
#             print("请输入正确格式的数字！")

# def validate_triangle(a,b,c):
#     #验证两边之和大于第三边
#     if (a + b <= c) or (a + c <= b) or (b + c <= a):
#         print("错误：不满足三角形两边之和大于第三边，请重新输入所有边长！")
#         return False
#     return True

# def get_triangle_side():
#     #获取有效三角形三边
#     while True:
#         a = get_postive_float("输入三角形第一条边a:")
#         b = get_postive_float("输入三角形第二条边b:")
#         c = get_postive_float("输入三角形第三条边c:")

#         if validate_triangle(a,b,c):
#             return a,b,c

# def calculate_area():
#     #计算三角形面积
#     a,b,c = get_triangle_side()
#     s = (a + b + c) / 2
#     return (s * (s - a) * (s - b) *(s - c)) ** 0.5

# if __name__ == '__main__':
#     area = calculate_area()
#     print(f"三角形面积为：{area:.2f}")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end = '')
#     print()
# lower = int(input("最小值:"))
# upper = int(input("最大值:"))

# for num in range(lower,upper + 1):
#     sum = 0
#     n = len(str(num))
    
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** n
#         temp //= 10
    
#     if num == sum:
#         print(f"{num} ",end = '')
# import calendar
# yy = int(input("输入年份"))
# mm = int(input("输入月份"))

# print(calendar.month(yy,mm))
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
# uinput = int(input("您要输出几项？"))

# if uinput <= 0:
#     print("请输入正数")
# else:
#     print("斐波那契数列：")
#     j = 1
#     for i in range(uinput):
#         print(f"{j} {recur_fibo(i)}")
#         j += 1

# def iterative_fibo(n_terms):
#     a, b = 0, 1
#     for _ in range(n_terms):
#         yield a
#         a, b = b, a + b

# # 使用示例
# for num in iterative_fibo(40):
# #     print(num)
    
# from functools import lru_cache

# @lru_cache(maxsize=None)  # 记忆化加速递归
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     return recur_fibo(n-1) + recur_fibo(n-2)

# # 输入验证增强版
# while True:
#     try:
#         n_terms = int(input("请输入要输出的斐波那契数列项数（正整数）: "))
#         if n_terms <= 0:
#             print("项数必须大于0！")
#         else:
#             break
#     except ValueError:
#         print("无效输入，请输入整数！")

# print("斐波那契数列前{}项：".format(n_terms))
# for i in range(n_terms):
#     print(recur_fibo(i))
# import time
 
# print('按下回车开始计时，按下 Ctrl + C 停止计时。')
 
# while True:
#     input("")  # 等待用户按下回车开始计时
#     start_time = time.time()  # 记录开始时间
#     print('开始计时...')
 
#     try:
#         while True:
#             elapsed_time = round(time.time() - start_time, 0)  # 计算经过的时间
#             print(f'计时: {elapsed_time} 秒', end="\r")  # 覆盖上次输出
#             time.sleep(1)
#     except KeyboardInterrupt:  # 捕捉 Ctrl + C 中断信号
#         end_time = time.time()  # 记录结束时间
#         total_time = round(end_time - start_time, 2)
#         print(f'\n计时结束，总共时间为: {total_time} 秒')
#         break

# import time

# print("按下回车开始计时，按下ctrl + C停止计时")

# while True:
#     input("")
#     start_time = time.time()#记录开始时间
#     print("开始计时")

#     try:
#         while True:
#             elapsed_time = round(time.time() - start_time,0)
#             print(f"计时：{elapsed_time}秒",end = '\r')#覆盖输出
#             time.sleep(1)
#     except KeyboardInterrupt:#捕捉ctrl + c中断信号
#         end_time = time.time()
#         total_time = round(end_time - start_time,2)
#         print(f"计时结束，总共时间为{total_time}秒")
#         break
#!/usr/bin/python3

# import threading
# import time

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.delay, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()

# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# threadLock = threading.Lock()
# threads = []

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# thread1.start()
# thread2.start()

# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)

# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

# import threading
# import time

# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, delay, lock):
#         super().__init__()
#         self.thread_id = thread_id
#         self.name = name
#         self.delay = delay
#         self.lock = lock  # 接收锁对象

#     def run(self):
#         print(f"开启线程：{self.name}")
#         # 使用传入的锁
#         self.lock.acquire()
#         try:
#             print_time(self.name, self.delay, 3)
#         finally:
#             self.lock.release()

# def print_time(thread_name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print(f"{thread_name}: {time.ctime(time.time())}")
#         counter -= 1

# # 在全局作用域创建锁
# thread_lock = threading.Lock()
# threads = []


# # 创建线程时传入锁对象
# thread1 = MyThread(1, "Thread-1", 1, thread_lock)
# thread2 = MyThread(2, "Thread-2", 2, thread_lock)

# thread1.start()
# thread2.start()

# threads.append(thread1)
# threads.append(thread2)

# for t in threads:
#     t.join()

# print("退出主线程")

#!/usr/bin/python3

# import time

# localtime = time.localtime(time.time())
# print ("1.本地时间为 :", localtime)

# localtime = time.asctime(time.localtime(time.time()))
# print("2.本地时间为：",localtime)

# print(time.strftime("3.本地时间为：%Y-%m-%d %H:%M:%S",time.localtime()))

# print(time.strftime("4.本地时间为：%y-%m-%d %H:%M:%S",time.localtime()))

# print(time.strftime("5.本地时间为：%a %b %d %H:%M:%S",time.localtime()))

# a = "Sat Mar 28 22:24:24 2016"
# print (time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# import numpy
# import pyecharts
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# # 内置主题类型可查看 pyecharts.globals.ThemeType
# from pyecharts.globals import ThemeType

# # 准备数据
# x_data = ['一月', '二月', '三月', '四月', '五月']
# y_data = [10, 20, 15, 25, 30]

# # 创建柱状图
# bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 初始主题为亮色系
# bar_chart.add_xaxis(x_data)
# bar_chart.add_yaxis("销售额", y_data)

# # 配置图表
# bar_chart.set_global_opts(
#     title_opts=opts.TitleOpts(title="月度销售额柱状图"),
#     xaxis_opts=opts.AxisOpts(name="月份"),
#     yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
# )

# # 切换到暗色系主题
# bar_chart.set_global_opts(theme=ThemeType.DARK)

# # 渲染图表
# bar_chart.render("themed_bar_chart.html")


# import numpy
# import pyecharts
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.globals import ThemeType

# # 准备数据
# x_data = ['一月', '二月', '三月', '四月', '五月']
# y_data = [10, 20, 15, 25, 30]

# # 创建柱状图（直接初始化暗色主题）
# bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 直接设置最终主题
# bar_chart.add_xaxis(x_data)
# bar_chart.add_yaxis("销售额", y_data)

# # 配置图表
# bar_chart.set_global_opts(
#     title_opts=opts.TitleOpts(title="月度销售额柱状图"),
#     xaxis_opts=opts.AxisOpts(name="月份"),
#     yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
# )

# # 渲染图表
# bar_chart.render("themed_bar_chart.html")
# from selenium import webdriver
# from selenium.webdriver.common.by import By  # 导入 By 模块
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # 设置驱动的路径，启动浏览器
# service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver")
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)


# try:
#     # 打开百度首页
#     driver.get("https://www.baidu.com")

#     # 查找搜索框元素
#     search_box = driver.find_element(By.ID, "kw")

#     # 输入搜索内容
#     search_box.send_keys("Selenium Python")

#     # 提交搜索表单
#     search_box.send_keys(Keys.RETURN)

#     # 等待搜索结果加载
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "content_left"))
#     )

#     # 打印页面标题
#     print("页面标题是:", driver.title)

# finally:
#     # 关闭浏览器
#     driver.quit()

# import warnings
# from urllib3.exceptions import NotOpenSSLWarning  # 导入特定警告类
# warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# # 自动配置驱动
# service = ChromeService(executable_path=ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     driver.get("https://www.baidu.com")
#     search_box = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "kw"))
#     )
#     search_box.send_keys("Selenium Python" + Keys.RETURN)
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "content_left"))
#     )
#     print("页面标题是:", driver.title)
# except Exception as e:
#     print("运行出错:", e)
# finally:
#     driver.quit()
# from urllib.request import urlopen

# try:
#     myURL = urlopen("https://www.runoob.com/")
#     f = open("runoob_urllib_test.html", "wb")
#     f.write(myURL.read())
# finally: 
#     f.close
#####################
# import urllib.request
# import urllib.parse

# url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
# keyword = 'Python 教程' 
# key_code = urllib.request.quote(keyword)  # 对请求进行编码
# url_all = url+key_code
# header = {
#     'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }   #头部信息
# request = urllib.request.Request(url_all,headers=header)
# reponse = urllib.request.urlopen(request).read()

# try:
#     fh = open("./urllib_test_runoob_search.html","wb")    # 将文件写入到当前目录中
#     fh.write(reponse)
# finally:
#     fh.close()

# import urllib.request
# import urllib.parse
# from chardet import detect  # 用于自动检测编码

# url = 'https://www.runoob.com/?s='
# keyword = 'Python 教程'
# key_code = urllib.request.quote(keyword)
# url_all = url + key_code

# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
# }

# try:
#     # 发送请求
#     request = urllib.request.Request(url_all, headers=header)
#     response = urllib.request.urlopen(request)
#     content = response.read()

#     # 检测编码
#     charset = response.headers.get_content_charset()
#     if not charset:
#         # 若头部无编码信息，自动检测
#         charset = detect(content)['encoding']
    
#     # 解码内容
#     html = content.decode(charset, errors='ignore')

#     # 写入文件（使用正确编码）
#     with open("./urllib_test_runoob_search2.html", "w", encoding=charset) as fh:
#         fh.write(html)
    
#     print(f"文件已保存，编码为：{charset}")

# except Exception as e:
#     print(f"运行出错：{e}")


# import requests
# from chardet import detect

# url = 'https://www.runoob.com/?s='
# keyword = 'Python 教程'
# params = {'s': keyword}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
# }

# try:
#     response = requests.get(url, params=params, headers=headers)
#     response.raise_for_status()

#     # 检测编码
#     if response.encoding is None:
#         detected = detect(response.content)
#         encoding = detected['encoding']
#     else:
#         encoding = response.encoding

#     # 手动覆盖常见中文编码
#     if encoding.lower() not in ['utf-8', 'utf8']:
#         encoding = 'gb18030'

#     # 重新解码确保正确
#     html = response.content.decode(encoding, errors='ignore')

#     # 写入文件
#     with open("./urllib_test_runoob_search3.html", "w", encoding=encoding) as fh:
#         fh.write(html)
    
#     print(f"文件已保存，编码为：{encoding}")

# except Exception as e:
#     print(f"运行出错：{e}")


# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.baidu.com/'

# try:
#     # 发送请求并自动处理编码
#     response = requests.get(url)
#     response.encoding = response.apparent_encoding  # 自动检测真实编码
    
#     if response.status_code != 200:
#         raise Exception(f"请求失败，状态码：{response.status_code}")

#     soup = BeautifulSoup(response.text, 'lxml')
    
#     # 查找所有<a>标签并取第一个
#     links = soup.find_all('a')
#     if not links:
#         raise Exception("未找到<a>标签")
#     for i in links[10]:
#         first_link = links[i]
#         print(f"第{i}个<a>标签:", first_link)
#         print("----------------------------")
#         # # 获取父标签文本（去除空白）
#         # parent_tag = first_link.parent
#         # print("父标签文本:", parent_tag.get_text(strip=True))
#         parent_tag = first_link.parent

#         # 如果父标签是 NavigableString，向上查找真正的 Tag 父级
#         if isinstance(parent_tag, bs4.element.NavigableString):
#             current_parent = parent_tag.parent
#             print("父标签文本(Tag):", current_parent.get_text(strip=True))
#         else:
#             print("父标签文本:", parent_tag.get_text(strip=True))

# except Exception as e:
#     print(f"程序出错: {e}")
# import bs4
# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.baidu.com/'

# try:
#     response = requests.get(url)
#     response.encoding = response.apparent_encoding  # 自动检测编码
    
#     if response.status_code != 200:
#         raise Exception(f"请求失败，状态码：{response.status_code}")
    
#     soup = BeautifulSoup(response.text, 'lxml')
#     links = soup.find_all('a')

#     if not links:
#         raise Exception("未找到<a>标签")

#     # 仅遍历前10个链接（防止索引越界）
#     for idx, link in enumerate(links[:10]):
#         print(f"第{idx}个<a>标签:", link)
#         print("----------------------------")

#         # 获取父标签文本（跳过非Tag父级）
#         parent_tag = link.parent
#         if isinstance(parent_tag, bs4.element.Tag):  # 确保是Tag对象
#             print("父标签文本:", parent_tag.get_text(strip=True))
#         else:
#             print("父标签不是有效的HTML标签")
#         print("\n")

# except Exception as e:
#     print(f"程序出错: {e}")
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         g = [[] for _ in range(n)]
#         for x, y, d in roads:
#             g[x - 1].append((y - 1, d))
#             g[y - 1].append((x - 1, d))
#         ans = inf
#         vis = [False] * n
#         def dfs(x: int) -> None:
#             nonlocal ans
#             vis[x] = True
#             for y, d in g[x]:
#                 ans = min(ans, d)
#                 if not vis[y]:
#                     dfs(y)
#         dfs(0)
#         return ans
# from typing import List
# import math

# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         # 初始化邻接表，每个节点对应一个列表存储邻接节点及距离
#         g = [[] for _ in range(n)]
#         for x, y, d in roads:
#             # 将城市编号转换为0-based索引，添加双向边
#             g[x - 1].append((y - 1, d))
#             g[y - 1].append((x - 1, d))
#         ans = math.inf  # 初始化为无穷大，记录最小距离
#         vis = [False] * n  # 标记节点是否被访问过
        
#         def dfs(x: int) -> None:
#             nonlocal ans #声明后才能在函数内部进行修改
#             vis[x] = True  # 标记当前节点已访问
#             for y, d in g[x]:  # 遍历所有邻接边
#                 ans = min(ans, d)  # 更新全局最小值
#                 if not vis[y]:  # 若邻接节点未访问，递归遍历
#                     dfs(y)
        
#         dfs(0)  # 从节点0（城市1）开始DFS遍历
#         return ans  # 返回连通块中的最小边

# solution = Solution()
# n = 4
# roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# result = solution.minScore(n,roads = roads )
# print(result)
# import bisect
# from typing import List

# class FenwickTree:
#     def __init__(self, size):
#         self.n = size
#         self.tree = [0] * (self.n + 2)  # 1-based索引
    
#     def update(self, idx, delta):
#         while idx <= self.n:
#             self.tree[idx] += delta
#             idx += idx & -idx
    
#     def query_prefix(self, idx):
#         res = 0
#         while idx > 0:
#             res += self.tree[idx]
#             idx -= idx & -idx
#         return res
    
#     def query_range(self, l, r):
#         if l > r:
#             return 0
#         return self.query_prefix(r) - self.query_prefix(l - 1)

# class Solution:
#     def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
#         # 收集所有hi和yj的值进行离散化
#         all_hi = []
#         for l, h in rectangles:
#             all_hi.append(h)
#         for x, y in points:
#             all_hi.append(y)
#         # 排序并去重
#         sorted_hi = sorted(list(set(all_hi)))
#         # 映射到1-based索引
#         hi_map = {v: i + 1 for i, v in enumerate(sorted_hi)}
        
#         # 创建事件列表：矩形点和查询点按x降序处理
#         events = []
#         # 处理矩形点：事件类型为0，存储负的x和负的hi以便排序
#         for l, h in rectangles:
#             events.append((-l, -h, 0))  # 类型0表示矩形点
#         # 处理查询点：事件类型为1，存储负的x和负的y，并保留原始索引
#         for idx, (x, y) in enumerate(points):
#             events.append((-x, -y, 1, idx))  # 类型1表示查询点
        
#         # 排序事件：按x降序（即事件中的第一个元素升序），相同x时矩形点优先（类型0在前）
#         events.sort(key=lambda e: (e[0], e[2]))
        
#         # 初始化Fenwick树
#         ft = FenwickTree(len(sorted_hi))
#         ans = [0] * len(points)
        
#         for event in events:
#             if event[2] == 0:
#                 # 处理矩形点：插入hi到Fenwick树
#                 h = -event[1]
#                 mapped_idx = hi_map[h]
#                 ft.update(mapped_idx, 1)
#             else:
#                 # 处理查询点：查询>=yj的数量
#                 y = -event[1]
#                 original_idx = event[3]
#                 # 找到离散化后的最小索引 >= y
#                 pos = bisect.bisect_left(sorted_hi, y)
#                 if pos == len(sorted_hi):
#                     ans[original_idx] = 0
#                 else:
#                     min_mapped = pos + 1  # 转为1-based索引
#                     max_mapped = len(sorted_hi)
#                     count = ft.query_range(min_mapped, max_mapped)
#                     ans[original_idx] = count
#         return ans

# class Solution:
#     def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
#         players.sort()
#         trainers.sort()
        
#         i = j = count = 0
#         n,m = len(players),len(trainers)

#         while i < n and j < m:
#             if players[i] <= trainers[j]:
#                 i += 1
#                 j += 1
#                 count += 1
#             else:
#                 j += 1
        
#         return count 

# print("hello world",'hello python');print("    ",1)
# print("hello","world",'sad',sep = '-`',end = '!\n')

# print('i的值为:%d'%2.134)

# a = 'abcdef'
# print(a)
# print(a[5:1:-2])
# print(a[5:1:2])

# print("My name is %s and my weight is %d kg" % (senhuang,80))

# matrix = [[0 for _ in range(3)] for _ in range(3)]
# print(matrix)

# dict = {}
# dict['one'] = 'This is one'
# dict[2] = 'This is two'

# print(dict['one'])
# print(dict[2])
# print(dict.keys())
# print(dict.values())

# x = 5

# if x > 3:
#     pass
# else :
#     print("x小于等于3")

# result = [i for i in range(4)]
# print(result)

# list = [1,2,3,4]
# it = iter(list)
# for i in range(5): 
#     print(next(it))

# students = [
#     {'name': 'Alice', 'score': 85},
#     {'name': 'Bob', 'score': 92},
#     {'name': 'Charlie', 'score': 78}
# ]

# key=lambda student: student['score']
# print(key(students[1]))

# debug_demo.py 
# def calculate_sum(n):
#     total = 0
#     for i in range(n + 1):
#         total += i
#         print(f"i={i}, total={total}")
#     return total

# def main():
#     numbers = [1, 2, 3, 4, 5]
#     result = calculate_sum(5)
#     print(f"最终结果: {result}")
    
#     # 处理列表
#     squares = [x**2 for x in numbers]
#     print(f"平方列表: {squares}")

# if __name__ == "__main__":
#     main()

# def creat   e_functions():
#     functions = []
#     for i in range(3):
#         def func():
#             return i
#         functions.append(func)
#     return functions

# funcs = create_functions()
# for f in funcs:
#     print(f())  # 全部输出: 2

# import builtins
# dir(builtins)

# num_str = '123'
# num_int = int(num_str)
# num_float = float(num_int)
# print(f"类型转换:{type(num_str)} -> {type(num_int)} -> {type(num_float)}")

# score = 84

# if score >= 95:
#     grade = 'A'
# elif score >=85:
#     grade = 'B'
# elif score >= 75:
#     grade = 'C'
# else:
#     grade = 'D'

# print(f"分数是{score},等级是{grade}")

# squares = [x**2 for x in range(10)]
# print(squares)

# squares_dict = {x:x**2 for x in range(10)}
# print(squares_dict)

# unique_squares = {x**2 for x in [1,-1,2,2,3,-3,4,5]}
# print(unique_squares)

# def add_num(x,y):
#     return x + y

# add_lambda = lambda x,y:x+y

# print(f"常规函数：{add_num(2,3)}")
# print(f"lambda函数:{add_lambda(2,3)}")  

# def calculator():
#     while True:
#         print("简易计算器")
#         print("1:加法 2.减法 3.乘法 4.除法 5.退出")
#         choice = input("请输入数字，选择运算：")
    
#         if choice == '5':
#             print("退出计算器")
#             break
        
#         if choice not in ['1','2','3','4']:
#             print("无效选择，请重新输入")
#             continue
#         else:
#             try:
#                 num1 = float(input("请输入第一个数字:"))
#                 num2 = float(input("请输入第二个数字:"))

#                 if choice == '1':
#                     result = num1 + num2
#                     print(f"结果: {num1} + {num2} = {result}")
#                 elif choice == '2':
#                     result = num1 - num2
#                     print(f"结果: {num1} - {num2} = {result}")
#                 elif choice == '3':
#                     result = num1 * num2
#                     print(f"结果: {num1} * {num2} = {result}") 
#                 elif choice == '4':
#                     if num2 != 0:
#                         result = num1 / num2
#                         print(f"结果: {num1} / {num2} = {result}")
#                     else:
#                         print("错误：除数不能为零")
#             except ValueError:
#                 print("无效输入，请输入数字")

# calculator()

# class TodoList:
#     def __init__(self):
#         self.tasks = []
    
#     def add_task(self, task):
#         self.tasks.append({"task": task, "completed": False})
#         print(f"添加任务: {task}")
    
#     def view_tasks(self):
#         print("\n待办事项:")
#         for i, task in enumerate(self.tasks, 1):
#             status = "✓" if task["completed"] else "○"
#             print(f"{i}. {status} {task['task']}")
    
#     def complete_task(self, task_num):
#         if 1 <= task_num <= len(self.tasks):
#             self.tasks[task_num-1]["completed"] = True
#             print(f"完成任务: {self.tasks[task_num-1]['task']}")
#         else:
#             print("无效的任务编号")

# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self,task):
#         self.tasks.append({"task":task,"completed":False})
#         print(f"添加任务:{task}")

#     def view_tasks(self):
#         print("待办事项:")

# list = [{"one":1},{"two":2},{"three":3},{"four":4}]
# # print(enumerate(list,1))
# # for index,item in enumerate(list,1):
# #     print(f"第{index}个元素是:{item}")

# # enum_obj = enumerate(list,1)

# print(next(enumerate(list,1)))
# print(next(enumerate(list,1)))
# print(next(enumerate(list,1)))
# print(next(enumerate(list,1)))
# print(next(enumerate(list,1)))
# print(next(enum_obj))
# print(next(enum_obj))
# print(next(enum_obj))
# print(next(enum_obj))

# class TodoList:
#     def __init__(self):
#         self.tasks = []
    
#     def add_task(self,task):
#         self.tasks.append({"task":task,"completed":False})
#         print(f"添加任务:{task}")
    
#     def view_task(self):
#         print("\待办事项")
#         for i,task in enumerate(self.tasks,1):
#             status = '√' if task['completed'] else 'O'
#             print(f"{i}.{status}{task['task']}")

#     def complete_task(self,task_num):
#         if 1 <= task_num <= len(self.tasks):
#             self.tasks[task_num - 1]["completed"] = True
#             print(f"完成任务:{self.tasks[task_num - 1]['task']}")
#         else:
#             print("无效的任务编号")

# todo = TodoList()
# todo.add_task("学习python")
# todo.add_task("完成项目")
# todo.view_task()

# name : str = 'Alice'
# print(name)

# age: int = '30'
# print(age)

# def greet(name:str) -> int:
#     return(f"Hello,{name}")

# print(greet('Wang'))


# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write("第一行内容\n")
#     f.write("第二行内容\n")
#     f.write("第三行内容\n")
#     f.write("第四行内容\n")

# with open('test.txt', 'a',encoding = 'utf-8') as f:
#     f.write('这是追加的内容\n')

# with open('test.txt','r+',encoding = 'utf-8') as f:
#     content = f.read()
#     f.write("这是读写模式添加的内容\n")

# with open('test.txt','r', encoding = 'utf-8') as f:
#     content = f.read()
#     print("读取整个文件:")
#     print(content)

# with open('test.txt','r', encoding = 'utf-8') as f:
#     print("\n逐行读取:")
#     for line in f:
#         print(f"行内容:{line.strip()}")

# with open('test.txt','r',encoding = 'utf-8') as f:
#     lines = f.readlines()
#     print(f"\n读取所有行到列表:{lines}")

# # 二进制模式（处理图片、视频等）
# with open('test.txt', 'rb') as f:
#     binary_content = f.read()
#     print(f"\n二进制内容前100字节: {binary_content[:100]}")

import os

class NoteManager:
    def __init__(self, notes_dir="notes"):
        """
        初始化笔记管理器
        notes_dir: 存放笔记文件的目录（默认为 notes）
        """
        self.notes_dir = notes_dir
        # 如果目录不存在则创建（确保后续读写不会出错）
        if not os.path.exists(notes_dir):
            os.makedirs(notes_dir)
    
    def create_note(self, title, content):
        """创建新笔记并写入内容
        title: 笔记标题（将用于文件名）
        content: 笔记内容字符串
        """
        # 使用标题作为文件名，追加 .txt 后缀
        filename = f"{self.notes_dir}/{title}.txt"
        # 以 UTF-8 编码写入文件，覆盖已存在同名文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"笔记 '{title}' 已创建")
    
    def list_notes(self):
        """列出 notes_dir 中所有以 .txt 结尾的笔记文件并显示标题（去掉后缀）"""
        notes = [f for f in os.listdir(self.notes_dir) if f.endswith('.txt')]
        if not notes:
            print("没有找到笔记")
            return
        
        print("\n所有笔记:")
        # 枚举并显示去掉 .txt 后缀的标题
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note[:-4]}")
    
    def read_note(self, title):
        """读取并打印指定标题的笔记内容
        title: 笔记标题（不带后缀）
        """
        filename = f"{self.notes_dir}/{title}.txt"
        try:
            # 以 UTF-8 编码读取文件内容
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"\n{title}:\n{content}")
        except FileNotFoundError:
            print(f"笔记 '{title}' 不存在")
    
    def delete_note(self, title):
        """删除指定标题的笔记文件
        title: 笔记标题（不带后缀）
        """
        filename = f"{self.notes_dir}/{title}.txt"
        try:
            os.remove(filename)
            print(f"笔记 '{title}' 已删除")
        except FileNotFoundError:
            print(f"笔记 '{title}' 不存在")

# 使用示例：一个简单的终端交互式笔记应用
def note_app():
    # 创建管理器实例（默认在当前目录下创建 notes 文件夹）
    manager = NoteManager()
    
    while True:
        # 打印菜单，提示用户选择操作
        print("\n=== 个人笔记管理器 ===")
        print("1. 创建笔记")
        print("2. 查看笔记列表")
        print("3. 读取笔记")
        print("4. 删除笔记")
        print("5. 退出")
        
        choice = input("请选择操作: ")
        
        if choice == '1':
            # 创建笔记：提示标题和内容
            title = input("输入笔记标题: ")
            content = input("输入笔记内容: ")
            manager.create_note(title, content)
        elif choice == '2':
            # 列出所有笔记标题
            manager.list_notes()
        elif choice == '3':
            # 读取指定标题的笔记内容
            title = input("输入要读取的笔记标题: ")
            manager.read_note(title)
        elif choice == '4':
            # 删除指定标题的笔记
            title = input("输入要删除的笔记标题: ")
            manager.delete_note(title)
        elif choice == '5':
            # 退出循环，结束程序
            break
        else:
            print("无效选择")       

# 直接运行脚本时启动笔记应用
note_app()

# import os 
# current_directory = os.getcwd()
# print(f"当前工作目录:{current_directory}")

# file_and_dir = os.listdir()
# print(f"当前目录下的文件和文件夹:{file_and_dir}")