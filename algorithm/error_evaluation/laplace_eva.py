import numpy as np
import math

class LaplaceExperiment:
    """
    实验类，用于计算标准 Laplace 机制的实验误差以及理论误差上界
    """
    def __init__(self, laplace_instance, x_list):
        """
        参数:
            laplace_instance: LaplaceMechanism 类的实例
            x_list: 实验数据列表
        """
        self.algorithm = laplace_instance
        self.x_list = x_list
        self.true_sum = sum(x_list)
        self.sensitivity = laplace_instance.sensitivity
        self.epsilon = laplace_instance.epsilon
    
    def run_experiment(self, n_trials=1000):
        """
        重复调用 Laplace 机制 n_trials 次，返回平均绝对误差和标准差
        """
        errors = []
        for _ in range(n_trials):
            noisy_sum, _ = self.algorithm.run(self.x_list)
            errors.append(abs(noisy_sum - self.true_sum))
        return np.mean(errors)
    
    def theoretical_error_bound(self, beta=0.05):
        """
        Laplace 机制的理论误差上界（常见置信范围：~95%）
        """
        return self.sensitivity / self.epsilon * math.log(1 / beta)

   