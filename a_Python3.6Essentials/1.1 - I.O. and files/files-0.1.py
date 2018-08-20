import shutil
new_file_path = shutil.copy('files-0.1.py','./../filecopy.py')

# copying withe the Metadata using copy 2
new_file_path2 = shutil.copy2('files-0.2.py','./filecopy2.py')
