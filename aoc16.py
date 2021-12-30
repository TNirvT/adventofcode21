import math

def open_file(file_name):
    with open(file_name) as f:
        return f.readline().rstrip()

def hex_to_bin(hex_str: str):
    # binary = format(int(hex_str, 16), "b")
    # return "0" * ((4 - (len(binary) % 4)) % 4) + binary
    return "".join([format(int(x, 16), "04b") for x in hex_str])

def unpack(binary: str):
    ver = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)

    if type_id == 4:
        # not operator

        substring = binary[6:]
        literal_bits = ""
        while substring[0] != "0":
            literal_bits += substring[1:5]
            substring = substring[5:]
        return {
            "version": ver,
            "literal": int(literal_bits + substring[1:5], 2),
            "tail": substring[5:]
        }

    literals = []
    if binary[6] == "0":
        # operator w/ 15bits define total length

        tot_length = int(binary[7:22], 2)
        substring = binary[22:22 + tot_length]
        while True:
            subpacket = unpack(substring)
            ver += subpacket["version"]
            literals.append(subpacket["literal"])

            substring = subpacket["tail"]
            if not substring:
                tail = binary[22 + tot_length:]
                break
    
    else:   # binary[6] == "1"
        # operator w/ 11bits define total no. of subpackets

        tot_subpackets = int(binary[7:18], 2)
        substring = binary[18:]
        for _ in range(tot_subpackets):
            subpacket = unpack(substring)
            ver += subpacket["version"]
            literals.append(subpacket["literal"])
            substring = subpacket["tail"]
        tail = substring
    
    literal_ops = operator(literals, type_id)

    return {
        "version": ver,
        "literal": literal_ops,
        "tail": tail
    }

def operator(literals: list, type_id: int) -> int:
    match type_id:
        case 0:
            return sum(literals)
        case 1:
            return math.prod(literals)
        case 2:
            return min(literals)
        case 3:
            return max(literals)
        case 5:
            return int(literals[0] > literals[1])
        case 6:
            return int(literals[0] < literals[1])
        case 7:
            return int(literals[0] == literals[1])

if __name__ == "__main__":
    # hex_str = open_file("test.txt")
    hex_str = open_file("aoc16.txt")

    binary = hex_to_bin(hex_str)
    print(binary)
    unpacked = unpack(binary)
    # print(*unpacked.items(), sep="\n")
    print(f"Part one: {unpacked['version']}")
    print(f"Part two: {unpacked['literal']}")
