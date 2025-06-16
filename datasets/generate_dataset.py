import pandas as pd
import numpy as np

# Sample synthetic DoS dataset
data = {
    'duration': np.random.randint(0, 10, 100),
    'protocol_type': np.random.choice(['tcp', 'udp', 'icmp'], 100),
    'src_bytes': np.random.randint(0, 1000, 100),
    'dst_bytes': np.random.randint(0, 1000, 100),
    'flag': np.random.choice(['SF', 'S0', 'REJ'], 100),
    'attack': np.random.choice(['normal', 'dos'], 100)
}

df = pd.DataFrame(data)
df.to_csv('datasets/dos_sample.csv', index=False)

print("✅ Dataset generated and saved to datasets/dos_sample.csv")
