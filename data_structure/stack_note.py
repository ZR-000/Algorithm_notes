# 突出特点：后进先出，插入和删除均在栈顶进行，有一个顶指针top用于指示栈顶位置

# 使用数组实现，数组末端即栈顶

class Stack():
    def __init__(self) -> None:
        self.list=[]

    def length(self):
        return len(self.list)
    
    def isempty(self):
        return self.list==[]
    def push(self,d):
        self.list.append(d)
    def gettop(self):
        if self.isempty():
            raise StackUnderflow("in SStack.top()")
        else:
            return self.list[-1]
    def pop(self):
        if self.isempty():
            # return 'Stack is empty'
            raise StackUnderflow("in SStack.top()")
        else:
            return self.list.pop()
    
class StackUnderflow(ValueError):
    pass

ss=Stack()
for i in range(5):
    ss.push(i)
for i in range(6):
    ss.pop()
