def minSubsequences(source, target):
    # 创建一个字典来存储source字符串中每个字符的最后出现的索引
    last_occurrence = {}
    for i, char in enumerate(source):
        last_occurrence[char] = i

    # 初始化count变量来跟踪所需的子序列数量
    count = 0
    # 初始化指针来跟踪目标字符串中的当前索引
    pointer = 0

    while pointer < len(target):
        # 初始化变量来跟踪source字符串中的当前索引
        source_pointer = last_occurrence.get(target[pointer], -1)
        # 如果在source中找不到字符，则返回-1，因为无法形成目标字符串
        if source_pointer == -1:
            return -1
        # 否则，增加子序列的计数，并将指针移动到目标中的下一个字符
        count += 1
        pointer += 1
        # 移动source_pointer和pointer到source和target中的下一个字符
        while pointer < len(target) and source_pointer < len(source) - 1:
            source_pointer += 1
            if target[pointer] == source[source_pointer]:
                pointer += 1
    return count

# 测试用例
print(minSubsequences("abc", "abcbc"))  # 输出: 2
print(minSubsequences("abc", "acdbc"))  # 输出: -1
print(minSubsequences("xyz", "xzyxz"))  # 输出: 3
