


class BinTNode:
    # 二叉树结点类
    def __init__(self,dat,left=None,right=None) -> None:
        self.data=dat
        self.left=left
        self.right=right
t=BinTNode(1,BinTNode(2),BinTNode(3))

def count_BinTNodes(t):
    # 统计树中结点个数
    if t is None:
        # 对空树的处理
        return 0
    else:
        # 递归
        return 1 + count_BinTNodes(t.left)+count_BinTNodes(t.right)


# 遍历算法的实现
## 深度优先遍历（递归方式定义函数）

def preorder(t,proc): # proc是具体的结点数据操作
    '''
    根优先
    '''
    assert(isinstance(t,BinTNode))
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)

## 宽度优先遍历


# 输出二叉树
def print_BinTNodes(t):
    if t is None:
        print("^",end="") #空树输出
        return
    print("("+str(t.data),end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")",end="")

print_BinTNodes(t)