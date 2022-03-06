alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")
    try_again1 = input("\ndo you want to try again?[Y] or [N]\n")
    if try_again1 == "n":
        try_again = False


import art

print(art.logo)

try_again = True
start = True
answer = input("do you want to start? [Y] or [N]\n")
if answer == "y":
    start = True
else:
    start = False
while start == True and try_again == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 52:
        shift -= 52
    elif shift > 26:
        shift -= 26

    # Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
