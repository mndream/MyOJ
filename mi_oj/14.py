'''
在一个有序的经过旋转的数组里查找一个数
假设一个有序的数组，经过未知次数的旋转（例如0 1 2 4 5 6 7 被旋转成 4 5 6 7 0 1 2），
从中查找一个目标值，如果存在，返回其下标，不存在，返回-1。注：假设数组无重复数字
输入一个有序经过旋转的数组和要查找的目标数字，数组中各数字用“逗号”分隔，数组和目标数字用“空格”分隔
输出一个整数，表示该目标数字的下标（不存在返回-1）
输入样例
4,5,6,7,0,1,2 6
输出样例
2
'''
def solution(line):
    a, b = line.strip().split()
    a = a.split(",")
    for i in range(len(a)):
        if a[i] == b:
            return str(i)
    return str(-1)

print(solution(input()))