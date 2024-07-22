from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

adult = fetch_openml(name='adult', version=2, as_frame=True)
X = adult.data
y = adult.target

protected_attribute = 'sex'

X = pd.get_dummies(X, drop_first=True)
y = (y == '>50K').astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=70)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

model = LogisticRegression(random_state=70)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

overall_accuracy = (y_pred == y_test).mean()

# accuracy for each group
male_mask = X_test[protected_attribute + '_Male'] == 1
female_mask = X_test[protected_attribute + '_Male'] == 0

male_accuracy = (y_pred[male_mask] == y_test[male_mask]).mean()
female_accuracy = (y_pred[female_mask] == y_test[female_mask]).mean()

# confusion matrices
male_cm = confusion_matrix(y_test[male_mask], y_pred[male_mask])
female_cm = confusion_matrix(y_test[female_mask], y_pred[female_mask])

# calculate TP and FP rates
def calculate_rates(cm):
    tn, fp, fn, tp = cm.ravel()
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)

    return tpr, fpr

male_tpr, male_fpr = calculate_rates(male_cm)
female_tpr, female_fpr = calculate_rates(female_cm)

# Bias metric calculation
statistical_parity_difference = male_accuracy - female_accuracy
equal_opportunity_difference = male_tpr - female_tpr
average_odds_difference = ((male_tpr - female_tpr) + (male_fpr - female_fpr)) / 2

print(f"Overall Accuracy: {overall_accuracy:.4f}")
print(f"Male Accuracy: {male_accuracy:.4f}")
print(f"Female Accuracy: {female_accuracy:.4f}")
print(f"Statistical Parity Difference: {statistical_parity_difference:.4f}")
print(f"Equal Opportunity Difference: {equal_opportunity_difference:.4f}")
print(f"Average Odds Difference: {average_odds_difference:.4f}")
