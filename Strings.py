str1 = 'Hello World!'
str2 = 'Python Programming'
str3 = "this is string example....wow!!!"

print('str1[0]:  ',str1[0])
print('str2[1:5]:  ', str2[1:5])
print ('~~~~~~updating strings~~~~~~~~\n')
print(str1[:6]+'Python')
print('~~~~~escape characters~~~~~~~~\n')
print(str1+'\n\t'+'newline')
print('~~~~~~special operaters~~~~~~~~\n')
print('H' in str1)
print('C:\\location')
print(r'C:\\location')
print('~~~~~~~~~~Built in method~~~~~~~~~~\n')

print ("str.capitalize() : ", str3.capitalize())
print ("str.center(40, '*') : ", str3.center(40, '*'))
sub='i'
print ("str.count('i') : ", str3.count(sub))
sub='exam'
print ("str.count('exam', 10, 40) : ", str3.count(sub,10,40))
print('~~~~~~~~ENDSWITH and Startwith~~~~~~~~~\n')
suffix='!!'
print (str3.endswith(suffix))
print (str3.endswith(suffix, 20))
print (str3.startswith( 'this' ))
suffix='exam'
print (str3.endswith(suffix))
print (str3.endswith(suffix, 0, 19))
print('~~~~~~~~~(r)Find and (r)Index~~~~~~~~~\n')
print(str3.find('x', 0, len(str3)))
print(str3.rfind('t', 0, len(str3)))
print(str3.find('x', 20, len(str3)))
print(str3.index('x', 0, len(str3)))
print(str3.rindex('t', 0, len(str3)))
print('''~~~~~~~~~~~~is family~~~~~~~~~~~~\n''')
word = '''isalnum
isalpha
isdigit
isnumeric
islower
lower
isupper
upper
istitle
title
isspace
swapcase
'''
print(word)
print('right just (rjust): ', str1.rjust(len(str1)+1, '*'))
print ('left just(ljust): ', str1.ljust(len(str1)+1, '*'))
print('trim char(lstip): ', str3.lstrip())
print('~~~~~~~~maketrans~~~~~~~~\n')
intans = 'aeiou'
outtrans = '12345'
trans = str3.maketrans(intans,outtrans)
print(str3.translate(trans))
print('~~~~~~~~Replace~~~~~~~\n')
print (str3.replace("is", "was"))
print (str3.replace("is", "was", 1))
print('~~~~~~~split and splitlines~~~~~~~~~~\n')
print(str3.split())
print(str3.split('w',1))