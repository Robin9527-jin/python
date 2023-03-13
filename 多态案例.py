# 接下俩用一个小案例来演示一下 多态

# 定义狗的基类
class Dog(object):
    def __init__(self,name):
        self.name = name
    # 狗的行为
    def game(self):
        print("[%s]在蹦蹦跳跳的玩耍。。。" % self.name)

# 定义狗类
class FlyDog(Dog):  # 继承基类
    def game(self):  # 方法重写
        print("[%s]在天上飞来飞去。。。" % self.name)


# 定义人类
class Persion(object):
    def __init__(self,name):
        self.name = name
    # 人的行为
    def game_with_dog(self,dog):  #与狗狗玩耍,将狗对象作为参数传递
        # print("[%s]在和[%s]快乐的玩耍。。。" %(self.name,dog.name))
        dog.game()


# 创建啸天犬
xiaotianquan = FlyDog("啸天犬")
# 创建旺财
dog = Dog("旺财")

# 创建人对象

xiaoming = Persion("小明")
xiaoming.game_with_dog(dog)
xiaoming.game_with_dog(xiaotianquan)