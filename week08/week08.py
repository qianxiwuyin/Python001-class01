'''
#作业一
容器序列
list，tuple，collections.deque,dict
扁平序列
str
可变序列
list,dict，collections.deque
不可变序列
str，tuple
'''

#作业二
def add(x,y,z):
	return x,y,z
list1 = [2,3]
list2 = [1,2,3]
list3 = [1,3,4]
def testmap(function,*iterables):
    for args in zip(*iterables):
        yield  function(*args)

a=list(testmap(add,list1,list2,list3))
print(a)


#作业三
import datetime
import time

def timer(func):
    def TestFunc(*args,**kwargs):
        start = datetime.datetime.now()
        ret = func(*args,**kwargs)
        time.sleep(3)
        end = datetime.datetime.now()
        print(f'函数执行开始时间：{start}')
        print(f'开始执行结束时间：{end}')
        print(end-start)
        return ret
    return TestFunc

@timer
def test(a,b):
    print(a-b)
test(4,2)

