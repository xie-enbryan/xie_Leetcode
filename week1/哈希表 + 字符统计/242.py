# 输入： 两个字符串
#操作： 要判断两个单词的组成是否完全相同
# 输出： 布尔值，true false

# 伪代码思路
# 遍历其中一个字符，让它们按照字母的大小顺序进行排列
# 遍历另一个字符，同样让它们按照字母的大小顺序进行排列
# 然后比较两个字符
    # 若有一个不一样，直接返回false

# 否则，返回True

def compare_two_str(strs1: str, strs2: str) -> bool:
    strs1 = ''.join(sorted(strs1))
    strs2 = ''.join(sorted(strs2))

    if len(strs1) != len(strs2):
        return False

    for i in range(len(strs1)):
        if strs1[i] != strs2 [i]:
            return False

    return  True

def update_compare_two_str (strs1: str, strs2: str) -> bool:
    return ''.join(sorted(strs1)) ==  ''.join(sorted(strs2))



# 使用哈希表的解法
# 如果两个字符是异位词，它们中的每个字母出现的次数是一样的，
# 可以比较两个中，每个字母出现的次数，
# 然后比较两个统计结果是不是相同的，如果相同就是True， 不相同就是False
# 这里我们使用了python的内置函数块，Counter计数器，可以自动去遍历，并统计每一个字母出现的次数

from collections import Counter
def Reupdate_compare_two_str (strs1: str, strs2: str) -> bool:
    return Counter(strs1) == Counter(strs2)