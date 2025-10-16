import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample Dataset
data = {
    'Age': [25, 35, 45, 30, 60, 50],
    'Blood_Pressure': [120, 130, 140, 110, 150, 145],
    'Sugar_Level': [90, 110, 160, 85, 180, 170],
    'Treatment': ['Normal Diet', 'Low Sugar Diet', 'Insulin', 'Normal Diet', 'Insulin', 'Low Sugar Diet']
}

df = pd.DataFrame(data)
df.head()
