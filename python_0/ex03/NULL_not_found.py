def NULL_not_found(object: any) -> int:
    # your code here
    if isinstance(object, type(None)):
        print(f"Nothing: {object} {type(None)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {float}")
    elif isinstance(object, int):
        print(f"Zero: {object} {int}")
    elif isinstance(object, str):
        print(f"Empty: {object} {str}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {bool}")
    else:
        print("Type not Found")
    return 1
