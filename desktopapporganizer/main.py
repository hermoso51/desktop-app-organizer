import os
import shutil


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

categories = {
    "Image" : [".png",".jpg",".jpeg",".gif"],
    "Documents" : [".pdf", ".docx", ".txt"],
    "Executables" : [".exe", ".msi", ".bat"],
    "Shortcuts" : [".lnk", ",url"]
}
for folder in categories:
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path,file)
    if os.path.isfile(file_path):
         _, ext = os.path.splitext(file)
         for folder, extensions in categories.items():
             if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(desktop_path, folder, file))
                break
