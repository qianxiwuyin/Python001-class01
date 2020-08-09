
class AnimalMixin(object):
    def Cat(self,name,type,size,nature):
        self.name = name
        if  size !='中' and type =='食肉' and  nature=='凶猛':
            print('不适合作为宠物')
        else:
            print('适合作为宠物')
class Cat(AnimalMixin):
    voice = True
    def __init__(self, name, type, size, nature):
        self.name = name
        self.type = type
        self.type = size
        self.type = nature
    def Cat(self):
        return super().Cat()

class Zoo(object):
    def __init__(self,name):
        self.name = name
        self.animal = []
    #判断是否有动物生成
    def add_animal(self, i):
        if i in self.animal:
            raise Exception("已存在此动物")
        else:
            self.animal.append(i)

    def __getattr__(self, item):
        return False

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')

    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'cat1')