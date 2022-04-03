# 由n个有限节点组成的一个具有层次关系的集合
# 二叉树：每个节点上最多有2个子树的树结构

# 二叉树性质
## 第k层上的节点数，最多2^(k-1)
## 深度为h的二叉树的节点数，最多2^h-1个
## 包含n个节点的数敢赌，至少log2(n+1)
## 任意二叉树，叶子节点数n0，度为2的节点为n2，则n0=n2+1

## 常见二叉树：满二叉树、完全二叉树、平衡二叉树、搜索二叉树

# 二叉树的实现
# 二叉树的每个节点都是node类对象，通过Tree类中的add()方法逐个项树中加入节点

from platform import node
from re import T


class Node():
    def __init__(self,val=None,left=None,right=None) -> None:
        '''
        节点值和节点指针域（左右指针）
        '''
        self.value=val
        self.left=left
        self.right=right

class Tree():
    def __init__(self,node=None) -> None:
        #根节点
        self.root=node

    def add_node(self,item=None):
        node=Node(val=item)
        if not self.root:
            self.root=node
        else:
            #遍历各个节点，检查左右指针域：空则添加子节点；非空当前子节点入队，进入下次循环
            # 下次循环队列内节点检查并添加子树（节点）
            queue=[]
            queue.append(self.root)
            while True:
                current_exist_node=queue.pop(0)
                if current_exist_node.value is None:
                    #检查空值节点，不存储
                    continue
                if not current_exist_node.left:
                    current_exist_node.left=node
                    return
                elif not current_exist_node.right:
                    current_exist_node.right=node
                    return
                else:
                    queue.append(current_exist_node.left)
                    queue.append(current_exist_node.right)
tree=Tree()

# 自定义的二叉树
for i in range(10):
    if i==3:
        i=None
    tree.add_node(i)