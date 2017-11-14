import sys

def search(origin_string, string):
    """
        查找string是否存在于origin_string中
    """
    match_table = partial_match_table(string)
    index = 0
    j = 0 
    o_end_index = len(origin_string)
    s_end_index = len(string)
    flags = False
    while index < o_end_index:
        if j >= s_end_index:
            flags = True
            break
        if string[j] == origin_string[index]:
            index += 1
            j += 1
        else:
            index = max(j - 1 - match_table[j-1], index + 1)
            j = 0
    if index >= o_end_index and j >= s_end_index:
        flags = True

    return flags

def partial_match_table(string):
    """获取部分匹配表"""
    match_table = [-1] * len(string)
    index = 1
    i = len(string) + 1
    while index < i:
        sub_string = string[:index]
        prefix_list = prefix(sub_string)  # 获取前缀表
        suffix_list = suffix(sub_string)  # 获取后缀表
        max_match_len = get_max_length(prefix_list, suffix_list)
        match_table[index-1] = max_match_len
        index += 1
    return match_table

def get_max_length(prefix_list, suffix_list):
    """处理前,后缀表, 获取最大匹配长度"""
    sub_match_list = [len(s) for s in prefix_list if s in suffix_list]
    if sub_match_list:
        return max(sub_match_list)
    return 0

def prefix(sub_string):
    """
       获取字符串的前缀(除了字符串的最后一个字符的所有
       子字符串)(abcde: [a, ab, abc, abcd])
    """
    prefix_list = list()
    index = 1
    i = len(sub_string)
    while index < i:
        prefix_list.append(sub_string[:index])
        index += 1
    return prefix_list

def suffix(sub_string):
    """
        获取字符串的后缀(除了字符串的首字母之外的所有
        子字符串)(abcde: [bcde, cde, de, e])
    """
    suffix_list = list()
    index = 1
    i = len(sub_string)
    while index < i:
        suffix_list.append(sub_string[index:])
        index += 1
    return suffix_list
    

if __name__ == '__main__':
    origin_string = sys.argv[1]
    string = sys.argv[2]
    print(search(origin_string, string))
