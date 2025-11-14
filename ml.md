# ✅ **MACHINE LEARNING PRACTICAL VIVA NOTES (Option B – Medium Detail, Consistent Length)**

---

# **ML Practical 1 — Uber Price Prediction (Regression)**

## **Aim**

To predict Uber ride fare using Linear Regression and Random Forest Regression after preprocessing and exploratory data analysis.

---

## **Concept Summary**

Uber fare depends on features such as:

* Pickup & Drop coordinates
* Distance (computed using Haversine formula)
* Passenger count
* Date/time features

We perform:

1. **Preprocessing**

   * Removing missing values
   * Converting date-time (extract hour, day, month)
   * Removing irrelevant columns
2. **Outlier detection**

   * Extreme distance values
   * Unrealistic fares
3. **Correlation analysis**

   * Heatmap to check multicollinearity
4. **Regression Models**

   * **Linear Regression**: predicts based on line equation
   * **Random Forest Regression**: ensemble of decision trees
5. **Evaluation**

   * R² score
   * RMSE (Root Mean Squared Error)

---

## **Model Comparison**

* **Linear Regression**

  * Fast
  * Works well if data is linear
* **Random Forest**

  * More accurate
  * Handles non-linearity, outliers, noise

---

## **Evaluation Metrics**

* **R² Score** – how much variance model explains
* **RMSE** – penalizes large errors
* **MAE** – average absolute error

Typically RF > LR in performance.

---

## **Viva Questions**

**Q1. Why Random Forest performs better than Linear Regression?**
Because real-world fare is non-linear and RF captures complex relationships.

**Q2. Why compute distance using Haversine instead of Euclidean?**
Because Earth is spherical; GPS coordinates require great-circle distance.

**Q3. What is multicollinearity?**
Highly correlated features → affects linear regression stability.

**Q4. Why remove outliers?**
They distort regression coefficients and reduce accuracy.

**Q5. Why split dataset into train-test?**
To evaluate model performance on unseen data.

---

---

# **ML Practical 2 — Email Spam Classification (KNN + SVM)**

## **Aim**

To classify emails as spam or not spam using KNN and SVM, and compare accuracy.

---

## **Concept Summary**

### **Dataset**

emails.csv containing text features or word frequencies.

### **Steps**

1. **Text Preprocessing**

   * If raw text → tokenization
   * If dataset already contains word counts → skip direct vectorization

2. **Train-Test Split**

3. **Vectorization**

   * Convert text into numeric vectors
   * Bag-of-Words via CountVectorizer

4. **Models Used**

   * **KNN**

     * Compares email distances
     * Sensitive to high dimensions
   * **SVM**

     * Finds best separating hyperplane
     * Works extremely well for text

---

## **Which model works better?**

* **SVM** generally beats KNN because:

  * High-dimensional data
  * Sparse vectors
  * Linear separability is good for spam classification

---

## **Evaluation Metric**

* **Accuracy**
* **Confusion Matrix** (TN, FP, FN, TP)

---

## **Viva Questions**

**Q1. Why convert text to numerical format?**
ML models work only with numbers, not raw text.

**Q2. Why SVM → better for text?**
Because high-dimensional sparse data fits well with linear kernels.

**Q3. What is hyperplane?**
A decision boundary that separates classes.

**Q4. What are drawbacks of KNN?**
Slow for large datasets, affected by irrelevant features.

**Q5. Why use train-test split?**
To measure real generalization ability.

---

---

# **ML Practical 3 — ANN for Customer Churn Prediction**

## **Aim**

To build an Artificial Neural Network to predict whether a customer will leave the bank.

---

## **Concept Summary**

### **Dataset Features**

* Age, Gender, Geography
* Credit Score
* Account balance
* Number of products
* Active member?
* Estimated salary

Target Variable: **Exited** (0 = No, 1 = Yes)

---

## **Steps**

### **1. Preprocessing**

* Remove irrelevant columns (CustomerID, Surname)
* Convert categorical → One Hot Encoding
* Normalize/Standardize input features

### **2. Train-Test Split**

### **3. ANN Architecture**

Typical network:

* Input layer (10–12 neurons)
* Hidden layers (ReLU activation)
* Output layer (sigmoid)

### **4. Training**

* Loss: Binary Crossentropy
* Optimizer: Adam
* Metrics: Accuracy

### **5. Evaluation**

* Confusion Matrix
* Accuracy
* Precision/Recall if needed

---

## **Points of Improvement**

* Increase hidden layers
* Use dropout to reduce overfitting
* Tune learning rate
* More epochs

---

## **Viva Questions**

**Q1. Why normalization is needed for ANN?**
Gradient descent converges faster when features are scaled.

**Q2. Why use sigmoid in output layer?**
Binary classification → outputs probability between 0 & 1.

**Q3. What is backpropagation?**
Algorithm to update weights using gradients.

**Q4. Why One Hot Encoding?**
Neural networks can’t handle text categories.

**Q5. What causes overfitting in ANN?**
Too many parameters, too few samples.

---

---

# **ML Practical 4 — Gradient Descent**

## **Aim**

To implement gradient descent on y = (x+3)² starting from x=2.

