# 队列类的list实现

from cmath import e
from multiprocessing.spawn import old_main_modules


class SQueue():
    def __init__(self,init_len=8):
        self._len=init_len          #存储区长度
        self._elems=[0]*init_len    #元素存储
        self._head=0                #表头元素下标
        self._num=0                 #元素个数

    def is_empty(self):
        return self._num==0

    def peek(self):
        if self._num ==0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    def dequeue(self):
        if self._num ==0:
            raise QueueUnderflow
        e=self._elems[self._head]
        self._head=(self._head+1)%self._len
        self._num-=1
        return e
    
    def enqueue(self,e):
        if self._num ==self._len:
            # 按需扩展存储区
            pass
        self._elems[(self._head+self._num)%self.len] =e
        self._num+=1

    def __extend(self):
        # 扩展存储区:每次扩展1倍
        old_len=self._len
        self._len*=2
        new_elems=[0]*self._len
        for i in range(old_len):
            new_elems[i] =self._elems[(self._head+i)%self._len]
        self._elems, self._head=new_elems,0

class QueueUnderflow(ValueError):
    pass
