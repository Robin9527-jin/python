#! /Users/jinchaofei/.conda/envs/pythonProject/bin/python

firname = '张'
latname = 3
print((firname + str(latname)) * 10)
#
# age = int(input("请输入你的年龄："))
# if age >= 16:
#     print("你已经成年了")
# else:
#     print("你还时个小朋友")
# price_r = float(input("请输入单价："))
# weight_r = float(input("请输入重量："))
# # price_r = input("请输入单价：")
# # weight_r = input("请输入重量：")
# # price = float(price_r)
# # weight = float(weight_r)
# #计算总价
# money = price_r * weight_r
# print("苹果总价是 %.2f,单价是 %.2f,重量是 %.2f" %(money,price_r,weight_r))

# scale = 0.55
# print("数据百分比是 %.2f %%" %(scale*100))
# a = 16
# print("输出整型 %06d" %a)
# print("输出字符串 %s" %scale)

# 使用逻辑运算符判断年龄是否合法
age = 17
gender = "M"

# if 0 <= age <= 120:
#     print("年龄合法")
# if age >=18 or gender == "M":
#     print("您的年龄 %d 岁,性别 %s" %(age,gender))
# else:
#     print("年龄不在合法范围内！")

# 多添件下执行不同的代码
# day = int(input("输入日期："))
# if day == 214:
#     print("今天是情人节")
# elif day == 1224:
#     print("今天是平安夜")
# elif day == 218:
#     print("今天是你的生日")
# else:
#     print("今天是个平凡的日子")

# if 嵌套
# 小练习：过安检

# 定义车票
# def ticket(name):
#     #车票名称
#     if name == "jcf":
#         return True
#     else:
#         return False
# tik = ticket(str(input("请输入姓名来检查车票：")))
# print("分割线","-"*50)
# #检查是否有车票
# if tik == True:
#     print("车票检查通过，请过安检")
#     # 定义道具长度
#     dao = int(input("刀长："))
#     # 检查道具长度是否超过20cm
#     # 如果超过20厘米不许上车
#     if dao > 20:
#         print("道具长度超过20厘米，请交由安检处理")
#     else:
#         print("长度小于20厘米，可以上车")
# else:
#     print("请先买票！")


import random

# 石头剪刀布小游戏
# 规则：玩家选择出拳（1：石头；2：剪刀；3：布）
# while True:
#     player = int(input("请玩家出拳（1：石头；2：剪刀；3：布）："))
#     computer = random.randint(1, 3)
#     #电脑随机出拳
#         #输出玩家与电脑的出拳
#     #比较大小
#     if player > 3 or player == 0 or player == "":
#         print("您输入的选项错误，请重新输入！")
#         print("-" * 30, "分割线", "-" * 30)
#         continue
#
#     elif ((player==1 and computer==2)
#             or (player==2 and computer==3)
#             or (player==3 and computer==1)):
#         print("本轮玩家出的是 %d -- 电脑出的是 %d" %(player,computer))
#         print("本轮玩家赢！")
#         print("-"*30,"分割线","-"*30)
#         continue
#     elif player == computer:
#         print("本轮平局！")
#         print("-" * 30, "分割线", "-" * 30)
#         continue
#
#     else:
#         print("本轮比试电脑赢！")
#         print("-" * 30, "分割线", "-" * 30)
#         continue

# while循环执行n遍代码

# i = 0
# while i <= 5:
#     print("当前i=: %d" % i)
#     i += 1
# print("循环结束后I=: %d" % i)

# 循环计算0-100之间数字的总和
# i = 0
# cont = 0
# num = 0
# while i <= 10:
#     print("第 %d 遍循环 i = : %d" %(i,i))
#     cont += i
#     print("第 %d 遍计算结果cont = ：%d" % (i,cont))
#     if cont % 2 == 0:
#         print("【第 %d 次计算得出偶数 %d ：】"%(i,cont))  #得出0-100之间的偶数
#         num += cont
#     i += 1
# 计算0-100之间的偶数相加的总和
# i = 0
# ret = 0
# while i <= 100:
#     print("i = %d:" % i)
#     if i % 2 == 0:
#         ret += i
#         print("ret第 %d 次结果= %d :" %(i,ret))
#     i += 1
# print("0-100之间偶数相加的结果是：%d" % ret)

