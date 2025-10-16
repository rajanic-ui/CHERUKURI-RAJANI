import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    'Age': [25, 35, 45, 30, 60, 50],
    'Blood_Pressure': [120, 130, 140, 110, 150, 145],
    'Sugar_Level': [90, 110, 160, 85, 180, 170],
    'Treatment': ['Normal Diet', 'Low Sugar Diet', 'Insulin', 'Normal Diet', 'Insulin', 'Low Sugar Diet']
}

df = pd.DataFrame(data)

# Features and target
X = df[['Age', 'Blood_Pressure', 'Sugar_Level']]
y = df['Treatment']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

print("---- AI-Driven Personalized Medical Suggestion ----")
age = int(input("Enter your Age: "))
bp = int(input("Enter your Blood Pressure: "))
sugar = int(input("Enter your Sugar Level: "))

prediction = model.predict([[age, bp, sugar]])
print("\nRecommended Treatment Plan:", prediction[0])
print("\n✅ AI-driven personalized medical creation completed successfully!")
