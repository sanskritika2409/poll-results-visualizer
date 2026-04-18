import os
import pandas as pd

def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base)

    path = os.path.join(project_root, "data", "poll_data.csv")

    return pd.read_csv(path)