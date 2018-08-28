class Quantity:
    def __init__(self,storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if type(value) is not str:
            if value >0:
                instance.__dict__[self.storage_name] = value
            else:
                raise ValueError('value must be > 0')
        else:
            if len(value) > 5:
                instance.__dict__[self.storage_name] = value
            else:
                raise ValueError('the length must be > 5')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')
    description = Quantity('description')

    def __init__(self,description,weight,price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__=='__main__':
    obj = LineItem("test instance",10,-30.6)
    #obj 是一个LineItem的实例
    print(obj.subtotal())
