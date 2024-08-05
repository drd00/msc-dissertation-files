# Fairness metrics for use-case
The use of this selection of fairness metrics is based upon an example provided with AIF360 on a Medical Expenditure dataset. This repository details some fairness metrics which can be used together to determine whether there is bias.

The tutorial can be found here: https://github.com/Trusted-AI/AIF360/blob/main/examples/tutorial_medical_expenditure.ipynb. It describes that: "Bias detection is demonstrated using several metrics, including disparate impact, average odds difference, statistical parity difference, equality opportunity difference and Theil index.

# Running the code
The Python code in this folder uses scikit-learn.

To run the code, first install the necessary dependencies by navigating to the `@/bias-tests/` folder, and then entering `pip install -r requirements.txt` (optionally activating a Python virtual environment first, with `python3 -m venv @/venv` or similar, and then activating the virtual environment), where `@` indicates the project root directory. Then run `python3 @/bias-tests/adult-dataset/bias-test-adult-dataset.py` or `python3 @/bias-tests/adult-dataset/bias-test-adult-model.py`.

