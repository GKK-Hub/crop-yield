import pandas as pd
from pathlib import Path

def combine_cleaned_files(input_dir: str, output_dir: str) -> None:
    input_path = Path(input_dir)
    files = sorted(input_path.glob("*.csv")) 

    combined_df = None

    for file in files:
        df = pd.read_csv(file)

        if combined_df is None:
            combined_df = df

        else:
            combined_df = pd.merge(combined_df, df, how="inner", on=["year", "dist_name"])
    
    output_path = Path(output_dir)
    combined_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_dir = "data\\processed_files"
    output_dir = "data\\combined_file\\combined.csv"
    combine_cleaned_files(input_dir, output_dir)