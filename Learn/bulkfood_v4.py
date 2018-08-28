class Quantity:
    _count = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._count
        self.storage_name = '_{}#{}'.format(prefix,index)
        cls._count += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance,self.storage_name)

    def __set__(self, instance, value):
        if type(value) is not str:
            if value >0:
                setattr(instance,self.storage_name,value)
            else:
                raise ValueError('value must be > 0')
        else:
            if len(value) > 5:
                setattr(instance, self.storage_name, value)
            else:
                raise ValueError('the length must be > 5')


class LineItem:
    weight = Quantity()
    price = Quantity()
    def __init__(self,description,weight,price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__=='__main__':
    print(LineItem.weight)