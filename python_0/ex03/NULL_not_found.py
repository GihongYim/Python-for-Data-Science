def NULL_not_found(object: any) -> int:
    # your code here
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and object != float('NaN'):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {object} {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
    return 1
