import pathlib
for child in pathlib.Path('./').iterdir():
    if child.is_file():
        print(child)
