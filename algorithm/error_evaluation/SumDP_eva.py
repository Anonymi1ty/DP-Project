import math
import numpy as np


class SumDPExperiment:
    """
    实验类，用于计算 SumDP 算法的实验误差以及理论误差上界
    """
    def __init__(self, sumdp_instance, x_list):
        """
        参数:
            sumdp_instance: SumDP 类的实例
            x_list: 实验数据列表
        """
        self.algorithm = sumdp_instance
        self.x_list = x_list
        self.true_sum = sum(x_list)
        self.max_val = max(x_list) if x_list else 0
    
    def run_experiment(self, n_trials=1000):
        """
        重复调用 SumDP 算法 n_trials 次，返回平均绝对误差
        """
        errors = []
        for _ in range(n_trials):
            final_sum, tau, _ = self.algorithm.run(self.x_list)
            errors.append(abs(final_sum - self.true_sum))
        return np.mean(errors)
    
    def theoretical_error_bound(self):
        """
        根据理论分析，计算误差上界：
            上界估计为：2.6 * Max(D) * ln(2*(L+1)/beta) / epsilon
        """
        return self.max_val * 2.6 * math.log(2 * (self.algorithm.L + 1) / self.algorithm.beta) / self.algorithm.epsilon
