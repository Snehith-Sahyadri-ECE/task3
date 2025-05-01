import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
df = pd.read_csv('house_data.csv')
print("✅ Dataset loaded successfully!")
print(df.head())

# Step 2: Check for missing values
print("\n🧼 Checking for missing values:")
print(df.isnull().sum())

# Step 3: Select features and target
X = df[['area']]              # Independent variable
y = df['price']               # Dependent variable

# Step 4: Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict using the model
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation:")
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R² Score: {r2}")

# Step 8: Plot regression line
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("📈 Simple Linear Regression - Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.show()

# Step 9: Coefficients
print("\n📐 Regression Coefficients:")
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")

input("✅ Press Enter to exit...")
