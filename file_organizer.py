import os
import shutil

# directory = os.path.join(os.path.expanduser("~"), "Fort Kochi")
directory = "/Users/admin/Downloads/Fort Kochi"
extensions = {
    ".jpg": "Images",
".png":"Images",
".gif": "Images",
".mp4": "Videos",
".mov": "Videos",
".doc":"Documents",
".pdf": "Documents",
".txt":"Documents",
".mp3":"Music",
".wav": "Music"}

for filename in os.listdir(directory):
    # print(filename)
    file_path = os.path.join(directory, filename)
    # print(file_path)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        # print(extension)
        if extension in extensions:
            folder_name = extensions[extension]
            # print(folder_name)
            folder_path = os.path.join(directory, folder_name)
            # print(folder_path)
            os.makedirs(folder_path, exist_ok=True)
            destination_path = os.path.join(folder_path, filename)
            # print(destination_path)
            shutil.move(file_path, destination_path) # i think what is happening here is they are just changing the path name, because that is what is literally written in the code
            print (f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. It is a directory.")
print("File organization completed.")
            