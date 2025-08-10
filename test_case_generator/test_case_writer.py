import pandas as pd
import os

def write_test_cases(test_cases, output_path="output/test_cases.csv"):
    """
    Writes the generated test cases to a CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(test_cases, columns=["ID", "Action", "Input", "Expected Output"])
    df.to_csv(output_path, index=False)
    print(f"✅ Test cases saved to {output_path}")
