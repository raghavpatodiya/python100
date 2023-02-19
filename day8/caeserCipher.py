# def greet(name):   # name is the parameter & Raghav is the argument 
#     print(f"Hello {name}")
#     print(f"{name}'s World")
#     print("!")
# greet("Raghav")



# def greet2(name, age):
#     print(f"You're {name}.")
#     print(f"You're {age} years old.")
# greet2("Raghav", 20)


# def greet2(name, age):
#     print(f"You're {name}.")
#     print(f"You're {age} years old.")
# greet2(age=20, name="Raghav")


# def encrypt(plain_text, shift_amount):
#         cipher_text=""
#         for letter in plain_text:
#             position =alphabet.index(letter)
#             new_position=position+shift_amount
#             new_letter=alphabet[new_position]
#             cipher_text+=new_letter
#         print(f"The encoded text is {cipher_text}.")

# def decrypt(encoded_text, shift_amount):
#         plain_text=""
#         for letter in encoded_text:
#             position =alphabet.index(letter)
#             new_position=position-shift_amount
#             new_letter=alphabet[new_position]
#             plain_text+=new_letter
#         print(f"The decoded text is {plain_text}.")
def caeser(input_text, input_shift):
    caeser_text=""
    for char in input_text:
            if char in alphabet:
                position =alphabet.index(char)
                if direction=="encode":
                    new_position=position+input_shift
                elif direction=="decode":
                    new_position=position-input_shift
                new_letter=alphabet[new_position]
                caeser_text+=new_letter
            else:
                caeser_text +=char
    print(f"The {direction}d text is: {caeser_text}")


from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26 # shift value within range
    caeser(input_text=text, input_shift=shift)
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if result =="no":
        should_continue=False
        print("Goodbye")
# if direction=="encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
#     decrypt(encoded_text=text, shift_amount=shift)
# else:
#     print("Wrong Input")








        