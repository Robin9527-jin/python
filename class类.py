# 类的定义
# class ClaTest():
#     # 类方法的定义与函数的定义唯一区别就是方法的第一个参数必须是self
#     def num(self):
#         pass

# 【类的三要素：类名、属性、方法】

# 类的概念：
# 类就相当于是一张图纸，由类创建出来的东西就叫【对象】；对象也就是类的实例
# 类的命名规则：大驼峰命名法，每个单词的首字母要大写 ClassTest
# 类名的确定：需求中出现的名词，通常就作为类
# 属性和方法的确定：
#     对对象的特征描述，通常可以定义成属性
#     对对象行为的描述：通常可以定义成方法

# 在类中，重要有两部分构成
#     类是一个比较抽象的概念，它是一堆具有相同 特征 或 行为 的事物的统称，不能够直接使用
#     特征也叫 属性
#     行为也叫 方法
#     1，属性（数据）
#         类的属性一定要在类中定义，不能在类外面定义
#         可以在类中定义初始化方法，来给类的属性定义初始值
#         创建类对象的时候，会自动调用初始化方法
#         如果不知道要给属性定义什么初始值，可以把None作为初始值，后面可以通过对象调用属性重新赋值
#     2，方法（行为）
#         在类中的__init__()方法下面定义 self.name= 属性初始值
#         在定义属性时，如果属性值不确定，可以给方法增加一个形参，把形参作为属性值，这样就可以在创建对象时定义属性值

# __del__应用场景：
#   当一个对象在内存中销毁前，会自动调用__del__方法
#   __del__方法可以在对象被销毁前再做一些事情

# __str__应用场景：
#     当我们需要打印对象变量时，需要输出自定义内容，可以使用__str__来完成
#     __str__方法是必须要返回一个字符串的 ！！

# 封装：
#     封装是面向对象变成的一大特点
#     学习面向对象编程的正确过程是，将属性和方法封装在类中，使用类创建对象，通过对象区调用方法
#     一个对象的属性，可以时另一个类创建的对象

# class PerSion:
#     #在类中定义第一个属性
#
#     #定义一个类的初始化方法
#     def __init__(self,new_name):
#         self.name = new_name
#         print("重头再来！")
#     #在类中定义第一个方法
#     def names(self,new_name):
#         if new_name == self.name:
#             # print(name)
#             return new_name
#     def __del__(self):
#         print("毁灭吧，人类！")
#
#     def __str__(self):
#         return "%s 你来了啊" % self.name

#
# r = PerSion("小明")
# r.age = 18
# print(r.names("小明"))
# print(r)


# 小案例
# 小明爱跑步
#     小明体重 75。0公斤
#     每次吃饭会增加1公斤体重
#     每次跑步会减少1.5公斤体重

# 定义类
# class Persion:
#
#     # 定义属性初始化方法
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#     # 定义吃饭方法
#     def eat(self):
#         self.weight -= 1.5
#         print("%s 今天跑了5公里，当前的体重是 %.2f 公斤" % (self.name,self.weight))
#
#         # return self.weight
#     def runing(self):
#         self.weight += 1
#         print("%s 今天吃了炸鸡，当前体重是 %.2f 公斤" %(self.name,self.weight))
#
#
# student = Persion("张三",76)
# student.eat()
# student.runing()

# 小案例2
# 新房子增加家具

# 定义一个家具类
# class HouseItme:
#     # 给家具定义初始化属性
#     def __init__(self,name,area):
#         self.itmename = name  #家具名称
#         self.area = area    #占地面积
#
#     # 输出初始化属性
#     def __str__(self):
#         return "%s 占地面积 %.2f 平方米" % (self.itmename,self.area)
#
# table = HouseItme("餐桌",1.5)
# bed = HouseItme("水床",4.5)
# chest = HouseItme("柜子",2)
#
# print(table.itmename,bed.itmename,chest.itmename)
# print(table.area,bed.area,chest.area)
#
#
# # 定义house 类
# class House:
#     # 定义初始化属性
#     def __init__(self, house_type, house_area, free_area):
#         self.house_type = house_type
#         self.house_area = house_area
#         self.free_area = free_area
#         self.itme_list = []
#
#     # 输出初始化属性
#     def __str__(self):
#         return "%s: 总面积: %.2f, 剩余面积: %.2f，共有家具数量: %d; 名称：%s" %(self.house_type,
#                                                             self.house_area,
#                                                             self.free_area,
#                                                             len(self.itme_list),
#                                                             self.itme_list)
#
#     # 添加家具
#     def add_itme(self,itme,area):
#         self.free_area -= area
#         self.itme_list.append(itme)
#         print("恭喜你，新增了 %s,占地面积 %.2f平米"% (itme,area))
#
#
#
#
# house = House("大别野",388,388)
# house.add_itme(table.itmename,table.area)
# house.add_itme(bed.itmename,bed.area)
# print(house)



