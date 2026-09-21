import os
import shutil

# Folder where your .jpg files are currently present
source_folder = "source_images"

# Folder where you want to move the .jpg files
destination_folder = "jpg_files"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created folder: {destination_folder}")

# Check if source folder exists
if not os.path.exists(source_folder):
    print(f"Error: '{source_folder}' folder not found.")
    print("Please create a folder named 'source_images' and put some .jpg files in it.")
else:
    files = os.listdir(source_folder)
    moved_count = 0

    for file in files:
        # Check if file is .jpg or .jpeg
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"\nSuccessfully moved {moved_count} .jpg file(s) to '{destination_folder}' folder.")