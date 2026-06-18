import pandas as pd

df = pd.read_csv("titanic.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['Age'].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['Fare'], bins=20)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Count")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()