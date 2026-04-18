import os
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# FIX PATH (VERY IMPORTANT)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILE_PATH = os.path.join(DATA_DIR, "poll_data.csv")

# -----------------------------
# GENERATE DATA
# -----------------------------
np.random.seed(42)

n = 500

age_groups = ["18-24", "25-34", "35-44", "45-60"]
genders = ["Male", "Female", "Other"]
tools = ["Python", "Excel", "R", "Power BI", "SQL"]
regions = ["North", "South", "East", "West", "Central"]

feedback = [
    "Very useful tool",
    "Needs improvement",
    "Loved it",
    "Too complex",
    "Excellent experience",
    "Average",
    "Highly recommended",
    "Could be better"
]

start = datetime(2024, 1, 1)

data = []

for i in range(n):
    data.append({
        "ID": i + 1,
        "Timestamp": start + timedelta(days=random.randint(0, 120)),
        "Age_Group": random.choice(age_groups),
        "Gender": random.choice(genders),
        "Region": random.choice(regions),
        "Preferred_Tool": random.choice(tools),
        "Satisfaction": random.randint(1, 5),
        "Feedback": random.choice(feedback)
    })

df = pd.DataFrame(data)

# -----------------------------
# SAVE FILE (FORCE CHECK)
# -----------------------------
df.to_csv(FILE_PATH, index=False)

print("✅ Dataset created successfully at:")
print(FILE_PATH)
print("Rows:", len(df))