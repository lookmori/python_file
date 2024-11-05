### 打印从1-1000之间所有是7的倍数的数字


## range(a,b) 从a开始，到b-1结束 
for i in range(1,1001):
    if i%7 == 0:
        print(i)