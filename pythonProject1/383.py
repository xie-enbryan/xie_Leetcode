# 输入： 两个字符串
# 操作要求：判断 ransomNote 能不能由 magazine 里面的字符构成
# 输出： 返回bool值

# 一样的思路, 第一步，先把字符串，按大小顺序排好，如给定，abs, sbak
# 我就要排成abs, abks
# 做比较，我用一个计数器，来判断是不是全部在里面，
# 如果a在里面，计数器+1， 如果b在里面，计数器也+1， 如果s在里面，计数器+1
# 最终去判断计数器是不是等于字符串(abs)的长度，如果等于，那么就是全部在里面，返回True，如果不等于，就是有些不在里面，返回False

def compare_twoString (ransomNote: str, magazine: str) -> bool :
    if ransomNote is None:
        return False
    if magazine is None:
        return False

    ransomNote = ''.join(sorted(ransomNote))
    magazine = ''.join(sorted(magazine))

    count = 0
    for i in range(len(magazine)):
        if count == len(ransomNote):
            return True
        if ransomNote[count] == magazine [i]:
            count+=1

    return count == len(ransomNote)

# GPT的思路，还是用counter计数器
# 我想拼出ransomNote， 就必须要保证magazine里面有足够的字母， 数量要足够
# 那就用计数器，记录magazine里面的字母个数
# 然后遍历ransomNote里的每个字母，
    # 每用一个，就把字典里，这个字母的个数-1，
    # 如果发现这个字母根本没有，或者次数用光了，那就返回False，因为已经没有字母可以拼出来了
# 如果ransomNote所有的字母都能减掉，说明能拼出，return True
from collections import Counter
def compare_twoString (ransomNote: str, magazine: str) -> bool:
   ransomNote_count =  Counter(ransomNote)
   magazine_count = Counter(magazine)

   for char in ransomNote_count:
       if ransomNote_count[char] >  magazine_count.get(char, 0):
           return  False
   return True
