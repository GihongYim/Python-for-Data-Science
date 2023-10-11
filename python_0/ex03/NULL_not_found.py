import math

def NULL_not_found(object: any) -> int:
#your code here
    if object.__class__.__name__ == "NoneType":
        if object == None:
            print("Nothing = " + str(locals()['object']) + " " + str(type(object)))
        else:
            print("Type not Found")
            return 1
    elif object.__class__.__name__ == "float":
        if math.isnan(object) :
            print("Cheese = " + str(locals()['object']) + " " + str(type(object)))
        else:
            print("Type not Found")
            return 1
    elif object.__class__.__name__ == "int":
        if object == 0:
            print("Zero = " + str(locals()['object']) + " " + str(type(object)))
        else:
            print("Type not Found")
            return 1
    elif object.__class__.__name__ == "str":
        if object == '':
            print("Empty = " + str(locals()['object']) + " " + str(type(object)))
        else:
            print("Type not Found")
            return 1
    elif object.__class__.__name__ == "bool":
        if object == False:
            print("Fake = " + str(locals()['object']) + " " + str(type(object)))
        else:
            print("Type not Found")
            return 1
    else:
        return 1
    return 0
    