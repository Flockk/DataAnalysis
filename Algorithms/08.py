def days_to_cut_all_trees(A, K, B, M, X):
    left, right = 0, X * max(A, B)
    while right - left > 1:
        mid = left + (right - left) // 2
        if (mid - mid // K) * A + (mid - mid // M) * B >= X:
            right = mid
        else:
            left = mid
    return right


A, K, B, M, X = map(int, input().split())
print(days_to_cut_all_trees(A, K, B, M, X))
