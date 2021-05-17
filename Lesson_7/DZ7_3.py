import os
import shutil

directory_main = "my_project"
subfolders = [f.path for f in os.scandir(directory_main) if f.is_dir()]
print(subfolders)

for directory in subfolders:
    sub_sub_folders = [f.path for f in os.scandir(directory) if f.is_dir()]
    for each in sub_sub_folders:
        if each.endswith("templates"):
            sub_sub_sub_folders = [f.path for f in os.scandir(each) if f.is_dir()]
            print(sub_sub_sub_folders)
            shutil.move(*sub_sub_sub_folders, subfolders[4])