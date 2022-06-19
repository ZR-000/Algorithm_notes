# 队列
# 显著特点：先进先出
#  分为双端队列和一般的单端队列

# 队列的基本结构
# 先进先出，尾部添加新元素，头部删除元素
# 建立顺序队列结构必须为其静态分配或动态申请一片连续的存储空间，并设置两个指针进行管理。一个是队头指针front，它指向队头元素；另一个是队尾指针rear，它指向下一个入队元素的存储位置
# 初始状态下，front和rear为-1；当front=rear时，队列中没有任何元素，称为空队列；每次在队尾插入一个元素是，rear增1；每次在队头删除一个元素时，front增1

# 队列的实现
# 使用数组（列表）实现，append()入队，pop()退出第一个元素出队

from queue import Queue

class queue():
    def __init__(self):
        self.list=[]

    # 入队
    def enqueue(self,item):
        self.list.append(item)

    # 出队
    def dequeue(self):
        self.list.pop(0)

    def is_empty(self):
        return len(self.list)==0
    def size(self):
        return len(self.list)

# Python的queue模块提供了队列类型Queue

Q=Queue(maxsize=2)
# If maxsize is <= 0, the queue size is infinite

# 队尾添加元素
Q.put(0)
Q.put(1)

# 队列头部取出元素，返回头部元素
print('头部元素',Q.get())

# 判断是否为空
print('是否为空',Q.empty())

# 队列当前长度
print('队列长度',Q.qsize())

# 判断队列是否达到最大长度限制
print('是否达最大长度限制：',Q.full())
print(Q.queue)