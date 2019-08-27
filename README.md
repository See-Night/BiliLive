# DDMonitor
直播检测工具

#### 需要mutt+msmtp支持。
详细配置请看
>>https://my.oschina.net/u/2607319/blog/707960

** MySQL **  
```
配置MySQL用户密码
$ sudo mysql
>> use mysql;
>> update user set plugin="mysql_native_password" where user="root";
>> flush privileges;
>> update user set authentication_string=PASSWORD("新密码") where user="root";
>> flush privileges;
>> exit;

重启MySQL
$ sudo /etc/init.d/mysql restart

登录MySQL（不使用sudo权限）,如果可以登录进去就说明配置完成
$ mysql -u root -p

新建数据库
>> create database Bili_Comments character set 'utf8' collate 'utf8_general_ci';
>> exit;

```
  
** Monitor.py **  

数据库储存：
```
conn = pymysql.connect(
		host = 'localhost',
		port = 3306,
		user = 'root',           #MySQL用户名
		password = '123456',     #MySQL密码
		db = 'Monitor',    #数据库名称
		charset = 'utf8'
	)
```

** 启动 ** 
`$ python3 ~/.LiveMonitor/Monitor.py`
