# 输入： 字符数组，如： s = ["h","e","l","l","o"]
# 输出： 反转后的字符数组，如s= ["o","l","l","e","h"]
# 操作： 这种原地修改的，就是双指针的解法，从两头开始遍历，然后交换

def reverse_string (s: list[str]) -> list[str]:
    # 定义双指针，一个读，一个写
    # 遍历这个字符数组
    left, right = 0, len(s)-1

    while left < right :
        s[left], s[right] = s[right], s[left] ## 直接进行原地交换
        left +=1
        right -=1

    return s
