import os

FILE_POSITION = 'D:\一阶段'

filelist = os.listdir('D:\一阶段')
# print(filelist)  
for f in filelist:
    try:
        file_path = FILE_POSITION + '\\' + f 
        for i in os.listdir(file_path):
            if '.sb3' in i:
                del_file = file_path + '\\' + i
                print('要删除的文件地址是',del_file)
                os.remove(del_file)
    except FileNotFoundError:
        print('文件不存在')

