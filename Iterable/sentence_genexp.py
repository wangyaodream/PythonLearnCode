import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text)) #生成器表达式是一个语法糖，完全可以替换换成生成器函数，有时候使用生成器表达式更便利

    