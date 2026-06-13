
import math

def llama3_rope_rescale(inv_freq, original_context_length, low_freq_factor, high_freq_factor, scaling_factor):
    # 计算高低频波长阈值
    low_freq_wavelen = original_context_length / low_freq_factor
    high_freq_wavelen = original_context_length / high_freq_factor
    
    adjusted_inv_freq = []
    for freq in inv_freq:
        # 计算当前逆频率对应的波长
        wavelen = 2 * math.pi / freq
        
        if wavelen > low_freq_wavelen:
            # 低频区：直接缩放
            new_freq = freq / scaling_factor
        elif wavelen < high_freq_wavelen:
            # 高频区：保持不变
            new_freq = freq
        else:
            # 中频区：平滑插值
            smooth = (original_context_length / wavelen - low_freq_factor) / (high_freq_factor - low_freq_factor)
            new_freq = (1 - smooth) * (freq / scaling_factor) + smooth * freq
        
        # 四舍五入到6位小数
        adjusted_inv_freq.append(round(new_freq, 6))
    
    return adjusted_inv_freq

# 测试题目示例
input_inv_freq = [0.5, 0.05, 0.005]
result = llama3_rope_rescale(input_inv_freq, 2048, 1, 4, 2)
print(result)  # 输出: [0.5, 0.05, 0.003025]
