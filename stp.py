import os
import paramiko
import json
import stat


def create_sftp_file(sftp,remoteDir):
    try:
        if stat.S_ISDIR(sftp.stat(remoteDir).st_mode):
            pass
    except Exception as e:
        sftp.mkdir(remoteDir)


def upload(local_path, remote_path):
    """
    上传文件夹或文件到远程服务器
    """
    if os.path.isfile(local_path):
        # 是文件
        create_remote_file = os.path.join(remote_path, local_path.strip('./'))
        sftp.put(local_path, create_remote_file)
    else:
        # 是文件夹
        try:
            sftp.stat(remote_path)
        except FileNotFoundError:
            sftp.mkdir(remote_path)
        if os.path.isdir(local_path):
            create_remote_file = os.path.join(remote_path, local_path.strip('./'))
            create_sftp_file(sftp,create_remote_file)

        for file in os.listdir(local_path):
            sub_local_path = os.path.join(local_path.strip('./')+'/', file)
            sub_remote_path = os.path.join(create_remote_file+'/', file)
            print(create_remote_file)
            print(sub_remote_path)

            upload(sub_local_path, sub_remote_path)



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
    upload('./python学习思维导图.pdf', '/www/wwwroot/code/python/')
    # 关闭连接
    transport.close()
    f.close()

