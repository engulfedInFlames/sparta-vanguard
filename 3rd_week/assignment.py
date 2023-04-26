# 파스칼의 삼각형
memo = {
    1: [1],
    2: [1, 1],
}


def func(n: int, memo: dict):
    memo[n] = []
    for i in range(n):
        if i == 0 or i == n - 1:
            memo[n].append(1)
        else:
            pre_arr = memo[n - 1]
            memo[n].append(pre_arr[i - 1] + pre_arr[i])


def pascal(n: int, memo: dict):
    if n in memo:
        return memo[n]

    for i in range(1, n + 1):
        func(i, memo)

    return memo[n]


pascal(8, memo)
print(memo)