# continue 关键字
# i = 0
# while i <= 10:
#
#     if i == 4:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j,end="----")
#         j += 1
#     print("*")
#     i += 1

##while 循环嵌套
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d*%d=\"%d\" \t" %(col,row,(col*row)),end="")
#         # print("这是列",end=" ")
#         col += 1
#     print("这是行")
#     row += 1
# 求100-1000以内的水仙花数
# 定义初始值
# i = 100
#
# while i < 1000:
#
#     #获取百位数
#     a = i // 100
#     #获取十位数
#     b = (i -a * 100) // 10
#     #获取个位数
#     c = i % 10
#     if a**3 + b**3 + c**3 == i: #判断i是否是水仙花数
#         print(i)
#     i += 1


# def multiple_tatle(row,col):
#     ret = row + col
#     print("%d+%d=: %d" %(row,col,ret))
#
# multiple_tatle(2,3)

# #使用return来返回函数内部的结果
# def multiple_tatle(row,col):
#     ret = row + col
#     return ret
#
# result = multiple_tatle(2,3)
# print(result)

# import main
#
#
# def line(char,times):
#     ret = char * times
#     print(ret)
#
#
# def lines(char,times):
#     """
#     打印多行分割线
#     :param char:打印的符号
#     :param times:需要重复的次数
#     :return:
#     """
#     row = 0
#     while row <5:
#         line(char,times)
#         row += 1
#
# lines(main.char,main.times)

# 列表中常用的操作方法
name_list = ["小红", "张三", "李四"]
temp_list = ["孙悟空", "祝二哥", "沙师弟", "白龙马", "唐生", "哪吒"]

print(max(name_list))  # 获取列表的最大值（根据索引值来比较）
print(min(name_list))  # 获取列表的最小值（根据索引值来比较）

# insert 向列表中插入数据（）
#     需要两个参数：
#     1，第一个参数是索引，表示要插入的位置（如果该索引有数据则顺延）
#     2，第二个参数表示要插入的数据,不限数据类型
name_list.insert(0, "小明")
name_list.insert(1, ("小张", 27))
# print(name_list)
# print(name_list.index("张三"))

# append 向列表的末尾添加数据
name_list.append("王小二")
# name_list.append(temp_list) #把另一个列表的元素添加到列表
# name_list.append(temp_list[1]) #把另外一个列表中的某个元素添加到列表中
# name_list.append(temp_list[0:5])
# print(name_list)

# extend 把另外一个列表中的数据完整的追加到另一个列表中(末尾追加)
# 参数；列表的变量名作为参数传递

# name_list.extend(temp_list)
name_list.extend(temp_list)
# print(name_list)


# 删除数据
a = name_list[0]
# remove() 可以删除列表中指定的数据,参数可以是列表中的元素或变量名而不能是索引值
name_list.remove(a)
# pop() 方法默认删除列表最后一个元素；也可以指定一个元素的索引值来删除元素
name_list.pop()
name_list.pop(1)

# clear()方法可以清空列表内元素
# name_list.clear()

# del 关键字：本质上是用来把一个变量从内存中删除，如过这个变量被del，后续的代码将不能在使用这个变量
# del name_list
del name_list[0]  # 使用del删除列表中指定的元素

# 日常开发中如果要删除列表中元素，尽量使用列表提供的方法，比如：pop(),remove()
print(name_list)

# 列表的统计
# len() 方法可以统计列表中元素的总数,需要将列表的变量名作为参数传递
list_len = len(name_list)
print(list_len)
# count() 方法用来统计列表中某个元素出现的次数，将需要统计的元素作为参数传递
b = name_list[0]
count = name_list.count(b)
print(count)

# 排序
# sort()方法可以对列表中的元素由小到大进行排序，默认是升序
ls = [2, 4, 6, 8, 1, 3, 5, 7]
ls.sort()
# ls.sort(reverse=True)  #reserve参数等于True时，则表示降序,由大到小排序

name_list.reverse()  # reverse()方法可以对列表中的元素进行反转、逆序
# print(name_list)

