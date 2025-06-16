
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open("models/dos_model.pkl", "rb") as f:
    model = pickle.load(f)

# LabelEncoder setup (same encoding as training)
protocols = ['tcp', 'udp', 'icmp']
flags = ['SF', 'S0', 'REJ']
attacks = ['normal', 'dos']

le_protocol = LabelEncoder()
le_protocol.fit(protocols)

le_flag = LabelEncoder()
le_flag.fit(flags)

# ---- Sample input (you can change these values) ----
sample = {
    'duration': 2,
    'protocol_type': 'tcp',
    'src_bytes': 5,
    'dst_bytes': 0,
    'flag': 'S0'
}

# Convert to DataFrame
df = pd.DataFrame([sample])

# Encode categorical values
df['protocol_type'] = le_protocol.transform(df['protocol_type'])
df['flag'] = le_flag.transform(df['flag'])

# Predict using the model
prediction = model.predict(df)

# Output result
if prediction[0] == 1:
    print("🚨 DoS Attack Detected!")
else:
    print("✅ Normal Traffic")
