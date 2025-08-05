import pandas as pd
from datetime import timedelta

# Parse and normalize data
df = pd.read_csv("./1337CorpADServer.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='s', errors='coerce')
df = df.sort_values(by=["User", "Timestamp"])

# Filter Only Logons
df_logons = df[df["Message"].str.contains("Logged On", case=False)].copy()


# Calculate Per-User Time Delta Between Logons
df_logons["Delta"] = df_logons.groupby("User")["Timestamp"].diff()

# Flag Fast Logins (< 1min apart)
suspicious_logons = df_logons[df_logons["Delta"] < timedelta(minutes=1)]

print("\n Users with rapid logon frequence (<1 min apart)")
print(suspicious_logons[["User", "Timestamp", "Delta"]].head(30))

print("Conclusion: User 'BCombs' is logging in abnormaly.")
print("run fin.")

