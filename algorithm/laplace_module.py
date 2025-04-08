import numpy as np

class LaplaceMechanism:
    """
    Laplace Mechanism for DP sum estimation.

    Parameters:
        epsilon: Privacy budget ε
        sensitivity: Sensitivity of the sum function (usually max contribution per user)
    """
    def __init__(self, epsilon, sensitivity):
        self.epsilon = epsilon
        self.sensitivity = sensitivity

    def run(self, x_list):
        """
        Applies the Laplace Mechanism to compute a noisy sum.

        Input:
            x_list: List of numerical values (e.g., integers or floats)

        Output:
            noisy_sum: True sum plus Laplace noise
            noise: The sampled Laplace noise added
        """
        true_sum = sum(x_list)
        scale = self.sensitivity / self.epsilon
        noise = np.random.laplace(loc=0.0, scale=scale)
        noisy_sum = true_sum + noise
        return noisy_sum, noise
