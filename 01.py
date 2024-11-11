import os
def isDir(remote_path,fileName):
    # path_01 = os.path.join(remote_path,fileName.strip('./')).replace('\\','/')
    if os.path.isdir(fileName):
            for file in os.listdir(fileName):
                print(file,'222222222')
                local_01 = os.path.join(fileName,file).replace('\\','/')
                print(local_01,'33333333')
                isDir(local_01,file)
    else:
        create_remote_file = os.path.join(remote_path, fileName.strip('/')).replace('\\','/')
        print(create_remote_file)

# isDir('/www/code/','./test_01')


def fi(path_file):
    remote_path=''
    if os.path.isdir(path_file):
          for file in os.listdir(path_file):
               remote_path = os.path.join(path_file,file).replace('\\','/')
               print(remote_path)
               fi(remote_path)
    else:
         return remote_path


fi('./test_01')