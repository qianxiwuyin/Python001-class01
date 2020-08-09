学习笔记


__dict__ 查看属性
__fly 属性 防止人为错误修改

@classmethod :构造函数，__new__只能再一个类中构造一次，他能构造多次
用途：父类与子类；方法调用做预处理

@staticmethod:静态方法，不定义self，作为转化和判断的功能

__getattribute__ ：属性存在或者不存在都会拦截

__getattr__ 对于不存在__dict__中的属性，就会拦截，对相应的处理返回想要的属性,

两者同时存在，执行顺序：优先__getattribute__ ；
getattribute会影响性能，getattr虽然会改变行为，但是再dict中

属性描述符
property 并不是函数是特殊类，
实现get和set方法 被称为数据描述符
只实现了get是非数据描述符
用途：可以设置属性访问权限，提高数据安全性
比如 有些数据设置不可以修改，

类的继承
当前类或者父类继承了object类 是新式类，否则是经典类，有object就是
type元类创建 type类 ，元类type 创建object类
type父类是object，object没有父类

父子类的概念和区分
1.可以实现多重继承和多个父类
2.要继承父类的东西可以使用super()
多重继承顺序问题
新式类 广度优先，经典类是深度优先，父类到父类搜寻
再使用广式类的时候 先进行广度优先查询，没有之后再进行深度优先
查看钻石继承关系的过程 class.mro()
有向无环图

分析思路
5个原则和设计模式
工厂模式
静态创建类 常见
动态创建类 少用，一般用于框架，django


元类type
元类要求必须实现new方法，写框架的时候需要

抽象基类
不能进行实列化

mixin 类
改变类的顺序，插入信息


