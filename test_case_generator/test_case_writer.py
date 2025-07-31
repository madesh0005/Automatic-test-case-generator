import pandas as pd
import os

def write_to_csv(test_cases, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame(test_cases)
    df.to_csv(filepath, index=False)
    print(f"✅ Test cases saved to {filepath}")
