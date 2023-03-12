def zhuangshiqi(old):

    def new_fonc(*args,**kwargs):
        print("%s 计算开始。。。。" % old.__name__)
        ret = old(*args,**kwargs)  #old就是原函数
        print("计算结束。。。")
        return ret  # 返回函数计算结果
    return new_fonc  #把装饰函数作为返回值返回


# 三层函数嵌套
# 定义一个装饰器，在函数执行前需要输入执行的描述
def decorator(execute):
    # 定义扩展功能
    def new_decor(old):
        #内部处理
        def ret(*args,**kwargs):
            print("开始执行。。。")
            r = old(*args,**kwargs)
            return r  #返回原函数执行结果
        return ret #返回函数处理结果

    print("执行结束。。。")
    return new_decor


# @zhuangshiqi
@zhuangshiqi
def fn(a,b):
    return a + b

print(fn(1,2))

