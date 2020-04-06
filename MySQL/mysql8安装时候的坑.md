### 源码安装，初始密码不提示你！

~~~linux
cat /var/log/mysqld.log  
~~~

如果你不知道路劲，那你久去cat /etc/my.cnf看下，里面说明了服务端，客户端的一些配置情况

什么？  my.cnf也不知道？   百度，百度，百度



### mysql8作为高版本

~~~linux

mysql> show databases;
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
mysql> use mysql;
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement

~~~

**wdnmd**,,还有那些报错提示，更新難道不會一起跟新了麽？？？？？

这个时候应该

老版本   5.5   5.6之类的

~~~linux
mysql> SET PASSWORD = PASSWORD('Xiaoming250'); 
~~~

但是  5.6 以上就行不通了吧

怎么半？

~~~Linux
mysql> ALTER USER USER() IDENTIFIED BY 'Xiaoming250';
~~~

原因分析：

MySQL版本5.6.6版本起，添加了password_expired功能，它允许设置用户的过期时间。这个特性已经添加到mysql.user数据表，但是它的默认值是”N”，可以使用ALTER USER语句来修改这个值。

输入以下命令，将账号密码强制到期：

~~~linux
mysql> ALTER USER 'xiaoming'@'localhost' PASSWORD EXPIRE;
~~~

但是我劝你善良