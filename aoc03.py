inputs = []
gamma = ""
epsilon = ""

with open("aoc03.txt", "r") as f:
    inputs = f.readlines()

inputs = [line.rstrip() for line in inputs]
n = len(inputs)
print(f"n={n}")

for i in range(12):
    count = 0
    for bitString in inputs:
        match bitString[i]:
            case '0':
                pass
            case '1':
                count += 1
    if count > n//2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f"gamma={int(gamma, 2)}")
print(f"epsilon={int(epsilon, 2)}")
print(f"result={int(gamma, 2) * int(epsilon, 2)}")

oxygen = co2 = inputs

def elimination(data, common = True):
    index = 0
    while len(data) > 1:
        if index > 12:
            print("invalid data set")
            raise IndexError

        string0 = []
        string1 = []
        for bitString in data:
            match bitString[index]:
                case '0':
                    string0.append(bitString)
                case '1':
                    string1.append(bitString)
        if (common and len(string1) >= len(string0)) or (not common and len(string1) < len(string0)):
            data = string1
        else:
            data = string0
        
        index += 1
    return data

oxygenRating = int(elimination(inputs)[0], 2)
print(f"oxygen= {oxygenRating}")
co2Rating = int(elimination(inputs, False)[0], 2)
print(f"co2= {co2Rating}")
print(f"result= {oxygenRating*co2Rating}")
