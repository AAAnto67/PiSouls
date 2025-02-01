Number = 1001

for i in range(len(str(Number))):
    print(int(str(Number)[i]))

NumberDecomposed = [int(str(Number[i])) for i in range(len(str(Number)))]
print(NumberDecomposed)