# 输入：  非空 整数数组 nums
# 除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 输出： 输出这个特定的元素


# 思路： 可以直接用Counter计数器，记录每个元素出现的次数，因为除了某一个特定的元素是一次，其余均是两次
from collections import Counter
def find_specific_number (nums: list[int])-> int:

    for i in range(len(nums)):
        if nums.count (nums[i]) == 1:
            return nums[i]

# 尝试使用哈希+判断来做， 做法如下：
from  collections import Counter
def update_find_specific_element (nums: list[int]) -> bool:
    new_nums = Counter(nums)
    for key, value in new_nums.items():
        if value == 1:
            return key

# 使用官方的标准解法，用异或解法XOR 它会成对的消除元素，只留下单独的那一个
def find_only_number (nums: list[int]) -> int:
    result =  0

    for num in nums:
        result ^= num # 使用异或运算
    return result






