import math
from scipy import stats

def calculate_confidence_interval(data, confidence_level):
    # 步骤1：计算样本量和样本均值
    n = len(data)
    mean = sum(data) / n
    
    # 步骤2：计算样本标准差（分母n-1，无偏估计）
    squared_deviations_sum = sum((x - mean) ** 2 for x in data)
    sample_std = math.sqrt(squared_deviations_sum / (n - 1))
    
    # 步骤3：计算标准误
    standard_error = sample_std / math.sqrt(n)
    
    # 步骤4：计算自由度
    df = n - 1
    
    # 步骤5：计算双侧t临界值
    alpha = 1 - confidence_level
    t_critical = stats.t.ppf(1 - alpha / 2, df) 
    
    # 步骤6：计算边际误差
    margin_of_error = t_critical * standard_error
    
    # 步骤7：计算置信区间上下界
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    
    # 整理成字典返回，保留小数位数和题目示例对齐
    return {
        'mean': round(mean, 4),
        'standard_error': round(standard_error, 4),
        'margin_of_error': round(margin_of_error, 3),
        'lower_bound': round(lower_bound, 3),
        'upper_bound': round(upper_bound, 3),
        'confidence_level': confidence_level
    }

# 测试题目示例
data = [10, 12, 11, 13, 14, 10, 12, 11]
result = calculate_confidence_interval(data, 0.95)
print("置信区间结果：", result)