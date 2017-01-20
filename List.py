list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']


print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)   # Prints concatenated lists
print('~~~~~~~~~~~delete items~~~~~~~~~~~~~~~\n')
del tinylist[1]
print(tinylist)
print('\n')
word = '''basic list operations includes:
len
+
*
(item) in (list)
for item in list
'''
print(word+'\n')

list1, list2 = [123, 'abc'], [123, 123, 'xyz']
list1.append(1)
print('list1.append(1): ', list1)
print('list count: ', list2.count(123))
list1.extend(list2)
print('list extend: ', list1)
print('list index: ', list1.index('abc'))
list1.insert(1, 'def')
print('list insert: ', list1)
list1.pop(1)
print(list1.pop(1))
print('list pop: ', list1)
list1.remove(123)
print('list remove: ', list1)
word = '''pop returns the obj of what it removes
remove return nothing
pop can take 0 arg
remove must have an arg\n'''
print(word)
list1.reverse()
print('list reverse: ', list1)
print('~~when it comes to sort, the objs in list must with same type~~\n')






