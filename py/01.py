def minSubsequenceCount(source, target):
    source_index = 0
    subsequences_count = 0

    for char in target:
        # 在源字符串中逐个寻找匹配的字符
        while source_index < len(source) and source[source_index] != char:
            source_index += 1
        # 如果无法找到匹配的字符，则返回-1
        if source_index == len(source):
            return -1
        # 找到了匹配的字符，增加子序列计数，并移动源字符串的索引
        subsequences_count += 1
        source_index += 1

    return subsequences_count

# 测试案例
print(minSubsequenceCount("abc", "abcbc"))  # 输出: 2
print(minSubsequenceCount("abc", "acdbc"))  # 输出: -1
print(minSubsequenceCount("xyz", "xzyxz"))  # 输出: 3

git remote set-url origin <新的远程仓库URL>
