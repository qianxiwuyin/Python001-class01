学习笔记

django 创建文件夹
python manage.py startapp index 应用层
index/models.py 模型
index/views 视图

python manage.py runserver 0.0.0.0:80
改变端口号

注意 运行完之后 记得CTRL+c 停止

url调度器 urlconf 处理各种请求

django支持对url设置变量 int,str,uuid,slug,path
过滤器的方法： 正则，自定义过滤器
url 正则写法  re_path((正则匹配的值)，views.myyear,name='模板的名称绑定用') 

数据库注意点，再主init文件加入
import pymysql
pymysql.install_as_MySQLdb()

view 视图 作用 执行层，分析数据层和模板链接
render 是封装了response
response 是直接返回

快捷函数 
render 指定返回一个response的文件
redirect() 返回到传递的参数的适当url
get_object_or_404() 引发404 而不是模型异常
