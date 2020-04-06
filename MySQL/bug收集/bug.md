错误堆栈

~~~python
Traceback (most recent call last):
  File "E:/auto/DATABASES/MySQL/code/models.py", line 59, in <module>
    client = MySQLClient(host="localhost")
  File "E:/auto/DATABASES/MySQL/code/models.py", line 43, in __init__
    self.conn = pymysql.connect(**config)
  File "D:\python\Pythonhomework\Django\virtual\env4\lib\site-packages\pymysql\__init__.py", line 94, in Connect
    return Connection(*args, **kwargs)
  File "D:\python\Pythonhomework\Django\virtual\env4\lib\site-packages\pymysql\connections.py", line 327, in __init__
    self.connect()
  File "D:\python\Pythonhomework\Django\virtual\env4\lib\site-packages\pymysql\connections.py", line 598, in connect
    self._request_authentication()
  File "D:\python\Pythonhomework\Django\virtual\env4\lib\site-packages\pymysql\connections.py", line 808, in _request_authentication
    authresp = _auth.scramble_native_password(self.password, self.salt)
  File "D:\python\Pythonhomework\Django\virtual\env4\lib\site-packages\pymysql\_auth.py", line 31, in scramble_native_password
    stage1 = sha1_new(password).digest()
  File "C:\Users\海心er\AppData\Local\Programs\Python\Python36\lib\hashlib.py", line 149, in __hash_new
    return _hashlib.new(name, data)
TypeError: object supporting the buffer API required
~~~

~~~markdown
	根据错误栈可知道  这个和密码有关系
~~~

~~~python
# 这是连接数据库pymysql.connect的参数类型   看  password  要求是字符串类型
def __init__(self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
                 charset='', sql_mode=None,
                 read_default_file=None, conv=None, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
                 connect_timeout=10, ssl=None, read_default_group=None,
                 compress=None, named_pipe=None,
                 autocommit=False, db=None, passwd=None, local_infile=False,
                 max_allowed_packet=16*1024*1024, defer_connect=False,
                 auth_plugin_map=None, read_timeout=None, write_timeout=None,
                 bind_address=None, binary_prefix=False, program_name=None,
                 server_public_key=None):
    pass

# 我的代码
def __init__(self, host, database=None, mysql_port=3306, password=123456, refresh=True):
    pass
# 典型的类型不符合   修改成字符串就行了
~~~

