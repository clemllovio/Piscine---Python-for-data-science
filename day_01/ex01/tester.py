from array2D import slice_me

# Normal test
family = [[1.80, 78.4],
          [2.15, 102.7],
          [33, 36],
          [1.88, 75.2]]
try:
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
except ValueError as e:
    print(e)
