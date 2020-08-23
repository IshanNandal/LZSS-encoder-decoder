# Name: Ishan Nandal
# Student ID: 28278046


def elias_encoder(number):
    encoded_string_list = [bin(number)[2:]]

    while len(encoded_string_list[0]) > 1:
        encoded_string_list.insert(0, "0" + bin(len(encoded_string_list[0]) - 1)[3:])

    encoded_string = ""
    for i in range(len(encoded_string_list)):
        encoded_string += encoded_string_list[i]

    return encoded_string


def elias_decoder(codeword):
    if codeword == "1":
        return 1

    else:
        read_length = 1
        component = "0"
        pos = 0

        while component[0] != "1":
            component = "1" + component[1:]
            pos += read_length
            read_length = int(component, 2) + 1
            component = codeword[pos: pos + read_length]

        return int(component, 2)


if __name__ == "__main__":
    print(elias_encoder(70))
    print(elias_decoder(elias_encoder(70)))

"""
l1 = len(minimal_binary_code) - 1
modified_code_l1 = "0" + bin(l1)[3:]

l2 = len(modified_code_l1) - 1
modified_code_l2 = "0" + bin(l2)[3:]

l3 = len(modified_code_l2) - 1
modified_code_l3 = "0" + bin(l3)[3:]

encoded_string = modified_code_l3 + modified_code_l2 + modified_code_l1 + minimal_binary_code

print("minimal_binary_code:", minimal_binary_code)
print("l1:", l1)
print("modified_code_l1:", modified_code_l1)
print("l2:", l2)
print("modified_code_l2:", modified_code_l2)
print("l3:", l3)
print("modified_code_l3:", modified_code_l3)

print("Encoded string:", encoded_string)
"""
