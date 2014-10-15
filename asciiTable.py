# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
    if decimalValue == 0:
        hex = 0 
    while decimalValue != 0:
        hexValue = decimalValue % 16 
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
  
# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

def fileToDict(value1):
    # Dumping values in to a dictionary
    d = {}
    with open("unknown.txt") as f:
        for line in f:
           (key, val) = line.split(',')
           d[int(key)] = val
    x = d.get(value1, 'Entry Not Found')
    x = x.rstrip()
    return x

def drawTable():
    heading = '-' * 131
    headingText = "| {:<9} | {:<25} | {:<5} |".format(str('Decimal'),str('ASCII'),str('Hex'))
    headingText2 = " {:<9} | {:<5} | {:<5} |".format(str('Decimal'),str('ASCII'),str('Hex'))
    print('+', heading, '+', sep="")
    print(headingText, headingText2, headingText2, headingText2, sep="")
    print('+', heading, '+', sep="")
    # Drawing the table horizontally
    for i in range(32):
        line = ""
        for j in range(i, i + 96 + 1, 32):
            if j >= 0 and j <= 31:
                line = line + "| {:<9} | {:<25} | {:<5} |".format(str(j),fileToDict(j),decimalToHex(j))
                k = len(line)
            if j >= 32 and j <= 126:
                line = line + " {:<9} | {:<5} | {:<5} |".format(str(j),chr(j),decimalToHex(j))
            if j == 127:
                line = line + " {:<9} | {:<5} | {:<5} |".format(str(j),fileToDict(j),decimalToHex(j))
        print(line)
    print('+', heading, '+', sep="")

def main():
    drawTable()

main()
