# 生成器函数
# 生成器——一边循环一边计算的机制，依次产生按生成器内部运算产生的数据
# 返回一个迭代对象，只能用于迭代操作
# 函数体中包含yield关键字（专门用于生成器的return）
    # 作用相当于return，但只返回一次计算值
    # return语句仍然可以使用但其返回值不能被获取,且导致无法继获取下一个值抛出异常Stop Iteration
# 可以使用next()迭代，每次next()只会返回一次yield指然后暂停于当前位置,执行到结尾抛出异常Stop Iteration



from re import T


def add():
    sum=0
    for i in range (10):
        sum+=i
        yield sum
g=add()
print(g)
print(next(g))
print(next(g))

# 括号匹配问题

def check_parents(text):
    # 括号配对检查函数,text是被检查的正文串
    parents="()[]{}"
    open_parents="([{"
    opposite={")":"(","]":"[","}":"{"}

    def parents_gen(text):
        # 括号生成器.每次调用返回下一括号及其位置
        i, text_len=0,len(text)
        while True:
            while i<text_len and text[i] not in parents:
                i+=1
            if i>= text_len:
                # 用于终止迭代
                return
            yield text[i],i
            i+=1

    st=[]
    for pr, i in parents_gen(text):
        if pr in open_parents:
            st.append(pr)
        elif st.pop(-1) !=opposite[pr]:
            print("unmatching is found at",i,"for",pr)
            return False
    if st:
        print("unmatched for open_parent(s) last")
    else:
        print("all are matched")
    return True
check_parents("()(")