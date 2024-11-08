## 变量
> 变量：变化的量。存储的内容可能发生变化。

#### 规则

* 只能由数字，字母，下划线组成
* 不能以数字开头，变量名之间不能使用空格分开
* 不能使用python关键字，或者函数
#### 语法
```python

变量名 = 值

age = 16 # 定义一个变量 age ，存储 数字16。从右往左读，将数字16赋值给变量age，= 是赋值的意思
```
## 输入输出函数

> 接受外部输入时需要用到输入函数 `input()` 。一般输入函数和变量结合使用，输入的内容都需要用变量保存，以便后边的使用(input() 函数默认会将输入的内容保存为**字符串**)

> 将内容输出让我们看到 使用输出函数（或者叫打印函数）`print()`

> **input() 括号里边一般填写的是提示信息**
```python
# 输入你的姓名并打印

# 将输入的内容存到变量name中
name =  input('请输入你的姓名：')
print(name)
print('张三')
```
**当输入的内容需要作为数字做运算时，就需要使用int()或者float()**

```python
age = int(input('请输入你的年龄'))
if age>18:
    print('我成年了')
elif age>10:
    print('我还在长个子')
else:
    print('我还是小孩子')
```
> int()  将括号里内容装为整数
> float() 将括号里内容装为浮点数
## 数学运算
||加法|减法|乘法|除法|求余|整除|判断相等|大于|小于|大于等于|小于等于|
|---|---|---|---|---|---|---|---|---|---|---|---|
||+|-|*|/|%|//|==|>|<|>=|<=|
||2+3|3-2|3*2|3/2|5%2(只要余数)|5//2(要整除部分)|5==2(判断两边是否相等，结果为True，False中一个)|3>2|3<2|4>=4|5<=7|
|结果|5|1|6|1.5|1|2|False|True|False|True|True|
## 判断

#### 对条件的判断 ，条件的结果只有两种结果，真 True，假 False
> 可以只使用if，也可以只使用if else。但是 elif 的使用，前边必须有if
```python
if 条件：
    条件成立做的事
elif 条件：
    条件成立做的事
else:
    上边条件都不成立做的事
# if 意为如果， else 意为否则， elif 意为否则如果


# 如果年龄大于18岁，打印 我成年了，如果年龄大于10岁，打印 我还在长个子，否则打印 我还是小孩子
age = 18

if age>18:
    print('我成年了')
elif age>10:
    print('我还在长个子')
else:
    print('我还是小孩子')

```
## 循环
#### for循环（有限次循环）
```python
for 变量 in range(a,b,c):
    循环体内容

# a,b,c 都是数字。 从a开始，到b-1结束，每个数字间差c 。c 默认是1


for i in range(0,11,2):
    print(i)
# 打印结果如下
# 0
# 2
# 4
# 6
# 8
# 10

for i in range(0,3):
    print(i)

for i in range(3):
    print(i)
# 这两种写法等价

# 0
# 1
# 2
```

#### while 循环（无限循环或有限循环）
**有限循环** 当条件成立时（为True）会执行循环体内容
```python
while 条件：
    条件成立做的事（循环体）

# 一个会不断减小的数字 ，刚开始它的值是10000，当它大于100时就会不断减小10
num = 10000
while num>100:
    num = num - 10
```
**无限循环**上边说过条件成立会执行循环体内容，那我们可以直接将条件结果设为True，此时变为无限循环
```python
while True:
    print('我是无限循环，我不会停止')
```
## turtle

```python
# 要使用画图，必须导入turtle ，且导入这一行尽量放在程序开头
from turtle import *

# 画一个边长为100的正方形
# A 方法
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
#B方法
for i in range(4):
    forward(100)
    left(90)
```






