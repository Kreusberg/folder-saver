import os
from tkinter.filedialog import askdirectory
from distutils.dir_util import copy_tree

try:
    # Choose the name of the Backup Directory
    backup_dir = input(str("Choose the name of the Backup Directory: "))

    # Gets user home path
    home_path = os.environ["USERPROFILE"]

    # join home path + backup directory
    backup_dir_path = os.path.join(home_path, backup_dir)

    # Create backup directory
    os.mkdir(backup_dir_path)

    # Asks for the directory to save
    path = askdirectory(title="Choose a folder to make backup locally in your computer")

    # Copy all their files in path and paste in backup_dir_path
    copy_tree(path, backup_dir_path)

except FileExistsError as error:
    print("For your safety, it is not possible to save files in an existing folder. Please, try again.")
