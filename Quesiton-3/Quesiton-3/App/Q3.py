def evalBinary(string):
    if string is None or len(string) == 0:
        return("Invalid")
    val1 = int(string[0])
    for i in range(1, len(string), 2):
        op = string[i]
        val2 = int(string[i + 1])
        if op == 'Z':
            val1 = val1 ^ val2
        elif op == 'Y':
            val1 = val1 | val2
        elif op == 'X':
            val1 = val1 & val2
    return val1