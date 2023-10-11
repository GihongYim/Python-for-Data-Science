def all_thing_is_obj(object: any) -> int:
    if object.__class__.__name__ == "list":
        print("List: {}".format(type(object)))
    elif object.__class__.__name__ == "tuple":
        print("Tuple: {}".format(type(object)))
    elif object.__class__.__name__ == "set":
        print("Set: {}".format(type(object)))
    elif object.__class__.__name__ == "dict":
        print("Dict: {}".format(type(object)))
    elif object.__class__.__name__ == "str":
        print("{} is in the kitchen : {} ".format(object, type(object)))
    else:
        print("Type not found")    
    return 42