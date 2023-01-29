n, a, b = map(int, input().split())
count = 0
for x in range(n // a + 1):
    y = (n - a * x) // b
    if a * x + b * y == n:
        count += 1
print(count)