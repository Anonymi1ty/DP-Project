import numpy as np
import math

class LaplaceExperiment:
    """
    Experiment class for evaluating the empirical and theoretical error of the standard Laplace mechanism.
    """
    def __init__(self, laplace_instance, x_list):
        """
        Parameters:
            laplace_instance: An instance of the LaplaceMechanism class
            x_list: List of input data values for the experiment
        """
        self.algorithm = laplace_instance
        self.x_list = x_list
        self.true_sum = sum(x_list)
        self.sensitivity = laplace_instance.sensitivity
        self.epsilon = laplace_instance.epsilon
    
    def run_experiment(self, n_trials=1000):
        """
        Repeatedly run the Laplace mechanism n_trials times and return the average absolute error.
        """
        errors = []
        for _ in range(n_trials):
            noisy_sum, _ = self.algorithm.run(self.x_list)
            errors.append(abs(noisy_sum - self.true_sum))
        return np.mean(errors)
    
    def theoretical_error_bound(self, beta=0.05):
        """
        Compute the theoretical upper bound on the Laplace mechanism’s error 
        under a typical confidence level (~95%).
        """
        return self.sensitivity / self.epsilon * math.log(1 / beta)
