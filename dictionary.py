my_dict = {}
my_dict = {1: 'apple', 2:'ball'}
my_dict = {'name': 'John', 1:[2,3,4]}
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get ('age'))
my_dict['age'] = 27
print (my_dict)
my_dict['adress'] = 'downtown'
print (my_dict)
print("Address :", my_dict.get('address'))
my_dict.clear()
print (my_dict)