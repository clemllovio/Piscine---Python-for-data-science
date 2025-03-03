import math

def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif obj_type is float and math.isnan(object):
        print("Cheese: nan", type(object))
        return 0
    elif obj_type is int and object == 0:
        print("Zero: 0", type(object))
        return 0
    elif obj_type is str and len(object) == 0:
        print("Empty:", type(object))
        return 0
    elif obj_type is bool and object is False:
        print("Fake: False", type(object))
        return 0
    else:
        print("Type not found")
        return 1
