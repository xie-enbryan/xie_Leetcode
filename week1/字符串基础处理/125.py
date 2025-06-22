# 输入： 一个字符串
# 输出： 返回bool值，是回文就返回true，不是回文返回false
# 操作： 1. 移除非字母，非数字的字符。 2. 将所有的字母都转换成小写的字母
# 遍历这个字符串，
    # 如果这个字符是非字母，非数字，那么就移除掉
    # 如果是字母，判断是不是小写，或者说直接转成小写
    # 如果是数字，直接保留
import re


# 处理完所有的字符后，进行字符之间的比较
# 第一个与最后一个比较，第二个与倒数第二个比较这样子 。。。。

def is_Same_words (s: str) -> bool:
    new_s =""
    for char in s:
        if char.isalnum():
            if char.isalpha():
                new_s += char.lower()
            elif char.isdigit():
                new_s +=char
    new_s_1 = ""
    for char in reversed(new_s):
        new_s_1 += char

    if new_s == new_s_1:
        return True
    else:
        return False

## 上面那种写法是对的，不过太复杂了，
# GPT给出了一种比较简单的写法,思路跟上面是一样的
# 遍历字符，把数字和字母变成小写，非数字字母的不用管
# 然后比较字符与反转后的字符是否相等
def update_is_same_word (s: str) -> bool:
    for char in s:
        if char.isalnum():
            new_s = ''.join(char)

    return new_s == new_s[::-1] # 这个叫做切片处理，[start, end, step],
                               # 从start的字符开始，到end位置的字符结束，step=1表示正向遍历，-1 表示负向遍历


#  使用双指针思路，
# 也就是一边遍历，然后一个左指针从左边头部到尾部去遍历， 一个右指针从右边尾部到头部去遍历
# 当遍历到非字母，非数字时， 指针直接跳过这个字符，遇到字母和数字时，就直接比较
# 最后如果有不相等的字符，直接返回False， 如果全部都相等，那么我们就返回True
# 结束这个循环的条件就是，当我左指针比右之指针大时，即左指针遍历到了右边的区域时，结束这个循环。

def check_is_same_word (s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            if not s[left].isalnum():
                left +=1
                continue  # 加了这个，跳回 while 循环，不执行后面比对！
            if not s[right].isalnum():
                right -=1
                continue # 加了这个，跳回 while 循环，不执行后面比对！

            if s[left] != s[right]:
                return  False
            left +=1
            right -=1

        return True


# 使用正则表达式， 正则表达式也是一样的思路，进行数据的清洗， 然后用python切片进行比较。
# 正则表达式[pattern, replacement, string]。
# pattern: 表示要正则匹配的模板，replacement 要用来替换的东西， 最后一个就是字符串。

def update_check_is_same_word (s: str) -> bool:
     new_s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
     return new_s == new_s[::-1]








