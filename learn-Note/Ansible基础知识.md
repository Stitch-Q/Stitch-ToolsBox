### 1. Ansible command模块

使用方法：

```bash
ansible 主机名或者主机组名 -m command -a 命令内容
```

command 模块在远端主机执行方法：

- 当在管理节点执行ansible命令的时候，会将命令作为py文件，拷贝到需要执行的主机目录下的.ansible目录下，然后执行.py文件

command模块的执行：

**选项**：

- chdir ----执行命令之前先执行目录切换

- creates ----判断目录是否存在，不存在则执行，存在则跳过

- removes ----判断目录是否存在，存在则执行，不存在则跳过

- 使用方法：

  ```bash
  ansible 主机名或者主机组名 -m command -a 'chdir=/opt/install date'
  ```

修改默认登录用户：

修改/etc/ansible/host文件，在主机IP后增加  ansible_ssh_user=用户名  ansible_ssh_pass=密码 参数



### 2. Ansible 远程主机批量提权操作（sudo)

### 3. ansible 之shell，raw模块

shell模块：

​	用于再远程节点上执行命令，用法和command一样，不过shell模块在执行命令的时候使用的事/bin/sh，所以shell模块可以在执行机上执行任何命令。

官方建议，command 模块用起来更安全，更有可预知性

raw 模块：

​	raw模块功能类似于前面说的command，shell能够完成的操作，raw模块也都能完成，不同的是，raw模块不需要远程主机上安装python环境

​	通常可以用于执行机无法安装python环境，或者执行机中python版本不能满足要求的情况 

### 4、ansible 之script模块

### 5、ansible 之 ping、file 模块

### 6、ansible 之 copy模块

### 7、ansible 之 service模块

### 8、ansible 之 cron 模块

### 9、ansible 之 yum模块，usr模块

### 10、ansible 之synchronize模块

### 11、ansible 之setup模块、get_url模块

### 12、playbook 简介于playbook文件格式

### 13、playbook文件的组成于语法

### 14、playbook 的使用于案例解析





​			

​	