# import time
from datetime import datetime


timetoday = datetime.now()
print(timetoday.strftime("%H:%M:%S"))
# 定义一个可以返回函数执行时间的装饰器
def datetimes(fnc):
    print(f'{fnc.__name__} 执行完成的时间是 {datetime.now().strftime("%H:%M:%S")}')
    return fnc


@datetimes
def fn(a,b):
    return a + b

print(fn(10,20))
