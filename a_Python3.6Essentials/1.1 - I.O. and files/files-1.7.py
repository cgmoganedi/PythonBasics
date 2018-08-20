import zipfile
my_zip = zipfile.ZipFile('file1.zip', 'a')
data_in = my_zip.read('data1.txt')
my_zip.write('data2.txt', 'data_out')
my_zip.close()
