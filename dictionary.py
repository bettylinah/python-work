my_dictionary ={
    "name":"linah",
    "gender":"female",
    "age":18,
    "marital status":"divorced",
}
print(my_dictionary)
print(my_dictionary["name"])
print(my_dictionary["marital status"])
print(my_dictionary.get("gender"))
my_dictionary["marital status"] ="married"
print(my_dictionary)
my_dictionary["age"]=24
print(my_dictionary)
my_dictionary["location"]="kisumu"
print(my_dictionary)
my_dictionary["salary"]=50000
print(my_dictionary)
my_dictionary2=my_dictionary.copy
print(my_dictionary2)
print(len(my_dictionary))
print(len(my_dictionary))
my_dictionary.pop("marital status")
print(my_dictionary)
my_dictionary.pop("name")
print(my_dictionary)
del my_dictionary["gender"]
my_dictionary.clear()
print(my_dictionary)
del my_dictionary

my_car={
    "name":"land cruiser",
    "modele":"veight",
    "year of manufacture":"2013",
    "origin":"japan",
    "color":"black",
}
print(my_car)
my_car["designer"]="jimin"
print(my_car)
my_car["origin"]="south korea"
print(my_car)
del my_car["modele"]
print(my_car)


