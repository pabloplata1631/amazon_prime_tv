import os
import kaggle

# Set up your Kaggle dataset name and destination folder
dataset_name = "shivamb/amazon-prime-movies-and-tv-shows"
destination_folder = r'C:\Users\karla\Documents\Projects\amazon_prime_tv\data\raw'

# Download the dataset using the Kaggle API
kaggle.api.dataset_download_files(dataset_name, path=destination_folder, unzip=True)

# List files in the destination folder
files_in_folder = os.listdir(destination_folder)

# Iterate over the files and remove any zip files
for file in files_in_folder:
    file_path = os.path.join(destination_folder, file)
    if file.endswith('.zip'):
        os.remove(file_path)
        print(f"Existing file '{file}' deleted.")

print("Amazon Prime TV Dataset - Download completed.")
