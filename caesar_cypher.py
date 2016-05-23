import pyperclip

# The string to be encrypted
message = "This is my secret message. The password is runningwater1919"

# Encryption Key
key = 13

# tells the program to encrypt or decrypt
mode = "encrypt"

# every possible symbol that can be encrypted
LETTERS = " #$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~"

# stores the encrypted/decrypted form of the message
translated = ""

# capitalize the string in message
# message = message.upper()

# run the encryption/decryption code on each symbol in the message string

for symbol in message:
    if symbol in LETTERS:
        # get the encrypted or decrypted number for this symbol
        num = LETTERS.find(symbol)  # get the number of the symbol
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        # handle the wrap-around if number is longer than the length of LETTERS
        # or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print translated message to the screen
print(translated)

# copy the translated string to the clipboard
pyperclip.copy(translated)
