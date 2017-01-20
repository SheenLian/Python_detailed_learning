print('~~~~~~~built in method for dict~~~~')
dict = {'Name': 'Sheen',
        'Age': 27,
        'Gender': 'male'}
print(dict)
dict_clear = dict.clear()
dict = {'Name': 'Sheen',
        'Age': 27,
        'Gender': 'male'}
print('dict.clear: ', dict_clear)
dict_copy = dict.copy()
print('dict.copy: ', dict_copy)
dict_keys = ['name', 'age', 'gender']
dict2 = dict.fromkeys(dict_keys)
print('dict.keys', dict2)
print('dict.get: ', dict.get('Name'))
print('dict.items: ', dict.items())
print('dict.keys: ', dict.keys())
print('dict.values: ', dict.values())
print('dict.pop: ', dict.pop('name',False))