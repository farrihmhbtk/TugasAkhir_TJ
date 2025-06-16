import os
import pandas as pd
import shutil

# Get the directory where the script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Loop through all files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):  # Check if it's a CSV file
        file_path = os.path.join(folder_path, file)
        try:
            df = pd.read_csv(file_path)  # Read CSV
            row_count = len(df)  # Count rows excluding header

            # Generate new filename by adding row count
            file_name, file_ext = os.path.splitext(file)  # Split name and extension
            new_file_name = f"{file_name} ({row_count}){file_ext}"
            new_file_path = os.path.join(folder_path, new_file_name)

            # Copy and rename the file
            shutil.copy(file_path, new_file_path)

            print(f"Duplicated: {file} -> {new_file_name}")

        except Exception as e:
            print(f"Error processing {file}: {e}")