# for 循环遍历
"""
for 用来按顺序从列表中一次获取数据，每次获取一个元素
并且把获取到的数据保存在for后面定义的变量名中
: for 循环可以遍历任何非数字类型的变量，如：列表，元组，字典，字符串
： 世纪开发中，除非能够确认元组的数据类型，否则一般不会对元组进行遍历，因为一般元组中的数据类型是不同的
"""
# for name in name_list:  #name就相当于在循环体中定义了一个变量名
#     print(name)

# 元组tuple
# 元组定义后不可被修改
# 定义空元组
tuple_a = ()
# 定义一个只包含一个元素的元组,必须以逗号结尾
tuple_b = (3, 5, 6, 8, 2, 5, 3)
# 把一个列表转换为元组,使用tuple()函数，并把需要转换的列表作为参数传递，转换完成之后把结果赋值给一个变量
ls_tup = tuple(name_list)

# 把一个字符串转换为元组
ls_tup1 = tuple(firname)
# print("转换字符串",ls_tup1)

# 元组的常用操作方法
# count() 统计元组内元素出现的次数,并把统计结果返回,需要把元素作为参数传递
# print(tuple_b.count(3))
# index()方法可以获取元组中元素的索引值，需要把元素作为参数传递
# print(tuple_b.index(8))
# len()方法，用来获取元组的长度，需要把元组变量名作为参数传递
# print(len(tuple_b))
# tuple[index] 从元组中获取数据
# print(tuple_b[2])
# print(tuple_b[0:])
# print(tuple_b[0:2])
# tuple_c = tuple_b[0:]
# print(tuple_c)

# 元组与格式化字符串
# 格式化字符串的时候，% 后面的（）实际上就是一个元组
name_tuple = ("张三", 19, 1.88)
# print("%s %d 岁了，身高%.2f" %name_tuple) #以元组的变量名来填充占位符
str = "%s %d 岁了，身高%.2f" % name_tuple  # 在字符串中填充占位符，类似于拼接字符串
# print(str)

# 字典
# 字典是一个无序的数据集合,python3.9好像去除了这个问题
# 列表是一个有序的数据集合
# 字典使用键值对来保存数据
# 字典的key就是索引
# 字典的key必须是唯一的，值可以是任何数据类型，但键只能是字符串、数字、元组

# 在使用print()函数输出字典
dict_name = {"name": "小明",
             "age": 19,
             "身高": 1.75}

# print(dict_name)
# 从字典中取值
# 根据字典的key来获取数据
# print(dict_name["name"])
# get()方法，需要把key作为参数传递，返回对应key的值，如果key不存在则返回默认值None
# print(dict_name.get("name"))


# 增加/修改 字典的值
# 在字典名称后面的方括号中写入key，并跟上要赋值的数据，如果这个key不存在，则增加键值对
# dict_name["weight"]=68
# 如果存在则修改这个key的值
# dict_name["name"]="小张"

# 删除
# pop()方法用来删除字典中的键值对，需要将字典的key作为参数传递来删除指定的数据
# dict_name.pop("name")


# print(dict_name)
# 遍历列表中的元素
# for i in name_list:
#     print("name=",i)
#
# # 遍历元组中的元素
# for i in tuple_b:
#     print(i)
#
# # 遍历字典中的key
# for i in dict_name:
#     print(i)
# # 遍历字典中的value
# for i in dict_name:
#     print(dict_name[i])
# # 遍历字典中的key:value
# for i in dict_name:
#     print("%s:%s" %(i,dict_name[i]))

# 列表与字典组合使用
# card_list = [
#     {"name":"张三","age":18,"height":1.78},
#     {"name":"李四","age":20,"height":1.67}
# ]
# print(card_list)
#
# for info in card_list:
#     print(info["name"],info["age"])

# 字符串的常用操作方法
string = "ahdajhgwjewe"  # 使用双引号定义字符串
string1 = 'hello"靳朝飞"'  # 使用单引号定义字符串，字符串内部可以嵌套双引号并输出双引号


