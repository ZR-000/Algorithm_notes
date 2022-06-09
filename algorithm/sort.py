def Insertsort(nums):
    #直接插入排序
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while(j>=0 and key<nums[j]):
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

def Insertsort2(nums):
    #折半插入排序
    for i in range(1,len(nums)):
        key=nums[i]
        low=0
        high=i-1
        while (low<=high):
            mid=int((low+high)/2)
            if key>=nums[mid]:
                low=mid+1
            if key<nums[mid]:
                high=mid-1
        j=i-1
        while (j>=low):
            nums[j+1]=nums[j]
            j-=1
        nums[low]=key
    return nums

def Bubblesort(nums):
    #冒泡法排序
    for i in range(len(nums)-1):
        flag=0
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                flag=1
        if flag==0:break #没有任何冒泡行为即为顺序数组
    return nums 

def Quicksort(nums,low,high):
    #快速排序法
    '''
    @param
        nums->list
        low ->int:一次交换排序的首位元素位置
        high->int:一次交换排序的末位元素位置
    '''
    i=low
    j=high
    key=nums[i]
    while(i<j):
        while(i<j and nums[j]>=key):
            j-=1
        nums[i]=nums[j]
        while(i<j and nums[i]<=key):
            i+=1
        nums[j]=nums[i]
    nums[i]=key
    if low <(i-1):
        Quicksort(nums,low,i-1)
    if (i+1)<high:
        Quicksort(nums,i+1,high)
    return nums


if __name__=='__main__':
    a=[2,1,3,5,3,4,0]
    b=Quicksort(a,0,len(a)-1)
    print(b)