import os
import shutil
categorioes = { "Images": [".jpg",".png",".jpeg",".gif"], "Documents":[".pdf",".docx",".txt"],
                "Videos":[".mp4",".mov",".avi"] }
print()
path = input("Enter the path to organize: ")

print("----- All Files in the folder -----")
for item in os.listdir(path):
    full_path = os.path.join(path,item)

    if os.path.isfile(full_path):
        ext = os.path.splitext(item)[1].lower()
        moved =False

        for folder, extentions in categorioes.items():
            if ext in extentions:
                dest_folder =os.path.join(path,folder)
                os.makedirs(dest_folder,exist_ok=True)
                shutil.move(full_path, os.path.join(dest_folder,item))
                print(f'Moved {item} to {folder}/')
                moved =True
                break
        if not moved:
            other_folders = os.path.join(path,"others")
            os.makedirs(other_folders,exist_ok=True)
            shutil.move(full_path, os.path.join(other_folders,item))
            print(f'Moved {item} to others/')
print()
print(" ------ Summary Report -----")
summary = {
    "Images":0,
    "Documents":0,
    "Videos":0,
    "Others":0
}

for folder in summary.keys():
    folder_path = os.path.join(path,folder)
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        summary[folder] = len(files)
for cat, count in summary.items():
    print(f' - {cat}: {count} file(s)')