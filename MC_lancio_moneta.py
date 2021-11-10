import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def mean(values, N):
    m = sum(values)/N
    return m


N_variables = 300
N_iterations = 10000
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

# Plot of the frequencies
plt.hist(no_heads, bins='auto')
plt.show()

