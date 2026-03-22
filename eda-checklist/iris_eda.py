import pandas as pd
import plotly.express as px

# Load the Iris dataset (replace with actual dataset link if provided)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Step 1: Inspect dataset structure
print("First 5 rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Step 2: Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Step 3: Analyze distribution of one feature (petal_length)
fig1 = px.histogram(df, x="petal_length", color="species", title="Distribution of Petal Length")
fig1.show()

# Step 4: Identify possible outliers
fig2 = px.box(df, x="species", y="sepal_width", title="Outliers in Sepal Width")
fig2.show()

# Step 5: Analyze relationships between variables
fig3 = px.scatter(df, x="petal_length", y="petal_width", color="species", title="Petal Length vs Petal Width")
fig3.show()

# Step 6: Insights by species
print("\nGroup by species:")
print(df.groupby("species").mean())
# Observation: Setosa species has the smallest petal length and width.
# Observation: Virginica species has the largest average petal length and width.
# Observation: Versicolor lies in between Setosa and Virginica in most features.
# Observation: Sepal width shows more variation in Setosa compared to other species.
# Observation: Petal length and petal width are strongly correlated, especially for Virginica.