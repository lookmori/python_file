# f = open('score.csv','r')
# a = []

# for i in f:
#     a.append(i.strip().split(','))
# f.close()
# print(a)


# for i in a:
#     s= ''
#     for j in i:
#         s+=j+" "
#     print(s)



# i = ['wang','86','90','99']
# for j in i:
#     s= ''
#     print(j)
#     print('{:6}\t'.format(j),'---')
#     print(f"{j[:6]}\t")
"""
count = 0

list = []
for i in range(0,1000):
    if i%3 == 0:
        a = i%10
        b = i//10%10
        c = i//10//10%10
    if c == 5:
        count+=1
    list.append(i)
    print("这样的三位数有：",list)
    print("总数量有：",count)
"""


# fruit 是变量
fruit = input('请输入你喜欢的水果？')
print(fruit)