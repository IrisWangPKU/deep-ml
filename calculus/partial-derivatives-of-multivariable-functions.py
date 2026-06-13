# 1. 定义函数：输入x,y，算结果
def poly2d(x, y):
    return x**2 * y + x * y**2

# 2. 核心函数：算变化率
def numerical_partial_derivatives(func, point, h=0.00001):
    partials = []          # 空袋子，装结果
    n_vars = len(point)    # 数有几个变量
    
    # 循环：有几个变量，就循环几次
    for i in range(n_vars):
        # 第一步：把当前变量 加一点点
        point_plus = list(point)
        point_plus[i] += h
        point_plus = tuple(point_plus)
        
        # 第二步：把当前变量 减一点点
        point_minus = list(point)
        point_minus[i] -= h
        point_minus = tuple(point_minus)
        
        # 第三步：算这个变量的变化率
        partial = (func(*point_plus) - func(*point_minus)) / (2*h)
        partials.append(partial)  # 装进袋子
    
    return tuple(partials)  # 把袋子里的结果打包返回

# 主程序
if __name__ == "__main__":
    func_name = poly2d
    point = (2.0, 3.0)
    result = numerical_partial_derivatives(func_name, point)
    print(result)