---

## **Concept Summary**

Gradient Descent updates:
x_new = x_old − α * derivative

For f(x) = (x+3)²
Derivative = 2(x+3)

Goal: reach minimum at x = −3

---

## **Process**

Start at x = 2
Gradually move towards −3
Learning rate controls speed

---

## **Viva Questions**

**Q1. What is gradient?**
Slope of tangent; direction of steepest ascent.

**Q2. Why subtract gradient?**
To move toward minimum.

**Q3. What if learning rate is too high?**
Overshooting → diverges.

**Q4. What if learning rate is too low?**
Very slow convergence.

**Q5. What is convex function?**
A curve with single global minimum → GD guaranteed to converge.

---

---

# **ML Practical 5 — KNN on Diabetes Dataset**

## **Aim**

To classify patients (diabetic/not) using KNN and compute accuracy, precision, recall.

---

## **Concept Summary**

Dataset contains:

* Pregnancies
* Glucose
* Blood Pressure
* BMI
* Age
* Outcome (0/1)

---

## **Steps**

1. Load dataset
2. Handle missing values
3. Normalize features (important for KNN)
4. Train-test split
5. KNN Classifier
6. Evaluation

   * Accuracy
   * Error Rate
   * Confusion Matrix
   * Precision
   * Recall

---

## **Viva Questions**

**Q1. Why normalization?**
KNN depends on distance — larger scale features dominate.

**Q2. What distance metric used?**
Euclidean usually.

**Q3. How to choose K?**
Using elbow curve on error rate.

**Q4. What is bias-variance tradeoff for K?**
Small K → high variance
Large K → high bias

**Q5. Why confusion matrix?**
To analyze false positives and false negatives.

---

---

# **ML Practical 6 — K-Means Clustering (Unsupervised)**

## **Aim**

To group customers (sales data) into clusters and determine K using elbow method.

---

## **Concept Summary**

### **K-Means Algorithm**

1. Choose K
2. Randomly initialize centroids
3. Assign data points to nearest centroid
4. Update centroids
5. Repeat until stable

---

## **Elbow Method**

Plot K vs. WCSS (Within Cluster Sum of Squares)
Look for “bend” → optimal K.

---

## **Clustering Usage**

* Customer segmentation
* Sales grouping
* Market analysis

---

## **Viva Questions**

**Q1. What is WCSS?**
Sum of squared distance of points from cluster centroid.

**Q2. Why elbow method?**
To avoid too many or too few clusters.

**Q3. Is K-Means supervised?**
No, it’s unsupervised.

**Q4. Limitation of K-Means?**
Fails on:

* Non-spherical clusters
* Different densities
* Outliers

**Q5. How initialization affects results?**
Bad centroids → poor clusters.

---

---

# **ML Practical 7 — Stock Market Trend Analysis + Simple Prediction**

## **Aim**

To analyze 20 years of Indian stock market data & predict future returns.

---

## **Concept Summary**

### **Steps**

1. Load dataset
2. Convert date column
3. Plot closing prices over years
4. Compute moving averages
5. Compute returns
6. Train simple prediction model (Linear Regression / RandomForest)

---

## **Indicators Used**

* 30-day moving average
* Yearly trend
* Volatility
* Monthly return

---

## **Why ML works here?**

Patterns exist in:

* Seasonality
* Long-term trends
* Market cycles

But stock prediction is limited due to randomness.

---

## **Viva Questions**

**Q1. Why moving average?**
To smooth fluctuations.

**Q2. Why stock prediction is hard?**
High noise, non-linearity, unpredictable events.

**Q3. Why need normalization?**
Algorithms perform better on scaled data.

**Q4. Which model works best?**
Random Forest usually better than Linear Regression.

**Q5. What features affect stock price?**
Open, High, Low, Volume, previous close.

---

---

# **ML Practical 8 — Titanic Survival Prediction**

## **Aim**

To predict survival during Titanic disaster using ML models.

---

## **Concept Summary**

### **Dataset Features**

* Pclass (1/2/3)
* Sex
* Age
* Fare
* SibSp, Parch
* Embarked
* Cabin (mostly missing)

---

## **Steps**

1. **Preprocessing**

   * Handle missing values (Age, Cabin, Embarked)
   * Convert categorical to numeric
   * Feature engineering (Title, Family size)

2. **Models Tested**

   * Logistic Regression
   * Random Forest
   * SVM
   * KNN
   * Naive Bayes

3. **Evaluation**

   * Accuracy
   * Confusion Matrix
   * ROC Curve
   * Feature Importance

Random Forest generally achieves highest accuracy.

---

## **Key Insights**

* Females survived more
* Children had higher survival rate
* 1st class passengers survived more
* Fare positively correlates with survival

---

## **Viva Questions**

**Q1. Why Titanic dataset is famous?**
Clean, balanced, and ideal for classification benchmarking.

**Q2. Why logistic regression used?**
Binary output (survived/not).

**Q3. Why random forest best?**
Captures non-linear feature interactions.

**Q4. Why one-hot encoding needed?**
Models cannot interpret text categories.

**Q5. Why check correlation?**
To avoid redundant features.
