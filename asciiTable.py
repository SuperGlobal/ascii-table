# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
 
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

def main():

    for i in range(32):
        line = ""
        for j in range(i, i + 96 + 1, 32):
            if j >= 0 and j <= 31:
                line = line + str(j) + " \t| " + " \t| " + decimalToHex(j) + " \t| "
            if j >= 32 and j <= 126:
                line = line + str(j) + " \t| " + chr(j) + " \t| " + decimalToHex(j) + " \t| "
            if j == 127:
                line = line + str(j) + " \t| " + chr(j) + " \t| " + decimalToHex(j) + " \t| "
        print(line)

main()
