'''
按照给定数组排序
描述
Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those in A2.
For the elements not present in A2. Append them at last in sorted order.
It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
Input:A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8} A2[] = {2, 1, 8, 3}Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
Since 2 is present first in A2[], all occurrences of 2s should appear first in A[], then all occurrences 1s as 1 comes after 2 in A[].
Next all occurrences of 8 and then all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]
Constraints:1 ≤ T ≤ 501 ≤ M ≤ 501 ≤ N ≤ 10 & N ≤ M1 ≤ A1[i], A2[i] ≤ 1000
输入
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is M and N. M is the number of elements in A1 and N is the number of elements in A2.
The second line of each test case contains M elements. The third line of each test case contains N elements.
输出
Print the sorted array according order defined by another array.
输入样例
1
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
输出样例
2 2 1 1 8 8 3 5 6 7 9
'''
def sortArr(A1, A2):
    res = []
    other = []
    for i in range(len(A2)):
        for j in range(len(A1)):
            if A1[j] == A2[i]:
                res.append(A1[j])
    for i in range(len(A1)):
        isRes = False
        for j in range(len(A2)):
            if A2[j] == A1[i]:
                isRes = True
        if not isRes:
            other.append(A1[i])
    other.sort()
    res.extend(other)
    resStr = ""
    for i in range(len(res)):
        resStr += str(res[i]) + " "
    print(resStr.strip())

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        M, N = map(int, input().split())
        A1 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))
        sortArr(A1, A2)