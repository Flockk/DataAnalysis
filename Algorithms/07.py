def min_calc_time(N, x, y):
    left = 0
    right = (N - 1) * max(x, y)

    while right > left + 1:
        mid = left + (right - left) // 2

        if (mid // x + mid // y) >= N - 1:
            right = mid
        else:
            left = mid
    return right + min(x, y)


N, x, y = map(int, input().split())
print(min_calc_time(N, x, y))
