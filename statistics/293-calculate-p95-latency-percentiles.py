
def calculate_latency_percentiles(latencies):
    # 处理空列表的边界情况
    if not latencies:
        return {
            'P50': 0.0,
            'P95': 0.0,
            'P99': 0.0
        }
    
    # 第一步：数据从小到大排序
    sorted_data = sorted(latencies)
    n = len(sorted_data)
    
    # 辅助函数：计算单个百分位
    def percentile(p):
        # 计算位置
        position = (p / 100.0) * (n - 1)
        low = int(position)       # 整数部分，低位索引
        high = low + 1            # 高位索引
        frac = position - low     # 小数部分，插值比例
        
        # 如果刚好是整数，直接返回对应值
        if high >= n:
            return sorted_data[low]
        
        # 线性插值计算
        return sorted_data[low] + frac * (sorted_data[high] - sorted_data[low])
    
    # 分别计算三个百分位，保留四位小数
    return {
        'P50': round(percentile(50), 4),
        'P95': round(percentile(95), 4),
        'P99': round(percentile(99), 4)
    }


# 测试题目示例
if __name__ == "__main__":
    latencies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = calculate_latency_percentiles(latencies)
    print("延迟百分位结果：", result)