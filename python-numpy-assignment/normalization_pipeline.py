import numpy as np

# Step 1: Create a NumPy array
data = np.array([10, 20, 30, 40])

# Step 2: Compute mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# Step 3: Normalize the data
normalized = (data - mean) / std

# Step 4: Reshape the normalized data into 2D
reshaped = normalized.reshape(2, 2)

# Step 5: Print outputs
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized data:", normalized)
print("Reshaped data:", reshaped)
print("Reshaped data shape:", reshaped.shape)