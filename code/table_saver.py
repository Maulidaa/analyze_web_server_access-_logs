import pandas as pd
import os


def save_to_table(data, file_path):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save data to CSV
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Table has been saved to {file_path}")
