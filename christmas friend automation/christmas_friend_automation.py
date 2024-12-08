import pandas as pd
import random

# Load data from Google Sheets export (CSV format)
data = pd.read_csv("Christmas Friend Trial - Form Responses 1.csv")  # Google Form responses

# Strip any extra spaces from the column names
data.columns = data.columns.str.strip()

# Shuffle participants
participants = data[['Name', 'Roll Number']].copy()
participants = participants.sample(frac=1).reset_index(drop=True)

# Assign friends (cyclic pairing)
participants['Christmas Friend'] = participants['Name'].shift(-1)
participants['Friend Roll Number'] = participants['Roll Number'].shift(-1)

# Handle last-to-first pairing
participants.iloc[-1, -2] = participants.iloc[0, 0]
participants.iloc[-1, -1] = participants.iloc[0, 1]

# Save assignments to a CSV
participants.to_csv("assignments.csv", index=False)
print("Christmas friend assignments generated!")
