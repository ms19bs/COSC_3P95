def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2 
        else:
            output_str += char.upper()
    return output_str

print(processString("abcdefG1"))
print(processString("CCDDEExy"))
print(processString("1234567b"))
print(processString("8665"))
print(processString("0"))
print(processString("abc123"))
print(processString("e3eee3e4"))
print(processString(",}~|e3?/[])"))
