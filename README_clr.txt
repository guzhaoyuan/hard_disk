# coding: utf-8
# 安装easy_install
wget -q http://peak.telecommunity.com/dist/ez_setup.py
sudo python ez_setup.py


# 安装 mysql, python-mysql
# 安装过程中需自行设置mysql的root账号密码
sudo apt-get install mysql-server python-mysqldb

# 安装 prettytable
sudo easy_install prettytable

# 安装 xlrd
sudo easy_install xlrd

# 在当前目录中登录mysql的root账号，运行config.sql
source ./config.sql

# 在python IDE中运行Demo.py，若打印出表格，则安装成功
