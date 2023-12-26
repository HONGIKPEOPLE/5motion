import os

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Check if it's a directory and starts with "Sentence"
        if os.path.isdir(folder_path) and folder_name.startswith("Sentence"):
            # Extract the number from the folder name
            try:
                _, number_str = folder_name.split('Sentence')
                number = int(number_str)
            except ValueError as e:
                print(f"Error extracting number from {folder_name}: {e}")
                continue

            # Create the new folder name
            new_number = number + 3000
            new_folder_name = f"S{new_number}"

            # Rename the folder
            new_folder_path = os.path.join(directory, new_folder_name)
            os.rename(folder_path, new_folder_path)
            print(f"Renamed: {folder_name} to {new_folder_name}")

if __name__ == "__main__":
    directory_path = r"E:\\TEST_PNG_WAV\\Model7_new\\Model7_portrait"
    rename_folders(directory_path)
