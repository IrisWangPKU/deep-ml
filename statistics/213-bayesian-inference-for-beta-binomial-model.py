
def beta_binomial_posterior(prior_alpha, prior_beta, successes, trials):
    # 步骤1：计算真实的失败次数
    failures = trials - successes
    
    # 步骤2：更新后验参数：先验计数 + 真实数据计数
    posterior_alpha = prior_alpha + successes
    posterior_beta = prior_beta + failures
    
    # 步骤3：计算后验均值
    posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)
    
    # 按题目格式返回：保留四位小数，返回元组
    return (float(posterior_alpha), float(posterior_beta), round(posterior_mean, 4))


# 测试题目示例
if __name__ == "__main__":
    result = beta_binomial_posterior(
        prior_alpha=1,
        prior_beta=1,
        successes=7,
        trials=10
    )
    print("结果：", result)