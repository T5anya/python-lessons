#DICTIONARY

#Dictionary is a collection of keys-value pairs.   
a = { 
"key": "value", 
"harry": "code", 
"marks": "100", 
"list": [1, 2, 9] 
} 
print(a["key"])  # Output: "value" 
print(a["list"])  # Output: [1, 2, 9] 
'''
1. it is unordered. 
2. It is mutable. 
3. It is indexed. 
4. Cannot contain duplicate keys. 
'''

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change #dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change #dict_keys(['brand', 'model', 'year', 'color'])


y=car.values() #
print(y) #before change #dict_values(['Ford', 'Mustang', 1964,'white'])
car["year"]=2020 #
print(y) #after change #dict_values(['Ford', 'Mustang', 2020,'white'])


z=car.items()
print(z) #([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020),('color','white')])
car["year"]=2025
print(z) #([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2025],('color','white')])

car.update({"year": 2020, "color":"red"})
print(car)#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020 , 'color':'red'}
'''
print(car.get("range")) # Prints None
print(car["range"]) # Returns an error
'''
car.pop("model")
print(car) #{'brand': 'Ford', 'year': 2020 , 'color':'red'}

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

car.popitem() #{'brand': 'Ford', 'year': 2020 }
print(car)

#The del keyword can also delete the dictionary completely:

del car
print(car) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)#{}

#NESTED DICTIONARIES

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

print(myfamily["child2"]["name"]) #Tobias