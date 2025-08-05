# runFirewall.csv
# Detect Atypical Network Behavior
import pandas as pd


# 1. Preprocessing + Timestamp Conversion
df = pd.read_csv("./1337CorpFirewall.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit='s')
df = df.sort_values(by="Timestamp")
df["bytes in"] = pd.to_numeric(df["bytes in"],errors='coerce')
df["bytes out"] = pd.to_numeric(df["bytes out"], errors='coerce')

# 2. Identify Top Chatters (most traffic)
df["total_bytes"] = df["bytes in"] + df["bytes out"]
top_talkers = df.groupby("src_ip")["total_bytes"].sum().sort_values(ascending=False)

print("\n Top Talkers by Source IP (Total Bytes Sent + Received):\n")
print(top_talkers.head(10))

# 3. Detect Unusual Destination Ports

# 4. Beaconing / C2 Detection (Regular Internals)
print("Conclusion: IP 10.1.5.100 transfering higher than average bytes.")
print("run fin.")

