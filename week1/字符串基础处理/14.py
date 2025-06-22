# 输入： 一个字符串数组
# 操作，从他们的头开始，选出各个元素，重复的部分
# 返回： 重复的部分

# 这应该是可以仿照双指针的，一个写，一个读。正常是每个list都拿一个出来比较，相同就记录，不相同就返回空
def  find_same_words (strs: str) -> str:
    # 写入的数组
    same_part = []
    for i in range(len(strs)): # 遍历原来的数组
        same_part[i]  =  list (str(strs[i])) # 将
        if same_part[i] != list(str(strs[i+1])):
            return None
    return str(same_part)

# 按照机器的思考逻辑，你应该是两两比较，比较完，得出相同的部分，相同的部分再去比较下一个元素
# 因为你遍历，一次只能遍历一个不，
# 遍历，肯定是要遍历的，遍历完跟谁比，跟第一个比，那要把第一个拿出来
def update_find_same_begin_words (strs: list[str]) -> str:
    # 自己容易写成if str == "": 去判空，实际上是错的，这里的对象类型是字符串列表，不是单独的字符串，你这个是判断字符串的
    # 况且，python里面判空，一般用if not xxx: 去判断是不是空 not “”=True
    if not strs:
        return "" # 空输入就返回空

    prefixe = strs[0]
   # 跳出循环条件这里也不是很懂

    # 这里的循环条件设置的也不是很懂
    # 自己经常写for i in range(len(strs)): 这种是拿索引值，这种通常用在双循环，需要索引值的情况下
    # 而这里这种for s in strs[1:]: 这里是直接拿列表里的值，s是用来赋值的，拿了一个列表strs的值，就直接赋值给s
    for s in strs[1:]:
        while not s.startswith(prefixe):
            # 这一步也是盲区，怎么在一个元素内，抹去掉最后一个字符
            # 我们的prefixe是一个字符串，而字符串也是有索引的，因此我们可以用prefixe[0,1,2,3,4]来指定索引，
            # 这里的prefixe[:-1]就是去掉最右边的索引值， 然后赋值给新的prefixe
            prefixe = prefixe[:-1]
            if prefixe == "":
                return ""
    return prefixe

def Reupdate_find_same_begin_words(strs:list[str])-> str:
    if not strs:
        return ""
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startwith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


















