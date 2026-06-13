def find_treasure(start_x, learning_rate=0.01, max_iter=10000, tolerance=1e-6):
    def df(x):
        return 4 * (x ** 3) - 9 * (x ** 2)
    x = start_x
    for _ in range(max_iter):
        gradient = df(x)
        x_new = x - learning_rate * gradient
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    return x

# 测试 1：从 x=0 开始找
result1 = find_treasure(start_x=0.0)
print("从 x=0.0 出发，找到宝藏位置 x =", result1)

# 测试 2：从 x=5 开始找（很远的地方）
result2 = find_treasure(start_x=5.0)
print("从 x=5.0 出发，找到宝藏位置 x =", result2)

# 测试 3：从 x=-1 开始找
result3 = find_treasure(start_x=-1.0)
print("从 x=-1.0 出发，找到宝藏位置 x =", result3)
