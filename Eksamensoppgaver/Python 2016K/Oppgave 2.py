#2a)
def load_bin(filename):
    try:
        with open(filename, 'r') as file:
           
            binary_string = ''
            for line in file:
                binary_string += line.strip()
        print(binary_string)
        return binary_string
    except:
        print("Error: Could not open file " + filename)

#2b)
def bin_to_dec(binary):
    number = 0
    for i in range(len(binary)):
        if binary[i] == '1':

            number += 2**(len(binary)-i-1)

    return number


#2c)
def dec_to_char(dec):
    alphabet = ' ,.ABCDEFGHIJKLMNOPQRSTUWXYZÆØÅ'
    if dec > 31 or dec < 0:
        return ''
    return alphabet[dec]

#2d)
def bin_to_txt(binstring):
    word = ''
    for i in range(len(binstring)//5):
        value = bin_to_dec(binstring[i*5:5*(i+1)])
        word += dec_to_char(value)

    return word
#2e)
def main():
    print("Binary-to-text converter")
    b_file = input("Name of binary file to load from: ")
    b_string = load_bin(b_file)
    txt = bin_to_txt(b_string)
    t_file = input("Name of text file to save to: ")

    try:
        with open(t_file, 'w') as file:
            file.write(txt)
        print(f"{b_file} has been converted and saved to {t_file}")

    except:
        print(f'Error: Could not write to {t_file}')

main()
