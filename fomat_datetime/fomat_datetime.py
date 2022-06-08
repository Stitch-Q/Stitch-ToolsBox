"""
author: stitch
date：2022年4月11日
readme: 批量修改执行机主机时间，避免时间不一致导致偶现问题
        主机的增减可以通过修改配置文件来实现
"""
import time
import logging
import paramiko
from time import strftime, localtime


def recordlog():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(filename)s : %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %A %H:%M:%S",
        filename='./log.txt',
        filemode='w'
    )


def ssh_commect(node_ip, passwd, locatime):
    host_ip = node_ip
    user_name = 'root'
    host_port = 22

    # 整理需要执行的命令
    now_datetime = 'date'
    change_datetime = "date -s %s" % locatime

    # 拼接命令
    command = now_datetime + ';' + change_datetime

    # 开始建立远程连接
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(host_ip, host_port, user_name, passwd)

    # 开始执行命令并获取执行结果
    stdin, stout, stderr = ssh.exec_command(command)
    out = stout.readline()
    err = stderr.readline()

    # 执行完成，关闭ssh连接;等待两秒钟，确认命令执行完成
    ssh.close()
    time.sleep(2)

    return out, err


# 读取配置文件
def read_nodefile(file_path):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            # 配置文件中需要添加备注，对备注信息做判断并打印
            if line[0] == '#':
                env_name = line[1:-1]
                logging.info("********开始处理%s" % env_name)
                continue
            # 执行修改时间命令，时间为当前机器当前时间
            else:
                local_time = strftime("%Y-%m-%d %A %H:%M:%S", localtime())
                node_ip, username, passwd = line.strip().strip(":")
                try:
                    logging.info("======开始处理 %s ======" % node_ip)
                    logging.info("===当前本地时间为%s===" % local_time)
                    res = ssh_commect(node_ip, passwd, local_time)
                    logging.info("=====%s处理完成=====" % node_ip)
                    return node_ip, res
                except Exception as e:
                    logging.warning("-------------%s处理失败----------" % node_ip)
                    return "未知错误", e


if __name__ == "__main__":
    filepath = './node.cfg'
    recordlog()
    Node_ip, msg = read_nodefile(filepath)
    print("****%s执行结果: %s" % (Node_ip, msg))
