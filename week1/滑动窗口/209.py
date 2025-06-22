# 输入： 一个含有 n 个正整数的数组和一个正整数 target
# 输出： 返回一个长度
# 操作： 其总和大于等于 target 的长度最小的 子数组
# 如果不存在符合条件的子数组，返回 0

# 思路：
# 我先给它排序，假设，我排好序后数组=[4,3,3,2,2,1]
# 接着，我就按照从大到小依次加起来，假设， 我给的target是9， 那么我就可以4+3+2

def find_ideal_nums (nums:list[int], target:int) -> int:

    # 如果整个加起来都< target， 那么就返回0
    if sum(nums) < target:
        return 0
    # 如果刚好=target， 那就直接返回原数组长度
    elif sum(nums) ==  target:
        return len(sum())
    else: # 这是最复杂的情况， 当sum(nums) > target 时， 就表明，这里面有可能有可以组成target的子数组
        mapping = {}


# 最笨的办法，就是每个数都从头加到尾， 看看哪种方式的长度最短，这种方式简单粗暴
def find_ideal_nums (nums: list[int], target: int) -> int :
    # 先计算它数组的长度，
    # 并且定义一个最大值，就是说，我见过一个最大值，比任何数都大，这样我们后面遍历到的数组和都会比这个值小，方便用min函数方法获取
    # 接着我们定义两层遍历，第一层先取第一个数。 第二层遍历，对取到的第一个数，依次往后+，
    # 接着我们就去判断相加得到的数和target进行对比，方便我们用min函数操作，得到最小的长度，
    # 最后返回长度
    n = len(nums)
    res = float ('inf') # 初始化一个很大的值，
    for i in range(n): # 取得第一个数
        total = 0
        for j in range(i, n): # 将i与后面的数，逐个相加
            total += nums[j]

            if total >= target:
                res = min(res, j-i+1)  # 获取最小长度
                break

    return res if res!=float('inf') else 0

# 最优解法，滑动窗口
def update_find_minSubarray (nums: list[int], target: int) -> int:
    left = 0 # 定义一个窗口左边的初始值
    res = float('inf')
    total = 0

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1
    return  res if res != float ('inf')  else 0









    pass


