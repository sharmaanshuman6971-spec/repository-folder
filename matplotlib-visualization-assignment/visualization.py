import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs list
epochs = list(range(1, 11))

# Step 2: Generate synthetic training loss values using NumPy
np.random.seed(42)  # for reproducibility
loss = np.linspace(0.9, 0.3, 10) + np.random.normal(0, 0.02, 10)

# Step 3a: Line Plot (Loss vs Epoch)
plt.figure(figsize=(6,4))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue')
plt.title("Training Loss Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# Step 3b: Scatter Plot (Epoch vs Loss)
plt.figure(figsize=(6,4))
plt.scatter(epochs, loss, color='red')
plt.title("Scatter Plot: Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

# Step 4: Bar Chart (Model Accuracy Comparison)
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(6,4))
plt.bar(models, accuracy, color=['green','orange','purple'])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0.8, 1.0)
plt.show()