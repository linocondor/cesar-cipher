import figures_cesar

print(figures_cesar.logo)

alphabet = figures_cesar.alphabet





repeat = False


def cesar_code(text, shift, direction):
        
    if direction == "encode":
        code = ""
        for letter in text:
            if alphabet.index(letter)+shift > len(alphabet):
                shift = shift % 26
                second = alphabet.index(letter)+shift
                code += alphabet[second]
                    
            else:
                code += alphabet[alphabet.index(letter)+shift]
                    
        print(f"The encoded text is {code}")
        return code

    elif direction == "decode":
        decode = ""
        for letter in text:
            if alphabet.index(letter)-shift <0:
                second = alphabet.index(letter)-shift + len(alphabet)
                decode += alphabet[second]
                    
            else:
                decode += alphabet[alphabet.index(letter)-shift]
                    
        print(f"The decoded text is {decode}")

while repeat == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar_code(text, shift, direction)
    repeat_y_n = input("You want to try again [y/n]:\n").lower()
    if repeat_y_n == "n":
        repeat = True
        
    
    