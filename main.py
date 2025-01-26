import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("boston1.csv")

# Print dataset overview
print("Dataset Overview:")
print(data.head())

# Verify column names
print("\nColumn Names:")
print(data.columns)

# Define features and target
try:
    X = data.drop(["PRICE"], axis=1)  # Replace 'MEDV' with 'PRICE'
    y = data["PRICE"]
except KeyError as e:
    print(f"Error: {e}")
    print("Please verify the column names in your dataset.")
    exit()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Plotting

# 1. Distribution of Actual vs Predicted Prices
plt.figure(figsize=(10, 6))
sns.histplot(y_test, color='blue', label='Actual', kde=True, stat="density", bins=30)
sns.histplot(y_pred, color='orange', label='Predicted', kde=True, stat="density", bins=30)
plt.title('Actual vs Predicted Prices')
plt.xlabel('Price')
plt.ylabel('Density')
plt.legend()
plt.show()

# 2. Scatter Plot of Predictions vs Actual Values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='purple')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
plt.title('Predicted vs Actual Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.grid(True)
plt.show()

# 3. Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, bins=30, color='green')
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
