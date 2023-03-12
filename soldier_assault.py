# 小案例3
# 士兵突击
# 士兵拥有一把AK47，可以开枪
# 枪里面没有子弹，可手动装填子弹，再开枪


# 定义枪类
class Gun:
    # 枪的属性初始化
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    # 装填子弹
    def load_gun(self, count):
        self.bullet_count += count
        print("子弹已装满 %d 发，可以再次开火" % count)

    # 开火
    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s]没有子弹了。。。" % self.model)
            return
        self.bullet_count -= 1
        print("[%s]哒哒哒.... %d" % (self.model,self.bullet_count))


# 创建枪对象
AK47 = Gun("AK47")

# 装填子弹
# AK47.load_gun(50)

# 开火
# AK47.shoot()


# 定义士兵类
class Soldier:
    # 初始化属性
    def __init__(self,name):
        self.gun = None
        self.name = name

    # 士兵行为
    def fire(self):
        # 判断士兵是否有枪
        if self.gun == None:
            print("[%s]还没有枪。。。" % self.name)
            return
        # 判断枪里是否有子弹
        if self.gun.bullet_count <= 0:
            print("[%s]里没有子弹，先装填子弹"% self.gun.model)
            self.gun.load_gun(50)
        # 开枪
        self.gun.shoot()



# 创建士兵对象
xusanduo = Soldier("许三多")
xusanduo.gun = AK47
xusanduo.fire()