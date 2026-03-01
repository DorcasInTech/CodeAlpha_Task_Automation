import os
import shutil

# 1. Setup your folder paths
source_folder = "my_files"
destination_folder = "organized_images"

# 2. Create the destination if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 3. Loop through the files using the os library
for file_name in os.listdir(source_folder):

    # Check for .jpg, .jpeg, AND .png
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # 4. Use shutil to move the file
        shutil.move(source_path, destination_path)
        print(f"Successfully moved: {file_name}")

print("Automation Task Completed!")
