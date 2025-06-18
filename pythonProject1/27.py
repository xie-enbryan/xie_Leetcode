# 输入： 给了一个数组还有一个值val
# 操作：把等于val的值给去掉，然后计算剩余的元素数量
# 输出： 去重后，数组中的元素数量，

# 遍历这个数组
# 判断遍历的值是不是=val值，
  # 如果不等于，则保留，并且计数+1
  # 如果=，则把后面的往前移，并且计数不变
  # 数组去空
  # 返回计数

def remove_element(nums: list, val: int) -> int:
    account = 0
    for i in range(len(nums)):
        if nums[i] != val:
            account +=1
    return account

# 这类题型总结：原地修改 + 双指针
#出现 “原地去重”、“原地修改数组” → 第一时间考虑：双指针（一个读一个写）
#快指针遍历，慢指针记录新数组的写入位置
# 最终返回 慢指针索引 就是结果长度
def update_remove_element (nums: list, val:int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow +=1

        return slow
