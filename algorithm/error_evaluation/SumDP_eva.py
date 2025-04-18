import math
import numpy as np


class SumDPExperiment:
    """
    Experiment class for computing the empirical and theoretical error bounds of the SumDP algorithm.
    """
    def __init__(self, sumdp_instance, x_list):
        """
        Parameters:
            sumdp_instance: An instance of the SumDP class
            x_list: List of input data values for the experiment
        """
        self.algorithm = sumdp_instance
        self.x_list = x_list
        self.true_sum = sum(x_list)
        self.max_val = max(x_list) if x_list else 0
    
    def run_experiment(self, n_trials=1000):
        """
        Run the SumDP algorithm repeatedly (n_trials times) and return the average absolute error.
        """
        errors = []
        for _ in range(n_trials):
            final_sum, tau, _ = self.algorithm.run(self.x_list)
            errors.append(abs(final_sum - self.true_sum))
        return np.mean(errors)
    
    def theoretical_error_bound(self):
        """
        Compute the theoretical upper bound on the error based on analysis:
            Bound ≈ 2.6 * Max(D) * ln(2*(L+1)/beta) / epsilon
        """
        return self.max_val * 2.6 * math.log(2 * (self.algorithm.L + 1) / self.algorithm.beta) / self.algorithm.epsilon
