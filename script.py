import os
import shutil

source = input("Enter source folder path: ").strip()
filename = input("Enter file name to search: ").strip()
destination = input("Enter destination folder path: ").strip()

if not os.path.isdir(source):
    print("Source folder not found!")

else:
    os.makedirs(destination, exist_ok=True)
    found = False

    for root, dirs, files in os.walk(source):
        for file in files:
            if file.lower() == filename.lower():
                src = os.path.join(root, file)
                dst = os.path.join(destination, file)

                shutil.move(src, dst)
                print("File moved successfully:", dst)
                found = True
                break

        if found:
            break

    if not found:
        print("File not found!")
