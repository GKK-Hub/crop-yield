"""
`all_process.py`

Batch processing script that reads all raw files in the `raw_files/` directory,
cleans them using functions from `common.py`, and writes the cleaned versions
to disk in the `processed_files/` directory.

- Monthly value files are averaged annually before saving.
- Other files undergo standard column cleanup and renaming.
"""

from pathlib import Path
from ..utils.common import *

# Define paths
raw_dir = Path("raw_files")
processed_dir = Path("data\\processed_files")
# processed_dir.mkdir(exist_ok=True)

# Files that need annual averaging
monthly_files = {
    "precipitation.csv",
    "minimum_temperature.csv",
    "maximum_temperature.csv",
    "actual_evapotranspiration.csv",
    "water_deficit.csv"
}

# Loop through all CSV files in the raw folder
for file_path in raw_dir.glob("*.csv"):
    print(f"Processing {file_path.name}...")

    # Read and clean
    df = read_csv(str(file_path))
    df = drop_location_id(df)
    df = update_district_names(df)
    df.columns = map_columns(df)

    # Determine whether to average or not
    if file_path.name in monthly_files:
        col_name = infer_column_name(file_path.name)
        df = annual_average(df, col_name)
    
    df = df.sort_values(['year', 'dist_name'])

    # Save output
    out_name = infer_output_name(file_path.name)
    out_path = processed_dir / out_name
    write_csv(df, str(out_path))

    print(f"Saved cleaned file to: {out_path}\n")

if __name__ == "__main__":
    print(__doc__)
