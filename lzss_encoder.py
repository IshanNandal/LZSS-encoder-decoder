# Name: Ishan Nandal
# Student ID: 28278046

from huffman_encoding import huffman_encoder
from elias_encoding import elias_encoder
import math


# Assumption: W and L are positive integers
def lzss_encoder(W, L, text):

    """
    --------------
        Header
    --------------
    """

    # print(huffman_encoder(text1))
    num_unique_chars = len(huffman_encoder(text))
    # print(huffman_encoder(text1)['c'])

    # ASCII code, Elias code of length of Huffman codeword, Huffman codeword
    header_data = []
    for i in huffman_encoder(text):
        huffman_code = huffman_encoder(text)[i]
        header_data.append(["0" + bin(ord(i))[2:], huffman_code, elias_encoder(len(huffman_code))])

    # print("Header format_fields:", header_data)

    header = elias_encoder(num_unique_chars)
    for i in header_data:
        header += i[0] + i[2] + i[1]

    # print("Header:", header)
    # return header

    """ 
    --------------      
         Data
    --------------
    """

    format_fields = [['1', text[0]]]
    data = ''

    i = 1
    while i < len(text):
        match_length = 0
        leftmost_index = max(i - W, 0)
        # print("Leftmost:", leftmost_index)
        j = 0

        while j < W:
            current_match_length = 0
            n = 0
            # jump_index = 0
            # print(text[i+n], text[leftmost_index+j+n], text[i+n] == text[leftmost_index + j + n])
            characters_match = text[i + n] == text[leftmost_index + j + n]

            while n < L and i + n < len(text) and leftmost_index + j < i and characters_match:

                current_match_length += 1
                n += 1
                # jump_index += 1
                if i + n < len(text):
                    characters_match = text[i + n] == text[leftmost_index + j + n]

            if current_match_length > match_length:
                match_length = current_match_length
                # print(leftmost_index, j, n, current_match_length, "\n")
                # jump_index = leftmost_index + n - current_match_length
                jump_index = j

            j += 1

        # print(i, "Match length:", match_length)

        # Format 0: Length of matched substring >= 3
        # < 0-bit, offset, length >
        if match_length >= 3:
            # print(leftmost_index, i , j)
            format_fields.append(['0', i - (leftmost_index + jump_index), match_length])

        # Format 1: Length of matched substring < 3
        # < 1-bit, char >
        else:
            format_fields.append(['1', text[i]])
            # print(format_fields)

        if match_length > 0 and i + match_length < len(text):
            i += match_length
        else:
            i += 1

    # print("format_fields:", format_fields)
    # print(len(format_fields))

    data += elias_encoder(len(format_fields))

    for i in range(len(format_fields)):
        if len(format_fields[i]) == 3:
            # print("format0", elias_encoder(format_fields[i][1]), elias_encoder(format_fields[i][2]))
            data += '0' + elias_encoder(format_fields[i][1]) + elias_encoder(format_fields[i][2])

        elif len(format_fields[i]) == 2:
            if format_fields[i][1] in huffman_encoder(text):
                huffman_code = huffman_encoder(text)[format_fields[i][1]]
                data += '1' + huffman_code
                # print("format1", huffman_code)

    # print(data)

    final_code = header + data
    # print(final_code)
    return final_code


if __name__ == "__main__":

    # lzss_encoder(6, 4, "aacaacabcaba")

    output = lzss_encoder(6, 4, "aacaacabcaba")
    print(output)

    count = 0
    while count < len(output):
        if output[count] == '1':
            break
        count += 1

    # print(count)

    int_output = int(output, 2)
    binary_output = count*'0' + bin(int_output)[2:]

    # print(int_output)
    # print(binary_output)
    # print(type(binary_output))

    bytearray1 = bytearray(output, 'utf-8')
    # print(bytearray1)

    # for e in range(math.ceil(len(output)/8)):
    # bytearray1.append()

    f1 = open('output_lzss_encoder.bin', 'wb')
    # f1.write(binary_output)
    # f1.write(int_output.to_bytes(math.ceil(len(output)/8), byteorder='little'))
    f1.write(bytearray1)
    f1.close()
