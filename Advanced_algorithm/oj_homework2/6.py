'''
计数排序
实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
输出的每一行为排序结果，用空格隔开，末尾不要空格。
输入样例
13 24 3 56 34 3 78 12 29 49 84 51 9 100
输出样例
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(int, input().split()))
            N = inputList[0]
            orderList = inputList[1:]
            orderDict = dict()
            for i in range(len(orderList)):
                orderDict[i] = 0    # 把下标设为键，避免排序元素相同
                for j in range(len(orderList)):
                    if i != j and orderList[j] < orderList[i]:
                        orderDict[i] += 1
            res = ""
            while len(orderDict) > 0:
                for key in orderDict.keys():
                    if orderDict[key] == min(orderDict.values()):
                        res += str(orderList[key]) + " "
                        orderDict.pop(key)
                        break
            print(res.strip())
    except EOFError:
        pass