str1 = 'hello world'
str2 = str1[::-1]
translation_table = str1.maketrans('abcd', 'efgt')

print (str2.translate(translation_table))

print (str1.translate(str1.maketrans({'1':None, 'W':None})))