# # len() 函数统计字符串的长度
# print(len(string))
# # count() 方法统计字符串中某个元素出现的次数
# print(string.count("w"))
# # index() 获取某个字符在字符串中的位置
# print(string.index("jhg"))
# print(string1)
# print(string1.find("靳朝飞",0,len(string1)))
# str1 = "禾\t古诗\t锄禾日当午\t汗滴禾下土\t谁知盘中餐\t粒粒皆辛苦"
#
# ls = ["禾\n\t",
#       "古诗，",
#       "锄禾日当午\n\t",
#       "汗滴禾下土\n\t",
#       "谁知盘中餐\n\t",
#       "粒粒皆辛苦\n\t"]
# for i in ls:
# print(i.strip().center(10,"*"))
# print(i.ljust(10))
# print(i.rjust(10,"*"))
# print(str1)
# lis = str1.split()
# str2 = "".join(lis)
# print(str2[3::2])

# print(string1.startswith("abd"))
# print(string1.endswith('靳朝飞"'))

# print(string1.replace("靳朝飞","张三"))
# print(string1.replace("靳朝飞","lisi"))


# 使用位与运算判断数字的奇偶数
# a = 3
# if a & 1 == 0:
#     print(f"{a}是偶数")
# else:
#     print(f"{a}是奇数")

# 运算符的优先级
# a = 1
# b = 2
# c = 3
# d = 1

# e = a + b * d - c
# print("a + b * d - c = %d" %e)  #计算顺序：(a + (b * d)) - c
# e = a + b * c / d
# print("a + b * c / d = %d" %e)  #计算顺序： a + (b * c) / d)
#
# e = a + b * d and a - d
# if a + b * d and a - d:
#     print("两个结果都大于0")
# else:
#     print("一个结果小于0")
# name = "李四"
# list2 = [1,2,3,4,5,6]
# list3 = [{"name":"张三"},{"name":"小明"}]
# for i in list3:
#     # print(i)
#     if i["name"] == name:
#         print("找到%s了" %name)
#         break
# else:
#     print("抱歉，未找到")

# 检查嵌套列表中是否存在指定的key
# n = input("请输入要查找的键：")
# list4 = [{"name":"张三"},{"name":"小明"}]
# for i in list4:
#     #遍历获取到的字典
#     count = 0
#     for k in i:
#         if k == n:
#             count += 1
#             print("共找到了%d个%s" %(count,n))
#     break
# else:
#     print("抱歉，未找到name")
#
# 全局变量定义时需要在函数的最上方
# 全局变量名称定义时，应和其他局部变量名称区分开，如：gl_var = n

# dic = {"name":"张三","age":"18"}
# # # print(id(dic))
# # # dic.pop("age")
# # # print(id(dic))
# # print("hash值是：",hash(float))
# def num():
#     global dic2
#     dic2 = {"weight":65}
#     print(dic)
#
# def num2():
#     print(dic2)
#
# num()
# num2()

# # 函数需要返回多个结果时，可以利用元组返回
# def fonc():
#     cpm = 20
#     cpt = 30
#     cpl = 40
#     return cpm,cpt,cpl   #使用元组返回多个结果时，可以省略掉括号
#
# r_cpm,r_cpt,r_cpl = fonc()  #将函数赋值给多个变量，函数的返回结果会依次赋值给每一个变量；变量的数量需要和函数的返回值数量一致
# print(r_cpm,r_cpt,r_cpl)
# 在函数内部对形参做赋值时，不会对函数外部的实参变量产生影响
# 当函数内部需要引用变量时，会优先在当前命名空间内查找，如果没有再向外部寻找

# gl_num = 10

# def demo(num):
# 如果传递的是可变类型的参数，在函数内部使用方法修改参数内容，会影响到外部的数据
# num.append(4)

# print(num)

# gl_num1 = [1,2,3]
# demo(gl_num1)
# print(gl_num1)

# # 如果对列表变量使用 += 操作，是不会对列表相加再重新赋值的操作，本质上是调用了列表的extend()方法
# gl_num2 = [1,2,3]
# gl_n = 20
# def num(num):
#     # num += num
#     # num = num+num
#     num.extend(num)
#     print(num)

# num(gl_num2)
#
# dic = [1,2,3]
# dic1 = (1,2,"xm")
# dic2 = "zhangsna"
# dic3 = 4
# dic += dic
# dic.extend(dic)
# print(dic)

