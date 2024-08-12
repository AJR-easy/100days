alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# def encrypt(txt,shft):
#     txt_length = len(txt)
#     encrypted_txt = ""
#     for char in txt:
#         ind = alphabet.index(char)
#         encrypted_char = alphabet[(ind+shft) % 26]
#         encrypted_txt += encrypted_char
#     print(f"The encoded text is {encrypted_txt}.")
#     return encrypted_txt


# def decrypt(txt,shft):
#     txt_length = len(txt)
#     decrypted_txt = ""
#     for char in txt:
#         ind = alphabet.index(char)
#         decrypted_char = alphabet[(ind - shft) % 26]
#         decrypted_txt += decrypted_char
#     print(f"The decoded text is {decrypted_txt}.")
#     return decrypted_txt


from art import logo

def caesar(txt,shft,drctn):
    txt_length = len(txt)
    new_txt = ""
    for char in txt:
        if char in alphabet:
            ind = alphabet.index(char)
            if drctn == "encode":
                new_char = alphabet[(ind+shft) % 26]
            elif drctn == "decode":
                new_char =  alphabet[(ind - shft) % 26]
            new_txt += new_char
        else:
            new_txt += char
    print(f"The encoded text is {new_txt}.")
    return new_txt


print(logo)

cont = "yes"

while cont == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text,shift,direction)
    cont = input("Do you want to continue?")
    if cont != "yes":
        print("Buh bye!")
        break

#print(decrypt(encrypt(text,shift),shift))

#print(encrypt(decrypt(text,shift),shift))

