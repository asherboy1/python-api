from webapicof import api       #直接导入内部实例化对象

api.sessionright()          #其中包含了 session的实例化

# api.login()     #用户名密码正确
# api.login(password='1')     #错误的密码
# api.get_customer()

api.customer_add()
api.customer_del()