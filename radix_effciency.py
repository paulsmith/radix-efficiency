import numpy as np
import matplotlib.pyplot as plt

def digits_in_base(n, base):
    if n == 0:
        return 1
    return int(np.log(n) / np.log(base)) + 1

def radix_economy(n, base):
    return base * digits_in_base(n, base)

# Generate x values (represented numbers)
x = np.logspace(0, 10, num=1000)

# Calculate radix economy for bases 2 to 16
bases = range(2, 21)
y = {base: [radix_economy(n, base) for n in x] for base in bases}

# Create the plot
plt.figure(figsize=(12, 8))
for base in bases:
    plt.plot(x, y[base], label=f'Base {base}')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Represented Number')
plt.ylabel('Radix Economy (radix * digits)')
plt.title('Radix Efficiency for Different Bases')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Add text annotation to highlight base 3
plt.text(1e9, 100, 'Base 3 becomes\nmost efficient\nfor large numbers', 
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

plt.show()
