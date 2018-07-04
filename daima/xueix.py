'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#print(fact(6))
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
#print(L)
L=list(range(100))
#print(L)
print(L[:10])
print(L[-10:])
print(L[-10::2])

for ch in 'ABC':
    print(ch)
    
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for i,value in enumerate(['a','b','c']):
    print(i,value)
    '''
'''
L=[x*x for x in range(1,11)]
print(L)
import os # 导入os模块，模块的概念后面讲到
L=[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(L)
'''
'''
g=(x*x for x in range(10))
for n in g:
    print(n," ", end="")
print('\n')

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        #print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
h=fib(6)
while True:
    try:
        x=next(h)
        print('h:',x," ",end="")
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
def triangles():  
    N=[1]  
    while True:  
        yield N        #generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行  
        N.append(0)  
        N=[N[i-1] + N[i] for i in range(len(N))]  #写法  
  
if __name__ == '__main__':  
    n=0  
    for t in triangles():  
        print(t)  
        n=n+1  
        if n == 10:  
            break  

f=abs
print(f(-10))
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))
'''
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
print(r)
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
from functools import reduce
def add(x, y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))
