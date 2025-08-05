# runSysLogs.py
# Detect Atypical Host Access Activity such as host hopping (lateral movements)

import pandas as pd

# Load CSV
df = pd.read_csv("./1337CorpSysLogs.csv")

# Convert Unix timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='s')
host_diversity = df.groupby("User")["Host Name"].nunique().sort_values(ascending=False)

# Print Top 10 users with most host diversity
print("\n Top Users by Unique Hosts Accessed (Host Hopping):")
print(host_diversity.head(30))

print("Conclusion: Every User has access to every Host.")

print("\nrun fin.")

