# Task 3 - Linear Regression (Housing Price Prediction)

## 🎯 Objective
Build a linear regression model to predict house prices based on area.

## 🛠 Tools Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## 🧾 Dataset
- Dataset: `housing.csv`
- Source: [Kaggle](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)

## 📚 Steps Performed
1. Loaded dataset using Pandas
2. Checked for missing values
3. Selected feature (`area`) and target (`price`)
4. Split dataset into training and testing sets
5. Trained Linear Regression model using `sklearn`
6. Evaluated using:
   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - R² Score
7. Plotted regression line vs actual data
8. Printed model coefficients

## 🧠 Sample Output
```text
MAE: 15286.12
MSE: 326719090.4
R² Score: 0.928
Intercept: 16500.4
Slope: 135.8
