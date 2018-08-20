import zipfile
my_zip = zipfile.ZipFile('archive1.zip', mode='w')
my_zip.write('file1.txt')
my_zip.close()
