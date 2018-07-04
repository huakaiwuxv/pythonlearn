def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C',' '])))


def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
#for n in primes():
    #if n < 1000:
        #print(n)
    #else:
    #   break



print(sorted([36, 5, -12, 9, -21]))
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#装饰器
def now():
    print('2015-3-25')
f = now
f()

print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now1():
    print('2015-3-25')
now1()

#偏函数
print(int('12345'))
print(int('12345',base=8))
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))

