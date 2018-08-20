import pathlib
p = pathlib.Path('./')
for child in p.iterdir():
    do_something(child)
