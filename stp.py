import os
import paramiko
import json
import stat


def create_sftp_file(sftp,remoteDir):
    try:
        if stat.S_ISDIR(sftp.stat(remoteDir).st_mode):
            pass
    except FileNotFoundError as e:
        print(remoteDir,'okokokokokok')
        sftp.mkdir(remoteDir)


def upload(local_path, remote_path):
    L_Lpath = local_path
    L_path = remote_path
    create_remote_file = remote_path
    """
    上传文件夹或文件到远程服务器
    """
    if os.path.isfile(local_path):
        # 是文件
        create_remote_file = os.path.join(remote_path, local_path.strip('./')).replace('\\','/')
        sftp.put(local_path, create_remote_file)
    else:
        create_remote_file = os.path.join(remote_path, local_path.strip('./')).replace('\\','/')
        if stat.S_ISDIR(sftp.stat(L_path).st_mode):
            pass
        create_sftp_file(sftp,create_remote_file)

        for file in os.listdir(local_path):
            sub_local_path = os.path.join(local_path.strip('\\')+'/', file) # ./test_01/test_0101
            upload(sub_local_path, L_path)



with open(r'./config.json','r') as f:
    k= json.load(f)
    username =str(k['username'])
    password = str(k['password'])
    host = str(k['hostname'])
    

    # 建立ssh连接
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    # 创建sftp实例
    sftp = paramiko.SFTPClient.from_transport(transport)
    upload('./md_to_pdf.py', '/www/wwwroot/code/python/')
    # 关闭连接
    transport.close()
    f.close()

