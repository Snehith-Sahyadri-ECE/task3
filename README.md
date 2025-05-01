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

Intercept: 16500.4
Slope: 135.8

✅ Dataset loaded successfully!
      price  area  bedrooms  ...  parking  prefarea furnishingstatus
0  13300000  7420         4  ...        2       yes        furnished
1  12250000  8960         4  ...        3        no        furnished
2  12250000  9960         3  ...        2       yes   semi-furnished
3  12215000  7500         4  ...        3       yes        furnished
4  11410000  7420         4  ...        2        no        furnished

[5 rows x 13 columns]

🧼 Checking for missing values:
price               0
area                0
bedrooms            0
bathrooms           0
stories             0
mainroad            0
guestroom           0
basement            0
hotwaterheating     0
airconditioning     0
parking             0
prefarea            0
furnishingstatus    0
dtype: int64

📊 Model Evaluation:
MAE: 1474748.1337969352
MSE: 3675286604768.185
R² Score: 0.27287851871974644
