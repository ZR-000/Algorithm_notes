#>无须再内存中顺序存储，即可保持数据之间的逻辑关系的数据结构
#相比数组，链表执行插入、删除等操作效率大大提高
#非顺序存储，删除和插入与长度无关，只需改变指针域，时间复杂度O(1)

# 链表的基本结构

#链表：由一个个节点（Node）连接而成

#节点：由数据域（Data）和指针域（Next）构成
#数据域：存储一般是整型、浮点型等数字类型
#指针域：存储下一个节点所在内存单元地址
#单链表：每个节点的指针域只指向下一个节点
#双向链表：每个节点的指针域分为前向指针和后向指针
#单向循环链表：尾节点指针域指向头节点，链表中存在环

# 链表的实现和操作

## 创建节点

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
# node1=Node(1)


# #创建单链表
class singlelink:
    #3个属性，头节点、尾节点、链表长度
    def __init__(self):
        self.head=None
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
            self.tail=self.head
        else:
            self.tail.next=item
            self.tail=item
          
        
        self.length+=1
        return item

    def find_node(self,value):
        '''
        通过数值查找链表中的所有符合数值的节点位置
        '''
        current_node=self.head
        node_id=1
        result=[]
        while current_node is not None:
            if current_node.has_value(value):
                result.append(node_id)
            node_id+=1
            current_node=current_node.next
        return result

    def print_Slink(self):
        '''
        按顺序输出链表
        '''
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next

    def insert_node(self,index,data):    
        """
        向链表插入节点
        :param index: 插入位置
        :param data:插入数据
            
        """                                                                     
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
            item.next=node
            prev.next=item
            self.length+=1
    def delete_item_byid(self,item_id):
        '''
        通过索引删除节点

        '''
        prev=self.head
        node=self.head
        if item_id==0:
            self.head=node.next
            return node.data
        j=0
        while node.next and j<item_id:
            
            prev=node
            node=node.next
            
            j+=1
        if j==item_id:
            prev.next=node.next
            self.length-=1
        return node.data
sl=singlelink()
sl.add_node(Node(1))
sl.add_node(Node(2))
sl.add_node(Node(3))
sl.add_node(2)
sl.insert_node(1,5)
print(sl.delete_item_byid(3))
sl.print_Slink()