def solve():
    inf = float('inf')
    s = list(input())
    k = int(input())
    n = len(s)

    # 首先预处理，将每个子串变为回文的修改次数
    g = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(n - 2, -1, -1):
        for r in range(l + 1, n):
            g[l][r] = (1 if s[l] != s[r] else 0) + g[l + 1][r - 1]

    # f(i, j)表示将前缀s[0..j]分割成至多i个子串，且每个子串都是回文的最少修改次数
    f = [[inf for _ in range(n)] for _ in range(k + 1)]
    # prev(i, j) 记录 f(i, j) 的转移来源
    prev = [[-1 for _ in range(n)] for _ in range(k + 1)]

    for j in range(n):
        f[1][j] = g[0][j]
        prev[1][j] = 0

    for i in range(2, k + 1):
        # 前面分割成至多i个，后面分割成至少k - i个
        for j in range(i - 1, n - k + i):
            # 最后一个子串的左端点
            for left in range(i - 1, j + 1):
                if f[i - 1][left - 1] + g[left][j] < f[i][j]:
                    f[i][j] = f[i - 1][left - 1] + g[left][j]
                    prev[i][j] = left

    # 找到最小修改次数和对应的分割数
    ans = inf
    best_i = -1
    for i in range(1, k + 1):
        if f[i][n - 1] < ans:
            ans = f[i][n - 1]
            best_i = i

    print(ans)

    # 回溯路径，记录子串并将其改为回文串
    path = []
    i = best_i
    j = n - 1
    while i > 0:
        left = prev[i][j]
        sub_s = s[left:j + 1]
        # 将子串变为回文串
        for l in range(len(sub_s) // 2):
            r = len(sub_s) - 1 - l
            if sub_s[l] != sub_s[r]:
                sub_s[l] = sub_s[r]
        path.append(''.join(sub_s))
        j = left - 1
        i -= 1

    # 反转路径，因为是从后往前回溯的
    path.reverse()
    print('+'.join(path))


if __name__ == "__main__":
    solve()