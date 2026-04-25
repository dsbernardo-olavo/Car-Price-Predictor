<p align="center">
  <img width="4400" height="676" alt="visual (1)" src="https://github.com/user-attachments/assets/40c0f4bc-9c72-4db8-9e37-7c18f227fba4" />
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

_The correlation table indicates that:_ Year plays a major role in determining car prices, followed by engine size, number of owners, and number of doors. Mileage shows a negative correlation, meaning that the higher the mileage, the lower the car’s price tends to be. The heatmap below shows the impact of each numerical category.

<p align="center">
<img width="612" height="442" alt="image" src="https://github.com/user-attachments/assets/e944cfd2-c742-4dca-8c10-3538250415f0" />
</p>

📈 **Boxplot chart of the target variable (price)**
<p align="center">
<img width="652" height="432" alt="image" src="https://github.com/user-attachments/assets/df698a3a-2e9d-4199-8708-0e4921f649ed" />
</p>

_The boxplot chart indicates that:_

- The first quartile is priced below approximately $6,500
- The second quartile (Median) shows that the cars are priced around $9,000
- The third quartile shows that 75% are priced below approximately $11,000
- The fourth quartile shows that the outliers are priced above $18,000

🧼 **Data cleaning**

Since the number of doors included the trunk in the count, cars with three doors were classified as **two‑door cars**, and cars with five doors were classified as **four‑door cars**.

🔮 **Prediction**
<p align="center">
<img width="281" height="67" alt="image" src="https://github.com/user-attachments/assets/f33f56dd-11d6-47c5-906e-cb88ad9f4244" />
</p>

The model shows very **strong performance**. The Root Mean Squared Error (RMSE) is about **64.93**, meaning that on average, the predictions deviate from the actual car prices by around $65. Most importantly, the R² score is 0.9995, indicating that the model explains more than **99.95%** of the variance in car prices.

🏭 **Residuals visualization**
<p align="center">
<img width="867" height="540" alt="image" src="https://github.com/user-attachments/assets/9ae00e99-93a3-410b-aa4b-b09f9b2bf160" />
</p>
<p align ="center">
<img width="598" height="452" alt="image" src="https://github.com/user-attachments/assets/289f0a90-dcd1-43ff-a921-f81eaf44625d" />
</p>

The first plot confirms that errors are generally small and randomly distributed, with only a few outliers at lower price ranges. Complementing this, the second plot shows that most predictions fall very close to the diagonal reference line, highlighting the model’s **strong fit** and **high explanatory power**. Together, these charts demonstrate both the accuracy of the predictions and the reliability of the error distribution.

👨‍💻 **Overall development:**

- **Model:** Linear regression
- **Data split:** Training (80%)/ Test (20%)
- **Preprocessing:** One-hot encoding for categorical variables (brand, model, transmission and fuel type) and standardization for numerical variables
- **Pipeline:** Integrated preprocessing and regression steps using _scikit-learn's pipeline_ in order to ensure reproductibility, prevent data leakage and keep a clean workflow.

📲 **App integration:**

This project includes an **interactive Streamlit app** that allows users to input car features and instantly receive a predicted price. The app integrates the trained pipeline (preprocessing + linear regression) and provides a user‑friendly interface for testing the model.

👉 https://car-price-predictor-dsbernardo.streamlit.app/ 

🛠️ **Tools used to build the project:**

- Kaggle
- Python
- https://share.streamlit.io/

📬 **Feel free to connect or discuss this project:**

🔗 **LinkedIn:** https://www.linkedin.com/in/ds-bernardo-olavo/  
📧 **Email:** dsbernardo.olavo@gmail.com


