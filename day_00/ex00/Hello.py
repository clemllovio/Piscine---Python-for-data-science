ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = "World!"

# Tuple
list_tmp = list(ft_list)
list_tmp[1] = "France!"
ft_tuple = tuple(list_tmp)

# Set
ft_set.add("Lyon!")
ft_set.remove("tutu!")

# Dict
ft_dict.update({"Hello" : "42Lyon!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)