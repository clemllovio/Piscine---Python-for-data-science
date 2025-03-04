def ft_tqdm(lst: range) -> None:
    """
     Custom implementation of a progress bar for iterating through a range.
    """
    length = len(lst)
    s = ' '
    char = "="
    for i, n in enumerate(lst):
        percentage = (i + 1) / length
        s = char * int(percentage * 75)
        print(f"\r{percentage:.0%}|{s:<75}| {i+1}/{length}", end="")
        yield i
