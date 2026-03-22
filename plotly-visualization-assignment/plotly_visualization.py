import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
training_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.35, 0.34, 0.33, 0.33, 0.32]

# Step 2: Convert to DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": training_loss
})

# Step 3: Create interactive line chart
fig = px.line(df, x="Epoch", y="Loss", title="Training Loss Over Epochs")

# Step 4: Add axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# Step 5: Add annotation (loss stabilizes around epoch 7)
fig.add_annotation(
    x=7, y=0.34,
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2
)

# Step 6: Show chart
fig.show()
# Observation: Training loss decreases steadily across epochs.
# Observation: Loss stabilizes around epoch 7, indicating convergence.