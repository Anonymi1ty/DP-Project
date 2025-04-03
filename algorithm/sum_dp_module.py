import math
import numpy as np

class SumDP:
    """
    SumDP 算法封装类
    
    参数:
        epsilon: 隐私预算 ε
        beta: 失败概率，用于阈值选择
        U: 数据上界，必须为 2 的幂（例如 U = 2^L）
    """
    def __init__(self, epsilon, beta, U):
        self.epsilon = epsilon
        self.beta = beta
        self.U = U
        self.L = int(math.log2(U))
    
    def run(self, x_list):
        """
        对输入数据 x_list 运行 SumDP 算法
        
        输入:
            x_list: 一个整数列表，每个元素属于 {0} ∪ [1, U]
            
        输出:
            final_sum: 聚合后的加噪求和结果
            tau: 选定的剪切阈值（满足 Max(D) ≤ τ ≤ 2·Max(D)）
            noisy_sums: 一个字典，记录每个子域 j 的加噪和（用于调试和分析）
        """
        # 将数据分区，每个非零值只会落入一个区间
        interval_values = {j: [] for j in range(0, self.L + 1)}
        for x in x_list:
            if x == 0:
                continue
            # 若 x==1，则归入 j=0，否则 j = ceil(log2(x))
            j = 0 if x == 1 else int(math.ceil(math.log2(x)))
            j = min(j, self.L)
            interval_values[j].append(x)
        
        # 对每个子域执行 BaseSumDP 随机化：真实和加上 Laplace 噪声
        noisy_sums = {}
        for j in range(0, self.L + 1):
            true_sum = sum(interval_values[j])
            scale = (2 ** j) / self.epsilon
            noise = np.random.laplace(loc=0.0, scale=scale)
            noisy_sums[j] = true_sum + noise
        
        # 阈值选择：遍历每个子域 j，计算 T_j，并选出最后一个满足 noisy_sum(j) > T_j 的 j
        j_star = None
        for j in range(0, self.L + 1):
            T_j = 1.3 * (2 ** j) * math.log(2 * (self.L + 1) / self.beta) / self.epsilon
            if noisy_sums[j] > T_j:
                j_star = j
        if j_star is None:
            return 0, None, noisy_sums
        
        tau = 2 ** j_star
        final_sum = sum(noisy_sums[j] for j in range(0, j_star + 1))
        return final_sum, tau, noisy_sums