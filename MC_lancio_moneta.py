import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt

def mean(values, N):
    m = sum(values)/N
    return m


def std(average_p, N):
    s = sqrt((average_p*(1-average_p))/N)
    return s


def t(p_true, p_est, sigma):
    t = abs(p_est - p_true)/sigma
    return t


N_variables = 300
N_iterations = 1000
results = []
no_heads = []

# Iterations for MC simulation
for n in range(N_iterations):
    xi = [np.random.uniform() for i in range(N_variables)]
    events = []
    # Splitting interval into two bins each representing 1/2
    # probability.
    for number in xi:
        if number < 0.5:
            events.append(0)
        else:
            events.append(1)
    results.append(events)

# Counting the 'heads' results
count = [dict(Counter(result)) for result in results]
for dictionary in count:
    no_heads.append(dictionary[1])

# Evaluation of estimated probability
average_value = mean(no_heads, N_iterations)
print(average_value)

# Compatibility test to estimate if spikes in the histogram are compatible with
# the calculated errors.

average_probability = average_value/N_variables
error = std(average_probability, N_iterations)
t_value = t(0.5, average_probability, error)

print(t_value)

# Plot of the frequencies
chosen_bins = [i for i in range(0, N_variables, 1)]
plt.hist(no_heads, bins=chosen_bins)
plt.show()

