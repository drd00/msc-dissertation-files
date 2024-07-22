from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np

adult = fetch_openml(name='adult', version=2, as_frame=True)
df = adult.data
df['income'] = adult.target

protected_attribute = 'sex'
outcome = 'income'

# Overall positive outcome rate
overall_positive_rate = (df[outcome] == '>50K').mean()

# Positive outcome rate for each group
male_positive_rate = df[df[protected_attribute] == 'Male'][outcome].value_counts(normalize=True)['>50K']
female_positive_rate = df[df[protected_attribute] == 'Female'][outcome].value_counts(normalize=True)['>50K']

# Bias metrics
# Disparate impact metric
disparate_impact = female_positive_rate / male_positive_rate

# Statistical parity difference
statistical_parity_difference = male_positive_rate - female_positive_rate

# Demographic parity ratio
demographic_parity_ratio = min(male_positive_rate, female_positive_rate) / max(male_positive_rate, female_positive_rate)

# Theil index
def theil_index(df, protected_attribute, outcome):
    groups = df.groupby(protected_attribute)
    total_count = len(df)
    total_positive = (df[outcome] == '>50K').sum()

    theil = 0
    for _, group in groups:
        group_count = len(group)
        group_positive = (group[outcome] == '>50K').sum()
        group_share = group_count / total_count
        group_outcome_rate = group_positive / group_count
        overall_outcome_rate = total_positive / total_count

        if group_outcome_rate > 0:
            theil += group_share * (group_outcome_rate / overall_outcome_rate) * np.log(group_outcome_rate / overall_outcome_rate)
        
    return theil

theil = theil_index(df, protected_attribute, outcome)

print(f"Overall positive outcome rate: {overall_positive_rate:.4f}")
print(f"Male positive outcome rate: {male_positive_rate:.4f}")
print(f"Female positive outcome rate: {female_positive_rate:.4f}")
print(f"Disparate Impact: {disparate_impact:.4f}")
print(f"Statistical Parity Difference: {statistical_parity_difference:.4f}")
print(f"Demographic Parity Ratio: {demographic_parity_ratio:.4f}")
print(f"Theil Index: {theil:.4f}")