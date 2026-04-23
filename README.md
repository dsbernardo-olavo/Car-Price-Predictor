<p align="center">
  <img width="4400" height="676" alt="visual" src="https://github.com/user-attachments/assets/3c8df5e9-808b-4819-85c4-720673e2e780" />
</p>

📊 This project aims to develop **a solution for predicting car prices based on historical data**.

<p align="center">
  <img width="1919" height="887" alt="image" src="https://github.com/user-attachments/assets/af954bdc-c096-4b04-a003-95a3739a06f9" />
</p>
🔗 https://car-price-predictor-dsbernardo.streamlit.app/

🏁 **Initial data exploration**
<p align="center">
<img width="681" height="304" alt="image" src="https://github.com/user-attachments/assets/c13dd4e8-da16-4313-a19f-a0314712a540" />
</p>

🔀 **Correlation between numerical categories**
<p align="center">
<img width="621" height="243" alt="image" src="https://github.com/user-attachments/assets/f38d641a-e43c-4050-a9f5-3cbf58a43fc0" />
</p>
_The correlation chart shows that:_
- The first quartile (Q1) is priced below approximately $6,500
- The second quartile (Median) shows that the cars are priced around $9,000
- The third quartile (Q3) shows that 75% are priced below approximately $11,000
- The fourth quartile (Q4) shows that the outliers are priced above $18,000

📈 **Boxplot chart of the target variable (price)**
<p align="center">
<img width="652" height="432" alt="image" src="https://github.com/user-attachments/assets/df698a3a-2e9d-4199-8708-0e4921f649ed" />
</p>

📈 **Heatmap of the predictable variables**
<p align="center">
<img width="612" height="442" alt="image" src="https://github.com/user-attachments/assets/e944cfd2-c742-4dca-8c10-3538250415f0" />
</p>

🧼 **Data cleaning**

Given that the number of doors was taking the car trunk into consideration, cars with three doors were considered cars with two doors and cars with five doors were considered cars with four doors.

**Linear regression model**

**Variable definition and data splitting into training and test sets**

x = df.drop('Price', axis= 1)
y = df['Price']
x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size= 0.2, random_state= 42
)

**Definition of transformation rules**

categorical_columns = ['Brand', 'Model', 'Transmission', 'Fuel_Type']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output= False), categorical_columns)
    ],
    remainder='passthrough'
)

**Pipeline**

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor), # Aquele que você já fez
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

**Training**

pipeline.fit(x_train, y_train)

**Prediction**

y_pred = pipeline.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)

print("RMSE:", rmse)
print("MSE:", mse)
print("R²:", r2)

**Residuals visualization**

residuals = y_test - y_pred
plt.figure(figsize=(10,6))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residual Plot - Model Error Analysis')
plt.xlabel('Predicted Price')
plt.ylabel('Residuals (Errors)')
plt.show()

**Actual vs Predicted**

plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted")
plt.show()

**Estimating the price of a new car**

new_car= {
    'Brand': ['Toyota'],
    'Model': ['Corolla'],
    'Year': [2008],
    'Engine_Size': [2.0],
    'Fuel_Type': ['Diesel'],
    'Transmission': ['Manual'],
    'Mileage': [15000],
    'Doors': [2],
    'Owner_Count': [1]
}
df_new_car = pd.DataFrame(new_car)
predicted_price = pipeline.predict(df_new_car)
print(f"The estimated price for this car is: ${predicted_price[0]:.2f}")

🛠️ **Tools used to build the project:**

- Kaggle (dataset source)
- Python
- https://share.streamlit.io/ (app development)

📬 **Feel free to connect or discuss this project:**

🔗 **LinkedIn:** https://www.linkedin.com/in/ds-bernardo-olavo/  
📧 **Email:** dsbernardo.olavo@gmail.com


