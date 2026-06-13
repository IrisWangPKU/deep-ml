import math  

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    func_dict = {
        'square': (lambda val: val ** 2, lambda val: 2 * val),
        'sin': (math.sin, math.cos),       # 改成 math.xxx
        'exp': (math.exp, math.exp),
        'log': (math.log, lambda val: 1 / val)
    }

    values = [x]
    for func_name in reversed(functions):
        forward_func, _ = func_dict[func_name]
        next_val = forward_func(values[-1])
        values.append(next_val)

    gradient = 1.0
    for func_name, val in zip(functions, reversed(values[:-1])):
        _, deriv_func = func_dict[func_name]
        gradient = gradient * deriv_func(val)
    
    return gradient

test_functions = ['sin', 'square']
test_x = 2.0
result = compute_chain_rule_gradient(test_functions, test_x)
print(f"计算结果: {result}")