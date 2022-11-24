"""
"""
import json
import paramiko


def ssh_connect(node_ip, username, passwd, command):
    host_ip = node_ip
    user_name = username
    host_port = 22

    # 开始建立远程连接
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(host_ip, host_port, user_name, passwd)

    # 开始执行命令并获取执行结果
    stdin, stout, stderr = ssh.exec_command(command)
    out = stout.read().decode()
    err = stderr.readline()

    # 执行完成，关闭ssh连接
    ssh.close()

    return out, err


# 拼接命令并执行
def ssh_command():
    pass


# 解析配置文件，修改host_ip,密码等
def read_json():
    json.load()
    pass


if __name__ == "__main__":
    print("测试")
