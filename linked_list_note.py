

#创建节点类
class Node:
    #创建节点
    #两个属性，数据域和指针域
    def __init__(self,data):
        self.data=data #数据域
        self.next=None #指针域
        return
    #一个方法：判断链内是否存在某一值的节点
    def has_value(self,value):
        if self.data==value:
            return True
        else:
            return False
#定义一个值为1的新节点
node1=Node(1)
# print(node1.next)

#创建单链表类
class singlelink:
    #3个属性，头节点、尾节点、链表长度
    def __init__(self):
        self.head=Node(1)
        self.tail=None
        self.length=0
        return
    #方法
    def isempty(self):
        """
        判断列表是否为空
        :return:
        """
        return self.length==0

    def add_node(self,item):
        """
        向链表结尾添加节点
        :param item:
        :return:
        """
        if not isinstance(item,Node):
            #判断是否为实例
            #isinstance Return whether an object is an instance of a class or of a subclass thereof.
            item=Node(item)

        if self.head is None:
            self.head=item
        else:
            self.tail.next=item
            self.tail=item
            self.length+=1
        return item

    def insert_node(self,index,data):
        if self.isempty():
            print("this link is empty")
            return
        if index <0 or index>=self.length:
            print("error: out of index")
            return
        item =Node(data)
        if index==0:
            item.next=self.head
            self.head=item
            self.length+=1
            return
        j=0
        node=self.head
        prev=self.head
        while node.next and j <index:
            prev=node
            node=node.next
            j+=1
        if j == index:
            item._next=node
            prev._next=item
            self.length+=1

sl=singlelink()
print(sl)
print(sl.length)
print(sl.head)
print(sl.head.next)
print(sl.head.data)