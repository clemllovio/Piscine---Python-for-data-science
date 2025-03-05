from load_image import ft_load
from pimp_image import ft_red, ft_green, ft_blue, ft_invert, ft_grey

try:
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Zoom Error: {e}")
