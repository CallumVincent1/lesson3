your_list = [12, "programming" ,27.0, 43, "lab3"]
print(len(your_list))
your_list.append(43.0)
your_list.insert(0,"first item")
your_list.remove("lab3")
len(your_list)
print(your_list[0])
your_list[1] = "programming 3"
print(type(your_list))
your_tuple = tuple(your_list)
print(type(your_tuple))
print(your_tuple[0])
print(len(your_tuple))
# your_tuple[0] = "new first item"  cant be done
second_tuple = (14,98.0, "third item")
joined_tuple = your_tuple + second_tuple
print(joined_tuple)
your_list = list(joined_tuple)
print(type(your_list))
your_set = set(your_list)
print(len(your_set))
your_set.add(74)
print(your_set)
your_set.add(98.0)
print(your_set)
another_set = {25,98, "numbers are fun"}
new_set = your_set & another_set
print(new_set)