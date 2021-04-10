import os

root_folder = "my_project"
folders = ["settings", "mainapp", "adminapp", "authapp"]

for directory in folders:
    path = os.path.join(root_folder, directory)
    os.makedirs(path, exist_ok=True)