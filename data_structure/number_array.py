#最基本的数据结构——数组
# Python中常用list表述数组，这里数组的定义无需指定长度，且可以动态增长，不断向后追加元素，一般不会出现数组溢出

# 一维数组

Arr=[1,2,3,4]
# print(Arr[0])

# 二维数组
Arr_2=[[1,2,3],[4,5,6]]
# print(Arr_2[0][1])

# 定义数组的常用方式之一
Array=[[0 for i in range(4)] for i in range(3)]
# print(Array)

# 数组的操作

## 增加
Array=[1,2,3,4]
Array.append(5)
# print(Array)

## 删除
Array=[1,2,3,4,1,5,4]
#移除列表中某个值的第一个匹配项
# Array.remove(1)
#print(Array)

#移除列表中的一个元素（默认最后一个，可以按索引删除），返回删除元素的值
# print('被删除的元素：',Array.pop())
# print('删除后的数组：',Array)
# print('指定索引删除的元素：',Array.pop(0))

#按照索引删除元素
# del Array[1]
# print(Array)

#清空
Array.clear()
# print(Array)

## 插入
#将指定对象插入到列表指定位置
Array=[1,2,3,4]
Array.insert(0,0)
# print(Array)

## 查找 修改
#是否含有 in

#某元素在数组中第一次出现的索引
Array=[4,2,3,4]
Index=Array.index(4)
# print(Index)

#修改直接通过索引修改

## 反转
Array.reverse()
# print(Array)

## 排序(默认升序)
#直接对原数组进行重新排序
Array.sort()
# print(Array)
Array.sort(reverse=True)
# print(Array)

#额外空间保存排序后数组
# print(sorted(Array))
# print(Array)

## 截取
Array=[1,2,3,4,1,5,4]
# print(Array[0:6:2])#步长为2
# print(Array[::-1]) #从右往左取