# 缺省参数
# 给函数参数指定一个默认值，方便调用

# def class_a(name,gender=True):
#     """
#     判断学生性别
#     :param name: 学生姓名
#     :param gender: 学生性别
#     :return: 返回判断结果
#     """
#     # if gender == True:
#     #     gender_text = "男生"
#     #     print("%s的性别是%s" % (name, gender_text))
#     # if gender == False:
#     #     gender_text = "女僧"
#     #     print("%s的性别是%s" % (name, gender_text))
#     gender_t = "男生"
#     if not gender:
#         gender_t = "女生"
#     print("%s 的性别是 %s" % (name,gender_t))
#
# print(class_a("laowang",gender=False))

# 多个缺省参数，调用时必须指定参数名
# def fonc(name, tatle="", gender_a=True):
#     gender_n = "男生"
#     if not gender:
#         gender_n = "女生"
#     print("%s %s的性别是 %s " % (tatle,name,gender_n))
#
# fonc("小明",gender_a=True)

# 多值参数

# def sum_num(*args):
#     num = 0
#     for n in args:
#         num += n
#     return num
#
#
# print(sum_num(1, 2, 3, 4, 5))

# 拆包语法
# tup = (1,2,3)
# dic = {"name":"xm","age":19}
# def dome(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# dome(*tup,**dic)
# dome(1,2,3,name="xm",age=19)

# 递归函数

# def sum_num(num):
#
#     print(num)
#     if num == 1:
#         return
#     sum_num(num - 1)
#
# sum_num(4)

# 计算1～n之间的数字累加

def num_sum(nums):
    """

    :param nums: 需要累加的数字
    :return: 返回累加的结果
    """
    if nums == 1:
        return 1
    temp = num_sum(nums - 1)
    return nums * temp


# def num_sum2(num):
#     n = num
#     for i in range(1,n):
#         n *= i
#     return n

# #
# num_sum(10)
# print(num_sum(10))
#
# list_num = []
# print(dir(num_sum))
# print(num_sum.__doc__)
# print(list_num.__add__())

# 使用递归函数检查一个字符串是否是回文

# def hui_wen(s):
#     # 定义基线条件
#     if len(s) < 2:
#         return True
#     # 判断第一个和最后一个字符是否一样
#     elif s[0] != s[-1]:
#         return False
#     # 执行递归，判断剩余字符串
#     return hui_wen(s[1:-1])
#
# print(hui_wen("a"))
#
# 命名空间与作用域

# glb_name = "xm"
# scope = locals()
# print(scope)

# 向命名空间内添加一个键值对，就相当于在全局作用域中增加类一个变量
# scope["age11"]= 18
# print(scope)

# globals()函数可以在任意位置获取全局命名空间

# def num():
#     a = 10
#     # scope = locals()
#     scope = globals()
#     scope["glb_name"] = "zhangsan"
#     return scope
#
# print(num())


# 高阶函数练习
# l = [1,2,3,4,5,6,7,8,9]
#
#
# # 获取列表中的偶数
# def fn1(i):
#     if i % 2 == 0:
#         return True
#     return False


# def fn2(i):
#     if i % 2 != 0:
#         return True
#     return False
#
# def fon(fonc,n):
#     """"""
#     m = []
#     for i in n:
#         if fonc(i):
#             m.append(i)
#     return m

# 匿名函数
# r = filter(lambda i : i % 2 != 0,l)
# print(list(r))
#
# # sort方法与sorted()函数
# # sort方法是列表的内置方法，只有可变序列可以调用
# # sorted()函数是python内置函数，可以对任意可变序列做排序，并且返回一个新序列
# l = [1,3,5,7,9,2,4,6,8,"9"]
# l1 = ["abc","hello","word"]
# l1.sort(key=len)
# print(l1)
# print(sorted(l))

# 闭包--函数嵌套
ls1 = [1, 2, 3, 4, 5, 6]

def make():
    # ret = []
    def avg(num):
        # ret.append(num)
        # print(ret)
        return sum(num) / len(num)

    return avg



r = make()
# ret = zhuangshiqi(make)
print(r(ls1))
