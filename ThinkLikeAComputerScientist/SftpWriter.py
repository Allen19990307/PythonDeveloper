# sftp sftpuser02@10.80.10.94:/sftpuser/E-commerceIndustryData/BrandData_TM_Season/197001/BrandData_TM_Season.csv   /data/E-commerceIndustryData/BrandData_TM_Season/197001/
# !/usr/bin/python
# coding=utf-8
import paramiko
import os
import stat


def sftp_download(sftp, localDir, remoteDir):
    # if remoteDir.find(".") == -1:#判断远程目录参数是否是目录，前提是远程的文件名中都包含扩展名，否则此方法不可用，比较靠谱的方法用下面这个
    if stat.S_ISDIR(sftp.stat(remoteDir).st_mode):  # 如果sftp服务端的remoterDir是目录，则返回True
        for file in sftp.listdir(remoteDir):
            remoteDirTmp = os.path.join(remoteDir, file)
            localDirTmp = os.path.join(localDir, file)
            sftp_download(sftp, localDirTmp, remoteDirTmp)
    else:
        localPath = localDir.rpartition("/")[0]
        if not os.path.exists(localPath):  # 如果本地目录不存在，则创建
            os.makedirs(localPath)  # 可创建多级目录
        print("download file:", remoteDir)
        try:
            sftp.get(remoteDir, localDir)
        except Exception as e:
            print('download exception:', e)


if __name__ == '__main__':
    host = '10.80.10.94'  # sftp主机
    port = 22  # 端口
    username = 'sftpuser02'  # sftp用户名
    password = 'Wu#wcn02.14'
    localDir = '/data/idp/E-commerceIndustryData'
    remoteDir = '/sftpuser/E-commerceIndustryData'  # 远程文件或目录
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    sftp_download(sftp, localDir, remoteDir)
    sf.close()

