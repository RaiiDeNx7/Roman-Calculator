def StringValue(letter):
    match letter:
        case "I" | "i" :
            return "1"
        case "V" | "v":
            return "5"
        case "X" | "x":
            return "10"
        case "L" | "l" :
            return "50"
        case "C" | "c":
            return "100"
        case "D" | "d":
            return "500"
        case "M" | "m":
            return "1000"
        case "+" :
            return "+"
        case "*" :
            return "*"
        case "-" :
            return "-"
        case "/" :
            return "/"
        case " ":
            return " "


        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Error: Incorrect Input"