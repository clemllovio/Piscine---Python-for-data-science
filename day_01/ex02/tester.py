from load_image import ft_load

try:
    print(ft_load(""))
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
