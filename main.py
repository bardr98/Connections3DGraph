import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv(r"Connections.csv")

# Map categorical variables to numerical codes
data['Company_code'], _ = pd.factorize(data['Company'])
data['Position_code'], _ = pd.factorize(data['Position'])

# Initialize plot
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='3d')

# Create color map
cmap = plt.get_cmap('viridis')

# Plot data
x = data['Company_code']
y = data['Position_code']
z = 149
for i in range(len(x)):
    colors = [cmap(i / len(x)) for i in range(len(x))]
    ax.scatter(x, y, z, s=50, alpha=0.6, c=colors)

# Set axis labels
ax.set_xlabel('Company', labelpad=10, fontsize=10)
ax.set_ylabel('Position', labelpad=10, fontsize=10)
ax.set_zlabel('Number of Connections', labelpad=10, fontsize=10)

# Set tick labels
ax.set_xticks(range(len(data['Company'])))
ax.set_yticks(range(len(data['Position'])))
ax.set_xticklabels(data['Company'], rotation=90, fontsize=0.2)
ax.set_yticklabels(data['Position'], fontsize=0.2)

# Adjust tick spacing
ax.tick_params(axis='x', pad=20)
ax.tick_params(axis='y', pad=20)

# Show plot
plt.show()
