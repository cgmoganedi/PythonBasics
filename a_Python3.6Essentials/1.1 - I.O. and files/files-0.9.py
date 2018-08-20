import pathlib
p = pathlib.Path('./')
modified_time = p.stat().st_mtime
print(modified_time)
