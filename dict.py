student = {
    "name": "Samanvitha",
    "age": "21",
    "city": "Hyderabad"
}
# print(student)
#print(dict_name["key"])
#print(student["name"])
#get() - Safest method to check for keys. It returns None if key is
#not present instead of KeyError
#print(student.get("place"))

#Adding new key value pair
student["place"] = "Hyd"
print(student)

#Update value
#dict_name["key"] = new_value
student["age"] = 100
print(student)