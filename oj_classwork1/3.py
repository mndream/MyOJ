'''
倒置个数
描述

有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，即i<j但是A[i]>A[j]则称它们是一个倒置，
设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)
输入
输入有多行，第一行整数T表示为测试用例个数，后面是T个测试用例，
每一个用例包括两行，第一行的一个整数是元素个数，第二行为用空格隔开的数组值。
输出
输出每一个用例的倒置个数，一行表示一个用例。
输入样例
1
8
8 3 2 9 7 1 5 4
输出样例
17

暴力求解
'''
def count(A):
    num = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if (A[i] > A[j]):
                num += 1
    return num
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(count(A))