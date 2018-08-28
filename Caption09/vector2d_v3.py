from array import array
import math

class Verctor2d:
    typecode = 'd' #vector2d 实例和字节序列之间转换时使用

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y


    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode,self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))


    #hash
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)




    #计算极坐标
    def angle(self):
        return math.atan2(self.y,self.x)

    # def __format__(self, format_spec=''):
    #     components = (format(c,format_spec) for c, in self)
    #     return "({},{})".format(*components)

    def __format__(self,fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self),self.angle())
            outer_fmt = '<{},{}>'
        else:
            coords = self
            outer_fmt = '({},{})'
        components = (format(c,fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    #classmethod 装饰器是python专用的

def main():
    v1 = Verctor2d(3,4)
    print(format(v1,'p'))


if __name__=='__main__':
    main()