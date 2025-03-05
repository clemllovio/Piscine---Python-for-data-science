def give_bmi(height: list[int | float],  weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of height and weight values.
    """
    if len(height) != len(weight):
        raise ValueError("Length of height and weight must be the same")
    res = [w / (h ** 2) for h, w in zip(height, weight) if type(h)
           in [int, float] and type(w) in [int, float] and h > 0 and w > 0]
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if the BMI is above a certain limit.
    """
    return [value > limit for value in bmi]
