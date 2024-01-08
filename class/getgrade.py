def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print(get_grade(85))

def get_grade_dict(score):
    return {
        90 <= score <= 100: "A",
        80 <= score < 90: "B",
        70 <= score < 80: "C",
        60 <= score < 70: "D",
        score < 60: "F",
    }.get(True, "Invalid score")

print(get_grade_dict(85))

def get_type(value):
    match type(value).__name__:
        case "int":
            return "Integer"
        case "float":
            return "Float"
        case "str":
            return "String"
        case "bool":
            return "Boolean"
        case "list":
            return "List"
        case "dict":
            return "Dictionary"
        case "set":
            return "Set"
        case "tuple":
            return "Tuple"

print(get_type(87))