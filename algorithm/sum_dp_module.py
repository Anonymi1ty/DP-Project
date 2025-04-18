import math
import numpy as np

class SumDP:
    """
    Wrapper class for the SumDP algorithm.
    
    Parameters:
        epsilon: Privacy budget ε
        beta: Failure probability, used for threshold selection
        U: Upper bound of data domain, must be a power of 2 (e.g., U = 2^L)
    """
    def __init__(self, epsilon, beta, U):
        self.epsilon = epsilon
        self.beta = beta
        self.U = U
        self.L = int(math.log2(U))
    
    def run(self, x_list):
        """
        Run the SumDP algorithm on the input data list.
        
        Input:
            x_list: A list of integers, each belonging to {0} ∪ [1, U]
            
        Output:
            final_sum: The aggregated and noise-added sum
            tau: The selected clipping threshold (satisfying Max(D) ≤ τ ≤ 2·Max(D))
            noisy_sums: A dictionary recording the noisy sum for each subdomain j (for debugging/analysis)
        """
        # Partition the data: each non-zero value will fall into exactly one interval
        interval_values = {j: [] for j in range(0, self.L + 1)}
        for x in x_list:
            if x == 0:
                continue
            # If x == 1, assign to j = 0; otherwise j = ceil(log2(x))
            j = 0 if x == 1 else int(math.ceil(math.log2(x)))
            j = min(j, self.L)
            interval_values[j].append(x)
        
        # Apply BaseSumDP mechanism on each subdomain: add Laplace noise to the true sum
        noisy_sums = {}
        for j in range(0, self.L + 1):
            true_sum = sum(interval_values[j])
            scale = (2 ** j) / self.epsilon
            noise = np.random.laplace(loc=0.0, scale=scale)
            noisy_sums[j] = true_sum + noise
        
        # Threshold selection: find the largest j where noisy_sum[j] > T_j
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
