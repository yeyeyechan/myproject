﻿# 인수 :


## default arugument:

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    
    while True:
       
       ok = raw_input(prompt)
       
       if ok in ('y', 'ye', 'yes'):
            
            return True
       
       if ok in ('n', 'no', 'nop', 'nope'):
       
       return False
       
       retries = retries - 1
       
       if retries < 0:
       
       raise IOError('refusenik user')
       
       print complaint

•giving only the mandatory argument: ask_ok('Do you really want to quit?')


•giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)

•or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



>>>>  default 설정이 된인자는 위와 같이 초기화때 값을 지정 안해도 된다.



## 주의

i = 5

def f(arg=i):
    print arg

i = 6
f()


>>>>  위의 값은 5이다. 디폴트 값은 함수 정의 부분에서 평가 되기 때문에 .(검토)

def f(a, L=[]):
    L.append(a)
    return L

print f(1)

print f(2)

print f(3)

>>>>  다만 디폴트 값은 오직 한번만 평가 되기 때문에 위와같이 계속 호출되는경우엔 결국 
 

리스트 L이 [1,2,3] 이 된다. 인수 누적

def f(a, L=None):

if L is None:

L = []

L.append(a)

return L


>>>>  디폴트가 공유되지 않게 하려면 위와 같이 하면된다.

f(1)
f(2)
f(3)
[1] / [2]  / [3]  출력



## keyword argument

>>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):


print "-- This parrot wouldn't", action,

print "if you put", voltage, "volts through it."

print "-- Lovely plumage, the", type

print "-- It's", state, "!"


parrot(1000)                                          # 1 positional argument

parrot(voltage=1000)                                  # 1 keyword argument

parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments

parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments

parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments

parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


parrot()                     # required argument missing

parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument

parrot(110, voltage=220)     # duplicate value for the same argument

parrot(actor='John Cleese')  # unknown keyword argument


>>>>  키워드 인자는 항상 위치 인자 다음에 나와야 한다. 위치 인자도 키워드 인자처럼 입력 가능하고

>>>>  키워드 인자 사용시 순서는 중요치 않음
(다시 보기!!)



## Arbitrary Argument List


>>>> def write_multiple_items(file, separator, *args):

file.write(separator.join(args))


(다시 보기!!)



## 언패킹



## 람다 

