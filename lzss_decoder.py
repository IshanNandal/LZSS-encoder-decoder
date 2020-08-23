# Name: Ishan Nandal
# Student ID: 28278046
from elias_encoding import elias_decoder


def lzss_decoder(binary_file):

    f1 = open(binary_file, 'rb')
    coded_content = f1.read()
    f1.close()

    print(coded_content)
    bits = coded_content.decode('utf-8')

    num_unique_chars = elias_decoder(bits)
    print(num_unique_chars)

    n_delete = len(bin(num_unique_chars)) - 1
    print(n_delete)
    coded_content = coded_content[n_delete:]
    print(coded_content)




if __name__ == "__main__":

    lzss_decoder('output_lzss_encoder.bin')

    output_file = open('output_lzss_decoder.txt', 'w')
    # ---- Write to file ----

    output_file.close()
