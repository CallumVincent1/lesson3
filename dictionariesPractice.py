my_dict = {"name" : "callum",
           "age" : 18,
           "is_student" : True,
           "sleep late" : False,
            "descriptive_message" : "callum is a student that likes gaming"}
#print(my_dict)


car = { "car_make" : "toyota",
        "car_model" : "corolla"}

print(car)
make = car["car_make"]
print(make)
car["year"] = 2024
print(car)
car["colour"] = "green"
print(car)
del(car["colour"])
print(car)