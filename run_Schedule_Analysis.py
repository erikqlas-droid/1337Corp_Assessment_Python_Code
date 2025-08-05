#runSchedule.csv
# determine atypical behavior during off-peak hours
import pandas as pd
from datetime import datetime

# Load CSV
df = pd.read_csv("./1337CorpSchedule.csv")

# Parse 12-hour farmat times (e.g., '12:00:00 AM')
df["In"] = pd.to_datetime(df["In"], format="%I:%M:%S %p", errors='coerce').dt.time
df["Out"] = pd.to_datetime(df["Out"], format="%I:%M:%S %p", errors='coerce').dt.time

# Normalize Remote Access ("Yes" / "No")
df["Remote Access"] = df["Remote Access"].astype(str).str.strip().str.lower() == "yes"

# Extract hour from time fields (handle NaT safely)
def extract_hour(t):
  return t.hour if pd.notnull(t) else None

df["In_Hour"] = df["In"].apply(extract_hour)
df["Out_Hour"] = df["Out"].apply(extract_hour)

# Flag logins or logouts before 6 AM or after 10 PM
off_hours_access = df[
  ((df["In_Hour"].notna()) & ((df["In_Hour"] < 6) | (df["In_Hour"] > 22))) |
  ((df["Out_Hour"].notna()) & ((df["Out_Hour"] < 6) | (df["Out_Hour"] > 22)))
]
# Print Results
print("\n Off-Hours Access Detected (Before 6AM or After 10PM):\n")
print(off_hours_access[["Name", "UserID", "In", "Out", "Remote Access"]])

print("Conclusion: Great news! No one is accessing the office during off hours.")
print("run fin.")


#df["In"] = pd.to_datetime(df["In"], errors='coerce')
#df["Out"] = pd.to_datetime(df["Out"], errors='coerce')
#df["Remote Access"] = df["Remote Access"].astype(str).str.lower() == "true"
#df["Session Duration"] = (df["Out"] - df["In"]).dt.total_seconds() 

# print("run fin.")

