import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("datasets/dos_sample.csv")

# Encode categorical variables
le = LabelEncoder()
df['protocol_type'] = le.fit_transform(df['protocol_type'])
df['flag'] = le.fit_transform(df['flag'])
df['attack'] = le.fit_transform(df['attack'])  # dos = 1, normal = 0

# Split features and labels
X = df.drop("attack", axis=1)
y = df["attack"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open("models/dos_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to models/dos_model.pkl")
