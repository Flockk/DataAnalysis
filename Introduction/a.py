# Координаты точки A
ax, ay = 1, 2

# Координаты точки B
bx, by = 5, 6

# Расстояние между точками A и B
dist = pow((pow((ax - bx), 2) + pow((ay - by), 2)), 0.5)
print(dist)