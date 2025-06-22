# 输入： 一个字符串
# 操作： 括号必须配对，左括号与右括号配对
# 输出：bool值（括号能否有效闭合配对）

# 用Counter计数器，分别计算左括号，右括号的数量
# 如果左括号数量=右括号数量，那就是能闭合，返回True
# 如果左括号数量！=右括号数量，那就是无法闭合，返回False
# Counter后，得到： {'(': 2, ']':3,  ')': 6, '[': 8}

from collections import  Counter

def check_bracket (self, s: str) -> bool:
    s_count = Counter(s)

    if s_count.get('(', 0) == s_count.get(')', 0):
        if s_count.get('[', 0) == s_count.get(']', 0):
            if s_count.get('{', 0) == s_count.get('}', 0):
                return True

    return False

# 以上的想法只匹配了数量，没有考虑到结构，举个反例 就能击破逻辑
# [)(}]{, 它们的数量都是相等的，但是结构不成型，应该返回False，但是用上面的方法返回的是True

# GPT的想法：  用栈，
# 我先把遇到的左括号，都拿个袋子（栈） 存起来，当遇到右括号时，我就把栈里的左括号拿出来，看看是不是跟这个右括号配对的，
# 如果最后栈为空，那么就是True，因为左括号和右括号完全配对，如果不为空，就是左括号比右括号多，或者说右括号比左括号多。
def checkValid (s: str)-> bool:
    # 准备一个袋子用来装左括号
    stack = []

    # 这个mapping主要用来判断是左括号还是右括号
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # 如果拿出来的是右括号
        if  char in mapping:#右括号
            # 首先判断你这个袋子有没有东西
            if not stack:
                return False
            # 走到这一步，证明你袋子确实有东西，那我们就拿一个出来
            top = stack.pop()

            # 我怎么知道拿出来的是不是我要的括号？
            if top != mapping.get(char):
                return False

        # 如果拿出来的是左括号
        else: #
            stack.append (char)

    return not stack






