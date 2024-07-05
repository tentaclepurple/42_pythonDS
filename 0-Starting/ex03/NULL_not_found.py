def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {obj_type}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Zero: {object} {obj_type}")
    elif isinstance(object, int) and object == 0:
        print(f"Empty: {object} {obj_type}")
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1