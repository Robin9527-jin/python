# 接下来用一个小案例来演示一下python中继承的概念

# 子类可以继承父类的属性和方法，不需要再次开发
# 子类只需要根据职责，去封装子类特有的属性和方法即可

# 继承相关的专业术语
#     Dog类继承Animal类 --- Animal是Dog的父类 --- Dog是Animal的类继承
#     Dog是Animal的派生类 --- Animal是Dog的基类 --- Dog从Animal类中派生

# 继承的传递行
#     子类继承父类相同的属性和方法，也可以继承父类的父类拥有的属性和方法
#     如：A类继承类B类的属性和方法，C类又继承B类，那么C类就具有A类和B类相同的属性和方法

# 方法的重写
#   当父类中的方法和属性不能满足子类的需求时，可以在子咧中重写一个与父类方法同名的方法
#   子类调用该方法时，会调用子类内部重写的方法，不会调用父类中的方法

# 定义一个动物类

class Animal:
    # 吃的方法
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def dark(self):
        print("汪汪叫")

# 定义一个狗类
class Dog(Animal):  #Animal作为Dog的父类，在定义子类的时候以参数的形式传递进来
    # 初始化属性
    def __init__(self,name):
        self.name = name


# 定义一个鸟类
class Bird(Dog):  # 继承Dog类的同时，相当于把Animal类的属性传递给Bird类
    # def __init__(self,name):
    #     self.name = name
    def dark(self):   # 方法的重写
        print("[%s]吱吱吱吱。。。" % self.name)
    def fly(self):
        print("飞翔。。。")


# 创建狗对象
dog = Dog("旺财")
dog.eat()
dog.drink()
dog.run()
dog.sleep()
dog.dark()

# 创建鸟对象
bird = Bird("大鹏")
bird.eat()
bird.drink()
bird.run()
bird.sleep()
bird.dark()
bird.fly()


