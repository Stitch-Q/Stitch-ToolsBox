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


# 解析json格式信息
def read_json(json_file):
    json.load(json_file)
    pass


# 解析自定义格式信息
def read_cfg(cfgfile):
    with open(cfgfile) as f:
        for line in f:
            if line[0] == "#":
                continue
            else:
                # noinspection PyBroadException
                try:
                    pass
                except Exception as e:
                    print("未知错误，请查看：%s" % e)
                    continue
                # 开始执行脚本
                pass


# 拼接命令(执行自动挂盘并格式化目录)
def mount_disk():

    mount = "fdisk -l;dmsetup remove_all;yes n|mkfs -t ext3 /dev/vdb;mount /dev/vdb /opt"
    # 修改文件系统静态信息文件
    edit_file = """"/dev/vdb  /opt  ext3  defaults  0  0" >> /etc/fstab;df -h"""

    # 拼接需要执行的命令
    last_cmd = mount + ";" + edit_file
    return last_cmd


def execute_cmd(hostip, password, sshcmd):
    res, err = ssh_connect(hostip, "root", password, sshcmd)
    return res, err


if __name__ == "__main__":
    configfile = "nodelist.cfg"
    read_cfg(configfile)
    print("测试")
