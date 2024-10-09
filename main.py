alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    shifted_indices = []
    cypher_message = []
    for index in range(len(plain_text)):
        if plain_text[index] in alphabet:
            shifted_indices.append(alphabet.index(plain_text[index]) + shift_amount)
        else:
            shifted_indices.append(plain_text[index])

    for item in shifted_indices:
        if type(item) == type("string"):
            cypher_message.append(item)
        elif item > 25:
            cypher_message.append(alphabet[item % 26])  # we use the modulo operator to avoid "IndexError: list index out of range" in words like civilization
        else:
            cypher_message.append(alphabet[item])

    print(shifted_indices)
    print(cypher_message)
    print(f'The encoded text is: {"".join(cypher_message)}')

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)
