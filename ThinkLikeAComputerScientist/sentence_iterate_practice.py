import re
import reprlib
# 使用正则表达进行sentence的拆分
from abc import abstractmethod
from collections import abc
from collections.abc import Iterable

re_word = re.compile('\w+')
class Sentence:
    def __init__(self,text):
        self.text  = text
        self.words = re_word.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
class Foo:
    def __iter__(self):
        pass
class Iterator(Iterable):
    __slots__ = ()
    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration
    def __iter__(self):
        return self
    @classmethod
    def __subclasshook__(cls,C):
        if cls is Iterator:
            if(any("__next__" in B.__dict__ for B in C.__mro__) and any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented

if __name__ == '__main__':
   s = Sentence('"I want them feel happy to grow",allen said,')
   for word in s:
       print(word)
   print('--------'+s[6])
   """判断是否是迭代器"""
   print(issubclass(Foo,abc.Iterable))
   f = Foo()
   isinstance(f,abc.Iterable)
   """使用迭代方法进行取数"""
   s3 = Sentence('Pig and Pepper')
   it = iter(s3)
   print(next(it)+' '+next(it)+' '+next(it))
   # print(next(it))
   print(list(it)+list(iter(s3)))

