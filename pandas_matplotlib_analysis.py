import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

print("✅ Script started")

# 1. Load dataset
iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

print("✅ Dataset loaded successfully")
print(df.head())

# 2. Data exploration
print("\nData info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())

# 3. Basic analysis
print("\nAverage measurements by species:")
print(df.groupby("species").mean())

# 4. Visualizations
# Histogram
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("histograms.png")
plt.close()
print("📊 Saved histograms.png")

# Scatter plot
df.plot(kind="scatter", x="sepal length (cm)", y="petal length (cm)", c="target", colormap="viridis")
plt.savefig("scatter.png")
plt.close()
print("📊 Saved scatter.png")

# Boxplot
df.boxplot(column="sepal length (cm)", by="species", figsize=(8, 6))
plt.title("Sepal Length by Species")
plt.suptitle("")
plt.savefig("boxplot.png")
plt.close()
print("📊 Saved boxplot.png")

print("\n✅ Analysis complete. Check your folder for PNG files.")
