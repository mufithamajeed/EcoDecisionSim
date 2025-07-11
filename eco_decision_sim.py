import numpy as np
import matplotlib.pyplot as plt

# Population Dynamics Simulation

def simulate_population(K, r, N0, t_max, noise_std=0):
    """
    Simulate stochastic logistic population growth.

    Parameters:
    - K: Carrying capacity
    - r: Growth rate
    - N0: Initial population size
    - t_max: Number of time steps
    - noise_std: Standard deviation of environmental noise

    Returns:
    - N: Array of population sizes over time
    """
    N = [N0]
    for t in range(1, t_max):
        growth = r * N[-1] * (1 - N[-1] / K)
        noise = np.random.normal(0, noise_std)
        N.append(max(N[-1] + growth + noise, 0))
    return np.array(N)


# Parameters
K = 1000          # Carrying capacity
r = 0.1           # Growth rate
N0 = 100          # Initial population
t_max = 100       # Number of time steps
noise_std = 20    # Environmental variability

# Simulations: No Action vs With Action
no_action = simulate_population(K, r, N0, t_max, noise_std)
with_action = simulate_population(K, r * 0.8, N0, t_max, noise_std)  # Management reduces growth rate

plt.figure(figsize=(10, 6))
plt.plot(no_action, label='No Management Action')
plt.plot(with_action, label='With Management Action')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Population Dynamics with and without Management Action')
plt.legend()
plt.grid(True)
plt.show()

# Value of Information (VOI)

def value_of_information(cost_of_learning, benefit_of_better_decision, prob_of_correct_decision):
    """
    Calculate the expected Value of Information (VOI) for a decision under uncertainty.

    VOI = (Benefit X Probability of Correct Decision) - Cost of Learning

    Parameters:
    - cost_of_learning: Cost of gathering better information
    - benefit_of_better_decision: Expected benefit (e.g., avoided losses, higher yield)
    - prob_of_correct_decision: Probability that new information leads to correct action

    Returns:
    - voi: Estimated Value of Information
    """
    voi = (benefit_of_better_decision * prob_of_correct_decision) - cost_of_learning
    return voi


# Example VOI calculation
cost = 50
benefit = 300
prob = 0.7

voi = value_of_information(cost, benefit, prob)
print(f"Estimated Value of Information: {voi:.2f} units")
